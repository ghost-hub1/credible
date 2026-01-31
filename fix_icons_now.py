import os
import re

def create_emergency_fix():
    root_dir = r"C:\My Web Sites\credible"
    
    print("🚀 Creating emergency icon fix...")
    
    # Create CSS with inline SVG
    css = '''/* EMERGENCY ICON FIX - Inline SVG */
.icon-menu, .icon-chevron-right, .icon-chevron-left, 
.icon-close, .icon-search, .icon-credit-score, .icon-coins,
.icon-arrow-forward, .icon-arrow-back, .icon-user,
.icon-phone, .icon-email, .icon-star, .slick-prev, .slick-next {
    display: inline-block;
    width: 24px;
    height: 24px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    vertical-align: middle;
}

/* Menu */
.icon-menu { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z' fill='black'/></svg>"); }

/* Chevrons */
.icon-chevron-right { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z' fill='black'/></svg>"); }
.icon-chevron-left { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z' fill='black'/></svg>"); }

/* Arrows */
.icon-arrow-forward, .icon-arrow-right { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z' fill='black'/></svg>"); }
.icon-arrow-back, .icon-arrow-left { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20z' fill='black'/></svg>"); }

/* Financial */
.icon-credit-score { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z' fill='black'/><path d='M8 12h8v2H8z' fill='black'/></svg>"); }
.icon-coins { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><circle cx='12' cy='12' r='10' fill='gold' stroke='brown'/><circle cx='8' cy='8' r='3' fill='goldenrod'/><circle cx='16' cy='16' r='3' fill='goldenrod'/></svg>"); }

/* Common */
.icon-search { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z' fill='black'/></svg>"); }
.icon-close { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z' fill='black'/></svg>"); }
.icon-user { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z' fill='black'/></svg>"); }
.icon-phone { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z' fill='black'/></svg>"); }
.icon-email { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8l8 5 8-5v10zm-8-7L4 6h16l-8 5z' fill='black'/></svg>"); }
.icon-star { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z' fill='gold' stroke='orange'/></svg>"); }

/* Slick */
.slick-prev { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z' fill='black'/></svg>"); }
.slick-next { background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z' fill='black'/></svg>"); }

/* Colors */
.icon-primary { border: 2px solid blue; }
.icon-success { border: 2px solid green; }
.icon-warning { border: 2px solid orange; }
.icon-error { border: 2px solid red; }

/* Show something is there */
[class*="icon-"]:empty::before {
    content: "Icon";
    font-size: 8px;
    color: gray;
    display: block;
    text-align: center;
    line-height: 24px;
}
'''
    
    # Create CSS file
    css_dir = os.path.join(root_dir, "css")
    os.makedirs(css_dir, exist_ok=True)
    
    css_file = os.path.join(css_dir, "emergency-icons.css")
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css)
    
    print(f"✅ Created CSS: {css_file}")
    
    # Add CSS to all HTML files
    css_link = '<link rel="stylesheet" href="css/emergency-icons.css">'
    
    updated = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add CSS if not already there
                if 'emergency-icons.css' not in content:
                    # Clean up old icon CSS
                    content = re.sub(r'<link[^>]*svg-icons\.css[^>]*>', '', content)
                    content = re.sub(r'<link[^>]*inline-icons\.css[^>]*>', '', content)
                    
                    if '</head>' in content:
                        new_content = content.replace('</head>', f'    {css_link}\n</head>')
                    else:
                        new_content = f'<head>\n{css_link}\n</head>\n{content}'
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    updated += 1
                    print(f"✅ Updated: {file}")
    
    print(f"\n🎉 Updated {updated} HTML files")
    
    # Create test file
    test_html = '''<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="css/emergency-icons.css">
    <style>
        body { font-family: Arial; padding: 20px; }
        .test { margin: 10px 0; padding: 10px; border: 1px solid #ccc; }
        .icon-demo { margin: 5px; }
    </style>
</head>
<body>
    <h1>✅ Emergency Icon Test</h1>
    
    <div class="test">
        <h3>Basic Icons:</h3>
        <p><span class="icon-menu icon-demo"></span> Menu</p>
        <p><span class="icon-chevron-right icon-demo"></span> Chevron Right</p>
        <p><span class="icon-chevron-left icon-demo"></span> Chevron Left</p>
        <p><span class="icon-close icon-demo"></span> Close</p>
        <p><span class="icon-search icon-demo"></span> Search</p>
    </div>
    
    <div class="test">
        <h3>Financial Icons:</h3>
        <p><span class="icon-credit-score icon-demo"></span> Credit Score</p>
        <p><span class="icon-coins icon-demo"></span> Coins</p>
    </div>
    
    <div class="test">
        <h3>Arrow Icons:</h3>
        <p><span class="icon-arrow-forward icon-demo"></span> Arrow Forward</p>
        <p><span class="icon-arrow-back icon-demo"></span> Arrow Back</p>
    </div>
    
    <div class="test">
        <h3>Other Icons:</h3>
        <p><span class="icon-user icon-demo"></span> User</p>
        <p><span class="icon-phone icon-demo"></span> Phone</p>
        <p><span class="icon-email icon-demo"></span> Email</p>
        <p><span class="icon-star icon-demo"></span> Star</p>
    </div>
    
    <script>
        console.log('Icons should show as colored squares');
        console.log('If you see "Icon" text, images are not loading');
    </script>
</body>
</html>'''
    
    test_file = os.path.join(root_dir, "test-icons-fixed.html")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(test_html)
    
    print(f"\n✅ Created test file: {test_file}")
    print("\n📋 NEXT:")
    print("1. Open test-icons-fixed.html in your browser")
    print("2. You should see colored squares/icons")
    print("3. Open any other HTML file - icons should work!")
    print("\n🔄 If icons don't show, your browser may be blocking data URLs")
    print("   Try running: python -m http.server 8000")

if __name__ == "__main__":
    create_emergency_fix()
    