import os

def fix_all_html_files():
    directory = r"C:\My Web Sites\credible"
    
    # The SIMPLE fix that works
    fix_html = '''<!-- ===== ICON FIX - DO NOT REMOVE ===== -->
<link rel="stylesheet" href="/fontawesome/css/all.min.css">
<link rel="stylesheet" href="/css/absolute-fix.css">
<style>
    /* Emergency inline fix */
    [class*="icon-"]:before {
        font-family: "Font Awesome 6 Free" !important;
        font-weight: 900 !important;
    }
    .icon-menu:before { content: "\\f0c9"; }
    .icon-chevron-right:before { content: "\\f054"; }
    .icon-chevron-left:before { content: "\\f053"; }
    .icon-check:before { content: "\\f00c"; }
    .icon-close:before { content: "\\f00d"; }
    .icon-search:before { content: "\\f002"; }
    .icon-arrow-forward:before { content: "\\f061"; }
    .icon-credit-score:before { content: "\\f09d"; }
    .icon-coins:before { content: "\\f51e"; }
</style>
<!-- ===== END ICON FIX ===== -->'''
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove any previous icon fixes to avoid conflicts
                lines_to_remove = [
                    'fontawesome-override',
                    'fontawesome-fix.css',
                    'universal-icons.css',
                    'all-icons-fix.css',
                    'icon-emergency-fix.css',
                    '<!-- Universal Icons Fix -->',
                    '<!-- Local FontAwesome -->',
                    '<!-- FontAwesome CSS -->',
                    'cdnjs.cloudflare.com/ajax/libs/font-awesome',
                    '<!-- ===== ICON FIX'
                ]
                
                for line in lines_to_remove:
                    if line in content:
                        # Find and remove the entire line/block
                        lines = content.split('\n')
                        cleaned_lines = []
                        skip_next = False
                        for i, l in enumerate(lines):
                            if skip_next:
                                skip_next = False
                                continue
                            if line in l:
                                # Skip this line
                                continue
                            if '<style>' in l and 'icon-' in lines[i+1] if i+1 < len(lines) else '':
                                # Skip style blocks about icons
                                skip_next = True
                                continue
                            cleaned_lines.append(l)
                        content = '\n'.join(cleaned_lines)
                
                # Add our fix at the beginning of head
                if '<head>' in content:
                    # Insert after <head>
                    head_pos = content.find('<head>') + 6
                    new_content = content[:head_pos] + '\n' + fix_html + content[head_pos:]
                elif '</head>' in content:
                    # Insert before </head>
                    new_content = content.replace('</head>', fix_html + '\n</head>')
                else:
                    # No head? Add one
                    new_content = '<head>\n' + fix_html + '\n</head>\n' + content
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Fixed: {file_path}")

if __name__ == "__main__":
    print("🛠️  Applying the FINAL icon fix to ALL HTML files...")
    fix_all_html_files()
    print("\n🎉 DONE! Now:")
    print("1. Create /css/absolute-fix.css with the CSS above")
    print("2. Open any HTML file and refresh with Ctrl+F5")
    print("3. Icons SHOULD now work on ALL pages")
    