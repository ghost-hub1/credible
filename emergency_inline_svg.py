# emergency_inline_svg.py
import os
import re
import base64

def create_inline_svg_fix():
    root_dir = r"C:\My Web Sites\credible"
    
    # Create emergency CSS with inline SVG data URLs
    css_content = '''/* EMERGENCY INLINE SVG FIX - No external files needed */
[class*="icon-"], .slick-prev, .slick-next, .cred-icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    vertical-align: middle;
}

/* Menu Icon */
.icon-menu {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Chevron Icons */
.icon-chevron-right {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-chevron-left {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Arrow Icons */
.icon-arrow-forward, .icon-arrow-right {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-arrow-back, .icon-arrow-left {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Financial Icons */
.icon-credit-score {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z' fill='currentColor'/%3E%3Cpath d='M8 12h8v2H8z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-coins {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z' fill='currentColor'/%3E%3Ccircle cx='8.5' cy='9.5' r='1.5' fill='currentColor'/%3E%3Ccircle cx='15.5' cy='14.5' r='1.5' fill='currentColor'/%3E%3Cpath d='M12 15.5c1.93 0 3.5-1.57 3.5-3.5S13.93 8.5 12 8.5 8.5 10.07 8.5 12s1.57 3.5 3.5 3.5z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Common Icons */
.icon-search {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-close {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-check {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-user {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-phone {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-email {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8l8 5 8-5v10zm-8-7L4 6h16l-8 5z' fill='currentColor'/%3E%3C/svg%3E");
}

.icon-star {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Slick Slider */
.slick-prev {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z' fill='currentColor'/%3E%3C/svg%3E");
}

.slick-next {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Size variations */
.icon-small, .credible-icon.small { width: 16px; height: 16px; }
.icon-medium, .credible-icon.medium { width: 20px; height: 20px; }
.icon-large, .credible-icon.large { width: 32px; height: 32px; }

/* Color classes */
.icon-primary { background-color: rgba(0, 102, 204, 0.1); }
.icon-success { background-color: rgba(76, 175, 80, 0.1); }
.icon-warning { background-color: rgba(255, 152, 0, 0.1); }
.icon-error { background-color: rgba(244, 67, 54, 0.1); }

/* Debug mode - shows border */
[class*="icon-"] {
    border: 1px solid rgba(0,0,0,0.1);
}
'''
    
    # Create CSS directory and file
    css_dir = os.path.join(root_dir, "css")
    os.makedirs(css_dir, exist_ok=True)
    
    css_path = os.path.join(css_dir, "inline-icons.css")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    
    print(f"✅ Created inline SVG CSS: {css_path}")
    
    # Now add this CSS to ALL HTML files
    css_link = '<link rel="stylesheet" href="/css/inline-icons.css">'
    
    files_updated = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove any existing SVG CSS links to avoid conflicts
                content = re.sub(r'<link[^>]*svg-icons\.css[^>]*>', '', content)
                content = re.sub(r'<link[^>]*inline-icons\.css[^>]*>', '', content)
                
                # Add our inline CSS link
                if '</head>' in content:
                    new_content = content.replace('</head>', f'    {css_link}\n</head>')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    files_updated += 1
                    print(f"✅ Updated: {file}")
    
    print(f"\n🎉 Updated {files_updated} HTML files")
    print("\n🔄 Open any HTML file and refresh with Ctrl+F5")
    print("📋 Icons will now show as background images (no SVG files needed)")

if __name__ == "__main__":
    create_inline_svg_fix()
    