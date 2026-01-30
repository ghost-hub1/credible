// Save as /js/icon-nuclear-fix.js
document.addEventListener('DOMContentLoaded', function() {
    // Function to force icons to show
    function forceIcons() {
        // For every element with icon in class
        document.querySelectorAll('[class*="icon"]').forEach(el => {
            // Add a data attribute to mark as fixed
            if (!el.dataset.iconFixed) {
                el.dataset.iconFixed = 'true';
                
                // Force FontAwesome
                el.style.fontFamily = "'Font Awesome 6 Free'";
                el.style.fontWeight = '900';
                el.style.fontStyle = 'normal';
                
                // Map common icons
                const classes = el.className;
                if (classes.includes('menu')) el.innerHTML = '&#xf0c9;';
                if (classes.includes('chevron-right')) el.innerHTML = '&#xf054;';
                if (classes.includes('chevron-left')) el.innerHTML = '&#xf053;';
                if (classes.includes('arrow-forward')) el.innerHTML = '&#xf061;';
                if (classes.includes('credit-score')) el.innerHTML = '&#xf09d;';
                if (classes.includes('coins')) el.innerHTML = '&#xf51e;';
            }
        });
        
        // Fix slick buttons
        document.querySelectorAll('.slick-prev, .slick-next').forEach(btn => {
            if (!btn.dataset.iconFixed) {
                btn.dataset.iconFixed = 'true';
                btn.innerHTML = btn.classList.contains('slick-prev') ? '&#xf060;' : '&#xf061;';
            }
        });
    }
    
    // Run immediately
    forceIcons();
    
    // Run again after a delay
    setTimeout(forceIcons, 500);
    setTimeout(forceIcons, 1000);
    
    // Watch for new elements
    const observer = new MutationObserver(forceIcons);
    observer.observe(document.body, { childList: true, subtree: true });
});
