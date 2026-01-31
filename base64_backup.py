import base64
import os

# Convert font to base64
font_path = r"C:\My Web Sites\credible\fontawesome\webfonts\fa-solid-900.woff2"
if os.path.exists(font_path):
    with open(font_path, 'rb') as f:
        font_data = f.read()
    
    base64_font = base64.b64encode(font_data).decode('utf-8')
    
    # Create the CSS with the base64 font
    css = f'''@font-face {{
  font-family: 'FontAwesomeDataURI';
  src: url('data:font/woff2;charset=utf-8;base64,{base64_font}') format('woff2');
  font-weight: 900;
  font-display: block;
}}'''
    
    print("✅ Base64 font generated. Replace [PASTE_BASE64_HERE] in the CSS with:")
    print("\n...long base64 string...")
else:
    print(f"❌ Font not found at: {font_path}")
    