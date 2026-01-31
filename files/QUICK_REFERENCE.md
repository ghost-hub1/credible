# Quick Reference: Icon Fix for Cloned Credible Site

## 📋 What This Fixes
- Broken icons from cdn.credible.com
- Failed FontAwesome attempts
- Non-working SVG conversions

## ⚡ Quick Implementation (3 Steps)

### 1️⃣ Add to `<head>` (Every Page)
```html
<head>
<!-- Copy the full icon fix code from ICON_FIX_GUIDE.md -->
<!-- Paste it right after <head> tag -->
```

### 2️⃣ Delete Old Code
Remove these from every page:
- `/fontawesome/css/all.min.css`
- `/css/absolute-fix.css`
- Old icon font CSS

### 3️⃣ Test
Open browser console → Should see:
`✅ SVG Icons loaded successfully`

## 🎨 Included Icons

✓ menu
✓ chevron-right, chevron-left
✓ check, close
✓ search
✓ arrow-forward
✓ credit-score
✓ coins
✓ star
✓ phone
✓ email
✓ home
✓ person
✓ calendar

## 🔧 Common Tasks

### Change Icon Color
```html
<span class="icon-menu" style="color: red;">Menu</span>
```

### Change Icon Size
```css
.icon-menu .icon-svg {
    width: 30px;
    height: 30px;
}
```

### Add New Icon
Find SVG at fonts.google.com/icons, then:
```javascript
// In the icons object
'new-icon-name': '<svg class="icon-svg" viewBox="0 0 24 24"><path d="..."/></svg>'
```

## 🐛 Troubleshooting

**Problem:** Icons not showing
**Fix:** Check browser console for errors

**Problem:** Wrong icon appears
**Fix:** Verify class name matches icon name exactly

**Problem:** Icon too small/large
**Fix:** Add size CSS (see above)

## 💡 Pro Tips

1. Test one page first before applying to all
2. Keep all icon definitions in one place
3. Use browser DevTools to inspect icons
4. Console message confirms successful load

## 📁 Files You Need

1. **ICON_FIX_GUIDE.md** - Full documentation
2. **index-fixed.html** - Example implementation
3. This quick reference

## ✅ Success Checklist

- [ ] Code added to `<head>` of all pages
- [ ] Old FontAwesome code removed
- [ ] Console shows success message
- [ ] All icons display correctly
- [ ] Icons work on hover/click
- [ ] No console errors

---

**Need Help?** Check ICON_FIX_GUIDE.md for detailed instructions
