# TatzMy Tattoo Studio — website

A multi-page static site for TatzMy, a custom tattoo studio in Kuala Lumpur.
Design direction modelled on the Uroki Framer template (dark editorial look,
marquee typography, pinned scroll sections) with fully original content,
copy, imagery and code.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| Work gallery | `work.html` |
| Team | `team.html` |
| Artist detail ×7 | `team/<slug>/index.html` (farid, junhao, aisyah, weiming, danial, meilin, arjun) |
| 404 | `404.html` |

## Editing content

All copy, artists, services and contact facts live at the top of
**`build.py`**. Edit the DATA block, then regenerate every page with:

```bash
python3 build.py
```

Styles: `assets/css/style.css` · Animations/interactions: `assets/js/main.js`
(no dependencies, no build tools needed).

## Signature effects (all vanilla JS/CSS)

- Intro overlay: masked logo slide-in → curtain lift (home only)
- Fixed header with `mix-blend-mode: difference` + spring drop-in
- Infinite marquees: hero title, work strip, hero mini-strip, footer wordmark
- Pinned hero — sections slide over it; fixed footer revealed at page end
- About: paragraphs light up as you scroll; ghost studio image swaps in sync
- Services: floating image on hover, text inverts via blend mode
- CTA: white full-viewport takeover while pinned (reversible on scroll)
- Team cards: name slides up from the clipped edge; team page adds a
  grayscale→colour reveal
- Booking: glass panel over grayscale video loop, colour video inside panel

## Previewing locally

Serving from `~/Desktop` can hit macOS privacy protection (server sees 404s).
Copy the folder somewhere neutral and serve it there, e.g.:

```bash
rsync -a ~/Desktop/TatzMy/ /tmp/tatzmy/ && python3 -m http.server 9310 -d /tmp/tatzmy
```

## Placeholder facts — TODO confirm before going live

- Address: 12-2, Jalan Mesui, Bukit Bintang, 50200 Kuala Lumpur
- Phone: +60 12-345 6789 · Email: hello@tatzmy.my
- Social URLs (instagram/tiktok/facebook @tatzmy)
- Founding year (2014), founder name (Farid Rahman) and all artist bios —
  the artists are fictional personas written for this mockup
- Booking form is demo-only (no backend; shows a thank-you state)

## Media

Photos and videos are free-license stock from Pexels (chosen for an
Asian/Malaysian look). Fonts: General Sans (Fontshare) + Inter — both
self-hosted in `assets/fonts/`, free licenses.
