/* TATZMY — interaction engine (no dependencies) */
(function () {
  'use strict';

  /* ---------- intro overlay (home only) ---------- */
  var intro = document.querySelector('.intro');
  if (intro) {
    document.documentElement.style.overflow = 'hidden';
    setTimeout(function () { intro.classList.add('reveal'); }, 150);
    setTimeout(function () { intro.classList.add('exit'); }, 1450);
    setTimeout(function () {
      intro.classList.add('lift');
      document.documentElement.style.overflow = '';
    }, 1900);
    setTimeout(function () { intro.remove(); }, 3100);
  }

  /* ---------- infinite marquees ---------- */
  function marquee(el) {
    var track = el.querySelector('.track');
    if (!track) return;
    var speed = parseFloat(el.getAttribute('data-speed') || '60'); // px/s
    var dir = parseFloat(el.getAttribute('data-dir') || '-1');

    var base = Array.prototype.slice.call(track.children);
    var unit = 0;

    // measure one loop's width, then clone until the track always covers the
    // viewport at the wrap point (unit + 2x container) so the loop is seamless.
    // Re-run after images/fonts load and on resize — widths change.
    function measure() {
      Array.prototype.slice.call(track.querySelectorAll('[data-clone]')).forEach(function (n) { n.remove(); });
      var gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap) || 0;
      unit = 0;
      base.forEach(function (n) { unit += n.getBoundingClientRect().width + gap; });
      if (unit <= 0) return;
      var safety = 0;
      while (track.scrollWidth < unit + el.offsetWidth * 2 && safety < 60) {
        base.forEach(function (n) {
          var c = n.cloneNode(true);
          c.setAttribute('aria-hidden', 'true');
          c.setAttribute('data-clone', '');
          track.appendChild(c);
        });
        safety++;
      }
    }
    measure();
    window.addEventListener('load', measure);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
    window.addEventListener('resize', measure);

    var x = 0, last = null, paused = false;
    el.addEventListener('mouseenter', function () { if (el.hasAttribute('data-pause')) paused = true; });
    el.addEventListener('mouseleave', function () { paused = false; });
    function tick(t) {
      if (last !== null && !paused && !document.hidden && unit > 0) {
        x += dir * speed * (t - last) / 1000;
        x = x % unit;
        if (x > 0) x -= unit;
        track.style.transform = 'translateX(' + x.toFixed(2) + 'px)';
      }
      last = t;
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  document.querySelectorAll('[data-marquee]').forEach(marquee);

  /* ---------- rolling button text (hover in = roll up, hover out = roll back) ---------- */
  function rollify(target, host) {
    if (!target || target.querySelector('.roll')) return;
    var text = target.textContent.replace(/\s+/g, ' ').trim();
    if (!text) return;
    var roll = document.createElement('span');
    roll.className = 'roll';
    [0, 1].forEach(function (i) {
      var line = document.createElement('span');
      line.className = 'roll-line';
      line.textContent = text;
      if (i) line.setAttribute('aria-hidden', 'true');
      roll.appendChild(line);
    });
    target.textContent = '';
    target.appendChild(roll);
    (host || target).classList.add('roll-hover');
  }
  document.querySelectorAll('.btn-pill').forEach(function (b) { rollify(b.querySelector('.txt'), b); });
  document.querySelectorAll('.nav-link').forEach(function (n) { rollify(n.querySelector('p'), n); });
  document.querySelectorAll('.booking button[type=submit]').forEach(function (b) { rollify(b, b); });

  /* ---------- appear on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.appear').forEach(function (n) { io.observe(n); });

  /* ---------- about-2: light paragraphs + scroll-driven image brightness ---------- */
  var textCol = document.querySelector('.about-2 .text-col');
  if (textCol) {
    var paras = textCol.querySelectorAll('p');
    var imgs = document.querySelectorAll('.about-2 .img-sticky img');
    var pio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add('lit');
        else if (e.boundingClientRect.top > 0) e.target.classList.remove('lit');
      });
    }, { rootMargin: '-30% 0px -45% 0px' });
    paras.forEach(function (p) { pio.observe(p); });

    // each image fades up as its paragraph approaches the reading line,
    // peaks while the text is lit, then hands over to the next image
    if (imgs.length) {
      var aboutTick = false;
      var updateAboutImgs = function () {
        aboutTick = false;
        var vh = window.innerHeight;
        var focus = vh * 0.45;
        var centers = Array.prototype.map.call(paras, function (p) {
          var r = p.getBoundingClientRect();
          return r.top + r.height / 2;
        });
        // keep each image's fade range under half the paragraph spacing so one
        // image is fully out before the next comes in — no double-exposure mix
        var minSpacing = Infinity;
        for (var s = 1; s < centers.length; s++) {
          minSpacing = Math.min(minSpacing, Math.abs(centers[s] - centers[s - 1]));
        }
        if (!isFinite(minSpacing)) minSpacing = vh * 0.8;
        var range = Math.max(140, minSpacing * 0.45);
        var t = Array.prototype.map.call(imgs, function () { return 0; });
        centers.forEach(function (c, i) {
          var v = 1 - Math.min(1, Math.abs(c - focus) / range);
          var k = Math.min(i, imgs.length - 1);
          if (v > t[k]) t[k] = v;
        });
        imgs.forEach(function (im, k) {
          im.style.opacity = (0.65 * t[k]).toFixed(3);
        });
      };
      var onAboutScroll = function () {
        if (!aboutTick) { aboutTick = true; requestAnimationFrame(updateAboutImgs); }
      };
      window.addEventListener('scroll', onAboutScroll, { passive: true });
      window.addEventListener('resize', onAboutScroll);
      updateAboutImgs();
    }
  }

  /* ---------- CTA white takeover (turns white at mid-viewport, stays white
       once passed so the sections after it continue seamlessly) ---------- */
  var cta = document.querySelector('.cta-scroll');
  if (cta) {
    var trigger = cta.querySelector('.cta-trigger');
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        cta.classList.toggle('on', en.boundingClientRect.top <= window.innerHeight * 0.5);
      });
    }, { threshold: [0, 0.25, 0.5, 0.75, 1] });
    if (trigger) tio.observe(trigger);

    // fully scroll-scrubbed takeover: the sheet's rise and the text zoom are
    // pure functions of scroll position — scrub down, it fills; scrub up, it
    // drains. Zoom ramps from the moment the section enters the viewport.
    var ctaWf = cta.querySelector('.whiteframe');
    var ctaSub = cta.querySelector('.frame .t-sub');
    var ctaTick = false;
    var ctaScrub = function () {
      ctaTick = false;
      var r = cta.getBoundingClientRect();
      var vh = window.innerHeight;
      var pinSpan = r.height - vh;
      var pPin = pinSpan > 0 ? Math.min(1, Math.max(0, -r.top / pinSpan)) : 0;
      var pAll = Math.min(1, Math.max(0, (vh - r.top) / r.height));
      if (ctaWf) ctaWf.style.transform = 'translateY(' + ((1 - pPin) * 100).toFixed(2) + '%)';
      if (ctaSub) ctaSub.style.transform = 'scale(' + (1 + 0.12 * pAll).toFixed(4) + ')';
    };
    var onCtaScroll = function () {
      if (!ctaTick) { ctaTick = true; requestAnimationFrame(ctaScrub); }
    };
    window.addEventListener('scroll', onCtaScroll, { passive: true });
    window.addEventListener('resize', onCtaScroll);
    ctaScrub();
  }

  /* ---------- footer reveal: match the window to the real footer height ---------- */
  var foot = document.querySelector('.site-footer');
  function sizeReveal() {
    if (foot) document.documentElement.style.setProperty('--footer-reveal', foot.offsetHeight + 'px');
  }
  sizeReveal();
  window.addEventListener('resize', sizeReveal);
  window.addEventListener('load', sizeReveal);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(sizeReveal);
  if (foot && window.ResizeObserver) new ResizeObserver(sizeReveal).observe(foot);

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      document.body.classList.toggle('menu-open');
    });
    document.querySelectorAll('.mobile-menu a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
    });
  }

  /* ---------- autoplay videos (some browsers need a nudge) ---------- */
  document.querySelectorAll('video[autoplay]').forEach(function (v) {
    v.muted = true;
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
  });

  /* ---------- booking form (demo submit) ---------- */
  document.querySelectorAll('.booking form').forEach(function (f) {
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      // honeypot check
      var trap = f.querySelector('.hp input');
      if (trap && trap.value) return;
      var btn = f.querySelector('button[type=submit]');
      var orig = btn.innerHTML; // keep the roll markup for restore
      btn.textContent = 'Thank you — we’ll be in touch';
      btn.disabled = true;
      setTimeout(function () {
        btn.innerHTML = orig;
        btn.disabled = false;
        f.reset();
      }, 4000);
    });
  });

  /* ---------- smooth anchor scrolling ---------- */
  document.querySelectorAll('a[href*="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var url = new URL(a.href, location.href);
      if (url.pathname === location.pathname && url.hash) {
        var t = document.querySelector(url.hash);
        if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
      }
    });
  });
})();
