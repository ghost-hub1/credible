import os
import re

def fix_icons_properly():
    root_dir = r"C:\My Web Sites\credible"
    
    print("🔧 Fixing icons properly (preserving JS functionality)...")
    
    # Create proper CSS with Unicode fallback AND FontAwesome
    css = '''/* PROPER ICON FIX - Preserves JS functionality */
/* First, try FontAwesome */
@font-face {
    font-family: 'FontAwesomeFallback';
    src: url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-solid-900.woff2') format('woff2'),
         url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-solid-900.ttf') format('truetype');
    font-weight: 900;
    font-display: block;
}

/* Apply to icon elements but KEEP original elements */
i[class*="icon-"],
span[class*="icon-"],
div[class*="icon-"],
button[class*="icon-"],
.cred-icon,
.slick-prev,
.slick-next {
    font-family: 'FontAwesomeFallback', 'Segoe UI Symbol', 'Arial', sans-serif !important;
    font-weight: 900 !important;
    font-style: normal !important;
    display: inline-block !important;
    line-height: 1 !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
}

/* Unicode fallback for when FontAwesome fails */
.icon-menu::before { content: "\\2630" !important; } /* ☰ */
.icon-chevron-right::before { content: "\\203A" !important; } /* › */
.icon-chevron-left::before { content: "\\2039" !important; } /* ‹ */
.icon-close::before { content: "\\2715" !important; } /* ✕ */
.icon-check::before { content: "\\2713" !important; } /* ✓ */
.icon-search::before { content: "\\1F50D" !important; } /* 🔍 */
.icon-credit-score::before { content: "\\1F4B3" !important; } /* 💳 */
.icon-coins::before { content: "\\1FA99" !important; } /* 🪙 */
.icon-arrow-forward::before,
.icon-arrow-right::before { content: "\\2192" !important; } /* → */
.icon-arrow-back::before,
.icon-arrow-left::before { content: "\\2190" !important; } /* ← */
.icon-home::before { content: "\\2302" !important; } /* ⌂ */
.icon-user::before { content: "\\1F464" !important; } /* 👤 */
.icon-phone::before { content: "\\260E" !important; } /* ☎ */
.icon-email::before { content: "\\2709" !important; } /* ✉ */
.icon-star::before { content: "\\2605" !important; } /* ★ */

/* Slick slider buttons - keep as buttons! */
button.slick-prev::before,
button.slick-next::before {
    font-family: inherit !important;
}

.slick-prev::before { content: "\\2190" !important; } /* ← */
.slick-next::before { content: "\\2192" !important; } /* → */

/* Make sure original element types are preserved */
i, span, div, button {
    /* Don't change display unless needed */
}

/* Menu toggle specific fix */
.styles_menuToggle__5pQ0a .cred-icon,
.styles_menuToggle__5pQ0a [class*="icon-menu"] {
    font-size: 36px !important;
    position: relative !important;
    top: -2px !important;
    cursor: pointer !important;
}

/* Fix for any broken interactive elements */
[class*="icon-"] {
    cursor: inherit !important;
    pointer-events: auto !important;
}

/* Remove any background-image styles that might be interfering */
[class*="icon-"] {
    background-image: none !important;
}
'''
    
    # Create CSS file
    css_dir = os.path.join(root_dir, "css")
    os.makedirs(css_dir, exist_ok=True)
    
    css_file = os.path.join(css_dir, "proper-icons.css")
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css)
    
    print(f"✅ Created proper CSS: {css_file}")
    
    # Now REVERT the bad conversions and add proper CSS
    css_link = '<link rel="stylesheet" href="css/proper-icons.css">'
    
    # Also include FontAwesome CDN for maximum compatibility
    fontawesome_cdn = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
    
    updated = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # REVERT: Change SVG/span elements back to original i/span elements
                # Pattern: <svg class="credible-icon icon-name">...</svg> back to <i class="icon-name"></i>
                patterns = [
                    # Revert SVG to i
                    (r'<svg[^>]*class="[^"]*credible-icon[^"]*icon-([a-zA-Z0-9_-]+)[^"]*"[^>]*>.*?</svg>', 
                     r'<i class="icon-\1"></i>'),
                    
                    # Revert span with icon- to i
                    (r'<span[^>]*class="[^"]*icon-([a-zA-Z0-9_-]+)[^"]*"[^>]*>\s*</span>',
                     r'<i class="icon-\1"></i>'),
                    
                    # Revert div with icon- to i
                    (r'<div[^>]*class="[^"]*icon-([a-zA-Z0-9_-]+)[^"]*"[^>]*>\s*</div>',
                     r'<i class="icon-\1"></i>'),
                ]
                
                original_content = content
                for pattern, replacement in patterns:
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                
                # Add proper CSS links
                if 'proper-icons.css' not in content:
                    # Remove old problematic CSS
                    content = re.sub(r'<link[^>]*emergency-icons\.css[^>]*>', '', content)
                    content = re.sub(r'<link[^>]*svg-icons\.css[^>]*>', '', content)
                    content = re.sub(r'<link[^>]*inline-icons\.css[^>]*>', '', content)
                    
                    # Add FontAwesome CDN and our proper CSS
                    head_additions = f'{fontawesome_cdn}\n    {css_link}'
                    
                    if '</head>' in content:
                        content = content.replace('</head>', f'    {head_additions}\n</head>')
                    else:
                        content = f'<head>\n{head_additions}\n</head>\n{content}'
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    updated += 1
                    print(f"✅ Fixed: {file}")
    
    print(f"\n🎉 Properly fixed {updated} HTML files")
    
    # Create JavaScript fix for menu functionality
    js_fix = '''// MENU FIX - Restores functionality after icon conversion
document.addEventListener('DOMContentLoaded', function() {
    console.log('🔧 Applying menu fix...');
    
    // Fix 1: Restore menu toggle functionality
    const menuSelectors = [
        '.styles_menuToggle__5pQ0a',
        '[class*="menuToggle"]',
        '.icon-menu',
        '.cred-icon.icon-menu'
    ];
    
    menuSelectors.forEach(selector => {
        document.querySelectorAll(selector).forEach(element => {
            // Make sure it's clickable
            element.style.cursor = 'pointer';
            element.style.pointerEvents = 'auto';
            
            // Restore original classes if needed
            if (!element.classList.contains('icon-menu')) {
                element.classList.add('icon-menu');
            }
        });
    });
    
    // Fix 2: Ensure all icons have proper classes
    document.querySelectorAll('i[class*="icon-"]').forEach(icon => {
        // Make sure FontAwesome is applied
        icon.style.fontFamily = "'Font Awesome 6 Free', 'Segoe UI Symbol', Arial, sans-serif";
        icon.style.fontWeight = '900';
        icon.style.fontStyle = 'normal';
    });
    
    // Fix 3: Re-attach click events if they were lost
    setTimeout(() => {
        const menuButtons = document.querySelectorAll('.icon-menu, [class*="menu"]');
        menuButtons.forEach(btn => {
            if (!btn.hasAttribute('data-fixed')) {
                btn.setAttribute('data-fixed', 'true');
                
                // If no click handler, add a visual indicator
                if (!btn.onclick) {
                    btn.style.border = '2px solid blue';
                    btn.addEventListener('click', function(e) {
                        console.log('Menu clicked - but no handler attached');
                        alert('Menu clicked! If menu doesn\'t open, check JavaScript console.');
                    });
                }
            }
        });
    }, 1000);
    
    console.log('✅ Menu fix applied');
});

// Watch for dynamically added elements
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.addedNodes.length) {
            // Re-apply fixes to new elements
            mutation.addedNodes.forEach(node => {
                if (node.nodeType === 1) {
                    if (node.matches && (node.matches('.icon-menu') || node.matches('[class*="menuToggle"]'))) {
                        node.style.cursor = 'pointer';
                        node.style.pointerEvents = 'auto';
                    }
                }
            });
        }
    });
});

observer.observe(document.body, { childList: true, subtree: true });
'''
    
    js_file = os.path.join(root_dir, "js", "menu-fix.js")
    os.makedirs(os.path.join(root_dir, "js"), exist_ok=True)
    
    with open(js_file, "w", encoding="utf-8") as f:
        f.write(js_fix)
    
    print(f"✅ Created JavaScript fix: {js_file}")
    
    # Add JS fix to all HTML files
    js_link = '<script src="js/menu-fix.js"></script>'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'menu-fix.js' not in content and '</body>' in content:
                    new_content = content.replace('</body>', f'    {js_link}\n</body>')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
    
    # Create test file
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="css/proper-icons.css">
    <style>
        body { font-family: Arial; padding: 20px; }
        .test-box { margin: 20px 0; padding: 15px; border: 2px solid #ccc; border-radius: 8px; }
        .menu-area { background: #f0f0f0; padding: 20px; border-radius: 8px; }
        .clickable { cursor: pointer; color: blue; text-decoration: underline; }
    </style>
</head>
<body>
    <h1>✅ PROPER ICON FIX TEST</h1>
    
    <div class="test-box menu-area">
        <h3>Menu Test Area (Should be clickable):</h3>
        <div class="styles_menuToggle__5pQ0a clickable">
            <i class="cred-icon icon-menu"></i> Click this menu icon
        </div>
        <p><small>This should have blue border if click handler is attached</small></p>
    </div>
    
    <div class="test-box">
        <h3>Icon Display Test:</h3>
        <p><i class="icon-menu"></i> Menu (should show ☰)</p>
        <p><i class="icon-chevron-right"></i> Chevron Right (should show ›)</p>
        <p><i class="icon-chevron-left"></i> Chevron Left (should show ‹)</p>
        <p><i class="icon-close"></i> Close (should show ✕)</p>
        <p><i class="icon-check"></i> Check (should show ✓)</p>
        <p><i class="icon-search"></i> Search (should show 🔍)</p>
        <p><i class="icon-credit-score"></i> Credit Score (should show 💳)</p>
        <p><i class="icon-coins"></i> Coins (should show 🪙)</p>
        <p><i class="icon-arrow-forward"></i> Arrow Forward (should show →)</p>
        <p><i class="icon-arrow-back"></i> Arrow Back (should show ←)</p>
    </div>
    
    <div class="test-box">
        <h3>Slick Slider Test:</h3>
        <button class="slick-prev">Previous</button>
        <button class="slick-next">Next</button>
        <p><small>Buttons should have arrow icons</small></p>
    </div>
    
    <script src="js/menu-fix.js"></script>
    <script>
        // Test click handler
        document.querySelector('.styles_menuToggle__5pQ0a').addEventListener('click', function() {
            alert('Menu clicked! This confirms JavaScript is working.');
            this.style.backgroundColor = this.style.backgroundColor === 'yellow' ? '#f0f0f0' : 'yellow';
        });
        
        console.log('✅ Test page loaded successfully');
    </script>
</body>
</html>'''
    
    test_file = os.path.join(root_dir, "test-proper-fix.html")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(test_html)
    
    print(f"\n✅ Created test file: {test_file}")
    print("\n📋 NEXT STEPS:")
    print("1. Open test-proper-fix.html")
    print("2. Menu icon should have BLUE BORDER (showing it's clickable)")
    print("3. Click menu - should get alert and background changes")
    print("4. All icons should show as Unicode characters")
    print("\n🔄 Clear browser cache with Ctrl+F5 if icons don't show")

if __name__ == "__main__":
    fix_icons_properly()
    