from lib import *
import math, json

# ---- per-film type identities (shared with the film pages) ----
FILM_FONTS = {
  'red':  ('Tilt Neon', "'Tilt Neon', sans-serif"),
  'bae':  ('Silkscreen', "'Silkscreen', monospace"),
  'know': ('Rubik Mono One', "'Rubik Mono One', sans-serif"),
  'date': ('Nunito', "'Nunito', sans-serif"),
  'oh':   ('DotGothic16', "'DotGothic16', sans-serif"),
  'rc':   ('Zilla Slab', "'Zilla Slab', serif"),
  'men':  ('Saira Stencil One', "'Saira Stencil One', sans-serif"),
  'rrcr': ('DM Serif Display', "'DM Serif Display', serif"),
}
FILMS = [
  ('film-its-giving-red-flags.html', 'red', 'It’s Giving Red Flags', 'red-flags', 'Consent · red flags'),
  ('film-baecode-game-on.html', 'bae', 'BAEcode: Game On!', 'gameon8', 'Bystander intervention'),
  ('film-knowb4unude.html', 'know', '#knowB4Unude', 'knowb4unude', 'Nudes · digital safety'),
  ('film-race-rape-culture-resistance.html', 'rrcr', 'Race, Rape Culture & Resistance', '2l3a1960', 'Four-lesson series'),
  ('film-dating-after-sexual-assault.html', 'date', 'Intimacy & Dating After Assault', 'yt-rixb8vlmajy', 'Healing · partners'),
  ('film-online-harassment-of-survivors.html', 'oh', 'End Online Harassment of Survivors', 'qts-full-cast-copy-2', 'Online harassment'),
  ('film-rape-culture.html', 'rc', 'Rape Culture → Culture of Respect', 'yt-fsmycfjpws4', 'With Charlie Coleman'),
  ('film-sexual-assault-of-men.html', 'men', 'Supporting Male Survivors', 'safebae-14', 'Theo’s story'),
]

def film_font_link(subset=True):
    fams = []
    for k, (fam, _) in FILM_FONTS.items():
        txt = ''.join(sorted(set(''.join(t for _, kk, t, _, _ in FILMS if kk == k) + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))) if subset else ''
        q = 'family=' + fam.replace(' ', '+') + (':wght@800' if fam == 'Nunito' else '') + (':wght@700' if fam == 'Zilla Slab' else '')
        fams.append(q)
    return '&'.join(fams)

def film_strip(cls=''):
    cards = []
    for href, k, title, im, tag in FILMS:
        cards.append(f'''<a class="fcard fcard--{k}" href="{href}">{img(im, '')}<span class="fcard__shade"></span><span class="fcard__tag">{esc(tag)}</span><span class="fcard__title">{esc(title)}</span><span class="fcard__go">Film + guide &rarr;</span></a>''')
    return f'<div class="fstrip {cls}">' + ''.join(cards) + '</div>'

FILM_STRIP_CSS = '''
.fstrip{display:grid; grid-auto-flow:column; grid-auto-columns:minmax(230px,1fr); gap:14px; overflow-x:auto; padding:4px 2px 18px; scroll-snap-type:x mandatory; scrollbar-width:thin}
.fcard{position:relative; aspect-ratio:3/4; border-radius:14px; overflow:hidden; color:#fff; text-decoration:none; scroll-snap-align:start; background:#000; display:block; isolation:isolate}
.fcard img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s, filter .4s; filter:saturate(.85)}
.fcard:hover img{transform:scale(1.06); filter:saturate(1.05)}
.fcard__shade{position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,.05) 30%, rgba(8,24,30,.92))}
.fcard__tag{position:absolute; top:12px; left:12px; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; background:rgba(8,24,30,.65); padding:4px 8px; border-radius:4px}
.fcard__title{position:absolute; left:14px; right:14px; bottom:44px; font-size:1.55rem; line-height:1.02}
.fcard__go{position:absolute; left:14px; bottom:14px; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint)}
.fcard--red .fcard__title{font-family:'Tilt Neon',sans-serif; color:#ffd9d9; text-shadow:0 0 6px #fe7171, 0 0 18px #fe7171, 0 0 36px rgba(254,113,113,.7); text-transform:uppercase; font-size:1.7rem}
.fcard--bae .fcard__title{font-family:'Silkscreen',monospace; color:#ffd2d2; text-shadow:3px 3px 0 #210658; font-size:1.45rem}
.fcard--know .fcard__title{font-family:'Rubik Mono One',sans-serif; color:var(--mint); font-size:1.35rem}
.fcard--date .fcard__title{font-family:'Nunito',sans-serif; font-weight:800; color:var(--aqua); text-transform:lowercase; font-size:1.6rem}
.fcard--oh .fcard__title{font-family:'DotGothic16',sans-serif; color:var(--mint); text-transform:uppercase; font-size:1.4rem}
.fcard--rc .fcard__title{font-family:'Zilla Slab',serif; font-weight:700; color:#fff; font-size:1.6rem}
.fcard--men .fcard__title{font-family:'Saira Stencil One',sans-serif; color:#fff; letter-spacing:.06em; text-transform:uppercase; font-size:1.5rem}
.fcard--rrcr .fcard__title{font-family:'DM Serif Display',serif; color:#fff; font-size:1.7rem}
'''

def ring_svg():
    comps = [
      ('Peer Educator Training & Youth Leadership', 'peer-educator.html', '#15ffc8', '#1d414e'),
      ('Healthy Relationship & Consent Curriculum', 'consent-curriculum.html', '#13848f', '#fff'),
      ('Faculty & Staff Training', 'professional-development.html', '#1d5a66', '#fff'),
      ('School Policy Support', 'policy-reform-guide.html', '#1d414e', '#fff'),
      ('Anonymous Reporting Tool (SafeBAE x REES)', '#rees', '#fe7171', '#1d414e'),
      ('Educational Resources to Reduce Recidivism', 'accountability-training.html', '#7dbbc1', '#1d414e'),
    ]
    cx = cy = 210; R = 200; r = 128; gap = 2.4
    paths = []
    for i, (t, h, fill, ink) in enumerate(comps):
        a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
        p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
        x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
        d = f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'
        am = math.radians(-90 + i * 60 + 30); tx, ty = p((R + r) / 2, am)
        paths.append(f'<g class="seg" data-seg="{i}" tabindex="0" role="button" aria-label="{esc(t)}"><path d="{d}" fill="{fill}"/><text x="{tx:.1f}" y="{ty+9:.1f}" text-anchor="middle" fill="{ink}" font-family="Archivo" font-weight="900" font-size="26">{i+1}</text></g>')
    return f'<svg class="ring" viewBox="0 0 420 420" aria-label="SafeBAE 360 components">{"".join(paths)}<text x="210" y="205" text-anchor="middle" class="ring__c" font-family="Archivo" font-weight="900" font-size="64" fill="#1d414e" style="font-stretch:125%">360&deg;</text><text x="210" y="238" text-anchor="middle" font-family="IBM Plex Mono" font-weight="600" font-size="13" fill="#46646e" letter-spacing="2">SIX COMPONENTS</text></svg>', comps

COMP_TEXT = [
  'Students complete a self-paced, online certification to become Peer Educators. Youth leaders help shape implementation, lead presentations, co-facilitate curriculum sessions, organize campaigns through SafeBAE Clubs, and receive ongoing mentorship from our team.',
  'A trauma-informed curriculum aligned with the National Health Education Standards. Lessons cover consent, boundaries, communication, digital safety, healing, and accountability, with lesson plans, slides, activities, and printable resources.',
  'Professional development for teachers, staff, and administrators on trauma-informed response, supporting marginalized students, and building a school culture of consent and accountability. Flexible and tailored to each school.',
  'Hands-on consultation to audit and revise sexual misconduct and Title IX policies, with annotated audits, student-centered model language, communication templates, and rollout strategies.',
  'A secure, private space where students can document incidents of harm at their own pace, report anonymously or by name to their school, and connect with school-specific resources and support.',
  'Tools for students who have caused harm, supporting education, accountability, and behavior change. Includes the structured Accountability Training and Vibe Check, rooted in prevention, healing, and restorative justice rather than punishment.',
]

HOME_CSS = FILM_STRIP_CSS + '''
.hero{background:var(--slate); color:#fff; position:relative; overflow:hidden}
.hero__grid{display:grid; grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr); gap:clamp(24px,4vw,56px); align-items:center; min-height:min(760px, calc(100vh - 112px)); padding-block:clamp(40px,5vw,64px)}
.hero__title{font-size:clamp(2.8rem,6.3vw,6.6rem); line-height:.86; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .35em}
.hero__title span{display:block; white-space:nowrap}
.hero__title b{color:var(--mint); font-weight:900}
.hero__title i{font-style:normal; display:inline-block; animation:stretch 1.2s cubic-bezier(.2,.8,.2,1) both}
.hero__title span:nth-child(2) i{animation-delay:.12s} .hero__title span:nth-child(3) i{animation-delay:.24s} .hero__title span:nth-child(4) i{animation-delay:.36s}
@keyframes stretch{from{font-stretch:62%; opacity:.25; letter-spacing:-.06em} to{font-stretch:125%; opacity:1; letter-spacing:-.02em}}
.hero__key{display:flex; align-items:center; gap:10px; font-family:var(--mono); font-size:.78rem; letter-spacing:.06em; color:var(--aqua); margin:-.4em 0 1.4em}
.hero__key b{color:var(--mint)}
.hero .lede{color:rgba(255,255,255,.9); max-width:none}
.hero__proof{display:flex; flex-wrap:wrap; gap:8px 22px; margin-top:26px; font-weight:600; font-size:.9rem; color:var(--aqua)}
.hero__proof span::before{content:""; display:inline-block; width:8px; height:8px; background:var(--mint); margin-right:8px; transform:rotate(45deg) translateY(-2px)}
.wall{position:relative; height:min(680px, 78vh); display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; mask-image:linear-gradient(transparent, #000 10%, #000 88%, transparent); -webkit-mask-image:linear-gradient(transparent, #000 10%, #000 88%, transparent)}
.wall__col{overflow:hidden; position:relative}
.wall__track{display:flex; flex-direction:column; gap:12px; animation:up 60s linear infinite}
.wall__col:nth-child(2) .wall__track{animation-direction:reverse; animation-duration:72s}
.wall__col:nth-child(3) .wall__track{animation-duration:66s}
.wall img{width:100%; aspect-ratio:4/5; object-fit:cover; border-radius:12px}
.wall__col:nth-child(2) img:nth-child(odd){aspect-ratio:1}
@keyframes up{to{transform:translateY(-50%)}}
.wall:hover .wall__track{animation-play-state:paused}
.hero__stickers{position:absolute; inset:0; pointer-events:none; z-index:3}
.hero__stickers .sticker{position:absolute}
@media (max-width:900px){
  .hero__grid{grid-template-columns:1fr; min-height:0}
  .wall{height:220px; grid-template-columns:1fr; mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent); -webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
  .wall__col:not(:first-child){display:none}
  .wall__track{flex-direction:row; animation-name:left; width:max-content}
  .wall img{width:170px; height:210px; aspect-ratio:auto}
  @keyframes left{to{transform:translateX(-50%)}}
}
/* who */
.who__tabs{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; margin-bottom:22px}
.who__tab{font:inherit; text-align:left; padding:16px 16px 14px; border-radius:12px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; display:flex; flex-direction:column; gap:4px; transition:border-color .2s, background .2s}
.who__tab small{font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--teal)}
.who__tab span{font-family:var(--display); font-weight:800; font-stretch:110%; font-size:1.15rem; line-height:1.1}
.who__tab:hover{border-color:var(--teal)}
.who__tab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.who__tab[aria-selected="true"] small{color:var(--mint)}
.who__tab--help small{color:var(--coral)}
.who__panel{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(20px,4vw,48px); align-items:stretch}
.who__img{border-radius:var(--r-lg); overflow:hidden; min-height:320px; position:relative}
.who__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.who__img .sticker{position:absolute; left:16px; bottom:16px}
.who__panel h3{font-size:clamp(1.5rem,2.4vw,2rem); margin-bottom:.4em}
@media (max-width:960px){ .who__tabs{grid-template-columns:repeat(2,minmax(0,1fr))} .who__tabs > :last-child:nth-child(odd){grid-column:1/-1} .who__panel{grid-template-columns:1fr} .who__img{min-height:220px} }
/* vibe */
.vibe{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(28px,5vw,72px); align-items:center}
.vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.3rem; color:var(--mint); margin-bottom:22px}
.vibe__mark .daisy{width:42px; height:42px}
.qs{position:relative; height:calc(clamp(2.3rem,5vw,4.4rem) * 2.1); overflow:hidden; margin:0 0 .3em}
.qs span{position:absolute; inset:0; display:flex; align-items:flex-end; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.3rem,5vw,4.4rem); line-height:1; letter-spacing:-.02em; color:#fff; transform:translateY(110%); transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s; opacity:0}
.qs span.on{transform:none; opacity:1}
.qs span.out{transform:translateY(-110%); opacity:0}
.vibe__press{display:flex; flex-wrap:wrap; gap:22px 34px; align-items:center; margin-top:30px; padding-top:22px; border-top:1px solid rgba(255,255,255,.25)}
.vibe__press img{height:30px; width:auto; filter:brightness(0) invert(1); opacity:.92}
.vibe__press span{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua)}
.phone{position:relative; width:min(320px,78vw); margin-inline:auto; aspect-ratio:390/800; border-radius:46px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6), 0 0 0 2px rgba(255,255,255,.08); overflow:hidden; transform:rotate(-4deg)}
.phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.phone-wrap{position:relative}
.phone-wrap .sticker{position:absolute; z-index:2}
/* cpet */
.facts{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin:22px 0}
.fact{background:#fff; border-radius:12px; padding:14px 16px; border:1px solid var(--line)}
.fact b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:1.7rem; line-height:1; color:var(--logo-teal)}
.fact span{font-size:.85rem; font-weight:600; color:var(--ink-soft)}
/* library teaser */
.libsearch{display:flex; gap:10px; max-width:640px; margin-top:22px}
.libsearch input{flex:1; min-width:0; font:inherit; font-size:1.05rem; padding:14px 16px; border-radius:10px; border:2px solid rgba(255,255,255,.25); background:rgba(255,255,255,.06); color:#fff}
.libsearch input::placeholder{color:rgba(209,254,255,.7)}
.libsearch input:focus{outline:0; border-color:var(--mint)}
.libcounts{display:flex; flex-wrap:wrap; gap:8px; margin-top:16px}
.libcounts a{font-family:var(--mono); font-size:.75rem; letter-spacing:.06em; text-transform:uppercase; text-decoration:none; padding:7px 11px; border-radius:6px; border:1.5px solid rgba(209,254,255,.35); color:var(--aqua)}
.libcounts a:hover{border-color:var(--mint); color:var(--mint)}
/* ring */
.ring-wrap{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,4vw,60px); align-items:center}
.ring{width:100%; max-width:440px; margin-inline:auto; display:block; overflow:visible}
.seg{cursor:pointer; transition:transform .25s; transform-origin:210px 210px; outline:none}
.seg path{transition:filter .25s, opacity .25s}
.ring.has-active .seg:not(.on) path{opacity:.35}
.seg.on{transform:scale(1.04)}
.seg:focus-visible path{stroke:#1d414e; stroke-width:4}
.comp{min-height:260px}
.comp__n{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:4rem; line-height:1; color:var(--teal)}
.comp h3{font-size:clamp(1.4rem,2.2vw,1.9rem)}
.comp__list{display:flex; flex-wrap:wrap; gap:6px; margin-top:18px}
.comp__list button{font:inherit; font-size:.82rem; font-weight:700; border:1.5px solid var(--line); background:#fff; border-radius:999px; padding:6px 12px; cursor:pointer; color:var(--slate)}
.comp__list button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
@media (max-width:860px){.ring-wrap{grid-template-columns:1fr} .ring{max-width:320px}}
@media (max-width:860px){.vibe{grid-template-columns:minmax(0,1fr)} .phone{width:min(280px,70vw)}}
@media (max-width:560px){.pods{grid-template-columns:repeat(2,minmax(0,1fr))}}
/* rees */
.rees-feats{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; margin:24px 0}
.rees-feats div{background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-radius:12px; padding:18px}
.rees-feats b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.1rem; color:var(--mint); margin-bottom:4px}
.rees-feats p{margin:0; font-size:.92rem; color:rgba(255,255,255,.82)}
@media (max-width:760px){.rees-feats{grid-template-columns:1fr} .facts{grid-template-columns:1fr}}
/* podcasts */
.pods{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:12px}
.pod{display:block; text-decoration:none; color:inherit}
.pod img{width:100%; aspect-ratio:1; object-fit:cover; border-radius:12px; margin-bottom:8px; transition:transform .3s}
.pod:hover img{transform:translateY(-4px)}
.pod b{display:block; font-size:.88rem; line-height:1.25; font-weight:700}
.pod small{display:block; font-size:.74rem; color:var(--ink-soft); margin-top:2px}
@media (max-width:960px){.pods{grid-template-columns:repeat(3,minmax(0,1fr))}}
/* daisy teaser */
.fd{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(24px,4vw,64px); align-items:center}
.fd__photo{position:relative}
.fd__photo img{border-radius:var(--r-lg); width:100%; aspect-ratio:4/5; object-fit:cover; filter:grayscale(.15)}
.fd__photo .daisy{position:absolute; right:-10px; top:-18px; width:84px; height:84px; color:var(--mint)}
.fd__quote{font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.15rem; line-height:1.4; border-left:4px solid var(--mint); padding-left:18px; margin:22px 0; color:var(--aqua)}
@media (max-width:860px){.fd{grid-template-columns:1fr} .fd__photo{max-width:380px}}
.partner-quote{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,60px); align-items:center}
@media (max-width:860px){.partner-quote{grid-template-columns:1fr}}
'''

def home():
    wall_cols = [
      ['000422', 'clubhero', 'img-2395', 'dsc01134', '2023-institute-selfie', 'img-9509-1'],
      ['1-000383-edited', 'clubtabling', '000263', 'sumact5', 'p1002709', 'img-6620'],
      ['000398', '066', 'img-1286', '1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'img-3755', 'safebae-consent-summits'],
    ]
    cols = ''.join('<div class="wall__col"><div class="wall__track">' + ''.join(img(n, '', loading='eager' if i < 2 else 'lazy') for i, n in enumerate(c + c)) + '</div></div>' for c in wall_cols)

    who = [
      ('student', 'I’m a', 'student', '1-000383-edited', 'Lead prevention at your school', 'SafeBAE was founded by teen survivors who wanted their schools to change. Everything here is free for students.', [
         ('Become a Certified Peer Educator', 'Free, self-paced, 16 online modules and an official certificate.', 'peer-educator.html', ['Free', '16 modules']),
         ('Start or join a SafeBAE club', 'Register a new chapter, affiliate a club you already run, or restart last year’s.', 'clubs.html', ['Club Hub access']),
         ('Practice in the BAE Skills Lab', 'Short interactive activities about consent, boundaries and healthy relationships.', 'https://skills-lab.safebae.org/', ['Games']),
         ('Know your rights under Title IX', 'What your school owes you, and how to find your Title IX Coordinator.', 'title-ix.html', ['Rights'])]),
      ('parent', 'I’m a', 'parent or caregiver', 'us-sometale-parent', 'Support the young people in your life', 'Young people look to the adults around them for cues about relationships, boundaries and safety.', [
         ('Parents & caregivers', 'Early conversations, supporting a survivor, reporting options and alternative justice.', 'parents.html', ['Start here']),
         ('Check Their Vibe: an adult’s guide', 'How to share Vibe Check with a young person and keep it voluntary.', 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf', ['PDF guide']),
         ('Listen: How to Not (Accidentally) Raise a Rapist', 'Shael Norris on The Longest Shortest Time.', 'library.html#parenting', ['Podcast']),
         ('If your child tells you something happened', 'Believe first, avoid blame, seek support, and care for yourself.', 'survivor-support.html', ['Support'])]),
      ('educator', 'I’m an', 'educator', 'img-2395', 'Bring youth-led prevention to your classroom', 'Start wherever you can. Every film comes with a ready-to-teach guide built for short, meaningful discussions.', [
         ('Films & teaching guides', 'Youth-made films, each paired with discussion prompts and activities.', 'library.html#guides', ['8 guides']),
         ('Healthy Relationship & Consent Curriculum', '15 lessons aligned with the National Health Education Standards.', 'consent-curriculum.html', ['NHES']),
         ('Bring SafeBAE to your school', 'Assemblies, staff training and the full 360° Schools model.', 'request-a-program.html', ['Sliding scale']),
         ('Free prevention posters', 'For classrooms, counseling offices, hallways and wellness centers.', 'posters.html', ['Download'])]),
      ('college', 'I’m in', 'college', '1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'Change the schools you came from', 'Mentor high schoolers, start a campus chapter, and get certified.', [
         ('Become a college mentor', 'Help high school students build clubs and push for safer policies.', 'college.html', ['Mentorship']),
         ('Start a SafeBAE club on campus', 'Resources, training and support for events, campaigns and advocacy.', 'clubs.html', ['Clubs']),
         ('Certified Peer Educator Training', 'Certified students are prioritized for paid mentorship opportunities.', 'peer-educator.html', ['Free'])]),
      ('help', 'I', 'need support', '000263', 'You are not alone', 'If something happened to you or a friend, or you’re worried about something you did, start here.', [
         ('Talk to someone now', 'Free, confidential hotlines, most open 24/7.', 'survivor-support.html#hotlines', ['24/7']),
         ('How to support a friend', 'What to say, what to avoid, and how to let them lead.', 'survivor-support.html', ['Support']),
         ('Worried you crossed a line?', 'Vibe Check is anonymous. Nothing is stored or reported.', 'https://checkyourvibe.org/', ['Anonymous']),
         ('Document what happened, privately', 'A free, encrypted record with REES, at your own pace.', 'https://safebae.reessecureus.com/en/Login', ['Private']),
         ('Your options at school', 'Title IX, supportive measures and reporting options.', 'title-ix.html', ['Rights'])]),
    ]
    tabs = ''.join(f'<button class="who__tab{" who__tab--help" if k=="help" else ""}" role="tab" id="who-{k}" aria-controls="whop-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(pre)}</small><span>{esc(lbl)}</span></button>' for i, (k, pre, lbl, *_r) in enumerate(who))
    panels = ''.join(f'''<div class="who__panel" role="tabpanel" id="whop-{k}" aria-labelledby="who-{k}"{'' if i==0 else ' hidden'}>
      <div class="who__img">{img(im, '')}{'<span class="sticker sticker--coral">Free &amp; confidential</span>' if k=='help' else '<span class="sticker">Free for students</span>' if k=='student' else ''}</div>
      <div><h3>{esc(h)}</h3><p class="muted">{esc(p)}</p><div class="rows">{''.join(row(t, dsc, u, m) for t, dsc, u, m in rows)}</div></div></div>''' for i, (k, pre, lbl, im, h, p, rows) in enumerate(who))

    svg, comps = ring_svg()
    comp_btns = ''.join(f'<button aria-pressed="{str(i==0).lower()}" data-seg="{i}">{i+1}. {esc(t.split(" (")[0])}</button>' for i, (t, *_r) in enumerate(comps))
    comp_data = json.dumps([{'t': t, 'h': h, 'd': COMP_TEXT[i]} for i, (t, h, *_r) in enumerate(comps)])

    pods = [('3h2vVAyCO9q0bKyPhcASa3', 'Psych Talk', 'Sexual Violence Prevention for Teens'), ('0v2G7MraWG1V2iyXgGKOUF', 'The Longest Shortest Time', 'Preventing Teens from Joining the Manosphere'),
            ('5xOYkKKsC9qZgeGGGO9WQW', 'When Dating Hurts', 'Shael Norris: Stopping Sexual Violence'), ('042UsrG0aMabkTo66WQQWc', 'The She Matters Podcast', 'Centering Youth Voices'),
            ('4jjztQt08zjUR9guFgJ56x', 'The Longest Shortest Time', 'How to Not (Accidentally) Raise a Rapist'), ('0JfMJbj7ZvISm8m7gp39YS', 'The Measure of Everyday Life', 'Reducing Tolerance for Sexual Assault')]
    pod_html = ''.join(f'<a class="pod" href="https://open.spotify.com/episode/{i}" target="_blank" rel="noopener">{img("sp-"+i.lower(), "")}<b>{esc(t)}</b><small>{esc(s)}</small></a>' for i, s, t in pods)

    partner_logos = ['rini-color-01cbb034', 'alliance-logo-color-vertical', '6716423ef4c1138196fb7101-phillips-exeter-academy-lion', 'walogolg-3', 'header-logo-stacked-3', 'chatgpt-image-dec-10-2025-08-34-32-am', '9e389524-a5f5-4c66-aee6-395723e59586', '63750970-0a6d-4483-b1d7-351445fc2a67', 'ridoh-logo', 'nova-logo', 'logo-mahperd', 'vrlc-logo-final-rgb-for-posters-white-on-blue', 'sml-logo-tag-long']
    marq = ''.join(img(n, '', loading='eager') for n in partner_logos)

    body = f'''
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="eyebrow" style="color:var(--mint)">Survivor-founded &middot; Youth-led &middot; Since 2015</p>
      <h1 class="hero__title" aria-label="Safe Before Anyone Else"><span>Safe</span><span><b>B</b><i>efore</i></span><span><b>A</b><i>nyone</i></span><span><b>E</b><i>lse.</i></span></h1>
      <p class="hero__key"><span class="daisy" style="color:var(--mint)"></span><span>That’s what the <b>BAE</b> in SafeBAE stands for.</span></p>
      <p class="lede">SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. Our programs are free for students and built to change school culture from the inside.</p>
      <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('Bring SafeBAE to your school', 'request-a-program.html', 'ghost')}{btn('Donate', 'donate.html', 'coral')}</div>
      <div class="hero__proof"><span>3,000+ Certified Peer Educators</span><span>70+ clubs every year</span><span>Published in the Journal of Child Sexual Abuse</span></div>
    </div>
    <div class="wall" aria-hidden="true">{cols}
      <div class="hero__stickers"><span class="sticker" style="left:4%;top:16%">Youth-led</span><span class="sticker sticker--coral sticker--r" style="right:6%;top:46%">Survivor-founded</span><span class="sticker sticker--aqua" style="left:30%;bottom:12%">Free for students</span></div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Start here</p><h2>What brings you to SafeBAE?</h2></div></div>
    <div data-tabs="who"><div class="who__tabs" role="tablist" aria-label="Who are you?">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap vibe">
    <div>
      <div class="vibe__mark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <div class="qs" aria-live="off"><span class="on">Did I harm someone?</span><span>Was that consent?</span><span>Did I cross a boundary?</span><span>Am I a bad person?</span><span>Not sure if you crossed a line?</span></div>
      <p class="lede" style="color:#fff">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <p style="color:rgba(255,255,255,.88)">Young people are increasingly turning to anonymous forums and AI chatbots to ask difficult questions about relationships and consent. AI is built to tell you what you want to hear. Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication and accountability. No names, no accounts, and nothing is stored.</p>
      <div class="btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}{btn('Adult guide (PDF)', 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf', 'ghost')}</div>
      <div class="vibe__press"><span>As covered by</span>{img('the-guardian-logo-vector', 'The Guardian')}{img('vox-logo-svg-1', 'Vox')}{img('trendwatching-logo', 'TrendWatching')}</div>
    </div>
    <div class="phone-wrap">
      <div class="phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
      <span class="sticker" style="left:-4%;top:18%">Anonymous</span>
      <span class="sticker sticker--white sticker--r" style="right:0;bottom:20%">Nothing is stored</span>
    </div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap split">
    <div>
      {eyebrow('For Daisy: Before Anyone Else', True)}
      <h2>Certified Peer Educator Training</h2>
      <p class="lede">A free, self-paced training that prepares high school students to lead conversations about consent, healthy relationships and their lived experiences, and to drive prevention in their own schools.</p>
      <div class="facts"><div class="fact"><b>16</b><span>interactive modules</span></div><div class="fact"><b>$0</b><span>for students, anywhere</span></div><div class="fact"><b>3,000+</b><span>certified so far</span></div></div>
      <div class="btns">{btn('Register here', 'peer-educator.html#register', 'slate', arrow=True)}{btn('Ver en Español', 'espanol.html', 'ghost')}{btn('Resume training', 'https://learning.safebae.org/students', 'ghost')}</div>
      <p class="small muted" style="margin-top:18px">Offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission. #ForDaisy</p>
    </div>
    {cpet_player()}
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">The Library</p><h2>Films made by young people. Lessons ready to teach.</h2>
      <p class="lede muted" style="margin-top:.6em">Every film, podcast and teaching guide SafeBAE has made, now in one searchable library.</p></div></div>
    <form class="libsearch" action="library.html" data-libsearch><label class="sr-only" for="home-q">Search the library</label><input id="home-q" name="q" type="search" placeholder="Try “bystander”, “nudes” or “male survivors”"><button class="btn" type="submit">Search</button></form>
    <div class="libcounts"><a href="library.html#films">Films &amp; videos</a><a href="library.html#podcasts">17 podcasts</a><a href="library.html#guides">8 teaching guides</a><a href="film-race-rape-culture-resistance.html">Race, Rape Culture &amp; Resistance</a></div>
  </div>
  <div class="wrap wrap--wide" style="margin-top:28px">{film_strip()}</div>
</section>

<section class="band band--paper" id="rees-and-360">
  <div class="wrap">
    <div class="ring-wrap">
      <div>{svg}</div>
      <div>
        <p class="eyebrow">Youth-led, school-wide culture change</p>
        <h2>SafeBAE 360° Schools</h2>
        <p class="muted">A comprehensive, survivor-centered prevention model rooted in trauma-informed care. Schools can start with one component or build the whole model over time.</p>
        <div class="comp" id="comp"><div class="comp__n">1</div><h3>{esc(comps[0][0])}</h3><p>{esc(COMP_TEXT[0])}</p><a class="arrow-link" href="{comps[0][1]}">Learn more</a></div>
        <div class="comp__list" role="group" aria-label="Choose a component">{comp_btns}</div>
        <div class="btns" style="margin-top:24px">{btn('Explore 360° Schools', '360-schools.html', 'slate', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate" id="rees">
  <div class="wrap split split--wide-l">
    <div>
      <p class="eyebrow">SafeBAE x REES</p>
      <h2>Document your experience, privately and securely.</h2>
      <p class="lede" style="color:rgba(255,255,255,.88)">A free tool that gives every student a private, encrypted space to document incidents of harm or violence at their own pace. Nothing is shared without your consent.</p>
      <div class="rees-feats"><div><b>Private documentation</b><p>Create a secure, encrypted record of what happened, on your own time, entirely for yourself.</p></div><div><b>At your own pace</b><p>Come back whenever you’re ready. Your documentation is saved, with no pressure and no deadline.</p></div><div><b>At partner schools</b><p>Students can choose to report anonymously to their school and access school-specific resources.</p></div></div>
      <div class="btns">{btn('Student access', 'https://safebae.reessecureus.com/en/Login', 'mint')}{btn('Become a partner school', 'request-a-program.html', 'ghost')}</div>
    </div>
    <div style="border-radius:var(--r-lg);padding:34px;display:grid;place-items:center">{img('logo-horiz-rgb', 'REES')}</div>
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap stats">
    <div class="stat"><b>3,000+</b><span>Certified Peer Educators trained</span></div>
    <div class="stat"><b>70+</b><span>active SafeBAE clubs each year</span></div>
    <div class="stat"><b>86,000+</b><span>students reached through our digital resources</span></div>
    <div class="stat"><b>2015</b><span>founded by teen survivors and their families</span></div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap partner-quote">
    <div>
      <p class="eyebrow">Making an immediate impact</p>
      <blockquote class="quote" style="font-size:clamp(1.15rem,1.8vw,1.55rem)">…she has friends that are a couple, and they were in an unhealthy relationship and your presentation changed the way they now treat one another. She also said that she was able to look at herself and how she treated her partner and make changes as well.</blockquote>
      <span class="cite muted">Dawn M. Keys, Newport Prevention Coalition Coordinator</span>
    </div>
    {yt('ur2b6V1Pipk', 'A school leader’s perspective', label='2 min')}
  </div>
  <div class="wrap" style="margin-top:46px"><p class="eyebrow">Recent partner schools &amp; collaborators</p><div class="marquee logo-strip"><div class="marquee__track">{marq}{marq}</div></div></div>
</section>

<section class="band band--mist">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Heard on</p><h2>SafeBAE in conversation</h2></div>{btn('All 17 episodes', 'library.html#podcasts', 'slate', arrow=True)}</div>
    <div class="pods">{pod_html}</div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap fd">
    <div class="fd__photo">{img('crazy-daisy', 'Daisy Coleman')}<span class="daisy"></span></div>
    <div>
      <p class="eyebrow">#ForDaisy</p>
      <h2>Remembering our co-founder, Daisy Coleman.</h2>
      <p class="lede" style="color:rgba(255,255,255,.88)">As a teenage survivor, Daisy shared her story in the documentary <i>Audrie &amp; Daisy</i>. Her vision became the foundation of SafeBAE and helped ignite a youth-led movement. Every year, hundreds of people still find their way to this work through her story.</p>
      <p class="fd__quote">“All the organizing that happened after Daisy spoke out may not necessarily be a direct result but is certainly a ripple effect.” <span class="mono small" style="display:block;margin-top:6px;color:rgba(255,255,255,.7)">The Cut, “What Daisy Coleman Changed”</span></p>
      <div class="btns">{btn('Visit the tribute wall', 'fordaisy.html', 'mint', arrow=True)}{btn('Add your message', 'fordaisy.html#add', 'ghost')}</div>
    </div>
  </div>
</section>
{give_band()}
'''
    scripts = '<script>' + HOME_JS.replace('__COMP__', comp_data) + '</script>'
    page('index.html', 'SafeBAE', 'SafeBAE provides youth-led sexual violence prevention programs, consent education curriculum, and peer educator training for middle and high schools nationwide.',
         body, active='', body_class='home', fonts=film_font_link(), head_extra=f'<style>{HOME_CSS}</style>', scripts=scripts)

def cpet_player(extra_cls=''):
    caps = ['The only survivor-founded, youth-led org preventing sexual violence in schools', 'Why this training matters', 'Module 1 · Rape Culture & Shifting to a Culture of Respect', 'Consent starts way before sex. It starts when you’re a kid', 'The 6 Pillars of Consent', 'The foundation of a healthy relationship', 'BAEcode: real scripts for speaking up', 'Online safety & digital harassment', 'Supporting a partner who is a survivor', 'Wisdom from co-founder Daisy Coleman', 'Finish all 16 modules and become a Certified Peer Educator']
    slides = ''.join(f'<div class="player__slide{" on" if i==0 else ""}" data-cap="{esc(c)}">{img("preview"+str(i+1), c, loading="eager" if i==0 else "lazy")}</div>' for i, c in enumerate(caps))
    return f'''<div class="player {extra_cls}" data-player data-zoom data-interval="4500" aria-roledescription="carousel" aria-label="Sample slides from the Certified Peer Educator Training"><div class="player__bar"><i></i></div>{slides}<div class="player__ctl"><button data-prev aria-label="Previous slide">&#8249;</button><span class="player__cap"></span><button data-next aria-label="Next slide">&#8250;</button></div></div>'''

HOME_JS = r'''
(function(){
  var qs = document.querySelectorAll('.qs span'), i = 0, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(qs.length && !reduce){ setInterval(function(){ var cur = qs[i]; cur.classList.remove('on'); cur.classList.add('out'); i = (i+1) % qs.length; var nx = qs[i]; nx.classList.remove('out'); void nx.offsetWidth; nx.classList.add('on'); setTimeout(function(){ cur.classList.remove('out'); }, 800); }, 2600); }
  var C = __COMP__, ring = document.querySelector('.ring'), comp = document.getElementById('comp');
  function pick(n){ var c = C[n]; comp.innerHTML = '<div class="comp__n">' + (n+1) + '</div><h3>' + c.t + '</h3><p>' + c.d + '</p><a class="arrow-link" href="' + c.h + '">Learn more</a>'; document.querySelectorAll('.seg').forEach(function(s){ s.classList.toggle('on', +s.dataset.seg === n); }); document.querySelectorAll('.comp__list button').forEach(function(b){ b.setAttribute('aria-pressed', String(+b.dataset.seg === n)); }); ring.classList.add('has-active'); }
  document.querySelectorAll('.seg, .comp__list button').forEach(function(s){ s.addEventListener('click', function(){ pick(+s.dataset.seg); }); s.addEventListener('keydown', function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); pick(+s.dataset.seg); } }); s.addEventListener('mouseenter', function(){ if(s.classList.contains('seg')) pick(+s.dataset.seg); }); });
  if(ring) pick(0);
  var f = document.querySelector('[data-libsearch]');
  if(f) f.addEventListener('submit', function(e){ e.preventDefault(); var q = f.querySelector('input').value.trim(); try{ sessionStorage.setItem('libq', q); }catch(err){} var dest = 'library.html' + (q && /^[a-z0-9]+$/i.test(q) ? '#q-' + q : ''); if(window.SB && window.SB.go) window.SB.go(dest); else location.href = dest; });
})();
'''
