"""360° Schools group: 360-schools, consent-curriculum, professional-development,
policy-reform-guide, accountability-training."""
from lib import *
from pages_home import ring_svg, COMP_TEXT
from films_common import help_inline, HELPLINE_CSS
from data import PODCASTS
import math

CAL = 'https://calendly.com/shaelnorris/60min'
PODIA = 'https://safebae.podia.com/'
PILOT_PDF = 'https://www.safebae.org/wp-content/uploads/2025/06/SafeBAE-360-Schools-Pilot-Data.pdf'
POLICY_PODIA = 'https://safebae.podia.com/sexual-misconduct-policy-reform-guide'
ACC_PODIA = 'https://safebae.podia.com/7db95b2a-0fc8-47a7-b4f2-69c2a01232a9'
REES_LOGIN = 'https://safebae.reessecureus.com/en/Login'
VC = 'https://checkyourvibe.org/'
VC_GUIDE = 'https://www.safebae.org/wp-content/uploads/2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
EMAIL = 'info@safebae.org'

_SVG, RCOMPS = ring_svg()   # (title, href, fill, ink)
SHORT = ['Peer Educator Training', 'Consent Curriculum', 'Faculty & Staff Training', 'Policy Support', 'Anonymous Reporting (REES)', 'Accountability Resources']
FAM_HREF = ['peer-educator.html', 'consent-curriculum.html', 'professional-development.html', 'policy-reform-guide.html', '360-schools.html#rees', 'accountability-training.html']

# ------------------------------------------------------------------ shared bits
def seg_path(i, cx, cy, R, r, gap):
    a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
    p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
    x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'

def mini_ring(active=None, cls='s3-mring', inner=22):
    segs = []
    for i, (t, h, fill, ink) in enumerate(RCOMPS):
        on = active is None or i == active
        segs.append(f'<path d="{seg_path(i, 50, 50, 49, inner, 4)}" fill="{fill if on else "currentColor"}"' + ('' if on else ' opacity=".18"') + '/>')
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{"".join(segs)}</svg>'

def badge(i):
    return f'<a class="s3-badge" href="360-schools.html">{mini_ring(i)}<span><b>SafeBAE 360&deg;</b> &middot; Component {i+1} of 6</span></a>'

def crumbs(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in items) + '</nav>'

def family(active):
    items = []
    for i, (t, h, fill, ink) in enumerate(RCOMPS):
        on = i == active
        items.append(f'<a class="s3-fam__item{" is-on" if on else ""}" href="{FAM_HREF[i]}" style="--c:{fill}"' + (' aria-current="page"' if on else '') +
                     f'><span class="n">{i+1}</span><b>{esc(SHORT[i])}</b><small>{"You are here" if on else "View &rarr;"}</small></a>')
    return f'''<section class="band band--mist band--tight s3-fam">
  <div class="wrap">
    <div class="s3-fam__head"><div><h2>The six components of SafeBAE 360&deg;</h2><p class="muted" style="margin:.5em 0 0">Each component works on its own or as part of the whole-school model.</p></div>{btn('See the whole model', '360-schools.html', 'slate', arrow=True)}</div>
    <nav class="s3-fam__list" aria-label="SafeBAE 360° components">{''.join(items)}</nav>
  </div>
</section>'''

PRICE = 'Cost should never be a barrier to prevention. SafeBAE offers flexible, sliding scale pricing tailored to each school’s needs and capacity, considering program scope, number of speakers and travel requirements.'

def cta(h2, lede, photo=None, photo_alt='', sticker='Youth-led, survivor-centered', extra='', note=''):
    acts = f'''<div class="s3-acts">
      <a class="s3-act s3-act--main" href="request-a-program.html"><span class="s3-act__k">Form</span><span><b>Request a program</b><small>Tell us what your school is looking for and how to follow up.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="s3-act" href="{CAL}" target="_blank" rel="noopener"><span class="s3-act__k">60 min</span><span><b>Book a meeting</b><small>Talk through scope, timing and sliding scale pricing.</small></span><span class="go" aria-hidden="true">&#8599;</span></a>
      <a class="s3-act" href="mailto:{EMAIL}"><span class="s3-act__k">Email</span><span><b>{EMAIL}</b><small>Questions, training and technical assistance.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>'''
    body = f'''<div class="s3-cta__body">
      <h2>{h2}</h2>
      <p class="lede">{lede}</p>
      {acts}
      <p class="s3-price"><b>Flexible pricing.</b> {esc(PRICE)}</p>{note}
      {f'<div class="btns" style="margin-top:16px">{extra}</div>' if extra else ''}
    </div>'''
    if photo:
        return f'''<section class="s3-cta" id="bring"><div class="wrap s3-cta__grid">
    <div class="s3-cta__photo">{img(photo, photo_alt)}<span class="sticker">{esc(sticker)}</span></div>
    {body}
  </div></section>'''
    return f'<section class="s3-cta s3-cta--nophoto" id="bring"><div class="wrap s3-cta__grid">{body}</div></section>'

AI_URL = 'https://ai-literacy.safebae.org'
AI_TOPICS = 'how AI works, how feeds and AI shape what we see and believe, AI and healthy relationships, using AI well, fake images, and sextortion'

def cal(mon, big):
    return f'<div class="s3-cal" aria-hidden="true"><span>{mon}</span><b>{big}</b></div>'

def new_programs(h2, lede, plus=False, ask='request-a-program.html'):
    ai = f'''<article class="s3-np">
      <div class="s3-np__top">{cal('Oct', '26&ndash;30')}<div><span class="s3-np__k">New &middot; Free &middot; Ages 13+</span><p class="s3-np__when">Launches during U.S. Media Literacy Week, October 26&ndash;30, 2026</p></div></div>
      <h3>SafeBAE AI Literacy Training</h3>
      <p>Six free, self-paced modules for high school and college students. Anyone 13 or older can take it. It covers {AI_TOPICS}.</p>
      <p>Educators can register for group access. Learners create a free account so their progress saves.</p>
      <div class="btns">{btn('About the training', 'ai-literacy.html', 'slate', arrow=True)}{btn('Open the training', AI_URL, 'ghost')}</div>
    </article>'''
    ssp = f'''<article class="s3-np">
      <div class="s3-np__top">{cal('Nov', '2026')}<div><span class="s3-np__k">New program for schools</span><p class="s3-np__when">Launching November 2026</p></div></div>
      <h3>Sexual Strangulation Prevention</h3>
      <p>SafeBAE&rsquo;s new program for schools on sexual strangulation, which young people call &ldquo;choking.&rdquo;</p>
      <blockquote class="s3-np__line">There&rsquo;s no safe way to choke someone.<cite>Choking Hazard campaign</cite></blockquote>
      <p>The Choking Hazard campaign gives young people, parents and educators the evidence, myth vs. fact, the signs that need medical care, and free warning posters.</p>
      <div class="btns">{btn('Ask about the program', ask, 'slate', arrow=True)}{btn('Choking Hazard campaign', 'choking-hazard.html', 'ghost')}</div>
    </article>'''
    g = (f'<div class="s3-plus" aria-hidden="true"><span class="s3-plus__ring">{mini_ring(None, "", 34)}<b>360&deg;</b></span><i>+</i>'
         f'<span class="s3-plus__chips"><em>AI Literacy</em><em>Strangulation Prevention</em></span></div>') if plus else ''
    return f'''<section class="band band--deep s3-new" id="new">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">New for 2026&ndash;27</p><h2>{h2}</h2><p class="lede lede--full">{lede}</p></div>{g}</div>
    <div class="s3-nps">{ai}{ssp}</div>
  </div>
</section>'''

def checks(items, cls='s3-checks'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def vibe_band(context='360'):
    if context == '360':
        eb = 'Component 6 &middot; Vibe Check by SafeBAE'
        h = 'Vibe Check: a self-assessment for students worried they crossed a line'
        p1 = 'Vibe Check is a free, anonymous reflection tool that helps students recognize unhealthy relationship behaviors and warning signs in themselves. It guides young people through confusing situations and connects them with evidence-based resources on consent, communication and accountability.'
    else:
        eb = 'Alongside the training &middot; Vibe Check by SafeBAE'
        h = 'Vibe Check: private reflection, never an assignment'
        p1 = 'Vibe Check is the other half of this component: a free, anonymous self-assessment that helps students recognize unhealthy relationship behaviors and warning signs in themselves, and points them to real resources on consent, communication and accountability.'
    return f'''<section class="band band--teal s3-vibe" id="vibe-check">
  <div class="wrap s3-vibe__grid">
    <div class="s3-vibe__phone"><div class="s3-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div><span class="sticker" style="left:-2%;top:16%">Anonymous</span><span class="sticker sticker--white sticker--r" style="right:2%;bottom:18%">Nothing is stored</span></div>
    <div>
      <div class="s3-vibe__mark"><span class="daisy"></span>{eb}</div>
      <h2>{h}</h2>
      <p class="lede" style="color:#fff">{p1}</p>
      <p style="color:rgba(255,255,255,.88)">No names, no accounts, and nothing is stored. It disappears when the browser closes. It is not a replacement for professional support: a young person who has been involved in a serious incident, experienced trauma or is in crisis should be connected with a qualified counselor or crisis service.</p>
      <div class="s3-vibe__tip"><b>Share it. Don’t assign it.</b><span>SafeBAE’s guide for adults advises against bringing Vibe Check up in the same moment as an incident, during a disciplinary conversation, or when emotions are running high. If it sounds like a punishment or an assignment, students won’t engage honestly.</span></div>
      <div class="btns">{btn('Open Vibe Check', VC, 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}{btn('Adult guide (PDF)', VC_GUIDE, 'ghost')}</div>
      <div class="s3-vibe__press"><span>As covered by</span>{img('the-guardian-logo-vector', 'The Guardian')}{img('vox-logo-svg-1', 'Vox')}{img('trendwatching-logo', 'TrendWatching')}</div>
    </div>
  </div>
</section>'''

# ------------------------------------------------------------------ CSS
CSS = '''
/* ---- shared: 360 family ---- */
.s3-badge{display:flex; width:max-content; max-width:100%; align-items:center; gap:10px; background:#fff; color:var(--slate); border:1px solid var(--line); border-radius:999px; padding:4px 14px 4px 4px; text-decoration:none; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:500; margin:0 0 18px; box-shadow:var(--shadow-soft); transition:box-shadow .2s var(--ease)}
.s3 main a.s3-badge{color:var(--slate)}
.s3-badge b{font-weight:700}
.s3-badge:hover{box-shadow:0 0 0 3px var(--mint)}
.s3-mring{width:40px; height:40px; flex:none; color:var(--slate)}
.s3-fam__head{display:flex; justify-content:space-between; align-items:end; gap:16px 30px; flex-wrap:wrap; margin-bottom:22px}
.s3-fam__head > div{flex:1 1 420px; min-width:0}
.s3-fam__head h2{margin:0; font-size:clamp(1.6rem,2.8vw,2.4rem)}
.s3-fam__list{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:10px}
.s3-fam__item{display:flex; flex-direction:column; gap:6px; padding:14px 14px 12px; background:#fff; border:1px solid var(--line); border-top:7px solid var(--c); border-radius:12px; text-decoration:none; color:var(--slate); min-width:0; transition:transform .2s, box-shadow .2s}
.s3-fam__item:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.s3-fam__item .n{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:1.7rem; line-height:1; color:var(--logo-teal)}
.s3-fam__item b{font-family:var(--display); font-stretch:104%; font-size:1rem; line-height:1.2}
.s3-fam__item small{margin-top:auto; padding-top:6px; font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal)}
.s3-fam__item.is-on{background:var(--slate); color:#fff; border-color:var(--slate); border-top-color:var(--c)}
.s3-fam__item.is-on .n,.s3-fam__item.is-on small{color:var(--mint)}
@media (max-width:1000px){.s3-fam__list{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:520px){.s3-fam__list{grid-template-columns:repeat(2,minmax(0,1fr))}}

.s3-cta{background:var(--slate-deep); color:#fff; padding-block:var(--band)}
.s3-cta__grid{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.s3-cta__photo{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:360px}
.s3-cta__photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-cta__photo .sticker{position:absolute; left:16px; bottom:18px}
.s3-cta__body{min-width:0}
.s3-cta h2{font-size:clamp(1.7rem,4vw,3.4rem); overflow-wrap:break-word; font-stretch:118%; text-transform:uppercase; font-weight:900; line-height:.95; letter-spacing:-.015em}
.s3-cta .lede{color:rgba(255,255,255,.9)}
.s3-cta .eyebrow{color:var(--mint)}
.s3-acts{display:grid; gap:10px; margin:20px 0 18px}
.s3-act{display:grid; grid-template-columns:68px minmax(0,1fr) auto; gap:16px; align-items:center; padding:15px 18px; border-radius:12px; background:rgba(255,255,255,.06); border:1.5px solid var(--line-dark); color:#fff!important; text-decoration:none; transition:border-color .2s, transform .2s}
.s3-act:hover{border-color:var(--mint); transform:translateX(3px)}
.s3-act b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.18rem; line-height:1.15; overflow-wrap:anywhere}
.s3-act small{display:block; opacity:.82; font-size:.88rem; line-height:1.4; margin-top:2px}
.s3-act__k{font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint)}
.s3-act .go{width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.1); font-weight:800}
.s3-act--main{background:var(--mint); color:var(--slate)!important; border-color:var(--mint)}
.s3-act--main .s3-act__k{color:var(--slate)}
.s3-act--main .go{background:var(--slate); color:var(--mint)}
.s3-act--main:hover{border-color:#fff}
.s3-price{font-size:.92rem; color:rgba(255,255,255,.8); border-top:1px solid var(--line-dark); padding-top:14px; margin:0}
.s3-price b{color:#fff}
.s3-cta--nophoto .s3-cta__grid{grid-template-columns:1fr}
.s3-cta--nophoto .s3-acts{grid-template-columns:repeat(3,minmax(0,1fr))}
.s3-cta--nophoto .s3-act{grid-template-columns:minmax(0,1fr) auto; align-content:start}
.s3-cta--nophoto .s3-act__k{grid-column:1/-1}
@media (max-width:900px){.s3-cta__grid{grid-template-columns:1fr} .s3-cta__photo{min-height:240px} .s3-cta--nophoto .s3-acts{grid-template-columns:1fr}}
@media (max-width:480px){.s3-act{grid-template-columns:minmax(0,1fr) auto; gap:4px 12px} .s3-act__k{grid-column:1/-1}}

.s3-checks{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.s3-checks li{position:relative; padding-left:30px; margin:0; font-weight:600; line-height:1.4}
.s3-checks li::before{content:""; position:absolute; left:0; top:.12em; width:20px; height:20px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/13px no-repeat}
.s3-checks--2{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px 20px}
@media (max-width:620px){.s3-checks--2{grid-template-columns:1fr}}

.s3-h2xl{font-size:clamp(2.1rem,4.4vw,3.8rem); font-stretch:118%; font-weight:900; text-transform:uppercase; line-height:.94; letter-spacing:-.015em}
.s3-lede-full{max-width:none}

/* spec sheet */
.s3-spec{margin:0; display:grid; border-top:1px solid var(--line)}
.s3-spec > div{display:grid; grid-template-columns:minmax(120px,.42fr) minmax(0,1fr); gap:6px 22px; padding:14px 0; border-bottom:1px solid var(--line)}
.s3-spec dt{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; padding-top:.3em}
.s3-spec dd{margin:0; font-weight:600; line-height:1.45}
@media (max-width:520px){.s3-spec > div{grid-template-columns:1fr}}

/* vibe band */
.s3-vibe__grid{display:grid; grid-template-columns:minmax(0,.75fr) minmax(0,1.25fr); gap:clamp(28px,5vw,72px); align-items:center}
.s3-vibe__phone{position:relative}
.s3-vibe__phone .sticker{position:absolute; z-index:2}
.s3-phone{position:relative; width:min(300px,72vw); margin-inline:auto; aspect-ratio:390/800; border-radius:44px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6), 0 0 0 2px rgba(255,255,255,.08); overflow:hidden; transform:rotate(3deg)}
.s3-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.s3-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:#fff; margin-bottom:16px}
.s3-vibe__mark .daisy{color:var(--mint)}
.s3-vibe__mark .daisy{width:34px; height:34px}
.s3-vibe h2{font-size:clamp(1.9rem,3.6vw,3.1rem)}
.s3-vibe__tip{display:grid; gap:4px; background:var(--slate); border-left:6px solid var(--mint); border-radius:12px; padding:16px 18px; margin:18px 0 22px}
.s3-vibe__tip b{font-family:var(--display); font-stretch:110%; font-size:1.15rem; color:var(--mint)}
.s3-vibe__tip span{font-size:.95rem; color:rgba(255,255,255,.88)}
.s3-vibe__press{display:flex; flex-wrap:wrap; gap:16px 26px; align-items:center; margin-top:26px; padding-top:20px; border-top:1px solid rgba(255,255,255,.25)}
.s3-vibe__press img{height:30px; width:auto; filter:brightness(0) invert(1); opacity:.92}
.s3-vibe__press span{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:#fff}
@media (max-width:860px){.s3-vibe__grid{grid-template-columns:1fr} .s3-vibe__phone{order:2; max-width:420px; margin-inline:auto; width:100%} .s3-phone{width:min(220px,56vw)}}

/* evidence */
.s3-ev .eyebrow{color:var(--slate)}
.s3-evtabs{display:flex; gap:8px; flex-wrap:wrap; margin:0 0 18px}
.s3-evtabs button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1rem; padding:10px 18px; border-radius:999px; border:2px solid var(--slate); background:transparent; color:var(--slate); cursor:pointer}
.s3-evtabs button[aria-selected="true"]{background:var(--slate); color:#fff}
.s3-stats{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.s3-stat{background:#fff; border-radius:14px; padding:20px 22px; min-width:0; display:flex; flex-direction:column; gap:4px}
.s3-stat b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.4rem,4vw,3.6rem); line-height:.9; letter-spacing:-.02em; color:var(--logo-teal)}
.s3-stat .k{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-stat p{margin:6px 0 0; font-size:.95rem; line-height:1.45; font-weight:500}
.s3-stat--wide{grid-column:1/-1; display:grid; grid-template-columns:auto minmax(0,1fr); gap:6px 26px; align-items:center; background:var(--slate); color:#fff}
.s3-stat--wide b{color:var(--mint); font-size:clamp(3.4rem,7vw,6rem)}
.s3-stat--wide .k{color:var(--aqua)}
.s3-stat--wide p{font-size:clamp(1.05rem,1.6vw,1.3rem); font-weight:600; margin:0}
.s3-evsrc{font-size:.85rem; margin:14px 0 0}
.s3-evfoot{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(20px,3vw,40px); align-items:center; margin-top:clamp(28px,4vw,44px); padding-top:clamp(24px,3vw,36px); border-top:2px solid rgba(29,65,78,.2)}
.s3-voices{display:grid; gap:12px}
.s3-voice{background:rgba(255,255,255,.6); border-radius:12px; padding:14px 18px; margin:0}
.s3-voice p{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.08rem; line-height:1.3; margin:0}
.s3-voice cite{display:block; font-style:normal; font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; margin-top:8px}
@media (max-width:860px){.s3-stats{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-evfoot{grid-template-columns:1fr}}
@media (max-width:560px){.s3-stats{grid-template-columns:1fr} .s3-stat--wide{grid-template-columns:1fr}}

/* steps */
.s3-steps4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media (max-width:1000px){.s3-steps4{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:560px){.s3-steps4{grid-template-columns:1fr}}
/* 2.0: eyebrows Logo Teal on light, mint on dark, white on teal */
.s3 main .eyebrow{color:var(--logo-teal)}
.s3 main :is(.band--slate,.band--deep,.band--logo,.s3-cta,.phero--logo) .eyebrow{color:var(--mint)}
.s3 main :is(.band--teal) .eyebrow{color:#fff}
.s3 main .s3-ev .eyebrow{color:var(--slate)}
/* custom-hero grammar */
.s3-hx{position:relative; overflow:hidden}
.s3-hx > .wrap{position:relative; z-index:1}
/* new for 2026-27 */
.s3-new{overflow:hidden}
.s3-new > .wrap{position:relative; z-index:1}
.s3-new .wm-daisy{right:-10%; bottom:-40%}
.s3-nps{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(16px,2vw,24px); align-items:stretch}
.s3-np{background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3vw,36px); display:flex; flex-direction:column; gap:12px; box-shadow:var(--shadow-soft); min-width:0}
.s3-np h3{margin:0; font-size:clamp(1.5rem,2.4vw,2.1rem)}
.s3-np p{margin:0; color:var(--ink-soft)}
.s3-np .btns{margin-top:auto; padding-top:8px}
.s3-np__top{display:flex; gap:18px; align-items:center; padding-bottom:16px; margin-bottom:2px; border-bottom:1px solid var(--line)}
.s3-np__k{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3 .s3-np .s3-np__when{margin:4px 0 0; font-weight:700; color:var(--slate); line-height:1.3}
.s3-cal{flex:none; width:86px; border-radius:12px; overflow:hidden; text-align:center; background:var(--slate); color:#fff; box-shadow:4px 4px 0 var(--mint); transform:rotate(-3deg)}
.s3-cal span{display:block; background:var(--mint); color:var(--slate); font-family:var(--mono); font-size:.66rem; letter-spacing:.16em; text-transform:uppercase; font-weight:700; padding:4px 0}
.s3-cal b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.4rem; line-height:1; padding:12px 4px 12px}
.s3-np__line{margin:2px 0; padding:12px 16px; border-left:5px solid var(--slate); background:var(--aqua); border-radius:0 12px 12px 0; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.15rem; line-height:1.25; color:var(--slate)}
.s3-np__line cite{display:block; margin-top:6px; font-style:normal; font-family:var(--mono); font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-plus{display:flex; align-items:center; gap:14px; flex:none}
.s3-plus__ring{position:relative; width:104px; height:104px; display:grid; place-items:center; flex:none}
.s3-plus__ring svg{position:absolute; inset:0; width:100%; height:100%; animation:s3spin 60s linear infinite}
.s3-plus__ring b{position:relative; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:1.05rem; color:#fff}
.s3-plus > i{font-style:normal; font-family:var(--display); font-weight:900; font-size:2.6rem; color:var(--mint); line-height:1}
.s3-plus__chips{display:grid; gap:8px}
.s3-plus__chips em{font-style:normal; font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:6px 10px; border-radius:8px; border:1.5px dashed rgba(21,255,200,.6); color:var(--mint); white-space:nowrap}
@keyframes s3spin{to{transform:rotate(360deg)}}
@media (max-width:860px){.s3-nps{grid-template-columns:1fr}}
@media (max-width:520px){.s3-plus{display:none}}
/* quote card */
.s3-q{font-family:var(--display); font-stretch:104%; font-weight:700; line-height:1.28; margin:0; text-wrap:pretty}
'''

CSS_360 = '''
/* ---- 360 hero ---- */
.s3-hero{color:#fff}
.s3-hero .wm-daisy{right:auto; left:-14%; bottom:-30%}
.s3-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,4vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.s3-hero h1{font-weight:900; font-stretch:122%; text-transform:uppercase; line-height:.88; letter-spacing:-.02em; font-size:clamp(2.4rem,4.6vw,4.2rem); margin:0 0 .35em}
.s3-hero h1 span{display:block}
.s3-hero h1 .big{font-size:2.3em; font-stretch:125%; line-height:.84; letter-spacing:-.035em; margin:.02em 0 .04em}
.s3-hero__sub{font-family:var(--display); font-stretch:108%; font-weight:700; font-size:clamp(1.15rem,1.7vw,1.45rem); line-height:1.25; color:var(--aqua); margin:0 0 .9em}
.s3-hero .lede{color:rgba(255,255,255,.88); font-size:clamp(1rem,1.25vw,1.15rem)}
.s3-proof{display:flex; flex-wrap:wrap; gap:8px 22px; margin:24px 0 0; padding:0; list-style:none; font-weight:600; font-size:.9rem; color:var(--aqua)}
.s3-proof li{margin:0}
.s3-proof li::before{content:""; display:inline-block; width:8px; height:8px; background:var(--mint); margin-right:8px; transform:rotate(45deg) translateY(-2px)}
.s3-mosaic{position:relative; display:grid; grid-template-columns:1fr 1fr; gap:12px; align-items:start}
.s3-mosaic__col{display:grid; gap:12px; min-width:0}
.s3-mosaic__col:nth-child(2){margin-top:56px}
.s3-mosaic img{width:100%; border-radius:var(--r-xl); object-fit:cover}
.s3-mosaic .t{aspect-ratio:4/5} .s3-mosaic .s{aspect-ratio:1}
.s3-orb{position:absolute; left:50%; top:52%; width:clamp(130px,14vw,190px); aspect-ratio:1; transform:translate(-50%,-50%); border-radius:50%; background:var(--slate); box-shadow:0 0 0 10px var(--slate), 0 24px 60px -10px rgba(0,0,0,.6); display:grid; place-items:center; z-index:2}
.s3-orb svg{position:absolute; inset:6px; width:calc(100% - 12px); height:calc(100% - 12px); animation:s3spin 48s linear infinite}
.s3-orb span{position:relative; font-family:var(--display); font-weight:900; font-stretch:125%; color:#fff; font-size:clamp(1.6rem,2.4vw,2.3rem); letter-spacing:-.02em}
@keyframes s3spin{to{transform:rotate(360deg)}}
.s3-mosaic .sticker{position:absolute; z-index:3}
@media (max-width:900px){.s3-hero__grid{grid-template-columns:1fr} .s3-mosaic{max-width:560px}}

/* intro */
.s3-intro{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,60px); align-items:stretch}
.s3-intro__card{background:#fff; border-radius:var(--r-xl); padding:clamp(22px,3vw,34px); border:1px solid var(--line); border-top:8px solid var(--mint); display:flex; flex-direction:column}
.s3-intro__card h3{font-size:clamp(1.4rem,2.2vw,1.9rem)}
.s3-intro__card .btns{margin-top:auto; padding-top:16px}
@media (max-width:860px){.s3-intro{grid-template-columns:1fr}}

/* ring */
.s3-ringwrap{display:grid; grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr); gap:clamp(24px,4vw,64px); align-items:center}
.s3-ringwrap .ring{width:100%; max-width:460px; margin-inline:auto; display:block; overflow:visible}
.s3-ringwrap .seg{cursor:pointer; transition:transform .25s; transform-origin:210px 210px; outline:none}
.s3-ringwrap .seg path{transition:opacity .25s}
.s3-ringwrap .ring.has-active .seg:not(.on) path{opacity:.35}
.s3-ringwrap .seg.on{transform:scale(1.045)}
.s3-ringwrap .seg:focus-visible path{stroke:#1d414e; stroke-width:4}
.s3-ringhint{text-align:center; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-soft); margin-top:14px}
.s3-pick{display:flex; flex-wrap:wrap; gap:6px; margin-bottom:18px}
.s3-pick button{font:inherit; font-size:.82rem; font-weight:700; border:1.5px solid var(--line); background:#fff; border-radius:999px; padding:6px 12px; cursor:pointer; color:var(--slate); display:inline-flex; align-items:center; gap:7px}
.s3-pick button i{width:10px; height:10px; border-radius:50%; background:var(--c); box-shadow:0 0 0 1px rgba(29,65,78,.25)}
.s3-pick button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.s3-comps{display:grid}
.js .s3-comp{grid-area:1/1; visibility:hidden; opacity:0; transition:opacity .3s}
.js .s3-comp.on{visibility:visible; opacity:1}
.s3-comp{min-width:0; padding:4px 0 8px}
.s3-comp + .s3-comp{margin-top:28px}
.js .s3-comp + .s3-comp{margin-top:0}
.s3-comp__top{display:flex; gap:16px; align-items:center; margin-bottom:12px}
.s3-comp__n{flex:none; width:64px; height:64px; border-radius:50%; display:grid; place-items:center; background:var(--c); color:var(--ci); font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2rem; line-height:1}
.s3-comp__top h3{margin:0; font-size:clamp(1.4rem,2.3vw,2rem)}
.s3-comp > p{color:var(--ink-soft)}
.s3-comp .s3-checks{margin:16px 0 18px}
.s3-comp__links{display:flex; flex-wrap:wrap; gap:10px}
@media (max-width:900px){.s3-ringwrap{grid-template-columns:1fr} .s3-ringwrap .ring{max-width:320px}}

.s3-steps-note{display:flex; flex-wrap:wrap; gap:12px 24px; align-items:center; justify-content:space-between; margin-top:22px; padding:16px 20px; border-radius:12px; border:1px dashed rgba(209,254,255,.35)}
.s3-steps-note p{margin:0; color:rgba(255,255,255,.85); flex:1 1 420px}

/* roles */
.s3-roles__tabs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin-bottom:22px}
.s3-roles__tab{font:inherit; text-align:left; padding:14px 16px; border-radius:12px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; display:flex; flex-direction:column; gap:3px}
.s3-roles__tab small{font-family:var(--mono); font-size:.64rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal)}
.s3-roles__tab span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.1rem; line-height:1.15}
.s3-roles__tab:hover{border-color:var(--teal)}
.s3-roles__tab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.s3-roles__tab[aria-selected="true"] small{color:var(--mint)}
.s3-roles__panel{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(20px,4vw,48px); align-items:stretch}
.s3-roles__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:300px}
.s3-roles__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-roles__panel h3{font-size:clamp(1.4rem,2.3vw,1.9rem); margin-bottom:.35em}
@media (max-width:900px){.s3-roles__tabs{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-roles__panel{grid-template-columns:1fr} .s3-roles__img{min-height:200px}}

/* impact quote */
.s3-impact{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,72px); align-items:center}
.s3-pq{margin:0; position:relative; padding-left:clamp(0px,2vw,28px); border-left:4px solid var(--mint)}
.s3-pq .quote{font-size:clamp(1.12rem,1.6vw,1.42rem); line-height:1.42; font-weight:600; color:#fff}
.s3-pq .quote::before{font-size:5em; margin-bottom:.12em}
.s3-pq .cite{color:var(--mint)}
.s3-imp__vid .small{margin-top:14px; color:rgba(255,255,255,.82)}
@media (max-width:620px){.s3-pq{padding-left:16px}}
@media (max-width:860px){.s3-impact{grid-template-columns:1fr}}

/* logos */
.s3-logos{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.s3-logo{background:transparent; border:1px solid var(--line); border-radius:12px; padding:18px 14px 14px; display:flex; flex-direction:column; align-items:center; justify-content:space-between; gap:12px; min-height:156px; text-align:center; min-width:0}
.s3-logo img{height:92px; width:100%; object-fit:contain; margin:auto 0}
.s3-logo span{font-size:.78rem; font-weight:600; color:var(--ink-soft); line-height:1.3}
@media (max-width:760px){.s3-logos{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-logo{min-height:130px} .s3-logo img{height:70px}}

/* rees */
.s3-rees{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:clamp(24px,4vw,60px); align-items:center}
.s3-rees__feats{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:22px 0}
.s3-rees__feats div{background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-radius:12px; padding:18px; min-width:0}
.s3-rees__feats b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.08rem; color:var(--mint); margin-bottom:4px}
.s3-rees__feats p{margin:0; font-size:.92rem; color:rgba(255,255,255,.82)}
.s3-rees__logo{background:rgba(255,255,255,.04); border:1.5px solid var(--line-dark); border-radius:var(--r-xl); padding:34px; display:grid; place-items:center; gap:16px}
.s3-rees__logo img{filter:brightness(0) invert(1); max-width:240px; width:100%}
.s3-rees__logo p{margin:0; color:var(--aqua); font-weight:600; text-align:center; font-size:.95rem}
@media (max-width:860px){.s3-rees{grid-template-columns:1fr} .s3-rees__feats{grid-template-columns:1fr}}

/* pods */
.s3-pods{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.s3-pods .audio{height:100%}
.s3-pods .audio > span:nth-of-type(1){min-width:0}
@media (max-width:960px){.s3-pods{grid-template-columns:1fr}}
'''

CSS_CURR = '''
.s3-ch{background:var(--aqua); color:var(--slate); overflow:hidden}
.s3-ch .crumbs{color:var(--ink-soft)} .s3-ch .crumbs a{color:var(--logo-teal)}
.s3-ch__grid{display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(28px,4vw,64px); align-items:center; padding-block:clamp(48px,6vw,84px)}
.s3-ch h1{font-weight:900; font-stretch:110%; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; font-size:clamp(1.9rem,3.7vw,3.5rem); margin:0 0 .35em; color:var(--slate); overflow-wrap:anywhere}
.s3-ch .wm-daisy{color:var(--logo-teal); opacity:.08}
@media (prefers-reduced-motion:no-preference){.s3-tile{animation:s3pop .55s var(--ease) backwards; animation-delay:calc(var(--i) * 40ms + .25s)}}
@keyframes s3pop{from{opacity:0; transform:translateY(12px) scale(.94)}}
.s3-ch .lede{max-width:none}
.s3-facts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:8px; margin:6px 0 24px}
.s3-facts div{background:#fff; border-radius:12px; padding:12px 14px; min-width:0}
.s3-facts b{display:block; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.5rem; line-height:1; color:var(--logo-teal)}
.s3-facts span{display:block; font-size:.8rem; font-weight:600; color:var(--ink-soft); margin-top:4px; line-height:1.3}
@media (max-width:620px){.s3-facts{grid-template-columns:repeat(2,minmax(0,1fr))}}
.s3-tiles{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px}
.s3-tile{position:relative; display:grid; grid-template-columns:auto minmax(0,1fr); align-items:center; gap:12px; min-height:84px; padding:12px 14px; border-radius:12px; text-decoration:none; background:var(--tb); color:var(--tc); border:2px solid var(--tbd, transparent); transition:transform .2s, box-shadow .2s; min-width:0; overflow:hidden}
.s3-tile:hover{transform:translateY(-4px) rotate(-1deg); box-shadow:var(--shadow-soft)}
.s3-tile b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(1.5rem,2.3vw,2.2rem); line-height:.9; min-width:1.15em; text-align:center}
.s3-tile span{font-size:.84rem; font-weight:700; line-height:1.22}
.u-core{--tb:var(--slate); --tc:#fff} .u-core b{color:var(--mint)}
.u-found{--tb:var(--logo-teal); --tc:#fff} .u-found b{color:var(--aqua)}
.u-heal{--tb:#fff; --tc:var(--slate); --tbd:var(--teal)} .u-heal b{color:var(--teal)}
.u-just{--tb:var(--mint); --tc:var(--slate)}
.s3-legend{display:flex; flex-wrap:wrap; gap:8px 18px; margin-top:16px; font-size:.82rem; font-weight:600}
.s3-legend span{display:inline-flex; align-items:center; gap:8px}
.s3-legend i{width:14px; height:14px; border-radius:4px; background:var(--tb); border:2px solid var(--tbd, transparent)}
@media (max-width:900px){.s3-ch__grid{grid-template-columns:1fr}}
@media (max-width:620px){.s3-tile{grid-template-columns:1fr; align-content:start; gap:6px; padding:10px} .s3-tile b{text-align:left} .s3-tile span{font-size:.72rem; overflow-wrap:anywhere}}

.s3-who3{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.s3-who3 > div{background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:24px; min-width:0; display:flex; flex-direction:column; gap:8px}
.s3-who3 small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-who3 h3{margin:0; font-size:1.4rem}
.s3-who3 p{margin:0; color:var(--ink-soft); font-size:.96rem}
.s3-who3 .arrow-link{margin-top:auto; padding-top:6px}
@media (max-width:860px){.s3-who3{grid-template-columns:1fr}}

#lessons{scroll-margin-top:90px}
.s3-utabs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin:0 0 20px}
.s3-utabs button{font:inherit; cursor:pointer; text-align:left; padding:14px 16px; border-radius:14px; border:2px solid var(--line-dark); background:transparent; color:#fff; display:flex; flex-direction:column; gap:4px; min-width:0}
.s3-utabs button small{display:flex; align-items:center; gap:8px; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua)}
.s3-utabs button small i{width:12px; height:12px; border-radius:3px; background:var(--tb); border:2px solid var(--tbd, rgba(255,255,255,.4))}
.s3-utabs button span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.15rem; line-height:1.15}
.s3-utabs button:hover{border-color:var(--mint)}
.s3-utabs button[aria-selected="true"]{background:#fff; color:var(--slate); border-color:#fff}
.s3-utabs button[aria-selected="true"] small{color:var(--logo-teal)}
.s3-unit{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(20px,4vw,52px); align-items:start}
.s3-unit h3{font-size:clamp(1.6rem,2.8vw,2.4rem); margin-bottom:.3em}
.s3-unit__range{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); margin:0 0 10px}
.s3-unit > div > p{color:rgba(255,255,255,.85)}
.s3-lessons{display:grid; gap:8px}
.s3-lesson{display:grid; grid-template-columns:64px minmax(0,1fr); gap:4px 16px; align-items:center; padding:14px 16px; border-radius:12px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); scroll-margin-top:110px; transition:background .3s, box-shadow .3s}
.s3-lesson__n{grid-row:span 2; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.4rem; line-height:1; color:var(--mint); text-align:center}
.s3-lesson__t{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.18rem; line-height:1.2}
.s3-lesson__t:last-child{grid-row:span 2}
.s3-lesson__rel{font-size:.84rem; font-weight:600; color:var(--aqua)!important; text-decoration:none}
.s3-lesson__rel:hover{text-decoration:underline; text-decoration-color:var(--mint)}
.s3-lesson__rel::before{content:"Related in the library: "; font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; text-transform:uppercase; color:rgba(255,255,255,.6); font-weight:500}
.s3-lesson.is-hl{background:rgba(21,255,200,.16); box-shadow:0 0 0 2px var(--mint)}
@media (max-width:900px){.s3-utabs{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-unit{grid-template-columns:1fr}}
@media (max-width:460px){.s3-lesson{grid-template-columns:44px minmax(0,1fr)} .s3-lesson__n{font-size:1.8rem}}

.s3-incl{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,4vw,60px); align-items:stretch}
.s3-incl__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:380px}
.s3-incl__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-incl__img .sticker{position:absolute; right:16px; bottom:18px}
.s3-pack{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:20px 0}
.s3-pack div{border-radius:14px; padding:18px; background:var(--mist); border:1px solid var(--line); min-width:0}
.s3-pack div:nth-child(1){background:var(--slate); color:#fff; border-color:var(--slate)}
.s3-pack div:nth-child(4){background:var(--mint); border-color:var(--mint)}
.s3-pack small{display:block; font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; opacity:.75; margin-bottom:6px}
.s3-pack b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.2}
@media (max-width:860px){.s3-incl{grid-template-columns:1fr} .s3-incl__img{min-height:240px}}
@media (max-width:520px){.s3-pack{grid-template-columns:1fr}}

.s3-fac{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,60px); align-items:stretch}
.s3-anat{color:var(--slate); background:#fff; border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft); display:flex; flex-direction:column}
.s3-anat__img{flex:1 1 auto; min-height:240px; position:relative; overflow:hidden}
.s3-anat__img img{position:absolute; inset:0}
.s3-anat__img img{width:100%; height:100%; object-fit:cover}
.s3-anat__body{padding:20px 22px 22px}
.s3-anat__body h3{font-size:1.3rem}
.s3-anat ul{list-style:none; padding:0; margin:0; display:flex; flex-wrap:wrap; gap:8px}
.s3-anat li{margin:0; padding:8px 12px; border-radius:8px; background:var(--aqua); font-weight:700; font-size:.9rem}
.s3-anat li.k{background:var(--slate); color:#fff}
.s3-email{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; margin-top:18px; padding:16px 18px; border-radius:14px; background:#fff; color:var(--slate); border:1px solid var(--line)}
#guide .lede{color:#fff} #guide p{color:rgba(255,255,255,.88)} #guide .s3-email p, #guide .helpline span{color:inherit}
.s3-email b{font-family:var(--display); font-stretch:106%}
@media (max-width:900px){.s3-fac{grid-template-columns:1fr}}
.s3-two{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px}
.s3-three{grid-template-columns:repeat(3,minmax(0,1fr))}
.s3 .s3-two > a{color:var(--slate)}
.s3 .s3-two .arrow-link{color:var(--logo-teal)}
.s3-two > a.is-new{background:var(--mint); border-color:var(--mint)}
.s3-two > a.is-new small{color:var(--slate)}
.s3-two > a.is-new p{color:var(--slate)}
@media (max-width:960px){.s3-three{grid-template-columns:1fr}}
.s3-two > a{display:flex; flex-direction:column; gap:8px; padding:26px; border-radius:var(--r-xl); text-decoration:none; color:var(--slate); background:#fff; border:1px solid var(--line); transition:transform .2s, box-shadow .2s; min-width:0}
.s3-two > a:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.s3-two small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-two h3{margin:0; font-size:1.45rem}
.s3-two p{margin:0; color:var(--ink-soft)}
.s3-two .arrow-link{margin-top:auto; padding-top:6px}
@media (max-width:760px){.s3-two{grid-template-columns:1fr}}
'''

CSS_PD = '''
.s3-pdh .phero__media img{aspect-ratio:5/4}
.s3-pdh h1{font-size:clamp(2.1rem,3.9vw,3.7rem); font-stretch:114%}
.s3-pdh .lede{max-width:none}
.s3-aud{display:flex; flex-wrap:wrap; gap:8px; margin:-.2em 0 1.4em}
.s3-aud span{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:6px 10px; border-radius:6px; background:rgba(255,255,255,.12); color:#fff; border:1px solid rgba(255,255,255,.22)}
.s3-topics{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px}
.s3-topic{display:flex; flex-direction:column; gap:12px; padding:22px; border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); border-top:8px solid var(--c); min-width:0}
.s3-topic h3{margin:0; font-size:clamp(1.15rem,1.6vw,1.35rem); line-height:1.2}
.s3-topic small{font-family:var(--mono); font-size:.66rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-topic .arrow-link{margin-top:auto; font-size:.92rem; display:block}
.s3-topic .arrow-link::after{content:"\\00a0\\2192"; display:inline; margin-left:.15em}
@media (max-width:960px){.s3-topics{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:620px){.s3-topics{grid-template-columns:1fr}}
.s3-fmt{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.s3-fmt__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:340px}
.s3-fmt__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-fmt__card{background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3vw,34px); min-width:0}
.s3-fmt__card .eyebrow{color:var(--teal)}
.s3-modes{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; margin:18px 0 6px}
.s3-modes div{border-radius:12px; padding:16px; background:var(--aqua); text-align:center}
.s3-modes div:last-child{background:var(--mint)}
.s3-modes b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.05rem,3.6vw,1.5rem); line-height:1; text-transform:uppercase}
.s3-modes span{font-size:.82rem; font-weight:600}
@media (max-width:860px){.s3-fmt{grid-template-columns:1fr} .s3-fmt__img{min-height:240px}}
.s3-tgrid{display:grid; grid-template-columns:minmax(0,1.55fr) minmax(0,.85fr); gap:14px; align-items:stretch}
.s3-bars{background:#fff; border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); display:grid; gap:16px; box-shadow:var(--shadow-soft)}
.s3-bars__cap{margin:0; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-bar__t{margin:0 0 6px; font-weight:600; font-size:.95rem; line-height:1.35}
.s3-bar__track{display:flex; align-items:center; gap:12px}
.s3-bar__track i{display:block; flex:none; height:22px; border-radius:0 6px 6px 0; background:var(--slate); width:calc(var(--v) / 55 * (100% - 74px)); transition:width 1s var(--ease)}
.s3-bar:first-of-type .s3-bar__track i{background:var(--teal)}
.s3-bar__track b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:1.6rem; line-height:1; color:var(--logo-teal)}
.js .s3-bars:not(.in) .s3-bar__track i{width:0}
.s3-tside{display:grid; gap:14px}
.s3-tside .s3-stat{justify-content:center}
@media (max-width:900px){.s3-tgrid{grid-template-columns:1fr} .s3-tside{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.s3-tside{grid-template-columns:1fr}}
.s3-tq{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:16px 30px; align-items:center; margin-top:22px; padding-top:22px; border-top:2px solid rgba(29,65,78,.2)}
.s3-tq .s3-q{font-size:clamp(1.1rem,1.8vw,1.45rem)}
@media (max-width:760px){.s3-tq{grid-template-columns:1fr}}
'''

CSS_POL = '''
.s3-ph{background:var(--teal); color:#fff; overflow:hidden}
.s3-ph__grid{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,4vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.s3-ph h1{font-weight:900; font-stretch:118%; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; font-size:clamp(2.2rem,4.4vw,4.1rem); margin:0 0 .35em}
.s3-ph .wm-daisy{color:var(--aqua); opacity:.12}
.s3-ph .lede{color:rgba(255,255,255,.92); max-width:none}
.s3-ph .crumbs{color:#fff} .s3-ph .crumbs a{color:#fff; text-decoration:underline; text-decoration-color:rgba(255,255,255,.5); text-underline-offset:3px}
.s3-covers{position:relative; aspect-ratio:1/.9; max-width:540px; margin-inline:auto; width:100%}
.s3-cover{position:absolute; margin:0; background:#fff; padding:10px; border-radius:14px; box-shadow:var(--shadow-soft), 0 30px 60px -30px rgba(0,0,0,.45)}
.s3-cover img{border-radius:4px; width:100%}
.s3-cover--student{right:2%; top:2%; width:46%; transform:rotate(5deg)}
.s3-cover--admin{left:6%; top:6%; width:52%; transform:rotate(-4deg); z-index:2}
.s3-cover--admin .s3-cover__lines{display:grid; gap:7px; margin-top:12px}
.s3-cover--admin .s3-cover__lines i{display:block; height:7px; border-radius:4px; background:var(--gray)}
.s3-cover--admin .s3-cover__lines i:nth-child(2){width:86%} .s3-cover--admin .s3-cover__lines i:nth-child(3){width:64%}
.s3-cover .sticker{position:absolute; white-space:nowrap}
@media (max-width:520px){.s3-cover .sticker{font-size:.72rem}}
.s3-cover--student .sticker{right:-8px; top:-16px}
.s3-cover--admin .sticker{left:-12px; bottom:-14px}
@media (max-width:900px){.s3-ph__grid{grid-template-columns:1fr} .s3-covers{max-width:440px}}

.s3-why{display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(24px,4vw,64px); align-items:start}
.s3-why .tl__item{grid-template-columns:110px minmax(0,1fr)}
.s3-why .tl__year.now{color:var(--slate); display:flex; align-items:center; gap:.3em}
.s3-why .tl__year.now::before{content:""; width:.42em; height:.42em; border-radius:50%; background:var(--coral); flex:none; box-shadow:0 0 0 4px rgba(254,113,113,.25)}
.s3-risk{display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:24px}
.s3-risk div{border-radius:14px; padding:18px 20px; min-width:0}
.s3-risk div:first-child{background:var(--slate); color:#fff}
.s3-risk div:last-child{background:var(--aqua)}
.s3-risk small{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; margin-bottom:6px; opacity:.8}
.s3-risk b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.25}
@media (max-width:900px){.s3-why{grid-template-columns:1fr}} @media (max-width:560px){.s3-risk{grid-template-columns:1fr} .s3-why .tl__item{grid-template-columns:1fr}}

.s3-gp{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; align-items:stretch}
.s3-gp > div{border-radius:var(--r-xl); padding:clamp(22px,3vw,32px); display:flex; flex-direction:column; gap:10px; min-width:0}
.s3-gp > div:first-child{background:#fff; color:var(--slate)}
.s3-gp > div:last-child{background:rgba(255,255,255,.06); border:1px solid var(--line-dark)}
.s3-gp h3{font-size:clamp(1.35rem,2vw,1.7rem); margin:0}
.s3-gp small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-gp > div:last-child small{color:var(--mint)}
.s3-gp > div:last-child .s3-checks li::before{background-color:var(--mint)}
.s3-gp .btns{margin-top:auto; padding-top:10px}
.s3-gp p{margin:0}
.s3-gp__foot{margin-top:auto; padding-top:12px; display:flex; align-items:flex-end; gap:20px; flex-wrap:wrap}
.s3-gp__foot .btns{margin:0; padding:0}
.s3-gp__cover img{width:118px; height:auto; border-radius:8px; border:1px solid var(--line); box-shadow:var(--shadow-soft); transform:rotate(-2deg)}
.s3-qual{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; margin-top:18px}
.s3-qual span{display:block; text-align:center; padding:12px 8px; border-radius:10px; border:2px solid var(--mint); color:var(--mint); font-family:var(--display); font-weight:900; font-stretch:115%; text-transform:uppercase; font-size:.92rem; line-height:1.1}
@media (max-width:860px){.s3-gp{grid-template-columns:1fr}}

.s3-uses{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.s3-uses > div{background:#fff; border:1px solid var(--line); border-top:7px solid var(--mint); border-radius:var(--r-xl); padding:22px; min-width:0}
.s3-uses > div:nth-child(2){border-top-color:var(--teal)} .s3-uses > div:nth-child(3){border-top-color:var(--logo-teal)} .s3-uses > div:nth-child(4){border-top-color:var(--slate)}
.s3-uses h3{font-size:1.2rem} .s3-uses p{margin:0; color:var(--ink-soft); font-size:.95rem}
@media (max-width:1000px){.s3-uses{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:560px){.s3-uses{grid-template-columns:1fr}}
.band--logo .s3-stud .lede{color:#fff} .band--logo .s3-stud p{color:rgba(255,255,255,.88)}
.s3-stud{display:grid; grid-template-columns:minmax(0,.55fr) minmax(0,1.45fr); gap:clamp(24px,4vw,64px); align-items:center}
.s3-stud__cover img{width:100%; max-width:300px; border-radius:10px; box-shadow:0 30px 60px -24px rgba(0,0,0,.6); transform:rotate(-3deg)}
@media (max-width:760px){.s3-stud{grid-template-columns:1fr} .s3-stud__cover img{max-width:200px}}
'''

CSS_ACC = '''
.s3-ah{color:#fff}
.s3-ah__grid{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,4vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.s3-ah .crumbs{color:rgba(255,255,255,.75)}
.s3-ah h1{font-weight:900; font-stretch:108%; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; font-size:clamp(1.9rem,3.6vw,3.4rem); margin:0 0 .35em; color:#fff; overflow-wrap:anywhere}
.s3-ah .lede{max-width:none; color:rgba(255,255,255,.9)}
.s3-ahv{position:relative; padding:0 0 72px 0}
.s3-ahv__img{border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft)}
.s3-ahv__img img{width:100%; aspect-ratio:4/3; object-fit:cover}
.s3-ahv .sticker{position:absolute; right:-8px; top:18px; z-index:2}
.s3-ahq{position:absolute; left:-28px; bottom:0; width:min(86%,440px); margin:0; z-index:2; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:22px 26px 20px; box-shadow:var(--shadow-soft), 0 24px 50px -30px rgba(0,0,0,.5); animation:sb-rise .9s .35s var(--ease) both}
.s3-ahq .s3-q{font-size:clamp(1.15rem,1.75vw,1.5rem); line-height:1.2}
.s3-ahq .s3-q::before{content:"\\201C"; display:block; font-size:3em; line-height:.5; margin-bottom:.08em; color:var(--teal); font-stretch:125%}
.s3-ahq cite{display:block; margin-top:12px; font-style:normal; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal)}
@media (max-width:900px){.s3-ahv{padding:0; max-width:620px} .s3-ahq{position:relative; left:auto; bottom:auto; width:auto; margin:-44px 14px 0}}
@media (max-width:900px){.s3-ah__grid{grid-template-columns:1fr}}
.s3-choice{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,64px); align-items:center}
.s3-choice__card{background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:clamp(24px,3.4vw,40px); display:flex; flex-direction:column; justify-content:center; min-width:0}
.s3-choice__card strong{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(2.6rem,5.2vw,4.6rem); line-height:.85; letter-spacing:-.03em; margin-bottom:.25em}
.s3-choice__card p{font-weight:600; font-size:1.05rem; margin:0}
@media (max-width:860px){.s3-choice{grid-template-columns:1fr}}
.s3-atopics{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px}
.s3-atopic{display:flex; flex-direction:column; justify-content:space-between; gap:12px; padding:18px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); min-height:132px; min-width:0}
.s3-atopic b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.12rem; line-height:1.2}
.s3-atopic span{align-self:flex-start; font-family:var(--mono); font-size:.62rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint); border:1px solid rgba(21,255,200,.45); border-radius:4px; padding:3px 6px}
@media (max-width:960px){.s3-atopics{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:520px){.s3-atopic{min-height:0; padding:14px} .s3-atopic b{font-size:.98rem}}
.s3-fit{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,4vw,64px); align-items:start}
@media (max-width:860px){.s3-fit{grid-template-columns:1fr}}
'''

# ------------------------------------------------------------------ data
COMP_DATA = [
  dict(text='Students complete a self-paced, online certification to become Peer Educators, equipping them with the knowledge, skills, and support to lead prevention efforts in their schools. Youth leaders help shape implementation, lead presentations, co-facilitate curriculum sessions, organize campaigns through SafeBAE Clubs, and receive ongoing mentorship from our team.',
       gets=['Self-paced online certification', 'Youth leaders who help shape implementation', 'Student-led presentations', 'Co-facilitators for curriculum sessions', 'Campaigns through SafeBAE Clubs', 'Ongoing mentorship from our team'],
       links=[('Peer Educator Training', 'peer-educator.html'), ('SafeBAE Clubs', 'clubs.html')]),
  dict(text='A trauma-informed curriculum of 15 lessons aligned with the National Health Education Standards. Lessons cover consent, boundaries, communication, digital safety, healing, and accountability. Schools receive a complete curriculum package, including lesson plans, slides, activities, and printable resources, delivered by teachers and peer educators with support from our team.',
       gets=['15 lessons aligned with NHES', 'Lesson plans and facilitation guides', 'Slide decks and multimedia', 'Activities, assessments and printables', 'Available in English and Spanish', 'Support from our team'],
       links=[('The 15 lessons', 'consent-curriculum.html')]),
  dict(text='Professional development for teachers, staff, and administrators focuses on trauma-informed response, supporting marginalized students, and building a school culture of consent and accountability. Trainings are flexible and tailored to school contexts.',
       gets=['Trauma-informed response', 'Supporting marginalized students', 'A culture of consent and accountability', 'Teachers, staff and administrators', 'Tailored to your school', 'In person or virtual'],
       links=[('Faculty & Staff Training', 'professional-development.html')]),
  dict(text='Hands-on consultation helps schools audit and revise sexual misconduct and Title IX policies. Support includes annotated audits, student-centered model language, communication templates, and rollout strategies to ensure policies are accessible, compliant, trusted, and trauma-informed.',
       gets=['Annotated audits', 'Student-centered model language', 'Communication templates', 'Rollout strategies'],
       links=[('Policy Reform Guide', 'policy-reform-guide.html'), ('Student version', 'reform-policy.html')]),
  dict(text='A secure, private space where students can document incidents of harm or violence at their own pace. Students have the option to report anonymously or by name directly to their school, and are connected with school-specific resources and support. Schools can partner with SafeBAE and REES to implement this tool, creating a trusted, customized reporting system that works for their community.',
       gets=['Private documentation, at a student’s own pace', 'Anonymous or named reports to the school', 'School-specific resources and support', 'A reporting system customized to your community'],
       links=[('About the tool', '#rees')]),
  dict(text='A suite of tools designed for students who have caused harm, supporting education, accountability, and behavior change. It includes our structured Accountability Training and Vibe Check, a self-assessment tool that helps students recognize unhealthy relationship behaviors and warning signs in themselves. Rooted in prevention, healing, and restorative justice rather than punishment, these resources give schools a trauma-informed, developmentally appropriate alternative to traditional disciplinary responses.',
       gets=['Structured Accountability Training', 'Vibe Check self-assessment', 'Rooted in restorative justice', 'Developmentally appropriate'],
       links=[('Accountability Training', 'accountability-training.html'), ('Vibe Check', '#vibe-check')]),
]

UNITS = [
  ('core', 'u-core', 'Core Concepts', 'Lessons 1–6', 'Basic concepts to address with students related to dating violence, sexual violence, and healthy relationships.',
   [(1, 'Healthy Relationships', ('It’s Giving Red Flags', 'film-its-giving-red-flags.html')), (2, 'Consent', None),
    (3, 'Online Safety & Sending Nudes', ('#knowB4Unude', 'film-knowb4unude.html')), (4, 'Bystander Intervention', ('BAEcode: Game On!', 'film-baecode-game-on.html')),
    (5, 'Male Youth & Sexual Violence', ('Supporting Male Survivors', 'film-sexual-assault-of-men.html')), (6, 'If You’ve Been Accused of Sexual Assault', ('Accountability Training', 'accountability-training.html'))]),
  ('foundations', 'u-found', 'Foundational Knowledge', 'Lessons 7–10', 'Foundations of understanding sexual violence, expanding on definitions of crimes, and the influence of media, pop culture, and myths.',
   [(7, 'Rape Culture', ('Rape Culture to a Culture of Respect', 'film-rape-culture.html')), (8, 'Sexual Harassment, Assault, Rape – Defined', None),
    (9, 'Violence in the Media', None), (10, 'Myths, Facts & Stats', ('Myths & Facts', 'myths-facts.html'))]),
  ('healing', 'u-heal', 'Healing Resources', 'Lessons 11–13', 'Victim support and healing after incidents of violence, including how peers can support survivors and how individuals can take steps towards healing and moving forward in new relationships.',
   [(11, 'Healing After Sexual Violence', None), (12, 'Support a Survivor', ('Survivor Support', 'survivor-support.html')),
    (13, 'Dating After Violence', ('Intimacy & Dating After Assault', 'film-dating-after-sexual-assault.html'))]),
  ('justice', 'u-just', 'Justice Options', 'Lessons 14–15', 'Options for justice after experiencing violence with a focus on victim autonomy, a review of Title IX policies and procedures, and other methods for reporting crimes.',
   [(14, 'Title IX', ('Title IX: your rights at school', 'title-ix.html')), (15, 'Options for Reporting', None)]),
]

STUDENT_STATS = [
  ('23%', 'increase', 'in students attending an event or program about what they can do as a bystander to stop dating violence, sexual violence or stalking'),
  ('18%', 'increase', 'in students knowing how to find school policies about dating violence, sexual violence or stalking, or having been given a copy'),
  ('17%', 'increase', 'in students having a conversation with a teacher or administrator at their school about healthy relationships'),
  ('10%', 'increase', 'in students discussing dating violence, sexual violence or stalking with another student at their school'),
  ('10%', 'less likely', 'to describe barriers to bystander intervention that would stop them from intervening if they saw harm occurring'),
  ('5%', 'increase', 'in students having a conversation with another student about healthy relationships'),
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
    return f'<div class="s3-stat {cls}"><b>{esc(n)}</b><div><span class="k">{esc(k)}</span><p>{esc(d)}</p></div></div>'

# ------------------------------------------------------------------ pages
def p360():
    comps = RCOMPS
    # hero orb ring
    orb = mini_ring(None, 's3-orbsvg')
    mosaic = f'''<div class="s3-mosaic">
      <div class="s3-mosaic__col">{img('1-000383-edited', 'SafeBAE youth leaders in tie-dye shirts posing together', 't', loading='eager')}{img('1-9035c3ab-2096-403f-9e8d-56238bfde8a1', 'Two students and a SafeBAE staff member holding SafeBAE t-shirts', 's', loading='eager')}</div>
      <div class="s3-mosaic__col">{img('1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'Students holding up SafeBAE water bottles outdoors', 's', loading='eager')}{img('1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'Five young SafeBAE leaders standing together on a campus walkway', 't', loading='eager')}</div>
      <div class="s3-orb" aria-hidden="true">{orb}<span>360&deg;</span></div>
      <span class="sticker" style="left:-10px;top:8%">Youth-led</span>
      <span class="sticker sticker--white sticker--r" style="right:-6px;bottom:10%">Survivor-centered</span>
    </div>'''
    hero = f'''<section class="s3-hero s3-hx band--slate">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-hero__grid">
    <div class="rise">
      {crumbs([('Home', 'index.html'), ('360° Schools', None)])}
      <p class="eyebrow">For schools and districts</p>
      <h1 aria-label="SafeBAE 360° Schools"><span>SafeBAE</span><span class="big mk">360&deg;</span><span>Schools</span></h1>
      <p class="s3-hero__sub">Tools, training and youth leadership to build safer school communities, together.</p>
      <p class="lede">SafeBAE 360° is a comprehensive, survivor-centered prevention model that reimagines how schools address sexual and dating violence. Created by and for young people, it builds lasting infrastructure for prevention across education, leadership, policy, reporting and accountability, so that every student has access to support and every school has the tools to respond.</p>
      <div class="btns">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('Book a 60-minute meeting', CAL, 'ghost')}</div>
      <ul class="s3-proof"><li>Six components</li><li>Start with one or build the whole model</li><li>Sliding scale pricing</li></ul>
    </div>
    {mosaic}
  </div>
</section>'''

    intro = f'''<section class="band band--mist">
  <div class="wrap s3-intro">
    <div>
      <h2>Young people lead every implementation.</h2>
      <p class="lede">Rather than treating students as passive recipients of adult-designed interventions, SafeBAE 360° equips young people to lead. Each implementation is adapted to the school’s specific context, prioritizing cultural relevance, sustainability, and alignment with the needs of those most impacted.</p>
      <p>Schools can implement SafeBAE 360° in full or one component at a time. Either way, it rests on the belief that real prevention requires collective and sustained change.</p>
    </div>
    <div class="s3-intro__card">
      <h3>Let’s start the conversation.</h3>
      <p>We’d love to connect, whether you’re ready to explore full implementation or looking for a starting point. Some partners begin with a single assembly or awareness event, while others start a deeper collaboration right away. Wherever you begin, we can help you take actionable steps toward safer, more supportive school environments.</p>
      <div class="btns">{btn('Request a program', 'request-a-program.html', 'slate', arrow=True)}{btn('Browse all resources', 'resources.html', 'ghost')}{btn('Shop educational products', PODIA, 'ghost')}</div>
    </div>
  </div>
</section>'''

    picks = ''.join(f'<button type="button" data-pick="{i}" aria-pressed="{str(i==0).lower()}" style="--c:{c[2]}"><i></i>{i+1}. {esc(SHORT[i])}</button>' for i, c in enumerate(comps))
    panels = []
    for i, (t, h, fill, ink) in enumerate(comps):
        d = COMP_DATA[i]
        links = ''.join(f'<a class="arrow-link" href="{hh}">{esc(lbl)}</a>' for lbl, hh in d['links'])
        panels.append(f'''<div class="s3-comp{' on' if i==0 else ''}" id="component-{i+1}" style="--c:{fill}; --ci:{ink}">
        <div class="s3-comp__top"><span class="s3-comp__n">{i+1}</span><h3>{esc(t)}</h3></div>
        <p>{esc(d['text'])}</p>
        {checks([esc(x) for x in d['gets']], 's3-checks s3-checks--2')}
        <div class="s3-comp__links">{links}</div>
      </div>''')
    ring = f'''<section class="band band--paper" id="components">
  <div class="wrap">
    <div class="section-head"><div><h2>Six components that work together</h2>
      <p class="lede lede--full muted">SafeBAE 360° includes six core components that create lasting, schoolwide culture change, where prevention, support, and accountability are embedded in everyday life. Each component can also be implemented on its own, depending on a school’s needs.</p></div></div>
    <div class="s3-ringwrap">
      <div>{_SVG}<p class="s3-ringhint">Select a segment to see each component</p></div>
      <div>
        <div class="s3-pick" role="group" aria-label="Choose a component">{picks}</div>
        <div class="s3-comps" aria-live="polite">{''.join(panels)}</div>
      </div>
    </div>
  </div>
</section>'''

    steps = [
      ('Start the conversation', f'Book a 60-minute meeting with the SafeBAE team, or send a program request telling us what you’re looking for and how to follow up.'),
      ('Choose a starting point', 'Some partners begin with a single assembly or awareness event. Others start a deeper collaboration right away. Every component can be delivered on its own.'),
      ('Adapt it to your school', 'Each implementation is adapted to your school’s context, prioritizing cultural relevance, sustainability, and the needs of those most impacted.'),
      ('Build over time', 'Youth leaders help shape implementation as components are added, building toward the collective and sustained change that real prevention requires.'),
    ]
    steps_html = ''.join(f'<div class="step"><span class="step__n">{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(steps))
    how = f'''<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><h2>How schools adopt SafeBAE 360°</h2></div>{btn('Book a meeting', CAL, 'mint')}</div>
    <div class="steps s3-steps4">{steps_html}</div>
    <div class="s3-steps-note"><p><b style="color:#fff">Starting with an assembly?</b> SafeBAE assemblies and school events are always co-presented with youth leaders and tailored to be age-appropriate. They often become the starting place for longer-term collaboration.</p>{btn('Assemblies & pricing', 'request-a-program.html', 'ghost', 'sm', arrow=True)}</div>
  </div>
</section>'''

    roles = [
      ('leaders', 'District &amp; school', 'Leaders &amp; administrators', '066', 'SafeBAE staff and youth leaders in front of a full gym of students at a school assembly',
       'Strengthen policy, train staff and give students a lasting role in prevention',
       'Start with the piece your school needs most and add components as capacity grows. Pricing is on a sliding scale.',
       [('School Policy Reform Guide', 'A step-by-step resource for strengthening sexual misconduct policies beyond the federal minimum.', 'policy-reform-guide.html', ['Administrators', 'Districts']),
        ('Faculty & Staff Training', 'Trauma-informed professional development, in person or virtual.', 'professional-development.html', ['PD']),
        ('Healthy Relationship & Consent Curriculum', '15 lessons aligned with the National Health Education Standards.', 'consent-curriculum.html', ['NHES']),
        ('Talk through scope and pricing', 'Sliding scale pricing based on program scope, number of speakers and travel.', CAL, ['60 min'])]),
      ('counselors', 'Counselors &amp;', 'Title IX staff', 'img-2395', 'Two SafeBAE facilitators leading a discussion in front of a classroom whiteboard',
       'Give students safe ways to come forward and a path to accountability',
       'Students can document harm privately and report to your school on their terms. Students who have caused harm get structured education, while survivors keep the choice of how to proceed.',
       [('Accountability Training', 'A multi-lesson virtual program for students who have harmed another student.', 'accountability-training.html', ['Respondents']),
        ('Anonymous reporting with REES', 'Students document incidents privately and can report anonymously or by name.', '#rees', ['Partner schools']),
        ('Responding to disclosures', 'Staff training on trauma-informed responses to disclosures of harm.', 'professional-development.html', ['PD']),
        ('Vibe Check', 'A free, anonymous reflection tool for students worried they crossed a line.', 'vibe-check.html', ['Anonymous'])]),
      ('teachers', 'Health &amp;', 'Classroom teachers', '20240627-171417-646d14-4', 'Students raising their hands during a SafeBAE classroom session',
       'Teach consent and healthy relationships with ready-made lessons',
       'Teach the curriculum yourself, co-teach with Certified Peer Educators, or have the SafeBAE team deliver it.',
       [('Healthy Relationship & Consent Curriculum', '15 lessons of 45 to 60 minutes with slides, facilitator guides and knowledge checks.', 'consent-curriculum.html', ['15 lessons']),
        ('Films & teaching guides', 'Youth-made films, each with a free teaching guide for short, meaningful discussions.', 'library.html#guides', ['Free']),
        ('Peer educators as co-teachers', 'Certified Peer Educators co-facilitate curriculum sessions.', 'peer-educator.html', ['Youth-led']),
        ('Free prevention posters', 'For classrooms, counseling offices, hallways and wellness centers.', 'posters.html', ['Download'])]),
      ('students', 'For', 'Students', 'safebae-consent-summits', 'A group of SafeBAE youth leaders in SafeBAE shirts at a consent summit by the water',
       'Lead prevention at your school',
       'Youth leaders help shape implementation, lead presentations, co-facilitate curriculum sessions and organize campaigns through SafeBAE Clubs. Everything for students is free.',
       [('Certified Peer Educator Training', 'Free, self-paced, 16 online modules and an official certificate.', 'peer-educator.html', ['Free']),
        ('Start or join a SafeBAE club', 'Register a new chapter, affiliate a club you already run, or restart last year’s.', 'clubs.html', ['Clubs']),
        ('Reform your school’s policy', 'The student guide to advocating for safer, survivor-centered policies.', 'reform-policy.html', ['Student guide'])]),
    ]
    rtabs = ''.join(f'<button class="s3-roles__tab" role="tab" id="role-{k}" aria-controls="rolep-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{pre}</small><span>{lbl}</span></button>' for i, (k, pre, lbl, *_r) in enumerate(roles))
    rpanels = ''.join(f'''<div class="s3-roles__panel" role="tabpanel" id="rolep-{k}" aria-labelledby="role-{k}"{'' if i==0 else ' hidden'}>
      <div class="s3-roles__img">{img(im, alt)}</div>
      <div><h3>{esc(h)}</h3><p class="muted">{esc(p)}</p><div class="rows">{''.join(row(t, dd, u, m) for t, dd, u, m in rws)}</div></div></div>''' for i, (k, pre, lbl, im, alt, h, p, rws) in enumerate(roles))
    who = f'''<section class="band band--paper" id="who">
  <div class="wrap">
    <div class="section-head"><div><h2>Where each role starts</h2></div></div>
    <div data-tabs="s3-roles"><div class="s3-roles__tabs" role="tablist" aria-label="Choose your role">{rtabs}</div>{rpanels}</div>
  </div>
</section>'''

    st_students = ''.join(stat(*s) for s in STUDENT_STATS)
    st_teachers = stat(*TEACHER_STATS[0], cls='s3-stat--wide') + ''.join(stat(*s) for s in TEACHER_STATS[1:])
    ev = f'''<section class="band band--mint s3-ev" id="evidence">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Pilot data &middot; 2023&ndash;24 school year</p><h2>What the 360° pilot found</h2>
      <p class="lede lede--full">We believe prevention should always be youth-led and evidence-driven. {esc(PILOT_LINE)}</p></div></div>
    <div data-tabs="s3-pilot">
      <div class="s3-evtabs" role="tablist" aria-label="Pilot results"><button role="tab" id="pilot-students" aria-controls="pilotp-students" aria-selected="true" tabindex="0">Students</button><button role="tab" id="pilot-teachers" aria-controls="pilotp-teachers" aria-selected="false" tabindex="-1">Teachers</button></div>
      <div role="tabpanel" id="pilotp-students" aria-labelledby="pilot-students"><p style="font-weight:600;margin:0 0 14px">Students who took part in SafeBAE’s programs were more prepared to step in when they witnessed harmful or potentially harmful actions.</p><div class="s3-stats">{st_students}</div></div>
      <div role="tabpanel" id="pilotp-teachers" aria-labelledby="pilot-teachers" hidden><p style="font-weight:600;margin:0 0 14px">Teachers who took part in SafeBAE’s programs were more likely to believe that their school policies could protect students from violence and thoroughly respond if violence occurs.</p><div class="s3-stats">{st_teachers}</div></div>
    </div>
    <p class="s3-evsrc">Source: SafeBAE 360° Schools Pilot Data, 2023–24 school year. {a('Download the pilot data report (PDF)', PILOT_PDF, 'link')}</p>
    <div class="s3-evfoot">
      <div>{yt('BmLIDyPsQz4', 'Does Prevention Work? SafeBAE’s Data & Impact Report', label='Watch')}</div>
      <div>
        <div class="s3-voices">
          <blockquote class="s3-voice"><p>“I like the focus on empowering students and making them central to the work.”</p><cite>Pilot participant</cite></blockquote>
          <blockquote class="s3-voice"><p>“[SafeBAE] works collaboratively with students to promote healthier relationships and a positive dating culture in and out of school.”</p><cite>Teacher, pilot school</cite></blockquote>
        </div>
        <p style="margin:16px 0 0;font-weight:500">Our findings come from ongoing evaluations, youth-designed surveys, internal assessments, and published research, including a study in the <i>Journal of Child Sexual Abuse</i>.</p>
        <div class="btns" style="margin-top:16px">{btn('Download data report', PILOT_PDF, 'slate')}{btn('Data & impact', 'impact.html', 'ghost', arrow=True)}</div>
      </div>
    </div>
  </div>
</section>'''

    impact = f'''<section class="band band--logo s3-imp">
  <div class="wrap s3-impact">
    <figure class="s3-pq">
      <blockquote class="quote">I wanted to give you some uplifting news. I was talking with my intern from the school you visited and she informed me that the presentation that you did really affected the youth at the school. In fact, she has friends that are a couple, and they were in an unhealthy relationship and your presentation changed the way they now treat one another. She also said that she was able to look at herself and how she treated her partner and make changes as well. I wanted you to know that you really make a difference and thank you, once more, for touching the lives of our youth.</blockquote>
      <figcaption class="cite">Dawn M. Keys, Newport Prevention Coalition Coordinator</figcaption>
    </figure>
    <div class="s3-imp__vid">
      {yt('ur2b6V1Pipk', 'SafeBAE at Alliance Ted K. Tajima High School', label='Watch')}
      <p class="small">Araceli Martinez, Community Schools Coordinator at Alliance Ted K. Tajima High School, reflects on why she brings SafeBAE to her campus and what she’s seen students gain from it.</p>
    </div>
  </div>
</section>'''

    logos = [('rini-color-01cbb034', 'Rhode Island Nurses Institute Middle College'), ('chatgpt-image-dec-10-2025-08-34-32-am', 'Paul Cuffee School'),
             ('alliance-logo-color-vertical', 'Alliance College-Ready Public Schools'), ('walogolg-3', 'Worcester Academy'),
             ('header-logo-stacked-3', 'Central Catholic High School'), ('6716423ef4c1138196fb7101-phillips-exeter-academy-lion', 'Phillips Exeter Academy'),
             ('9e389524-a5f5-4c66-aee6-395723e59586', 'Flintridge Prep'), ('63750970-0a6d-4483-b1d7-351445fc2a67', 'Harvard-Westlake School')]
    partners = f'''<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Recent partner schools</h2></div>{btn('Partners & press', 'partners-press.html', 'ghost', arrow=True)}</div>
    <div class="s3-logos">{''.join(f'<div class="s3-logo">{img(n, nm + " logo")}<span aria-hidden="true">{esc(nm)}</span></div>' for n, nm in logos)}</div>
  </div>
</section>'''

    rees = f'''<section class="band band--slate" id="rees">
  <div class="wrap s3-rees">
    <div>
      <p class="eyebrow">Component 5 &middot; SafeBAE x REES</p>
      <h2>An anonymous reporting tool built with REES</h2>
      <p class="lede" style="color:rgba(255,255,255,.9)">A secure, private space where students can document incidents of harm or violence at their own pace. Schools can partner with SafeBAE and REES to implement it, creating a trusted, customized reporting system that works for their community.</p>
      <div class="s3-rees__feats">
        <div><b>Private documentation</b><p>Students create a secure, encrypted record of what happened, on their own time.</p></div>
        <div><b>Anonymous or by name</b><p>Students choose whether to report anonymously or by name, directly to their school.</p></div>
        <div><b>School-specific support</b><p>Students are connected with resources and support at their own school.</p></div>
      </div>
      <div class="btns">{btn('Become a partner school', 'request-a-program.html', 'mint', arrow=True)}{btn('Student access', REES_LOGIN, 'ghost')}</div>
    </div>
    <div class="s3-rees__logo">{img('logo-horiz-rgb', 'REES')}<p>Nothing is shared without the student’s consent.</p></div>
  </div>
</section>'''

    pod_ids = ['5PzGRtkgUIBtCjVqhgstq7', '7GItNGhw4HvpawqV461rO0', '3h2vVAyCO9q0bKyPhcASa3']
    pmap = {p[0]: p for p in PODCASTS}
    pods = ''.join(spotify(pid, pmap[pid][1], pmap[pid][2]) for pid in pod_ids)
    listen = f'''<section class="band band--mist band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Listen: SafeBAE on prevention in schools</h2></div>{btn('All podcasts', 'library.html#podcasts', 'slate', arrow=True)}</div>
    <div class="s3-pods">{pods}</div>
  </div>
</section>'''

    new = new_programs('Two new programs schools can add',
        'SafeBAE is adding two programs this school year: a free AI literacy training for students, and a sexual strangulation prevention program for schools. Either can be added alongside SafeBAE 360°.', plus=True)
    body = hero + ring + new + intro + how + who + impact + ev + rees + partners + vibe_band('360') + listen + cta(
        'Bring SafeBAE 360° to your school',
        'Start with an assembly, a single component or the full model. Wherever you begin, we can help you take actionable steps toward a safer, more supportive school.',
        'dsc01134', 'SafeBAE youth leaders in SafeBAE shirts', 'Created by and for young people',
        extra=btn('Shop educational products', PODIA, 'ghost', 'sm'))
    js = r'''<script>(function(){
  var w = document.querySelector('.s3-ringwrap'); if(!w) return;
  var ring = w.querySelector('.ring'), segs = w.querySelectorAll('.seg'), btns = w.querySelectorAll('[data-pick]'), panels = w.querySelectorAll('.s3-comp');
  var hover = window.matchMedia && matchMedia('(hover:hover)').matches;
  function pick(n){
    panels.forEach(function(p, i){ p.classList.toggle('on', i === n); p.setAttribute('aria-hidden', String(i !== n)); });
    segs.forEach(function(s){ s.classList.toggle('on', +s.getAttribute('data-seg') === n); s.setAttribute('aria-pressed', String(+s.getAttribute('data-seg') === n)); });
    btns.forEach(function(b){ b.setAttribute('aria-pressed', String(+b.getAttribute('data-pick') === n)); });
    ring.classList.add('has-active');
  }
  segs.forEach(function(s){ var n = +s.getAttribute('data-seg');
    s.addEventListener('click', function(){ pick(n); });
    s.addEventListener('keydown', function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); pick(n); } });
    s.addEventListener('mouseenter', function(){ if(hover) pick(n); });
  });
  btns.forEach(function(b){ b.addEventListener('click', function(){ pick(+b.getAttribute('data-pick')); }); });
  var m = /^#component-([1-6])$/.exec(location.hash); pick(m ? +m[1] - 1 : 0);
})();</script>'''
    page('360-schools.html', '360° Schools · SafeBAE',
         'SafeBAE 360 is a whole-school approach to preventing sexual and dating violence, with six components that put youth in the lead on lasting culture change.',
         body, active='schools', body_class='s3 s3-360', head_extra=f'<style>{CSS}{CSS_360}</style>', scripts=js)


def curriculum():
    tiles = []
    for key, ucls, name, rng, desc, lessons in UNITS:
        for n, t, rel in lessons:
            tiles.append(f'<a class="s3-tile {ucls}" href="#lessons" data-unit="{key}" data-lesson="{n}" style="--i:{n}" aria-label="Lesson {n}: {esc(t)}"><b>{n}</b><span>{esc(t)}</span></a>')
    legend = ''.join(f'<span class="{ucls}"><i></i>{esc(name)}</span>' for key, ucls, name, *_r in UNITS)
    hero = f'''<section class="s3-ch s3-hx">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-ch__grid">
    <div class="rise">
      {crumbs([('Home', 'index.html'), ('360° Schools', '360-schools.html'), ('Consent Curriculum', None)])}
      {badge(1)}
      <h1>Healthy Relationship &amp; <span class="mk">Consent</span> Curriculum</h1>
      <p class="lede">A flexible, trauma-informed curriculum of 15 interactive lessons aligned with the National Health Education Standards (NHES). Lessons explore consent, communication, boundaries, digital safety, survivor support, healing, and more.</p>
      <div class="s3-facts"><div><b>15</b><span>interactive lessons</span></div><div><b>45–60</b><span>minutes per lesson</span></div><div><b>NHES</b><span>standards aligned</span></div><div><b>2</b><span>languages: English &amp; Spanish</span></div></div>
      <div class="btns">{btn('See all 15 lessons', '#lessons', 'slate', arrow=True)}{btn('Get the curriculum', PODIA, 'ghost')}</div>
    </div>
    <div>
      <div class="s3-tiles">{''.join(tiles)}</div>
      <div class="s3-legend">{legend}</div>
    </div>
  </div>
</section>'''

    deliver = f'''<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>Three ways to deliver it</h2>
      <p class="lede lede--full muted">Developed with youth and expert collaborators, the curriculum also includes lessons on sexting and tech-facilitated abuse, dating after sexual assault, and accountability for those who’ve caused harm. Content is available in English and Spanish.</p></div></div>
    <div class="s3-who3">
      <div><small>Option</small><h3>Taught by your teachers</h3><p>Facilitators are encouraged to bring their own voice and teaching style, with a slide-by-slide facilitator guide to lead the conversation.</p><a class="arrow-link" href="#guide">Inside the facilitator guide</a></div>
      <div><small>Option</small><h3>Co-taught with peer educators</h3><p>Certified Peer Educators co-facilitate curriculum sessions alongside your teachers.</p><a class="arrow-link" href="peer-educator.html">Peer Educator Training</a></div>
      <div><small>Option</small><h3>Delivered by SafeBAE</h3><p>The SafeBAE team can deliver the lessons directly to your students.</p><a class="arrow-link" href="request-a-program.html">Request a program</a></div>
    </div>
  </div>
</section>'''

    utabs, upanels = [], []
    for i, (key, ucls, name, rng, desc, lessons) in enumerate(UNITS):
        utabs.append(f'<button role="tab" id="tab-{key}" aria-controls="unit-{key}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" class="{ucls}"><small><i></i>{esc(rng)}</small><span>{esc(name)}</span></button>')
        ls = ''.join(f'<div class="s3-lesson" id="lesson-{n}"><span class="s3-lesson__n">{n}</span><span class="s3-lesson__t">{esc(t)}</span>' +
                     (f'<a class="s3-lesson__rel" href="{rel[1]}">{esc(rel[0])}</a>' if rel else '') + '</div>' for n, t, rel in lessons)
        upanels.append(f'''<div class="s3-unit" role="tabpanel" id="unit-{key}" aria-labelledby="tab-{key}"{'' if i==0 else ' hidden'}>
        <div><p class="s3-unit__range">{esc(rng)} &middot; {len(lessons)} lessons</p><h3>{esc(name)}</h3><p>{esc(desc)}</p></div>
        <div class="s3-lessons">{ls}</div></div>''')
    lessons = f'''<section class="band band--slate" id="lessons">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">4 units &middot; 15 lessons</p><h2>The 15 lessons</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">The curriculum addresses core concepts in healthy relationship education and sexual violence prevention. Each lesson includes visual slides, interactive video content, and talking points to engage students in learning.</p></div></div>
    <div data-tabs="s3-units"><div class="s3-utabs" role="tablist" aria-label="Curriculum units">{''.join(utabs)}</div>{''.join(upanels)}</div>
  </div>
</section>'''

    incl = f'''<section class="band band--paper">
  <div class="wrap s3-incl">
    <div class="s3-incl__img">{img('img-9509-1', 'Students decorating “Yes means yes” consent posters with markers')}<span class="sticker sticker--r">Posters &amp; printables included</span></div>
    <div>
      <h2>A complete curriculum package</h2>
      <div class="s3-pack">
        <div><small>Teach</small><b>Full lesson plans and facilitation guides</b></div>
        <div><small>Show</small><b>Slide decks and multimedia materials</b></div>
        <div><small>Print</small><b>Posters and printable resources</b></div>
        <div><small>Check</small><b>Assessments and interactive activities</b></div>
      </div>
      <p class="muted">The package helps schools deliver engaging, developmentally appropriate prevention education with clarity, consistency, and care.</p>
      <div class="btns">{btn('Get the curriculum', PODIA, 'slate')}{btn('Ask about pricing', CAL, 'ghost')}</div>
    </div>
  </div>
</section>'''

    fac = f'''<section class="band band--logo" id="guide">
  <div class="wrap s3-fac">
    <div>
      <p class="eyebrow">Facilitator’s guide</p>
      <h2>How each lesson runs</h2>
      <p class="lede">SafeBAE’s curriculum is engaging, interactive, and youth-centered. SafeBAE worked with student leaders to develop each lesson, which includes visual slides with content and videos for student engagement, as well as a facilitator’s guide.</p>
      <p>Each lesson runs between 45 and 60 minutes, with learning objectives and knowledge checks included for students. Facilitators are encouraged to bring their voice and teaching style to each lesson, and may find the slide-by-slide facilitator guide helpful in leading the conversation.</p>
      <p>The curriculum covers important and sensitive topics, so SafeBAE encourages curiosity and questions.</p>
      <div class="s3-email"><span><b>Training and technical assistance</b><br><span class="small" style="color:var(--ink-soft)">We’re happy to help with any request by email.</span></span><span class="copy">{EMAIL}<button type="button" data-copy="{EMAIL}">Copy</button></span></div>
      <div style="margin-top:14px">{help_inline()}</div>
    </div>
    <div class="s3-anat">
      <div class="s3-anat__img">{img('img-3947', 'A SafeBAE lesson projected at the front of a classroom while students watch')}</div>
      <div class="s3-anat__body"><h3>Inside every lesson</h3>
        <ul><li class="k">45–60 minutes</li><li>Learning objectives</li><li>Visual slides</li><li>Video content</li><li>Talking points</li><li>Knowledge checks</li><li>Slide-by-slide facilitator guide</li></ul>
      </div>
    </div>
  </div>
</section>'''

    smaller = f'''<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><h2>More for your classroom</h2></div></div>
    <div class="s3-two s3-three">
      <a href="library.html#guides"><small>Starting smaller</small><h3>Free films and teaching guides</h3><p>Every SafeBAE film comes with a ready-to-teach guide for short, meaningful discussions.</p><span class="arrow-link">Browse the library</span></a>
      <a href="peer-educator.html"><small>Pair it with</small><h3>Certified Peer Educator Training</h3><p>Students complete a free, self-paced online certification and can then co-facilitate curriculum sessions with you.</p><span class="arrow-link">Peer Educator Training</span></a>
      <a href="ai-literacy.html" class="is-new"><small>New &middot; launches October 26&ndash;30, 2026</small><h3>SafeBAE AI Literacy Training</h3><p>Six free, self-paced modules for high school and college students, including AI and healthy relationships, fake images and sextortion. Educators can register for group access.</p><span class="arrow-link">About the training</span></a>
    </div>
  </div>
</section>'''

    body = hero + lessons + deliver + fac + incl + smaller + family(1) + cta(
        'Bring the curriculum to your school',
        'Purchase the curriculum online, or talk with us about delivery by teachers, peer educators or the SafeBAE team and about sliding scale pricing.',
        'p1002709', 'SafeBAE youth media team on a film set holding a clapperboard', 'Lessons built with student leaders',
        extra=btn('Get the curriculum online', PODIA, 'ghost', 'sm'))
    js = r'''<script>(function(){
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.s3-tile[data-lesson]').forEach(function(t){
    t.addEventListener('click', function(e){
      e.preventDefault();
      var tab = document.getElementById('tab-' + t.getAttribute('data-unit')); if(tab) tab.click();
      var li = document.getElementById('lesson-' + t.getAttribute('data-lesson')), sec = document.getElementById('lessons');
      if(sec) sec.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block: 'start'});
      document.querySelectorAll('.s3-lesson.is-hl').forEach(function(x){ x.classList.remove('is-hl'); });
      if(li){ void li.offsetWidth; li.classList.add('is-hl'); setTimeout(function(){ li.classList.remove('is-hl'); }, 2600); }
    });
  });
})();</script>'''
    page('consent-curriculum.html', 'Consent Curriculum · SafeBAE',
         'SafeBAE’s healthy relationship and consent curriculum: 15 lessons aligned with the National Health Education Standards, covering consent, sexting and accountability. Built with youth, available in English and Spanish.',
         body, active='schools', body_class='s3 s3-curr', head_extra=f'<style>{CSS}{HELPLINE_CSS}{CSS_CURR}</style>', scripts=js)


BARS_JS = r'''<script>(function(){ var b = document.querySelector('[data-bars]'); if(!b) return; if(!('IntersectionObserver' in window)){ b.classList.add('in'); return; } var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ b.classList.add('in'); io.disconnect(); } }); }, {threshold:.25}); io.observe(b); })();</script>'''

def pd():
    hero = f'''<section class="phero phero--logo phero--split s3-pdh"><span class="phero__wm" aria-hidden="true"></span><div class="wrap"><div>
      {crumbs([('Home', 'index.html'), ('360° Schools', '360-schools.html'), ('Faculty & Staff Training', None)])}
      {badge(2)}
      <h1>Professional development for <span class="mk">faculty &amp; staff</span></h1>
      <div class="s3-aud"><span>Teachers</span><span>Staff</span><span>Administrators</span></div>
      <p class="lede">Prevention is most effective when faculty and staff have the right tools and training. SafeBAE provides professional development for teachers, staff, and administrators that is trauma-informed, flexible, and tailored to your school’s needs.</p>
      <div class="btns">{btn('Request training', 'request-a-program.html', 'mint', arrow=True)}{btn('Book a meeting', CAL, 'ghost')}</div>
    </div><div class="phero__media">{img('img-2400', 'Students and adults seated in a circle during a SafeBAE session in a classroom', loading='eager')}<span class="sticker">In person or virtual</span></div></div></section>'''

    topics = [
      ('Trauma-informed responses to disclosures of harm', 'What to do when a student tells you', ('Survivor support', 'survivor-support.html'), 'var(--teal)'),
      ('Building a school culture of consent and accountability', 'Schoolwide', ('Consent Curriculum', 'consent-curriculum.html'), 'var(--mint)'),
      ('Supporting student survivors', 'Students', ('Title IX: rights at school', 'title-ix.html'), '#7dbbc1'),
      ('Understanding and advancing school policy reform to strengthen protections and reduce liability', 'Policy', ('Policy Reform Guide', 'policy-reform-guide.html'), 'var(--slate)'),
      ('Supporting youth leadership and engagement in prevention', 'Youth leadership', ('Peer Educator Training', 'peer-educator.html'), 'var(--logo-teal)'),
      ('Supporting marginalized students', 'Equity', ('Race, Rape Culture & Resistance', 'film-race-rape-culture-resistance.html'), 'var(--aqua)'),
    ]
    th = ''.join(f'<div class="s3-topic" style="--c:{c}"><small>{esc(k)}</small><h3>{esc(t)}</h3><a class="arrow-link" href="{h}">Related: {esc(l)}</a></div>' for t, k, (l, h), c in topics)
    tsec = f'''<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>What the trainings cover</h2>
      <p class="lede lede--full muted">Every training is trauma-informed and built around your school. Sessions draw on these focus areas.</p></div></div>
    <div class="s3-topics">{th}</div>
    <div style="margin-top:22px">{help_inline()}</div>
  </div>
</section>'''

    fmt = f'''<section class="band band--slate">
  <div class="wrap s3-fmt">
    <div class="s3-fmt__img">{img('img-2395', 'Two SafeBAE facilitators leading a session in front of a whiteboard')}</div>
    <div class="s3-fmt__card">
      <h2 style="font-size:clamp(1.7rem,3vw,2.5rem)">How trainings are delivered</h2>
      <p style="color:var(--ink-soft)">We adapt every training to the context of your school.</p>
      <div class="s3-modes"><div><b>In person</b><span>At your school</span></div><div><b>Virtual</b><span>Online sessions</span></div></div>
      <dl class="s3-spec" style="margin-top:16px">
        <div><dt>Audience</dt><dd>Teachers, staff and administrators</dd></div>
        <div><dt>Approach</dt><dd>Trauma-informed, flexible and tailored to your school’s unique needs</dd></div>
        <div><dt>Part of</dt><dd>SafeBAE 360° Schools, or on its own</dd></div>
      </dl>
    </div>
  </div>
</section>'''

    bars = ''.join(f'<div class="s3-bar" style="--v:{v[:-1]}"><p class="s3-bar__t">{esc(d[len("in teachers "):][0].upper() + d[len("in teachers "):][1:])}</p><div class="s3-bar__track"><i></i><b>{esc(v)}</b></div></div>' for v, k, d in TEACHER_STATS[:5])
    tstats = f'''<div class="s3-tgrid">
      <div class="s3-bars" data-bars><p class="s3-bars__cap">Increase among teachers after SafeBAE programming</p>{bars}</div>
      <div class="s3-tside">{stat(*TEACHER_STATS[5])}{stat(*TEACHER_STATS[6])}</div>
    </div>'''
    tev = f'''<section class="band band--mint s3-ev">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Pilot data &middot; 2023&ndash;24 school year</p><h2>What teachers reported</h2>
      <p class="lede lede--full">{esc(PILOT_LINE)} Teachers who took part in SafeBAE’s programs were more likely to believe that their school policies could protect students from violence and thoroughly respond if violence occurs.</p></div></div>
    {tstats}
    <div class="s3-tq">
      <blockquote class="s3-voice" style="margin:0;background:transparent;padding:0"><p class="s3-q">“[SafeBAE provides] information surrounding issues relevant to everyone, not just students.”</p><cite>Teacher, 360° pilot school</cite></blockquote>
      <div class="btns">{btn('Pilot data (PDF)', PILOT_PDF, 'slate')}{btn('All results', '360-schools.html#evidence', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>'''

    new = new_programs('Two new programs for your school', 'Educators can register for group access to the free SafeBAE AI Literacy Training, and SafeBAE’s Sexual Strangulation Prevention program for schools launches in November 2026.')
    body = hero + tsec + fmt + tev + new + family(2) + cta(
        'Request professional development for your school',
        'Tell us about your faculty and staff and what you need. We adapt every training to your school and can deliver it in person or virtually.',
        'safebae-8', 'SafeBAE youth leaders in SafeBAE shirts standing together by the water', 'Trauma-informed')
    page('professional-development.html', 'Faculty & Staff Training · SafeBAE',
         'Trauma-informed professional development for teachers, staff, and administrators, tailored to your school and built to support youth-led prevention.',
         body, active='schools', body_class='s3 s3-pd', head_extra=f'<style>{CSS}{HELPLINE_CSS}{CSS_PD}</style>', scripts=BARS_JS)


def policy():
    hero = f'''<section class="s3-ph s3-hx band--teal">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-ph__grid">
    <div class="rise">
      {crumbs([('Home', 'index.html'), ('360° Schools', '360-schools.html'), ('Policy Reform Guide', None)])}
      {badge(3)}
      <p class="eyebrow">For administrators, faculty and district leaders</p>
      <h1>School Sexual Misconduct <span class="mk">Policy Reform</span> Guide</h1>
      <p class="lede">Strong, trauma-informed policies are the foundation of a safe school community. SafeBAE’s guide is a step-by-step resource to help administrators, faculty, and district leaders strengthen their policies beyond the bare federal minimum.</p>
      <div class="btns">{btn('Get the guide', POLICY_PODIA, 'mint')}{btn('Student version', 'reform-policy.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="s3-covers">
      <figure class="s3-cover s3-cover--student">{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide for students, 2024 update', loading='eager')}<figcaption class="sticker sticker--aqua">For students</figcaption></figure>
      <figure class="s3-cover s3-cover--admin">{img('policy-guide-admin-cover', 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide for school administrators, 2024 update', loading='eager')}<figcaption class="sticker">For administrators</figcaption></figure>
    </div>
  </div>
</section>'''

    why = f'''<section class="band band--paper">
  <div class="wrap s3-why">
    <div>
      <h2>Federal Title IX rules keep shifting</h2>
      <p class="lede">Since 2020, shifting federal Title IX regulations have left schools caught in the middle of inconsistent rules, legal challenges, and unclear enforcement.</p>
      <p>Strengthening your school’s policies proactively protects students and safeguards your institution. It also shows leadership in creating safer, healthier learning environments.</p>
    </div>
    <div>
    <div class="tl">
      <div class="tl__item"><div class="tl__year">2020</div><div><h3>The 2020 rule</h3><p>Narrowed protections for survivors and restricted schools’ ability to respond effectively.</p></div></div>
      <div class="tl__item"><div class="tl__year">2024</div><div><h3>New guidelines</h3><p>Attempted to restore protections, but were quickly tied up in court.</p></div></div>
      <div class="tl__item"><div class="tl__year now">Now</div><div><h3>Back under the 2020 rule</h3><p>Most schools have been forced back under the restrictive 2020 rule, leaving students and districts vulnerable.</p></div></div>
    </div>
    <div class="s3-risk"><div><small>For students</small><b>Survivors face heightened risk of further harm.</b></div><div><small>For districts</small><b>Administrators face potential legal exposure without clear, stable standards to follow.</b></div></div>
    </div>
  </div>
</section>'''

    guide = f'''<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><h2>The guide, and hands-on support</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">Grounded in trauma-informed practice and survivor-centered values, the guide walks you through building policies that promote transparency, accountability, and safety for every student.</p></div></div>
    <div class="s3-gp">
      <div><small>Self-guided</small><h3>The Policy Reform Guide</h3>
        {checks(['A step-by-step guide to creating a comprehensive, trauma-informed policy', 'Built to take your policy beyond the bare federal minimum', 'Grounded in trauma-informed practice and survivor-centered values', 'Written for administrators, faculty and district leaders'])}
        <div class="s3-gp__foot"><div class="s3-gp__cover">{img('policy-guide-admin-cover', 'Cover of the Policy Reform Guide for school administrators')}</div><div class="btns">{btn('Get the guide', POLICY_PODIA, 'slate')}</div></div></div>
      <div><small>Component 4 of SafeBAE 360°</small><h3>School policy support</h3>
        <p style="color:rgba(255,255,255,.88)">Hands-on consultation helps schools audit and revise sexual misconduct and Title IX policies.</p>
        {checks(['Annotated audits', 'Student-centered model language', 'Communication templates', 'Rollout strategies'], 's3-checks s3-checks--2')}
        <p style="color:rgba(255,255,255,.75);font-size:.9rem">The goal is a policy that is:</p>
        <div class="s3-qual" style="margin-top:0"><span>Accessible</span><span>Compliant</span><span>Trusted</span><span>Trauma-informed</span></div>
        <div class="btns">{btn('Request policy support', 'request-a-program.html', 'mint', arrow=True)}</div></div>
    </div>
  </div>
</section>'''

    steps = [
      ('Read the guide', 'Work through the step-by-step guide with your administrators, faculty and district leaders.'),
      ('Audit your current policy', 'Review your sexual misconduct and Title IX policies against it. SafeBAE can provide an annotated audit.'),
      ('Revise with students in mind', 'Use student-centered model language. Students can use their own version of the guide to advocate alongside you.'),
      ('Communicate and roll out', 'Use communication templates and rollout strategies so the new policy is accessible and trusted.'),
    ]
    sh = ''.join(f'<div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in steps)
    use = f'''<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>Putting the guide to work</h2></div>{btn('Book a meeting', CAL, 'slate')}</div>
    <div class="s3-uses">{sh}</div>
    <div class="note" style="margin-top:20px;display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between"><p style="margin:0;flex:1 1 420px"><b>Train the people who carry it out.</b> SafeBAE’s faculty and staff training includes understanding and advancing school policy reform to strengthen protections and reduce liability.</p>{btn('Faculty & Staff Training', 'professional-development.html', 'ghost', 'sm', arrow=True)}</div>
  </div>
</section>'''

    stud = f'''<section class="band band--logo">
  <div class="wrap s3-stud">
    <div class="s3-stud__cover">{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', 'Cover of the Student Policy Reform Guide')}</div>
    <div>
      <p class="eyebrow">For students, parents and community stakeholders</p>
      <h2>The Student Policy Reform Guide</h2>
      <p class="lede">A step-by-step resource that helps students advocate for safer, trauma-informed, and survivor-centered policies in their district. Students, parents and community stakeholders can use it to push for clarity, accountability, and real protection in their schools.</p>
      <p>SafeBAE asks only that you register to receive the student guide and keep in touch about your progress.</p>
      <div class="btns">{btn('Get the student guide', 'reform-policy.html', 'mint', arrow=True)}{btn('Title IX: rights at school', 'title-ix.html', 'ghost')}</div>
    </div>
  </div>
</section>'''

    body = hero + why + guide + use + stud + family(3) + cta(
        'Get policy support for your district',
        'Start with the guide, or bring SafeBAE in for hands-on consultation: annotated audits, model language, communication templates and rollout strategies.',
        'img-3755', 'Students and an adult posing together in a school hallway', 'Student-centered policy',
        extra=btn('Get the guide', POLICY_PODIA, 'ghost', 'sm'))
    page('policy-reform-guide.html', 'Policy Reform Guide for Schools · SafeBAE',
         'A guide to reforming your school’s sexual misconduct policy with strong, trauma-informed protections as federal Title IX rules keep shifting.',
         body, active='schools', body_class='s3 s3-pol', head_extra=f'<style>{CSS}{CSS_POL}</style>')


def accountability():
    hero = f'''<section class="s3-ah s3-hx band--logo">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-ah__grid">
    <div class="rise">
      {crumbs([('Home', 'index.html'), ('360° Schools', '360-schools.html'), ('Accountability Training', None)])}
      {badge(5)}
      <p class="eyebrow">For students who have caused harm</p>
      <h1><span class="mk">Accountability</span> Training for Schools</h1>
      <p class="lede">A multi-lesson virtual program developed specifically for students who have harmed another student. It helps them reflect on intention versus outcome, identify harmful behaviors, and reduce the likelihood of reoffending.</p>
      <div class="btns">{btn('Learn more', ACC_PODIA, 'mint')}{btn('Talk with our team', CAL, 'ghost')}</div>
    </div>
    <div class="s3-ahv">
      <div class="s3-ahv__img">{img('us-duford-laptop-notebook', 'Overhead view of hands at a laptop, one writing in a notebook', loading='eager')}</div>
      <span class="sticker">Multi-lesson &middot; virtual</span>
      <figure class="s3-ahq">
        <blockquote class="s3-q">I want them to apologize, and I want them to not do this to anyone else.</blockquote>
        <cite>Two requests we hear from survivors, again and again</cite>
      </figure>
    </div>
  </div>
</section>'''

    why = f'''<section class="band band--paper">
  <div class="wrap s3-choice">
    <div>
      <h2>Survivors asked for more options</h2>
      <p class="lede">Historically, schools, universities, and courts across the country have had virtually no resources to address students accused of or found responsible for sexual assault. In most Title IX cases, the primary resolution has been suspension or expulsion.</p>
      <p>In our work with survivors, we often hear how traumatizing and difficult investigations can be, and how many survivors want alternatives. Some would like resolution options that focus on accountability and healing rather than only punishment.</p>
      <p>As part of our mission to provide resources for both prevention and response, we developed this training specifically for students who have harmed another student.</p>
    </div>
    <div class="s3-choice__card"><strong>Choice</strong><p>Survivors must be free to decide what path feels safest and most meaningful for them. Not all will choose these alternatives.</p></div>
  </div>
</section>'''

    topics = ['How to Respond If You’ve Been Accused', 'The Origins of Rape Culture', 'Sexual Assault, Harassment, and Rape – Defined', 'Consent',
              'Healthy Relationships', 'Male Youth & Sexual Violence', 'Myths, Facts & Statistics', 'Sexual Violence & Relationships in Media',
              'Online Safety & Sending Nudes', 'Healing After Sexual Violence', 'Dating Someone Who Has Experienced Sexual Violence', 'Bystander Intervention']
    th = ''.join(f'<div class="s3-atopic"><b>{esc(t)}</b><span>+ knowledge check</span></div>' for t in topics)
    covers = f'''<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><h2>What the training covers</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">Through a comprehensive, multi-lesson virtual program, participants are guided through these core topics. Each lesson is followed by a knowledge check to ensure understanding.</p></div></div>
    <div class="s3-atopics">{th}</div>
  </div>
</section>'''

    fit = f'''<section class="band band--paper">
  <div class="wrap s3-fit">
    <div>
      <h2>An alternative to discipline alone</h2>
      <p class="lede">The training is designed for use in school Title IX processes, in formal or informal resolutions, or in court settings. It is intended to support behavior change and reduce the likelihood of recidivism among respondents.</p>
      <p>The training is part of the sixth SafeBAE 360° component, educational resources to reduce recidivism, rooted in prevention, healing, and restorative justice rather than punishment. Together with Vibe Check, these resources give schools a trauma-informed, developmentally appropriate alternative to traditional disciplinary responses.</p>
      <div style="margin-top:20px">{help_inline()}</div>
    </div>
    <div>
      <dl class="s3-spec">
        <div><dt>Format</dt><dd>A multi-lesson virtual program</dd></div>
        <div><dt>For</dt><dd>Students who have harmed another student</dd></div>
        <div><dt>Checks</dt><dd>A knowledge check after every lesson</dd></div>
        <div><dt>Completion</dt><dd>Proof of completion is available upon request</dd></div>
        <div><dt>Languages</dt><dd>English and Spanish</dd></div>
        <div><dt>Access</dt><dd>Available for purchase through an annual unlimited-use license or a single-use license. A single-use purchase includes a one-hour, one-on-one consultation.</dd></div>
        <div><dt>Development</dt><dd>Created by experts in partnership with young survivors. As with all of our programs, we welcome feedback to continuously improve and expand inclusivity.</dd></div>
      </dl>
      <div class="btns" style="margin-top:20px">{btn('See licenses', ACC_PODIA, 'slate')}{btn('Ask a question', 'mailto:' + EMAIL, 'ghost')}</div>
    </div>
  </div>
</section>'''

    body = hero + why + covers + fit + vibe_band('acc') + family(5) + cta(
        'Bring Accountability Training to your school',
        'Talk with us about how the training fits your Title IX process, which license suits your school, and sliding scale pricing.',
        extra=btn('See licenses', ACC_PODIA, 'ghost', 'sm'))
    page('accountability-training.html', 'Accountability Training for Schools · SafeBAE',
         'SafeBAE’s accountability training helps schools respond to students who cause harm with survivor-centered options beyond suspension and expulsion.',
         body, active='schools', body_class='s3 s3-acc', head_extra=f'<style>{CSS}{HELPLINE_CSS}{CSS_ACC}</style>')


def build():
    p360()
    curriculum()
    pd()
    policy()
    accountability()

if __name__ == '__main__':
    build()
