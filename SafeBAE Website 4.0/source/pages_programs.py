"""Request a Program tab: request-a-program.html (the hub: every program a school can
request, pricing and the request form) and assemblies.html (the Assemblies program).
Every fact comes from the live safebae.org Request a Program and 360° Schools pages and
from what the rebuilt program pages already state."""
from lib import *
from pages_home import FILMS, FILM_STRIP_CSS, film_font_link, ring_svg
import math

CALENDLY = CAL_MEET
EMAIL = 'info@safebae.org'

_RING, RCOMPS = ring_svg()   # (title, href, fill, ink) for the six 360° components
RING_HREF = ['peer-educator.html', 'consent-curriculum.html', 'professional-development.html', 'policy-reform-guide.html',
             '360-schools.html#rees', 'accountability-training.html']


# ------------------------------------------------------------------ shared bits
def crumbs(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in items) + '</nav>'


def _seg(i, cx, cy, R, r, gap):
    a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
    p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
    x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'


def mini_ring(cls='pg-mring', inner=22):
    segs = ''.join(f'<path d="{_seg(i, 50, 50, 49, inner, 4)}" fill="{c[2]}"/>' for i, c in enumerate(RCOMPS))
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{segs}</svg>'


def ring_links():
    """The 360° ring with every segment as a link to its program."""
    svg = _RING
    for i, (t, h, fill, ink) in enumerate(RCOMPS):
        svg = svg.replace(f'<g class="seg" data-seg="{i}" tabindex="0" role="button" aria-label="{esc(t)}">',
                          f'<a class="seg" data-seg="{i}" href="{RING_HREF[i]}" aria-label="Component {i+1}: {esc(t)}">')
    svg = svg.replace('</text></g>', '</text></a>')
    return svg.replace('aria-label="SafeBAE 360 components"', 'role="group" aria-label="The six components of SafeBAE 360° Schools"')


def meeting_embed():
    """Calendly: site.js swaps in the iframe on a live site; anywhere else this booking card shows."""
    return (f'<div class="embed" data-embed="{CALENDLY}?hide_gdpr_banner=1" data-h="760" data-title="Book a meeting with SafeBAE">'
            '<div class="embed__fallback pg-ticket"><div class="pg-ticket__tile" aria-hidden="true"><span>Meeting</span><b>60</b><i>minutes</i></div>'
            f'<div class="pg-ticket__txt"><p class="pg-ticket__t">A 60-minute meeting with the SafeBAE team</p><p>Pick a time that works for you on our Calendly page.</p>{btn("Book a meeting", CALENDLY, "slate")}</div></div></div>')


def static_form(fid, subject):
    return f'''<form class="form pg-form" data-static data-mailto="{EMAIL}" data-subject="{esc(subject)}" aria-label="Request a program">
  <div class="pg-form__row">
    <div class="field"><label for="{fid}-name">Name</label><input id="{fid}-name" name="Name" autocomplete="name" required></div>
    <div class="field"><label for="{fid}-org">School or organization</label><input id="{fid}-org" name="School or organization" autocomplete="organization" required></div>
  </div>
  <div class="pg-form__row">
    <div class="field"><label for="{fid}-email">Email address</label><input id="{fid}-email" name="Email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="{fid}-phone">Cell phone</label><input id="{fid}-phone" name="Cell phone" type="tel" autocomplete="tel" required></div>
  </div>
  <div class="field"><label for="{fid}-msg">What are you hoping to book or learn more about?</label><textarea id="{fid}-msg" name="Request" placeholder="Share what you’re hoping to book or learn more about…"></textarea></div>
  <div class="btns"><button class="btn btn--slate" type="submit">Submit request</button><span class="form__note">Or email {a(EMAIL, 'mailto:' + EMAIL, 'link')}</span></div>
  <p class="form__done" role="status">Thank you. Your email app should open with your request ready to send. If it doesn’t, write to {EMAIL}.</p>
</form>'''


# Every program a school can request. who = who it is for; text = what the site already says about it.
PROGRAMS = [
    dict(key='assemblies', name='Assemblies', short='Assemblies', who='For schools taking a first step', href='assemblies.html', go='About assemblies',
         text='One-time assemblies and awareness events, always co-presented with youth leaders and tailored to be age-appropriate, relevant, and impactful.'),
    dict(key='curriculum', name='Consent Curriculum', short='Consent Curriculum', who='For students and their teachers', href='consent-curriculum.html', go='See the 15 lessons',
         text='A trauma-informed curriculum of 15 lessons aligned with the National Health Education Standards, available in English and Spanish.'),
    dict(key='pd', name='Faculty & Staff Training', short='Faculty & Staff Training', who='For teachers, staff and administrators', href='professional-development.html', go='About the training',
         text='Professional development on trauma-informed response, supporting marginalized students, and building a school culture of consent and accountability.'),
    dict(key='policy', name='School Policy Support', short='School Policy Support', who='For administrators and district leaders', href='policy-reform-guide.html', go='Policy Reform Guide',
         text='Hands-on consultation to audit and revise sexual misconduct and Title IX policies, alongside SafeBAE’s step-by-step Policy Reform Guide.'),
    dict(key='accountability', name='Accountability Training', short='Accountability Training', who='For students who have caused harm', href='accountability-training.html', go='About the training',
         text='A multi-lesson virtual program that helps students reflect on intention versus outcome, identify harmful behaviors, and reduce the likelihood of reoffending.'),
    dict(key='peer', name='Peer Educator Training', short='Peer Educator Training', who='For student leaders', href='peer-educator.html', go='Peer Educator Training',
         text='Students complete a self-paced, online certification to become Peer Educators, then lead presentations, co-facilitate curriculum sessions and organize campaigns.'),
    dict(key='rees', name='Anonymous Reporting Tool', short='Anonymous Reporting Tool', who='For students at partner schools', href='360-schools.html#rees', go='SafeBAE x REES',
         text='A secure, private space where students can document incidents of harm at their own pace and report to their school anonymously or by name.'),
    dict(key='ai', name='SafeBAE AI Literacy Training', short='AI Literacy Training', who='For students 13 and older', href='ai-literacy.html', go='About the training', new=True,
         text='Six free, self-paced modules, including AI and healthy relationships, fake images and sextortion. Launches during U.S. Media Literacy Week, October 26–30, 2026.'),
    dict(key='ssp', name='Sexual Strangulation Prevention', short='Sexual Strangulation Prevention', who='For schools', href='choking-hazard.html#schools', go='For schools', new=True,
         text='SafeBAE’s new program for schools on sexual strangulation, which young people call “choking.” It launches in November 2026.'),
]


def prog_card(p):
    new = p.get('new')
    flag = '<span class="pg-flag">New</span>' if new else ''
    return (f'<a class="pg-card{" is-new" if new else ""}" href="{p["href"]}">'
            f'<span class="pg-card__who"><span>{esc(p["who"])}</span>{flag}</span>'
            f'<h3>{esc(p["name"])}</h3><p>{esc(p["text"])}</p>'
            f'<span class="pg-card__go"><span>{esc(p["go"])}</span><i aria-hidden="true">&rarr;</i></span></a>')


def prog_tile(p):
    new = p.get('new')
    return (f'<a class="pg-tile{" is-new" if new else ""}" href="{p["href"]}"><small>{"New &middot; " if new else ""}{esc(p["who"])}</small>'
            f'<b>{esc(p["short"])}</b><i aria-hidden="true">&rarr;</i></a>')


def leaders(band='band--paper'):
    """School-leader testimonial: the Araceli Martinez video and the Dawn M. Keys quote. Same on both pages."""
    return f'''<section class="band {band} pg-leaders" id="school-leaders">
  <div class="wrap">
    <div class="section-head"><div><h2>What school leaders say about SafeBAE</h2>
      <p class="lede lede--full">Hear from SafeBAE school partner Araceli Martinez, Community Schools Coordinator at Alliance Ted K. Tajima High School, as she reflects on why she brings SafeBAE to her campus and what she’s seen students gain from it.</p></div></div>
    <div class="pg-voices">
      {yt('ur2b6V1Pipk', 'A school leader’s perspective', label='Araceli Martinez')}
      <figure class="pg-quote"><blockquote>“…I was talking with my intern from the school you visited and she informed me that the presentation that you did really affected the youth at the school. In fact, she has friends that are a couple, and they were in an unhealthy relationship and your presentation changed the way they now treat one another. She also said that she was able to look at herself and how she treated her partner and make changes as well.”</blockquote><figcaption>Dawn M. Keys, Newport Prevention Coalition Coordinator</figcaption></figure>
    </div>
  </div>
</section>'''


FACTORS = ['Program scope', 'Number of speakers', 'Travel requirements']


def factors(cls=''):
    return (f'<div class="pg-factors {cls}"><p class="pg-factors__k">We consider factors like</p><ul>'
            + ''.join(f'<li>{esc(x)}</li>' for x in FACTORS) + '</ul></div>')


TABGO_JS = r'''<script>(function(){
  document.querySelectorAll('[data-tab-go]').forEach(function(l){ l.addEventListener('click', function(e){
    var t = document.getElementById(l.getAttribute('data-tab-go')); if(!t) return;
    e.preventDefault(); t.click(); var box = t.closest('[data-tabs]') || t; box.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block:'start'});
    try{ history.replaceState(null, '', '#' + t.id.replace(/^tab-/, '')); }catch(err){}
  }); });
})();</script>'''

# ------------------------------------------------------------------ CSS
PG_CSS = '''
/* ---------- shared: Request a Program tab ---------- */
.pg main .eyebrow{color:var(--logo-teal)}
.pg main :where(.band--slate,.band--deep,.band--logo,.phero) .eyebrow{color:var(--mint)}
.pg main .band--mint .eyebrow{color:var(--slate)}
.pg main :is(.band--slate,.band--deep,.band--logo) > .wrap > .section-head .lede{color:rgba(255,255,255,.9)}
.pg main section[id]{scroll-margin-top:76px}
.pg .section-head .lede{max-width:none}

/* program cards: label, name, two lines, link. Rows line up across the grid. */
.pg-menu{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.pg-card{display:grid; grid-template-rows:auto auto 1fr auto; row-gap:10px; padding:var(--pad-card); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); color:var(--slate); text-decoration:none; min-width:0; transition:transform .22s var(--ease), box-shadow .22s var(--ease)}
@supports (grid-template-rows:subgrid){ .pg-card{grid-row:span 4; grid-template-rows:subgrid} }
.pg-card__who{display:flex; align-items:flex-start; justify-content:space-between; gap:10px; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; line-height:1.45; color:var(--logo-teal)}
.pg-flag{flex:none; background:var(--slate); color:var(--mint); padding:1px 8px; border-radius:5px; letter-spacing:.1em}
.pg-card h3{margin:0; font-size:clamp(1.3rem,1.8vw,1.5rem); line-height:1.1; color:var(--logo-teal)}
.pg-card p{margin:0; color:var(--ink-soft); font-size:.97rem; line-height:1.5}
.pg-card__go{display:flex; align-items:center; justify-content:space-between; gap:12px; margin-top:8px; padding-top:14px; border-top:1px solid var(--line); font-weight:700; font-size:.95rem; color:var(--logo-teal)}
.pg-card__go i,.pg-tile i{flex:none; width:36px; height:36px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s var(--ease)}
.pg-card:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.pg-card:hover .pg-card__go i,.pg-tile:hover i{background:var(--mint); transform:translateX(3px)}
.pg-card.is-new{background:var(--mint); border-color:var(--mint)}
.pg-card.is-new .pg-card__who,.pg-card.is-new h3,.pg-card.is-new p,.pg-card.is-new .pg-card__go{color:var(--slate)}
.pg-card.is-new .pg-card__go{border-top-color:rgba(29,65,78,.28)}
.pg-card.is-new .pg-card__go i,.pg-tile.is-new i{background:var(--slate); color:var(--mint)}
.pg-card.is-new:hover .pg-card__go i,.pg-tile.is-new:hover i{background:#fff; color:var(--slate)}
@media (max-width:900px){
  .pg-menu{grid-template-columns:1fr; gap:12px}
  .pg-card{grid-row:auto; grid-template-rows:auto; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); column-gap:clamp(18px,3vw,32px); grid-template-areas:"who text" "name text" "go go"; align-items:start}
  .pg-card__who{grid-area:who} .pg-card h3{grid-area:name} .pg-card p{grid-area:text} .pg-card__go{grid-area:go}
}
@media (max-width:620px){ .pg-card{grid-template-columns:1fr; grid-template-areas:"who" "name" "text" "go"} }

/* compact program tiles */
.pg-tile{display:grid; grid-template-columns:minmax(0,1fr) auto; grid-template-rows:auto 1fr; gap:8px 12px; align-items:end; min-height:124px; padding:16px 16px 14px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line); color:var(--slate); text-decoration:none; min-width:0; transition:transform .2s var(--ease), box-shadow .2s var(--ease), background .2s}
.pg-tile small{grid-column:1/-1; align-self:start; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; line-height:1.4; color:var(--logo-teal)}
.pg-tile b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.2rem; line-height:1.12; color:var(--logo-teal)}
.pg-tile:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); background:#fff}
.pg-tile.is-new{background:var(--mint); border-color:var(--mint)}
.pg-tile.is-new small,.pg-tile.is-new b{color:var(--slate)}
.pg-tile.is-new:hover{background:var(--mint)}

/* the 360 pill (same mark as the program pages) */
.pg-badge{display:flex; width:max-content; max-width:100%; align-items:center; gap:10px; background:#fff; border:1px solid var(--line); border-radius:999px; padding:4px 14px 4px 4px; text-decoration:none; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; font-weight:500; margin:0 0 18px; box-shadow:var(--shadow-soft); transition:box-shadow .2s var(--ease)}
.pg main a.pg-badge{color:var(--slate)}
.pg-badge b{font-weight:700}
.pg-badge:hover{box-shadow:0 0 0 3px var(--mint)}
.pg-mring{width:40px; height:40px; flex:none}

/* school leaders: video and quote end level */
.pg-voices{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.pg-voices .vid{aspect-ratio:auto; width:100%; height:100%; min-height:clamp(240px,30.5vw,372px); border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.pg-quote{margin:0; display:flex; flex-direction:column; background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.pg-quote blockquote{margin:0; font-family:var(--display); font-stretch:104%; font-weight:600; font-size:clamp(1rem,1.22vw,1.12rem); line-height:1.42; text-wrap:pretty}
.pg-quote blockquote::before{content:"\\201C"; display:block; font-weight:900; font-stretch:125%; font-size:3.6rem; line-height:.62; color:var(--mint); margin:.12em 0 .06em}
.pg-quote figcaption{margin-top:auto; padding-top:16px; font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; color:var(--mint); line-height:1.5}
@media (max-width:900px){.pg-voices{grid-template-columns:1fr} .pg-voices .vid{aspect-ratio:16/9; height:auto; min-height:0}}

/* pricing factors */
.pg-factors{background:#fff; color:var(--slate); border:2px solid var(--slate); border-radius:var(--r-xl); box-shadow:5px 5px 0 var(--slate); padding:8px clamp(18px,2.2vw,28px) 6px; display:flex; flex-direction:column; min-width:0}
.pg-factors__k{margin:0; padding:12px 0 10px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.pg-factors ul{list-style:none; margin:0; padding:0; flex:1; display:flex; flex-direction:column}
.pg-factors li{margin:0; flex:1; display:flex; align-items:center; gap:14px; padding:14px 0; border-top:1px solid var(--line); font-family:var(--display); font-weight:900; font-stretch:114%; font-size:clamp(1.3rem,2vw,1.75rem); line-height:1.05}
.pg-factors li::before{content:""; flex:none; width:12px; height:12px; background:var(--mint); border:2px solid var(--slate); border-radius:3px; transform:rotate(45deg)}

/* request actions */
.pg-acts{display:grid; gap:10px}
.pg-act{display:grid; grid-template-columns:64px minmax(0,1fr) auto; gap:16px; align-items:center; padding:15px 18px; border-radius:14px; background:rgba(255,255,255,.06); border:1.5px solid var(--line-dark); text-decoration:none; transition:border-color .2s, transform .2s var(--ease)}
.pg main a.pg-act{color:#fff}
.pg-act:hover{border-color:var(--mint); transform:translateX(3px)}
.pg-act b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.18rem; line-height:1.15; overflow-wrap:anywhere}
.pg-act small{display:block; color:rgba(255,255,255,.84); font-size:.9rem; line-height:1.4; margin-top:2px}
.pg-act__k{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.pg-act .go{width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.1); font-weight:800}
.pg-act--main{background:var(--mint); border-color:var(--mint)}
.pg main a.pg-act--main{color:var(--slate)}
.pg-act--main small{color:var(--slate)}
.pg-act--main .pg-act__k{color:var(--slate)}
.pg-act--main .go{background:var(--slate); color:var(--mint)}
.pg-act--main:hover{border-color:#fff}
@media (max-width:480px){.pg-act{grid-template-columns:minmax(0,1fr) auto; gap:4px 12px} .pg-act__k{grid-column:1/-1}}

/* form + embed fallback */
.pg-form__row{display:grid; grid-template-columns:1fr 1fr; gap:14px}
.pg-form .form__note{font-size:.9rem}
@media (max-width:560px){.pg-form__row{grid-template-columns:1fr}}
.pg-ticket{display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(18px,3vw,34px); align-items:center; border-radius:14px; padding:clamp(20px,3vw,34px); background:var(--mist)}
.pg-ticket__tile{width:124px; border-radius:16px; overflow:hidden; text-align:center; background:var(--slate); color:#fff; box-shadow:5px 5px 0 var(--mint); transform:rotate(-3deg)}
.pg-ticket__tile span{display:block; background:var(--mint); color:var(--slate); font-family:var(--mono); font-size:.7rem; letter-spacing:.16em; text-transform:uppercase; font-weight:700; padding:6px 0 5px}
.pg-ticket__tile b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:3.6rem; line-height:1; padding:12px 0 0; letter-spacing:-.02em}
.pg-ticket__tile i{display:block; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; color:var(--mint); padding:4px 0 14px}
.pg-ticket__txt p{margin:0 0 14px; color:var(--ink-soft)}
.pg-ticket__txt .pg-ticket__t{margin:0 0 6px; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.25rem,1.9vw,1.55rem); line-height:1.12; color:var(--logo-teal)}
@media (max-width:520px){.pg-ticket{grid-template-columns:1fr; justify-items:start}}
'''

RQ_CSS = '''
/* ---------- request-a-program: hero ---------- */
.rq-hero .phero__img{left:36%; -webkit-mask-image:linear-gradient(90deg, transparent 0, #000 46%); mask-image:linear-gradient(90deg, transparent 0, #000 46%)}
.rq-hero .phero__img img{opacity:.82; filter:none; object-position:50% 36%}
.rq-hero .phero__img::after{background:linear-gradient(90deg, rgba(29,65,78,.5) 0%, rgba(29,65,78,.12) 70%, rgba(29,65,78,.2) 100%)}
.rq-hero .wrap > *{max-width:min(100%,620px)}
.rq-hero .phero__wm{right:auto; left:-15%; bottom:-52%; --wm-o:.12}
@media (max-width:860px){.rq-hero .phero__img{left:0; -webkit-mask-image:none; mask-image:none} .rq-hero .phero__img img{opacity:.42} .rq-hero .phero__img::after{background:linear-gradient(90deg, rgba(29,65,78,.92) 0%, rgba(29,65,78,.7) 60%, rgba(29,65,78,.4) 100%)}}

/* ---------- the 360 approach band ---------- */
.rq-360__grid{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,5vw,72px); align-items:center}
.rq-360 h2{margin-bottom:.4em}
.rq-360 .lede{margin:0}
.rq-ring{position:relative; width:min(100%,430px); margin-inline:auto; aspect-ratio:1; border-radius:50%; background:#fff; padding:6.5%; box-shadow:0 0 0 12px rgba(255,255,255,.1), 0 34px 60px -30px rgba(0,0,0,.6)}
.rq-ring .ring{width:100%; height:100%; display:block; overflow:visible}
.rq-ring .seg{cursor:pointer; outline:none; transform-origin:210px 210px; transition:transform .6s var(--ease), opacity .45s ease}
.rq-ring .seg path{transition:opacity .25s}
.rq-ring .ring.has-active .seg:not(.on) path{opacity:.3}
.rq-ring .seg.on{transform:scale(1.05)}
.rq-ring .seg:focus-visible path{stroke:#1d414e; stroke-width:5}
.rq-ring .ring > text{transition:opacity .5s .45s}
.js .rq-ring:not(.in) .seg{opacity:0; transform:scale(.84) rotate(-16deg)}
.js .rq-ring:not(.in) .ring > text{opacity:0}
.rq-ring:not(.ready) .seg:nth-child(2){transition-delay:.07s} .rq-ring:not(.ready) .seg:nth-child(3){transition-delay:.14s} .rq-ring:not(.ready) .seg:nth-child(4){transition-delay:.21s} .rq-ring:not(.ready) .seg:nth-child(5){transition-delay:.28s} .rq-ring:not(.ready) .seg:nth-child(6){transition-delay:.35s}
.rq-ring.ready .seg{transition:transform .25s var(--ease)}
.rq-legend{list-style:none; margin:24px 0 26px; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(3,auto); grid-auto-flow:column; gap:8px 12px}
.rq-legend li{margin:0; min-width:0}
.rq-legend a{display:grid; grid-template-columns:auto minmax(0,1fr); align-items:center; gap:12px; height:100%; min-height:58px; padding:8px 14px 8px 9px; border-radius:14px; border:1.5px solid var(--line-dark); background:rgba(255,255,255,.05); text-decoration:none; font-weight:700; font-size:.97rem; line-height:1.25; transition:border-color .2s, background .2s}
.pg main .rq-legend a{color:#fff}
.rq-legend i{width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:var(--c); color:var(--ci); box-shadow:0 0 0 2px #fff; font-style:normal; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.05rem; line-height:1}
.rq-legend a:hover,.rq-legend a.on,.rq-legend a:focus-visible{border-color:var(--mint); background:rgba(21,255,200,.14)}
@media (max-width:900px){.rq-360__grid{grid-template-columns:1fr} .rq-ring{width:min(78%,340px)}}
@media (max-width:560px){.rq-legend{grid-template-columns:1fr; grid-template-rows:none; grid-auto-flow:row}}

/* ---------- pricing ---------- */
/* the request section follows directly, so pricing ends with its factors: no buttons of its own */
.rq-price{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:22px clamp(28px,5vw,72px); align-items:center}
.rq-price__head{min-width:0}
.rq-price__head .lede{margin-bottom:0}
@media (max-width:900px){.rq-price{grid-template-columns:1fr}}

/* ---------- start: form and booking ---------- */
.rq-start [data-tabs]{scroll-margin-top:100px}
.rq-start .section-head{align-items:center}
.rq-start .section-head > .rq-tabs{flex:0 0 auto}
.rq-tabs{display:flex; flex-wrap:wrap; gap:8px; margin:0}
.rq-tabs .tab{min-height:46px; padding:10px 20px; scroll-margin-top:170px}
.rq-panel{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.rq-panel__side{display:flex; flex-direction:column; min-width:0}
.rq-panel__side h3{font-size:clamp(1.4rem,2.2vw,1.9rem); margin-bottom:.35em}
.rq-panel__side > p{margin:0 0 18px; color:rgba(255,255,255,.84)}
.rq-panel__side .fill-img{flex:1; min-height:220px}
.rq-card{display:flex; flex-direction:column; background:#fff; color:var(--slate); border-radius:var(--r-xl); box-shadow:var(--shadow-soft); padding:var(--pad-card); min-width:0}
.pg main .rq-card a:not(.btn){color:var(--logo-teal)}
.rq-card--embed{padding:10px}
.rq-card .embed{flex:1; display:flex; flex-direction:column}
.rq-card .embed > *{flex:1}
.rq-panel--book{align-items:start}
.rq-panel--book .rq-panel__side{position:sticky; top:110px}
.rq-panel--book .rq-panel__side > p{margin-bottom:14px}
.pg main .rq-open{color:var(--mint); min-height:44px}
@media (max-width:560px){.rq-start .section-head > .rq-tabs{flex:1 1 100%} .rq-tabs .tab{flex:1 1 0; padding-inline:10px; white-space:nowrap}}
@media (max-width:900px){.rq-panel{grid-template-columns:1fr} .rq-panel__side .fill-img{display:none} .rq-panel--book .rq-panel__side{position:static}}
'''

AS_CSS = FILM_STRIP_CSS + '''
/* ---------- assemblies: hero ---------- */
.as-hero .wrap{grid-template-columns:minmax(0,1.04fr) minmax(0,.96fr)}
@media (max-width:1140px){.as-hero .wrap{grid-template-columns:minmax(0,1.14fr) minmax(0,.86fr); gap:32px}}
.as-hero__txt{container-type:inline-size; min-width:0}
.as-hero h1{margin-bottom:.4em; font-size:clamp(1.5rem,2.6vw,2.4rem); font-stretch:116%; line-height:1}
.as-hero h1 span{display:block}
.as-hero h1 .as-big{font-size:clamp(2.2rem,4.5vw,4.1rem); font-size:11.7cqi; font-stretch:125%; line-height:.86; letter-spacing:-.03em; margin:0 0 .1em -.03em}
.as-hero .phero__wm{right:auto; left:-16%; bottom:-46%; --wm-o:.12}
.as-hero .phero__media img{aspect-ratio:5/4; object-position:50% 40%}
.as-hero .phero__media .sticker{left:auto; right:-10px; bottom:auto; top:22px; transform:rotate(3deg)}
.as-hero figcaption{margin-top:12px; font-size:.85rem; color:rgba(255,255,255,.72)}
@media (max-width:860px){.as-hero h1 .as-big{font-size:10.4vw; font-size:11.7cqi} .as-hero .wrap{grid-template-columns:1fr} .as-hero .phero__media{order:0; max-width:none} .as-hero .phero__media .sticker{right:10px}}
@media (max-width:520px){.as-hero .phero__media .sticker{font-size:.74rem; white-space:nowrap; top:14px}}

/* ---------- the first-step line ---------- */
.as-path{--dot:30px; --ln:4px; list-style:none; margin:0; padding:0; position:relative; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0 var(--gap)}
.as-path::before{content:""; position:absolute; left:calc(var(--dot) / 2); right:14px; top:calc(var(--dot) / 2 - var(--ln) / 2); height:var(--ln); background:repeating-linear-gradient(90deg, var(--teal) 0 14px, transparent 14px 24px); transition:clip-path 1.5s var(--ease)}
.as-path::after{content:""; position:absolute; right:0; top:calc(var(--dot) / 2 - 9px); border-left:15px solid var(--teal); border-block:9px solid transparent; transition:opacity .3s 1.3s}
.as-path li{position:relative; margin:0; min-width:0; padding:calc(var(--dot) + 20px) 0 0}
@supports (grid-template-rows:subgrid){ .as-path{grid-template-rows:auto auto} .as-path li{display:grid; grid-row:span 2; grid-template-rows:subgrid; row-gap:0} }
.as-path li::before{content:""; position:absolute; left:0; top:0; width:var(--dot); height:var(--dot); border-radius:50%; background:#fff; border:var(--ln) solid var(--teal); transition:transform .5s var(--ease); transition-delay:calc(var(--i) * .32s + .1s)}
.as-path li.is-start::before{background:var(--slate); border-color:var(--mint); box-shadow:0 0 0 5px var(--slate)}
.as-path small,.as-path b{transition:opacity .5s ease, transform .5s var(--ease); transition-delay:calc(var(--i) * .32s + .2s)}
.as-path small{display:block; align-self:end; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); line-height:1.45; margin-bottom:6px}
.as-path b{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.3rem,1.95vw,1.7rem); line-height:1.1; color:var(--slate); padding-right:10px; text-wrap:balance}
.as-path li.is-start b{color:var(--logo-teal)}
.js .as-path:not(.in)::before{clip-path:inset(0 100% 0 0)}
.as-path::before{clip-path:inset(0 0 0 0)}
.js .as-path:not(.in)::after{opacity:0}
.js .as-path:not(.in) li::before{transform:scale(0)}
.js .as-path:not(.in) small,.js .as-path:not(.in) b{opacity:0; transform:translateY(8px)}
@media (max-width:760px){
  .as-path{grid-template-columns:1fr; grid-template-rows:none; gap:26px 0}
  .as-path li{display:block}
  .as-path::before{left:calc(var(--dot) / 2 - var(--ln) / 2); right:auto; top:calc(var(--dot) / 2); bottom:14px; width:var(--ln); height:auto; background:repeating-linear-gradient(180deg, var(--teal) 0 14px, transparent 14px 24px)}
  .as-path::after{right:auto; left:calc(var(--dot) / 2 - 9px); top:auto; bottom:0; border:0; border-top:15px solid var(--teal); border-inline:9px solid transparent}
  .as-path li{padding:2px 0 0 calc(var(--dot) + 16px)}
  .as-path li:last-child{padding-bottom:30px}
  .js .as-path:not(.in)::before{clip-path:inset(0 0 100% 0)}
}
/* the other end of the path: one panel. Left, the honest line and the approach behind every program; right, where schools go next */
.as-next{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,3.4vw,48px); align-items:stretch; margin-top:clamp(32px,4vw,52px); padding:clamp(24px,3vw,40px); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.as-next__say{display:flex; flex-direction:column; min-width:0}
.as-next__big{margin:0 0 .55em; font-family:var(--display); font-weight:900; font-stretch:116%; font-size:clamp(1.6rem,2.7vw,2.45rem); line-height:1.02; letter-spacing:-.02em; text-wrap:balance}
.as-next__say > p:not(.as-next__big){margin:0 0 22px; font-size:1.04rem; font-weight:500; line-height:1.55; color:rgba(255,255,255,.9)}
.as-360{margin-top:auto; display:grid; grid-template-columns:auto minmax(0,1fr); gap:14px; align-items:center; padding:14px 16px; border-radius:14px; border:1.5px solid var(--line-dark); background:rgba(255,255,255,.05); text-decoration:none; transition:border-color .2s, background .2s}
.pg main a.as-360{color:#fff}
.as-360:hover{border-color:var(--mint); background:rgba(21,255,200,.1)}
.as-360__ring{width:56px; height:56px; border-radius:50%; background:#fff; padding:6px; flex:none}
.as-360__ring svg{width:100%; height:100%; display:block}
.as-360 b{display:block; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.06rem; line-height:1.2}
.as-360 i{display:inline-flex; gap:.45em; margin-top:4px; font-style:normal; font-weight:700; font-size:.95rem; color:var(--mint)}
.as-360 i::after{content:"\\2192"; transition:transform .18s}
.as-360:hover i::after{transform:translateX(4px)}
.as-next__go{min-width:0; display:flex; flex-direction:column}
.as-next__k{margin:0 0 12px; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.as-next__tiles{flex:1; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:10px}
.as-next .pg-tile{min-height:0; padding:12px 14px 12px 16px; align-items:center; gap:4px 12px; border-color:transparent}
.as-next .pg-tile small{font-size:.7rem}
.as-next .pg-tile b{font-size:1.1rem}
.as-next .pg-tile i{width:32px; height:32px}
@media (max-width:1000px){ .as-next{grid-template-columns:1fr} .as-360{margin-top:4px} }
@media (max-width:560px){ .as-next__tiles{grid-template-columns:1fr} }

/* ---------- what every assembly includes ---------- */
.as-three{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0 var(--gap)}
.as-has{min-width:0}
@supports (grid-template-rows:subgrid){ .as-has{display:grid; grid-row:span 3; grid-template-rows:subgrid} }
.as-has__img{position:relative; aspect-ratio:4/3; border-radius:var(--r-xl); overflow:hidden; background:var(--slate)}
.as-has__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.as-has:hover .as-has__img img{transform:scale(1.035)}
.as-has h3{margin:20px 4px 0; font-size:clamp(1.25rem,1.7vw,1.4rem); display:flex; gap:12px; align-items:flex-start}
.as-has h3::before{content:""; flex:none; width:24px; height:24px; margin-top:.04em; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/15px no-repeat}
.as-has p{margin:8px 4px 0 40px; color:rgba(255,255,255,.86); font-size:.98rem; line-height:1.5}
@media (max-width:860px){.as-three{grid-template-columns:1fr; gap:18px 0} .as-has{display:grid; grid-row:auto; grid-template-rows:auto auto; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); column-gap:18px} .as-has__img{grid-row:1 / 3} .as-has h3{margin-top:0; align-self:end} .as-has p{align-self:start}}
@media (max-width:560px){.as-three{gap:26px 0} .as-has{display:block} .as-has h3{margin-top:16px}}

/* ---------- films ---------- */
.as-filmrow{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.as-filmrow .fcard{border-radius:var(--r-xl)}
.as-filmrow .fcard img{filter:none}
.as-filmrow .fcard--know img{object-position:92% 50%}
.as-filmrow .fcard__tag{font-size:.7rem}
.as-filmrow .fcard__go{font-size:.74rem}
.as-filmrow .fcard__title{bottom:46px; overflow-wrap:anywhere}
.as-filmrow .fcard--know .fcard__title{font-size:clamp(.95rem,1.5vw,1.35rem)}
.as-more{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); align-items:center; gap:10px var(--gap); margin:22px 0 0; padding-top:20px; border-top:1px solid var(--line-dark)}
.as-more > b{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.as-more .arrow-link{font-size:.98rem}
@media (max-width:900px){.as-more .arrow-link{min-height:44px} .as-more{gap:0 var(--gap)} .as-more > b{margin-bottom:6px} .as-filmrow{grid-template-columns:repeat(2,minmax(0,1fr))} .as-filmrow .fcard--know .fcard__title{font-size:clamp(.74rem,3.4vw,1.35rem)} .as-more{grid-template-columns:1fr}}

/* ---------- request an assembly (light): actions beside the pricing card, ending level ---------- */
.as-req__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.as-req__body{min-width:0; display:flex; flex-direction:column}
.as-req h2{font-size:clamp(1.9rem,4vw,3.4rem); font-stretch:118%; text-transform:uppercase; font-weight:900; line-height:.95; letter-spacing:-.015em; color:var(--logo-teal)}
.as-req .lede{margin-bottom:22px}
.as-req .pg-acts{margin-top:auto}
.as-req .pg-act{background:#fff; border-color:var(--line); box-shadow:var(--shadow-soft)}
.pg main .as-req a.pg-act{color:var(--slate)}
.as-req .pg-act small{color:var(--ink-soft)}
.as-req .pg-act__k{color:var(--logo-teal)}
.as-req .pg-act .go{background:var(--aqua); color:var(--logo-teal)}
.as-req .pg-act:hover{border-color:var(--teal)}
.as-req .pg-act--main{background:var(--slate); border-color:var(--slate)}
.pg main .as-req a.pg-act--main{color:#fff}
.as-req .pg-act--main small{color:rgba(255,255,255,.86)}
.as-req .pg-act--main .pg-act__k{color:var(--mint)}
.as-req .pg-act--main .go{background:var(--mint); color:var(--slate)}
.as-req .pg-act--main:hover{border-color:var(--slate)}
.as-price{display:flex; flex-direction:column; min-width:0; background:#fff; color:var(--slate); border:2px solid var(--slate); border-radius:var(--r-xl); box-shadow:6px 6px 0 var(--slate); padding:var(--pad-card)}
.as-price .eyebrow{margin-bottom:.7rem}
.as-price h3{font-size:clamp(1.4rem,2.1vw,1.85rem); line-height:1.05; margin-bottom:.4em; color:var(--logo-teal)}
.as-price > p:not(.eyebrow):not(.pg-factors__k){margin:0 0 6px; font-size:1rem; line-height:1.5; color:var(--ink-soft)}
.as-price .pg-factors__k{padding-top:16px}
.as-price__f{list-style:none; margin:0 0 18px; padding:0}
.as-price__f li{margin:0; display:flex; align-items:center; gap:12px; padding:11px 0; border-top:1px solid var(--line); font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.15rem,1.6vw,1.35rem); line-height:1.1}
.as-price__f li::before{content:""; flex:none; width:11px; height:11px; background:var(--mint); border:2px solid var(--slate); border-radius:3px; transform:rotate(45deg)}
.as-price .arrow-link{margin-top:auto}
@media (max-width:900px){ .as-req__grid{grid-template-columns:1fr} }
'''


# =====================================================================
# request-a-program.html
# =====================================================================
def request():
    hero = phero('Request a <span class="mk">program</span>', 'Bring SafeBAE to your school, campus or community.', '',
                 [('Home', 'index.html'), ('Request a Program', None)], kind='', image='dsc04560',
                 actions=btn('Send a request', '#start', 'mint', arrow=True, attrs=' data-tab-go="tab-request"') + btn('Book a meeting', '#start', 'ghost', attrs=' data-tab-go="tab-book"')
                 ).replace('class="phero ', 'class="phero rq-hero ', 1)

    menu = f'''<section class="band band--mist" id="programs">
  <div class="wrap">
    <div class="section-head"><div><h2>Start with one event, or build a whole-school program</h2>
      <p class="lede lede--full">We offer flexible options to meet your school’s needs. Some partners begin with a single assembly or awareness event, while others start a deeper collaboration right away.</p></div></div>
    <div class="pg-menu">{''.join(prog_card(p) for p in PROGRAMS)}</div>
  </div>
</section>'''

    legend = ''.join(f'<li><a href="{RING_HREF[i]}" data-leg="{i}" style="--c:{c[2]}; --ci:{c[3]}"><i aria-hidden="true">{i+1}</i><span>{esc(c[0])}</span></a></li>' for i, c in enumerate(RCOMPS))
    approach = f'''<section class="band band--logo rq-360" id="approach">
  <div class="wrap rq-360__grid">
    <div class="rq-ring" data-ring>{ring_links()}</div>
    <div>
      <h2>Every program is built on the SafeBAE 360° approach</h2>
      <p class="lede">SafeBAE 360° Schools is our whole-school approach to preventing sexual and dating violence, with six core components that work together. Each component can be delivered on its own or as part of the whole, tailored to your school’s needs, goals, and capacity.</p>
      <ol class="rq-legend">{legend}</ol>
      <div class="btns">{btn('How 360° Schools works', '360-schools.html', 'mint', arrow=True)}</div>
    </div>
  </div>
</section>'''

    pricing = f'''<section class="band band--mint" id="pricing">
  <div class="wrap rq-price">
    <div class="rq-price__head">
      <p class="eyebrow">Flexible pricing for school partners</p>
      <h2>Cost should never be a barrier to prevention</h2>
      <p class="lede">That’s why we offer a flexible, sliding-scale pricing model tailored to each school’s needs and capacity, always striving to meet partners where they are.</p>
    </div>
    {factors()}
  </div>
</section>'''

    start = f'''<section class="band band--slate rq-start" id="start">
  <div class="wrap" data-tabs="request-start">
    <div class="section-head"><div><h2>Ready to request a program?</h2></div>
      <div class="rq-tabs" role="tablist" aria-label="How would you like to start?"><button class="tab" role="tab" id="tab-request" aria-controls="rp-request" aria-selected="true">Send a request</button><button class="tab" role="tab" id="tab-book" aria-controls="rp-book" aria-selected="false" tabindex="-1">Book a meeting</button></div></div>
    <div role="tabpanel" id="rp-request" aria-labelledby="tab-request">
      <div class="rq-panel">
        <div class="rq-panel__side"><h3>Tell us what you’re looking for</h3><p>Share key details about your needs and let us know how to follow up.</p>
          <div class="fill-img">{img('img-3947', 'A presenter at the front of a classroom with slides on a screen while students watch from their tables')}</div></div>
        <div class="rq-card">{static_form('req', 'Program request')}</div>
      </div>
    </div>
    <div role="tabpanel" id="rp-book" aria-labelledby="tab-book" hidden>
      <div class="rq-panel rq-panel--book">
        <div class="rq-panel__side"><h3>Book a meeting with our team</h3><p>Book a meeting with us to learn more and get started. We’ll talk through your school’s needs, goals and capacity, and how our sliding-scale pricing applies.</p>
          <a class="arrow-link rq-open" href="{CALENDLY}" target="_blank" rel="noopener">Open Calendly in a new tab</a></div>
        <div class="rq-card rq-card--embed">{meeting_embed()}</div>
      </div>
    </div>
  </div>
</section>'''

    body = hero + menu + approach + leaders() + pricing + start
    ring_js = r'''<script>(function(){
  var w = document.querySelector('[data-ring]'); if(!w) return;
  var ring = w.querySelector('.ring'), segs = [].slice.call(w.querySelectorAll('.seg')), items = [].slice.call(document.querySelectorAll('.rq-legend a'));
  function on(n){ segs.forEach(function(s, i){ s.classList.toggle('on', i === n); }); items.forEach(function(x, i){ x.classList.toggle('on', i === n); }); ring.classList.toggle('has-active', n >= 0); }
  function wire(list){ list.forEach(function(el, i){
    el.addEventListener('mouseenter', function(){ on(i); }); el.addEventListener('focus', function(){ on(i); });
    el.addEventListener('mouseleave', function(){ on(-1); }); el.addEventListener('blur', function(){ on(-1); });
  }); }
  wire(segs); wire(items);
  function go(){ w.classList.add('in'); setTimeout(function(){ w.classList.add('ready'); }, 1200); }
  if(!('IntersectionObserver' in window)){ go(); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ go(); io.disconnect(); } }); }, {threshold: .3});
  io.observe(w);
})();</script>'''
    page('request-a-program.html', 'Request a Program · SafeBAE',
         'Request a SafeBAE program for your school, campus or community: assemblies, curriculum, staff training, policy support and more, with flexible sliding-scale pricing.',
         body, active='programs', head_extra=f'<style>{PG_CSS}{RQ_CSS}</style>', body_class='pg pg-rq', scripts=TABGO_JS + ring_js)


# =====================================================================
# assemblies.html
# =====================================================================
ASSEMBLY_FILMS = ['red', 'bae', 'know', 'rc']            # four of the seven films that come with a teaching guide; the other three are linked under them
MORE_FILMS = [('Intimacy & Dating After Sexual Assault', 'film-dating-after-sexual-assault.html'),
              ('Ending Online Harassment of Survivors', 'film-online-harassment-of-survivors.html'),
              ('Supporting Male Survivors', 'film-sexual-assault-of-men.html')]
FILM_IMG = {'red': 'yt-ett8bnlbwwg'}   # the film's own still crops to a portrait better than its title card


def fcard(key):
    href, k, title, im, tag = next(f for f in FILMS if f[1] == key)
    return (f'<a class="fcard fcard--{k}" href="{href}">{img(FILM_IMG.get(k, im), "")}<span class="fcard__shade"></span>'
            f'<span class="fcard__tag">{esc(tag)}</span><span class="fcard__title">{esc(title)}</span><span class="fcard__go">Film + guide &rarr;</span></a>')


def assemblies():
    ask = 'request-a-program.html#start'
    hero = f'''<section class="phero phero--split as-hero"><span class="phero__wm" aria-hidden="true"></span><div class="wrap"><div class="as-hero__txt">
      {crumbs([('Home', 'index.html'), ('Request a Program', 'request-a-program.html'), ('Assemblies', None)])}
      <a class="pg-badge" href="360-schools.html">{mini_ring()}<span><b>SafeBAE 360&deg;</b> &middot; A first step</span></a>
      <h1><span class="as-big mk">Assemblies</span> <span>&amp; one-time events</span></h1>
      <p class="lede">Many school partners start with a one-time assembly or awareness event. Ours are always co-presented with youth leaders and tailored to your students.</p>
      <div class="btns">{btn('Request an assembly', ask, 'mint', arrow=True)}{btn('Book a meeting', CALENDLY, 'ghost')}</div>
    </div><div class="phero__media">{img('066', 'Five presenters, one in a SafeBAE shirt, standing together in front of bleachers full of students in a school gym', loading='eager')}<span class="sticker">Co-presented with youth leaders</span></div></div></section>'''

    nodes = [('is-start', 'An accessible first step', 'One assembly or awareness event'),
             ('', 'It can spark', 'Critical conversations'),
             ('', 'It can open the door to', 'Deeper engagement'),
             ('', 'It is often the starting place for', 'Longer-term collaboration')]
    path = ''.join(f'<li class="{c}" style="--i:{i}"><small>{esc(k)}</small><b>{esc(t)}</b></li>' for i, (c, k, t) in enumerate(nodes))
    tiles = ''.join(prog_tile(p) for p in PROGRAMS if p['key'] != 'assemblies')
    first = f'''<section class="band band--paper" id="first-step">
  <div class="wrap">
    <div class="section-head"><div><h2>An assembly is a <span class="mk">first step</span></h2>
      <p class="lede lede--full">We know many school partners seek one-time assemblies or awareness events as an accessible first step, and we’re happy to offer them.</p></div></div>
    <ol class="as-path" data-path>{path}</ol>
    <div class="as-next" id="next">
      <div class="as-next__say">
        <p class="as-next__big">Assemblies alone cannot replace sustained prevention work.</p>
        <p>They are a powerful entry point for schools beginning their partnership with us. Wherever you begin, we can help you take actionable steps toward building safer, more supportive school environments.</p>
        <a class="as-360" href="360-schools.html"><span class="as-360__ring">{mini_ring('', 24)}</span><span><b>Every program is built on the SafeBAE 360° approach</b><i>How 360° Schools works</i></span></a>
      </div>
      <div class="as-next__go">
        <p class="as-next__k">Where schools go after an assembly</p>
        <div class="as-next__tiles">{tiles}</div>
      </div>
    </div>
  </div>
</section>'''

    has = [('assembly-stage-group', 'A group of people standing together on a stage in front of a projection screen', 'object-position:50% 28%',
            'Youth leaders co-present', 'Our assemblies and school events are always co-presented with youth leaders.'),
           ('img-2400', 'Students and adults seated in a circle in a classroom', '',
            'Age-appropriate', 'Each event is tailored to be age-appropriate for the students in the room.'),
           ('assembly-whiteboard', 'A woman writing the word “Respect” on a classroom whiteboard', 'object-position:60% 40%',
            'Tailored to your school', 'We tailor every assembly to be relevant and impactful for your school community.')]
    has_html = ''.join(f'<div class="as-has"><div class="as-has__img">{img(im, alt, style=st)}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for im, alt, st, t, d in has)
    every = f'''<section class="band band--deep" id="includes">
  <div class="wrap">
    <div class="section-head"><div><h2>What every SafeBAE assembly includes</h2></div>{btn('Request an assembly', ask, 'mint', arrow=True)}</div>
    <div class="as-three">{has_html}</div>
  </div>
</section>'''

    more = ''.join(f'<a class="arrow-link" href="{h}">{esc(t)}</a>' for t, h in MORE_FILMS)
    films = f'''<section class="band band--logo as-films" id="films">
  <div class="wrap">
    <div class="section-head"><div><h2>Films to build an event around</h2>
      <p class="lede lede--full">SafeBAE’s youth-made films each come with a free teaching guide. “School assembly or presentation” is one of the uses SafeBAE lists for them.</p></div>{btn('All films and guides', 'library.html#films', 'mint', arrow=True)}</div>
    <div class="as-filmrow">{''.join(fcard(k) for k in ASSEMBLY_FILMS)}</div>
    <p class="as-more"><b>More films with teaching guides</b>{more}</p>
  </div>
</section>'''

    fac = ''.join(f'<li>{esc(x)}</li>' for x in FACTORS)
    req = f'''<section class="band band--aqua as-req" id="request">
  <div class="wrap as-req__grid">
    <div class="as-req__body">
      <h2>Request an assembly</h2>
      <p class="lede">Tell us what you’re looking for and how to follow up, or book a meeting with us to learn more and get started.</p>
      <div class="pg-acts">
        <a class="pg-act pg-act--main" href="{ask}"><span class="pg-act__k">Form</span><span><b>Send a request</b><small>Share key details about your needs and let us know how to follow up.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
        <a class="pg-act" href="{CALENDLY}" target="_blank" rel="noopener"><span class="pg-act__k">60 min</span><span><b>Book a meeting</b><small>Pick a time that works for you on our Calendly page.</small></span><span class="go" aria-hidden="true">&#8599;</span></a>
        <a class="pg-act" href="mailto:{EMAIL}"><span class="pg-act__k">Email</span><span><b>{EMAIL}</b><small>Write to us instead of using the form.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
    <div class="as-price">
      <p class="eyebrow">Flexible pricing for school partners</p>
      <h3>Cost should never be a barrier to prevention</h3>
      <p>We offer a flexible, sliding-scale pricing model tailored to each school’s needs and capacity, always striving to meet partners where they are.</p>
      <p class="pg-factors__k">We consider factors like</p>
      <ul class="as-price__f">{fac}</ul>
      <a class="arrow-link" href="request-a-program.html#pricing">Pricing for school partners</a>
    </div>
  </div>
</section>'''

    body = hero + first + every + leaders() + films + req
    js = r'''<script>(function(){
  var p = document.querySelector('[data-path]'); if(!p) return;
  if(!('IntersectionObserver' in window)){ p.classList.add('in'); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ p.classList.add('in'); io.disconnect(); } }); }, {threshold: .4});
  io.observe(p);
})();</script>'''
    page('assemblies.html', 'Assemblies · SafeBAE',
         'Book a SafeBAE assembly or awareness event for your school. Every assembly is co-presented with youth leaders and tailored to your students, with sliding-scale pricing.',
         body, active='programs', head_extra=f'<style>{PG_CSS}{AS_CSS}</style>', body_class='pg pg-as', fonts=film_font_link(), scripts=js)


def build():
    request()
    assemblies()


if __name__ == '__main__':
    build()
