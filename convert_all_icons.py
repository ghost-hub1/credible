import os
import re
import json
from pathlib import Path

class IconConverter:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.icon_mapping = self.load_icon_mapping()
        self.conversion_stats = {
            'files_processed': 0,
            'icons_converted': 0,
            'icons_skipped': 0,
            'total_elements': 0
        }
    
    def load_icon_mapping(self):
        return {
            # Navigation
            'icon-menu': 'icon-menu',
            'icon-close': 'icon-close',
            'icon-search': 'icon-search',
            'icon-chevron-right': 'icon-chevron-right',
            'icon-chevron-left': 'icon-chevron-left',
            'icon-arrow-forward': 'icon-chevron-right',
            'icon-arrow-back': 'icon-chevron-left',
            'icon-arrow-right': 'icon-chevron-right',
            'icon-arrow-left': 'icon-chevron-left',
            
            # Financial (Credible Specific)
            'icon-credit-score': 'icon-credit-score',
            'icon-coins': 'icon-coins',
            'icon-loan': 'icon-loan',
            'icon-bank': 'icon-bank',
            'icon-wallet': 'icon-wallet',
            
            # Common
            'icon-user': 'icon-user',
            'icon-phone': 'icon-phone',
            'icon-email': 'icon-email',
            'icon-star': 'icon-star',
            
            # Slick Slider
            'slick-prev': 'icon-chevron-left',
            'slick-next': 'icon-chevron-right',
        }
    
    def find_icon_elements(self, content):
        patterns = [
            r'<i\s+([^>]*class="[^"]*(icon-[a-zA-Z0-9_-]+)[^"]*"[^>]*)>\s*</i>',
            r'<span\s+([^>]*class="[^"]*(icon-[a-zA-Z0-9_-]+)[^"]*"[^>]*)>\s*</span>',
            r'<div\s+([^>]*class="[^"]*(icon-[a-zA-Z0-9_-]+)[^"]*"[^>]*)>\s*</div>',
            r'<button\s+([^>]*class="[^"]*(slick-[a-zA-Z0-9_-]+)[^"]*"[^>]*)>\s*</button>',
        ]
        
        elements = []
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                elements.append({
                    'full_match': match.group(0),
                    'tag': match.group(1) if len(match.groups()) > 1 else 'i',
                    'classes': self.extract_classes(match.group(0)),
                    'start': match.start(),
                    'end': match.end()
                })
        return elements
    
    def extract_classes(self, html):
        class_match = re.search(r'class="([^"]*)"', html)
        if class_match:
            return class_match.group(1).split()
        return []
    
    def get_svg_replacement(self, icon_classes, original_html):
        svg_id = None
        for cls in icon_classes:
            if cls in self.icon_mapping:
                svg_id = self.icon_mapping[cls]
                break
        
        if not svg_id:
            placeholder_text = icon_classes[0].replace('icon-', '').replace('-', ' ').title() if icon_classes else 'icon'
            return f'<span class="icon-placeholder" title="{placeholder_text}">[{placeholder_text[0]}]</span>'
        
        non_icon_classes = [cls for cls in icon_classes if not cls.startswith('icon-') and cls != svg_id]
        all_classes = ['credible-icon', svg_id] + non_icon_classes
        
        style_match = re.search(r'style="([^"]*)"', original_html)
        style_attr = f' style="{style_match.group(1)}"' if style_match else ''
        
        other_attrs = []
        for attr in ['id', 'data-', 'aria-', 'title', 'alt']:
            if attr.endswith('-'):
                attr_match = re.search(fr'{attr}[a-zA-Z0-9_-]+="[^"]*"', original_html)
            else:
                attr_match = re.search(fr'{attr}="[^"]*"', original_html)
            if attr_match:
                other_attrs.append(attr_match.group(0))
        
        svg_html = f'''<svg class="{' '.join(all_classes)}"{style_attr} {' '.join(other_attrs)} width="24" height="24" viewBox="0 0 24 24">
    <use href="/icons/credible-icons.svg#{svg_id}"></use>
</svg>'''
        
        return svg_html
    
    def convert_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        elements = self.find_icon_elements(content)
        
        if not elements:
            return False
        
        elements.sort(key=lambda x: x['start'], reverse=True)
        
        converted_count = 0
        for element in elements:
            if '<svg' in element['full_match'] or 'credible-icons.svg' in element['full_match']:
                continue
            
            svg_replacement = self.get_svg_replacement(element['classes'], element['full_match'])
            content = content[:element['start']] + svg_replacement + content[element['end']:]
            converted_count += 1
        
        if converted_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.conversion_stats['icons_converted'] += converted_count
            self.conversion_stats['total_elements'] += len(elements)
            return True
        
        return False
    
    def add_svg_css_reference(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        css_link = '<link rel="stylesheet" href="/css/svg-icons.css">'
        
        if 'svg-icons.css' in content:
            return False
        
        if '</head>' in content:
            new_content = content.replace('</head>', f'    {css_link}\n</head>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    
    def run_conversion(self):
        print("🚀 Converting all icons to SVG...")
        print("=" * 60)
        
        html_files = list(self.project_root.rglob('*.html'))
        
        for html_file in html_files:
            try:
                if self.convert_html_file(html_file):
                    self.conversion_stats['files_processed'] += 1
                    print(f"✅ Converted: {html_file.relative_to(self.project_root)}")
                
                self.add_svg_css_reference(html_file)
                
            except Exception as e:
                print(f"❌ Error: {html_file}: {str(e)}")
        
        self.create_svg_css()
        self.generate_report()
        print("\n🎉 CONVERSION COMPLETE!")
    
    def generate_report(self):
        report = f"""
📊 CONVERSION REPORT:
{'=' * 40}
Files Processed: {self.conversion_stats['files_processed']}
Icons Converted: {self.conversion_stats['icons_converted']}
Total Elements Found: {self.conversion_stats['total_elements']}
"""
        print(report)
        
        with open('icon-conversion-report.txt', 'w', encoding='utf-8') as f:
            f.write(report)
    
    def create_svg_css(self):
        css_dir = self.project_root / 'css'
        css_dir.mkdir(exist_ok=True)
        
        css_content = '''/* SVG ICON STYLING */
.credible-icon,
[class^="icon-"],
[class*=" icon-"],
.slick-prev,
.slick-next {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  fill: currentColor;
  vertical-align: middle;
}

.credible-icon.small,
.icon-small { width: 16px; height: 16px; }
.credible-icon.medium,
.icon-medium { width: 20px; height: 20px; }
.credible-icon.large,
.icon-large { width: 32px; height: 32px; }

.icon-primary { fill: #0066cc; }
.icon-success { fill: #4CAF50; }
.icon-warning { fill: #FF9800; }
.icon-error { fill: #f44336; }

button.slick-prev,
button.slick-next {
  background: transparent;
  border: none;
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
}

button.slick-prev:hover,
button.slick-next:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.icon-placeholder {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background: #f0f0f0;
  border-radius: 4px;
  font-size: 12px;
  color: #666;
  font-weight: bold;
}
'''
        
        with open(css_dir / 'svg-icons.css', 'w') as f:
            f.write(css_content)
        
        print(f"✅ Created: {css_dir / 'svg-icons.css'}")

def main():
    project_root = r"C:\\My Web Sites\\credible"
    
    if not os.path.exists(project_root):
        print(f"❌ Directory not found: {project_root}")
        return
    
    converter = IconConverter(project_root)
    converter.run_conversion()
    
    print("\n📋 NEXT STEPS:")
    print("1. Icons have been converted to SVG")
    print("2. CSS has been added to all HTML files")
    print("3. Clear browser cache with Ctrl+F5")
    print("4. Open any HTML file to see working icons!")

if __name__ == "__main__":
    main()
