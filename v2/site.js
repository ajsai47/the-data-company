(function () {
  var nav = document.getElementById('nav');
  var hero = document.querySelector('[data-launch]');
  var page = location.pathname.split('/').pop();
  var t = new URLSearchParams(location.search).get('t');
  document.querySelectorAll('a[href$=".html"],a[href*=".html#"]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (h.split('#')[0] === page) a.classList.add('on');
    if (t && !/^https?:/.test(h)) {
      var p = h.split('#');
      a.setAttribute('href', p[0] + (p[0].indexOf('?') > -1 ? '&' : '?') + 't=' + t + (p[1] ? '#' + p[1] : ''));
    }
  });
  var menu = nav && nav.querySelector('.menu');
  if (menu) menu.addEventListener('click', function () { nav.classList.toggle('open'); });
  var links = nav && nav.querySelector('.links');
  if (links) links.addEventListener('click', function (e) {
    if (e.target === links) location.href = nav.querySelector('.btn').href;
  });
  var px = document.querySelectorAll('.phero .bg');
  function f() {
    var lim = hero ? hero.offsetHeight - innerHeight * 1.1 : innerHeight * 0.6;
    if (nav) nav.classList.toggle('solid', scrollY > lim);
    px.forEach(function (b) { b.style.setProperty('--y', (scrollY * 0.18).toFixed(1)); });
    requestAnimationFrame(f);
  }
  requestAnimationFrame(f);
})();
