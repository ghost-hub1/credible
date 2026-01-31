# fix_menu_functionality.py
import os
import re

def find_and_fix_menu():
    root_dir = r"C:\My Web Sites\credible"
    
    print("🔍 Finding and fixing menu functionality...")
    print("=" * 60)
    
    # Step 1: Find all JavaScript files
    js_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.js', '.jsx')):
                js_files.append(os.path.join(root, file))
    
    # Step 2: Look for menu-related JavaScript
    menu_js_patterns = [
        r'menuToggle',
        r'\.menu',
        r'toggleMenu',
        r'openMenu',
        r'closeMenu',
        r'nav.*toggle',
        r'click.*menu',
        r'addEventListener.*menu',
        r'document\.querySelector.*menu',
        r'document\.getElementById.*menu',
        r'\.styles_menuToggle__',
        r'cred-icon.*click',
        r'icon-menu.*click'
    ]
    
    menu_js_found = []
    
    for js_file in js_files:
        try:
            with open(js_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            found_patterns = []
            for pattern in menu_js_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_patterns.append(pattern)
            
            if found_patterns:
                menu_js_found.append((js_file, found_patterns))
                print(f"\n📄 Found menu JS in: {js_file}")
                print(f"   Patterns: {', '.join(found_patterns)}")
                
                # Show relevant lines
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if any(re.search(pattern, line, re.IGNORECASE) for pattern in found_patterns[:3]):
                        if len(line.strip()) > 10:  # Skip empty lines
                            print(f"   Line {i+1}: {line.strip()[:100]}")
        
        except Exception as e:
            continue
    
    # Step 3: Create a UNIVERSAL MENU FIX
    print("\n" + "=" * 60)
    print("🔧 Creating universal menu fix...")
    
    universal_fix_js = '''// UNIVERSAL MENU FIX - Works with any menu system
(function() {
    console.log('🚀 Universal Menu Fix loading...');
    
    // Wait for page to be interactive
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMenuFix);
    } else {
        initMenuFix();
    }
    
    function initMenuFix() {
        console.log('🔧 Initializing menu fix...');
        
        // Find ALL possible menu toggle elements
        const menuSelectors = [
            // Original Credible selectors
            '.styles_menuToggle__5pQ0a',
            '.cred-icon.icon-menu',
            '.icon-menu',
            '[class*="menuToggle"]',
            '[class*="menu-toggle"]',
            
            // Common menu classes
            '.menu-toggle',
            '.nav-toggle',
            '.hamburger',
            '.hamburger-menu',
            '.mobile-menu-toggle',
            
            // Any element with menu in class near nav
            'nav [class*="menu"]',
            'header [class*="menu"]',
            '.navbar [class*="menu"]',
            
            // Button with menu icon
            'button .icon-menu',
            'button .cred-icon'
        ];
        
        // Find the menu toggle
        let menuToggle = null;
        for (const selector of menuSelectors) {
            const element = document.querySelector(selector);
            if (element && (element.offsetWidth > 0 || element.offsetHeight > 0)) {
                menuToggle = element;
                console.log(`✅ Found menu toggle: ${selector}`);
                break;
            }
        }
        
        if (!menuToggle) {
            console.log('⚠️ No menu toggle found with selectors, searching broadly...');
            // Last resort: find any clickable element with menu icon
            const allElements = document.querySelectorAll('*');
            for (const el of allElements) {
                const classes = el.className || '';
                if ((classes.includes('icon-menu') || classes.includes('cred-icon')) && 
                    (el.tagName === 'BUTTON' || el.tagName === 'DIV' || el.tagName === 'SPAN' || el.tagName === 'I')) {
                    menuToggle = el;
                    console.log('✅ Found menu toggle by icon class');
                    break;
                }
            }
        }
        
        // Find the menu to toggle (nav, aside, div with menu)
        const menuSelectorsToToggle = [
            'nav',
            'aside',
            '.menu',
            '.nav-menu',
            '.mobile-menu',
            '.navbar-menu',
            '[class*="menu"]:not([class*="menuToggle"])',
            '.styles_menu__',
            '#mobile-menu',
            '#nav-menu'
        ];
        
        let menuToToggle = null;
        for (const selector of menuSelectorsToToggle) {
            const element = document.querySelector(selector);
            if (element && (element.offsetWidth > 0 || element.offsetHeight > 0)) {
                menuToToggle = element;
                console.log(`✅ Found menu to toggle: ${selector}`);
                break;
            }
        }
        
        // If we found both, attach click handler
        if (menuToggle && menuToToggle) {
            console.log('🎯 Attaching menu click handler...');
            
            // Make sure menu is hidden by default (for mobile)
            if (window.innerWidth < 992) {
                menuToToggle.style.display = 'none';
            }
            
            // Add visual indicator
            menuToggle.style.cursor = 'pointer';
            menuToggle.style.outline = '2px solid #4CAF50';
            menuToggle.style.outlineOffset = '2px';
            menuToggle.setAttribute('title', 'Click to open menu (fixed)');
            
            // Add click handler
            menuToggle.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                console.log('🎯 Menu clicked!');
                
                // Toggle menu visibility
                if (menuToToggle.style.display === 'none' || menuToToggle.style.display === '') {
                    menuToToggle.style.display = 'block';
                    menuToToggle.style.position = 'absolute';
                    menuToToggle.style.top = '60px';
                    menuToToggle.style.left = '0';
                    menuToToggle.style.right = '0';
                    menuToToggle.style.background = 'white';
                    menuToToggle.style.zIndex = '1000';
                    menuToToggle.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
                    menuToToggle.style.padding = '20px';
                    
                    // Visual feedback
                    menuToggle.style.backgroundColor = '#4CAF50';
                    menuToggle.style.color = 'white';
                    
                    console.log('✅ Menu opened');
                } else {
                    menuToToggle.style.display = 'none';
                    menuToggle.style.backgroundColor = '';
                    menuToggle.style.color = '';
                    
                    console.log('✅ Menu closed');
                }
                
                // Also try to trigger any existing handlers
                if (typeof window.toggleMenu === 'function') {
                    window.toggleMenu();
                }
                if (typeof window.openMenu === 'function') {
                    window.openMenu();
                }
            });
            
            console.log('✅ Menu fix applied successfully!');
            
        } else {
            console.log('⚠️ Could not find complete menu setup');
            console.log(`   Toggle: ${menuToggle ? 'Found' : 'Not found'}`);
            console.log(`   Menu: ${menuToToggle ? 'Found' : 'Not found'}`);
            
            // Create a fallback menu if nothing found
            createFallbackMenu();
        }
        
        // Also fix any existing event listeners that might be broken
        fixBrokenEventListeners();
    }
    
    function createFallbackMenu() {
        console.log('🛠 Creating fallback menu...');
        
        // Check if we at least have a menu toggle
        const menuToggle = document.querySelector('.icon-menu, .cred-icon.icon-menu, .styles_menuToggle__5pQ0a');
        if (menuToggle) {
            // Create a simple menu
            const fallbackMenu = document.createElement('div');
            fallbackMenu.id = 'fallback-menu';
            fallbackMenu.innerHTML = '''
                <div style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 9999; display: none;">
                    <div style="position: absolute; top: 60px; left: 0; right: 0; background: white; padding: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                        <h3>Menu</h3>
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            <li><a href="/" style="display: block; padding: 10px; color: #333; text-decoration: none;">Home</a></li>
                            <li><a href="/personal-loan.html" style="display: block; padding: 10px; color: #333; text-decoration: none;">Personal Loans</a></li>
                            <li><a href="/student-loans.html" style="display: block; padding: 10px; color: #333; text-decoration: none;">Student Loans</a></li>
                            <li><a href="/mortgage.html" style="display: block; padding: 10px; color: #333; text-decoration: none;">Mortgage</a></li>
                            <li><button onclick="document.getElementById(\'fallback-menu\').style.display=\'none\'" style="margin-top: 20px; padding: 10px 20px; background: #f44336; color: white; border: none; border-radius: 4px; cursor: pointer;">Close</button></li>
                        </ul>
                    </div>
                </div>
            ''';
            
            document.body.appendChild(fallbackMenu);
            
            // Add click handler to toggle
            menuToggle.style.cursor = 'pointer';
            menuToggle.style.border = '2px solid blue';
            menuToggle.addEventListener('click', function() {
                const menu = document.getElementById('fallback-menu');
                menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
            });
            
            console.log('✅ Fallback menu created');
        }
    }
    
    function fixBrokenEventListeners() {
        // Try to find and fix any broken event listeners
        const elements = document.querySelectorAll('*');
        elements.forEach(el => {
            const classes = el.className || '';
            if (classes.includes('menuToggle') || classes.includes('icon-menu')) {
                // Ensure it has pointer cursor
                el.style.cursor = 'pointer';
                
                // If it has no click handler, add a basic one
                if (!el.onclick && !el.hasAttribute('data-fixed')) {
                    el.setAttribute('data-fixed', 'true');
                    el.addEventListener('click', function() {
                        console.log('Menu element clicked (fixed handler)');
                        alert('Menu clicked! If menu doesn\'t open, the original JavaScript might be broken.');
                    });
                }
            }
        });
    }
    
    // Also run on window resize (for mobile/desktop toggle)
    window.addEventListener('resize', function() {
        const menu = document.querySelector('nav, .menu, .mobile-menu');
        if (menu && window.innerWidth >= 992) {
            menu.style.display = 'block';
            menu.style.position = 'static';
        }
    });
    
    // Run again after a delay to catch dynamically loaded content
    setTimeout(initMenuFix, 1000);
    setTimeout(initMenuFix, 3000);
    
    console.log('✅ Universal Menu Fix loaded');
})();
'''
    
    # Save the universal fix
    js_dir = os.path.join(root_dir, "js")
    os.makedirs(js_dir, exist_ok=True)
    
    universal_fix_file = os.path.join(js_dir, "universal-menu-fix.js")
    with open(universal_fix_file, "w", encoding="utf-8") as f:
        f.write(universal_fix_js)
    
    print(f"✅ Created universal menu fix: {universal_fix_file}")
    
    # Step 4: Add the fix to ALL HTML files
    print("\n🔧 Adding menu fix to all HTML files...")
    
    fixed_count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add the universal menu fix
                js_link = '<script src="js/universal-menu-fix.js"></script>'
                
                if 'universal-menu-fix.js' not in content and '</body>' in content:
                    new_content = content.replace('</body>', f'    {js_link}\n</body>')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    fixed_count += 1
                    print(f"✅ Added to: {file}")
    
    print(f"\n🎉 Added menu fix to {fixed_count} HTML files")
    
    # Step 5: Create a diagnostic test page
    diagnostic_html = '''<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="css/ultimate-icons.css">
    <style>
        body { font-family: Arial; padding: 20px; }
        .test-area { 
            margin: 20px 0; 
            padding: 20px; 
            border: 3px solid #2196F3;
            border-radius: 10px;
            background: #E3F2FD;
        }
        .menu-container {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .original-menu {
            background: #FFEBEE;
            border: 2px solid #F44336;
        }
        .fixed-menu {
            background: #E8F5E9;
            border: 2px solid #4CAF50;
        }
        h1 { color: #2196F3; }
        h3 { color: #FF9800; }
        .success { color: #4CAF50; font-weight: bold; }
        .warning { color: #FF9800; }
        .error { color: #F44336; }
        button { 
            margin: 5px; 
            padding: 10px 20px; 
            background: #2196F3; 
            color: white; 
            border: none; 
            border-radius: 4px; 
            cursor: pointer; 
        }
        button:hover { background: #1976D2; }
    </style>
</head>
<body>
    <h1>🔧 MENU FUNCTIONALITY DIAGNOSTIC</h1>
    
    <div class="test-area">
        <h3>Test 1: Original Menu Structure</h3>
        <div class="menu-container original-menu">
            <p>This mimics your original menu structure:</p>
            <div class="styles_menuToggle__5pQ0a" style="cursor: pointer; padding: 10px; background: #FFCDD2; display: inline-block;">
                <i class="cred-icon icon-menu"></i> Click me (original structure)
            </div>
            <nav style="display: none; padding: 20px; background: white; margin-top: 10px; border: 1px solid #ccc;">
                <p>This is the menu that should open</p>
                <ul>
                    <li>Menu Item 1</li>
                    <li>Menu Item 2</li>
                    <li>Menu Item 3</li>
                </ul>
            </nav>
        </div>
    </div>
    
    <div class="test-area">
        <h3>Test 2: Click Test</h3>
        <p>Click these elements to test responsiveness:</p>
        <button onclick="alert('Regular button works!')">Test Regular Button</button>
        <br><br>
        <div style="display: flex; gap: 10px;">
            <div onclick="alert('Div with onclick works!')" style="padding: 10px; background: #E1BEE7; cursor: pointer;">Div with onclick</div>
            <span onclick="alert('Span with onclick works!')" style="padding: 10px; background: #C8E6C9; cursor: pointer;">Span with onclick</span>
            <i onclick="alert('Icon with onclick works!')" class="icon-menu" style="padding: 10px; background: #BBDEFB; cursor: pointer;">Icon with onclick</i>
        </div>
    </div>
    
    <div class="test-area">
        <h3>Test 3: Universal Menu Fix Status</h3>
        <div id="status">Checking menu fix status...</div>
        <button onclick="checkMenuFix()">Check Menu Fix</button>
        <button onclick="testMenuToggle()">Test Menu Toggle</button>
    </div>
    
    <div class="test-area fixed-menu">
        <h3>Instructions:</h3>
        <ol>
            <li>Click the "Check Menu Fix" button above</li>
            <li>If it finds menu elements, they will be highlighted in GREEN</li>
            <li>Click the menu icon - it should open/close the nav</li>
            <li>Check browser console (F12) for debug messages</li>
        </ol>
        <p class="warning">If menu doesn't work, the original JavaScript might be missing or broken.</p>
    </div>
    
    <script src="js/universal-menu-fix.js"></script>
    <script>
        function checkMenuFix() {
            const status = document.getElementById('status');
            
            // Check if universal fix is loaded
            if (typeof window.initMenuFix === 'function') {
                status.innerHTML = '<p class="success">✅ Universal Menu Fix is loaded!</p>';
            } else {
                status.innerHTML = '<p class="error">❌ Universal Menu Fix NOT loaded</p>';
            }
            
            // Find menu elements
            const menuToggle = document.querySelector('.styles_menuToggle__5pQ0a, .icon-menu, .cred-icon');
            const menu = document.querySelector('nav, .menu, [class*="menu"]:not([class*="Toggle"])');
            
            if (menuToggle) {
                status.innerHTML += `<p class="success">✅ Found menu toggle: ${menuToggle.className}</p>`;
                menuToggle.style.outline = '3px solid #4CAF50';
            } else {
                status.innerHTML += '<p class="error">❌ No menu toggle found</p>';
            }
            
            if (menu) {
                status.innerHTML += `<p class="success">✅ Found menu: ${menu.className || menu.tagName}</p>`;
                menu.style.outline = '3px solid #2196F3';
            } else {
                status.innerHTML += '<p class="error">❌ No menu found</p>';
            }
            
            console.log('Menu toggle:', menuToggle);
            console.log('Menu:', menu);
        }
        
        function testMenuToggle() {
            const menuToggle = document.querySelector('.styles_menuToggle__5pQ0a, .icon-menu, .cred-icon');
            const menu = document.querySelector('nav, .menu');
            
            if (menuToggle && menu) {
                if (menu.style.display === 'none' || menu.style.display === '') {
                    menu.style.display = 'block';
                    alert('Menu opened manually');
                } else {
                    menu.style.display = 'none';
                    alert('Menu closed manually');
                }
            } else {
                alert('Could not find menu elements to toggle');
            }
        }
        
        // Auto-check on load
        setTimeout(checkMenuFix, 1000);
        
        console.log('Diagnostic page loaded');
        console.log('Check elements with classes: styles_menuToggle__5pQ0a, cred-icon, icon-menu');
    </script>
</body>
</html>'''
    
    diagnostic_file = os.path.join(root_dir, "menu-diagnostic.html")
    with open(diagnostic_file, "w", encoding="utf-8") as f:
        f.write(diagnostic_html)
    
    print(f"\n✅ Created diagnostic page: {diagnostic_file}")
    
    print("\n" + "=" * 60)
    print("📋 NEXT STEPS:")
    print("1. Open menu-diagnostic.html")
    print("2. Click 'Check Menu Fix' button")
    print("3. It will highlight menu elements in GREEN if found")
    print("4. Click the menu icon - it should work now!")
    print("\n🔄 If still not working, we need to find the ORIGINAL menu JavaScript")
    print("   and restore it or integrate with our fix.")

if __name__ == "__main__":
    find_and_fix_menu()
    