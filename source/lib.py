import json, html, os, re
SITE = '/home/claude/site'
MANIFEST = json.load(open('/home/claude/img_manifest.json'))
USED_IMAGES = set()

def esc(s):
    return html.escape(str(s), quote=True)

# ---------------- links ----------------
EXT_RE = re.compile(r'^(https?:|mailto:|tel:)')
def is_ext(href):
    return bool(EXT_RE.match(href))

def a(label, href, cls='', ext=None, attrs=''):
    ext = is_ext(href) if ext is None else ext
    t = ' target="_blank" rel="noopener"' if ext and href.startswith('http') else ''
    c = f' class="{cls}"' if cls else ''
    return f'<a href="{esc(href)}"{c}{t}{attrs}>{label}</a>'

def btn(label, href, kind='', size='', ext=None, arrow=False, attrs=''):
    ext = is_ext(href) if ext is None else ext
    cls = 'btn' + (f' btn--{kind}' if kind else '') + (f' btn--{size}' if size else '')
    inner = esc(label) if '<' not in label else label
    if ext and href.startswith('http'):
        inner += '<span aria-hidden="true">&nbsp;&#8599;</span>'
    elif arrow:
        inner += '<span class="arr" aria-hidden="true">&rarr;</span>'
    return a(inner, href, cls, ext, attrs)

# ---------------- images ----------------
def img(name, alt='', cls='', loading='lazy', style='', sizes=''):
    if name.startswith('http') or name.endswith('.svg'):
        src = name if name.startswith('http') else f'assets/img/{name}'
        return f'<img src="{src}" alt="{esc(alt)}"' + (f' class="{cls}"' if cls else '') + f' loading="{loading}" decoding="async">'
    m = MANIFEST.get(name)
    if not m:
        if os.path.exists(f'{SITE}/assets/img/{name}.webp'):
            from PIL import Image
            im = Image.open(f'{SITE}/assets/img/{name}.webp'); m = {'w': im.width, 'h': im.height}
            MANIFEST[name] = m
        else:
            raise KeyError('missing image ' + name)
    USED_IMAGES.add(name)
    st = f' style="{style}"' if style else ''
    return (f'<img src="assets/img/{name}.webp" width="{m["w"]}" height="{m["h"]}" alt="{esc(alt)}"'
            + (f' class="{cls}"' if cls else '') + f' loading="{loading}" decoding="async"{st}>')

def imgsrc(name):
    USED_IMAGES.add(name)
    return f'assets/img/{name}.webp'

# ---------------- icons (geometric only) ----------------
ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>'

LOGO_SVG = open(f'{SITE}/assets/img/logo.svg').read().replace('<svg ', '<svg role="img" aria-label="SafeBAE" ', 1)

def daisy(cls=''):
    return f'<span class="daisy {cls}" aria-hidden="true"></span>'

# ---------------- media facades ----------------
def yt(vid, title, thumb=None, label='Watch', cls='', start=None):
    thumb = thumb or 'yt-' + re.sub(r'[^a-z0-9]+', '-', vid.lower()).strip('-')
    url = f'https://www.youtube.com/watch?v={vid}' + (f'&t={start}s' if start else '')
    s = f' data-start="{start}"' if start else ''
    return (f'<a class="vid {cls}" href="{url}" target="_blank" rel="noopener" data-yt="{vid}"{s} aria-label="Play video: {esc(title)}">'
            f'{img(thumb, "")}<span class="vid__play"><span>{ICON_PLAY}</span></span>'
            f'<span class="vid__label"><span>{esc(title)}</span><small>{esc(label)}</small></span></a>')

def spotify(eid, title, show, thumb=None, kind='episode'):
    thumb = thumb or 'sp-' + eid.lower()
    return (f'<a class="audio" href="https://open.spotify.com/{kind}/{eid}" target="_blank" rel="noopener" data-spotify="{kind}/{eid}" aria-label="Listen: {esc(title)}">'
            f'{img(thumb, "")}<span><b>{esc(title)}</b><small>{esc(show)}</small></span><span class="playdot">{ICON_PLAY}</span></a>')

def embed(src, link, label, height=720, title='Embedded form', cta='Open the form'):
    """Iframe that only loads on a real website; elsewhere shows a link."""
    return (f'<div class="embed" data-embed="{esc(src)}" data-h="{height}" data-title="{esc(title)}">'
            f'<div class="embed__fallback note"><p><b>{esc(label)}</b></p>{btn(cta, link, "teal")}</div></div>')

# ---------------- chips ----------------
def chips(items, kind=''):
    return '<div class="chips">' + ''.join(f'<span class="chip{(" chip--"+kind) if kind else ""}">{esc(i)}</span>' for i in items) + '</div>'

def eyebrow(text, d=False):
    return f'<p class="eyebrow">{daisy() if d else ""}{text}</p>'

# ---------------- navigation ----------------
NAV = [
  ('About', 'about', 'safebae-executive-director-shael-norris', 'Founded by teen survivors in 2015', 'about.html', [
     ('About SafeBAE', 'about.html', 'Our mission, our story and how we began'),
     ('Our Team', 'team.html', 'Staff, youth media team and our board'),
     ('Data & Impact', 'impact.html', 'Published research, surveys and reports'),
     ('Partners & Press', 'partners-press.html', 'Podcasts, partner films and media'),
     ('#ForDaisy', 'fordaisy.html', 'Remembering co-founder Daisy Coleman'),
     ('Contact', 'contact.html', 'Reach the SafeBAE team'),
  ]),
  ('Students', 'students', 'clubhero', 'Start a SafeBAE club at your school', 'clubs.html', [
     ('For Students', 'students.html', 'Everything for high school students'),
     ('Peer Educator Training', 'peer-educator.html', 'Free, self-paced, 16 modules'),
     ('SafeBAE Clubs', 'clubs.html', 'Start, affiliate or restart a chapter'),
     ('Reform Your School’s Policy', 'reform-policy.html', 'A student guide to stronger policies'),
     ('Summer Activist Institute', 'summer-institute.html', 'Meet the fellows'),
     ('En Español', 'espanol.html', 'Entrenamiento en español'),
  ]),
  ('Adults', 'adults', 'us-sometale-parent', 'Tools for parents and caregivers', 'parents.html', [
     ('For Adults', 'adults.html', 'Start here if you support young people'),
     ('Parents & Caregivers', 'parents.html', 'Conversations, support and next steps'),
     ('Educators', 'educators.html', 'Classroom tools at every level of use'),
     ('College Students', 'college.html', 'Mentor high schoolers, start a campus club'),
     ('Request a Program', 'request-a-program.html', 'Bring SafeBAE to your community'),
  ]),
  ('360° Schools', 'schools', '066', 'A whole-school prevention model', '360-schools.html', [
     ('SafeBAE 360° Schools', '360-schools.html', 'Six components, adapted to your school'),
     ('Consent Curriculum', 'consent-curriculum.html', '15 lessons aligned to NHES'),
     ('Faculty & Staff Training', 'professional-development.html', 'Trauma-informed professional development'),
     ('Policy Reform Guide', 'policy-reform-guide.html', 'For administrators and districts'),
     ('Accountability Training', 'accountability-training.html', 'For students who have caused harm'),
     ('Request a Program', 'request-a-program.html', 'Assemblies, trainings and pricing'),
  ]),
  ('Library', 'library', 'gameon8', '12 films, 17 podcasts, 8 teaching guides', 'library.html', [
     ('The Library', 'library.html', 'Search every film, podcast and guide'),
     ('Films & videos', 'library.html#films', 'Youth-made films with lesson plans'),
     ('Podcasts', 'library.html#podcasts', 'Conversations with SafeBAE leaders'),
     ('Teaching guides', 'library.html#guides', 'Ready-to-teach discussion guides'),
     ('Race, Rape Culture & Resistance', 'film-race-rape-culture-resistance.html', 'A four-lesson learning series'),
     ('Posters', 'posters.html', 'Free downloadable prevention posters'),
  ]),
  ('Resources', 'resources', 'yt-ng8s3w1etru', 'Vibe Check: no judgment, just answers', 'vibe-check.html', [
     ('Resources Hub', 'resources.html', 'Every SafeBAE resource, sorted'),
     ('Vibe Check', 'vibe-check.html', 'Anonymous reflection tool'),
     ('Survivor Support', 'survivor-support.html', 'Hotlines, healing and how to help'),
     ('Title IX', 'title-ix.html', 'Your rights at school'),
     ('Myths & Facts', 'myths-facts.html', 'What the research actually says'),
     ('FAQ', 'faq.html', 'Straight answers to common questions'),
     ('BAE Skills Lab', 'https://skills-lab.safebae.org/', 'Interactive consent activities'),
     ('Blog', 'blog.html', 'Stories, analysis and news'),
  ]),
]

def header(active=''):
    items = []
    for label, key, fimg, ftxt, fhref, links in NAV:
        cur = ' aria-current="true"' if key == active else ''
        lks = ''.join(
            f'<a href="{esc(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') +
            f'><span>{esc(t)}{" &#8599;" if h.startswith("http") else ""}</span><small>{esc(d)}</small></a>' for t, h, d in links)
        items.append(
            f'<div class="nav__item"><button class="nav__top" aria-expanded="false"{cur}>{esc(label)}<span class="caret" aria-hidden="true"></span></button>'
            f'<div class="mega"><div class="mega__links">{lks}</div>'
            f'<a class="mega__feature" href="{fhref}">{img(fimg, "")}<em>Featured</em><b>{esc(ftxt)}</b></a></div></div>')
    drawer = ''.join(
        f'<details><summary>{esc(label)}</summary>' + ''.join(
            f'<a href="{esc(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'>{esc(t)}</a>' for t, h, d in links) + '</details>'
        for label, key, fimg, ftxt, fhref, links in NAV)
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="utility">
  <div class="wrap">
    <div class="utility__help"><span>Need to talk to someone?</span> <span><strong>Text LOVEIS</strong> to 22522</span> <span class="hide-sm"><strong>Call</strong> 800-656-HOPE (4673)</span> <button class="linkish" data-open-help style="background:none;border:0;color:var(--mint);font:inherit;font-weight:700;cursor:pointer;padding:0">All hotlines</button></div>
    <div class="utility__right"><a href="contact.html" class="hide-sm">Contact</a><button class="quick-exit" data-quick-exit title="Leave this site quickly (press Esc twice)">Quick exit <kbd>Esc Esc</kbd></button></div>
  </div>
</div>
<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="SafeBAE home">{LOGO_SVG}</a>
    <nav class="nav" aria-label="Main">{''.join(items)}</nav>
    <div class="header-actions">
      <button class="icon-btn" data-open-search aria-label="Search the site">{ICON_SEARCH}<kbd>&#8984;K</kbd></button>
      <button class="icon-btn help-btn" data-open-help><span class="daisy" aria-hidden="true" style="width:1.1em;height:1.1em"></span><span class="lbl">Get help</span></button>
      {btn('Donate', 'donate.html', 'mint', 'sm')}
      <button class="icon-btn menu-btn" data-open-menu aria-label="Open menu">{ICON_MENU}</button>
    </div>
  </div>
</header>
<div class="drawer" id="menu" aria-hidden="true">
  <div class="drawer__scrim" data-close></div>
  <div class="drawer__panel" role="dialog" aria-label="Menu">
    <div class="drawer__head"><span style="width:120px;color:var(--mint);display:block">{LOGO_SVG}</span><button class="close-x" data-close aria-label="Close menu">&times;</button></div>
    <a class="solo" href="index.html">Home</a>
    {drawer}
    <a class="solo" href="contact.html">Contact</a>
    <div class="btns">{btn('Donate', 'donate.html', 'mint')}<button class="btn btn--coral" data-open-help>Get help now</button></div>
  </div>
</div>'''

HOTLINES = [
  ('love is respect', 'National Teen Dating Abuse Helpline', 'Text LOVEIS to 22522 · Call 1-866-331-9474', 'Free, confidential 24/7 peer support for teens experiencing dating abuse.', 'https://www.loveisrespect.org'),
  ('RAINN', 'National Sexual Assault Hotline', 'Call 800-656-HOPE (4673) · Text HOPE to 64673', 'Free, confidential 24/7 support for survivors and their loved ones.', 'https://rainn.org/help-and-healing/hotline/'),
  ('988 Suicide & Crisis Lifeline', '24/7 suicide & crisis support', 'Call or text 988', 'For anyone in suicidal crisis or emotional distress. Chat at 988lifeline.org.', 'https://988lifeline.org'),
  ('Trevor Lifeline', 'Crisis support for LGBTQ+ youth', 'Text START to 678-678 · Call 1-866-488-7386', '24/7 crisis counseling from The Trevor Project.', 'https://www.thetrevorproject.org/get-help/'),
  ('Crisis Text Line', 'Free 24/7 crisis counseling', 'Text HOME to 741741 · Text HOLA (Español)', 'Text with a live crisis counselor about anything.', 'https://www.crisistextline.org/'),
  ('Take Back The Night', 'Free legal hotline', 'Call 567-742-8837 (567-SHATTER)', 'Free legal assistance for survivors.', 'https://takebackthenight.org/legal-assistance/'),
  ('SAMHSA National Helpline', 'Mental health & substance use', 'Call 1-800-662-HELP (4357)', 'Free, confidential treatment referrals in English and Spanish.', 'https://www.samhsa.gov/find-help/helplines/national-helpline'),
  ('Raliance', 'Local rape crisis center directory', 'Find the center nearest you', 'A national directory of local rape crisis centers.', 'https://www.raliance.org/rape-crisis-centers/'),
]

def help_drawer():
    rows = ''.join(f'<div class="hotline"><b>{esc(n)}</b><small>{esc(s)}</small><span class="num">{esc(num)}</span><small>{esc(d)} {a("Visit site", u, "link")}</small></div>' for n, s, num, d, u in HOTLINES)
    return f'''
<div class="help" id="help" aria-hidden="true">
  <div class="drawer__scrim" data-close></div>
  <div class="help__panel" role="dialog" aria-label="Get help now">
    <div class="drawer__head"><p class="eyebrow" style="margin:0;color:var(--coral)">Get help now</p><button class="close-x" data-close aria-label="Close">&times;</button></div>
    <h2>You don’t have to figure this out alone.</h2>
    <p class="muted">These services are free and confidential, and most are open 24/7. If you are in immediate danger, call 911.</p>
    {rows}
    <div class="note" style="margin-top:18px"><b>Worried you crossed a line?</b><br><span class="muted">Vibe Check is a free, anonymous reflection tool. Nothing is stored or reported.</span><div class="btns" style="margin-top:12px">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'teal', 'sm')}</div></div>
    <p class="small muted" style="margin-top:18px">Press <span class="kbd">Esc</span> twice anywhere on this site to leave quickly.</p>
  </div>
</div>'''

def palette():
    return f'''
<div class="palette" id="palette" aria-hidden="true">
  <div class="palette__box" role="dialog" aria-label="Search SafeBAE">
    <div class="palette__input">{ICON_SEARCH}<input id="palette-q" type="search" placeholder="Search films, podcasts, guides, pages, answers…" autocomplete="off" aria-label="Search"><button class="close-x" data-close aria-label="Close search" style="width:34px;height:34px;font-size:1rem">&times;</button></div>
    <div class="palette__list" id="palette-list" role="listbox"></div>
    <div class="palette__foot"><span><kbd>&uarr;</kbd> <kbd>&darr;</kbd> to move</span><span><kbd>Enter</kbd> to open</span><span><kbd>Esc</kbd> to close</span></div>
  </div>
</div>
<div class="lightbox" id="lightbox" aria-hidden="true"><button class="close-x" data-close aria-label="Close">&times;</button><button class="lightbox__nav lightbox__prev" aria-label="Previous">&#8249;</button><img alt=""><button class="lightbox__nav lightbox__next" aria-label="Next">&#8250;</button><p class="lightbox__cap"></p></div>'''

FOOT_COLS = [
  ('About', [('About SafeBAE','about.html'),('Our Team','team.html'),('Data & Impact','impact.html'),('Partners & Press','partners-press.html'),('#ForDaisy','fordaisy.html'),('Contact','contact.html')]),
  ('Students', [('For Students','students.html'),('Peer Educator Training','peer-educator.html'),('SafeBAE Clubs','clubs.html'),('Club Hub','https://clubs.safebae.org'),('Summer Activist Institute','summer-institute.html'),('Reform Your Policy','reform-policy.html'),('En Español','espanol.html')]),
  ('Adults & Schools', [('For Adults','adults.html'),('Parents & Caregivers','parents.html'),('Educators','educators.html'),('College Students','college.html'),('360° Schools','360-schools.html'),('Request a Program','request-a-program.html')]),
  ('Resources', [('The Library','library.html'),('Resources Hub','resources.html'),('Vibe Check','vibe-check.html'),('BAE Skills Lab','https://skills-lab.safebae.org/'),('Survivor Support','survivor-support.html'),('Title IX','title-ix.html'),('Myths & Facts','myths-facts.html'),('FAQ','faq.html'),('Posters','posters.html'),('Blog','blog.html')]),
]

def footer():
    cols = ''.join(f'<div><h4>{esc(t)}</h4><ul>' + ''.join(f'<li>{a(esc(l), h, "ext" if h.startswith("http") else "")}</li>' for l, h in links) + '</ul></div>' for t, links in FOOT_COLS)
    return f'''
<section class="support-strip" aria-label="Support resources">
  <div class="wrap">
    <b>Need support right now?</b>
    <div class="nums"><span>Text <strong>LOVEIS</strong> to 22522</span><span>Call <strong>800-656-HOPE</strong></span><span>Call or text <strong>988</strong></span><span>LGBTQ+ youth: text <strong>START</strong> to 678-678</span></div>
    <button data-open-help>All hotlines</button>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        {LOGO_SVG}
        <p>The only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide.</p>
        <div class="btns" style="margin-top:16px">{btn('Donate', 'donate.html', 'mint', 'sm')}{btn('Get the newsletter', 'https://substack.com/@safebae', 'ghost', 'sm')}</div>
        <div class="tag-row" style="margin-top:18px; gap:14px; font-weight:600">
          {a('Instagram','https://www.instagram.com/safe_bae/','ext')}{a('TikTok','https://www.tiktok.com/@safe_bae','ext')}{a('YouTube','https://www.youtube.com/@SafeBAE','ext')}{a('LinkedIn','https://www.linkedin.com/company/safebae/','ext')}{a('Substack','https://substack.com/@safebae','ext')}{a('Facebook','https://www.facebook.com/www.safebae.org','ext')}
        </div>
      </div>
      {cols}
    </div>
    <div class="footer-bottom">
      <div class="candid">{img('candid-platinum-seal-of-transparency-1-0', 'Candid Platinum Seal of Transparency 2025')}<span>SafeBAE is a registered 501(c)(3) nonprofit.<br>EIN 81-5451147 &middot; 7 Evelyn Drive, Bristol, RI 02809</span></div>
      <div class="tag-row" style="gap:18px">{a('Donate','donate.html')}{a('Chip In','chip-in.html')}{a('Fundraise','fundraise.html')}{a('Shop educational products','https://safebae.podia.com/','ext')}{a('Digital Bookshop','https://bookshop.org/shop/SafeBAE','ext')}{a('Photo credits','credits.html')}</div>
      <span>&copy; 2026 SafeBAE</span>
    </div>
  </div>
</footer>'''

FONTS_BASE = 'family=Archivo:wdth,wght@62..125,400..900&family=Montserrat:ital,wght@0,400..800;1,400..600&family=IBM+Plex+Mono:wght@400;500;600'

PAGES = {}

def page(slug, title, desc, body, active='', body_class='', fonts='', head_extra='', scripts='', og_img=None):
    f = FONTS_BASE + (('&' + fonts) if fonts else '')
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:site_name" content="SafeBAE">
<meta name="theme-color" content="#1d414e">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{f}&display=swap">
<link rel="stylesheet" href="assets/css/site.css">
{head_extra}
</head>
<body class="{body_class}">
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{help_drawer()}
{palette()}
<script src="assets/js/site.js"></script>
{scripts}
</body>
</html>'''
    PAGES[slug] = {'title': title, 'desc': desc}
    with open(f'{SITE}/{slug}', 'w') as fh:
        fh.write(doc)
    return slug

# ---------------- reusable sections ----------------
def phero(title, lede='', eyebrow_txt='', crumbs=None, kind='', image=None, media=None, actions='', sticker=None, extra=''):
    cr = ''
    if crumbs:
        cr = '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in crumbs) + '</nav>'
    cls = 'phero'
    if kind: cls += ' ' + ' '.join('phero--' + k for k in kind.split())
    imgpart = ''
    if image:
        cls += ' phero--image'
        imgpart = f'<div class="phero__img">{img(image, "", loading="eager")}</div>'
    if media:
        cls += ' phero--split'
        st = f'<span class="sticker">{esc(sticker)}</span>' if sticker else ''
        return f'''<section class="{cls}"><div class="wrap"><div>{cr}{eyebrow(eyebrow_txt) if eyebrow_txt else ''}<h1>{title}</h1>{f'<p class="lede">{lede}</p>' if lede else ''}{extra}{f'<div class="btns">{actions}</div>' if actions else ''}</div><div class="phero__media">{img(media, "", loading="eager")}{st}</div></div></section>'''
    return f'''<section class="{cls}">{imgpart}<div class="wrap">{cr}{eyebrow(eyebrow_txt) if eyebrow_txt else ''}<h1>{title}</h1>{f'<p class="lede">{lede}</p>' if lede else ''}{extra}{f'<div class="btns">{actions}</div>' if actions else ''}</div></section>'''

def give_band(text='Your donation makes an immediate impact by keeping consent education and resources free for students and schools across the US.'):
    return f'''<section class="band band--aqua band--tight"><div class="wrap give">
<div><p class="eyebrow">Your donation goes a long way</p><h2 style="margin:0 0 .3em">Keep prevention free for every student.</h2><p class="lede" style="margin:0">{esc(text)}</p></div>
<div class="btns" style="justify-content:flex-end">{btn('Donate today', 'donate.html', 'coral', arrow=True)}{btn('Give monthly', 'donate.html#give', 'slate')}</div>
</div></section>'''

def row(title, desc, href, meta=None):
    ext = href.startswith('http')
    m = f'<div class="row__meta">{"".join(f"<span class=chip>{esc(x)}</span>" for x in meta)}</div>' if meta else ''
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="row" href="{esc(href)}"{t}><span><b>{esc(title)}</b><small>{esc(desc)}</small>{m}</span><span class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</span></a>'
