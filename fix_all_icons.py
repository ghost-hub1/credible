#!/usr/bin/env python3
"""
Automated Icon Fix Script for Cloned Credible Website
This script automatically:
1. Finds all HTML files in your directory
2. Removes old broken icon code (FontAwesome, old fixes)
3. Adds the new working SVG icon solution
4. Creates backups of all modified files
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# The complete icon fix code to be added
ICON_FIX_CODE = '''<!-- ===== ICON FIX - WORKING SVG SOLUTION ===== -->
<style>
    /* Hide original broken icon elements */
    [class*="icon-"]:before,
    [class*="icon-"]:after {
        display: none !important;
    }
    
    /* SVG Icon Styling */
    .icon-svg {
        display: inline-block;
        width: 1em;
        height: 1em;
        fill: currentColor;
        vertical-align: middle;
        margin-right: 0.25em;
    }
    
    /* Specific icon sizes */
    .icon-menu .icon-svg,
    .icon-search .icon-svg { width: 20px; height: 20px; }
    
    .icon-chevron-right .icon-svg,
    .icon-chevron-left .icon-svg { width: 12px; height: 12px; }
    
    .icon-check .icon-svg { width: 16px; height: 16px; }
    .icon-close .icon-svg { width: 16px; height: 16px; }
    
    /* Make sure icons work with any background */
    .icon-svg { flex-shrink: 0; }
</style>

<script>
// SVG Icon Library - Add this right after page loads
document.addEventListener('DOMContentLoaded', function() {
    // Define all SVG icons
    const icons = {
        'menu': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>',
        'chevron-right': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>',
        'chevron-left': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>',
        'check': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>',
        'close': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>',
        'search': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>',
        'arrow-forward': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>',
        'credit-score': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg>',
        'coins': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M15 16c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0-6c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm-6 6c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0-6c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2z"/></svg>',
        'star': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>',
        'phone': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>',
        'email': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
        'home': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>',
        'person': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>',
        'calendar': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>',
        'arrow-down': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>',
        'arrow-up': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M7 14l5-5 5 5z"/></svg>',
        'info': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'warning': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg>',
        'success': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>',
        'download': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>',
        'upload': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z"/></svg>',
        'settings': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94L14.4 2.81c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>',
        'lock': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>',
        'unlock': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 17c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm6-9h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6h1.9c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm0 12H6V10h12v10z"/></svg>'
    };
    
    // Function to replace icon classes with SVG
    function replaceIcons() {
        const iconElements = document.querySelectorAll('[class*="icon-"]');
        
        iconElements.forEach(element => {
            const classes = element.className.split(' ');
            const iconClass = classes.find(cls => cls.startsWith('icon-'));
            if (!iconClass) return;
            
            const iconName = iconClass.replace('icon-', '');
            
            if (icons[iconName]) {
                if (!element.querySelector('.icon-svg')) {
                    element.insertAdjacentHTML('afterbegin', icons[iconName]);
                }
            }
        });
    }
    
    replaceIcons();
    
    // Watch for dynamically added content
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                replaceIcons();
            }
        });
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    console.log('✅ SVG Icons loaded successfully');
});
</script>
<!-- ===== END ICON FIX ===== -->
'''

# Patterns to identify and remove old icon fix attempts
PATTERNS_TO_REMOVE = [
    # FontAwesome links
    r'<link[^>]*fontawesome[^>]*>',
    r'<link[^>]*font-awesome[^>]*>',
    
    # Old CSS fix files
    r'<link[^>]*absolute-fix\.css[^>]*>',
    r'<link[^>]*icon-fix[^>]*>',
    
    # Old inline icon fix styles and comments
    r'<!-- ===== ICON FIX - DO NOT REMOVE ===== -->.*?<!-- ===== END ICON FIX ===== -->',
    
    # Old emergency inline fix
    r'<style>\s*/\*\s*Emergency inline fix\s*\*/.*?</style>',
    
    # Old menu fix script
    r'<script src=["\']js/menu-fix\.js["\']></script>',
    
    # Font status checker scripts
    r'<script>.*?font-status.*?</script>',
]


def create_backup(file_path):
    """Create a backup of the file with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(file_path).parent / "backups"
    backup_dir.mkdir(exist_ok=True)
    
    backup_path = backup_dir / f"{Path(file_path).stem}_backup_{timestamp}{Path(file_path).suffix}"
    shutil.copy2(file_path, backup_path)
    return backup_path


def remove_old_icon_code(content):
    """Remove all old icon fix attempts from HTML content"""
    cleaned_content = content
    
    # Remove each pattern (case insensitive, multiline, dotall)
    for pattern in PATTERNS_TO_REMOVE:
        cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.IGNORECASE | re.DOTALL)
    
    return cleaned_content


def add_new_icon_fix(content):
    """Add the new SVG icon fix code to the HTML"""
    # Find the <head> tag and add our code right after it
    head_pattern = r'(<head[^>]*>)'
    
    if re.search(head_pattern, content, re.IGNORECASE):
        # Add the icon fix code right after <head>
        new_content = re.sub(
            head_pattern,
            r'\1\n' + ICON_FIX_CODE,
            content,
            count=1,
            flags=re.IGNORECASE
        )
        return new_content
    else:
        print("⚠️  Warning: No <head> tag found in file")
        return content


def process_html_file(file_path):
    """Process a single HTML file"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if file already has the new fix
        if '<!-- ===== ICON FIX - WORKING SVG SOLUTION =====' in content:
            return 'ALREADY_FIXED'
        
        # Create backup
        backup_path = create_backup(file_path)
        
        # Remove old icon code
        cleaned_content = remove_old_icon_code(content)
        
        # Add new icon fix
        fixed_content = add_new_icon_fix(cleaned_content)
        
        # Write the fixed content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        return 'SUCCESS'
        
    except Exception as e:
        return f'ERROR: {str(e)}'


def find_html_files(directory):
    """Find all HTML files in the directory and subdirectories"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        # Skip backup directories
        dirs[:] = [d for d in dirs if d != 'backups']
        
        for file in files:
            if file.lower().endswith(('.html', '.htm')):
                html_files.append(os.path.join(root, file))
    
    return html_files


def main():
    """Main function to run the icon fix automation"""
    print("=" * 70)
    print("🔧 AUTOMATED ICON FIX SCRIPT FOR CLONED CREDIBLE WEBSITE")
    print("=" * 70)
    print()
    
    # Get the directory to process
    directory = input("Enter the directory path containing your HTML files\n(or press Enter for current directory): ").strip()
    
    if not directory:
        directory = os.getcwd()
    
    if not os.path.isdir(directory):
        print(f"❌ Error: Directory '{directory}' not found!")
        return
    
    print(f"\n📁 Searching for HTML files in: {directory}")
    print()
    
    # Find all HTML files
    html_files = find_html_files(directory)
    
    if not html_files:
        print("❌ No HTML files found in the specified directory!")
        return
    
    print(f"✅ Found {len(html_files)} HTML file(s)")
    print()
    
    # Show files and ask for confirmation
    print("Files to be processed:")
    for i, file in enumerate(html_files, 1):
        print(f"  {i}. {os.path.relpath(file, directory)}")
    
    print()
    confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("❌ Operation cancelled by user")
        return
    
    print()
    print("=" * 70)
    print("🚀 PROCESSING FILES...")
    print("=" * 70)
    print()
    
    # Process each file
    results = {
        'SUCCESS': [],
        'ALREADY_FIXED': [],
        'ERROR': []
    }
    
    for i, file_path in enumerate(html_files, 1):
        relative_path = os.path.relpath(file_path, directory)
        print(f"[{i}/{len(html_files)}] Processing: {relative_path}...", end=' ')
        
        result = process_html_file(file_path)
        
        if result == 'SUCCESS':
            print("✅ FIXED")
            results['SUCCESS'].append(relative_path)
        elif result == 'ALREADY_FIXED':
            print("⏭️  ALREADY FIXED")
            results['ALREADY_FIXED'].append(relative_path)
        else:
            print(f"❌ {result}")
            results['ERROR'].append((relative_path, result))
    
    # Print summary
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"✅ Successfully fixed: {len(results['SUCCESS'])} file(s)")
    print(f"⏭️  Already fixed: {len(results['ALREADY_FIXED'])} file(s)")
    print(f"❌ Errors: {len(results['ERROR'])} file(s)")
    print()
    
    if results['ERROR']:
        print("Files with errors:")
        for file, error in results['ERROR']:
            print(f"  - {file}: {error}")
        print()
    
    print("=" * 70)
    print("✅ DONE!")
    print("=" * 70)
    print()
    print("📌 IMPORTANT NOTES:")
    print("  1. Backups of all modified files are in the 'backups' folder")
    print("  2. Test your website to ensure all icons display correctly")
    print("  3. Check browser console - you should see '✅ SVG Icons loaded successfully'")
    print("  4. If something went wrong, restore from backups")
    print()
    print("🎉 Your icons should now work perfectly across all pages!")


if __name__ == "__main__":
    main()
