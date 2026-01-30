import os
import re

def add_css_to_html_files(directory):
    """Add universal icons CSS link to all HTML files in directory"""
    
    # The CSS link to add
    css_link = '\n    <!-- Universal Icons Fix -->\n    <link rel="stylesheet" href="/CREDIBLE/css/universal-icons.css">'
    
    # Count of files modified
    modified_count = 0
    
    # Walk through all directories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check if CSS already exists
                    if 'universal-icons.css' in content:
                        print(f"✓ Already has CSS: {file_path}")
                        continue
                    
                    # Find the head section and add CSS before closing head tag
                    if '</head>' in content:
                        # Add before closing head tag
                        new_content = content.replace('</head>', f'{css_link}\n</head>')
                        
                        # Write back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"✓ Updated: {file_path}")
                        modified_count += 1
                    
                    elif '<head>' in content:
                        # Add after opening head tag
                        new_content = content.replace('<head>', f'<head>{css_link}')
                        
                        # Write back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"✓ Updated: {file_path}")
                        modified_count += 1
                    
                    else:
                        # No head tag, add before body or at end of file
                        if '<body>' in content:
                            # Add before body tag
                            head_content = f'<head>{css_link}\n</head>\n'
                            new_content = content.replace('<body>', f'{head_content}<body>')
                        else:
                            # Add at beginning
                            new_content = f'<!DOCTYPE html>\n<html>\n<head>{css_link}\n</head>\n<body>\n{content}\n</body>\n</html>'
                        
                        # Write back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"✓ Updated (added head): {file_path}")
                        modified_count += 1
                        
                except Exception as e:
                    print(f"✗ Error with {file_path}: {str(e)}")
    
    print(f"\n✅ Complete! Modified {modified_count} HTML files.")
    return modified_count

if __name__ == "__main__":
    # CORRECTED PATH for Windows - use raw string or double backslashes
    credible_dir = r"C:\My Web Sites\credible"  # FIXED PATH
    
    if os.path.exists(credible_dir):
        print(f"Scanning directory: {credible_dir}")
        print("=" * 50)
        
        count = add_css_to_html_files(credible_dir)
        
        print("\n" + "=" * 50)
        print(f"✅ Successfully updated {count} HTML files with universal icon CSS.")
        print("\n📁 Make sure you have created this file:")
        print("C:\\My Web Sites\\credible\\css\\universal-icons.css")
        print("\n🔄 Clear browser cache (Ctrl+F5) after updating files.")
    else:
        print(f"❌ Directory not found: {credible_dir}")
        print("\n🔍 Available directories in C:\\My Web Sites\\:")
        try:
            if os.path.exists("C:\\My Web Sites"):
                items = os.listdir("C:\\My Web Sites")
                for item in items:
                    if os.path.isdir(os.path.join("C:\\My Web Sites", item)):
                        print(f"  📁 {item}")
        except:
            pass
        print("\n💡 Update the 'credible_dir' variable to the correct path.")
        