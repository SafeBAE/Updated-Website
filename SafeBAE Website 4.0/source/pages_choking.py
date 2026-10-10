"""choking-hazard.html (v4): SafeBAE's page for the Choking Hazard campaign.
v4 job: give context and send people to chokinghazard.org. The campaign site holds the evidence, myth vs. fact,
media ratings, posters and the film; this page keeps the essentials (three facts, what is on the campaign site,
the signs that need medical care, Vibe Check, the schools program) and links out for everything else.
Facts carried from v3 (research_new_pages.md section A; citations checked against chokinghazard.org, 9 Oct 2026).
Safety yellow (#FFD600) is the campaign's own accent and is used only for the label, stickers and tape."""
from lib import *
import films_common as _fc
from films_common import vibe_band
VIBE_CSS = getattr(_fc, 'VIBE_CSS', '')

CH = 'https://chokinghazard.org/'
CH_LEARN = CH + 'learn-more/'
CH_RATINGS = CH + 'media-ratings/'
CH_RES = CH + 'resources/'
CH_DL = CH + 'resources/#downloads'
CH_FILM = CH + 'film/'
MAIL = 'info@safebae.org'

# geometric warning triangle (rounded), ink + inner mark
TRI = ('<svg class="ch-tri" viewBox="0 0 48 42" aria-hidden="true" focusable="false">'
       '<path class="o" d="M21.4 3.5a3 3 0 0 1 5.2 0l19 33a3 3 0 0 1-2.6 4.5H5a3 3 0 0 1-2.6-4.5z"/>'
       '<rect class="i" x="21.6" y="13" width="4.8" height="15" rx="2.4"/><circle class="i" cx="24" cy="34" r="2.8"/></svg>')


def label(variant='', extra=''):
    """The campaign's warning label, drawn in HTML. Scales with its container (container query units)."""
    v = f' ch-label--{variant}' if variant else ''
    return (f'<div class="ch-lb{extra}"><div class="ch-label{v}">'
            f'<span class="ch-label__w">{TRI}<b>Warning</b></span>'
            f'<span class="ch-label__m">Choking is a hazard</span>'
            f'<span class="ch-label__s">May cause serious injury or death</span>'
            f'<span class="ch-label__u">chokinghazard.org</span></div></div>')


def tape(cls=''):
    unit = ''.join(f'<span>{TRI}Choking is a hazard</span><span>{TRI}chokinghazard.org</span>' for _ in range(4))
    return f'<div class="ch-tape {cls}"><div class="ch-tape__track">{unit}{unit}</div></div>'


def cite(t):
    return f'<p class="ch-cite">{t}</p>'


CSS = r'''
body.ch{--hz:#FFD600; --hz-ink:#0d0d0d; --hz-fold:#e0bc00}
.ch-tri{width:1.15em; height:1.01em; flex:none; display:inline-block; vertical-align:-.12em}
.ch-tri .o{fill:currentColor} .ch-tri .i{fill:var(--tri-in, var(--hz))}
.ch-cite{font-family:var(--mono); font-size:.82rem; letter-spacing:.01em; line-height:1.45; margin:14px 0 0; color:var(--ink-soft)}
:is(.band--slate,.band--deep,.ch-hero) .ch-cite{color:rgba(209,254,255,.72)}
.ch-k{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; margin:0 0 8px; color:var(--logo-teal)}
:is(.band--slate,.band--deep) .ch-k{color:var(--mint)}
.ch .section-head .lede{max-width:none}

/* ---------- warning label ---------- */
.ch-lb{container-type:inline-size; width:100%}
.ch-label{aspect-ratio:1200/648; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.2cqi; padding:3cqi 5cqi; background:var(--hz); color:var(--hz-ink); border:1.15cqi solid var(--hz-ink); border-radius:3.2cqi; font-family:var(--display); text-transform:uppercase; text-align:center; line-height:1; box-shadow:0 0 0 1.4cqi #fff, 0 30px 50px -18px rgba(0,0,0,.55); position:relative}
.ch-label__w{display:flex; align-items:center; gap:3.2cqi; font-weight:900; font-stretch:112%; font-size:13.2cqi; letter-spacing:.01em; margin-bottom:2.4cqi}
.ch-label__w .ch-tri{width:15.5cqi; height:13.6cqi}
.ch-label__m{font-weight:900; font-stretch:106%; font-size:7.3cqi; letter-spacing:.005em; white-space:nowrap}
.ch-label__s{font-weight:900; font-stretch:100%; font-size:3.95cqi; letter-spacing:.02em; white-space:nowrap}
.ch-label__u{font-weight:800; font-stretch:100%; text-transform:none; font-size:3.5cqi; margin-top:3.4cqi}
.ch-label--aqua{background:var(--aqua); color:var(--slate); border-color:var(--slate); --tri-in:var(--aqua)}
.ch-label--aqua .ch-label__w .ch-tri{color:var(--coral)}
.ch-label--aqua .ch-tri .i{fill:#fff}

/* ---------- hero ---------- */
.ch-hero{--wm-o:.13; position:relative; overflow:hidden; color:#fff; background-color:var(--slate); background-image:var(--grain), linear-gradient(rgba(209,254,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(209,254,255,.05) 1px, transparent 1px); background-size:auto, 34px 34px, 34px 34px}
.ch-hero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(64px,7vw,104px)}
.ch-hero .wrap > *{min-width:0}
.ch-hero .crumbs{color:rgba(255,255,255,.78)}
.ch-hero .eyebrow{color:var(--mint)}
.ch-hero h1{font-size:clamp(2.45rem,5.3vw,5.2rem); font-stretch:120%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .32em}
.ch-open{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.2rem,1.9vw,1.62rem); line-height:1.2; color:var(--aqua); margin:0 0 .7em}
.ch-hero .lede{color:rgba(255,255,255,.88)}
.ch-hero .mk{background:none; color:var(--mint)}
.ch-cn{display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; margin:22px 0 0; font-size:.9rem; color:rgba(255,255,255,.84)}
.ch-cn b{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--slate); background:var(--aqua); padding:3px 8px; border-radius:4px; flex:none}
.ch-hero__art{position:relative; padding:18% 0 4% 0}
.ch-lb--aqua{position:absolute; width:56%; right:-1%; top:0; transform:rotate(7deg); --r:7deg; animation:ch-slap .7s .35s var(--ease) both}
.ch-lb--main{position:relative; width:100%; transform:rotate(-4deg); --r:-4deg; animation:ch-slap .7s .1s var(--ease) both}
.ch-lb--main .ch-label::after{content:""; position:absolute; right:-1.15cqi; bottom:-1.15cqi; width:8cqi; height:8cqi; border-bottom-right-radius:3.2cqi; background:linear-gradient(135deg, var(--hz-fold) 0 49%, var(--slate) 51%); box-shadow:-3px -3px 8px rgba(0,0,0,.18)}
@keyframes ch-slap{0%{opacity:0; transform:rotate(calc(var(--r) - 6deg)) scale(1.22)} 65%{opacity:1; transform:rotate(var(--r)) scale(.97)} 100%{opacity:1; transform:rotate(var(--r)) scale(1)}}

/* ---------- hazard tape ---------- */
.ch-tapes{position:relative; z-index:3; height:clamp(84px,9vw,130px); margin-block:calc(clamp(84px,9vw,130px) / -2); overflow:hidden; pointer-events:none}
.ch-tape{position:absolute; left:-12%; width:124%; top:50%; height:clamp(36px,3.6vw,50px); margin-top:calc(clamp(36px,3.6vw,50px) / -2); background:var(--hz); color:var(--hz-ink); border-block:clamp(4px,.45vw,6px) solid var(--hz-ink); overflow:hidden; display:flex; align-items:center; box-shadow:0 10px 24px -10px rgba(0,0,0,.5)}
.ch-tape--a{transform:rotate(-2.2deg)}
.ch-tape--b{transform:rotate(1.6deg); filter:brightness(.96)}
.ch-tape__track{display:flex; width:max-content; animation:ch-roll 2.8s var(--ease) both}
.ch-tape--b .ch-tape__track{animation-name:ch-roll-b; animation-duration:3.2s}
.ch-tape__track span{display:inline-flex; align-items:center; gap:.5em; padding-inline:1.1em; font-family:var(--display); font-weight:900; font-stretch:110%; text-transform:uppercase; font-size:clamp(.82rem,1.25vw,1.1rem); letter-spacing:.02em; white-space:nowrap}
.ch-tape__track span:nth-child(even){text-transform:uppercase}
@keyframes ch-roll{from{transform:translateX(-2%)} to{transform:translateX(-9%)}}
@keyframes ch-roll-b{from{transform:translateX(-12%)} to{transform:translateX(-5%)}}


/* ---------- context: three facts ---------- */
.ch-facts{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0; border-block:2px solid var(--slate)}
.ch-fact{padding:clamp(22px,2.6vw,34px) clamp(18px,2.4vw,32px); border-left:1px solid var(--line); display:flex; flex-direction:column; min-width:0}
.ch-fact:first-child{border-left:0; padding-left:0}
.ch-fact:last-child{padding-right:0}
.ch-fact b{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3rem,5.6vw,5rem); line-height:.9; letter-spacing:-.03em; color:var(--logo-teal); margin:0 0 14px}
.ch-fact b small{font-size:.42em; letter-spacing:0; margin-left:.08em}
.ch-fact p{margin:0; font-size:1.08rem; line-height:1.5; font-weight:500}
.ch-fact .ch-cite{margin-top:auto; padding-top:16px}
.ch-ages{display:flex; flex-wrap:wrap; gap:8px 10px; margin:0 0 var(--head-gap)}
.ch-ages span{display:inline-flex; align-items:baseline; gap:8px; padding:7px 12px; border-radius:10px; background:var(--mist); border:1px solid var(--line); font-size:.95rem; font-weight:600}
.ch-ages span b{font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:var(--logo-teal)}

/* ---------- the campaign site: four doors ---------- */
.ch-site{background-image:var(--grain), linear-gradient(rgba(209,254,255,.035) 1px, transparent 1px), linear-gradient(90deg, rgba(209,254,255,.035) 1px, transparent 1px); background-size:auto, 34px 34px, 34px 34px}
.ch-site .section-head{align-items:flex-end}
.ch-doors{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ch-door{position:relative; display:flex; flex-direction:column; min-width:0; background:var(--slate-deep); border:1px solid var(--line-dark); border-radius:var(--r-xl); overflow:hidden; text-decoration:none; color:#fff!important; transition:transform .25s var(--ease), border-color .25s, box-shadow .25s}
.ch-door::before{content:""; height:14px; flex:none; background:repeating-linear-gradient(-45deg, var(--hz) 0 10px, var(--hz-ink) 10px 20px)}
.ch-door__b{flex:1; display:flex; flex-direction:column; padding:var(--pad-card)}
.ch-door .ch-k{color:var(--mint); margin-bottom:12px}
.ch-door h3{font-size:clamp(1.3rem,1.8vw,1.55rem); font-stretch:110%; margin:0 0 .5em; color:#fff}
.ch-door p{margin:0 0 20px; font-size:1rem; line-height:1.55; color:rgba(255,255,255,.86)}
.ch-door__u{margin-top:auto; padding-top:14px; border-top:1px solid var(--line-dark); font-family:var(--display); font-stretch:106%; font-size:1rem; font-weight:800; color:var(--mint); display:flex; justify-content:space-between; gap:8px}
.ch-door:hover{transform:translateY(-4px); border-color:rgba(21,255,200,.6); box-shadow:0 30px 50px -30px rgba(0,0,0,.7)}
.ch-door:hover .ch-door__u{color:var(--mint)}
.ch-go{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:16px 32px; margin-top:var(--gap); padding:clamp(20px,2.4vw,28px) var(--pad-card); border-radius:var(--r-xl); background:rgba(209,254,255,.06); border:1px solid var(--line-dark)}
.ch-go p{margin:0; font-size:1.08rem; color:rgba(255,255,255,.9); flex:1 1 380px}

/* ---------- if it already happened ---------- */
.ch-er .section-head .lede{color:var(--slate)}
.ch-er__g{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch}
.ch-er__g > *{min-width:0}
.ch-er__side{display:grid; grid-template-rows:minmax(0,1fr) auto; gap:var(--gap)}
.ch-ercard{position:relative; background:#fff; color:var(--slate); border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column; box-shadow:var(--shadow-soft)}
.ch-ercard__tape{height:16px; flex:none; background:repeating-linear-gradient(-45deg, var(--hz) 0 12px, var(--hz-ink) 12px 24px)}
.ch-ercard__b{flex:1; display:flex; flex-direction:column; padding:var(--pad-card)}
.ch-ercard h3{font-size:clamp(1.5rem,2.4vw,2rem); font-stretch:114%; font-weight:900; text-transform:uppercase; line-height:1; margin:0 0 .3em}
.ch-ercard .sub{font-weight:700; font-size:1.06rem; color:var(--logo-teal); margin:0 0 16px}
.ch-erlist{flex:1; list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:0 28px}
.ch-erlist li{position:relative; display:flex; align-items:center; margin:0; padding:11px 0 11px 34px; border-top:1.5px solid var(--line); font-size:1.04rem; line-height:1.38; font-weight:600}
.ch-erlist li:first-child{grid-column:1/-1}
.ch-erlist li::before{content:""; position:absolute; left:2px; top:50%; margin-top:-9px; width:20px; height:18px; background:var(--teal); clip-path:polygon(50% 0, 100% 100%, 0 100%)}
.ch-911{display:flex; flex-direction:column; background:var(--coral); color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card)}
.ch-911 h3{font-family:var(--display); font-size:clamp(2.2rem,3.6vw,3.2rem); font-stretch:122%; font-weight:900; text-transform:uppercase; margin:0 0 .12em; line-height:.95}
.ch-911 p{margin:0 0 8px; font-weight:800; font-size:1.08rem}
.ch-911 ul{list-style:none; margin:0; padding:0; font-weight:600; font-size:1rem; line-height:1.36}
.ch-911 li{position:relative; margin:0; padding:6px 0 6px 20px; border-top:1.5px solid rgba(29,65,78,.22)}
.ch-911 li::before{content:""; position:absolute; left:2px; top:.9em; width:8px; height:8px; border-radius:50%; background:var(--slate)}
.ch-say{container-type:inline-size; background:var(--slate); background-image:var(--grain); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card)}
.ch-say .ch-k{color:var(--mint); margin-bottom:10px}
.ch-say__q{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(1.6rem,11cqi,2.5rem); line-height:1; color:var(--mint); margin:0 0 .3em; text-transform:uppercase}
.ch-say p:not([class]){color:rgba(255,255,255,.9); font-size:1rem; margin:0}
.ch-er__foot{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:16px 32px; align-items:center; margin-top:var(--gap); padding-top:var(--gap); border-top:1px solid var(--line)}
.ch-er__foot p{margin:0}
.ch-er__foot .ch-u18{font-size:1rem; line-height:1.55}
.ch-er__foot .ch-cite{margin-top:8px}

/* ---------- schools ---------- */
.ch-sch{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:20px 40px; align-items:center}
.ch-sch h2{margin:0 0 .25em}
.ch-sch p:not(.eyebrow){margin:0; font-size:var(--fs-lede); font-weight:500}

@media (max-width:1100px){ .ch-doors{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width:960px){ .ch-er__g{grid-template-columns:minmax(0,1fr)} .ch-er__side{grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:none} }
@media (max-width:860px){
  .ch-hero > .wrap{grid-template-columns:minmax(0,1fr)}
  .ch-hero__art{order:-1; max-width:460px; padding-top:12%}
  .ch-facts{grid-template-columns:minmax(0,1fr)}
  .ch-fact{border-left:0; border-top:1px solid var(--line); padding-inline:0}
  .ch-fact:first-child{border-top:0}
  .ch-er__foot{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:760px){ .ch-erlist{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto} .ch-sch{grid-template-columns:minmax(0,1fr)} }
@media (max-width:620px){ .ch-doors,.ch-er__side{grid-template-columns:minmax(0,1fr)} }
@media (prefers-reduced-motion:reduce){ .ch-lb--main,.ch-lb--aqua{animation:none} }
'''


# ---------------------------------------------------------------- content
FACTS = [
  ('15', '', 'is the average age students first heard about choking during sex.', 'Herbenick et al., 2025'),
  ('11', 'lb', 'of force can close the carotid arteries, which carry blood to the brain. Opening a can takes about 20.', 'Armstrong &amp; Strack, 2016'),
  ('5–10', 's', 'after the carotid arteries close, a person can pass out. Someone who is unconscious can’t agree to anything.', 'Rossen, Kabat &amp; Anderson, 1943'),
]
AGES = [('14–17', 'sexually experienced girls', '11.9%'), ('18–24', 'women', '31.9%'), ('25–29', 'women', '40.6%')]

DOORS = [
  ('Learn more', 'The evidence', 'How common choking is, what it does to the brain and body, myth vs. fact, and the research behind each answer.', CH_LEARN, 'Read the evidence'),
  ('Media ratings', 'Rated CH, rated BAE', 'How TV, film, stand-up, songs and bestselling books show choking, and which ones show the harm.', CH_RATINGS, 'See the ratings'),
  ('Free downloads', 'Posters and the sticker', 'Warning posters and the sticker in yellow or aqua, to download, print and put up where young people will see them.', CH_DL, 'Download them'),
  ('Short film', 'One boy’s evening at his computer', 'A screenlife short film from SafeBAE, in production, told through the four videos he watches.', CH_FILM, 'About the film'),
]

ER_SIGNS = [
  'You passed out, even briefly, or can’t remember part of what happened',
  'Your breathing has changed',
  'Swallowing hurts or is difficult',
  'Your voice is hoarse, raspy or deeper, or it’s hard to speak',
  'Your neck hurts or is tender, or there’s a mark or bruise on it',
  'Your vision or hearing has changed, or your ears are ringing',
  'You have a headache, or feel dizzy or lightheaded',
  'There are small red spots in your eyes or on your face',
  'You lost control of your bladder or bowels',
]
CALL_911 = ['is unconscious', 'has trouble breathing', 'has a swelling neck', 'seems confused', 'has weakness or numbness on one side', 'has a seizure', 'shows signs of a stroke: a drooping face, a weak arm, slurred speech']


def build():
    hero = f'''
<section class="ch-hero" aria-labelledby="ch-h1">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Choking Hazard</span></nav>
      <p class="eyebrow">A SafeBAE campaign &middot; chokinghazard.org</p>
      <h1 id="ch-h1">There’s no <span class="mk">safe way</span> to choke someone.</h1>
      <p class="ch-open">Prevention has to start early, before the behavior does.</p>
      <p class="lede">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” By college, many young people have already heard about choking or encountered it in sexual contexts. Waiting until after high school to talk about the impact and harm of sexual strangulation is too late.</p>
      <div class="btns">{btn('Go to chokinghazard.org', CH, 'mint')}{btn('If it already happened', '#er', 'ghost', arrow=True)}</div>
      <p class="ch-cn"><b>Content note</b><span>Sexual strangulation, injury and death. Press Esc twice to leave quickly.</span></p>
    </div>
    <div class="ch-hero__art" role="img" aria-label="The Choking Hazard warning label: Warning. Choking is a hazard. May cause serious injury or death. chokinghazard.org">
      {label('aqua', ' ch-lb--aqua')}
      {label('', ' ch-lb--main')}
    </div>
  </div>
</section>
<div class="ch-tapes" aria-hidden="true">{tape('ch-tape--a')}{tape('ch-tape--b')}</div>'''

    facts = ''.join(f'<div class="ch-fact"><b>{n}{f"<small>{u}</small>" if u else ""}</b><p>{t}</p>{cite(c)}</div>' for n, u, t, c in FACTS)
    ages = ''.join(f'<span><b>{v}</b>ages {a}, {g}</span>' for a, g, v in AGES)
    context = f'''
<section class="band band--paper" id="how-common">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Why it matters</p><h2>It starts before college.</h2>
      <p class="lede lede--full">In a 2022 national U.S. survey, 11.9% of sexually experienced girls aged 14 to 17 said a partner had choked them. Among women aged 18 to 24 it was 31.9%, and among women aged 25 to 29, 40.6%.</p></div></div>
    <div class="ch-facts">{facts}</div>
  </div>
</section>'''

    doors = ''.join(f'<a class="ch-door" href="{h}" target="_blank" rel="noopener"><span class="ch-door__b"><span class="ch-k">{k}</span><h3>{t}</h3><p>{d}</p><span class="ch-door__u"><span>{p}</span><span aria-hidden="true">&#8599;</span></span></span></a>' for k, t, d, h, p in DOORS)
    site = f'''
<section class="band band--slate ch-site" id="campaign">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">chokinghazard.org</p><h2>Go deeper on the campaign site</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">It gives young people, parents and educators the evidence, myth vs. fact, the signs that need medical care, and free warning posters.</p></div></div>
    <div class="ch-doors">{doors}</div>
    <div class="ch-go"><p>Every fact on the campaign site comes with its source.</p>{btn('Go to chokinghazard.org', CH, 'mint')}</div>
  </div>
</section>'''

    er = f'''
<section class="band band--mist ch-er" id="er">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">If it has already happened</p><h2>Get medical help. Say what happened.</h2>
      <p class="lede lede--full">Some injuries show up later. Swelling in the throat can develop hours afterward, and a stroke from a torn artery can happen days or weeks later.</p></div></div>
    <div class="ch-er__g">
      <div class="ch-ercard"><span class="ch-ercard__tape" aria-hidden="true"></span><div class="ch-ercard__b">
        <h3>Go to an emergency room today if:</h3>
        <p class="sub">Even with no marks, and even if you agreed to it.</p>
        <ul class="ch-erlist">{''.join(f'<li>{esc(s)}</li>' for s in ER_SIGNS)}</ul>
      </div></div>
      <div class="ch-er__side">
        <div class="ch-911"><h3>Call 911</h3><p>if someone:</p><ul>{''.join(f'<li>{esc(s)}</li>' for s in CALL_911)}</ul></div>
        <div class="ch-say"><p class="ch-k">At the front desk, say</p><p class="ch-say__q">“I was strangled.”</p><p>Not only “my throat hurts.” The word tells staff which injuries to check for.</p></div>
      </div>
    </div>
    <div class="ch-er__foot">
      <div><p class="ch-u18"><b>If you’re under 18,</b> you can still get medical care. Staff may be required to report abuse of a minor, and you can ask what they would report before you share more. If symptoms start or get worse later, go back, even if you were already seen.</p>
        {cite('Training Institute on Strangulation Prevention medical recommendations (Smock, Green &amp; Sturgeon, rev. 2022). This is not medical advice.')}</div>
      <div class="btns">{btn('What to expect at the ER', CH_RES + '#er', 'slate')}<button class="btn btn--coral" type="button" data-open-help>Talk to someone now</button></div>
    </div>
  </div>
</section>'''

    vibe = vibe_band('If you strangled someone without their consent, pressured them, or went further than they agreed to, Vibe Check can help you reflect on what happened and what taking responsibility could look like.',
                     heading='Worried you hurt someone?')

    schools = f'''
<section class="band band--aqua band--tight" id="schools">
  <div class="wrap ch-sch">
    <div><p class="eyebrow">For schools &middot; launches November 2026</p><h2>Sexual Strangulation Prevention</h2>
      <p>SafeBAE’s new program for schools on sexual strangulation, which young people call “choking,” launches in November 2026.</p></div>
    <div class="btns">{btn('Request a program', 'request-a-program.html#start', 'slate', arrow=True)}</div>
  </div>
</section>'''

    body = hero + context + site + er + vibe + schools
    page('choking-hazard.html', 'Choking Hazard · SafeBAE',
         'Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” There’s no safe way to choke someone. Three facts, the signs that need medical care, and where to find the evidence and free posters on chokinghazard.org.',
         body, active='resources', body_class='ch', head_extra=f'<style>{VIBE_CSS}{CSS}</style>')


if __name__ == '__main__':
    build()
