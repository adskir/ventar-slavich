// Простое мобильное меню: клик по бургеру раскрывает/скрывает навигацию
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', function () {
    var isOpen = nav.classList.toggle('is-open');
    nav.style.display = isOpen ? 'flex' : 'none';
    if (isOpen) {
      nav.style.position = 'absolute';
      nav.style.top = '100%';
      nav.style.left = '0';
      nav.style.right = '0';
      nav.style.flexDirection = 'column';
      nav.style.background = '#0a0a0c';
      nav.style.padding = '20px 24px';
      nav.style.borderBottom = '1px solid rgba(245,244,242,0.14)';
    }
  });
});
