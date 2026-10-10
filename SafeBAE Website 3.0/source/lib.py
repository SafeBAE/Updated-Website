import json, html, os, re
SITE = '/home/claude/v3/site'
MANIFEST = json.load(open('/home/claude/v3/img_manifest.json'))
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
# v3 information architecture: six tabs. Request a Program replaces 360° Schools as a tab
# (360° is the approach behind the programs, one page under that tab); the Library and the
# trainings sit under Resources; #ForDaisy stays a tab.
CAL_MEET = 'https://calendly.com/shaelnorris/60min'
NAV = [
  dict(label='About', key='about', href='about.html', blurb='Founded by teen survivors in 2015. Led by young people ever since.',
       feature=('safebae-executive-director-shael-norris', 'Our story', 'Survivor-founded and youth-led since 2015', 'about.html'),
       groups=[
         ('The organization', '', [
            ('About SafeBAE', 'about.html', 'Our mission and how we began'),
            ('Our Team', 'team.html', 'Staff, youth media team and board'),
            ('Data & Impact', 'impact.html', 'Published research, surveys and reports'),
         ]),
         ('Connect', '', [
            ('Partners & Press', 'partners-press.html', 'Podcasts, partner films and media'),
            ('Contact', 'contact.html', 'Reach the SafeBAE team'),
            ('Donate', 'donate.html', 'Keep prevention free for students'),
         ]),
       ]),
  dict(label='Students', key='students', href='students.html', blurb='Everything here is free for students, and built by students.',
       feature=('clubhero', 'SafeBAE Clubs', 'Start a SafeBAE club at your school', 'clubs.html'),
       groups=[
         ('Get involved', '', [
            ('For Students', 'students.html', 'Everything for high school students'),
            ('SafeBAE Clubs', 'clubs.html', 'Start, affiliate or restart a chapter'),
            ('Reform Your School’s Policy', 'reform-policy.html', 'A student guide to stronger policies'),
            ('Summer Activist Institute', 'summer-institute.html', 'Meet the fellows'),
         ]),
         ('Free trainings', '', [
            ('Peer Educator Training', 'peer-educator.html', 'Self-paced, 16 modules, certificate'),
            ('AI Literacy Training', 'ai-literacy.html', 'New: six modules on AI and relationships'),
            ('BAE Skills Lab', 'skills-lab.html', 'Short interactive activities'),
            ('En Español', 'espanol.html', 'Entrenamiento en español'),
         ]),
       ]),
  dict(label='Adults', key='adults', href='adults.html', blurb='For the parents, caregivers, educators and mentors in a young person’s life.',
       feature=('us-sometale-parent', 'Parents & caregivers', 'Start the conversation early, and keep talking', 'parents.html'),
       groups=[
         ('By role', '', [
            ('For Adults', 'adults.html', 'Start here if you support young people'),
            ('Parents & Caregivers', 'parents.html', 'Conversations, support and next steps'),
            ('Educators', 'educators.html', 'Classroom tools at every level of use'),
            ('College Students', 'college.html', 'Mentor high schoolers, start a campus club'),
         ]),
         ('What adults ask about', '', [
            ('Choking Hazard', 'choking-hazard.html', 'New: what adults should know about sexual choking'),
            ('Vibe Check for adults', 'vibe-check.html#adults', 'How to share it with a young person'),
            ('If a young person tells you', 'survivor-support.html#when-someone-tells-you', 'What to say, and what to avoid'),
            ('Bring SafeBAE to your school', 'request-a-program.html', 'Assemblies, trainings and pricing'),
         ]),
       ]),
  dict(label='Request a Program', key='programs', href='request-a-program.html', blurb='Assemblies, curriculum, training and policy support, each one built on the SafeBAE 360° approach.',
       feature=('066', 'Assemblies', 'Co-presented with youth leaders at your school', 'assemblies.html'),
       groups=[
         ('Start here', '', [
            ('Request a Program', 'request-a-program.html', 'Every program and the request form'),
            ('SafeBAE 360° Schools', '360-schools.html', 'The whole-school approach behind our programs'),
            ('Pricing', 'request-a-program.html#pricing', 'Flexible, sliding scale'),
         ]),
         ('Programs', '', [
            ('Assemblies', 'assemblies.html', 'One-time events, co-presented with youth leaders'),
            ('Consent Curriculum', 'consent-curriculum.html', '15 lessons aligned to NHES'),
            ('Faculty & Staff Training', 'professional-development.html', 'Trauma-informed professional development'),
         ]),
         ('', '', [
            ('Policy Reform Guide', 'policy-reform-guide.html', 'For administrators and districts'),
            ('Accountability Training', 'accountability-training.html', 'For students who have caused harm'),
            ('Sexual Strangulation Prevention', 'choking-hazard.html#schools', 'New: launches November 2026'),
         ]),
       ]),
  dict(label='Resources', key='resources', href='resources.html', blurb='Every SafeBAE resource is free.', wide=True,
       feature=('vc-screen', 'Vibe Check', 'No judgment, just answers', 'vibe-check.html'),
       foot=('Resources Hub', 'resources.html', 'Every SafeBAE resource, sorted by who it’s for'),
       groups=[
         ('Trainings & tools', '', [
            ('Peer Educator Training', 'peer-educator.html', 'Free, self-paced, 16 modules'),
            ('AI Literacy Training', 'ai-literacy.html', 'New: free, for ages 13+'),
            ('Vibe Check', 'vibe-check.html', 'Anonymous reflection tool'),
            ('BAE Skills Lab', 'skills-lab.html', 'Interactive consent activities'),
            ('En Español', 'espanol.html', 'Entrenamiento para educadores pares'),
         ]),
         ('The Library', '', [
            ('Search the Library', 'library.html', 'Every film, podcast and guide'),
            ('Films & videos', 'library.html#films', 'Youth-made, with lesson plans'),
            ('Podcasts', 'library.html#podcasts', 'Conversations with SafeBAE leaders'),
            ('Teaching guides', 'library.html#guides', 'Ready-to-teach discussion guides'),
            ('Posters', 'posters.html', 'Free to download and print'),
         ]),
         ('Campaigns & series', '', [
            ('Choking Hazard', 'choking-hazard.html', 'There’s no safe way to choke someone'),
            ('#KnowB4UNude', 'film-knowb4unude.html', 'A PSA on nudes and online pressure'),
            ('It’s Giving Red Flags', 'film-its-giving-red-flags.html', 'A short film about consent'),
            ('BAEcode: Game On!', 'film-baecode-game-on.html', 'Bystander intervention'),
            ('Race, Rape Culture & Resistance', 'film-race-rape-culture-resistance.html', 'A four-lesson series'),
         ]),
         ('Support & answers', '', [
            ('Survivor Support', 'survivor-support.html', 'Hotlines, healing and how to help'),
            ('Title IX', 'title-ix.html', 'Your rights at school'),
            ('Myths & Facts', 'myths-facts.html', 'What the research says'),
            ('FAQ', 'faq.html', 'Straight answers to common questions'),
            ('Blog', 'blog.html', 'Stories, analysis and news'),
         ]),
       ]),
  dict(label='#ForDaisy', key='fordaisy', href='fordaisy.html', blurb='Remembering our co-founder, Daisy Coleman.',
       feature=('daisy-coleman', '#ForDaisy', 'Remembering our co-founder, Daisy Coleman', 'fordaisy.html'),
       groups=[
         ('Remembering Daisy', '', [
            ('Remembering Daisy', 'fordaisy.html', 'Her story, her statement and her legacy'),
            ('Tribute wall', 'fordaisy.html#wall', 'Messages from people Daisy reached'),
            ('Add your message', 'fordaisy.html#add', 'Share what Daisy meant to you'),
         ]),
         ('Her legacy', '', [
            ('Tattoos & Healing', 'fordaisy-tattoos.html', 'Daisy’s art, and a path some survivors take'),
            ('Peer Educator Training', 'peer-educator.html', 'Offered in Daisy’s memory'),
            ('About SafeBAE', 'about.html', 'The organization she co-founded'),
         ]),
       ]),
]
# older page modules pass these keys; they resolve to the v3 tabs
NAV_ALIAS = {'schools': 'programs', 'library': 'resources'}

RIBBON = [
  ('ai-literacy.html', 'New', 'The SafeBAE AI Literacy Training launches during Media Literacy Week, Oct 26–30'),
  ('choking-hazard.html', 'New', 'Choking Hazard: there’s no safe way to choke someone'),
]

def _navlink(t, h, d=''):
    ext = h.startswith('http')
    tgt = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a href="{esc(h)}"{tgt}><span>{esc(t)}{" &#8599;" if ext else ""}</span>' + (f'<small>{esc(d)}</small>' if d else '') + '</a>'

def header(active=''):
    active = NAV_ALIAS.get(active, active)
    items, drawer = [], []
    for n in NAV:
        key = n['key']
        cur = ' aria-current="true"' if key == active else ''
        cols = ''
        for gt, gh, links in n['groups']:
            head = (f'<a class="mega__h" href="{gh}">{esc(gt)}<i aria-hidden="true">&rarr;</i></a>' if gh else f'<p class="mega__h">{esc(gt)}</p>') if gt else '<p class="mega__h mega__h--blank" aria-hidden="true">&nbsp;</p>'
            cols += f'<div class="mega__col">{head}' + ''.join(_navlink(t, h, d) for t, h, d in links) + '</div>'
        fimg, fkick, ftxt, fhref = n['feature']
        intro = '' if n.get('wide') else (f'<div class="mega__intro"><b>{esc(n["label"])}</b><p>{esc(n["blurb"])}</p>'
                                         f'<a class="mega__all" href="{n["href"]}">{"Start here" if key != "fordaisy" else "Remember Daisy"}<i aria-hidden="true">&rarr;</i></a></div>')
        foot = ''
        if n.get('foot'):
            ft, fh, fd = n['foot']
            foot = f'<a class="mega__foot" href="{fh}"><b>{esc(ft)}</b><span>{esc(fd)}</span><i aria-hidden="true">&rarr;</i></a>'
        dz = ' nav__top--daisy' if key == 'fordaisy' else ''
        lead = '<span class="daisy" aria-hidden="true"></span>' if key == 'fordaisy' else ''
        items.append(
            f'<div class="nav__item"><button class="nav__top{dz}" aria-expanded="false"{cur}>{lead}{esc(n["label"])}<span class="caret" aria-hidden="true"></span></button>'
            f'<div class="mega mega--c{len(n["groups"])}{" mega--wide" if n.get("wide") else ""}" style="--cols:{len(n["groups"])}"><div class="mega__in">{intro}<div class="mega__cols">{cols}</div>'
            f'<a class="mega__feature" href="{fhref}">{img(fimg, "")}<em>{esc(fkick)}</em><b>{esc(ftxt)}</b></a>{foot}</div></div></div>')
        dl = ''
        for gt, gh, links in n['groups']:
            if gt: dl += f'<p class="drawer__g">{esc(gt)}</p>'
            dl += ''.join(f'<a href="{esc(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'>{esc(t)}</a>' for t, h, d in links)
        drawer.append(f'<details><summary>{esc(n["label"])}</summary>{dl}</details>')
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="utility">
  <div class="wrap">
    <div class="utility__help"><span>Need to talk to someone?</span> <span><strong>Text LOVEIS</strong> to 22522</span> <span class="hide-sm"><strong>Call</strong> 800-656-HOPE (4673)</span> <button class="linkish" data-open-help>All hotlines</button></div>
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
<div class="ribbon" id="sb-ribbon" role="region" aria-label="What's new at SafeBAE"><div class="wrap"><div class="ribbon__items">{''.join(f'<a href="{h}"><b>{esc(t)}</b><span>{esc(x)}</span><i aria-hidden="true">&rarr;</i></a>' for h, t, x in RIBBON)}</div><button class="ribbon__x" type="button" aria-label="Hide announcements" data-ribbon-x>&times;</button></div></div>
<div class="drawer" id="menu" aria-hidden="true">
  <div class="drawer__scrim" data-close></div>
  <div class="drawer__panel" role="dialog" aria-label="Menu">
    <div class="drawer__head"><span style="width:120px;color:var(--mint);display:block">{LOGO_SVG}</span><button class="close-x" data-close aria-label="Close menu">&times;</button></div>
    <a class="solo" href="index.html">Home</a>
    {''.join(drawer)}
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
  ('Students', [('For Students','students.html'),('SafeBAE Clubs','clubs.html'),('Club Hub','https://clubs.safebae.org'),('Peer Educator Training','peer-educator.html'),('AI Literacy Training','ai-literacy.html'),('Summer Institute','summer-institute.html'),('Reform Your Policy','reform-policy.html'),('En Español','espanol.html')]),
  ('Adults', [('For Adults','adults.html'),('Parents & Caregivers','parents.html'),('Educators','educators.html'),('College Students','college.html'),
              ('!Give', ''), ('Donate','donate.html'),('Chip In','chip-in.html'),('Fundraise','fundraise.html')]),
  ('Request a Program', [('All programs','request-a-program.html'),('Assemblies','assemblies.html'),('360° Schools','360-schools.html'),('Consent Curriculum','consent-curriculum.html'),('Faculty & Staff Training','professional-development.html'),('Policy Reform Guide','policy-reform-guide.html'),('Accountability Training','accountability-training.html'),('Strangulation Prevention','choking-hazard.html#schools')]),
  ('Resources', [('Resources Hub','resources.html'),('The Library','library.html'),('Posters','posters.html'),('Vibe Check','vibe-check.html'),('BAE Skills Lab','skills-lab.html'),('Choking Hazard','choking-hazard.html'),('#KnowB4UNude','film-knowb4unude.html'),('Blog','blog.html')]),
  ('Support & answers', [('Survivor Support','survivor-support.html'),('Hotlines','survivor-support.html#hotlines'),('Title IX','title-ix.html'),('Myths & Facts','myths-facts.html'),('FAQ','faq.html'),
              ('!#ForDaisy', ''), ('Remembering Daisy','fordaisy.html'),('Tattoos & Healing','fordaisy-tattoos.html')]),
  ('About', [('About SafeBAE','about.html'),('Our Team','team.html'),('Data & Impact','impact.html'),('Partners & Press','partners-press.html'),('Contact','contact.html'),
              ('!Shop', ''), ('Educational products','https://safebae.podia.com/'),('Digital Bookshop','https://bookshop.org/shop/SafeBAE')]),
]

SOCIAL = [
  ('Instagram', 'https://www.instagram.com/safe_bae/', '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3.2" y="3.2" width="17.6" height="17.6" rx="5"/><circle cx="12" cy="12" r="4.1"/><circle cx="17.2" cy="6.8" r="1.15" fill="currentColor" stroke="none"/></svg>'),
  ('TikTok', 'https://www.tiktok.com/@safe_bae', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'),
  ('YouTube', 'https://www.youtube.com/@SafeBAE', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.28 5 12 5 12 5s-6.28 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.76 1.77C5.72 19 12 19 12 19s6.28 0 7.84-.43a2.5 2.5 0 0 0 1.76-1.77A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8ZM10 15V9l5.2 3Z"/></svg>'),
  ('LinkedIn', 'https://www.linkedin.com/company/safebae/', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.94 8.5H3.56V20h3.38zM5.25 3.5a1.96 1.96 0 1 0 0 3.92 1.96 1.96 0 0 0 0-3.92ZM20.44 20v-6.3c0-3.1-1.65-4.54-3.86-4.54a3.33 3.33 0 0 0-3.02 1.66V8.5h-3.37V20h3.37v-6c0-1.2.6-2.05 1.76-2.05 1.1 0 1.74.78 1.74 2.05v6z"/></svg>'),
  ('Substack', 'https://substack.com/@safebae', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3.6h16v2.5H4zm0 4.7h16v2.5H4zM4 13h16v8.4l-8-4.5-8 4.5z"/></svg>'),
  ('Facebook', 'https://www.facebook.com/www.safebae.org', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.6 21.5v-8h2.7l.4-3.2h-3.1V8.3c0-.92.26-1.55 1.58-1.55h1.7V3.9a22 22 0 0 0-2.46-.13c-2.44 0-4.1 1.49-4.1 4.22v2.31H7.6v3.2h2.72v8z"/></svg>'),
]

def footer():
    def col(t, links):
        out = f'<div class="fcol"><h4>{esc(t)}</h4><ul>'
        for l, h in links:
            if l.startswith('!'):
                out += f'</ul><h4 class="fcol__sub">{esc(l[1:])}</h4><ul>'
            else:
                out += f'<li>{a(esc(l), h, "ext" if h.startswith("http") else "")}</li>'
        return out + '</ul></div>'
    cols = ''.join(col(t, links) for t, links in FOOT_COLS)
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="SafeBAE on {n}" title="{n}">{svg}</a>' for n, u, svg in SOCIAL)
    return f'''
<section class="support-strip" aria-label="Support resources">
  <div class="wrap">
    <b>Need support right now?</b>
    <div class="nums"><span>Text <strong>LOVEIS</strong> to 22522</span><span>Call <strong>800-656-HOPE</strong></span><span>Call or text <strong>988</strong></span><span>LGBTQ+ youth: text <strong>START</strong> to 678-678</span></div>
    <button data-open-help>All hotlines</button>
  </div>
</section>
<footer class="site-footer">
  <span class="footer-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <a class="footer-mark" href="index.html" aria-label="SafeBAE: Safe Before Anyone Else"><span class="fm-l fm-l1"><b>Safe</b> <b>B</b><i>efore</i></span><span class="fm-l fm-l2"><b>A</b><i>nyone</i> <b>E</b><i>lse.</i></span></a>
    <div class="footer-lead">
      <div class="footer-brand">{LOGO_SVG}<p>The only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide.</p></div>
      <div class="footer-act">
        <div class="btns">{btn('Donate', 'donate.html', 'mint')}{btn('Get the newsletter', 'https://substack.com/@safebae', 'ghost')}</div>
        <div class="socials">{soc}</div>
      </div>
    </div>
    <nav class="footer-cols" aria-label="Footer">{cols}</nav>
    <div class="footer-bottom">
      <div class="candid">{img('candid-platinum-seal-of-transparency-1-0', 'Candid Platinum Seal of Transparency 2025')}<span>SafeBAE is a registered 501(c)(3) nonprofit.<br>EIN 81-5451147 &middot; 7 Evelyn Drive, Bristol, RI 02809</span></div>
      <div class="footer-legal"><span>&copy; 2026 SafeBAE</span>{a('Photo credits','credits.html')}<a class="footer-up" href="#top"><span class="daisy" aria-hidden="true"></span>Back to top</a></div>
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
    wm = '<span class="phero__wm" aria-hidden="true"></span>'
    cls = 'phero'
    if kind: cls += ' ' + ' '.join('phero--' + k for k in kind.split())
    imgpart = ''
    if image:
        cls += ' phero--image'
        imgpart = f'<div class="phero__img">{img(image, "", loading="eager")}</div>'
    if media:
        cls += ' phero--split'
        st = f'<span class="sticker">{esc(sticker)}</span>' if sticker else ''
        return f'''<section class="{cls}">{wm}<div class="wrap"><div>{cr}{eyebrow(eyebrow_txt) if eyebrow_txt else ''}<h1>{title}</h1>{f'<p class="lede">{lede}</p>' if lede else ''}{extra}{f'<div class="btns">{actions}</div>' if actions else ''}</div><div class="phero__media">{img(media, "", loading="eager")}{st}</div></div></section>'''
    return f'''<section class="{cls}">{imgpart}{wm}<div class="wrap">{cr}{eyebrow(eyebrow_txt) if eyebrow_txt else ''}<h1>{title}</h1>{f'<p class="lede">{lede}</p>' if lede else ''}{extra}{f'<div class="btns">{actions}</div>' if actions else ''}</div></section>'''

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


# Choking Hazard campaign warning label (shared look; CSS .hz in site.css)
HZ_TRI = ('<svg viewBox="0 0 48 42" aria-hidden="true" focusable="false">'
          '<path class="o" d="M21.4 3.5a3 3 0 0 1 5.2 0l19 33a3 3 0 0 1-2.6 4.5H5a3 3 0 0 1-2.6-4.5z"/>'
          '<rect class="i" x="21.6" y="13" width="4.8" height="15" rx="2.4"/><circle class="i" cx="24" cy="34" r="2.8"/></svg>')


def hz_label(cls=''):
    return (f'<span class="hz {cls}" aria-hidden="true"><span class="hz__l">'
            f'<span class="hz__w">{HZ_TRI}<b>Warning</b></span>'
            '<span class="hz__m">Choking is a hazard</span>'
            '<span class="hz__s">May cause serious injury or death</span>'
            '<span class="hz__u">chokinghazard.org</span></span></span>')
