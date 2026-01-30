// FORCE ICONS TO SHOW - Works no matter what
(function() {
    console.log('🚀 FORCE-ICONS: Starting icon fix...');
    
    // Wait for page to load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', forceAllIcons);
    } else {
        forceAllIcons();
    }
    
    function forceAllIcons() {
        console.log('🔧 FORCE-ICONS: Running icon replacement...');
        
        // Map of icon classes to Unicode
        const iconMap = {
            'icon-menu': '&#xf0c9;',
            'icon-chevron-right': '&#xf054;',
            'icon-chevron-left': '&#xf053;',
            'icon-close': '&#xf00d;',
            'icon-check': '&#xf00c;',
            'icon-search': '&#xf002;',
            'icon-arrow-forward': '&#xf061;',
            'icon-credit-score': '&#xf09d;',
            'icon-coins': '&#xf51e;',
            'icon-arrow-right': '&#xf061;',
            'icon-arrow-left': '&#xf060;',
            'icon-home': '&#xf015;',
            'icon-user': '&#xf007;',
            'icon-phone': '&#xf095;',
            'icon-email': '&#xf0e0;',
            'icon-star': '&#xf005;'
        };
        
        // Replace ALL icon elements with actual Unicode
        Object.keys(iconMap).forEach(iconClass => {
            document.querySelectorAll('.' + iconClass).forEach(el => {
                if (!el.hasAttribute('data-icon-forced')) {
                    console.log(`🔄 Replacing ${iconClass} with icon`);
                    el.setAttribute('data-icon-forced', 'true');
                    el.innerHTML = iconMap[iconClass];
                    el.style.fontFamily = "'Font Awesome 6 Free', 'Segoe UI Symbol', sans-serif";
                    el.style.fontWeight = '900';
                }
            });
        });
        
        // Fix slick buttons
        document.querySelectorAll('.slick-prev, .slick-next').forEach(btn => {
            if (!btn.hasAttribute('data-icon-forced')) {
                btn.setAttribute('data-icon-forced', 'true');
                btn.innerHTML = btn.classList.contains('slick-prev') ? '&#xf060;' : '&#xf061;';
                btn.style.fontFamily = "'Font Awesome 6 Free', sans-serif";
                btn.style.fontSize = '24px';
                btn.style.fontWeight = '900';
            }
        });
        
        // Fix cred-icon elements
        document.querySelectorAll('.cred-icon').forEach(el => {
            if (!el.hasAttribute('data-icon-forced')) {
                el.setAttribute('data-icon-forced', 'true');
                // Try to guess which icon based on classes
                const classes = el.className;
                if (classes.includes('menu')) el.innerHTML = '&#xf0c9;';
                else if (classes.includes('check')) el.innerHTML = '&#xf00c;';
                else if (classes.includes('close')) el.innerHTML = '&#xf00d;';
                else if (classes.includes('search')) el.innerHTML = '&#xf002;';
                
                el.style.fontFamily = "'Font Awesome 6 Free', sans-serif";
                el.style.fontWeight = '900';
            }
        });
        
        console.log(`✅ FORCE-ICONS: Fixed ${document.querySelectorAll('[data-icon-forced]').length} icons`);
    }
    
    // Run multiple times to catch dynamic content
    setTimeout(forceAllIcons, 500);
    setTimeout(forceAllIcons, 1000);
    setTimeout(forceAllIcons, 2000);
    
    // Watch for new elements
    const observer = new MutationObserver(forceAllIcons);
    observer.observe(document.body, { childList: true, subtree: true });
})();
