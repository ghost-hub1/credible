import os
import re

def nuclear_fix_html_files():
    directory = r"C:\My Web Sites\credible"
    
    # The NUCLEAR FIX - Direct Unicode injection
    fix_css = '''<style>
    /* NUCLEAR ICON FIX - Direct Unicode Injection */
    .icon-menu:before { content: "\\f0c9" !important; }
    .icon-chevron-right:before { content: "\\f054" !important; }
    .icon-chevron-left:before { content: "\\f053" !important; }
    .icon-close:before { content: "\\f00d" !important; }
    .icon-check:before { content: "\\f00c" !important; }
    .icon-search:before { content: "\\f002" !important; }
    .icon-arrow-forward:before { content: "\\f061" !important; }
    .icon-credit-score:before { content: "\\f09d" !important; }
    .icon-coins:before { content: "\\f51e" !important; }
    
    .slick-prev:before { content: "\\f060" !important; }
    .slick-next:before { content: "\\f061" !important; }
    
    /* Force font loading */
    @font-face {
        font-family: 'FA-Nuclear';
        src: url('fontawesome/webfonts/fa-solid-900.woff2') format('woff2'),
             url('fontawesome/webfonts/fa-solid-900.ttf') format('truetype');
        font-weight: 900;
    }
    
    [class*="icon-"]:before, .slick-prev:before, .slick-next:before {
        font-family: 'FA-Nuclear', sans-serif !important;
        font-weight: 900 !important;
        display: inline-block !important;
    }
    </style>'''
    
    fix_js = '''<script>
    // Nuclear fallback - inject Unicode directly
    document.addEventListener('DOMContentLoaded', function() {
        var icons = {
            'icon-menu': '\\uf0c9',
            'icon-chevron-right': '\\uf054',
            'icon-chevron-left': '\\uf053',
            'icon-check': '\\uf00c',
            'icon-close': '\\uf00d'
        };
        for (var cls in icons) {
            document.querySelectorAll('.' + cls).forEach(function(el) {
                if (!el.dataset.fixed) {
                    el.dataset.fixed = 'true';
                    el.innerHTML = '&#' + icons[cls].charCodeAt(0) + ';';
                }
            });
        }
    });
    </script>'''
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add nuclear fix before </head>
                if '</head>' in content:
                    new_content = content.replace('</head>', fix_css + '\n</head>')
                    # Add JS before </body>
                    if '</body>' in new_content:
                        new_content = new_content.replace('</body>', fix_js + '\n</body>')
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"☢️ Nuclear fix applied to: {file_path}")

if __name__ == "__main__":
    print("⚠️  APPLYING NUCLEAR ICON FIX TO ALL FILES...")
    nuclear_fix_html_files()
    print("✅ DONE! Open any HTML file - icons SHOULD now show.")
    