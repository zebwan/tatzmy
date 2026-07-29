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
    var gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap) || 0;

    // clone children until track >= 2x container
    var base = Array.prototype.slice.call(track.children);
    var safety = 0;
    function width() { return track.scrollWidth; }
    while (width() < el.offsetWidth * 2 + 10 && safety < 40) {
      base.forEach(function (n) {
        var c = n.cloneNode(true);
        c.setAttribute('aria-hidden', 'true');
        track.appendChild(c);
      });
      safety++;
    }
    var unit = 0;
    base.forEach(function (n) { unit += n.getBoundingClientRect().width + gap; });
    if (unit <= 0) return;

    var x = 0, last = null, paused = false;
    el.addEventListener('mouseenter', function () { if (el.hasAttribute('data-pause')) paused = true; });
    el.addEventListener('mouseleave', function () { paused = false; });
    function tick(t) {
      if (last !== null && !paused && !document.hidden) {
        x += dir * speed * (t - last) / 1000;
        if (x <= -unit) x += unit;
        if (x > 0) x -= unit;
        track.style.transform = 'translateX(' + x.toFixed(2) + 'px)';
      }
      last = t;
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  document.querySelectorAll('[data-marquee]').forEach(marquee);

  /* ---------- appear on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.appear').forEach(function (n) { io.observe(n); });

  /* ---------- about-2: light paragraphs + swap sticky image ---------- */
  var textCol = document.querySelector('.about-2 .text-col');
  if (textCol) {
    var paras = textCol.querySelectorAll('p');
    var imgs = document.querySelectorAll('.about-2 .img-sticky img');
    var pio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = Array.prototype.indexOf.call(paras, e.target);
        if (e.isIntersecting) {
          e.target.classList.add('lit');
          imgs.forEach(function (im, k) {
            im.classList.toggle('on', k === Math.min(i, imgs.length - 1));
          });
        } else if (e.boundingClientRect.top > 0) {
          e.target.classList.remove('lit');
        }
      });
    }, { rootMargin: '-30% 0px -45% 0px' });
    paras.forEach(function (p) { pio.observe(p); });
    if (imgs.length) imgs[0].classList.add('on');
  }

  /* ---------- CTA white takeover (reversible, trigger at 50%) ---------- */
  var cta = document.querySelector('.cta-scroll');
  if (cta) {
    var trigger = cta.querySelector('.cta-trigger');
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        cta.classList.toggle('on', en.intersectionRatio >= 0.5);
      });
    }, { threshold: [0, 0.5, 1] });
    if (trigger) tio.observe(trigger);
  }

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
      btn.textContent = 'Thank you — we’ll be in touch';
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = 'Book a consultation';
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
