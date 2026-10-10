"""Four programs a school can request, each built on the SafeBAE 360° approach:
consent-curriculum, professional-development (Faculty & Staff Training), policy-reform-guide,
accountability-training. They sit under Request a Program next to assemblies.html
(pages_programs.py); 360-schools.html builds from pages_schools.py."""
from lib import *
from pages_home import ring_svg
from films_common import help_inline, HELPLINE_CSS
import math

CAL = 'https://calendly.com/shaelnorris/60min'
PODIA = 'https://safebae.podia.com/'
PILOT_PDF = 'https://www.safebae.org/wp-content/uploads/2025/06/SafeBAE-360-Schools-Pilot-Data.pdf'
POLICY_PODIA = 'https://safebae.podia.com/sexual-misconduct-policy-reform-guide'
ACC_PODIA = 'https://safebae.podia.com/7db95b2a-0fc8-47a7-b4f2-69c2a01232a9'
VC = 'https://checkyourvibe.org/'
VC_GUIDE = 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
EMAIL = 'info@safebae.org'
REQ = 'request-a-program.html'
ASK = 'request-a-program.html#start'
S360 = '360-schools.html'

_SVG, RCOMPS = ring_svg()   # (title, href, fill, ink) for the six components of the 360° approach


# ------------------------------------------------------------------ shared bits
def seg_path(i, cx, cy, R, r, gap):
    a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
    p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
    x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'


def mini_ring(cls='s3-mring', inner=22):
    segs = ''.join(f'<path d="{seg_path(i, 50, 50, 49, inner, 4)}" fill="{c[2]}"/>' for i, c in enumerate(RCOMPS))
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{segs}</svg>'


def pill():
    """The one line that ties a program to the approach behind it (same mark as assemblies.html)."""
    return f'<a class="s3-pill" href="{S360}">{mini_ring()}<span>Built on the <b>SafeBAE 360&deg;</b> approach</span></a>'


def crumbs(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in items) + '</nav>'


def hero(tone, crumb, h1, lede, media, proof, cls='', main='mint'):
    """One hero grammar for the four program pages: crumbs, 360 pill, H1 with a marker word, lede,
    the two actions, media on the right, and a line of facts along the foot."""
    return f'''<section class="s3-hero s3-hero--{tone} {cls}">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-hero__grid">
    <div class="rise s3-hero__txt">
      {crumbs([('Home', 'index.html'), ('Request a Program', REQ), (crumb, None)])}
      {pill()}
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <div class="btns">{btn('Request a program', ASK, main, arrow=True)}{btn('Book a 60-minute meeting', CAL, 'ghost')}</div>
    </div>
    {media}
  </div>
  <div class="wrap"><ul class="s3-proof">{''.join(f'<li>{p}</li>' for p in proof)}</ul></div>
</section>'''


# The Request a Program menu, as a strip on every program page.
PROGS = [
    ('assemblies', 'Assemblies', 'For schools taking a first step', 'assemblies.html'),
    ('curriculum', 'Consent Curriculum', 'For students and their teachers', 'consent-curriculum.html'),
    ('pd', 'Faculty & Staff Training', 'For teachers, staff and administrators', 'professional-development.html'),
    ('policy', 'Policy Reform Guide', 'For administrators and district leaders', 'policy-reform-guide.html'),
    ('accountability', 'Accountability Training', 'For students who have caused harm', 'accountability-training.html'),
    ('peer', 'Peer Educator Training', 'For student leaders', 'peer-educator.html'),
    ('rees', 'Anonymous Reporting Tool', 'With REES, for partner schools', '360-schools.html#rees'),
]


def programs(active):
    items = []
    for key, name, who, href in PROGS:
        if key == active:
            items.append(f'<span class="s3-prog is-on" aria-current="page"><small>You are here</small><b>{esc(name)}</b><i aria-hidden="true"><span class="daisy"></span></i></span>')
        else:
            items.append(f'<a class="s3-prog" href="{href}"><small>{esc(who)}</small><b>{esc(name)}</b><i aria-hidden="true">&rarr;</i></a>')
    items.append(f'<a class="s3-prog is-all" href="{REQ}"><small>Request a Program</small><b>All programs and pricing</b><i aria-hidden="true">&rarr;</i></a>')
    return f'''<section class="band band--mist band--tight s3-progs" id="programs">
  <div class="wrap">
    <div class="section-head"><div><h2>Programs schools can request</h2>
      <p class="lede lede--full">Every program is built on the SafeBAE 360° approach. Each one can be delivered on its own or as part of the whole.</p></div>
      <a class="btn btn--slate btn--sm section-head__act" href="{S360}">How 360° Schools works<span class="arr" aria-hidden="true">&rarr;</span></a></div>
    <nav class="s3-progs__grid" aria-label="SafeBAE programs for schools">{''.join(items)}</nav>
  </div>
</section>'''


PRICE = 'Cost should never be a barrier to prevention. SafeBAE offers flexible, sliding scale pricing tailored to each school’s needs and capacity, considering program scope, number of speakers and travel requirements.'


def cta(h2, lede, photo, photo_alt, sticker=None, extra='', pos='50% 30%'):
    """Closing request block, the same one 360-schools.html ends on."""
    acts = f'''<div class="s3-acts">
      <a class="s3-act s3-act--main" href="{ASK}"><span class="s3-act__k">Form</span><span><b>Request a program</b><small>Tell us what your school is looking for and how to follow up.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="s3-act" href="{CAL}" target="_blank" rel="noopener"><span class="s3-act__k">60 min</span><span><b>Book a 60-minute meeting</b><small>Talk through scope, timing and sliding scale pricing.</small></span><span class="go" aria-hidden="true">&#8599;</span></a>
      <a class="s3-act" href="mailto:{EMAIL}"><span class="s3-act__k">Email</span><span><b>{EMAIL}</b><small>Questions, training and technical assistance.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>'''
    st = f'<span class="sticker">{esc(sticker)}</span>' if sticker else ''
    return f'''<section class="s3-cta" id="bring"><div class="wrap s3-cta__grid">
    <div class="s3-cta__photo">{img(photo, photo_alt, style=f"object-position:{pos}")}{st}</div>
    <div class="s3-cta__body">
      <h2>{h2}</h2>
      <p class="lede">{lede}</p>
      {acts}
      <div class="s3-cta__foot"><p class="s3-price"><b>Flexible pricing.</b> {esc(PRICE)}</p>{extra}</div>
    </div>
  </div></section>'''


def checks(items, cls='s3-checks'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


# ---- the two new programs (same block as 360-schools.html)
AI_URL = 'https://ai-literacy.safebae.org'
AI_TOPICS = ['How AI works', 'How feeds and AI shape what we see and believe', 'AI and healthy relationships', 'Using AI well', 'Fake images', 'Sextortion']


def cal(mon, big):
    return f'<div class="s3-cal" aria-hidden="true"><span>{mon}</span><b>{big}</b></div>'


def new_programs(h2, lede):
    """Two cards with one anatomy (date, title, what it is, feature block, detail, actions); rows align by subgrid."""
    ai = f'''<article class="s3-np reveal">
      <div class="s3-np__top">{cal('Oct', '26&ndash;30')}<div><span class="s3-np__k">New &middot; Free &middot; Ages 13+</span><p class="s3-np__when">Launches during U.S. Media Literacy Week, October 26&ndash;30, 2026</p></div></div>
      <h3>SafeBAE AI Literacy Training</h3>
      <p>Six free, self-paced modules for high school and college students. Anyone 13 or older can take it.</p>
      <div class="s3-np__feat"><span class="s3-np__fk">What it covers</span><ul>{''.join(f'<li>{esc(t)}</li>' for t in AI_TOPICS)}</ul></div>
      <p>Educators can register for group access. Learners create a free account so their progress saves.</p>
      <div class="btns">{btn('About the training', 'ai-literacy.html', 'slate', arrow=True)}{btn('Open the training', AI_URL, 'ghost')}</div>
    </article>'''
    ssp = f'''<article class="s3-np reveal">
      <div class="s3-np__top">{cal('Nov', '2026')}<div><span class="s3-np__k">New program for schools</span><p class="s3-np__when">Launching November 2026</p></div></div>
      <h3>Sexual Strangulation Prevention</h3>
      <p>SafeBAE&rsquo;s new program for schools on sexual strangulation, which young people call &ldquo;choking.&rdquo;</p>
      <blockquote class="s3-np__feat s3-np__feat--line"><p>There&rsquo;s no safe way to choke someone.</p><cite class="s3-np__fk">Choking Hazard campaign</cite></blockquote>
      <p>The Choking Hazard campaign gives young people, parents and educators the evidence, myth vs. fact, the signs that need medical care, and free warning posters.</p>
      <div class="btns">{btn('Ask about the program', ASK, 'slate', arrow=True)}{btn('Choking Hazard campaign', 'choking-hazard.html', 'ghost')}</div>
    </article>'''
    return f'''<section class="band band--deep s3-new" id="new">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">New for 2026&ndash;27</p><h2>{h2}</h2><p class="lede lede--full">{lede}</p></div></div>
    <div class="s3-nps">{ai}{ssp}</div>
  </div>
</section>'''


def vibe_band():
    return f'''<section class="band band--teal s3-vibe" id="vibe-check">
  <div class="wrap s3-vibe__grid">
    <div class="s3-vibe__phone"><div class="s3-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div><span class="sticker" style="left:2%;top:15%">Anonymous</span><span class="sticker sticker--white sticker--r" style="right:3%;bottom:19%">Nothing is stored</span></div>
    <div class="s3-vibe__body">
      <div class="s3-vibe__mark"><span class="daisy"></span>Alongside the training &middot; Vibe Check by SafeBAE</div>
      <h2>Vibe Check: private reflection, never an assignment</h2>
      <p class="lede">Vibe Check pairs with the training: a free, anonymous self-assessment that helps students recognize unhealthy relationship behaviors and warning signs in themselves, and points them to real resources on consent, communication and accountability.</p>
      <p class="s3-vibe__p">No names, no accounts, and nothing is stored. It disappears when the browser closes. It is not a replacement for professional support: a young person who has been involved in a serious incident, experienced trauma or is in crisis should be connected with a qualified counselor or crisis service.</p>
      <div class="s3-vibe__tip"><b>Share it. Don’t assign it.</b><span>SafeBAE’s guide for adults advises against bringing Vibe Check up in the same moment as an incident, during a disciplinary conversation, or when emotions are running high. If it sounds like a punishment or an assignment, students won’t engage honestly.</span></div>
      <div class="btns">{btn('Open Vibe Check', VC, 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}{btn('Adult guide (PDF)', VC_GUIDE, 'ghost')}</div>
      <div class="s3-vibe__press"><span>As covered by</span>{img('the-guardian-logo-vector', 'The Guardian')}{img('vox-logo-svg-1', 'Vox')}{img('trendwatching-logo', 'TrendWatching')}</div>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------------ CSS
CSS = '''
/* ---- shared by the four program pages ---- */
.s3{--ck:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
.s3 main .eyebrow{color:var(--logo-teal)}
.s3 main :is(.band--slate,.band--deep,.band--logo,.s3-cta) .eyebrow{color:var(--mint)}
.s3 main .band--teal .eyebrow{color:#fff}
.s3 main .band--mint .eyebrow{color:var(--slate)}
.s3 main .section-head{margin-bottom:var(--head-gap)}
.s3 main .section-head .lede{max-width:none}
.s3 main :is(.band--slate,.band--deep,.band--logo) > .wrap > .section-head .lede{color:rgba(255,255,255,.9)}
.s3 main section[id]{scroll-margin-top:84px}
@media (max-width:860px){.s3 main .arrow-link{min-height:44px} .s3 main .btn--sm{min-height:44px}}

/* ---- hero: one grammar, four tones ---- */
.s3-hero{position:relative; overflow:hidden; color:#fff; background:var(--slate) var(--grain); --pf:var(--aqua); --pfd:var(--mint); --pfl:var(--line-dark); --h1:8.6cqi; --h1m:8.4vw}
.s3-hero--logo{background-color:var(--logo-teal)}
.s3-hero--deep{background-color:var(--slate-deep)}
.s3-hero--teal{background:var(--teal); --pf:#fff; --pfl:rgba(255,255,255,.34)}
.s3-hero--aqua{background:var(--aqua); color:var(--slate); --pf:var(--slate); --pfd:var(--teal); --pfl:var(--line)}
.s3-hero > .wrap{position:relative; z-index:1}
.s3-hero .wm-daisy{right:auto; left:-16%; bottom:-46%; --wm-o:.12}
.s3-hero--aqua .wm-daisy{color:var(--logo-teal); --wm-o:.12}
.s3-hero--teal .wm-daisy{color:var(--aqua); --wm-o:.16}
.s3-hero__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,60px); align-items:center; padding-block:clamp(40px,5vw,68px) clamp(28px,3.2vw,44px)}
.s3-hero__txt{min-width:0; container-type:inline-size}
.s3-hero .crumbs{margin-bottom:18px}
.s3-hero .crumbs a{padding-block:13px; margin-block:-13px}
.s3-hero--aqua .crumbs{color:var(--ink-soft)} .s3-hero--aqua .crumbs a{color:var(--logo-teal)}
.s3-hero--teal .crumbs{color:#fff} .s3-hero--teal .crumbs a{color:#fff; text-decoration:underline; text-decoration-color:rgba(255,255,255,.5); text-underline-offset:3px}
.s3-hero h1{font-weight:900; font-stretch:118%; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; font-size:clamp(1.9rem,var(--h1),3.9rem); margin:0 0 .42em; text-wrap:balance}
.s3-hero .mk{background:none; color:var(--mint); padding:0}
.s3-hero--aqua h1{color:var(--slate)}
.s3-hero--aqua .mk{background:linear-gradient(transparent 60%, var(--mint) 60% 92%, transparent 92%); color:inherit; padding:0 .06em}
.s3-hero .lede{max-width:none; color:rgba(255,255,255,.92); margin-bottom:1.3em}
.s3-hero--aqua .lede{color:var(--slate)}
.s3-hero--aqua :focus-visible{outline-color:var(--teal)}
.s3-hero__media{min-width:0; animation:sb-rise-r 1s .1s var(--ease) both}
.s3-pill{display:flex; width:max-content; max-width:100%; align-items:center; gap:10px; background:#fff; border:1px solid var(--line); border-radius:999px; padding:4px 16px 4px 4px; text-decoration:none; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:500; line-height:1.3; margin:0 0 18px; box-shadow:var(--shadow-soft); transition:box-shadow .2s var(--ease)}
.s3 main a.s3-pill{color:var(--slate)}
.s3-pill b{font-weight:700}
.s3-pill:hover{box-shadow:0 0 0 3px var(--mint)}
.s3-hero--aqua .s3-pill:hover{box-shadow:0 0 0 3px var(--teal)}
.s3-mring{width:40px; height:40px; flex:none}
.s3-proof{display:flex; flex-wrap:wrap; gap:8px clamp(20px,3vw,44px); margin:0; padding:16px 0 clamp(26px,3vw,40px); list-style:none; border-top:1px solid var(--pfl); font-weight:600; font-size:.95rem; color:var(--pf)}
.s3-proof li{margin:0; display:flex; align-items:center; gap:10px}
.s3-proof li::before{content:""; flex:none; width:9px; height:9px; background:var(--pfd); transform:rotate(45deg)}
.s3-shot{position:relative; margin:0}
.s3-shot img{width:100%; aspect-ratio:5/4; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.s3-shot .sticker{position:absolute; left:-14px; bottom:22px}
@media (min-width:901px) and (max-width:1180px){.s3-hero__txt .btns{display:inline-grid; grid-template-columns:minmax(0,1fr); gap:10px}}
@media (max-width:900px){
  .s3-hero__grid{grid-template-columns:1fr; gap:0}
  .s3-hero__txt{display:contents}
  .s3-hero__txt > *{order:1}
  .s3-hero__txt > .lede, .s3-hero__txt > .btns{order:3}
  .s3-hero__media{order:2; width:100%; margin:.3rem 0 1.5rem}
  .s3-hero h1{font-size:clamp(1.8rem,var(--h1m),3.4rem)}
  .s3-shot .sticker{left:10px}
  .s3-hero .wm-daisy{left:-52%; bottom:-12%; width:min(120vw,640px); --wm-o:.09}
}
@media (max-width:620px){.s3-hero .btns .btn{flex:1 1 100%}}
@media (max-width:520px){.s3-proof{flex-direction:column; gap:8px} .s3-pill{font-size:.7rem; letter-spacing:.06em}}

/* ---- check lists ---- */
.s3-checks{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.s3-checks li{position:relative; padding-left:32px; margin:0; font-weight:600; line-height:1.4}
.s3-checks li::before{content:""; position:absolute; left:0; top:.08em; width:22px; height:22px; border-radius:50%; background:var(--mint) var(--ck) center/14px no-repeat}
.s3-checks--2{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px 22px}
@media (max-width:620px){.s3-checks--2{grid-template-columns:1fr}}

/* ---- spec sheet ---- */
.s3-spec{margin:0; display:grid; border-top:1px solid var(--line)}
.s3-spec > div{display:grid; grid-template-columns:minmax(110px,.34fr) minmax(0,1fr); gap:4px 22px; padding:14px 0; border-bottom:1px solid var(--line)}
.s3-spec dt{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; padding-top:.34em}
.s3-spec dd{margin:0; font-weight:600; line-height:1.45}
@media (max-width:520px){.s3-spec > div{grid-template-columns:1fr}}

/* ---- program cards: label, name, text, link (same anatomy as the Request a Program menu) ---- */
.s3-cards{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.s3-card{display:grid; grid-template-rows:auto auto 1fr auto; row-gap:10px; padding:var(--pad-card); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); text-decoration:none; min-width:0; transition:transform .22s var(--ease), box-shadow .22s var(--ease)}
.s3 main a.s3-card{color:var(--slate)}
@supports (grid-template-rows:subgrid){ .s3-card{grid-row:span 4; grid-template-rows:subgrid} }
.s3-card__who{display:flex; align-items:flex-start; justify-content:space-between; gap:10px; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; line-height:1.45; color:var(--logo-teal)}
.s3-card h3{margin:0; font-size:clamp(1.3rem,1.8vw,1.5rem); line-height:1.1; color:var(--logo-teal)}
.s3-card p{margin:0; color:var(--ink-soft); font-size:.97rem; line-height:1.5}
.s3-card__go{display:flex; align-items:center; justify-content:space-between; gap:12px; margin-top:8px; padding-top:14px; border-top:1px solid var(--line); font-weight:700; font-size:.95rem; color:var(--logo-teal)}
.s3-card__go i,.s3-prog i{flex:none; width:36px; height:36px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s var(--ease)}
.s3-card:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.s3-card:hover .s3-card__go i, a.s3-prog:hover i{background:var(--mint); transform:translateX(3px)}
.s3-card.is-new{background:var(--mint); border-color:var(--mint)}
.s3-card.is-new .s3-card__who,.s3-card.is-new h3,.s3-card.is-new p,.s3-card.is-new .s3-card__go{color:var(--slate)}
.s3-card.is-new .s3-card__go{border-top-color:rgba(29,65,78,.28)}
.s3-card.is-new .s3-card__go i,.s3-prog.is-all i{background:var(--slate); color:var(--mint)}
.s3-card.is-new:hover .s3-card__go i, a.s3-prog.is-all:hover i{background:#fff; color:var(--slate)}
@media (max-width:900px){
  .s3-cards{grid-template-columns:1fr; gap:12px}
  .s3-card{grid-row:auto; grid-template-rows:auto; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); column-gap:clamp(18px,3vw,32px); grid-template-areas:"who text" "name text" "go go"; align-items:start}
  .s3-card__who{grid-area:who} .s3-card h3{grid-area:name} .s3-card p{grid-area:text} .s3-card__go{grid-area:go}
}
@media (max-width:620px){ .s3-card{grid-template-columns:1fr; grid-template-areas:"who" "name" "text" "go"} }

/* ---- programs strip ---- */
.s3-progs .section-head h2{font-size:clamp(1.6rem,2.8vw,2.4rem)}
.s3-progs .section-head .lede{font-size:1.06rem}
.s3-progs__grid{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.s3-prog{display:grid; grid-template-columns:minmax(0,1fr) auto; grid-template-rows:auto 1fr; gap:8px 12px; align-items:end; min-height:116px; padding:16px 16px 14px 18px; border-radius:14px; background:#fff; border:1px solid var(--line); text-decoration:none; min-width:0; transition:transform .2s var(--ease), box-shadow .2s var(--ease)}
.s3 main .s3-prog{color:var(--slate)}
.s3-prog small{grid-column:1/-1; align-self:start; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; line-height:1.4; color:var(--logo-teal)}
.s3-prog b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.2rem; line-height:1.12; color:var(--logo-teal)}
a.s3-prog:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.s3-prog.is-on{border-color:var(--slate); box-shadow:inset 0 0 0 1.5px var(--slate)}
.s3-prog.is-on small,.s3-prog.is-on b{color:var(--slate)}
.s3-prog.is-on i{background:var(--slate); color:var(--mint)}
.s3-prog.is-on i .daisy{width:20px; height:20px}
.s3-prog.is-all{background:var(--mint); border-color:var(--mint)}
.s3-prog.is-all small,.s3-prog.is-all b{color:var(--slate)}
@media (max-width:1040px){.s3-progs__grid{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-prog{min-height:100px}}
@media (max-width:520px){.s3-progs__grid{grid-template-columns:1fr; gap:10px} .s3-prog{min-height:0; grid-template-rows:auto auto; padding:14px 14px 14px 16px}}

/* ---- closing request block (same as 360-schools.html) ---- */
.s3-cta{background:var(--slate-deep) var(--grain); color:#fff; padding-block:var(--band)}
.s3-cta__grid{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.s3-cta__photo{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:360px}
.s3-cta__photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-cta__photo .sticker{position:absolute; left:16px; bottom:18px}
.s3-cta__body{min-width:0; display:flex; flex-direction:column}
.s3-cta h2{font-size:clamp(1.7rem,3.5vw,2.9rem); overflow-wrap:break-word; font-stretch:118%; text-transform:uppercase; font-weight:900; line-height:.95; letter-spacing:-.015em}
.s3-cta .lede{color:rgba(255,255,255,.9); margin-bottom:0}
.s3 .s3-cta .link{color:var(--mint)}
.s3-acts{display:grid; gap:10px; margin:22px 0 18px}
.s3-act{display:grid; grid-template-columns:68px minmax(0,1fr) auto; gap:16px; align-items:center; padding:15px 18px; border-radius:14px; background:rgba(255,255,255,.06); border:1.5px solid var(--line-dark); color:#fff!important; text-decoration:none; transition:border-color .2s, transform .2s var(--ease), background .2s}
.s3-act:hover{border-color:var(--mint); transform:translateX(4px); background:rgba(255,255,255,.1)}
.s3-act b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.2rem; line-height:1.15; overflow-wrap:anywhere}
.s3-act small{display:block; opacity:.86; font-size:.9rem; line-height:1.4; margin-top:2px}
.s3-act__k{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.s3-act .go{width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.1); font-weight:800; transition:transform .2s var(--ease)}
.s3-act:hover .go{transform:translateX(3px)}
.s3-act--main{background:var(--mint); color:var(--slate)!important; border-color:var(--mint)}
.s3-act--main .s3-act__k{color:var(--slate)}
.s3-act--main .go{background:var(--slate); color:var(--mint)}
.s3-act--main:hover{border-color:#fff; background:var(--mint)}
.s3-cta__foot{margin-top:auto; display:grid; grid-template-columns:minmax(0,1fr) auto; gap:14px 28px; align-items:center; border-top:1px solid var(--line-dark); padding-top:16px}
.s3-price{font-size:.92rem; color:rgba(255,255,255,.82); margin:0}
.s3-price b{color:#fff}
@media (max-width:900px){.s3-cta__grid{grid-template-columns:1fr; gap:0} .s3-cta__body{display:contents} .s3-cta__body > *{order:3} .s3-cta__body > h2{order:1} .s3-cta__photo{order:2; min-height:0; aspect-ratio:16/11; margin-bottom:22px} .s3-cta__foot{grid-template-columns:1fr; margin-top:0}}
@media (max-width:480px){.s3-act{grid-template-columns:minmax(0,1fr) auto; gap:4px 12px} .s3-act__k{grid-column:1/-1}}

/* ---- pilot stat cards (same anatomy as 360-schools.html) ---- */
.s3-stat{background:#fff; border-radius:14px; padding:20px 22px 22px; min-width:0; display:flex; flex-direction:column; gap:10px; box-shadow:0 10px 24px -20px rgba(22,53,64,.5)}
.s3-stat__n{display:flex; align-items:baseline; gap:12px; flex-wrap:wrap}
.s3-stat__n b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.4rem,3.7vw,3.3rem); line-height:.9; letter-spacing:-.02em; color:var(--logo-teal); font-variant-numeric:tabular-nums}
.s3-stat .k{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-meter{display:block; height:6px; border-radius:6px; background:rgba(29,65,78,.12); overflow:hidden}
.s3-meter i{display:block; height:100%; border-radius:6px; background:var(--teal); width:calc(var(--v) / 60 * 100%); transition:width 1.1s var(--ease)}
.s3-stat p{margin:0; font-size:.97rem; line-height:1.45; font-weight:500}
'''

CSS_NEW = '''
/* ---- new for 2026-27: two cards, one anatomy (same as 360-schools.html) ---- */
.s3-new{overflow:hidden}
.s3-new > .wrap{position:relative; z-index:1}
.s3-new .wm-daisy{right:-12%; bottom:-46%; --wm-o:.14}
.s3-nps{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(6,auto); gap:0 var(--gap)}
.s3-np{grid-row:span 6; display:grid; grid-template-rows:subgrid; row-gap:14px; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:var(--shadow-soft); min-width:0}
.s3-np h3{margin:4px 0 0; font-size:clamp(1.35rem,2vw,1.75rem)}
.s3-np > p{margin:0; color:var(--ink-soft); font-size:1rem}
.s3-np .btns{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; padding-top:6px; align-items:stretch}
.s3-np .btns .btn{padding-inline:.7em; font-size:.97rem}
.s3-np__top{display:flex; gap:18px; align-items:center; padding-bottom:16px; border-bottom:1px solid var(--line)}
.s3-np__k,.s3-np__fk{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); font-style:normal}
.s3 .s3-np .s3-np__when{margin:4px 0 0; font-weight:700; color:var(--slate); line-height:1.3}
.s3-cal{flex:none; width:88px; border-radius:12px; overflow:hidden; text-align:center; background:var(--slate); color:#fff; box-shadow:4px 4px 0 var(--mint); transform:rotate(-3deg)}
.s3-cal span{display:block; background:var(--mint); color:var(--slate); font-family:var(--mono); font-size:.72rem; letter-spacing:.16em; text-transform:uppercase; font-weight:700; padding:4px 0}
.s3-cal b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.4rem; line-height:1; padding:12px 4px}
.s3-np__feat{margin:2px 0; padding:16px 18px; border-radius:14px; background:var(--aqua); color:var(--slate); display:flex; flex-direction:column; justify-content:center; gap:10px; min-width:0}
.s3-np__feat ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px 18px}
.s3-np__feat li{position:relative; margin:0; padding-left:18px; font-weight:700; font-size:.95rem; line-height:1.3}
.s3-np__feat li::before{content:""; position:absolute; left:0; top:.42em; width:8px; height:8px; background:var(--teal); transform:rotate(45deg)}
.s3-np__feat--line{border-left:6px solid var(--slate); border-radius:0 14px 14px 0}
.s3 .s3-np__feat--line p{margin:0; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.35rem,2.2vw,1.85rem); line-height:1.08; letter-spacing:-.01em; color:var(--slate)}
@media (max-width:860px){.s3-nps{grid-template-columns:1fr; grid-template-rows:none; gap:var(--gap)} .s3-np{grid-row:auto; grid-template-rows:none}}
@media (max-width:460px){.s3-np__feat ul{grid-template-columns:1fr} .s3-np .btns{grid-template-columns:1fr}}
'''

CSS_VIBE = '''
/* ---- vibe check band (same as 360-schools.html) ---- */
.s3-vibe__grid{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:center}
.s3-vibe__phone{position:relative}
.s3-vibe__phone .sticker{position:absolute; z-index:2}
.s3-phone{position:relative; width:min(318px,72vw); margin-inline:auto; aspect-ratio:390/800; border-radius:44px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6), 0 0 0 2px rgba(255,255,255,.08); overflow:hidden; transform:rotate(3deg); transition:transform .6s var(--ease)}
.s3-vibe__phone:hover .s3-phone{transform:rotate(0deg) translateY(-6px)}
.s3-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.s3-vibe__body{min-width:0}
.s3-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:#fff; margin-bottom:14px}
.s3-vibe__mark .daisy{color:var(--mint); width:34px; height:34px}
.s3-vibe h2{font-size:clamp(1.8rem,3.1vw,2.7rem); margin-bottom:.45em}
.s3-vibe .lede{color:#fff; font-size:clamp(1.06rem,1.3vw,1.22rem); margin-bottom:.8em}
.s3-vibe .btns{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; align-items:stretch}
.s3-vibe .btns .btn{padding-inline:.6em}
@media (max-width:1180px){.s3-vibe .btns{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-vibe .btns .btn:first-child{grid-column:1/-1}}
@media (max-width:460px){.s3-vibe .btns{grid-template-columns:1fr}}
.s3-vibe__p{color:rgba(255,255,255,.92); margin:0}
.s3-vibe__tip{display:grid; gap:4px; background:var(--slate); border-left:6px solid var(--mint); border-radius:14px; padding:16px 20px; margin:18px 0 20px}
.s3-vibe__tip b{font-family:var(--display); font-stretch:110%; font-size:1.2rem; color:var(--mint)}
.s3-vibe__tip span{font-size:.97rem; color:rgba(255,255,255,.9)}
.s3-vibe__press{display:flex; flex-wrap:wrap; gap:14px 28px; align-items:center; margin-top:22px; padding-top:18px; border-top:1px solid rgba(255,255,255,.3)}
.s3-vibe__press img{height:30px; width:auto; filter:brightness(0) invert(1); opacity:.95}
.s3-vibe__press span{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:#fff}
@media (max-width:860px){.s3-vibe__grid{grid-template-columns:1fr; gap:0} .s3-vibe__body{display:contents} .s3-vibe__body > *{order:3} .s3-vibe__body > .s3-vibe__mark, .s3-vibe__body > h2{order:1} .s3-vibe__phone{order:2; max-width:420px; margin:10px auto 30px; width:100%} .s3-vibe__press span{flex-basis:100%} .s3-phone{width:min(230px,58vw)}}
'''

CSS_CURR = '''
/* ---- curriculum hero: the lesson board ---- */
.s3-ch{--h1:10cqi; --h1m:8.6vw}
.s3-ch .s3-hero__grid{grid-template-columns:minmax(0,5fr) minmax(0,7fr)}
.s3-ch .btns{display:inline-grid; grid-template-columns:minmax(0,1fr); gap:10px; justify-items:stretch}
.s3-board__cap{display:flex; justify-content:space-between; align-items:baseline; gap:6px 20px; flex-wrap:wrap; margin:0 0 12px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-tiles{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px}
.s3-tile{position:relative; display:grid; grid-template-columns:auto minmax(0,1fr); align-items:center; gap:12px; min-height:82px; padding:12px 14px; border-radius:14px; text-decoration:none; background:var(--tb); border:2px solid var(--tbd, transparent); transition:transform .2s var(--ease), box-shadow .2s; min-width:0}
.s3 main a.s3-tile{color:var(--tc)}
.s3-tile:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.s3-tile b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(1.6rem,2.2vw,2.1rem); line-height:.9; min-width:1.2em; text-align:center}
.s3-tile span{font-size:.92rem; font-weight:700; line-height:1.22}
.u-core{--tb:var(--slate); --tc:#fff} .u-core b{color:var(--mint)}
.u-found{--tb:var(--logo-teal); --tc:#fff} .u-found b{color:var(--aqua)}
.u-heal{--tb:#fff; --tc:var(--slate); --tbd:var(--teal)} .u-heal b{color:var(--teal)}
.u-just{--tb:var(--mint); --tc:var(--slate)}
@media (prefers-reduced-motion:no-preference){.s3-tile{animation:s3pop .5s var(--ease) backwards; animation-delay:calc(var(--i) * 35ms + .2s)}}
@keyframes s3pop{from{transform:translateY(10px) scale(.95)}}
.s3-legend{list-style:none; margin:14px 0 0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:2px 20px}
.s3-legend li{margin:0; min-width:0}
.s3-legend a{display:flex; align-items:center; gap:10px; min-height:36px; text-decoration:none; font-weight:700; font-size:.95rem; line-height:1.25}
.s3 main .s3-legend a{color:var(--slate)}
.s3-legend i{flex:none; width:16px; height:16px; border-radius:5px; background:var(--tb); border:2px solid var(--tbd, transparent)}
.s3-legend small{margin-left:auto; font-family:var(--mono); font-size:.8rem; letter-spacing:.06em; font-weight:600; color:var(--logo-teal); white-space:nowrap}
.s3-legend a:hover span{text-decoration:underline; text-decoration-color:var(--teal); text-underline-offset:3px}
@media (max-width:1100px){
  .s3-ch .s3-hero__grid{grid-template-columns:1fr; gap:0}
  .s3-ch .s3-hero__txt{display:contents}
  .s3-ch .s3-hero__txt > *{order:1}
  .s3-ch .s3-hero__txt > .lede, .s3-ch .s3-hero__txt > .btns{order:3}
  .s3-ch .s3-hero__media{order:2; width:100%; margin:.3rem 0 1.5rem}
  .s3-ch h1{font-size:clamp(1.8rem,var(--h1m),3.4rem)}
  .s3-ch .btns{display:flex}
}
@media (max-width:560px){
  .s3-tiles{grid-template-columns:repeat(5,minmax(0,1fr)); gap:6px}
  .s3-tile{grid-template-columns:1fr; min-height:0; aspect-ratio:1; padding:0; place-items:center; border-radius:12px}
  .s3-tile span{position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap}
  .s3-tile b{font-size:1.5rem}
  .s3-legend{grid-template-columns:1fr}
}

/* ---- the 15 lessons: unit tabs on one sheet ---- */
.s3-utabs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:8px; margin:0}
.s3-utabs button{font:inherit; cursor:pointer; text-align:left; padding:14px 18px 16px; border-radius:16px 16px 0 0; border:0; background:rgba(255,255,255,.08); color:#fff; display:flex; flex-direction:column; gap:5px; min-width:0; transition:background .2s}
.s3-utabs button small{display:flex; align-items:center; gap:8px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.s3-utabs button small i{flex:none; width:13px; height:13px; border-radius:4px; background:var(--tb); border:2px solid var(--tbd, rgba(255,255,255,.5))}
.s3-utabs button span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.2rem; line-height:1.15}
.s3-utabs button:hover{background:rgba(255,255,255,.17)}
.s3-utabs button[aria-selected="true"]{background:#fff; color:var(--slate)}
.s3-utabs button[aria-selected="true"] small{color:var(--logo-teal)}
.s3-utabs button[aria-selected="true"] small i{border-color:var(--tbd, var(--tb))}
.s3-utabs button:focus-visible{outline-offset:-5px}
.s3-utabs button[aria-selected="true"]:focus-visible{outline-color:var(--teal)}
.s3-unit{background:#fff; color:var(--slate); border-radius:0 0 var(--r-xl) var(--r-xl); padding:var(--pad-card); box-shadow:var(--shadow-soft)}
.s3-unit :focus-visible{outline-color:var(--teal)}
.s3-unit__intro{margin:0 0 20px; padding-bottom:20px; border-bottom:1px solid var(--line); font-size:1.12rem; font-weight:500; line-height:1.5}
.s3-lessons{display:grid; grid-template-columns:repeat(var(--n),minmax(0,1fr)); gap:12px}
.s3-lesson{display:grid; grid-template-columns:auto minmax(0,1fr); gap:4px 16px; align-items:center; align-content:center; min-height:92px; padding:14px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line); scroll-margin-top:150px; transition:background .3s, box-shadow .3s}
.s3-lesson__n{grid-row:1 / span 2; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.3rem; line-height:1; color:var(--teal); min-width:1.25em; text-align:center}
.s3-lesson__t{align-self:end; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.18rem; line-height:1.2; color:var(--logo-teal)}
.s3-lesson__t:last-child{grid-row:1 / span 2; align-self:center}
.s3-lesson__rel{align-self:start; justify-self:start; font-size:.93rem; font-weight:600; text-decoration:none; line-height:1.35}
.s3 main .s3-lesson__rel{color:var(--ink-soft)}
.s3-lesson__rel b{font-weight:700; color:var(--logo-teal); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
.s3-lesson__rel:hover b{text-decoration-color:var(--teal)}
.s3-lesson.is-hl{background:var(--aqua); box-shadow:0 0 0 3px var(--mint)}
@media (max-width:900px){
  .s3-utabs{grid-template-columns:repeat(2,minmax(0,1fr))}
  .s3-utabs button{border-radius:14px; padding:12px 14px}
  .s3-utabs button span{font-size:1.05rem}
  .s3-unit{border-radius:var(--r-xl); margin-top:10px}
  .s3-lessons{grid-template-columns:repeat(2,minmax(0,1fr))}
  .s3-lessons--3{grid-template-columns:1fr}
}
@media (max-width:620px){.s3-lessons{grid-template-columns:1fr} .s3-lesson{min-height:76px; padding:12px 14px} .s3-lesson__n{font-size:1.9rem}}

/* ---- three ways to deliver it ---- */
.s3-ways{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0 var(--gap)}
.s3-way{min-width:0; display:grid; grid-template-rows:auto auto 1fr auto}
@supports (grid-template-rows:subgrid){ .s3-way{grid-row:span 4; grid-template-rows:subgrid} }
.s3-way__img{position:relative; aspect-ratio:4/3; border-radius:var(--r-xl); overflow:hidden; background:var(--slate)}
.s3-way__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.s3-way:hover .s3-way__img img{transform:scale(1.035)}
.s3-way h3{margin:20px 4px 0; font-size:clamp(1.3rem,1.8vw,1.5rem); color:var(--logo-teal)}
.s3-way p{margin:8px 4px 0; color:var(--ink-soft); font-size:1rem; line-height:1.5}
.s3-way .arrow-link{margin:14px 4px 0; align-self:end; justify-self:start}
@media (max-width:860px){.s3-ways{grid-template-columns:1fr; gap:22px 0} .s3-way{grid-row:auto; grid-template-rows:auto auto auto; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); column-gap:18px} .s3-way__img{grid-row:1 / 4} .s3-way h3{margin-top:0; align-self:end} .s3-way p{align-self:start} .s3-way .arrow-link{margin-top:4px; align-self:start}}
@media (max-width:560px){.s3-ways{gap:28px 0} .s3-way{display:block} .s3-way h3{margin-top:16px} .s3-way .arrow-link{margin-top:8px}}

/* ---- facilitator's guide ---- */
.s3-fac{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap) clamp(28px,5vw,72px); align-items:center}
.s3-fac__body{min-width:0}
.s3-fac__body .lede{color:#fff}
.s3-fac__body > p:not(.eyebrow):not(.lede){color:rgba(255,255,255,.9)}
.s3-inside{margin-top:22px; padding-top:20px; border-top:1px solid var(--line-dark)}
.s3-inside > b{display:block; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.25rem; line-height:1.2; margin-bottom:14px; color:var(--mint)}
.s3-doc{margin:0; min-width:0; padding:14px 18px 0 6px}
.s3-doc__stack{position:relative}
.s3-doc__stack::before{content:""; position:absolute; inset:0; border-radius:14px; background:var(--aqua); opacity:.55; transform:rotate(-3.2deg)}
.s3-doc__sheet{position:relative; background:#fff; border-radius:14px; padding:10px; box-shadow:0 34px 60px -30px rgba(0,0,0,.65); transform:rotate(1.3deg); transition:transform .6s var(--ease)}
.s3-doc:hover .s3-doc__sheet{transform:rotate(0deg)}
.s3-doc__sheet img{width:100%; height:auto; border-radius:6px}
.s3-doc .sticker{position:absolute; right:-18px; top:-14px; z-index:2}
.s3-doc figcaption{position:relative; margin-top:24px; font-size:.92rem; color:rgba(255,255,255,.86)}
.s3-fac__foot{grid-column:1/-1; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap) clamp(28px,5vw,72px); align-items:stretch; margin-top:clamp(8px,1.4vw,18px)}
.s3-fac__foot > *{min-width:0}
.s3-email{display:flex; flex-direction:column; justify-content:center; gap:6px; padding:18px 22px; border-radius:14px; background:#fff; color:var(--slate)}
.s3-email small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-email p{margin:0; font-size:.98rem; font-weight:500; color:var(--ink-soft)}
.s3-email .s3-email__a{display:flex; flex-wrap:wrap; align-items:center; gap:8px 14px}
.s3 main .s3-email__a a{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.3rem,2vw,1.6rem); line-height:1.1; color:var(--logo-teal); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:4px; overflow-wrap:anywhere}
.s3-email__a button{font:inherit; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; min-height:32px; padding:4px 12px; border:0; border-radius:8px; background:var(--slate); color:#fff; cursor:pointer}
.s3-email__a button:hover{background:var(--teal)}
.s3-email :focus-visible{outline-color:var(--teal)}
@media (max-width:900px){.s3-fac{grid-template-columns:1fr; gap:0} .s3-fac__body{display:contents} .s3-fac__body > *{order:3} .s3-fac__body > .eyebrow, .s3-fac__body > h2{order:1} .s3-doc{order:2; max-width:560px; margin:4px 0 28px} .s3-fac__foot{order:4; grid-template-columns:1fr; gap:var(--gap); margin-top:26px}}

/* ---- the package ---- */
.s3-incl{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.s3-incl__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:380px; margin:0}
.s3-incl__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-incl__img .sticker{position:absolute; right:16px; bottom:18px}
.s3-incl__body{min-width:0; display:flex; flex-direction:column}
.s3-incl__body h2{margin-bottom:.4em}
.s3-incl__body .lede{margin-bottom:0}
.s3-pack{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:22px 0 6px}
.s3-pack div{border-radius:14px; padding:16px 18px 18px; background:var(--mist); border:1px solid var(--line); min-width:0}
.s3-pack small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin-bottom:6px}
.s3-pack b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.2; color:var(--logo-teal)}
.s3-incl__body .s3-spec{border-top:0; margin-bottom:22px}
.s3-incl__body .btns{margin-top:auto}
@media (max-width:900px){.s3-incl{grid-template-columns:1fr; gap:0} .s3-incl__body{display:contents} .s3-incl__body > *{order:3} .s3-incl__body > h2{order:1} .s3-incl__img{order:2; min-height:0; aspect-ratio:16/11; margin-bottom:22px}}
@media (max-width:520px){.s3-pack{grid-template-columns:1fr}}
'''

CSS_PD = '''
.s3-pdh{--h1:8.8cqi; --h1m:8.6vw}
/* ---- what the trainings cover ---- */
.s3-topics{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap) clamp(28px,4vw,56px); align-items:stretch}
.s3-focus{list-style:none; margin:0; padding:0; display:grid; border-top:1px solid var(--line); min-width:0}
.s3-focus li{margin:0; display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:4px 18px; align-items:center; padding:16px 4px; border-bottom:1px solid var(--line)}
.s3-focus li::before{content:""; width:28px; height:28px; border-radius:50%; background:var(--mint) var(--ck) center/17px no-repeat}
.s3-focus b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.12rem,1.5vw,1.26rem); line-height:1.22; color:var(--logo-teal); text-wrap:balance}
.s3-focus .arrow-link{font-size:.95rem; white-space:nowrap}
.s3-focus .arrow-link small{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--ink-soft); margin-right:.1em}
.s3-fact{margin:0; background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; gap:14px; min-width:0; container-type:inline-size}
.s3-fact figcaption{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.s3-fact blockquote{margin:auto 0; padding:0}
.s3-fact blockquote p{margin:0; font-family:var(--display); font-weight:700; font-stretch:106%; font-size:clamp(1.12rem,1.5vw,1.3rem); line-height:1.25; text-wrap:balance}
.s3-fact blockquote b{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(4rem,34cqi,6.6rem); line-height:.84; letter-spacing:-.04em; color:var(--mint); margin:.14em 0 .12em -.03em}
.s3-fact cite{display:block; margin-top:12px; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.s3-fact__foot{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:4px 16px; padding-top:14px; border-top:1px solid var(--line-dark)}
.s3-fact__foot span{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.1rem}
.s3 main .s3-fact .arrow-link{color:var(--mint)}
.s3-topics__help{grid-column:1/-1}
@media (max-width:1100px){.s3-focus li{grid-template-columns:auto minmax(0,1fr)} .s3-focus .arrow-link{grid-column:2; white-space:normal}}
@media (max-width:860px){.s3-topics{grid-template-columns:1fr} .s3-fact blockquote b{font-size:clamp(4rem,20cqi,6.6rem)}}

/* ---- how trainings are delivered ---- */
.s3-fmt{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.s3-fmt__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:340px; margin:0}
.s3-fmt__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-fmt__card{background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); min-width:0; box-shadow:var(--shadow-soft); display:flex; flex-direction:column}
.s3-fmt__card h2{font-size:clamp(1.7rem,3vw,2.5rem); margin-bottom:.35em}
.s3-fmt__card > p{color:var(--ink-soft); margin:0}
.s3 main .s3-fmt__card a{color:var(--logo-teal)}
.s3-modes{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:20px 0 18px}
.s3-modes div{border-radius:14px; padding:18px 16px; background:var(--aqua); text-align:center; min-width:0}
.s3-modes b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.15rem,2.2vw,1.6rem); line-height:1; text-transform:uppercase}
.s3-modes span{display:block; margin-top:6px; font-size:.95rem; font-weight:600}
.s3-fmt__card .s3-spec{margin-top:auto}
.s3-fmt__card .s3-spec > div:last-child{border-bottom:0; padding-bottom:0}
@media (max-width:900px){.s3-fmt{grid-template-columns:1fr} .s3-fmt__img{min-height:0; aspect-ratio:16/10}}

/* ---- what teachers reported: the chart ---- */
.s3-tgrid{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch}
.s3-chart{margin:0; background:#fff; border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:var(--shadow-soft); display:flex; flex-direction:column; min-width:0}
.s3-chart figcaption{display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:4px 20px; margin-bottom:18px; padding-bottom:16px; border-bottom:1px solid var(--line)}
.s3-chart figcaption b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.2rem,1.7vw,1.45rem); line-height:1.2; color:var(--logo-teal)}
.s3-chart figcaption span{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--ink-soft)}
.s3-bars{list-style:none; margin:0; padding:0; flex:1; display:grid; align-content:space-between; gap:16px; border-left:2px solid var(--slate)}
.s3-bar{margin:0; min-width:0}
.s3-bar__t{margin:0 0 7px; padding-left:14px; font-weight:600; font-size:1rem; line-height:1.35}
.s3-bar__track{display:flex; align-items:center; gap:12px}
.s3-bar__track i{display:block; flex:none; height:24px; border-radius:0 6px 6px 0; background:var(--teal); width:calc(var(--v) / 58 * (100% - 5.4rem)); transition:width 1.1s var(--ease), background .2s; transition-delay:calc(var(--i) * 90ms), 0s}
@media (hover:hover){.s3-bar:hover .s3-bar__track i{background:var(--logo-teal)}}
.s3-bar__track b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:1.75rem; line-height:1; letter-spacing:-.02em; color:var(--slate); font-variant-numeric:tabular-nums}
.js .s3-chart:not(.in) .s3-bar__track i{width:0}
.s3-tside{display:grid; grid-template-rows:1fr 1fr; gap:var(--gap); min-width:0}
.s3-tside .s3-stat{justify-content:center; padding:var(--pad-card); border-radius:var(--r-xl); gap:12px}
.s3-tside .s3-stat__n b{font-size:clamp(2.8rem,4.4vw,3.8rem)}
.s3-tside .s3-stat p{font-size:1rem}
.js .s3-tgrid:not(.in) .s3-meter i{width:0}
.s3-tq{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch; margin-top:var(--gap)}
.s3-voice{background:rgba(255,255,255,.62); border-radius:var(--r-xl); padding:20px var(--pad-card); margin:0; display:flex; flex-direction:column; justify-content:center; gap:10px; min-width:0}
.s3-voice p{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.12rem,1.6vw,1.4rem); line-height:1.28; margin:0; text-wrap:pretty}
.s3-voice cite{display:block; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.s3-tq .btns{display:grid; grid-template-columns:minmax(0,1fr); gap:12px; align-content:center}
@media (max-width:1000px){.s3-tgrid,.s3-tq{grid-template-columns:1fr} .s3-tside{grid-template-rows:none; grid-template-columns:repeat(2,minmax(0,1fr))} .s3-tq .btns{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.s3-tside{grid-template-columns:1fr} .s3-tq .btns{grid-template-columns:1fr} .s3-bar__track b{font-size:1.5rem} .s3-bar__track i{width:calc(var(--v) / 58 * (100% - 4.6rem))}}
'''

CSS_POL = '''
.s3-ph{--h1:8.2cqi; --h1m:8.2vw}
/* ---- hero: the two guides ---- */
.s3-covers{position:relative; aspect-ratio:1/.98; width:100%; max-width:500px; margin-inline:auto}
.s3-cover{position:absolute; display:block; background:#fff; padding:9px; border-radius:14px; box-shadow:0 30px 60px -28px rgba(0,0,0,.55); text-decoration:none; transition:transform .45s var(--ease), box-shadow .3s}
.s3-cover img{border-radius:5px; width:100%; height:auto}
.s3-cover--student{right:1%; top:1%; width:49%; transform:rotate(5deg)}
.s3-cover--admin{left:3%; top:9%; width:59%; transform:rotate(-4deg); z-index:2}
.s3-cover--student:hover{transform:rotate(2deg) translateY(-8px)}
.s3-cover--admin:hover{transform:rotate(-1.5deg) translateY(-8px)}
.s3-cover .sticker{position:absolute; white-space:nowrap}
.s3-cover--student .sticker{right:-10px; top:-16px}
.s3-cover--admin .sticker{left:-16px; bottom:-30px}
@media (max-width:900px){.s3-covers{max-width:420px}}
@media (max-width:520px){.s3-cover .sticker{font-size:.875rem; padding:.4em .6em .36em} .s3-cover--student .sticker{right:4px} .s3-cover--admin .sticker{left:-8px}}

/* ---- the shifting rules ---- */
.s3-shift{position:relative}
.s3-shift__track{position:relative; height:118px; margin-bottom:18px}
.s3-shift__track svg{position:absolute; inset:0; width:100%; height:100%; overflow:visible; transition:clip-path 1.9s var(--ease)}
.s3-shift__track svg path{fill:none; stroke:var(--teal); stroke-width:4; stroke-linecap:round; stroke-linejoin:round; vector-effect:non-scaling-stroke}
.s3-shift__track svg .g{stroke:var(--line); stroke-width:1}
.s3-shift__track svg .d{stroke-dasharray:3 9}
.s3-shift__ax{position:absolute; left:0; margin:0; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--ink-soft); line-height:1}
.s3-shift__ax--hi{top:-2px}
.s3-shift__dot{position:absolute; left:calc(var(--x) * 1%); top:calc(var(--y) * 1%); width:30px; height:30px; margin:-15px 0 0 0; border-radius:50%; background:#fff; border:4px solid var(--teal); transition:transform .5s var(--ease); transition-delay:var(--dl,0s)}
.s3-shift__dot--now{background:var(--coral); border-color:var(--slate); box-shadow:0 0 0 6px rgba(254,113,113,.28)}
.s3-shift__tag{position:absolute; left:calc(var(--x) * 1%); top:34px; margin:0; padding:3px 8px; border-radius:5px; background:var(--aqua); font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--slate); line-height:1.3; white-space:nowrap; transition:opacity .4s 1.1s}
.s3-shift__arrow{position:absolute; right:-2px; top:calc(var(--y) * 1%); margin-top:-9px; border-left:15px solid var(--teal); border-block:9px solid transparent; transition:opacity .3s 1.7s}
.s3-shift__list{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr))}
.s3-shift__list li{margin:0; min-width:0; padding-right:clamp(18px,3vw,44px)}
.s3-shift__y{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2rem,3.4vw,2.9rem); line-height:1; letter-spacing:-.02em; color:var(--teal)}
.s3-shift__list .is-now .s3-shift__y{color:var(--slate)}
.s3-shift__list h3{margin:.5em 0 .3em; font-size:clamp(1.25rem,1.8vw,1.5rem); color:var(--logo-teal)}
.s3-shift__list p{margin:0; color:var(--ink-soft); font-size:1rem}
.js .s3-shift:not(.in) .s3-shift__track svg{clip-path:inset(-20px 100% -20px 0)}
.s3-shift__track svg{clip-path:inset(-20px -20px -20px 0)}
.js .s3-shift:not(.in) .s3-shift__dot{transform:scale(0)}
.js .s3-shift:not(.in) .s3-shift__tag, .js .s3-shift:not(.in) .s3-shift__arrow{opacity:0}
@media (max-width:760px){
  .s3-shift__track{display:none}
  .s3-shift__list{grid-template-columns:1fr; gap:26px; position:relative; padding-left:46px}
  .s3-shift__list::before{content:""; position:absolute; left:13px; top:12px; bottom:10px; width:4px; border-radius:4px; background:var(--teal)}
  .s3-shift__list li{position:relative; padding-right:0}
  .s3-shift__list li::before{content:""; position:absolute; left:-46px; top:2px; width:30px; height:30px; border-radius:50%; background:#fff; border:4px solid var(--teal)}
  .s3-shift__list li.is-now::before{background:var(--coral); border-color:var(--slate)}
}
.s3-stake{margin-top:clamp(30px,4vw,48px); padding:clamp(24px,3.2vw,42px) clamp(22px,3.4vw,44px); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.s3-stake__big{margin:0; font-family:var(--display); font-weight:900; font-stretch:116%; font-size:clamp(1.5rem,3vw,2.6rem); line-height:1.02; letter-spacing:-.02em; text-wrap:balance}
.s3-stake__two{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px clamp(24px,4vw,56px); margin-top:clamp(18px,2.2vw,26px); padding-top:clamp(16px,2vw,22px); border-top:1px solid var(--line-dark)}
.s3-stake__two div{min-width:0}
.s3-stake__two small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin-bottom:6px}
.s3-stake__two b{display:block; font-family:var(--display); font-weight:700; font-stretch:106%; font-size:clamp(1.12rem,1.6vw,1.34rem); line-height:1.25}
.s3-stake__row{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:12px 32px; margin-top:clamp(18px,2.2vw,26px); padding-top:clamp(16px,2vw,22px); border-top:1px solid var(--line-dark)}
.s3-stake__row p{margin:0; font-size:1.04rem; font-weight:500; color:rgba(255,255,255,.9); flex:1 1 480px; min-width:0}
.s3 main .s3-stake .arrow-link{color:var(--mint)}
@media (max-width:620px){.s3-stake__two{grid-template-columns:1fr}}

/* ---- the guide, and hands-on support: two cards, one anatomy ---- */
.s3-gp{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(6,auto); gap:0 var(--gap)}
.s3-gpc{grid-row:span 6; display:grid; grid-template-rows:subgrid; row-gap:14px; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:var(--shadow-soft); min-width:0}
.s3-gpc > small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-gpc h3{font-size:clamp(1.4rem,2.1vw,1.8rem); margin:0; color:var(--logo-teal)}
.s3-gpc > p{margin:0; color:var(--ink-soft); font-size:1.02rem}
.s3-gpc .s3-checks{align-content:start}
.s3-gpc__x{display:flex; align-items:center; gap:18px; padding:16px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line); min-width:0}
.s3-gpc__x img{flex:none; width:84px; height:auto; border-radius:6px; border:1px solid var(--line); box-shadow:var(--shadow-soft); transform:rotate(-3deg)}
.s3-gpc__x p{margin:0; font-size:.97rem; font-weight:600; line-height:1.4}
.s3-gpc__x p small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin-bottom:5px}
.s3-gpc__x--q{flex-direction:column; align-items:stretch; gap:10px}
.s3-qual{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px}
.s3-qual li{margin:0; text-align:center; padding:9px 8px; border-radius:10px; background:#fff; border:1.5px solid var(--teal); color:var(--logo-teal); font-family:var(--display); font-weight:800; font-stretch:108%; font-size:.98rem; line-height:1.15}
.s3-gpc .btns .btn{flex:1 1 auto}
@media (max-width:860px){.s3-gp{grid-template-columns:1fr; grid-template-rows:none; gap:var(--gap)} .s3-gpc{grid-row:auto; grid-template-rows:none}}

/* ---- putting the guide to work (same step rhythm as 360-schools.html) ---- */
.s3-how{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,5vw,72px); align-items:stretch}
.s3-how__side{display:flex; flex-direction:column; gap:var(--gap); min-width:0}
.s3-how__side h2{margin:0}
.s3-how__side .btns{display:grid; grid-template-columns:minmax(0,1fr); gap:10px; width:min(100%,290px)}
.s3-how__note{margin-top:auto; border-radius:var(--r-xl); padding:var(--pad-card); background:var(--mist); border:1px solid var(--line)}
.s3-how__note b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.3rem; line-height:1.15; color:var(--logo-teal); margin-bottom:8px}
.s3-how__note p{margin:0 0 12px; color:var(--ink-soft); font-size:1rem}
.s3-how__steps{list-style:none; margin:0; padding:0; display:grid; gap:clamp(20px,2.4vw,30px); align-content:space-between}
.s3-how__steps li{position:relative; margin:0; display:grid; grid-template-columns:56px minmax(0,1fr); gap:clamp(16px,2vw,24px); align-items:start}
.s3-how__steps li:not(:last-child)::before{content:""; position:absolute; left:27px; top:62px; bottom:calc(-1 * clamp(20px,2.4vw,30px) + 6px); width:2px; border-radius:2px; background:rgba(19,132,143,.35)}
.s3-how__n{width:56px; height:56px; border-radius:50%; border:2px solid var(--teal); background:#fff; display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.5rem; color:var(--logo-teal); line-height:1}
.s3-how__steps h3{margin:.45em 0 .3em; font-size:clamp(1.25rem,1.8vw,1.5rem); color:var(--logo-teal)}
.s3-how__steps p{margin:0; color:var(--ink-soft); font-size:1rem}
@media (max-width:900px){.s3-how{grid-template-columns:1fr} .s3-how__side{display:contents} .s3-how__side h2{order:1} .s3-how__steps{order:2} .s3-how__side .btns{order:3} .s3-how__note{order:4; margin-top:0}}
@media (max-width:460px){.s3-how__steps li{grid-template-columns:44px minmax(0,1fr); gap:14px} .s3-how__n{width:44px; height:44px; font-size:1.2rem} .s3-how__steps li:not(:last-child)::before{left:21px; top:50px} .s3-how__steps h3{margin-top:.25em}}

/* ---- the student guide ---- */
.s3-stud{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,5vw,72px); align-items:center}
.s3-stud__body{min-width:0}
.s3-stud__body .lede{color:#fff}
.s3-stud__body > p:not(.eyebrow):not(.lede){color:rgba(255,255,255,.9)}
.s3-stud__body .btns{margin-top:22px}
.s3-stud__cover{position:relative; display:block; width:min(100%,330px); margin-inline:auto; text-decoration:none}
.s3-stud__cover::before{content:""; position:absolute; inset:0; border-radius:14px; background:var(--mint); transform:rotate(-7deg) translate(-10px,6px); opacity:.9}
.s3-stud__cover span{position:relative; display:block; background:#fff; padding:9px; border-radius:14px; box-shadow:0 30px 60px -26px rgba(0,0,0,.6); transform:rotate(3deg); transition:transform .45s var(--ease)}
.s3-stud__cover:hover span{transform:rotate(0deg) translateY(-6px)}
.s3-stud__cover img{width:100%; height:auto; border-radius:5px}
@media (max-width:860px){.s3-stud{grid-template-columns:1fr; gap:0} .s3-stud__body{display:contents} .s3-stud__body > *{order:3} .s3-stud__body > .eyebrow, .s3-stud__body > h2{order:1} .s3-stud__cover{order:2; width:min(64%,240px); margin-block:14px 34px}}
'''

CSS_ACC = '''
.s3-ah{--h1:8.2cqi; --h1m:7.4vw}
/* ---- hero: the two requests ---- */
.s3-ahv{position:relative; padding:0 0 clamp(96px,10vw,132px) 0}
.s3-ahv__img{border-radius:var(--r-xl); overflow:hidden; box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.s3-ahv__img img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:60% 50%}
.s3-ahq{position:absolute; left:clamp(-34px,-2.4vw,-14px); bottom:0; width:min(92%,430px); margin:0; z-index:2; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:24px 28px 22px; box-shadow:var(--shadow-soft), 0 24px 50px -30px rgba(0,0,0,.5); animation:s3-up .9s .3s var(--ease) both}
@keyframes s3-up{from{transform:translateY(22px)}}
.s3-ahq blockquote{margin:0; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:clamp(1.3rem,2vw,1.72rem); line-height:1.16; letter-spacing:-.005em; text-wrap:balance}
.s3-ahq blockquote::before{content:"\\201C"; display:block; font-weight:900; font-size:3.2em; line-height:.5; margin:.12em 0 .02em; color:var(--teal); font-stretch:125%}
.s3-ahq figcaption{display:block; margin-top:14px; padding-top:12px; border-top:1px solid var(--line); font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; line-height:1.5; color:var(--logo-teal); text-wrap:balance}
@media (max-width:900px){.s3-ahv{padding:0; max-width:620px} .s3-ahq{position:relative; left:auto; bottom:auto; width:auto; margin:-54px 14px 0}}

/* ---- more options, and the operative word ---- */
.s3-acc #why .section-head{margin-bottom:clamp(14px,1.6vw,20px)}
.s3-why{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px clamp(28px,5vw,72px); align-items:start}
.s3-why > div:last-child p{font-size:1.06rem}
.s3-why > div{min-width:0}
.s3-why .lede{margin:0}
.s3-why p:last-child{margin-bottom:0}
.s3-choice{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:16px clamp(28px,5vw,72px); align-items:center; margin-top:clamp(30px,4vw,48px); padding:clamp(24px,3vw,38px) clamp(22px,3.4vw,44px); border-radius:var(--r-xl); background:var(--mint); color:var(--slate)}
.s3-choice__word{min-width:0; container-type:inline-size}
.s3-choice small{display:block; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; margin-bottom:10px}
.s3-choice strong{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(3rem,19.6cqi,5.6rem); line-height:.8; letter-spacing:-.035em; margin-left:-.04em}
.s3-choice > p{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.2rem,1.9vw,1.6rem); line-height:1.26; margin:0; padding-left:clamp(18px,2.6vw,36px); border-left:3px solid rgba(29,65,78,.35); text-wrap:pretty}
@media (max-width:860px){.s3-why{grid-template-columns:1fr; align-items:start} .s3-choice{grid-template-columns:1fr} .s3-choice > p{padding-left:0; border-left:0; padding-top:16px; border-top:3px solid rgba(29,65,78,.35)}}

/* ---- what the training covers: one sheet of twelve ---- */
.s3-atable{border:1px solid var(--line-dark); border-radius:var(--r-xl); overflow:hidden; background:rgba(255,255,255,.04)}
.s3-atopics{list-style:none; margin:0 -1px -1px 0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr))}
.s3-atopics li{margin:0; display:grid; grid-template-columns:auto minmax(0,1fr); gap:14px; align-items:center; min-height:96px; padding:18px 20px; border-right:1px solid var(--line-dark); border-bottom:1px solid var(--line-dark); min-width:0; transition:background .2s}
.s3-atopics li:hover{background:rgba(255,255,255,.05)}
.s3-atopics li::before{content:""; width:26px; height:26px; border-radius:50%; background:var(--mint) var(--ck) center/16px no-repeat}
.s3-atopics b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.06rem,1.4vw,1.2rem); line-height:1.22}
.s3-atable__foot{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:14px 32px; padding:18px 20px; background:rgba(255,255,255,.05)}
.s3-atable__foot p{margin:0; display:flex; align-items:center; gap:14px; font-weight:600; font-size:1.02rem; color:rgba(255,255,255,.92); flex:1 1 420px; min-width:0}
.s3-atable__foot p::before{content:""; flex:none; width:26px; height:26px; border-radius:50%; background:var(--mint) var(--ck) center/16px no-repeat}
@media (max-width:1000px){.s3-atopics{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.s3-atopics{grid-template-columns:1fr} .s3-atopics li{min-height:0; padding:14px 16px}}

/* ---- an alternative to discipline alone ---- */
.s3-fit{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap) clamp(28px,5vw,72px); align-items:stretch}
.s3-fit__txt{min-width:0; display:flex; flex-direction:column}
.s3-fit__txt .btns{margin-top:auto; padding-top:22px}
.s3-fit__help{margin-top:22px}
.s3-fit__card{min-width:0; display:grid; background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:calc(var(--pad-card) - 14px) var(--pad-card)}
.s3-fit__card .s3-spec{border-top:0}
.s3-fit__card .s3-spec > div{align-content:start}
.s3-fit__card .s3-spec > div:last-child{border-bottom:0}
@media (max-width:900px){.s3-fit{grid-template-columns:1fr; gap:0} .s3-fit__txt{display:contents} .s3-fit__txt > *{order:1} .s3-fit__card{order:2; margin-top:8px} .s3-fit__txt > .btns{order:3; padding-top:22px} .s3-fit__help{order:4; margin-top:var(--gap)}}
'''

# ------------------------------------------------------------------ data
UNITS = [
  ('core', 'u-core', 'Core Concepts', 'Lessons 1–6', 'Basic concepts to address with students related to dating violence, sexual violence, and healthy relationships.', 3,
   [(1, 'Healthy Relationships', ('It’s Giving Red Flags', 'film-its-giving-red-flags.html')), (2, 'Consent', None),
    (3, 'Online Safety & Sending Nudes', ('#knowB4Unude', 'film-knowb4unude.html')), (4, 'Bystander Intervention', ('BAEcode: Game On!', 'film-baecode-game-on.html')),
    (5, 'Male Youth & Sexual Violence', ('Supporting Male Survivors', 'film-sexual-assault-of-men.html')), (6, 'If You’ve Been Accused of Sexual Assault', ('Accountability Training', 'accountability-training.html'))]),
  ('foundations', 'u-found', 'Foundational Knowledge', 'Lessons 7–10', 'Foundations of understanding sexual violence, expanding on definitions of crimes, and the influence of media, pop culture, and myths.', 2,
   [(7, 'Rape Culture', ('Rape Culture to a Culture of Respect', 'film-rape-culture.html')), (8, 'Sexual Harassment, Assault, Rape – Defined', None),
    (9, 'Violence in the Media', None), (10, 'Myths, Facts & Stats', ('Myths & Facts', 'myths-facts.html'))]),
  ('healing', 'u-heal', 'Healing Resources', 'Lessons 11–13', 'Victim support and healing after incidents of violence, including how peers can support survivors and how individuals can take steps towards healing and moving forward in new relationships.', 3,
   [(11, 'Healing After Sexual Violence', None), (12, 'Support a Survivor', ('Survivor Support', 'survivor-support.html')),
    (13, 'Dating After Violence', ('Intimacy & Dating After Assault', 'film-dating-after-sexual-assault.html'))]),
  ('justice', 'u-just', 'Justice Options', 'Lessons 14–15', 'Options for justice after experiencing violence with a focus on victim autonomy, a review of Title IX policies and procedures, and other methods for reporting crimes.', 2,
   [(14, 'Title IX', ('Title IX: your rights at school', 'title-ix.html')), (15, 'Options for Reporting', None)]),
]

TEACHER_STATS = [
  ('53%', 'increase', 'in teachers attending an event or program about what they can do as a bystander to stop dating violence, sexual violence or stalking'),
  ('24%', 'increase', 'in teachers stepping in to help a student who appeared to be at risk of, or was experiencing, dating violence, sexual violence or stalking'),
  ('19%', 'increase', 'in teachers discussing dating violence, sexual violence or stalking with another teacher or administrator at their school'),
  ('16%', 'increase', 'in teachers having a conversation with a student about healthy relationships'),
  ('14%', 'increase', 'in teachers discussing dating violence, sexual violence or stalking with their class'),
  ('15%', 'more teachers', 'believed students at their school would believe survivors of sexual violence after SafeBAE programming'),
  ('9.4%', 'more teachers', 'believed teachers and administrators would support survivors of sexual violence after SafeBAE programming'),
]
PILOT_LINE = 'In collaboration with Dr. Lindsay Orchowski at Brown University, SafeBAE evaluated program delivery at two Rhode Island partner schools, Rhode Island Nurses Institute and Paul Cuffee Charter School, during the 2023⁠–⁠24 school year.'


def stat(n, k, d, cls=''):
    num = n.rstrip('%'); dec = len(num.split('.')[1]) if '.' in num else 0
    return (f'<div class="s3-stat {cls}"><div class="s3-stat__n"><b data-n="{num}" data-d="{dec}">{esc(n)}</b><span class="k">{esc(k)}</span></div>'
            f'<span class="s3-meter" aria-hidden="true" style="--v:{num}"><i></i></span><p>{esc(d)}</p></div>')


# ------------------------------------------------------------------ pages
def curriculum():
    tiles = []
    for key, ucls, name, rng, desc, cols, lessons in UNITS:
        for n, t, rel in lessons:
            tiles.append(f'<a class="s3-tile {ucls}" href="#lesson-{n}" data-unit="{key}" data-lesson="{n}" style="--i:{n}" aria-label="Lesson {n}: {esc(t)}"><b>{n}</b><span>{esc(t)}</span></a>')
    legend = ''.join(f'<li><a class="{ucls}" href="#{key}" data-unit="{key}"><i></i><span>{esc(name)}</span><small><span class="sr-only">Lessons </span>{esc(rng.replace("Lessons ", ""))}</small></a></li>' for key, ucls, name, rng, *_r in UNITS)
    board = f'''<div class="s3-hero__media s3-board">
      <p class="s3-board__cap"><span>15 lessons in four units</span><span>Select a lesson</span></p>
      <div class="s3-tiles">{''.join(tiles)}</div>
      <ul class="s3-legend">{legend}</ul>
    </div>'''
    top = hero('aqua', 'Consent Curriculum',
               'Healthy Relationship &amp; <span class="mk">Consent</span> Curriculum',
               'A flexible, trauma-informed curriculum of 15 interactive lessons aligned with the National Health Education Standards (NHES). Lessons explore consent, communication, boundaries, digital safety, survivor support, healing, and more.',
               board, ['15 interactive lessons', '45–60 minutes per lesson', 'Aligned with the NHES', 'English and Spanish'],
               cls='s3-ch', main='slate')

    utabs, upanels = [], []
    for i, (key, ucls, name, rng, desc, cols, lessons) in enumerate(UNITS):
        utabs.append(f'<button role="tab" id="tab-{key}" aria-controls="unit-{key}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" class="{ucls}"><small><i></i>{esc(rng)}</small><span>{esc(name)}</span></button>')
        ls = ''.join(f'<div class="s3-lesson" id="lesson-{n}"><span class="s3-lesson__n">{n}</span><span class="s3-lesson__t">{esc(t)}</span>' +
                     (f'<a class="s3-lesson__rel" href="{rel[1]}">Related: <b>{esc(rel[0])}</b></a>' if rel else '') + '</div>' for n, t, rel in lessons)
        upanels.append(f'''<div class="s3-unit" role="tabpanel" id="unit-{key}" aria-labelledby="tab-{key}"{'' if i==0 else ' hidden'}>
        <h3 class="sr-only">{esc(name)}: {esc(rng)}</h3>
        <p class="s3-unit__intro">{esc(desc)}</p>
        <div class="s3-lessons s3-lessons--{cols}" style="--n:{cols}">{ls}</div></div>''')
    lessons = f'''<section class="band band--slate" id="lessons">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">4 units &middot; 15 lessons</p><h2>The 15 lessons</h2>
      <p class="lede lede--full">The curriculum addresses core concepts in healthy relationship education and sexual violence prevention. Each lesson includes visual slides, interactive video content, and talking points to engage students in learning.</p></div></div>
    <div data-tabs="s3-units"><div class="s3-utabs" role="tablist" aria-label="Curriculum units">{''.join(utabs)}</div>{''.join(upanels)}</div>
  </div>
</section>'''

    ways = [
      ('us-gariev-teacher', 'A teacher at a whiteboard pointing to students with their hands raised', 'object-position:40% 50%',
       'Taught by your teachers', 'Facilitators are encouraged to bring their own voice and teaching style, with a slide-by-slide facilitator guide to lead the conversation.',
       'Inside the facilitator guide', '#guide'),
      ('img-2395', 'Two SafeBAE presenters, one in a BAE shirt, leading a discussion at a classroom whiteboard', 'object-position:50% 40%',
       'Co-taught with peer educators', 'Certified Peer Educators co-facilitate curriculum sessions alongside your teachers.',
       'Peer Educator Training', 'peer-educator.html'),
      ('img-3947', 'A presenter at the front of a classroom with a SafeBAE lesson on the screen while students watch', 'object-position:60% 45%',
       'Delivered by SafeBAE', 'The SafeBAE team can deliver the lessons directly to your students.',
       'Request a program', ASK),
    ]
    ways_html = ''.join(f'<article class="s3-way"><div class="s3-way__img">{img(im, alt, style=st)}</div><h3>{esc(t)}</h3><p>{esc(d)}</p><a class="arrow-link" href="{h}">{esc(l)}</a></article>' for im, alt, st, t, d, l, h in ways)
    deliver = f'''<section class="band band--paper" id="deliver">
  <div class="wrap">
    <div class="section-head"><div><h2>Three ways to deliver it</h2>
      <p class="lede lede--full muted">Developed with youth and expert collaborators, the curriculum also includes lessons on sexting and tech-facilitated abuse, dating after sexual assault, and accountability for those who’ve caused harm. Content is available in English and Spanish.</p></div></div>
    <div class="s3-ways">{ways_html}</div>
  </div>
</section>'''

    fac = f'''<section class="band band--logo" id="guide">
  <div class="wrap s3-fac">
    <div class="s3-fac__body">
      <p class="eyebrow">Facilitator’s guide</p>
      <h2>How each lesson runs</h2>
      <p class="lede">SafeBAE’s curriculum is engaging, interactive, and youth-centered. SafeBAE worked with student leaders to develop each lesson, which includes visual slides with content and videos for student engagement, as well as a facilitator’s guide.</p>
      <p>Each lesson runs between 45 and 60 minutes, with learning objectives and knowledge checks included for students. Facilitators are encouraged to bring their voice and teaching style to each lesson, and may find the slide-by-slide facilitator guide helpful in leading the conversation.</p>
      <p>The curriculum covers important and sensitive topics, so SafeBAE encourages curiosity and questions.</p>
      <div class="s3-inside"><b>Inside every 45–60 minute lesson</b>
        {checks(['Learning objectives', 'Visual slides', 'Video content', 'Talking points', 'Knowledge checks', 'Slide-by-slide facilitator guide'], 's3-checks s3-checks--2')}</div>
    </div>
    <figure class="s3-doc reveal">
      <div class="s3-doc__stack"><span class="sticker sticker--r">Guide preview</span>
        <div class="s3-doc__sheet">{img('curr-facilitator-guide-p1', 'A page of the facilitator’s guide for Lesson 1, Healthy Relationships: lesson objectives, a time of 45 to 60 minutes, and facilitator notes and script for the first three slides')}</div></div>
      <figcaption>From the facilitator’s guide: Lesson 1, Healthy Relationships.</figcaption>
    </figure>
    <div class="s3-fac__foot">
      <div class="s3-email"><small>Training and technical assistance</small><p class="s3-email__a"><a href="mailto:{EMAIL}">{EMAIL}</a><button type="button" data-copy="{EMAIL}">Copy</button></p><p>We’re happy to help with any request by email.</p></div>
      {help_inline()}
    </div>
  </div>
</section>'''

    incl = f'''<section class="band band--paper" id="package">
  <div class="wrap s3-incl">
    <figure class="s3-incl__img">{img('img-9509-1', 'Students decorating “Yes means yes” consent posters with markers', style='object-position:50% 60%')}<span class="sticker sticker--r">Posters &amp; printables included</span></figure>
    <div class="s3-incl__body">
      <h2>A complete curriculum package</h2>
      <p class="lede">The package helps schools deliver engaging, developmentally appropriate prevention education with clarity, consistency, and care.</p>
      <div class="s3-pack">
        <div><small>Teach</small><b>Full lesson plans and facilitation guides</b></div>
        <div><small>Show</small><b>Slide decks and multimedia materials</b></div>
        <div><small>Print</small><b>Posters and printable resources</b></div>
        <div><small>Check</small><b>Assessments and interactive activities</b></div>
      </div>
      <dl class="s3-spec">
        <div><dt>Standards</dt><dd>Aligned with the National Health Education Standards (NHES)</dd></div>
        <div><dt>Languages</dt><dd>English and Spanish</dd></div>
      </dl>
      <div class="btns">{btn('Get the curriculum', PODIA, 'slate')}{btn('Ask about pricing', CAL, 'ghost')}</div>
    </div>
  </div>
</section>'''

    more = [
      ('library.html#guides', '', 'Starting smaller', 'Free films and teaching guides', 'Every SafeBAE film comes with a ready-to-teach guide for short, meaningful discussions.', 'Browse the library'),
      ('peer-educator.html', '', 'Pair it with', 'Certified Peer Educator Training', 'Students complete a free, self-paced online certification and can then co-facilitate curriculum sessions with you.', 'Peer Educator Training'),
      ('ai-literacy.html', ' is-new', 'New &middot; launches October 26&ndash;30, 2026', 'SafeBAE AI Literacy Training', 'Six free, self-paced modules for high school and college students. Educators can register for group access.', 'About the training'),
    ]
    more_html = ''.join(f'<a class="s3-card{c}" href="{h}"><span class="s3-card__who">{k}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><span class="s3-card__go"><span>{esc(g)}</span><i aria-hidden="true">&rarr;</i></span></a>' for h, c, k, t, d, g in more)
    smaller = f'''<section class="band band--deep" id="more">
  <div class="wrap">
    <div class="section-head"><div><h2>More for your classroom</h2></div></div>
    <div class="s3-cards">{more_html}</div>
  </div>
</section>'''

    body = top + lessons + deliver + fac + incl + smaller + programs('curriculum') + cta(
        'Bring the curriculum to your school',
        'Purchase the curriculum online, or talk with us about delivery by teachers, peer educators or the SafeBAE team and about sliding scale pricing.',
        'p1002709', 'SafeBAE youth media team on a film set holding a clapperboard', 'Lessons built with student leaders',
        extra=btn('Get the curriculum online', PODIA, 'ghost', 'sm'), pos='50% 40%')
    js = r'''<script>(function(){
  /* the lesson board: a tile opens its unit and marks the lesson; a legend entry opens the unit */
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var sec = document.getElementById('lessons'); if(!sec) return;
  function open(unit, lesson, scroll){
    var tab = document.getElementById('tab-' + unit); if(tab) tab.click();
    document.querySelectorAll('.s3-lesson.is-hl').forEach(function(x){ x.classList.remove('is-hl'); });
    var li = lesson ? document.getElementById('lesson-' + lesson) : null;
    if(scroll){ var y = sec.querySelector('[data-tabs]').getBoundingClientRect().top + window.pageYOffset - 100; window.scrollTo({top: y, behavior: reduce ? 'auto' : 'smooth'}); }
    if(li){ void li.offsetWidth; li.classList.add('is-hl'); setTimeout(function(){ li.classList.remove('is-hl'); }, 3200); }
  }
  document.querySelectorAll('[data-unit]').forEach(function(t){
    t.addEventListener('click', function(e){ e.preventDefault(); open(t.getAttribute('data-unit'), t.getAttribute('data-lesson'), true); });
  });
  function fromHash(){
    var u = /^#unit-([a-z]+)$/.exec(location.hash); if(u && document.getElementById('tab-' + u[1])){ open(u[1], null, true); return; }
    var m = /^#lesson-(\d+)$/.exec(location.hash); if(!m) return;
    var li = document.getElementById('lesson-' + m[1]), p = li && li.closest('[role="tabpanel"]'); if(!p) return;
    open(p.id.replace('unit-', ''), m[1], true);
  }
  window.addEventListener('hashchange', fromHash); setTimeout(fromHash, 60);
})();</script>'''
    page('consent-curriculum.html', 'Consent Curriculum · SafeBAE',
         'SafeBAE’s healthy relationship and consent curriculum: 15 lessons aligned with the National Health Education Standards, covering consent, sexting and accountability. Built with youth, available in English and Spanish.',
         body, active='programs', body_class='s3 s3-curr', head_extra=f'<style>{CSS}{HELPLINE_CSS}{CSS_CURR}</style>', scripts=js)


CHART_JS = r'''<script>(function(){
  /* the teacher chart: bars grow and numbers count up the first time it is seen */
  var grid = document.querySelector('.s3-tgrid'), chart = document.querySelector('[data-bars]'); if(!grid || !chart) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function run(){
    if(chart.classList.contains('in')) return; chart.classList.add('in'); grid.classList.add('in');
    if(reduce || !window.requestAnimationFrame) return;
    Array.prototype.forEach.call(grid.querySelectorAll('[data-n]'), function(el){
      var to = +el.getAttribute('data-n'), dec = +el.getAttribute('data-d') || 0, t0 = null;
      function step(t){ if(t0 === null) t0 = t; var k = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - k, 3); el.textContent = (to * e).toFixed(dec) + '%'; if(k < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    });
  }
  if(!('IntersectionObserver' in window)){ run(); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ io.disconnect(); run(); } }); }, {threshold: .25});
  io.observe(chart);
})();</script>'''


def pd():
    media = f'<figure class="s3-hero__media s3-shot">{img("img-2400", "Students and adults seated in a circle during a SafeBAE session in a classroom", loading="eager", style="object-position:50% 45%")}<span class="sticker">In person or virtual</span></figure>'
    top = hero('logo', 'Faculty & Staff Training',
               'Professional development for <span class="mk">faculty &amp; staff</span>',
               'Prevention is most effective when faculty and staff have the right tools and training. SafeBAE provides professional development for teachers, staff, and administrators that is trauma-informed, flexible, and tailored to your school’s needs.',
               media, ['For teachers, staff and administrators', 'Trauma-informed', 'In person or virtual', 'Tailored to your school'], cls='s3-pdh')

    topics = [
      ('Trauma-informed responses to disclosures of harm', ('Survivor support', 'survivor-support.html')),
      ('Building a school culture of consent and accountability', ('Consent Curriculum', 'consent-curriculum.html')),
      ('Supporting student survivors', ('Title IX: rights at school', 'title-ix.html')),
      ('Understanding and advancing school policy reform to strengthen protections and reduce liability', ('Policy Reform Guide', 'policy-reform-guide.html')),
      ('Supporting youth leadership and engagement in prevention', ('Peer Educator Training', 'peer-educator.html')),
      ('Supporting marginalized students', ('Race, Rape Culture & Resistance', 'film-race-rape-culture-resistance.html')),
    ]
    th = ''.join(f'<li><b>{esc(t)}</b><a class="arrow-link" href="{h}"><small>Related:</small> {esc(l)}</a></li>' for t, (l, h) in topics)
    tsec = f'''<section class="band band--paper" id="covers">
  <div class="wrap">
    <div class="section-head"><div><h2>What the trainings cover</h2>
      <p class="lede lede--full muted">Every training is trauma-informed and built around your school. Sessions draw on these focus areas.</p></div></div>
    <div class="s3-topics">
      <ul class="s3-focus">{th}</ul>
      <figure class="s3-fact reveal">
        <figcaption>From a SafeBAE poster</figcaption>
        <blockquote><p>By the time students are done with secondary school,</p><b>81%</b><p>have experienced some sort of sexual harassment.</p><cite>Gruber &amp; Fineran</cite></blockquote>
        <div class="s3-fact__foot"><span>Help us change that.</span><a class="arrow-link" href="posters.html">Free posters</a></div>
      </figure>
      <div class="s3-topics__help">{help_inline()}</div>
    </div>
  </div>
</section>'''

    fmt = f'''<section class="band band--slate" id="formats">
  <div class="wrap s3-fmt">
    <figure class="s3-fmt__img">{img('assembly-whiteboard', 'A woman writing the word “Respect” on a classroom whiteboard', style='object-position:60% 40%')}</figure>
    <div class="s3-fmt__card">
      <h2>How trainings are delivered</h2>
      <p>We adapt every training to the context of your school.</p>
      <div class="s3-modes"><div><b>In person</b><span>At your school</span></div><div><b>Virtual</b><span>Online sessions</span></div></div>
      <dl class="s3-spec">
        <div><dt>Audience</dt><dd>Teachers, staff and administrators</dd></div>
        <div><dt>Approach</dt><dd>Trauma-informed, flexible and tailored to your school’s unique needs</dd></div>
        <div><dt>Scope</dt><dd>On its own, or as part of {a('SafeBAE’s whole-school approach', S360, 'link')}</dd></div>
      </dl>
    </div>
  </div>
</section>'''

    def label(d):
        t = d[len('in teachers '):]
        return t[0].upper() + t[1:]
    bars = ''.join(f'<li class="s3-bar" style="--v:{v[:-1]}; --i:{i}"><p class="s3-bar__t">{esc(label(d))}</p><div class="s3-bar__track"><i></i><b data-n="{v[:-1]}">{esc(v)}</b></div></li>' for i, (v, k, d) in enumerate(TEACHER_STATS[:5]))
    tev = f'''<section class="band band--mint s3-ev" id="evidence">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Pilot data &middot; 2023&ndash;24 school year</p><h2>What teachers reported</h2>
      <p class="lede lede--full">{esc(PILOT_LINE)} Teachers who took part in SafeBAE’s programs were more likely to believe that their school policies could protect students from violence and thoroughly respond if violence occurs.</p></div></div>
    <div class="s3-tgrid">
      <figure class="s3-chart" data-bars>
        <figcaption><b>Increase among teachers after SafeBAE programming</b><span>Percent increase</span></figcaption>
        <ol class="s3-bars">{bars}</ol>
      </figure>
      <div class="s3-tside">{stat(*TEACHER_STATS[5])}{stat(*TEACHER_STATS[6])}</div>
    </div>
    <div class="s3-tq">
      <blockquote class="s3-voice"><p>“[SafeBAE provides] information surrounding issues relevant to everyone, not just students.”</p><cite>Teacher, 360° pilot school</cite></blockquote>
      <div class="btns">{btn('Pilot data (PDF)', PILOT_PDF, 'slate')}{btn('All pilot results', '360-schools.html#evidence', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>'''

    new = new_programs('Two new programs for your school', 'Educators can register for group access to the free SafeBAE AI Literacy Training, and SafeBAE’s Sexual Strangulation Prevention program for schools launches in November 2026.')
    body = top + tsec + fmt + tev + new + programs('pd') + cta(
        'Request training for your faculty and staff',
        'Tell us about your faculty and staff and what you need. We adapt every training to your school and can deliver it in person or virtually.',
        'safebae-8', 'SafeBAE youth leaders in SafeBAE shirts standing together by the water', 'Trauma-informed', pos='50% 50%')
    page('professional-development.html', 'Faculty & Staff Training · SafeBAE',
         'Trauma-informed professional development for teachers, staff, and administrators, tailored to your school and built to support youth-led prevention.',
         body, active='programs', body_class='s3 s3-pd', head_extra=f'<style>{CSS}{CSS_NEW}{HELPLINE_CSS}{CSS_PD}</style>', scripts=CHART_JS)


SHIFT_JS = r'''<script>(function(){
  var s = document.querySelector('[data-shift]'); if(!s) return;
  if(!('IntersectionObserver' in window)){ s.classList.add('in'); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ s.classList.add('in'); io.disconnect(); } }); }, {threshold: .35});
  io.observe(s);
})();</script>'''


def policy():
    media = f'''<div class="s3-hero__media s3-covers">
      <a class="s3-cover s3-cover--student" href="reform-policy.html" aria-label="The student version of the Policy Reform Guide">{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide for students, 2024 update', loading='eager')}<span class="sticker sticker--aqua">For students</span></a>
      <a class="s3-cover s3-cover--admin" href="{POLICY_PODIA}" target="_blank" rel="noopener" aria-label="Get the Policy Reform Guide for school administrators">{img('policy-guide-admin-cover', 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide for school administrators, 2024 update', loading='eager')}<span class="sticker">For administrators</span></a>
    </div>'''
    top = hero('teal', 'Policy Reform Guide',
               'School Sexual Misconduct <span class="mk">Policy Reform</span> Guide',
               'Strong, trauma-informed policies are the foundation of a safe school community. SafeBAE’s guide is a step-by-step resource to help administrators, faculty, and district leaders strengthen their policies beyond the bare federal minimum.',
               media, ['For administrators, faculty and district leaders', 'A step-by-step guide', 'Hands-on policy support on request'], cls='s3-ph')

    # the line: the 2020 rule, the 2024 attempt to restore protections (dashed: tied up in court), and back again
    line = ('<svg viewBox="0 0 1200 118" preserveAspectRatio="none" aria-hidden="true">'
            '<path class="g" d="M0 22H1200"/><path class="g" d="M0 96H1200"/>'
            '<path d="M15 96H362C392 96 388 22 415 22"/>'
            '<path class="d" d="M415 22H596"/>'
            '<path d="M596 22C628 22 620 96 652 96H1184"/></svg>')
    why = f'''<section class="band band--paper" id="why">
  <div class="wrap">
    <div class="section-head"><div><h2>Federal Title IX rules keep <span class="mk">shifting</span></h2>
      <p class="lede lede--full">Since 2020, shifting federal Title IX regulations have left schools caught in the middle of inconsistent rules, legal challenges, and unclear enforcement.</p></div></div>
    <div class="s3-shift" data-shift>
      <div class="s3-shift__track" aria-hidden="true">
        {line}
        <p class="s3-shift__ax s3-shift__ax--hi">More protection for survivors &uarr;</p>
        <span class="s3-shift__tag" style="--x:37.4">Tied up in court</span>
        <span class="s3-shift__dot" style="--x:0; --y:81.4; --dl:.1s"></span>
        <span class="s3-shift__dot" style="--x:33.333; --y:18.6; --dl:.7s"></span>
        <span class="s3-shift__dot s3-shift__dot--now" style="--x:66.667; --y:81.4; --dl:1.3s"></span>
        <span class="s3-shift__arrow" style="--y:81.4"></span>
      </div>
      <ol class="s3-shift__list">
        <li><span class="s3-shift__y">2020</span><h3>The 2020 rule</h3><p>Narrowed protections for survivors and restricted schools’ ability to respond effectively.</p></li>
        <li><span class="s3-shift__y">2024</span><h3>New guidelines</h3><p>Attempted to restore protections, but were quickly tied up in court.</p></li>
        <li class="is-now"><span class="s3-shift__y">Now</span><h3>Back under the 2020 rule</h3><p>Most schools have been forced back under the restrictive 2020 rule, leaving students and districts vulnerable.</p></li>
      </ol>
    </div>
    <div class="s3-stake">
      <p class="s3-stake__big">This federal uncertainty leaves both students and school districts vulnerable.</p>
      <div class="s3-stake__two"><div><small>For students</small><b>Survivors face heightened risk of further harm.</b></div><div><small>For districts</small><b>Administrators face potential legal exposure without clear, stable standards to follow.</b></div></div>
      <div class="s3-stake__row"><p>Strengthening your school’s policies proactively protects students and safeguards your institution. It also shows leadership in creating safer, healthier learning environments.</p><a class="arrow-link" href="#guide">The guide and hands-on support</a></div>
    </div>
  </div>
</section>'''

    guide = f'''<section class="band band--slate" id="guide">
  <div class="wrap">
    <div class="section-head"><div><h2>The guide, and hands-on support</h2>
      <p class="lede lede--full">Grounded in trauma-informed practice and survivor-centered values, the guide walks you through building policies that promote transparency, accountability, and safety for every student.</p></div></div>
    <div class="s3-gp">
      <article class="s3-gpc reveal"><small>Self-guided</small><h3>The Policy Reform Guide</h3>
        <p>A step-by-step guide to creating a comprehensive, trauma-informed policy.</p>
        {checks(['Built to take your policy beyond the bare federal minimum', 'Grounded in trauma-informed practice and survivor-centered values', 'Written for administrators, faculty and district leaders'])}
        <div class="s3-gpc__x">{img('policy-guide-admin-cover', '')}<p><small>2024 update</small>Sexual Misconduct Policy Reform Guide: a guide for school administrators in how to create a model policy.</p></div>
        <div class="btns">{btn('Get the guide', POLICY_PODIA, 'slate')}</div></article>
      <article class="s3-gpc reveal"><small>Hands-on consultation</small><h3>School policy support</h3>
        <p>Hands-on consultation helps schools audit and revise sexual misconduct and Title IX policies.</p>
        {checks(['Annotated audits', 'Student-centered model language', 'Communication templates', 'Rollout strategies'], 's3-checks s3-checks--2')}
        <div class="s3-gpc__x s3-gpc__x--q"><p><small>The goal is a policy that is</small></p><ul class="s3-qual"><li>Accessible</li><li>Compliant</li><li>Trusted</li><li>Trauma-informed</li></ul></div>
        <div class="btns">{btn('Request policy support', ASK, 'slate', arrow=True)}</div></article>
    </div>
  </div>
</section>'''

    steps = [
      ('Read the guide', 'Work through the step-by-step guide with your administrators, faculty and district leaders.'),
      ('Audit your current policy', 'Review your sexual misconduct and Title IX policies against it. SafeBAE can provide an annotated audit.'),
      ('Revise with students in mind', f'Use student-centered model language. Students can use {a("their own version of the guide", "reform-policy.html", "link")} to advocate alongside you.'),
      ('Communicate and roll out', 'Use communication templates and rollout strategies so the new policy is accessible and trusted.'),
    ]
    sh = ''.join(f'<li><span class="s3-how__n">{i+1}</span><div><h3>{esc(t)}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))
    use = f'''<section class="band band--paper" id="steps">
  <div class="wrap s3-how">
    <div class="s3-how__side">
      <h2>Putting the guide to work</h2>
      <div class="btns">{btn('Get the guide', POLICY_PODIA, 'slate', 'sm')}{btn('Book a 60-minute meeting', CAL, 'ghost', 'sm')}</div>
      <div class="s3-how__note reveal"><b>Train the people who carry it out.</b><p>SafeBAE’s faculty and staff training includes understanding and advancing school policy reform to strengthen protections and reduce liability.</p><a class="arrow-link" href="professional-development.html">Faculty &amp; Staff Training</a></div>
    </div>
    <ol class="s3-how__steps">{sh}</ol>
  </div>
</section>'''

    stud = f'''<section class="band band--logo" id="student-guide">
  <div class="wrap s3-stud">
    <div class="s3-stud__body">
      <p class="eyebrow">For students, parents and community stakeholders</p>
      <h2>The Student Policy Reform Guide</h2>
      <p class="lede">A step-by-step resource that helps students advocate for safer, trauma-informed, and survivor-centered policies in their district. Students, parents and community stakeholders can use it to push for clarity, accountability, and real protection in their schools.</p>
      <p>SafeBAE asks only that you register to receive the student guide and keep in touch about your progress.</p>
      <div class="btns">{btn('Get the student guide', 'reform-policy.html', 'mint', arrow=True)}{btn('Title IX: rights at school', 'title-ix.html', 'ghost')}</div>
    </div>
    <a class="s3-stud__cover reveal" href="reform-policy.html" aria-label="The Student Policy Reform Guide"><span>{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', 'Cover of the Student Policy Reform Guide: a guide for students in how to create a model policy, 2024 update')}</span></a>
  </div>
</section>'''

    body = top + why + guide + use + stud + programs('policy') + cta(
        'Get policy support for your district',
        'Start with the guide, or bring SafeBAE in for hands-on consultation: annotated audits, model language, communication templates and rollout strategies.',
        'img-3755', 'Students and an adult posing together in a school hallway', 'Student-centered policy',
        extra=btn('Get the guide', POLICY_PODIA, 'ghost', 'sm'), pos='50% 55%')
    page('policy-reform-guide.html', 'Policy Reform Guide for Schools · SafeBAE',
         'A guide to reforming your school’s sexual misconduct policy with strong, trauma-informed protections as federal Title IX rules keep shifting.',
         body, active='programs', body_class='s3 s3-pol', head_extra=f'<style>{CSS}{CSS_POL}</style>', scripts=SHIFT_JS)


def accountability():
    media = f'''<div class="s3-hero__media s3-ahv">
      <div class="s3-ahv__img">{img('us-duford-laptop-notebook', 'Overhead view of hands at a laptop, one writing in a notebook', loading='eager')}</div>
      <figure class="s3-ahq">
        <blockquote>I want them to apologize, and I want them to not do this to anyone else.</blockquote>
        <figcaption>Two requests we hear from survivors, again and again</figcaption>
      </figure>
    </div>'''
    top = hero('deep', 'Accountability Training',
               '<span class="mk">Accountability</span> Training for Schools',
               'A multi-lesson virtual program developed specifically for students who have harmed another student. It helps them reflect on intention versus outcome, identify harmful behaviors, and reduce the likelihood of reoffending.',
               media, ['For students who have caused harm', 'Multi-lesson and virtual', 'Knowledge checks', 'English and Spanish'], cls='s3-ah')

    why = f'''<section class="band band--paper" id="why">
  <div class="wrap">
    <div class="section-head"><div><h2>Survivors asked for more options</h2></div></div>
    <div class="s3-why">
      <div><p class="lede">Historically, schools, universities, and courts across the country have had virtually no resources to address students accused of or found responsible for sexual assault. In most Title IX cases, the primary resolution has been suspension or expulsion.</p></div>
      <div><p>In our work with survivors, we often hear how traumatizing and difficult investigations can be, and how many survivors want alternatives. Some would like resolution options that focus on accountability and healing rather than only punishment.</p>
        <p>As part of our mission to provide resources for both prevention and response, we developed this training specifically for students who have harmed another student.</p></div>
    </div>
    <div class="s3-choice reveal"><div class="s3-choice__word"><small>The operative word</small><strong>Choice</strong></div><p>Survivors must be free to decide what path feels safest and most meaningful for them. Not all will choose these alternatives.</p></div>
  </div>
</section>'''

    topics = ['How to Respond If You’ve Been Accused', 'The Origins of Rape Culture', 'Sexual Assault, Harassment, and Rape – Defined', 'Consent',
              'Healthy Relationships', 'Male Youth & Sexual Violence', 'Myths, Facts & Statistics', 'Sexual Violence & Relationships in Media',
              'Online Safety & Sending Nudes', 'Healing After Sexual Violence', 'Dating Someone Who Has Experienced Sexual Violence', 'Bystander Intervention']
    th = ''.join(f'<li><b>{esc(t)}</b></li>' for t in topics)
    covers = f'''<section class="band band--slate" id="covers">
  <div class="wrap">
    <div class="section-head"><div><h2>What the training covers</h2>
      <p class="lede lede--full">Through a comprehensive, multi-lesson virtual program, participants are guided through these core topics.</p></div></div>
    <div class="s3-atable reveal">
      <ul class="s3-atopics">{th}</ul>
      <div class="s3-atable__foot"><p>Each lesson is followed by a knowledge check to ensure understanding.</p>{btn('Learn more', ACC_PODIA, 'mint', 'sm')}</div>
    </div>
  </div>
</section>'''

    fit = f'''<section class="band band--paper" id="fit">
  <div class="wrap s3-fit">
    <div class="s3-fit__txt">
      <h2>An alternative to discipline alone</h2>
      <p class="lede">The training is designed for use in school Title IX processes, in formal or informal resolutions, or in court settings. It is intended to support behavior change and reduce the likelihood of recidivism among respondents.</p>
      <p>The training is one of the educational resources to reduce recidivism in {a('the SafeBAE 360° approach', S360, 'link')}, rooted in prevention, healing, and restorative justice rather than punishment. Together with Vibe Check, these resources give schools a trauma-informed, developmentally appropriate alternative to traditional disciplinary responses.</p>
      <div class="btns">{btn('See licenses', ACC_PODIA, 'slate')}{btn('Ask a question', 'mailto:' + EMAIL, 'ghost')}</div>
      <div class="s3-fit__help">{help_inline()}</div>
    </div>
    <div class="s3-fit__card">
      <dl class="s3-spec">
        <div><dt>Format</dt><dd>A multi-lesson virtual program</dd></div>
        <div><dt>For</dt><dd>Students who have harmed another student</dd></div>
        <div><dt>Checks</dt><dd>A knowledge check after every lesson</dd></div>
        <div><dt>Completion</dt><dd>Proof of completion is available upon request</dd></div>
        <div><dt>Languages</dt><dd>English and Spanish</dd></div>
        <div><dt>Access</dt><dd>Available for purchase through an annual unlimited-use license or a single-use license. A single-use purchase includes a one-hour, one-on-one consultation.</dd></div>
        <div><dt>Development</dt><dd>Created by experts in partnership with young survivors. As with all of our programs, we welcome feedback to continuously improve and expand inclusivity.</dd></div>
      </dl>
    </div>
  </div>
</section>'''

    body = top + why + covers + fit + vibe_band() + programs('accountability') + cta(
        'Bring Accountability Training to your school',
        'Talk with us about how the training fits your Title IX process, which license suits your school, and sliding scale pricing.',
        'us-colah-campus', 'Students walking past a campus building under a large tree',
        extra=btn('See licenses', ACC_PODIA, 'ghost', 'sm'), pos='55% 60%')
    page('accountability-training.html', 'Accountability Training for Schools · SafeBAE',
         'SafeBAE’s accountability training helps schools respond to students who cause harm with survivor-centered options beyond suspension and expulsion.',
         body, active='programs', body_class='s3 s3-acc', head_extra=f'<style>{CSS}{CSS_VIBE}{HELPLINE_CSS}{CSS_ACC}</style>')


def build():
    curriculum()
    pd()
    policy()
    accountability()


if __name__ == '__main__':
    build()
