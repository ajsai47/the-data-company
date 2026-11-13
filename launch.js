(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('[data-launch]').forEach(function (hero) {
    var v = hero.querySelector('video');
    var small = matchMedia('(max-width: 720px)').matches;
    v.muted = true;
    v.playsInline = true;
    v.preload = 'auto';
    v.src = small ? v.dataset.srcMobile : v.dataset.src;
    if (small && v.dataset.posterMobile) v.poster = v.dataset.posterMobile;

    var dur = 10, cur = 0, ready = false;
    v.addEventListener('loadedmetadata', function () {
      dur = v.duration || 10;
      ready = true;
      v.pause();
      if (reduce) v.currentTime = dur * 0.82;
    });
    v.play().then(function () { v.pause(); }).catch(function () {});

    var phased = hero.querySelectorAll('[data-from]');

    function progress() {
      var r = hero.getBoundingClientRect();
      var span = r.height - innerHeight;
      return span > 0 ? Math.min(1, Math.max(0, -r.top / span)) : 0;
    }

    function tick() {
      var p = progress();
      hero.style.setProperty('--p', p.toFixed(4));
      phased.forEach(function (el) {
        var a = +el.dataset.from, b = +(el.dataset.to || 2);
        el.classList.toggle('on', p >= a && p < b);
      });
      if (!ready && v.readyState >= 1) { dur = v.duration || 10; ready = true; }
      if (!reduce && ready) {
        var target = p * (dur - 0.08);
        cur += (target - cur) * 0.2;
        if (Math.abs(v.currentTime - cur) > 0.015 && !v.seeking) v.currentTime = cur;
      }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.reveal').forEach(function (el) {
    if (reduce) el.classList.add('in'); else io.observe(el);
  });
})();
