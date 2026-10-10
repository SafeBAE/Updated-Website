"""STUDENTS group, v3 (part two): clubs.html, reform-policy.html, summer-institute.html, espanol.html.
(students.html and peer-educator.html build from pages_students.py; the shared patterns here match that module.)
Run: python3 -c "import pages_students2; pages_students2.build()" """
from lib import *
from films_common import help_inline, HELPLINE_CSS

# ---------------------------------------------------------------- links
CLUB_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfoQAsZ5bZpRyBpL1ELxoC0yk5ewm5mkpoz6wwR49IcGoKtLQ/viewform'
POLICY_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdWO15lAjJlPeQd_nVJXyd_v0_XrnWWzjcV29rornyf4gFb_w/viewform'
ES_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLScz_QD0Ms-xgeDe7C3S_3W8SK1fI-u5rflrffsmhOSh1S7B3g/viewform'
CLUB_HUB = 'https://clubs.safebae.org'
CALENDLY = 'https://calendly.com/clubsupport-safebae/30min'
CLUB_EMAIL = 'clubsupport@safebae.org'

def crumbs(*items):
    parts = [('Home', 'index.html')] + list(items)
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in parts) + '</nav>'

def st_help():
    """Student-facing wording of the shared helpline strip."""
    return (help_inline().replace('Share these 24/7, confidential resources with students', 'Need to talk to someone? Free, confidential and open 24/7')
            .replace('btn btn--coral btn--sm', 'btn btn--slate btn--sm').replace('1-866-331-9474', '1&#8209;866&#8209;331&#8209;9474'))

def tile(title, desc, href, new=False):
    """A link tile: title, one line, round arrow. Same anatomy as the tiles on peer-educator.html."""
    ext = href.startswith('http')
    tg = ' target="_blank" rel="noopener"' if ext else ''
    chip = '<span class="chip chip--mint">New</span>' if new else ''
    return (f'<a class="st-tile" href="{esc(href)}"{tg}><b>{esc(title)}{chip}</b><small>{esc(desc)}</small>'
            f'<span class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</span></a>')

def form_card(src, link, label, title, cta, height, frame_title):
    """Registration form: the live form on a real site, a finished call card everywhere else."""
    return (f'<div class="embed" data-embed="{esc(src)}" data-h="{height}" data-title="{esc(frame_title)}">'
            f'<div class="embed__fallback"><small>{esc(label)}</small><h3>{esc(title)}</h3>{btn(cta, link, "slate")}</div></div>')

# ---------------------------------------------------------------- the student journey
JOURNEY = [
    ('Learn', 'Watch the films', 'Youth-made films with discussion guides, plus the BAE Skills Lab.', 'library.html#films'),
    ('Train', 'Become a Certified Peer Educator', 'Free and self-paced: 16 modules and a certificate.', 'peer-educator.html'),
    ('Lead', 'Start or join a SafeBAE club', 'Start, affiliate or restart a chapter at your school.', 'clubs.html'),
    ('Change', 'Reform your school’s policy', 'A student guide to stronger sexual misconduct policies.', 'reform-policy.html'),
]

def journey(cur=None):
    """Four equal cards (the same component as students.html). The current stop is marked instead of linked."""
    lis = []
    for verb, title, desc, href in JOURNEY:
        on = verb == cur
        mark = f'<span class="st-stop__go" aria-hidden="true">{daisy()}</span><span class="st-stop__here">You are here</span>' if on else '<span class="st-stop__go" aria-hidden="true">&rarr;</span>'
        inner = (f'<span class="st-stop__top"><span class="st-stop__verb">{esc(verb)}</span>{mark}</span>'
                 f'<b>{esc(title)}</b><small>{esc(desc)}</small>')
        if on:
            lis.append(f'<li class="on"><span class="st-stop" aria-current="page">{inner}</span></li>')
        else:
            lis.append(f'<li><a class="st-stop" href="{href}">{inner}</a></li>')
    return '<ol class="st-path reveal">' + ''.join(lis) + '</ol>'

# ---------------------------------------------------------------- shared CSS (all four pages)
CSS = HELPLINE_CSS + '''
/* eyebrows: Logo Teal on light, mint on dark, white on SafeBAE Teal, slate on mint */
.st main .eyebrow{color:var(--logo-teal)}
.st main :is(.band--slate,.band--deep,.band--logo,.st-ihero,.st-es) .eyebrow{color:var(--mint)}
.st main :is(.band--teal,.st-chero) .eyebrow{color:#fff}
.st main .band--mint .eyebrow{color:var(--slate)}
.st .section-head h2 + .lede{margin-top:.55em}
.st :is(.band--slate,.band--deep) .section-head .lede{color:rgba(255,255,255,.88)}
.st .band--teal .section-head .lede{color:#fff}
/* only one coral button per page (the shared donate button): the helpline button goes slate */
.st .helpline .btn--coral{--b:var(--slate); --t:#fff}
.st .helpline{border-radius:var(--r-xl); padding:var(--pad-card)}
.st .helpline b{font-size:1.15rem; line-height:1.2; margin-bottom:4px}
.st .helpline span{font-size:1rem; line-height:1.5}
.st .helpline .btn{flex:none}

/* journey: four equal stops (same component as students.html) */
.st-path{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.st-path li{margin:0; min-width:0; display:flex}
.st .st-stop{flex:1; min-width:0; display:flex; flex-direction:column; gap:6px; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; color:var(--slate); border:1px solid transparent; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.st a.st-stop:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.st-stop__top{position:relative; display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:clamp(20px,2.6vw,36px)}
.st-stop__verb{font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(1.25rem,1.85vw,1.65rem); line-height:1; letter-spacing:-.015em; color:var(--logo-teal); min-width:0}
.st-stop__go{flex:none; width:clamp(36px,3.4vw,44px); height:clamp(36px,3.4vw,44px); border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; font-size:1.1rem; transition:background .2s, color .2s, transform .25s var(--ease)}
a.st-stop:hover .st-stop__go{background:var(--slate); color:var(--mint); transform:translateX(4px)}
.st-stop b{font-family:var(--display); font-stretch:108%; font-size:1.28rem; line-height:1.15}
.st-stop small{font-size:.95rem; line-height:1.45; color:var(--ink-soft)}
.st-stop__here{position:absolute; left:0; top:100%; margin-top:7px; font-family:var(--mono); font-size:.72rem; line-height:1; letter-spacing:.1em; text-transform:uppercase; font-weight:600; white-space:nowrap}
.st-stop__go .daisy{width:24px; height:24px}
.band--paper .st-stop{border-color:var(--line)}
.band--paper a.st-stop:hover{border-color:var(--teal)}
.band--mint .st-path li.on .st-stop{background:var(--slate) var(--grain); color:#fff}
.band--mint .st-path li.on .st-stop__verb{color:var(--mint)}
.band--mint .st-path li.on small{color:rgba(255,255,255,.86)}
.band--mint .st-path li.on .st-stop__go{background:var(--mint); color:var(--slate)}
.st :is(.band--slate,.band--deep) .st-stop{background:rgba(255,255,255,.05); border-color:var(--line-dark); color:#fff}
:is(.band--slate,.band--deep) .st-stop__verb{color:var(--mint)}
:is(.band--slate,.band--deep) .st-stop small{color:rgba(255,255,255,.8)}
:is(.band--slate,.band--deep) .st-stop__go{background:rgba(255,255,255,.1); color:var(--mint)}
.st :is(.band--slate,.band--deep) a.st-stop:hover{border-color:var(--mint); box-shadow:none}
:is(.band--slate,.band--deep) a.st-stop:hover .st-stop__go{background:var(--mint); color:var(--slate)}
.st :is(.band--slate,.band--deep) .st-path li.on .st-stop{background:var(--mint); border-color:var(--mint); color:var(--slate)}
:is(.band--slate,.band--deep) .st-path li.on :is(.st-stop__verb,small){color:var(--slate)}
:is(.band--slate,.band--deep) .st-path li.on .st-stop__go{background:var(--slate); color:var(--mint)}
@media (max-width:1000px){.st-path{grid-template-columns:repeat(2,minmax(0,1fr))} .st-stop__go{width:44px; height:44px} .st-stop__verb{font-size:1.6rem}}
@media (max-width:560px){.st-path{grid-template-columns:minmax(0,1fr)} .st-stop__top{margin-bottom:14px} .st-path li.on .st-stop__top{margin-bottom:34px}}

/* photo that takes the height of the text beside it */
.st-fill{position:relative; margin:0; min-width:0; min-height:260px}
.st-fill > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.st-fill .sticker{position:absolute; left:-10px; bottom:22px; z-index:1}
.st-fill figcaption{position:absolute; left:0; right:0; bottom:0; padding:48px 22px 18px; border-radius:0 0 var(--r-xl) var(--r-xl); background:linear-gradient(180deg, rgba(8,24,30,0), rgba(8,24,30,.9)); color:#fff; font-size:.92rem; line-height:1.4; font-weight:500}
@media (max-width:900px){.st-fill{min-height:0; aspect-ratio:3/2} .st-fill .sticker{left:12px}}

.st-label{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin:0 0 12px}

/* link tiles (same anatomy as peer-educator.html) */
.st .st-tile{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:4px 14px; align-items:center; align-content:center; padding:18px 22px; border-radius:16px; background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); min-width:0; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.st .st-tile:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.st-tile b{display:flex; flex-wrap:wrap; align-items:center; gap:6px 10px; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; color:var(--logo-teal)}
.st-tile b .chip{font-size:.7rem; border:1.5px solid var(--slate)}
.st-tile small{grid-column:1; font-size:.95rem; line-height:1.4; color:var(--ink-soft)}
.st-tile .go{grid-row:1/3; grid-column:2; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .25s var(--ease)}
.st-tile:hover .go{background:var(--mint); transform:translateX(3px)}
.st :is(.band--slate,.band--deep) .st-tile{background:rgba(255,255,255,.05); border-color:var(--line-dark); color:#fff}
:is(.band--slate,.band--deep) .st-tile b{color:#fff}
:is(.band--slate,.band--deep) .st-tile small{color:rgba(255,255,255,.82)}
:is(.band--slate,.band--deep) .st-tile .go{background:rgba(255,255,255,.1); color:var(--mint)}
.st :is(.band--slate,.band--deep) .st-tile:hover{border-color:var(--mint); box-shadow:none}
:is(.band--slate,.band--deep) .st-tile:hover .go{background:var(--mint); color:var(--slate)}

/* register: a call card until the form loads; with the live form, a sticky side column beside it (as on peer-educator.html) */
.st-reg{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.st-reg__side{display:contents}
.st-reg__head{grid-column:1; grid-row:1; min-width:0; align-self:center; padding-right:clamp(0px,2vw,32px)}
.st-reg__head h2{margin-bottom:.35em}
.st-reg__head .lede{margin:0}
.st-reg__form{grid-column:2; grid-row:1; min-width:0; display:flex}
.st-reg__form .embed{flex:1; display:flex; min-width:0}
.st-reg__form .embed__fallback{flex:1; display:flex; flex-direction:column; align-items:flex-start; gap:10px; min-height:210px; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--mint); color:var(--slate); box-shadow:var(--shadow-soft)}
.st-reg__form .embed__fallback h3{font-size:clamp(1.35rem,2vw,1.7rem); margin:0}
.st-reg__form .embed__fallback small{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--slate)}
.st-reg__form .embed__fallback .btn{margin-top:auto}
.st-reg__links{grid-column:1/-1; grid-row:2; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap)}
.st-reg__links--one{grid-template-columns:minmax(0,1fr)}
.st-reg:has(iframe){grid-template-columns:minmax(0,4fr) minmax(0,8fr); align-items:start}
.st-reg:has(iframe) .st-reg__side{display:block; grid-column:1; grid-row:1; position:sticky; top:104px; min-width:0}
.st-reg:has(iframe) .st-reg__head{padding-right:0}
.st-reg:has(iframe) .st-reg__head h2{font-size:clamp(1.6rem,2.7vw,2.35rem); overflow-wrap:break-word}
.st-reg:has(iframe) .st-reg__links{grid-template-columns:minmax(0,1fr); gap:10px; margin-top:26px}
.st-reg:has(iframe) .st-reg__form .embed{display:block; background:#fff; border-radius:var(--r-xl); border:1px solid var(--line); padding:6px; box-shadow:var(--shadow-soft)}
.st-reg:has(iframe) .st-reg__form iframe{display:block; border-radius:16px!important}
@media (max-width:900px){
  .st-reg,.st-reg:has(iframe){grid-template-columns:minmax(0,1fr)}
  .st-reg__head,.st-reg__form,.st-reg__links{grid-column:1; grid-row:auto}
  .st-reg__head{order:1; padding-right:0} .st-reg__form{order:2}
  .st-reg__links{grid-template-columns:minmax(0,1fr); gap:10px; order:3}
  .st-reg__form .embed__fallback{min-height:0}
  .st-reg:has(iframe) .st-reg__side{display:contents}
  .st-reg:has(iframe) .st-reg__links{margin-top:0}
}
'''

# ================================================================= clubs.html
CLUB_CSS = '''
/* hero */
.st-chero{--wm-o:.26; background:var(--teal); color:#fff; position:relative; overflow:hidden}
.st-chero .wm-daisy{color:var(--aqua)}
.st-chero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,84px)}
.st-chero h1{font-size:clamp(2.3rem,3.9vw,3.5rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin-bottom:.4em; text-wrap:wrap}
.st-chero h1 > span{display:block}
.st-chero .mk{background:none; color:var(--aqua)}
.st-chero .lede{color:#fff; max-width:none}
.st-chero .crumbs{color:#fff}
.st-chero .crumbs a{color:#fff; text-decoration:underline; text-underline-offset:3px}
.st-chero :focus-visible{outline-color:#fff}
.st-cpair{position:relative; aspect-ratio:1/.9; animation:sb-rise-r 1s .1s var(--ease) both}
.st-cpair figure{position:absolute; margin:0; overflow:hidden; border-radius:var(--r-xl); box-shadow:0 30px 60px -28px rgba(10,30,36,.7); transition:transform .35s var(--ease)}
.st-cpair img{width:100%; height:100%; object-fit:cover}
.st-cpair .a{right:0; top:0; width:86%; height:80%}
.st-cpair .a img{object-position:50% 30%}
.st-cpair .b{left:0; bottom:0; width:47%; height:42%; border:6px solid #fff; border-radius:16px; transform:rotate(-3deg)}
.st-cpair .b:hover{transform:rotate(0) scale(1.03)}
.st-cpair .sticker{position:absolute; z-index:3; white-space:nowrap}
@media (max-width:900px){.st-chero > .wrap{grid-template-columns:minmax(0,1fr)} .st-cpair{max-width:520px; width:100%}}

/* which one fits: three choices on the left, the answer on the right */
.st-chooser{display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr); gap:var(--gap); align-items:stretch}
.st-choose{display:grid; grid-auto-rows:1fr; gap:12px; min-width:0}
.st-choose [role="tab"]{position:relative; scroll-margin-top:150px; font:inherit; text-align:left; cursor:pointer; display:grid; grid-template-columns:minmax(0,1fr) auto; align-content:center; align-items:center; gap:5px 14px; padding:18px 20px; border-radius:16px; border:2px solid var(--line); background:#fff; color:var(--slate); transition:border-color .2s, background .2s, color .2s}
.st-choose [role="tab"] span{font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.2rem,1.6vw,1.42rem); line-height:1.12}
.st-choose [role="tab"] small{grid-column:1; font-size:.95rem; font-weight:500; color:var(--ink-soft); line-height:1.4}
.st-choose [role="tab"] i{grid-column:2; grid-row:1/3; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-style:normal; font-weight:800; background:var(--aqua); color:var(--logo-teal); transition:background .2s, color .2s, transform .25s var(--ease)}
.st-choose [role="tab"]:hover{border-color:var(--teal)}
.st-choose [role="tab"]:hover i{transform:translateX(3px)}
.st-choose [role="tab"][aria-selected="true"]{background:var(--slate) var(--grain); color:#fff; border-color:var(--slate)}
.st-choose [role="tab"][aria-selected="true"] small{color:rgba(255,255,255,.86)}
.st-choose [role="tab"][aria-selected="true"] i{background:var(--mint); color:var(--slate)}
.st-choose [role="tab"][aria-selected="true"]::after{content:""; position:absolute; left:calc(100% + 2px); top:50%; width:var(--gap); height:4px; margin-top:-2px; background:var(--slate)}
.st-choice{grid-column:2; grid-row:1; min-width:0; display:grid; grid-template-columns:minmax(0,11fr) minmax(0,9fr); border-radius:var(--r-xl); overflow:hidden; background:var(--aqua); color:var(--slate)}
/* the three answers share one cell, so the block keeps its height when the choice changes */
.st-choice[hidden]{display:grid!important; visibility:hidden; pointer-events:none}
.st-choice__body{display:flex; flex-direction:column; padding:clamp(24px,3vw,40px); min-width:0}
.st-choice__body h3{font-size:clamp(1.45rem,2.05vw,1.8rem); line-height:1.1; margin:0 0 .6em}
.st-choice__body p{margin:0 0 1em; font-size:1.04rem; line-height:1.6}
.st-choice__body .st-choice__foot{margin:auto 0 0; padding-top:16px; border-top:1px solid rgba(29,65,78,.2); font-size:.95rem; line-height:1.5; color:var(--ink-soft)}
.st-choice__img{position:relative; margin:0; min-height:360px}
.st-choice__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
@media (max-width:900px){
  .st-chooser{grid-template-columns:minmax(0,1fr)}
  .st-choose{grid-template-columns:repeat(3,minmax(0,1fr)); grid-auto-rows:auto}
  .st-choose [role="tab"]{grid-template-columns:minmax(0,1fr); padding:16px}
  .st-choose [role="tab"] i,.st-choose [role="tab"][aria-selected="true"]::after{display:none}
  .st-choice{grid-column:1; grid-row:2}
}
@media (max-width:680px){
  .st-choose{grid-template-columns:minmax(0,1fr); gap:10px}
  .st-choose [role="tab"]{grid-template-columns:minmax(0,1fr) auto; min-height:64px}
  .st-choose [role="tab"] i{display:grid; transform:rotate(90deg)}
  .st-choose [role="tab"]:hover i{transform:rotate(90deg)}
  .st-choice{grid-template-columns:minmax(0,1fr)}
  .st-choice__img{min-height:0; aspect-ratio:3/2; order:-1}
}

/* the Club Hub: what is inside, beside three of its screens */
.st-hub{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(26px,4vw,60px); align-items:stretch}
.st-hub__list{display:flex; flex-direction:column; min-width:0}
.st-feats{list-style:none; margin:0 0 26px; padding:0; border-top:1px solid var(--line-dark)}
.st-feats li{margin:0; padding:13px 0; border-bottom:1px solid var(--line-dark)}
.st-feats b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.12rem; color:var(--mint); line-height:1.2; margin-bottom:3px}
.st-feats span{display:block; font-size:.96rem; color:rgba(255,255,255,.86); line-height:1.45}
.st-hub__list .btns{margin-top:auto}
.st-hub__desk{position:relative; display:flex; flex-direction:column; min-width:0}
.st-desk{position:relative; flex:1; min-width:0; min-height:470px}
.st-win{position:absolute; width:66%; padding:0; border:0; border-radius:14px; overflow:hidden; background:#fff; box-shadow:0 30px 60px -24px rgba(0,0,0,.7); cursor:zoom-in; transition:transform .35s var(--ease), box-shadow .35s; text-align:left; display:block}
.st-win:hover,.st-win:focus-visible{transform:rotate(0) scale(1.03); z-index:4; box-shadow:0 0 0 3px var(--mint), 0 30px 60px -24px rgba(0,0,0,.7)}
.st-win__bar{display:flex; align-items:center; gap:7px; height:30px; padding:0 12px; background:var(--aqua); font-family:var(--mono); font-size:.72rem; color:var(--slate); letter-spacing:.04em}
.st-win__bar i{width:9px; height:9px; border-radius:50%; background:rgba(29,65,78,.3); flex:none}
.st-win__bar i:last-of-type{margin-right:6px}
.st-win img{width:100%; aspect-ratio:1200/894; object-fit:cover; object-position:top}
.st-win--1{left:0; top:0; transform:rotate(-2.5deg); z-index:1}
.st-win--2{right:0; top:50%; margin-top:calc(-15px - 24.6%); transform:rotate(2deg); z-index:2}
.st-win--3{left:7%; bottom:0; transform:rotate(-1deg); z-index:3}
.st-desk__cap{position:absolute; right:0; bottom:0; width:24%; text-align:right; font-family:var(--mono); font-size:.72rem; line-height:1.5; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:900px){
  .st-hub{grid-template-columns:minmax(0,1fr)}
  .st-hub__list .btns{margin-top:0}
  .st-hub__desk{max-width:560px; width:100%}
  .st-desk{flex:none; min-height:0; aspect-ratio:1/1.04}
  .st-win{width:72%}
  .st-win--2{margin-top:calc(-15px - 26.8%)}
  .st-win--3{left:5%}
  .st-desk__cap{position:static; width:auto; margin-top:14px}
}

/* what a chapter does */
.st-do{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(26px,4vw,60px); align-items:stretch}
.st-do__photos{display:grid; grid-template-rows:repeat(2,minmax(0,1fr)); gap:var(--gap); min-width:0; min-height:540px}
.st-do__photos .st-fill{min-height:0}
.st-do__photos .st-fill:first-child > img{object-position:50% 38%}
.st-do__photos .st-fill:last-child > img{object-position:58% 50%}
.st-do__photos .sticker{left:auto; right:16px; bottom:auto; top:-14px}
.st-do__text{min-width:0; display:flex; flex-direction:column}
.st-do__text h2{margin-bottom:.45em}
.st-do__text > p{font-size:1.06rem; line-height:1.62}
.st-do__text .rows{margin-top:auto}
.st-do .row{padding:15px 4px; border-color:rgba(29,65,78,.2)}
.st-do .rows{border-color:rgba(29,65,78,.2)}
.st-do .row:hover{background:rgba(255,255,255,.5)}
.st-do .row b{display:flex; flex-wrap:wrap; align-items:center; gap:6px 10px; font-size:1.15rem}
.st-do .row b .chip{font-size:.7rem; background:var(--mint); border:1.5px solid var(--slate)}
.st-do .row small{font-size:.95rem}
.st-do .row .go{background:#fff}
.st-do .row:hover .go{background:var(--mint)}
@media (max-width:900px){.st-do{grid-template-columns:minmax(0,1fr); gap:0} .st-do__text{display:contents} .st-do__text h2{order:1} .st-do__photos{order:2; margin:6px 0 26px; min-height:0; grid-template-rows:none; grid-template-columns:repeat(2,minmax(0,1fr))} .st-do__text > p{order:3} .st-do__text .rows{order:4; margin-top:10px} .st-do__photos .st-fill{aspect-ratio:4/3}}
@media (max-width:560px){.st-do__photos{grid-template-columns:minmax(0,1fr)} .st-do__photos .st-fill{aspect-ratio:3/2}}

/* Hall of Fame */
.st-hof{display:grid; grid-template-columns:minmax(0,3fr) minmax(0,9fr); gap:clamp(26px,4vw,60px); align-items:center; margin:0}
.st-hof__img{position:relative}
.st-hof__img img{border-radius:var(--r-xl); width:100%; aspect-ratio:4/5; object-fit:cover; object-position:50% 18%; box-shadow:var(--shadow-soft)}
.st-hof__img .daisy{position:absolute; right:-18px; top:-18px; width:64px; height:64px; color:var(--mint)}
.st-hof__q{min-width:0}
.st-hof .eyebrow{margin-bottom:1.1rem}
.st-hof .quote{font-size:clamp(1.35rem,2.5vw,2.15rem); line-height:1.22}
.st-hof .quote::before{display:none}
.st-hof__by{display:grid; gap:3px; margin-top:22px; padding-left:18px; border-left:4px solid var(--mint)}
.st-hof__by b{font-family:var(--display); font-stretch:108%; font-size:1.2rem; line-height:1.2; color:#fff}
.st-hof__by span{font-size:.98rem; line-height:1.45; color:var(--aqua)}
@media (max-width:760px){.st-hof{grid-template-columns:minmax(0,1fr)} .st-hof__img{max-width:240px}}

/* two ways to reach the team: one anatomy, rows shared */
.st-contact{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(4,auto); gap:0 var(--gap)}
.st-contact > div{grid-row:span 4; display:grid; grid-template-rows:subgrid; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); box-shadow:var(--shadow-soft)}
.st-contact h3{font-size:1.45rem; margin:0 0 .4em}
.st-contact p{margin:0; font-size:1.02rem; color:var(--ink-soft)}
.st-contact__meta{display:flex; flex-wrap:wrap; gap:8px; align-items:center; min-height:40px; margin:18px 0 20px}
.st-contact__meta .chip{font-size:.76rem; padding:.5em .8em}
.st-contact .copy{font-size:.95rem; max-width:100%}
.st-contact .copy button{font-size:.76rem; padding:6px 10px; min-height:28px}
@media (pointer:coarse){.st-contact .copy button{min-height:44px; padding-inline:14px}}
@media (max-width:760px){.st-contact{grid-template-columns:minmax(0,1fr); grid-template-rows:none; gap:var(--gap)} .st-contact > div{grid-row:auto; grid-template-rows:none}}

/* register: the call, then the note for members of a club that is already registered. Both keep their actions in the same right-hand column. */
.st-creg{display:grid; gap:var(--gap)}
.st-creg > div{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,336px); gap:20px clamp(26px,4vw,60px); align-items:center; min-width:0; padding:clamp(24px,3.2vw,42px); border-radius:var(--r-xl)}
.st-creg .btns{display:grid; gap:12px}
.st-creg .btn{width:100%}
.st-creg__main{position:relative; overflow:hidden; background:var(--slate) var(--grain); color:#fff; box-shadow:var(--shadow-soft)}
.st-creg__main > *{position:relative; z-index:1}
.st-creg__main h2{margin-bottom:.35em}
.st-creg__main .lede{margin:0; color:rgba(255,255,255,.9)}
.st-creg__main .daisy-art{position:absolute; z-index:0; right:-70px; bottom:-170px; width:440px; color:var(--mint); opacity:.16}
.st-creg > .st-creg__side{background:#fff; color:var(--slate); padding-block:clamp(20px,2.4vw,30px)}
.st-creg__side h3{font-size:clamp(1.3rem,1.9vw,1.55rem); margin:0 0 .35em}
.st-creg__side p{margin:0; font-size:1.02rem; color:var(--ink-soft)}
@media (max-width:900px){.st-creg > div{grid-template-columns:minmax(0,1fr)} .st-creg .btns{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
'''

CLUB_JS = r'''<script>
(function(){
  /* the three choices are stacked on wide screens: up and down arrows move between them too */
  var tabs = [].slice.call(document.querySelectorAll('.st-choose [role="tab"]'));
  tabs.forEach(function(t, i){ t.addEventListener('keydown', function(e){ var n = e.key === 'ArrowDown' ? 1 : e.key === 'ArrowUp' ? -1 : 0; if(!n) return; e.preventDefault(); var nx = tabs[(i + n + tabs.length) % tabs.length]; nx.click(); nx.focus(); }); });
})();
</script>'''

def clubs():
    choices = [
        ('new', 'If there’s nothing like this at your school yet', 'Start a new chapter', 'Bring SafeBAE to your school for the first time',
         'Start a SafeBAE chapter from the ground up. Find an advisor, register your club, recruit your team, and use the Club Hub to plan meetings, activities, and events throughout the year.',
         'img-6834', 'A group of SafeBAE youth leaders together outdoors', '50% 45%'),
        ('affiliate', 'Student council, a wellness club, an affinity group', 'Affiliate an existing club', 'Bring SafeBAE into a club that’s already active',
         'Add SafeBAE to the work your club is already doing. Register as an affiliate, get access to the Club Hub, and use our activities, campaigns, and resources as part of your existing programming.',
         'img-9509-1', 'Students making hand-lettered consent posters', '50% 40%'),
        ('restart', 'If your school used to have one', 'Restart a previous chapter', 'Bring your school’s SafeBAE chapter back',
         'Pick up where a previous SafeBAE chapter left off. Re-register your chapter, reconnect with an advisor and students, and use the Club Hub to get meetings, activities, and events going again.',
         '000422', 'A large group of students in SafeBAE shirts on school steps', '48% 55%'),
    ]
    tabs = ''.join(f'<button role="tab" id="{k}" aria-controls="p-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><span>{esc(t)}</span><small>{esc(ifl)}</small><i aria-hidden="true">&rarr;</i></button>'
                   for i, (k, ifl, t, *_r) in enumerate(choices))
    panels = ''.join(f'''<div class="st-choice" role="tabpanel" id="p-{k}" aria-labelledby="{k}"{'' if i==0 else ' hidden'}>
      <div class="st-choice__body"><h3>{esc(tag)}</h3><p>{esc(d)}</p><p class="st-choice__foot">All three register through the same form and get the same Hub access and support. {a('Register below', '#register', 'link')}.</p></div>
      <figure class="st-choice__img">{img(im, alt, style='object-position:' + pos)}</figure></div>''' for i, (k, ifl, t, tag, d, im, alt, pos) in enumerate(choices))
    feats = [
        ('Find Your Next Action', 'Figure out what your chapter should do next.'),
        ('Awareness Event Library', 'Event ideas, plus tools for planning your year.'),
        ('Step-By-Step Guides', 'For running meetings and organizing events.'),
        ('Prevention Poster Builder', 'Create posters with your school’s support resources.'),
        ('Guides for Running Your Chapter', 'From finding an advisor and recruiting members to getting media attention and preparing the next group of leaders.'),
        ('And more', 'New tools, activities, and resources are added to the Club Hub throughout the year.'),
    ]
    feats_html = ''.join(f'<li><b>{esc(t)}</b><span>{esc(d)}</span></li>' for t, d in feats)
    wins = [('clubhub1', 'Find Your Next Action'), ('clubhub2', 'Awareness Event Library'), ('clubhub3', 'Build Your Calendar of Engagement')]
    wins_html = ''.join(f'<button class="st-win st-win--{i+1}" data-src="{imgsrc(n)}" data-cap="Club Hub: {esc(c)}" aria-label="Enlarge screenshot: {esc(c)}"><span class="st-win__bar"><i></i><i></i><i></i>clubs.safebae.org</span>{img(n, "Club Hub screen: " + c)}</button>' for i, (n, c) in enumerate(wins))

    def do_row(t, d, h, new=False):
        ext = h.startswith('http')
        tg = ' target="_blank" rel="noopener"' if ext else ''
        chip = '<span class="chip">New</span>' if new else ''
        return f'<a class="row" href="{esc(h)}"{tg}><span><b>{esc(t)}{chip}</b><small>{esc(d)}</small></span><span class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</span></a>'

    body = f'''
<section class="st-chero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      {crumbs(('Students', 'students.html'), ('SafeBAE Clubs', None))}
      <h1><span>Start a</span> <span>SafeBAE <span class="mk">club</span></span> <span>at your school</span></h1>
      <p class="lede">A SafeBAE club is a student-run chapter that brings consent and healthy relationship education to your school. You decide what your chapter does. We provide the training and materials, and our team is a quick email away when you need help. Registration is free.</p>
      <div class="btns">{btn('Register your club', CLUB_FORM, 'mint')}{btn('Already registered? Club Hub', CLUB_HUB, 'ghost')}</div>
    </div>
    <div class="st-cpair">
      <figure class="a">{img('clubhero', 'SafeBAE club members together at the beach', loading='eager')}</figure>
      <figure class="b">{img('img-1286', 'SafeBAE students in club shirts at the shore', loading='eager')}</figure>
      <span class="sticker" style="right:18px;top:-12px">Registration is free</span>
      <span class="sticker sticker--white sticker--r" style="right:-8px;bottom:9%">Renews each school year</span>
    </div>
  </div>
</section>

<section class="band band--paper" id="ways">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Three ways a club joins</p><h2>Which one fits your school?</h2><p class="lede lede--full">Start from scratch, restart a previous chapter, or add SafeBAE to a club you already run. The Club Hub walks you through each one step by step.</p></div></div>
    <div class="st-chooser reveal" data-tabs="clubway"><div class="st-choose" role="tablist" aria-label="Ways to join" aria-orientation="vertical">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="band band--slate" id="club-hub">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Members only</p><h2>Registering unlocks the Club Hub</h2><p class="lede lede--full">The Club Hub is the members-only site for registered SafeBAE chapters. Access is free and renews with your registration each school year.</p></div></div>
    <div class="st-hub reveal">
      <div class="st-hub__list">
        <p class="st-label">Inside, you’ll find</p>
        <ul class="st-feats">{feats_html}</ul>
        <div class="btns">{btn('Register to get access', CLUB_FORM, 'mint')}{btn('Open the Club Hub', CLUB_HUB, 'ghost')}</div>
      </div>
      <div class="st-hub__desk" data-gallery><div class="st-desk">{wins_html}</div><span class="st-desk__cap">Select a screen to enlarge</span></div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="chapters">
  <div class="wrap st-do reveal">
    <div class="st-do__photos">
      <figure class="st-fill">{img('club-table-nk-c', 'Students working on laptops around a table in a school library')}</figure>
      <figure class="st-fill">{img('clubtabling', 'A SafeBAE club table with red, yellow, and green flags, Can I Kiss You? buttons, and Vibe Check cards')}<span class="sticker">Can I kiss you?</span><figcaption>A SafeBAE club table with red, yellow and green flags, “Can I Kiss You?” buttons and Vibe Check cards.</figcaption></figure>
    </div>
    <div class="st-do__text">
      <h2>You decide what your chapter does</h2>
      <p>Meetings, awareness events, campaigns, posters for your school: your chapter sets the plan. Members get the Club Hub, virtual training sessions with the SafeBAE team, and free materials.</p>
      <p>After an event, send us photos and a couple of sentences. We share chapters’ work with clubs at other schools and on our social media, and we credit your club and school.</p>
      <div class="rows">
        {do_row('Get your leaders certified', 'The free Certified Peer Educator Training, 16 modules.', 'peer-educator.html')}
        {do_row('Practice in the BAE Skills Lab', 'Interactive activities for peer educators and club leaders.', 'skills-lab.html')}
        {do_row('Free prevention posters', 'Download and print for your school.', 'posters.html')}
        {do_row('Choking Hazard campaign', 'Free warning posters and the facts on sexual strangulation, which young people call “choking.”', 'choking-hazard.html', True)}
      </div>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <figure class="st-hof reveal">
      <div class="st-hof__img">{img('dorie', 'Dorie McNamara')}<span class="daisy" aria-hidden="true"></span></div>
      <div class="st-hof__q">
        <p class="eyebrow">From the Hall of Fame</p>
        <blockquote class="quote">“So many of my own friends had no idea what their rights are under Title IX… Starting the club and getting more students started on the training has made a great impact on not just myself but my entire Central community.”</blockquote>
        <figcaption class="st-hof__by"><b>Dorie McNamara</b><span>Former chapter lead and Certified Peer Educator at Central Catholic High School, now on SafeBAE’s Board of Directors</span></figcaption>
      </div>
    </figure>
  </div>
</section>

<section class="band band--paper" id="support">
  <div class="wrap">
    <div class="section-head"><div><h2>Questions, challenges or event ideas?</h2><p class="lede lede--full">Students and faculty advisors can both reach out to SafeBAE’s programming team.</p></div></div>
    <div class="st-contact reveal">
      <div><h3>Email the team</h3><p>Our team is a quick email away when you need help.</p>
        <div class="st-contact__meta"><span class="copy">{CLUB_EMAIL}<button data-copy="{CLUB_EMAIL}">Copy</button></span></div>
        <div class="btns">{btn('Email the team', 'mailto:' + CLUB_EMAIL, 'slate')}</div></div>
      <div><h3>Book a virtual meeting</h3><p>Pick a 30-minute slot with our programming team to talk through your chapter’s plans.</p>
        <div class="st-contact__meta"><span class="chip">30 minutes</span><span class="chip">Virtual</span></div>
        <div class="btns">{btn('Book a meeting', CALENDLY, 'slate')}</div></div>
    </div>
  </div>
</section>

<section class="band band--mint" id="register">
  <div class="wrap st-creg reveal">
    <div class="st-creg__main">
      <span class="daisy-art" aria-hidden="true"></span>
      <div>
        <h2>Registration takes a few minutes</h2>
        <p class="lede">It’s free and renews each school year. Once you register, you’ll get access to the Club Hub and be connected with your point of contact on the SafeBAE team.</p>
      </div>
      <div class="btns">{btn('Register your club', CLUB_FORM, 'mint')}{btn('Already registered? Club Hub', CLUB_HUB, 'ghost')}</div>
    </div>
    <div class="st-creg__side">
      <div>
        <h3>Joining a club that’s already registered?</h3>
        <p>You don’t need to register the club again. Create your own Club Hub account instead. Need help? Email {a(CLUB_EMAIL, 'mailto:' + CLUB_EMAIL, 'link')}.</p>
      </div>
      <div class="btns">{btn('Create a Club Hub account', CLUB_HUB, 'teal')}</div>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><h2>From learning to changing policy</h2><p class="lede lede--full">In college? {a('Start a SafeBAE club on your campus', 'college.html', 'link')} and mentor high school chapters.</p></div></div>
    {journey('Lead')}
  </div>
</section>
{give_band()}
'''
    page('clubs.html', 'SafeBAE Clubs · SafeBAE', 'Start a student club and lead sexual violence prevention at your school. Access free resources, trainings, and a national network of student leaders.',
         body, active='students', body_class='st st-clubs', head_extra=f'<style>{CSS}{CLUB_CSS}</style>', scripts=CLUB_JS)


# ================================================================= reform-policy.html
RP_CSS = '''
/* hero */
.st-rhero{--wm-o:.2; background:var(--aqua); color:var(--slate); position:relative; overflow:hidden}
.st-rhero .wm-daisy{color:var(--logo-teal)}
.st-rhero :focus-visible{outline-color:var(--teal)}
.st-rhero .crumbs{color:var(--ink-soft)} .st-rhero .crumbs a{color:var(--logo-teal)}
.st-rhero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,84px)}
.st-rhero h1{font-size:clamp(2.1rem,3.62vw,3.25rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.95; letter-spacing:-.02em; margin-bottom:.45em; text-wrap:wrap}
.st-rhero h1 > span{display:block}
.st-rhero .lede{max-width:none}
.st-cover{position:relative; width:min(80%,380px); margin-inline:auto; animation:sb-rise-r 1s .1s var(--ease) both}
.st-cover img{width:100%; border-radius:8px; transform:rotate(3deg); box-shadow:0 34px 60px -24px rgba(22,53,64,.6), 0 0 0 1px rgba(29,65,78,.12); transition:transform .4s var(--ease)}
.st-cover:hover img{transform:rotate(1deg) translateY(-4px)}
.st-cover .sticker{position:absolute; left:-18px; bottom:12%}
@media (max-width:900px){.st-rhero > .wrap{grid-template-columns:minmax(0,1fr)} .st-cover{width:min(64%,260px); margin:6px 0 0 14px}}

/* the swing: which way federal protections moved, 2020 to now (direction only, no values).
   Each point sits on the left text edge of the card that explains it. */
.st-swing{--pt:var(--pad-card); --col:calc((100% - 2 * var(--gap)) / 3); display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0 var(--gap)}
.st-swing__plot{grid-column:1/-1; position:relative; height:clamp(210px,19vw,260px)}
.st-swing__axis{position:absolute; left:0; top:0; margin:0; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua)}
.st-swing__axis--r{left:auto; right:0; color:rgba(209,254,255,.7); font-weight:500}
.st-swing__lvl{position:absolute; left:0; right:0; height:0; border-top:1px dashed rgba(209,254,255,.26)}
.st-swing__lvl span{position:absolute; right:0; bottom:8px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:rgba(209,254,255,.8); white-space:nowrap}
.st-swing__lvl--hi{top:26%}
.st-swing__lvl--lo{top:72%}
.st-swing__box{position:absolute; top:0; bottom:0; left:calc(var(--pt) + 11px); right:calc(var(--col) - var(--pt) - 11px)}
.st-swing__ink{position:absolute; inset:0; clip-path:inset(-60px -100vw -60px -60px); transition:clip-path 1.5s .15s cubic-bezier(.5,.1,.3,1)}
.st-swing__ink svg{position:absolute; inset:0; width:100%; height:100%; overflow:visible}
.st-swing .up{fill:none; stroke:var(--mint); stroke-width:6; stroke-linecap:round}
.st-swing .down{fill:none; stroke:var(--aqua); stroke-width:6; stroke-linecap:round; stroke-dasharray:1 15}
.st-swing .wash{fill:rgba(21,255,200,.07); stroke:none}
.st-swing__tail{position:absolute; top:72%; right:0; width:calc(var(--col) - var(--pt) - 11px - 16px); height:0; margin-top:-3px; border-top:6px dotted rgba(209,254,255,.4); transform-origin:0 50%; transition:transform .6s 1.5s var(--ease)}
.st-swing__stem{position:absolute; bottom:0; width:0; margin:12px 0 0 -1px; border-left:2px dashed rgba(209,254,255,.42); transform-origin:50% 0; transition:transform .5s var(--ease); transition-delay:var(--d,0s)}
.st-swing__pt{position:absolute; width:0; height:0; transition:transform .5s var(--ease); transition-delay:var(--d,0s)}
.st-swing__pt::before{content:""; position:absolute; left:-12px; top:-12px; width:24px; height:24px; border-radius:50%; background:var(--slate); border:6px solid var(--mint); box-sizing:border-box}
.st-swing__pt--alt::before{border-color:var(--aqua)}
.st-swing__pt b{position:absolute; left:-12px; white-space:nowrap; font-family:var(--mono); font-size:.76rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; line-height:1; color:var(--slate); background:var(--mint); padding:7px 10px; border-radius:8px; z-index:1}
.st-swing__pt--alt b{background:var(--aqua)}
.st-swing__pt b i{font-style:normal; display:none}
.st-swing__pt--lo b{top:24px}
.st-swing__pt--hi b{bottom:24px}
.js .st-swing.reveal.pre .st-swing__ink{clip-path:inset(-60px 100% -60px -60px)}
.js .st-swing.reveal.pre .st-swing__pt{transform:scale(.4)}
.js .st-swing.reveal.pre .st-swing__stem{transform:scaleY(0)}
.js .st-swing.reveal.pre .st-swing__tail{transform:scaleX(0)}
.st-swing__col{position:relative; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark)}
.st-swing__col > b{display:block; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2rem,3.2vw,2.8rem); line-height:1; letter-spacing:-.02em; color:var(--mint); margin-bottom:12px}
.st-swing__col h3{color:#fff; font-size:1.3rem; margin-bottom:.45em}
.st-swing__col p{margin:0; color:rgba(255,255,255,.84); font-size:.98rem; line-height:1.55}
@media (max-width:860px){
  .st-swing{grid-template-columns:minmax(0,1fr); gap:14px}
  .st-swing__plot{height:190px; margin:52px 0 6px}
  .st-swing__axis{top:-52px} .st-swing__axis--r{left:0; right:auto; top:-30px}
  .st-swing__box{left:14px; right:14px}
  .st-swing__tail,.st-swing__stem,.st-swing__lvl span{display:none}
  .st-swing__pt b i{display:inline}
  .st-swing__pt--mid b{left:50%; transform:translateX(-50%)}
  .st-swing__pt--end b{left:auto; right:-12px}
  .st-swing__axis{font-size:.7rem}
}
.st-strong{margin-top:var(--gap); padding:var(--pad-card); border-radius:var(--r-xl); background:var(--mint); color:var(--slate); display:flex; flex-wrap:wrap; gap:16px 40px; align-items:center; justify-content:space-between}
.st-strong p{flex:1 1 420px; margin:0; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.25rem,1.95vw,1.62rem); line-height:1.18; text-wrap:balance}

/* four steps, two by two, on one track */
.st-steps4{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.st-steps4 li{position:relative; margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); display:grid; grid-template-columns:52px minmax(0,1fr); gap:0 18px; align-items:start; align-content:center; min-width:0}
.st-steps4 li:nth-child(odd)::after{content:""; position:absolute; z-index:1; top:50%; margin-top:-2px; left:100%; width:var(--gap); height:4px; background:var(--teal)}
.st-steps4 .n{grid-row:1/3; align-self:center; width:52px; height:52px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.5rem}
.st-steps4 h3{grid-column:2; font-size:1.3rem; margin:0 0 5px}
.st-steps4 p{grid-column:2; margin:0; color:var(--ink-soft); font-size:1rem; line-height:1.55}
@media (max-width:760px){
  .st-steps4{grid-template-columns:minmax(0,1fr); gap:14px}
  .st-steps4 li:nth-child(odd)::after{display:none}
  .st-steps4 li:not(:last-child)::after{content:""; display:block; position:absolute; top:100%; margin:0; left:calc(var(--pad-card) + 24px); width:4px; height:14px; background:var(--teal)}
}
.st-who{margin-top:var(--gap); display:grid; grid-template-columns:auto auto minmax(0,1fr); gap:12px clamp(18px,2.6vw,36px); align-items:center; padding:20px var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line)}
.st-who__k{margin:0; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.15rem; color:var(--logo-teal); white-space:nowrap}
.st-who .chip{font-size:.78rem; padding:.5em .85em}
.st-who > p:last-child{margin:0; font-size:1.02rem}
@media (max-width:900px){.st-who{grid-template-columns:minmax(0,1fr)}}

/* Title IX panel beside the next places to go */
.st-rights{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.st-rights__panel{display:flex; flex-direction:column; min-width:0; padding:clamp(24px,3.2vw,42px); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.st-tix{flex:1; display:grid; align-content:stretch; margin:0; border-top:1px solid var(--line-dark)}
.st-tix > div{padding:16px 0; border-bottom:1px solid var(--line-dark)}
.st-tix h3{margin:0 0 6px; font-size:1.3rem; font-stretch:104%; line-height:1.2; color:var(--mint)}
.st-tix p{margin:0; font-size:1.04rem; line-height:1.55; color:rgba(255,255,255,.88)}
.st-rights__panel .btns{margin-top:auto; padding-top:26px}
.st-rights__more{display:grid; grid-auto-rows:1fr; gap:12px; min-width:0}
.st-rights + .helpline{margin-top:var(--gap)}
@media (max-width:1180px){.st-rights{grid-template-columns:minmax(0,1fr)} .st-rights__more{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:700px){.st-rights__more{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto}}
'''

def reform_policy():
    cover_alt = 'Cover of the SafeBAE Sexual Misconduct Policy Reform Guide: A Guide for Students in How to Create a Model Policy, 2024 update'
    chart_alt = 'Federal Title IX protections for survivors were narrowed in 2020, restored by new guidelines in 2024, then challenged in court, leaving schools back under the 2020 rule.'
    steps = [
        ('Register', f'Fill out the {a("short form below", "#register", "link")} to receive the guide.'),
        ('Get the guide and adjoining resources', 'Free access to the guide, a resource for students on how to create a model policy.'),
        ('Advocate in your district', 'Use the guide to push for clarity, accountability, and real protection in your schools.'),
        ('Keep in touch', 'Let SafeBAE know about your progress as you work with your school or district.'),
    ]
    steps_html = ''.join(f'<li><span class="n">{i+1}</span><h3>{esc(t)}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))
    more = [
        ('Learn it in the Peer Educator Training', 'Module 10 covers reporting options and investigation requirements; Module 11 covers your rights in school.', 'peer-educator.html#modules'),
        ('Organize with a SafeBAE club', 'Campaigns, events and support from the Club Hub.', 'clubs.html'),
        ('Policy Reform at the Summer Activist Institute', 'Title IX and Policy Reform were sessions at the 2024 institute.', 'summer-institute.html#schedule'),
        ('Bring policy support to your school', 'SafeBAE 360° Schools, our whole-school approach, includes hands-on policy consultation.', '360-schools.html'),
    ]
    more_html = ''.join(tile(t, d, h) for t, d, h in more)
    body = f'''
<section class="st-rhero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      {crumbs(('Students', 'students.html'), ('Reform Your School’s Policy', None))}
      <p class="eyebrow">Student Policy Reform Guide</p>
      <h1><span><span class="mk">Reform</span> your</span> <span>school’s sexual</span> <span>misconduct</span> <span>policy</span></h1>
      <p class="lede">Protecting your school community starts with strong, trauma-informed policies. SafeBAE’s Student Policy Reform Guide is a step-by-step resource to help you advocate for safer, trauma-informed and survivor-centered policies in your district.</p>
      <div class="btns">{btn('Register for the guide', '#register', 'slate', arrow=True)}{btn('Know your Title IX rights', 'title-ix.html', 'ghost')}</div>
    </div>
    <div class="st-cover">{img('2024-updates-safebae-sexual-misconduct-policy-reform-a-stude', cover_alt, loading='eager')}<span class="sticker">Free for students</span></div>
  </div>
</section>

<section class="band band--slate" id="shifting">
  <div class="wrap">
    <div class="section-head"><div><h2>Federal protections keep <span class="mk">shifting</span></h2><p class="lede lede--full">Since 2020, shifting federal Title IX rules have left survivors vulnerable and school districts facing legal risk.</p></div></div>
    <div class="st-swing reveal">
      <div class="st-swing__plot" role="img" aria-label="{esc(chart_alt)}">
        <p class="st-swing__axis" aria-hidden="true">&uarr; Federal protections for survivors</p><p class="st-swing__axis st-swing__axis--r" aria-hidden="true">Direction only, not to scale</p>
        <span class="st-swing__lvl st-swing__lvl--hi" aria-hidden="true"><span>Stronger</span></span>
        <span class="st-swing__lvl st-swing__lvl--lo" aria-hidden="true"><span>The 2020 rule</span></span>
        <div class="st-swing__box" aria-hidden="true">
          <div class="st-swing__ink"><svg viewBox="0 0 1000 200" preserveAspectRatio="none"><path class="wash" d="M0,144 C190,144 310,52 500,52 C690,52 810,144 1000,144 Z"/><path class="up" d="M0,144 C190,144 310,52 500,52" vector-effect="non-scaling-stroke"/><path class="down" d="M500,52 C690,52 810,144 1000,144" vector-effect="non-scaling-stroke"/></svg></div>
          <span class="st-swing__stem" style="left:0;top:72%;--d:.1s"></span><span class="st-swing__stem" style="left:50%;top:26%;--d:.7s"></span><span class="st-swing__stem" style="left:100%;top:72%;--d:1.3s"></span>
          <span class="st-swing__pt st-swing__pt--lo" style="left:0;top:72%"><b><i>2020 &middot; </i>Narrowed</b></span>
          <span class="st-swing__pt st-swing__pt--hi st-swing__pt--mid" style="left:50%;top:26%;--d:.6s"><b><i>2024 &middot; </i>Restored</b></span>
          <span class="st-swing__pt st-swing__pt--lo st-swing__pt--alt st-swing__pt--end" style="left:100%;top:72%;--d:1.2s"><b><i>Now &middot; </i>Pushed back</b></span>
        </div>
        <span class="st-swing__tail" aria-hidden="true"></span>
      </div>
      <article class="st-swing__col"><b>2020</b><h3>A harmful Title IX rule</h3><p>The 2020 Title IX rule issued by the Department of Education was widely recognized as harmful. It narrowed protections for survivors, restricted schools’ ability to respond effectively, and put students at greater risk of further harm.</p></article>
      <article class="st-swing__col"><b>2024</b><h3>New guidelines, challenged in court</h3><p>New guidelines were introduced in 2024 to restore protections. They were quickly challenged in court, and schools nationwide have been forced back under the restrictive 2020 rule.</p></article>
      <article class="st-swing__col"><b>Now</b><h3>Weak, inconsistent enforcement</h3><p>With the Department of Education weakened and inconsistent in its enforcement, survivors are left vulnerable and districts face heightened legal risks due to vague and harmful federal standards.</p></article>
    </div>
    <div class="st-strong reveal"><p>Together, we can strengthen protections for students and make schools safer across the country.</p>{btn('Register for the guide', '#register', 'slate', arrow=True)}</div>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><h2>A step&#8209;by&#8209;step guide for students</h2><p class="lede lede--full">SafeBAE created the Student Policy Reform Guide to help you advocate for safer, trauma-informed, and survivor-centered policies in your district.</p></div></div>
    <ol class="st-steps4 reveal" aria-label="How it works">{steps_html}</ol>
    <div class="st-who reveal"><p class="st-who__k">Who can use it</p>{chips(['Students', 'Parents', 'Community stakeholders'], 'slate')}<p>Use it to push for clarity, accountability, and real protection in your schools.</p></div>
  </div>
</section>

<section class="band band--deep" id="register">
  <div class="wrap st-reg">
    <div class="st-reg__side">
      <div class="st-reg__head">
        <p class="eyebrow">Free for students</p>
        <h2>Register to get the guide</h2>
        <p class="lede">We ask only that you register to receive the guide and keep in touch with us about your progress.</p>
      </div>
      <div class="st-reg__links st-reg__links--one">{tile('Administrator, teacher or district leader?', 'SafeBAE has a separate School Policy Reform Guide for administrators.', 'policy-reform-guide.html')}</div>
    </div>
    <div class="st-reg__form">{form_card(POLICY_FORM + '?embedded=true', POLICY_FORM, 'Student registration form', 'Register to receive the Student Policy Reform Guide', 'Open the form', 1100, 'Student Policy Reform Guide registration')}</div>
  </div>
</section>

<section class="band band--paper" id="title-ix">
  <div class="wrap">
    <div class="section-head"><div><h2>Know your rights under Title IX</h2><p class="lede lede--full">Title IX is the federal law that bars sex discrimination, including sexual harassment and assault, at any school that takes federal funding.</p></div></div>
    <div class="st-rights reveal">
      <div class="st-rights__panel">
        <div class="st-tix">
          <div><h3>Know your rights</h3><p>Your right to report, to supportive measures like a schedule change, and to a prompt, fair investigation.</p></div>
          <div><h3>Find your coordinator</h3><p>Learn whether your school is covered by Title IX, and how to find your school’s Title IX Coordinator.</p></div>
          <div><h3>Understand and change your school’s policy</h3><p>What your school’s sexual misconduct policy says, what a strong one should include, and how to advocate for change.</p></div>
        </div>
        <div class="btns">{btn('Title IX basics', 'title-ix.html', 'mint', arrow=True)}{btn('Get the guide', '#register', 'ghost')}</div>
      </div>
      <div class="st-rights__more">{more_html}</div>
    </div>
    {st_help()}
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Where policy change fits</h2></div></div>
    {journey('Change')}
  </div>
</section>
{give_band()}
'''
    page('reform-policy.html', 'Reform Your School’s Policy · SafeBAE', 'Advocate for school policy reform on sexual violence. Learn how to reform Title IX and misconduct policies with SafeBAE’s student-led guide.',
         body, active='students', body_class='st st-reform', head_extra=f'<style>{CSS}{RP_CSS}</style>')


# ================================================================= summer-institute.html
F2025 = ['Adrian Alie', 'Alan Mejia', 'Armando Refcalbo', 'Ava Maldonado', 'Ava Ram', 'Brianna Benitev', 'Cayden Michaud', 'Cyra Wuthrich',
         'David Zamora', ('Dolly Barrat', 'dolly-barratt'), 'Edwinah Magloire', 'Elle Mone', ('Isaac Smith NJ', 'isaac-smith-nj'), 'Isabella Cabral', 'Jaclyn Verde',
         'Jada Davis', 'Jada Martinez', 'Luisa Palomares', 'Mimi Ndiaye', 'Molly Pines', 'Nick Niedbalski', 'Riley Devereaux', 'Skyla Vivar Rosado',
         'Sophia Nguyen', ('Summer Wilson NJ', 'summer-wilson-nj'), 'Sunny Brynildsen', 'Yareli Huerta']
F2025 = [(x, re.sub(r'[^a-z0-9]+', '-', x.lower())) if isinstance(x, str) else x for x in F2025]
F2024 = [('Lilliana Katz-Hollander', 'lilliana-kh', 'she/her'), ('Anna Yang', 'anna-yang', ''), ('Apollo Knapp', 'apollo-knapp-headshot', 'He/They'),
         ('Arturo Rosado Taveras', 'arturo-rosadot', 'Also a 2023 fellow'), ('August Chandler', 'august-chandler', ''), ('Cole Firshein', 'cole-firshein', ''),
         ('Matteo Netto', 'matteo-netto', ''), ('Kaylee Cuevas', 'kaylee-cuevas', ''), ('Anna Diegnan', 'anna-deignan', ''),
         ('Lucy Wells-Davies', 'lucy-wells-davies-headshot', 'she/her'), ('Mara Scott', 'mara-scott', ''), ('Jada Metcalf', 'jada-metcalf-headshot', 'she/they'),
         ('Taniyah Jackson', 'taniyah-jackson', ''), ('Tristan Greene', 'tristan-greene-headshot', 'he/him'), ('Val Odiembo', 'val-odiembo', '')]
F2023 = [('Alison Chang', 'alison-chang-headshot-alison-chang', ''), ('Arturo Rosado Taveras', 'ca49ee25-ce60-4a29-ad70-3a3b48de9d32-arturo-rosado', 'Also a 2024 fellow'),
         ('Ava Dare', '3d9b25eb-3bc8-4f20-b5f9-c33b417a21cf-ava-dare', ''), ('Britney Cunningham', 'img-4121-britney-cunningham', ''),
         ('Cathy Williams', '30125793-52af-484d-8046-f75d312bcfbe-cathy-w', ''), ('Claudia Cham', 'img-8130-claudia-kulee-cham', ''),
         ('Dorie McNamara', '878c21b1-e5e6-4cea-8b5a-bfa7808d2636-dorie-mcnamara', ''), ('Enetu Nelson', 'img-1031-enetu-nelson', ''),
         ('Hector Jaco', 'img-8426-hector-jaco', ''), ('Inanna Balkin', 'img-7930-inanna-balkin', ''), ('Isabella Ocejo', 'img-5684-isabella-ocejo', ''),
         ('Jully Myrthil', 'img-5326-jully-m', ''), ('Maria Muntean', 'mariamuntean-maria-muntean', ''), ('Mia (Mimi) Stewart', 'renderedimage-mia-stewart', ''),
         ('Mica Ormeno', 'img-8576-micaela-ormeno', '')]
assert len(F2025) == 27 and len(F2024) == 15 and len(F2023) == 15  # the portrait grids are laid out for exactly these counts

SI_CSS = '''
/* hero: the fellows in session, in original colour */
.st-ihero{position:relative; overflow:hidden; background:var(--slate) var(--grain); color:#fff}
.st-ihero > .wrap{position:relative; z-index:1; padding-block:clamp(48px,6vw,84px); display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(28px,5vw,64px); align-items:center}
.st-ihero h1{font-size:clamp(2.6rem,5.4vw,5.2rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.88; letter-spacing:-.02em; margin:0 0 .35em}
.st-ihero h1 > span{display:block}
.st-ihero .mk{background:none; color:var(--mint)}
.st-ihero .lede{color:rgba(255,255,255,.9); max-width:none}
.st-count{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin-top:28px}
.st .st-count a{display:flex; flex-direction:column; justify-content:space-between; gap:10px; min-height:92px; padding:14px 14px 12px; border-radius:14px; border:2px solid rgba(209,254,255,.3); text-decoration:none; color:#fff; transition:border-color .2s, background .2s, transform .25s var(--ease)}
.st .st-count a:hover{border-color:var(--mint); background:rgba(21,255,200,.08); transform:translateY(-3px)}
.st-count b{font-family:var(--display); font-weight:900; font-stretch:120%; font-size:2.1rem; line-height:1; color:var(--mint); font-variant-numeric:tabular-nums}
.st-count b svg{width:.8em; height:.8em; display:block; margin:.1em 0}
.st-count span{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; line-height:1.35}
.st-ihero__photo{position:relative; margin:0; animation:sb-rise-r 1s .1s var(--ease) both}
.st-ihero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:62% 0; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.st-ihero__photo .sticker{position:absolute; left:-14px; bottom:22px}
@media (max-width:900px){.st-ihero > .wrap{grid-template-columns:minmax(0,1fr)} .st-ihero__photo{max-width:560px} .st-ihero__photo .sticker{left:10px}}
@media (max-width:520px){.st-count{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* the fellows: even walls of portraits, one per year */
.st-si .section-head .tabs{margin:0; max-width:100%}
@media (max-width:760px){.st-si .section-head .tabs{flex:1 1 100%!important}}
.st-si .tab{min-height:44px; display:inline-flex; align-items:center; gap:.5em; scroll-margin-top:170px}
.st-si .tab small{font-family:var(--mono); font-size:.76rem; font-weight:600; opacity:.8}
.st-fgrid{display:grid; grid-template-columns:repeat(9,minmax(0,1fr)); gap:24px 14px; list-style:none; padding:0; margin:0}
.st-fgrid--16{grid-template-columns:repeat(8,minmax(0,1fr)); gap:24px 16px}
.st-fellow{margin:0; min-width:0; animation:st-pop .5s var(--ease) both; animation-delay:calc(var(--i,0) * 14ms)}
@keyframes st-pop{from{transform:translateY(14px) scale(.95)}}
.st-fellow__img{display:block; aspect-ratio:4/5; border-radius:14px; overflow:hidden; background:var(--mist); margin-bottom:10px; transition:transform .3s var(--ease), box-shadow .3s}
.st-fellow__img img{width:100%; height:100%; object-fit:cover; object-position:center 28%}
.st-fellow:hover .st-fellow__img{transform:translateY(-4px) rotate(-1.5deg); box-shadow:0 0 0 3px var(--mint), 0 18px 30px -18px rgba(0,0,0,.5)}
.st-fellow b{display:block; font-family:var(--display); font-stretch:104%; line-height:1.2; font-size:.98rem; overflow-wrap:break-word}
.st-fellow small{display:block; color:var(--ink-soft); font-size:.875rem; line-height:1.3; margin-top:3px}
.st-fellow small.ret{color:var(--logo-teal); font-weight:700}
.st .st-fellow--more a{display:flex; flex-direction:column; justify-content:space-between; gap:6px; aspect-ratio:4/5; overflow:hidden; border-radius:14px; padding:14px 13px; background:var(--slate) var(--grain); color:#fff; text-decoration:none; transition:transform .3s var(--ease), box-shadow .3s}
.st .st-fellow--more a:hover{transform:translateY(-4px) rotate(-1.5deg); box-shadow:0 0 0 3px var(--mint), 0 18px 30px -18px rgba(0,0,0,.5)}
.st-fellow--more span{font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.5rem; line-height:1; letter-spacing:-.02em; color:var(--mint)}
.st-fellow--more b{font-size:1rem; line-height:1.2}
.st-fellow--more i{font-style:normal; display:inline-block; color:var(--mint); transition:transform .25s var(--ease)}
.st-fellow--more a:hover i{transform:translateX(4px)}
@media (max-width:1199px){.st-fgrid--27{gap:22px 12px} .st-fgrid--27 .st-fellow b{font-size:.9rem}}
@media (max-width:999px){
  .st-fgrid--27{grid-template-columns:repeat(12,minmax(0,1fr)); gap:22px 14px}
  .st-fgrid--27 .st-fellow b{font-size:.98rem}
  .st-fgrid--27 > li{grid-column:span 2}
  .st-fgrid--27 > li:nth-child(25){grid-column:4 / span 2}
}
@media (max-width:999px){.st-fgrid--16{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:619px){
  .st-fgrid,.st-fgrid--27,.st-fgrid--16{grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px 10px}
  .st-fgrid--27 > li,.st-fgrid--27 > li:nth-child(25){grid-column:auto}
  .st-fellow b{font-size:.92rem}
  .st-fgrid--16 .st-fellow--more{grid-column:1/-1}
  .st .st-fellow--more a{aspect-ratio:auto; flex-direction:row; align-items:center; min-height:64px; padding:12px 16px}
  .st-fellow--more span{flex:none}
  .st-fellow--more b{flex:1}
}

/* two days: the running order beside the institute's own poster */
.st-sched{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(26px,4vw,60px); align-items:stretch}
.st-day{list-style:none; margin:0; padding:0; display:grid; grid-auto-rows:minmax(52px,1fr); border-top:1px solid var(--line-dark); min-width:0}
.st-day li{position:relative; display:grid; grid-template-columns:112px minmax(0,1fr) auto; gap:6px 16px; align-items:center; padding:8px 0 8px 22px; border-bottom:1px solid var(--line-dark); margin:0}
.st-day li::before{content:""; position:absolute; left:0; top:50%; width:10px; height:10px; margin-top:-5px; border-radius:50%; background:var(--mint)}
.st-day li.meal::before{background:transparent; box-shadow:inset 0 0 0 2px rgba(209,254,255,.45)}
.st-day time{font-family:var(--mono); font-size:.92rem; font-weight:600; color:var(--mint); white-space:nowrap}
.st-day b{font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.2}
.st-day li.meal b{font-family:var(--body); font-weight:500; font-size:1.02rem; color:rgba(255,255,255,.76)}
.st-day li.meal time{color:var(--aqua)}
.st-day .t{display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end}
.st-day .t span{font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; padding:5px 8px; border-radius:6px; border:1px solid rgba(209,254,255,.35); color:var(--aqua); white-space:nowrap}
.st .st-day .t a{font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; padding:6px 9px; border-radius:6px; background:var(--mint); color:var(--slate); text-decoration:none; white-space:nowrap}
.st .st-day .t a:hover{background:#fff}
.st-sched__poster{display:flex; align-items:center; justify-content:center; min-width:0}
.st-poster{display:block; width:100%; border:0; padding:0; background:none; cursor:zoom-in; border-radius:16px; overflow:hidden; box-shadow:0 30px 60px -28px rgba(0,0,0,.7); transform:rotate(2deg); transition:transform .3s var(--ease)}
.st-poster:hover,.st-poster:focus-visible{transform:rotate(0) scale(1.02)}
.st-poster img{width:100%}
@media (max-width:900px){.st-sched{grid-template-columns:minmax(0,1fr)} .st-poster{max-width:340px} .st-sched__poster{justify-content:flex-start; padding-left:6px}}
@media (max-width:620px){.st-day{grid-auto-rows:auto} .st-day li{grid-template-columns:86px minmax(0,1fr); padding:12px 0 12px 20px} .st-day li::before{top:24px; margin-top:-5px} .st-day .t{grid-column:2; justify-content:flex-start} .st-day time{font-size:.88rem} .st .st-day .t a{display:inline-flex; align-items:center; min-height:44px; padding-inline:12px}}

/* episode: the film beside the cohort that made it */
.st-ep{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.st-ep .vid{border-radius:var(--r-xl)}
.st-ep .st-fill > img{object-position:50% 40%}
@media (max-width:900px){.st-ep{grid-template-columns:minmax(0,1fr)}}
'''

SCHED = {
  'tue': ('Tuesday, June 25', '24sumact', [
      ('8:30 AM', 'Yoga', [], 1), ('9:20 AM', 'Breakfast', [], 0), ('10:35 AM', 'Introductions & Self Care', [], 1), ('11:10 AM', 'Theories of Change', ['Group debrief'], 1),
      ('12:30 PM', 'Lunch', [], 0), ('1:35 PM', 'Title IX', ['Group debrief', ('Title IX', 'title-ix.html')], 1), ('2:55 PM', 'Sex Education', ['Break'], 1),
      ('4:50 PM', 'Professional Development', ['Break'], 1), ('6:00 PM', 'Dinner', [], 0), ('7:00 PM', 'Fun Activity!', [], 1)]),
  'wed': ('Wednesday, June 26', '24sumact2', [
      ('8:30 AM', 'Lighthouse Walk', [], 1), ('9:20 AM', 'Breakfast', ['Group debrief'], 0), ('11:10 AM', 'Centering the Margins', ['Break'], 1),
      ('12:20 PM', 'Storytelling for Change', [], 1), ('1:30 PM', 'Lunch/Break', [], 0), ('2:35 PM', 'Policy Reform', ['Break', ('Guide', 'reform-policy.html')], 1),
      ('4:00 PM', 'Engaging Men in the Convo', ['Break & debrief'], 1), ('5:45 PM', 'Self Care (part 2)', [], 1), ('6:00 PM', 'Dinner', [], 0), ('7:00 PM', 'Fun Activity!', [], 1)]),
}

# where the face sits in each portrait that is not a centred headshot (x y of object-position)
FACE_POS = {'lilliana-kh': 'center 20%', 'arturo-rosadot': 'center 12%', 'matteo-netto': 'center 20%', 'mara-scott': '24% center', 'tristan-greene-headshot': 'center 45%',
            'taniyah-jackson': 'center 40%', 'alison-chang-headshot-alison-chang': '80% 30%', 'ca49ee25-ce60-4a29-ad70-3a3b48de9d32-arturo-rosado': 'center 12%',
            '30125793-52af-484d-8046-f75d312bcfbe-cathy-w': 'center 35%', 'img-4121-britney-cunningham': '52% center', 'img-8130-claudia-kulee-cham': 'center 15%',
            'img-8426-hector-jaco': '0% center', 'img-8576-micaela-ormeno': 'center 46%'}

def fellow_card(i, name, slug, note=''):
    pos = FACE_POS.get(slug)
    st = f'object-position:{pos}' if pos else ''
    cls = ' class="ret"' if note.startswith('Also') else ''
    return (f'<li class="st-fellow" style="--i:{i}"><span class="st-fellow__img">{img(slug, name, style=st)}</span><b>{esc(name)}</b>'
            + (f'<small{cls}>{esc(note)}</small>' if note else '') + '</li>')

def more_card(i, kicker, label, href):
    return f'<li class="st-fellow st-fellow--more" style="--i:{i}"><a href="{href}"><span>{esc(kicker)}</span><b>{esc(label)} <i aria-hidden="true">&rarr;</i></b></a></li>'

PLAY_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 3v18l16-9z"/></svg>'

def summer_institute():
    p25 = ''.join(fellow_card(i, n.replace(' NJ', ''), s, 'NJ' if n.endswith(' NJ') else '') for i, (n, s) in enumerate(F2025))
    p24 = ''.join(fellow_card(i, *f) for i, f in enumerate(F2024)) + more_card(15, '2024', 'See the two-day schedule', '#schedule')
    p23 = ''.join(fellow_card(i, *f) for i, f in enumerate(F2023)) + more_card(15, '2023', 'Watch an episode', '#episode')
    cohorts = [('f2025', '2025 Fellows', p25, 'st-fgrid--27', len(F2025)), ('f2024', '2024 Fellows', p24, 'st-fgrid--16', len(F2024)), ('f2023', '2023 Fellows', p23, 'st-fgrid--16', len(F2023))]
    tabs = ''.join(f'<button class="tab" role="tab" id="{k}" aria-controls="p-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(lbl)} <small>{n}</small></button>' for i, (k, lbl, _p, _c, n) in enumerate(cohorts))
    panels = ''.join(f'<div role="tabpanel" id="p-{k}" aria-labelledby="{k}"{"" if i==0 else " hidden"}><ul class="st-fgrid {c}">{p}</ul></div>' for i, (k, lbl, p, c, n) in enumerate(cohorts))

    def day_rows(rows):
        out = []
        for t, s, tags, sess in rows:
            tg = ''.join((f'<a href="{x[1]}">{esc(x[0])} &rarr;</a>' if isinstance(x, tuple) else f'<span>{esc(x)}</span>') for x in tags)
            out.append(f'<li class="{"" if sess else "meal"}"><time>{t}</time><b>{esc(s)}</b><span class="t">{tg}</span></li>')
        return '<ol class="st-day">' + ''.join(out) + '</ol>'
    stabs = ''.join(f'<button class="tab" role="tab" id="d-{k}" aria-controls="dp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(v[0])}</button>' for i, (k, v) in enumerate(SCHED.items()))
    spanels = ''.join(f'''<div role="tabpanel" id="dp-{k}" aria-labelledby="d-{k}"{"" if i==0 else " hidden"}><div class="st-sched">{day_rows(v[2])}
      <div class="st-sched__poster" data-gallery><button class="st-poster" data-src="{imgsrc(v[1])}" data-cap="2024 Activist Institute schedule: {esc(v[0])}" aria-label="Enlarge the {esc(v[0])} schedule poster">{img(v[1], f"Activist Institute schedule poster for {v[0]}, 2024")}</button></div></div></div>''' for i, (k, v) in enumerate(SCHED.items()))

    body = f'''
<section class="st-ihero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
   <div class="rise">
    {crumbs(('Students', 'students.html'), ('Summer Activist Institute', None))}
    <p class="eyebrow">SafeBAE Summer Activist Institute</p>
    <h1><span>Meet the</span><span><span class="mk">fellows</span></span></h1>
    <p class="lede">Fellows of SafeBAE’s Summer Activist Institute from 2023, 2024 and 2025. The 2024 institute ran two days of sessions on theories of change, Title IX, sex education, policy reform, storytelling for change and engaging men in the conversation.</p>
    <div class="st-count"><a href="#f2025"><b>{len(F2025)}</b><span>2025 fellows</span></a><a href="#f2024"><b>{len(F2024)}</b><span>2024 fellows</span></a><a href="#f2023"><b>{len(F2023)}</b><span>2023 fellows</span></a><a href="#episode"><b>{PLAY_SVG}</b><span>Watch an episode</span></a></div>
   </div>
   <figure class="st-ihero__photo">{img('sumact5', 'Summer Activist Institute fellows in a discussion circle', loading='eager')}<span class="sticker">2023 &middot; 2024 &middot; 2025</span></figure>
  </div>
</section>

<section class="band band--paper" id="fellows">
  <div class="wrap" data-tabs="fellows">
    <div class="section-head"><div><h2>The fellows</h2></div><div class="tabs section-head__act" role="tablist" aria-label="Fellows by year">{tabs}</div></div>
    {panels}
  </div>
</section>

<section class="band band--slate" id="schedule">
  <div class="wrap" data-tabs="sched">
    <div class="section-head"><div><p class="eyebrow">June 2024 &middot; Activist Institute</p><h2>Two days at the 2024 institute</h2><p class="lede lede--full">Each day started with yoga or a lighthouse walk and ended with dinner and a fun activity.</p></div><div class="tabs section-head__act" role="tablist" aria-label="Schedule by day">{stabs}</div></div>
    {spanels}
  </div>
</section>

<section class="band band--teal" id="episode">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From the 2023 institute</p><h2>Watch an episode</h2><p class="lede lede--full">Episode 3 of SafeBAE’s 2023 Summer Activist Institute series.</p></div>{btn('SafeBAE on YouTube', 'https://www.youtube.com/@SafeBAE', 'mint').replace('class="btn', 'class="section-head__act btn', 1)}</div>
    <div class="st-ep reveal">
      {yt('4sr3NAPzqs0', '2023 Summer Activist Institute: Episode 3', label='Episode 3')}
      <figure class="st-fill">{img('img-6834', 'A group selfie of fellows at the 2023 Summer Activist Institute')}<figcaption>The 2023 institute</figcaption></figure>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>Ways to lead at your school</h2><p class="lede lede--full">The Peer Educator Training, SafeBAE clubs and the Student Policy Reform Guide are open to students now.</p></div></div>
    {journey()}
  </div>
</section>
{give_band()}
'''
    page('summer-institute.html', 'Summer Activist Institute · SafeBAE', 'Meet the fellows of the SafeBAE Summer Activist Institute and see the 2024 institute schedule.',
         body, active='students', body_class='st st-si', head_extra=f'<style>{CSS}{SI_CSS}</style>')


# ================================================================= espanol.html
ES_MODULES = ['Cultura de la Violación y cómo puede ayudar a cambiar a una cultura de respeto', 'Definiendo: Acoso Sexual, Agresión y Violación', 'Consentimiento',
              'Relaciones Saludables', 'Jóvenes Identificados como hombres y Violencia Sexual', 'Mitos, Datos y Estadísticas', 'Relaciones y Violencia Sexual en los Medios',
              'Seguridad en Línea y el Envío de Fotos Íntimas', 'Si Has Sido Acusado', 'Cómo apoyar a un sobreviviente', 'Opciones para Denunciar y Requisitos de Investigación',
              'Recuperación después de Violencia Sexual', 'Título IX: Derechos en la Escuela', 'Intervención del Espectador',
              'Relaciones de Pareja Después de Experimentar Violencia Sexual', 'Hablar en Público: Consejos para Presentar']

ES_CSS = '''
/* hero: the Spanish reading of BAE, closed by the dedication (as on the English training page) */
.st-es{position:relative; overflow:hidden; background:var(--logo-teal) var(--grain); color:#fff}
.st-es > .wrap{position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(52px,6.4vw,88px) clamp(40px,5vw,64px)}
.st-es h1{font-size:clamp(2.6rem,6vw,5.6rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; margin:0 0 .35em}
.st-es h1 > span{display:block}
.st-es .mk{background:none; color:var(--mint)}
.st-es .lede{color:rgba(255,255,255,.92); max-width:none}
.st-es__sub{font-family:var(--display); font-weight:800; font-stretch:112%; font-size:clamp(1.3rem,2.3vw,2rem); line-height:1.15; color:var(--mint); margin:-.2em 0 .8em}
.st-es .crumbs a{color:var(--aqua)}
.st-es__photo{position:relative; margin:0; animation:sb-rise-r 1s .1s var(--ease) both}
.st-es__photo img{width:100%; aspect-ratio:5/4; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.st-es__photo .sticker{position:absolute; left:-14px; bottom:22px}
@media (max-width:900px){.st-es > .wrap{grid-template-columns:minmax(0,1fr)} .st-es__photo{max-width:560px} .st-es__photo .sticker{left:10px}}
.st-ded{position:relative; z-index:2; background:linear-gradient(90deg, var(--line-dark) 0, var(--line-dark) 52%, transparent 66%) top left/100% 1px no-repeat; animation:sb-rise .8s .3s var(--ease) both}
.st-ded__in{position:relative; max-width:var(--wrap); margin-inline:auto; padding:clamp(22px,2.6vw,32px) var(--gutter)}
.st-ded__txt{position:relative; z-index:1; width:min(100%, 64%); display:grid; gap:10px}
.st-ded__k{margin:0; font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.st-ded__t{margin:0; font-family:var(--display); font-weight:600; font-stretch:104%; font-size:clamp(1.08rem,1.5vw,1.34rem); line-height:1.36; color:#fff; text-wrap:pretty}
.st .st-ded__link{justify-self:start; display:inline-flex; align-items:center; gap:.45em; min-height:32px; font-family:var(--display); font-weight:800; font-stretch:106%; color:var(--mint); text-decoration:none}
.st-ded__link span{transition:transform .2s var(--ease)}
.st-ded__link:hover{text-decoration:underline; text-underline-offset:4px}
.st-ded__link:hover span{transform:translateX(4px)}
.st-ded .daisy-art{position:absolute; z-index:0; right:calc(var(--gutter) - 40px); bottom:-46%; width:min(40%,470px); color:var(--mint); opacity:.5; transform-origin:50% 55%; animation:sb-bloom 1.8s .2s var(--ease) both}
@media (max-width:860px){ .st-ded__txt{width:100%} .st-ded__link{min-height:44px} .st-ded__in{padding-bottom:clamp(120px,34vw,200px)} .st-ded .daisy-art{right:-6%; bottom:-28%; width:min(78%,420px)} }

/* what the training is, beside its three facts */
.st-que{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(26px,4vw,60px); align-items:stretch}
.st-que__text{min-width:0; align-self:center}
.st-que__text h2{margin-bottom:.45em}
.st-que__text p:not(.lede){font-size:1.06rem; line-height:1.65}
.st-facts3{list-style:none; margin:0; padding:6px var(--pad-card); display:grid; grid-auto-rows:1fr; border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff; box-shadow:var(--shadow-soft)}
.st-facts3 li{margin:0; display:grid; grid-template-columns:minmax(0,5fr) minmax(0,6fr); gap:16px; align-items:center; padding:18px 0; border-bottom:1px solid var(--line-dark)}
.st-facts3 li:last-child{border-bottom:0}
.st-facts3 b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.2rem,3.6vw,3.3rem); line-height:.95; letter-spacing:-.02em; color:var(--mint)}
.st-facts3 li:last-child b{font-size:clamp(1.5rem,2.3vw,2.05rem); line-height:1}
.st-facts3 span{font-size:1.02rem; font-weight:600; line-height:1.35}
@media (max-width:900px){.st-que{grid-template-columns:minmax(0,1fr)}}

/* the 16 modules, four by four (same anatomy as the English page) */
.st-mods{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; list-style:none; padding:0; margin:0}
.st-mod{display:grid; grid-template-columns:2.6rem minmax(0,1fr); gap:10px 8px; align-items:start; padding:18px; border-radius:14px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); margin:0; min-width:0; transition:background .2s, border-color .2s}
.st-mod:hover{background:rgba(21,255,200,.08); border-color:rgba(21,255,200,.45)}
.st-mod__n{font-family:var(--display); font-stretch:112%; font-weight:900; color:var(--mint); font-size:1.55rem; line-height:1.05; letter-spacing:-.02em}
.st-mod__t{font-weight:700; line-height:1.3; font-size:1rem; padding-top:.12em}
@media (max-width:1100px){.st-mods{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.st-mods{grid-template-columns:minmax(0,1fr)}}

/* six steps on a connected track that ends in the certificate */
.st-steps6{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.st-steps6 li{position:relative; margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); display:grid; grid-template-columns:48px minmax(0,1fr); gap:0 16px; align-items:center; align-content:center; min-width:0; min-height:112px}
.st-steps6 li:not(:nth-child(3n))::after{content:""; position:absolute; z-index:1; top:50%; margin-top:-2px; left:100%; width:var(--gap); height:4px; background:var(--teal)}
.st-steps6 .n{grid-row:1/3; width:48px; height:48px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.4rem}
.st-steps6 b{grid-column:2; font-family:var(--display); font-stretch:106%; font-size:1.2rem; line-height:1.22}
.st-steps6 a{grid-column:2; justify-self:start; margin-top:5px; font-weight:700; color:var(--logo-teal); text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:3px; text-decoration-color:var(--mint)}
@media (max-width:900px){.st-steps6 a{display:inline-flex; align-items:center; min-height:44px; margin-top:0}}
.st-steps6 a:hover{color:var(--teal)}
.st-steps6 li.cert{background:var(--mint); border-color:transparent; box-shadow:var(--shadow-soft)}
.st-steps6 li.cert .n{background:var(--slate); color:var(--mint)}
.st-steps6 li.cert b{padding-right:64px}
.st-seal{position:absolute; top:-20px; right:20px; width:72px; height:72px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center; box-shadow:0 0 0 5px var(--mint), 0 0 0 7px var(--slate), var(--shadow-soft); transform:rotate(-10deg)}
.st-seal .daisy{width:42px; height:42px}
@media (max-width:900px){
  .st-steps6{grid-template-columns:minmax(0,1fr); gap:14px}
  .st-steps6 li{min-height:0}
  .st-steps6 li:not(:nth-child(3n))::after{display:none}
  .st-steps6 li:not(:last-child)::after{content:""; display:block; position:absolute; top:100%; margin:0; left:calc(var(--pad-card) + 22px); width:4px; height:14px; background:var(--teal)}
}
.st-notes{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch; margin-top:var(--gap)}
.st-note{padding:var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); min-width:0}
.st-note b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; margin-bottom:6px}
.st-note p{margin:0; font-size:.98rem; color:var(--ink-soft)}
.st-notes .helpline{flex-wrap:wrap; align-content:center}
@media (max-width:900px){.st-notes{grid-template-columns:minmax(0,1fr)}}

/* the closing note */
.st-aviso{display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr); gap:14px var(--gap); align-items:start; padding:clamp(24px,3.2vw,42px); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line)}
.st-aviso h2{font-size:clamp(1.5rem,2.4vw,2rem); margin:0}
.st-aviso p{margin:0; font-size:1.04rem; line-height:1.65}
@media (max-width:900px){.st-aviso{grid-template-columns:minmax(0,1fr)}}
'''

def espanol():
    mods = ''.join(f'<li class="st-mod"><span class="st-mod__n">{i+1}</span><span class="st-mod__t">{esc(t)}</span></li>' for i, t in enumerate(ES_MODULES))
    steps = ['<b>Registrarse.</b><a href="#registro">¡Haga clic aquí!</a>', '<b>Crear un usuario en el Portal de Educación.</b>', '<b>Realizar los 16 módulos a su propio ritmo.</b>',
             '<b>Tomar la Encuesta Final.</b>', '<b>Programar una reunión individual con los directores juveniles.</b>', '<b>¡Obtener el certificado y empezar a educar!</b>']
    def step_li(i, s):
        last = i == len(steps) - 1
        seal = '<span class="st-seal" aria-hidden="true"><span class="daisy"></span></span>' if last else ''
        return f'<li{" class=cert" if last else ""}>{seal}<span class="n">{i+1}</span>{s}</li>'
    steps_html = ''.join(step_li(i, s) for i, s in enumerate(steps))
    es_form = form_card(ES_FORM + '?embedded=true', ES_FORM + '?usp=sharing', 'Formulario de registro', 'Registro para el entrenamiento en español', 'Abrir el formulario', 1300, 'Registro: entrenamiento en español')
    es_help = (f'<div class="helpline"><div><b>¿Necesita hablar con alguien ahora? Ayuda gratuita y confidencial, 24/7</b>'
               f'<span>Crisis Text Line: envíe HOLA al 741741 &middot; SAMHSA: 1&#8209;800&#8209;662&#8209;4357 (inglés y español) &middot; Si está en peligro inmediato, llame al 911.</span></div>'
               f'<button class="btn btn--slate btn--sm" data-open-help>Todas las líneas de ayuda (en inglés)</button></div>')
    dedication = ('<div class="st-ded"><div class="st-ded__in"><span class="daisy-art" aria-hidden="true"></span><div class="st-ded__txt">'
                  '<p class="st-ded__k">For Daisy: Antes que Nadie</p>'
                  '<p class="st-ded__t">Esta capacitación se ofrece en memoria de nuestra cofundadora, Daisy Coleman, cuya visión y liderazgo continúan inspirando la misión de SafeBAE y a los jóvenes de todo el país.</p>'
                  + a('#ForDaisy<span aria-hidden="true">&rarr;</span>', 'fordaisy.html', 'st-ded__link') + '</div></div></div>')
    body = f'''<div lang="es">
<section class="st-es">
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Ruta de navegación"><a href="index.html">Inicio</a><span>/</span><a href="students.html">Estudiantes</a><span>/</span><span>En Español</span></nav>
      <h1><span><span class="mk">Antes</span></span><span>que nadie</span></h1><p class="st-es__sub">El Entrenamiento de Educadores Certificados, ahora en español</p>
      <p class="lede">Estamos emocionados de anunciar que el Entrenamiento para ser educadores certificados de la cultura del consentimiento está disponible en español. Muchas gracias a Mariana Hernandez por dirigir este proyecto y a todos los demás que lo hicieron posible. ¡Los invitamos a completar el curso y expandir el impacto de SafeBAE en diferentes partes del mundo!</p>
      <div class="btns">{btn('Registrarse', '#registro', 'mint', arrow=True)}{btn('Ver la versión en inglés', 'peer-educator.html', 'ghost')}</div>
    </div>
    <figure class="st-es__photo">{img('1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'Jóvenes de SafeBAE con botellas de agua de SafeBAE en un parque', loading='eager')}<span class="sticker">16 módulos</span></figure>
  </div>
  {dedication}
</section>

<section class="band band--aqua">
  <div class="wrap st-que reveal">
    <div class="st-que__text">
      <h2>¿Qué es el Entrenamiento BAE?</h2>
      <p class="lede">El entrenamiento BAE es el programa de educación de SafeBAE. Es nuestra primera capacitación de certificación disponible a nivel nacional en Estados Unidos para prevenir la violencia sexual entre adolescentes.</p>
      <p>El programa tiene 16 módulos, disponibles bajo demanda. Los estudiantes que buscan convertirse en educadores y defensores líderes realizan estos módulos a su propio ritmo.</p>
    </div>
    <ul class="st-facts3"><li><b>16</b><span>módulos de capacitación</span></li><li><b>1:1</b><span>reunión individual con los directores juveniles</span></li><li><b>A su ritmo</b><span>módulos disponibles bajo demanda</span></li></ul>
  </div>
</section>

<section class="band band--slate" id="modulos">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">16 módulos</p><h2>El entrenamiento incluye</h2></div></div>
    <ol class="st-mods reveal">{mods}</ol>
  </div>
</section>

<section class="band band--paper" id="pasos">
  <div class="wrap">
    <div class="section-head"><div><h2>Pasos para realizar el entrenamiento</h2></div></div>
    <ol class="st-steps6 reveal">{steps_html}</ol>
    <div class="st-notes reveal">
      <div class="st-note"><b>Antes de registrarse</b><p>Por favor, tenga en cuenta que hay contenido desencadenante y sensible en los módulos. Cada nivel de la capacitación se realiza a su propio ritmo y está disponible para usted en cualquier momento después de que se registre, así que asegúrese de tomar tiempo para realizar descansos si los necesita.</p></div>
      {es_help}
    </div>
  </div>
</section>

<section class="band band--deep" id="registro">
  <div class="wrap st-reg">
    <div class="st-reg__side">
      <div class="st-reg__head">
        <h2>Registrarse para el entrenamiento</h2>
        <p class="lede">Complete el formulario de registro para comenzar el entrenamiento en español.</p>
      </div>
      <div class="st-reg__links">
        {tile('¿Prefiere el entrenamiento en inglés?', 'Regístrese para la versión en inglés del entrenamiento.', 'peer-educator.html#register')}
        {tile('¿Preguntas?', 'Comuníquese con el equipo de SafeBAE.', 'contact.html')}
      </div>
    </div>
    <div class="st-reg__form">{es_form}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="st-aviso reveal"><h2>Por favor, tenga en cuenta</h2><p>Nos enorgullecemos de ser aliados en todas las intersecciones, pero también sabemos que, a pesar de nuestros mejores esfuerzos, puede haber lugares donde lo podríamos haber hecho mejor. Buscamos y valoramos TODOS los comentarios y recomendaciones para seguir mejorando nuestro entrenamiento y ser lo más inclusivos posible. Sabemos que podemos y siempre buscaremos mejorar, ¡pero necesitamos SU ayuda y apoyo para lograrlo!</p></div>
  </div>
</section>

<section class="band band--aqua band--tight"><div class="wrap give">
<div><p class="eyebrow">Su donación llega lejos</p><h2 style="margin:0 0 .3em">Mantenga la prevención gratuita para cada estudiante.</h2><p class="lede" style="margin:0">Su donación tiene un impacto inmediato: nos permite ofrecer educación sobre el consentimiento y recursos gratuitos a estudiantes y escuelas en todo Estados Unidos.</p></div>
<div class="btns" style="justify-content:flex-end">{btn('Donar hoy', 'donate.html', 'coral', arrow=True)}</div>
</div></section>
</div>'''
    page('espanol.html', 'Entrenamiento en español · SafeBAE', 'El Entrenamiento para ser educadores certificados de SafeBAE, disponible en español: 16 módulos a su propio ritmo.',
         body, active='students', body_class='st st-es-page', head_extra=f'<style>{CSS}{ES_CSS}</style>')


def build():
    clubs()
    reform_policy()
    summer_institute()
    espanol()


if __name__ == '__main__':
    build()
