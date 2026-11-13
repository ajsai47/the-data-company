(function () {
  var nav = document.getElementById('nav');
  var hero = document.querySelector('[data-launch]');
  var page = location.pathname.split('/').pop() || 'home.html';
  var t = new URLSearchParams(location.search).get('t');
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (!/\.html/.test(h) || /^https?:/.test(h)) return;
    if (h.split(/[?#]/)[0] === page && a.closest('nav .links')) a.classList.add('on');
    if (t) {
      var p = h.split('#');
      a.setAttribute('href', p[0] + (p[0].indexOf('?') > -1 ? '&' : '?') + 't=' + t + (p[1] ? '#' + p[1] : ''));
    }
  });
  var menu = nav && nav.querySelector('.menu');
  if (menu) menu.addEventListener('click', function () { nav.classList.toggle('open'); });
  var bgs = [].slice.call(document.querySelectorAll('.scene .bg')).filter(function (b) { return !b.closest('.split'); });
  function f() {
    var lim = hero ? hero.offsetHeight - innerHeight * 1.05 : innerHeight * 0.5;
    if (nav) nav.classList.toggle('solid', scrollY > lim);
    bgs.forEach(function (b) {
      var r = b.parentNode.getBoundingClientRect();
      if (r.bottom > 0 && r.top < innerHeight) b.style.setProperty('--y', (r.top * -0.06).toFixed(1));
    });
    requestAnimationFrame(f);
  }
  requestAnimationFrame(f);
})();
