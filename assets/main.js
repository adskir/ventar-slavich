(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // мобильное меню
  var m = document.getElementById('mnav'), ob = document.querySelector('.menu-btn');
  if (m && ob) {
    var cb = m.querySelector('.close');
    var set = function (o) {
      m.classList.toggle('open', o);
      ob.setAttribute('aria-expanded', o ? 'true' : 'false');
      document.body.style.overflow = o ? 'hidden' : '';
      (o ? cb : ob).focus();
    };
    ob.addEventListener('click', function () { set(true); });
    cb.addEventListener('click', function () { set(false); });
    m.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  }

  // появление при прокрутке + счётчики
  var count = function (el) {
    var to = +el.getAttribute('data-to'), t0 = null;
    if (reduce) { el.textContent = to; return; }
    var step = function (t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / 1400), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * e);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  var els = document.querySelectorAll('.rv, .alerts, .steps, .funnel, .mark, [data-to]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        if (e.target.hasAttribute('data-to')) count(e.target);
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -10% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); if (el.hasAttribute('data-to')) el.textContent = el.getAttribute('data-to'); });
  }

  // печатающийся пример адреса
  var inp = document.querySelector('[data-type]');
  if (inp && !reduce) {
    var words = inp.getAttribute('data-type').split('|'), wi = 0, ci = 0, del = false;
    var tick = function () {
      if (document.activeElement === inp || inp.value) { inp.placeholder = 'адрес-вашего-сайта.ru'; return setTimeout(tick, 1200); }
      var w = words[wi];
      ci += del ? -1 : 1;
      inp.placeholder = w.slice(0, ci) + (ci % 2 ? '▍' : '');
      var d = del ? 45 : 95;
      if (!del && ci === w.length) { del = true; d = 1600; }
      else if (del && ci === 0) { del = false; wi = (wi + 1) % words.length; d = 400; }
      setTimeout(tick, d);
    };
    setTimeout(tick, 1600);
  }

  // адрес сайта из главной -> в форму контактов
  var q = new URLSearchParams(location.search).get('site');
  var siteField = document.getElementById('f-site');
  if (q && siteField) siteField.value = q;

  // год
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
