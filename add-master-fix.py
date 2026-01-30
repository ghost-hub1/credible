import os

def add_master_fix_to_all_files():
    directory = r"C:\My Web Sites\credible"
    master_css = '/css/all-icons-fix.css'
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove ALL conflicting icon styles first
                styles_to_remove = [
                    '<style>/* Fallback to system fonts',
                    '<style id="fontawesome-override">',
                    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com',
                    '<style>/* Local fallback',
                    '<style>/* Immediate fix',
                    '<link rel="stylesheet" href="/CREDIBLE/css/fontawesome-fix.css">'
                ]
                
                for style in styles_to_remove:
                    # Find and remove these style blocks
                    start = content.find(style)
                    if start != -1:
                        # Find the closing tag
                        end = content.find('</style>', start)
                        if end != -1:
                            end += 8  # Include </style>
                            content = content[:start] + content[end:]
                
                # Add our master fix
                fix_link = f'<link rel="stylesheet" href="{master_css}">'
                
                if master_css not in content:
                    # Add to head
                    if '</head>' in content:
                        content = content.replace('</head>', f'    {fix_link}\n</head>')
                    elif '<head>' in content:
                        content = content.replace('<head>', f'<head>\n    {fix_link}')
                    else:
                        # Add at beginning of file
                        content = f'<head>\n{fix_link}\n</head>\n{content}'
                
                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✓ Updated: {file_path}")

if __name__ == "__main__":
    print("🔄 Adding master icon fix to all HTML files...")
    add_master_fix_to_all_files()
    print("✅ Done! Clear browser cache (Ctrl+F5) and test ALL pages.")
    