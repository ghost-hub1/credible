// UNIVERSAL ICON FIX - Works on ALL pages automatically
document.addEventListener('DOMContentLoaded', function() {
  // Fix all elements with icon-* classes
  fixIconClasses();
  
  // Also fix dynamically added content
  const observer = new MutationObserver(fixIconClasses);
  observer.observe(document.body, { childList: true, subtree: true });
});

function fixIconClasses() {
  // Fix icon-* classes
  document.querySelectorAll('[class*="icon-"]').forEach(el => {
    if (!el.hasAttribute('data-icon-fixed')) {
      el.setAttribute('data-icon-fixed', 'true');
      el.style.fontStyle = 'normal';
    }
  });
  
  // Fix Slick slider arrows
  document.querySelectorAll('.slick-prev, .slick-next').forEach(btn => {
    if (!btn.hasAttribute('data-icon-fixed')) {
      btn.setAttribute('data-icon-fixed', 'true');
      if (!btn.innerHTML.includes('::before')) {
        btn.style.position = 'relative';
      }
    }
  });
  
  // Fix aria-label arrows
  document.querySelectorAll('[aria-label*="arrow"]').forEach(btn => {
    if (!btn.hasAttribute('data-icon-fixed')) {
      btn.setAttribute('data-icon-fixed', 'true');
      btn.style.position = 'relative';
    }
  });
}
