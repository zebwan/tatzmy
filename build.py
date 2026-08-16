#!/usr/bin/env python3
"""
TATZMY Tattoo Studio — static site generator.

All page content lives in the DATA block below. Edit it, then run:
    python3 build.py
Pages are written to the folder this script lives in.
"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

# ════════════════════════════════════════════════════════════════
# DATA
# ════════════════════════════════════════════════════════════════

SITE = {
    "name": "TatzMy Tattoo Studio",
    "title": "TatzMy Tattoo Studio — Custom Tattoos in Kuala Lumpur",
    "description": "TatzMy is a custom tattoo studio in Bukit Bintang, Kuala Lumpur. Bornean tribal, oriental, fine line, realism and blackwork by Malaysia's finest artists.",
    "based": "Based in Kuala Lumpur, Malaysia",
    "quote": "Skin remembers what words forget. Every piece we make carries a story worth keeping for life.",
    # TODO-confirm facts (see README)
    "phone_display": "+60 12-345 6789",
    "phone_link": "+60123456789",
    "email": "hello@tatzmy.my",
    "instagram": "https://instagram.com/tatzmy",
    "tiktok": "https://tiktok.com/@tatzmy",
    "facebook": "https://facebook.com/tatzmy",
    "maps": "https://maps.google.com/?q=Jalan+Mesui+Bukit+Bintang+Kuala+Lumpur",
    "address_lines": ["12-2, Jalan Mesui,", "Bukit Bintang,", "50200 Kuala Lumpur"],
    "year": "2026",
}

SERVICES = [  # (name, hover image)
    ("Bornean Tribal", "work-01"), ("Oriental", "work-23"), ("Fine Line", "work-07"),
    ("Realism", "work-04"), ("Geometric", "work-09"), ("Blackwork", "work-14"),
    ("Neotraditional", "work-22"),
]

PLACEMENTS = ["Neck", "Shoulder", "Arm", "Chest", "Ribs",
              "Back", "Thigh", "Calf", "Knee", "Ankle/Foot"]

ABOUT_LEAD = ("TatzMy Tattoo Studio sits on Jalan Mesui in the heart of Bukit Bintang, "
              "inside a restored pre-war shophouse a few steps from Changkat's night crowd. "
              "Built on craft, hygiene and an easy-going welcome, it is a space where ideas "
              "take their time — and where every client leaves wearing something personal.")

ABOUT_PARAS = [
    ("TatzMy was founded in 2014 by Farid Rahman, an artist with more than fifteen years "
     "behind the machine. His insistence on doing things properly — clean lines, clean "
     "needles, honest advice — shaped a studio that clients trust with their first tattoo "
     "and their fiftieth."),
    ("We are proudly Malaysian. Our artists draw from the region's deep ink heritage — "
     "Bornean tribal work, oriental brush traditions, Peranakan motifs — and bend it into "
     "pieces that feel contemporary rather than costume."),
    ("The studio doubles as a small gallery. Flash sheets, paintings and prints by our "
     "artists and friends rotate on the walls, so the room you get tattooed in never looks "
     "quite the same twice. Drop by, flip through the books, talk to us — consultations "
     "are free and unhurried."),
]

WORK_INTRO = ("Every tattoo starts as a conversation and a pencil sketch. "
              "What leaves the studio is drawn once, for one person, and never repeated.")

SERVICES_INTRO = ("From first consultation to final touch-up, every piece is designed around "
                  "your idea, your body and your budget.")

CTA_PARA = ("Choosing TatzMy means choosing work that heals well and ages better. We use "
            "sterile single-use needles, MOH-compliant hygiene practice, premium imported "
            "inks and proper aftercare guidance with every session — first-timers welcome.")

TEAM_INTRO = ("Seven residents, seven very different styles. "
              "Meet the hands behind every custom design.")


BOOKING = {
    "label": "In addition to your consultation",
    "heading": "Our artists will sketch your idea for free",
    "sub": ("Tell us what you have in mind and we will match you with the artist "
            "who fits your style, placement and budget."),
}

ARTISTS = [
    {
        "slug": "farid", "name": "Farid",
        "full": "Farid — founder of TatzMy Studio.",
        "portrait": "portrait-farid", "objpos": "50% 30%",
        "bio": [
            "Farid — founder of TatzMy Studio.",
            "Born in Kuching and raised between Sarawak and KL, he grew up around the "
            "hand-tapped tattoo traditions of Borneo, then studied graphic design at "
            "UiTM before ink pulled him in for good.",
            "He spent nine years at a legendary Petaling Street studio before opening "
            "TatzMy in 2014, and has judged and guested at conventions across "
            "Southeast Asia.",
            "He specialises in Bornean tribal and oriental work, and takes on the "
            "cover-ups other studios turn away.",
            "Off the clock you'll find him restoring old motorcycles and painting.",
        ],
        "gallery": ["work-01", "work-23", "work-10", "work-17"],
    },
    {
        "slug": "junhao", "name": "Jun Hao",
        "full": "Jun Hao — fine line specialist.",
        "portrait": "portrait-junhao", "objpos": "50% 28%",
        "bio": [
            "Jun Hao — fine line and micro-realism specialist.",
            "A Penang boy with an illustration background from The One Academy, he "
            "apprenticed in Georgetown before joining TatzMy in 2018.",
            "His single-needle botanical and script work has a quiet following on "
            "Instagram — expect a waiting list for his flash days.",
            "When he isn't tattooing he is sketching kopitiam scenes in fountain pen.",
        ],
        "gallery": ["work-03", "work-07", "work-24", "work-05"],
    },
    {
        "slug": "aisyah", "name": "Aisyah",
        "full": "Aisyah — blackwork artist.",
        "portrait": "portrait-aisyah", "objpos": "50% 25%",
        "bio": [
            "Aisyah — blackwork and dotwork artist.",
            "From Johor Bahru, self-taught through years of stick-and-poke practice "
            "before formal apprenticeship at TatzMy.",
            "Her heavy ornamental blackwork borrows from songket weave patterns and "
            "Islamic geometry — bold from across the room, intricate up close.",
            "She runs the studio's monthly beginner-friendly flash events.",
        ],
        "gallery": ["work-11", "work-12", "work-13", "work-14"],
    },
    {
        "slug": "weiming", "name": "Wei Ming",
        "full": "Wei Ming — realism artist.",
        "portrait": "portrait-weiming", "objpos": "50% 30%",
        "bio": [
            "Wei Ming — black-and-grey realism artist.",
            "Ipoh-born, he painted portraits for a living before switching to skin "
            "in 2016 — and it shows in his smooth graywash and patient shading.",
            "Pet portraits, family tributes and film stills are his bread and "
            "butter; large-scale sleeves are his favourite challenge.",
            "He is the quiet one in the studio. His clients usually fall asleep.",
        ],
        "gallery": ["work-02", "work-04", "work-06", "work-18"],
    },
    {
        "slug": "danial", "name": "Danial",
        "full": "Danial — geometric artist.",
        "portrait": "portrait-danial", "objpos": "50% 35%",
        "bio": [
            "Danial — geometric and abstract specialist.",
            "A former architecture student from Shah Alam who traded CAD for a "
            "rotary machine, he builds precise linework compositions that flow "
            "with the body's own lines.",
            "Sacred geometry, glitch patterns and negative-space experiments — "
            "bring him something strange and he will make it stranger.",
        ],
        "gallery": ["work-08", "work-09", "work-16", "work-15"],
    },
    {
        "slug": "meilin", "name": "Mei Lin",
        "full": "Mei Lin — neotraditional artist.",
        "portrait": "portrait-meilin", "objpos": "50% 40%",
        "bio": [
            "Mei Lin — neotraditional and colour specialist.",
            "KL-raised with a fashion-illustration diploma, she joined TatzMy in "
            "2019 after guesting across Bangkok and Taipei.",
            "Her saturated florals, koi and opera-mask pieces mix classic "
            "neotraditional weight with Chinese folk-art colour palettes.",
            "Ask her about matching pieces — she loves designing for pairs.",
        ],
        "gallery": ["work-22", "work-25", "work-26", "work-27"],
    },
    {
        "slug": "arjun", "name": "Arjun",
        "full": "Arjun — script and sketch artist.",
        "portrait": "portrait-arjun", "objpos": "50% 25%",
        "bio": [
            "Arjun — script, sketch-style and freehand artist.",
            "From Brickfields, he started as a signboard painter's apprentice and "
            "still hand-letters everything before it touches skin.",
            "Tamil, Jawi and Latin calligraphy, loose sketch-style portraits and "
            "freehand brush strokes are his signatures.",
            "He keeps a wall of rejected fonts he calls 'the graveyard'. Do not "
            "ask for those.",
        ],
        "gallery": ["work-19", "work-20", "work-21", "work-28"],
    },
]

# home hero mini-marquee + work strip + work page grid
HERO_STRIP = ["work-01", "work-23", "work-11", "work-22"]
WORK_STRIP = ["work-01", "work-02", "work-03", "work-11", "work-22",
              "work-05", "work-12", "work-08", "work-25", "work-20"]
WORK_PAGE = [  # (image, artist name) — first 6 visible, rest behind Load More
    ("work-01", "Farid"), ("work-03", "Jun Hao"), ("work-11", "Aisyah"),
    ("work-02", "Wei Ming"), ("work-08", "Danial"), ("work-22", "Mei Lin"),
    ("work-19", "Arjun"), ("work-23", "Farid"), ("work-13", "Aisyah"),
]

ABOUT_STICKY_IMGS = ["studio-neon", "studio-session", "studio-wide"]

# ════════════════════════════════════════════════════════════════
# SHARED PARTIALS
# ════════════════════════════════════════════════════════════════

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
         'stroke-linecap="round" stroke-linejoin="round" class="{cls}">'
         '<path d="M17.25 15.25 L17.25 6.75 L8.75 6.75"/>'
         '<path d="M17 7 L6.75 17.25"/></svg>')

def arrow(cls=""):
    return ARROW.format(cls=cls)

def e(s):
    return html.escape(s, quote=False)

def logo(r, cls=""):
    return (f'<a href="{r}index.html" class="logo {cls}" aria-label="TatzMy home">'
            f'<span class="word">Tatzmy</span><span class="sub">Tattoo Studio</span></a>')

def pill(href, label, icon=True):
    ico = f'<span class="ico">{arrow("a1")}{arrow("a2")}</span>' if icon else ''
    return (f'<a href="{href}" class="btn-pill t-label"><span class="txt">{e(label)}</span>{ico}</a>')

def sec_head(label, sub):
    return (f'<div class="sec-head appear"><div class="lbl-row"><h2 class="t-body">{e(label)}</h2></div>'
            f'<div class="sub-row"><p class="t-sub sub">{e(sub)}</p></div></div>')

def nav_link(href, label, current=False):
    cur = ' aria-current="page"' if current else ''
    return (f'<a href="{href}" class="nav-link"{cur}><p class="t-label">{e(label)}</p>'
            f'<span class="dash"></span></a>')

def header(r, page):
    links = [
        (f"{r}index.html", "Home", page == "home"),
        (f"{r}index.html#about-section", "About", False),
        (f"{r}work.html", "Work", page == "work"),
        (f"{r}index.html#services-section", "Services", False),
        (f"{r}team.html", "Team", page in ("team", "artist")),
    ]
    nav = "".join(nav_link(h, l, c) for h, l, c in links)
    mob_nav = "".join(f'<a class="big" href="{h}">{e(l)}</a>' for h, l, _ in links)
    return f'''
<header class="site-header">
  <div class="bar"><div class="container">
    {logo(r)}
    <div class="header-right">
      <nav class="nav-links" aria-label="Main">{nav}</nav>
      {pill(f"{r}index.html#book-consultation", "Book a consultation")}
    </div>
    <button class="burger" aria-label="Menu"><span class="l1"></span><span class="l2"></span><span class="l3"></span></button>
  </div></div>
</header>
<div class="mobile-menu">
  <div>
    <div class="group"><p class="t-meta">Menu</p>{mob_nav}</div>
    <div class="group"><p class="t-meta">Social</p>
      <a class="big" href="{SITE["instagram"]}" target="_blank" rel="noopener">Instagram</a>
      <a class="big" href="{SITE["tiktok"]}" target="_blank" rel="noopener">TikTok</a>
      <a class="big" href="{SITE["facebook"]}" target="_blank" rel="noopener">Facebook</a>
    </div>
  </div>
  {pill(f"{r}index.html#book-consultation", "Book a consultation")}
</div>'''

def foot_link(href, label, ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a href="{href}" class="t-label underline-link"{x}>{e(label)}</a>'

def footer(r):
    addr = "<br>".join(e(x) for x in SITE["address_lines"])
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-cols">
      <div class="footer-col"><p class="t-meta">Navigation</p><div class="links">
        {foot_link(f"{r}index.html", "Home")}
        {foot_link(f"{r}index.html#about-section", "About")}
        {foot_link(f"{r}work.html", "Work")}
        {foot_link(f"{r}index.html#services-section", "Services")}
        {foot_link(f"{r}team.html", "Team")}
        {foot_link(f"{r}404.html", "404")}
      </div></div>
      <div class="footer-col"><p class="t-meta">Social media</p><div class="links">
        {foot_link(SITE["instagram"], "Instagram", True)}
        {foot_link(SITE["tiktok"], "TikTok", True)}
        {foot_link(SITE["facebook"], "Facebook", True)}
      </div></div>
      <div class="footer-col"><p class="t-meta">Contact</p><div class="links">
        {foot_link("mailto:" + SITE["email"], SITE["email"])}
        {foot_link("tel:" + SITE["phone_link"], SITE["phone_display"])}
        {foot_link(SITE["maps"], "Find the studio", True)}
      </div></div>
      <div class="footer-col"><p class="t-meta">Take a seat</p>
        {pill(f"{r}index.html#book-consultation", "Book a consultation")}
      </div>
    </div>
    <div class="footer-logo-ticker ticker" data-marquee data-speed="70">
      <div class="track"><h1 class="t-display">Tatzmy&ensp;tattoo&ensp;studio&ensp;—&ensp;</h1></div>
    </div>
    <div class="footer-meta">
      <div class="col"><p class="t-meta">Tatzmy {SITE["year"]}&copy;</p><p class="t-meta">All rights reserved</p></div>
      <div class="col"><p class="t-meta">Custom tattoos&nbsp;&middot;&nbsp;Walk-ins by luck, bookings by design</p></div>
      <p class="t-meta addr">{addr}</p>
    </div>
  </div>
</footer>'''

def booking_section(r, section_id="book-consultation"):
    services = "".join(f"<option>{e(s)}</option>" for s, _ in SERVICES)
    artists = "".join(f"<option>{e(a['name'])}</option>" for a in ARTISTS)
    chips = "".join(
        f'<label class="t-label"><input type="checkbox" name="placement" value="{e(p)}">{e(p)}</label>'
        for p in PLACEMENTS)
    return f'''
<section class="section booking" id="{section_id}">
  <div class="bgvid"><video autoplay muted loop playsinline src="{r}assets/video/booking.mp4"></video></div>
  <div class="panel">
    <div class="content">
      <video autoplay muted loop playsinline src="{r}assets/video/booking.mp4"></video>
      <div class="txt">
        <p class="t-label">{e(BOOKING["label"])}</p>
        <div class="bottom">
          <p class="t-sub">{e(BOOKING["heading"])}</p>
          <p class="t-label">{e(BOOKING["sub"])}</p>
        </div>
      </div>
    </div>
    <form novalidate>
      <div class="fld"><label class="t-label" for="f-name">Full name</label>
        <input id="f-name" type="text" name="name" required></div>
      <div class="row2">
        <div class="fld"><label class="t-label" for="f-email">Email</label>
          <input id="f-email" type="email" name="email" required></div>
        <div class="fld"><label class="t-label" for="f-phone">Phone</label>
          <input id="f-phone" type="tel" name="phone" required></div>
      </div>
      <div class="row2">
        <div class="fld"><label class="t-label" for="f-service">Service</label>
          <select id="f-service" name="service" required>
            <option value="" disabled selected>Select…</option>{services}
          </select></div>
        <div class="fld"><label class="t-label" for="f-artist">Artist</label>
          <select id="f-artist" name="artist">
            <option value="" disabled selected>Select…</option>{artists}
          </select></div>
      </div>
      <div class="fld"><span class="t-label">Placement of tattoo</span>
        <div class="chips">{chips}</div></div>
      <div class="fld"><label class="t-label" for="f-idea">Describe your idea (optional)</label>
        <textarea id="f-idea" name="idea"></textarea></div>
      <div class="hp" aria-hidden="true"><input type="text" name="website" tabindex="-1" autocomplete="off"></div>
      <button type="submit" class="t-label">Book a consultation</button>
    </form>
  </div>
</section>'''

def team_card(r, a, cls=""):
    return f'''<a href="{r}team/{a["slug"]}/index.html" class="team-card {cls}">
  <span class="ph"><img src="{r}assets/img/{a["portrait"]}.jpg" alt="{e(a["name"])} — tattoo artist at TatzMy" style="object-position:{a["objpos"]}" loading="lazy"></span>
  <span class="nm"><p class="t-label">{e(a["name"])}</p>{arrow()}</span>
</a>'''

def page(path, title, desc, body, r, page_key, extra_head=""):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='black'/><text x='16' y='22' font-family='Arial' font-size='14' font-weight='bold' fill='white' text-anchor='middle'>TZ</text></svg>">
<link rel="stylesheet" href="{r}assets/css/style.css">{extra_head}
</head>
<body>
{header(r, page_key)}
<div class="page">
{body}
</div>
{footer(r)}
<script src="{r}assets/js/main.js"></script>
</body>
</html>'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", path)

# ════════════════════════════════════════════════════════════════
# PAGES
# ════════════════════════════════════════════════════════════════

def build_home():
    r = ""
    strip = "".join(f'<img src="assets/img/{i}.jpg" alt="Tattoo work by TatzMy artists">' for i in HERO_STRIP)
    work_strip = "".join(
        f'<figure><img src="assets/img/{i}.jpg" alt="Custom tattoo by TatzMy" loading="lazy"></figure>'
        for i in WORK_STRIP)
    about_paras = "".join(f'<p class="t-body">{e(p)}</p>' for p in ABOUT_PARAS)
    sticky_imgs = "".join(
        f'<img src="assets/img/{i}.jpg" alt="Inside TatzMy studio" loading="lazy">'
        for i in ABOUT_STICKY_IMGS)
    services = "".join(
        f'<div class="service-row"><span class="name">{e(s)}</span>'
        f'<img class="hover-img" src="assets/img/{img}.jpg" alt="" loading="lazy"></div>'
        for s, img in SERVICES)
    team_cards = "".join(team_card(r, a) for a in ARTISTS[:4])

    body = f'''
<div class="intro" aria-hidden="true">
  <div class="curtain"></div>
  <div class="logo-window"><div class="logo-slide">
    <span class="logo"><span class="word">Tatzmy</span><span class="sub">Tattoo Studio</span></span>
  </div></div>
</div>

<header class="hero">
  <div class="container">
    <div class="top-block">
      <div class="top-row">
        <div class="socials">
          <a class="t-label underline-link" href="{SITE["instagram"]}" target="_blank" rel="noopener">Instagram</a>
          <a class="t-label underline-link" href="{SITE["tiktok"]}" target="_blank" rel="noopener">TikTok</a>
          <a class="t-label underline-link" href="tel:{SITE["phone_link"]}">{e(SITE["phone_display"])}</a>
        </div>
        <p class="quote t-label">{e(SITE["quote"])}</p>
      </div>
      <div class="hero-title ticker" data-marquee data-speed="60">
        <div class="track"><h1 class="t-display">Tatzmy&ensp;tattoo&ensp;studio&ensp;&ensp;</h1></div>
      </div>
    </div>
    <div class="hero-photo"><img src="assets/img/hero-cutout.webp" alt="Full back-piece tattoo by TatzMy Tattoo Studio"></div>
    <div class="bottom-row">
      <p class="based t-body">{e(SITE["based"])}</p>
      <div class="see-work">
        <a href="work.html" class="lbl t-label">See work {arrow()}</a>
        <div class="mini-marquee ticker" data-marquee data-speed="40">
          <div class="track">{strip}</div>
        </div>
      </div>
    </div>
  </div>
</header>

<section class="section about-lead" id="about-section">
  <div class="inner">
    {sec_head("About", ABOUT_LEAD)}
  </div>
</section>

<section class="section about-2">
  <div class="inner">
    <div class="text-col">{about_paras}</div>
    <div class="img-col"><div class="img-sticky"><div class="frame">{sticky_imgs}</div></div></div>
  </div>
</section>

<section class="section work-strip">
  <div class="inner">
    {sec_head("Work", WORK_INTRO)}
  </div>
  <div class="strip-ticker ticker" data-marquee data-speed="80" data-pause>
    <div class="track">{work_strip}</div>
  </div>
  <div class="center-cta appear">{pill("work.html", "See all works", icon=False)}</div>
</section>

<section class="section" id="services-section">
  <div class="inner">
    {sec_head("Services", SERVICES_INTRO)}
    <div class="services-stack appear">{services}</div>
  </div>
</section>

<section class="cta-scroll">
  <div class="pin">
    <div class="whiteframe"></div>
    <div class="frame">
      <p class="t-sub">{e(CTA_PARA)}</p>
      {pill("index.html#book-consultation", "Book a consultation")}
    </div>
  </div>
  <div class="cta-trigger"></div>
</section>

<section class="section sec-white" style="padding-bottom:140px">
  <div class="inner">
    {sec_head("Our team", TEAM_INTRO)}
    <div class="team-home-grid appear">{team_cards}</div>
    <div class="center-cta appear">{pill("team.html", "View all", icon=False)}</div>
  </div>
</section>

{booking_section(r)}
'''
    page("index.html", SITE["title"], SITE["description"], body, r, "home")

def build_work():
    r = ""
    cards = ""
    for i, (img, artist) in enumerate(WORK_PAGE):
        hide = ' data-more hidden' if i >= 6 else ''
        cards += (f'<div class="work-card"{hide}><img src="assets/img/{img}.jpg" '
                  f'alt="Tattoo by {e(artist)}" loading="lazy">'
                  f'<p class="who t-label">Artist — {e(artist)}</p></div>')
    body = f'''
<section class="page-hero"><h2 class="t-hero">Work</h2></section>
<section class="section" style="padding-top:0">
  <div class="inner">
    <div class="work-grid">{cards}</div>
    <div class="center-cta"><button class="btn-pill t-label" id="load-more" style="border:0;background:none;cursor:pointer">
      <span class="txt">Load more</span></button></div>
  </div>
</section>
{booking_section(r)}
<script>
document.getElementById('load-more').addEventListener('click', function () {{
  document.querySelectorAll('[data-more]').forEach(function (n) {{ n.hidden = false; }});
  this.remove();
}});
</script>'''
    page("work.html", "Work — " + SITE["name"],
         "Selected tattoo work from the TatzMy studio in Kuala Lumpur.",
         body, r, "work")

def build_team():
    r = ""
    cards = "".join(team_card(r, a) for a in ARTISTS)
    body = f'''
<section class="page-hero"><h2 class="t-hero">Team</h2></section>
<section class="section" style="padding-top:0">
  <div class="inner"><div class="team-grid">{cards}</div></div>
</section>
{booking_section(r)}'''
    page("team.html", "Team — " + SITE["name"],
         "Meet the seven resident artists of TatzMy Tattoo Studio, Kuala Lumpur.",
         body, r, "team")

def build_artists():
    r = "../../"
    for i, a in enumerate(ARTISTS):
        prev_a = ARTISTS[i - 1] if i > 0 else None
        next_a = ARTISTS[i + 1] if i < len(ARTISTS) - 1 else None
        bio = "".join(f'<p class="t-body">{e(p)}</p>' for p in a["bio"])
        gal = "".join(
            f'<figure><img src="{r}assets/img/{g}.jpg" alt="Tattoo by {e(a["name"])}" loading="lazy"></figure>'
            for g in a["gallery"])
        prev_html = (f'<p class="t-body"><a class="underline-link" href="../{prev_a["slug"]}/index.html">&lsaquo; {e(prev_a["name"])}</a></p>'
                     if prev_a else '<span></span>')
        next_html = (f'<p class="t-body"><a class="underline-link" href="../{next_a["slug"]}/index.html">{e(next_a["name"])} &rsaquo;</a></p>'
                     if next_a else '<span></span>')
        body = f'''
<section class="page-hero"><h2 class="t-hero">{e(a["name"])}</h2></section>
<section class="section artist-about" style="padding-top:0">
  <div class="inner">
    <div class="brief">
      <div class="bio">{bio}</div>
      <div class="cta-row">
        {pill("index.html#team-booking", "Book " + a["name"])}
        <a class="t-label underline-link" href="{SITE["instagram"]}" target="_blank" rel="noopener">Instagram</a>
      </div>
    </div>
    <figure><img src="{r}assets/img/{a["portrait"]}.jpg" alt="{e(a["name"])} — tattoo artist" style="object-position:{a["objpos"]}"></figure>
  </div>
</section>
<section class="section artist-work">
  <div class="inner">
    <h2 class="t-section" style="text-align:center">Work</h2>
    <div class="artist-grid">{gal}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="prevnext">{prev_html}{next_html}</div>
</section>
{booking_section(r, "team-booking")}'''
        page(f"team/{a['slug']}/index.html",
             f"{a['name'].upper()} — {SITE['name']}",
             f"{a['full']} Custom tattoos at TatzMy Studio, Kuala Lumpur.",
             body, r, "artist")

def build_404():
    r = ""
    body = f'''
<section class="notfound">
  <h2 class="t-hero" style="font-size:120px">404</h2>
  <p class="t-body">This page has faded like cheap ink. Let's get you back.</p>
  {pill("index.html", "Back to home")}
</section>'''
    page("404.html", "Page not found — " + SITE["name"],
         "Page not found.", body, r, "404")

if __name__ == "__main__":
    build_home()
    build_work()
    build_team()
    build_artists()
    build_404()
    print("done.")
