@echo off
echo 🚀 Setting up SVG Icon System...
echo.

REM Create necessary directories
if not exist "icons" mkdir icons
if not exist "css" mkdir css

echo 📁 Created directories: icons, css
echo.

REM Run the conversion
python convert_all_icons.py

echo.
echo ✅ SETUP COMPLETE!
echo.
echo 📋 What was done:
echo 1. Created SVG sprite with Credible icons
echo 2. Converted all HTML icon elements to SVG
echo 3. Added professional CSS styling
echo 4. Generated conversion report
echo.
echo 🔄 To update icons after HTML changes, run this file again.
echo 🖥️  Open any HTML file and refresh with Ctrl+F5
echo.
pause