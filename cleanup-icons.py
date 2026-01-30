import os
import re

def cleanup_html_file(file_path):
    """Remove conflicting icon styles from HTML file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patterns to remove (conflicting styles)
    patterns_to_remove = [
        r'<style id="fontawesome-override">.*?</style>',
        r'<style>\s*/\* Fallback to system fonts.*?</style>',
        r'<link rel="stylesheet" href="[^"]*fontawesome-fix\.css">',
        r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/',
        r'<style>\s*/\* Local fallback in case CDN fails.*?</style>',
        r'<style>\s*/\* Immediate fix for your current icons.*?</style>',
        r'<link rel="stylesheet" href="/CREDIBLE/css/fontawesome-fix\.css">',
        r'<link rel="stylesheet" href="\./fontawesome/css/v4-shims\.min\.css">'
    ]
    
    cleaned_content = content
    for pattern in patterns_to_remove:
        cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.DOTALL)
    
    # Ensure we have the 3 essential links
    essential_css = '''<!-- Essential CSS for Icons -->
    <link rel="stylesheet" href="fontawesome/css/all.min.css">
    <link rel="stylesheet" href="css/universal-icons.css">'''
    
    # Check if already present
    if 'css/universal-icons.css' not in cleaned_content:
        # Add after opening head tag
        if '<head>' in cleaned_content:
            cleaned_content = cleaned_content.replace('<head>', f'<head>\n{essential_css}')
        elif '</head>' in cleaned_content:
            cleaned_content = cleaned_content.replace('</head>', f'{essential_css}\n</head>')
    
    # Remove empty style tags
    cleaned_content = re.sub(r'<style>\s*</style>', '', cleaned_content)
    
    # Write back if changed
    if cleaned_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        return True
    
    return False

def cleanup_all_html_files(directory):
    """Clean up all HTML files in directory"""
    
    cleaned_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    if cleanup_html_file(file_path):
                        print(f"✓ Cleaned: {file_path}")
                        cleaned_count += 1
                    else:
                        print(f"✓ Already clean: {file_path}")
                except Exception as e:
                    print(f"✗ Error cleaning {file_path}: {str(e)}")
    
    return cleaned_count

if __name__ == "__main__":
    directory = r"C:\My Web Sites\credible"
    
    if os.path.exists(directory):
        print(f"🧹 Cleaning up conflicting styles in {directory}")
        print("=" * 60)
        
        count = cleanup_all_html_files(directory)
        
        print("\n" + "=" * 60)
        print(f"✅ Successfully cleaned {count} HTML files")
        print("\n📁 Make sure you have created:")
        print("   C:\\My Web Sites\\credible\\css\\universal-icons.css")
        print("\n🔄 Clear browser cache (Ctrl+F5) and test your pages!")
    else:
        print(f"❌ Directory not found: {directory}")
