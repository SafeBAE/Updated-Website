"""STUDENTS group, v3: students.html and peer-educator.html.
(clubs, reform-policy, summer-institute and espanol build from pages_students2.py.)
Run: python3 -c "import pages_students; pages_students.build()" """
from lib import *
from films_common import help_inline, HELPLINE_CSS
from pages_home import cpet_player, film_strip, FILM_STRIP_CSS, film_font_link
from urllib.parse import quote as _q

# ---------------------------------------------------------------- links
CPET_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSf5tlvO1pFmNl01tnrdSQCpPPaYB5djk81uu7eUyVTMzWj3kQ/viewform'
CLUB_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfoQAsZ5bZpRyBpL1ELxoC0yk5ewm5mkpoz6wwR49IcGoKtLQ/viewform'
RESUME = 'https://learning.safebae.org/students'
SKILLS = 'https://skills-lab.safebae.org/'
VIBE = 'https://checkyourvibe.org/'
AI_URL = 'https://ai-literacy.safebae.org'

def crumbs(*items):
    parts = [('Home', 'index.html')] + list(items)
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in parts) + '</nav>'

def st_help():
    """Student-facing wording of the shared helpline strip."""
    return help_inline().replace('Share these 24/7, confidential resources with students', 'Need to talk to someone? Free, confidential and open 24/7').replace('btn btn--coral btn--sm', 'btn btn--slate btn--sm')

def phero_alt(html_, media, alt):
    """phero() renders its media image with alt=""; give it real alt text."""
    return re.sub(r'(<img src="assets/img/' + re.escape(media) + r'\.webp"[^>]*?) alt=""', lambda m: m.group(1) + f' alt="{esc(alt)}"', html_, count=1)

def check_list(items, cls=''):
    return f'<ul class="st-check {cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

# hand-drawn marks in the AI Literacy Training's own style (same shapes as the AI page and the home page)
def _svg_uri(svg):
    return 'url("data:image/svg+xml,' + _q(svg, safe=" =:/'-.,()") + '")'

def _brush(fill, op):
    return _svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400' preserveAspectRatio='none'><g fill='{fill}' fill-opacity='{op}'>"
                    "<path d='M90 84Q960 -44 1812 84Q1834 88 1848 118Q1880 190 1891 288Q1893 312 1872 310Q960 230 152 310Q134 311 124 290Q92 205 78 112Q74 87 90 84Z'/>"
                    "<path d='M38 158Q900 32 1766 158Q1788 162 1802 192Q1832 262 1842 360Q1845 384 1822 382Q960 306 103 383Q84 384 74 362Q43 280 28 186Q24 161 38 158Z'/></g></svg>")

def _wave(stroke):
    return _svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 14' preserveAspectRatio='none'><path d='M2 8C20 2 34 2 52 8S84 14 102 8S134 2 152 8S184 14 198 7' fill='none' stroke='{stroke}' stroke-width='2.4' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")

AI_LOOP = '<svg class="st-loop__svg" viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M34 30C120 6 300 2 368 22C396 30 402 66 384 88C346 116 124 122 42 106C8 98 2 66 16 44C28 24 84 12 156 8" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'

# ---------------------------------------------------------------- the student journey
JOURNEY = [
    ('Learn', 'Watch the films', 'Youth-made films with discussion guides, plus the BAE Skills Lab.', 'library.html#films'),
    ('Train', 'Become a Certified Peer Educator', 'Free and self-paced: 16 modules and a certificate.', 'peer-educator.html'),
    ('Lead', 'Start or join a SafeBAE club', 'Start, affiliate or restart a chapter at your school.', 'clubs.html'),
    ('Change', 'Reform your school’s policy', 'A student guide to stronger sexual misconduct policies.', 'reform-policy.html'),
]

def journey(cur=None):
    """Four equal cards. On peer-educator.html the current stop is marked instead of linked."""
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
    return '<ol class="st-path">' + ''.join(lis) + '</ol>'

# ---------------------------------------------------------------- shared CSS (both pages)
CSS = HELPLINE_CSS + '''
/* eyebrows: Logo Teal on light, mint on dark, white on SafeBAE Teal, slate on mint */
.st main .eyebrow{color:var(--logo-teal)}
.st main :is(.band--slate,.band--deep,.band--logo,.st-hero,.phero:not(.phero--aqua):not(.phero--teal),.st-box--slate) .eyebrow{color:var(--mint)}
.st main .band--teal .eyebrow{color:#fff}
.st main :is(.band--mint,.st-box--mint) .eyebrow{color:var(--slate)}
.st .band--teal .cite{color:#fff}
.st .band--teal .arrow-link{color:#fff; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:4px}
.st .phero .link{color:var(--mint)}
.st .section-head h2 + .lede{margin-top:.55em}
/* only one coral button per page (the shared donate button): helpline buttons go slate */
.st .helpline .btn--coral{--b:var(--slate); --t:#fff}
.st .helpline{border-radius:var(--r-xl); padding:var(--pad-card)}
.st .helpline b{font-size:1.15rem; line-height:1.2; margin-bottom:4px}
/* the shared slide player: readable caption, no bar once it has stopped advancing */
/* slides are 16:9: give the control bar its own height so no slide is letterboxed */
.st .player{border-radius:var(--r-xl); aspect-ratio:auto}
.st .player::before{content:""; display:block; padding-top:calc(56.25% + 56px)}
.st .player__cap{font-size:.92rem}
.st .player__ctl button{width:44px; height:44px}
.st .player__bar{transition:opacity .4s}
.st .player.is-stopped .player__bar{opacity:0}

/* journey: four equal stops */
.st-path{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.st-path li{margin:0; min-width:0; display:flex}
.st-stop{flex:1; min-width:0; display:flex; flex-direction:column; gap:6px; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; color:var(--slate); border:1px solid transparent; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
a.st-stop:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.st-stop__top{display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:clamp(20px,2.6vw,36px)}
.st-stop__verb{font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(1.25rem,1.85vw,1.65rem); line-height:1; letter-spacing:-.015em; color:var(--logo-teal); min-width:0}
.st-stop__go{flex:none; width:clamp(36px,3.4vw,44px); height:clamp(36px,3.4vw,44px); border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; font-size:1.1rem; transition:background .2s, color .2s, transform .25s var(--ease)}
a.st-stop:hover .st-stop__go{background:var(--slate); color:var(--mint); transform:translateX(4px)}
.st-stop b{font-family:var(--display); font-stretch:108%; font-size:1.28rem; line-height:1.15}
.st-stop small{font-size:.95rem; line-height:1.45; color:var(--ink-soft)}
.st-stop__top{position:relative}
.st-stop__here{position:absolute; left:0; top:100%; margin-top:7px; font-family:var(--mono); font-size:.72rem; line-height:1; letter-spacing:.1em; text-transform:uppercase; font-weight:600; white-space:nowrap}
.st-stop__go .daisy{width:24px; height:24px}
:is(.band--slate,.band--deep) .st-stop{background:rgba(255,255,255,.05); border-color:var(--line-dark); color:#fff}
:is(.band--slate,.band--deep) .st-stop__verb{color:var(--mint)}
:is(.band--slate,.band--deep) .st-stop small{color:rgba(255,255,255,.8)}
:is(.band--slate,.band--deep) .st-stop__go{background:rgba(255,255,255,.1); color:var(--mint)}
:is(.band--slate,.band--deep) a.st-stop:hover{border-color:var(--mint); box-shadow:none}
:is(.band--slate,.band--deep) a.st-stop:hover .st-stop__go{background:var(--mint); color:var(--slate)}
:is(.band--slate,.band--deep) .st-path li.on .st-stop{background:var(--mint); border-color:var(--mint); color:var(--slate)}
:is(.band--slate,.band--deep) .st-path li.on :is(.st-stop__verb,small){color:var(--slate)}
:is(.band--slate,.band--deep) .st-path li.on .st-stop__go{background:var(--slate); color:var(--mint)}
@media (max-width:1000px){.st-path{grid-template-columns:repeat(2,minmax(0,1fr))} .st-stop__go{width:44px; height:44px} .st-stop__verb{font-size:1.6rem}}
@media (max-width:560px){.st-path{grid-template-columns:minmax(0,1fr)} .st-stop__top{margin-bottom:14px} .st-path li.on .st-stop__top{margin-bottom:34px}}

/* checklist */
.st-check{list-style:none; padding:0; margin:0; display:grid; gap:14px}
.st-check li{position:relative; padding-left:38px; margin:0; font-weight:600; line-height:1.45}
.st-check li::before{content:""; position:absolute; left:0; top:.05em; width:25px; height:25px; border-radius:7px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}

/* a pair of equal boxes */
.st-duo{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.st-box{border-radius:var(--r-xl); padding:clamp(24px,3.2vw,42px); display:flex; flex-direction:column; min-width:0}
.st-box > .btns{margin-top:auto; padding-top:26px}
.st-box--mint{background:var(--mint); color:var(--slate)}
.st-box--slate{background:var(--slate) var(--grain); color:#fff}
@media (max-width:860px){.st-duo{grid-template-columns:minmax(0,1fr)}}

/* photo that takes the height of the text beside it */
.st-fill{position:relative; margin:0; min-width:0; min-height:260px}
.st-fill > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.st-fill .sticker{position:absolute; left:-10px; bottom:22px; z-index:1}
@media (max-width:900px){.st-fill{min-height:0; aspect-ratio:3/2} .st-fill .sticker{left:12px}}

/* quote */
.st-quote{margin:0; border-left:6px solid var(--mint); padding:4px 0 4px clamp(18px,3vw,32px)}
.st-quote .quote::before{display:none}

.st-label{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin:0 0 12px}
'''

# script shared by both pages: the slide player advances through its slides once, then waits for the visitor
PLAYER_JS = r'''
  [].forEach.call(document.querySelectorAll('[data-player]'), function(p){
    var slides = [].slice.call(p.querySelectorAll('.player__slide')), seenLast = false, stopped = false;
    function cur(){ for(var i=0;i<slides.length;i++){ if(slides[i].classList.contains('on')) return i; } return 0; }
    function hold(){ try{ p.dispatchEvent(new Event('focusin')); }catch(e){} }
    function stop(){ if(stopped) return; stopped = true; p.classList.add('is-stopped'); hold(); }
    p.addEventListener('mouseleave', function(){ if(stopped) hold(); });
    p.addEventListener('click', function(e){ if(e.target.closest && e.target.closest('button')) stop(); });
    p.stStop = stop;
    if('MutationObserver' in window){ new MutationObserver(function(){ var c = cur(); if(c === slides.length - 1) seenLast = true; else if(c === 0 && seenLast) stop(); }).observe(p, {subtree:true, attributes:true, attributeFilter:['class']}); }
  });
'''

# ================================================================= students.html
HUB_CSS = FILM_STRIP_CSS.replace('#210658', '#1d414e') + '''
/* hero */
.st-hero{background:var(--slate) var(--grain); color:#fff; position:relative; overflow:hidden}
.st-hero > .wrap{position:relative; z-index:1}
.st-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(44px,6vw,84px)}
.st-hero__title{font-size:clamp(2.4rem,5vw,5.1rem); line-height:.88; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .4em}
.st-hero__title > span{display:block}
.st-hero .mk{background:none; color:var(--mint)}
.st-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.st-proof{display:flex; flex-wrap:wrap; gap:8px 22px; margin-top:24px; font-weight:600; font-size:.92rem; color:var(--aqua)}
.st-proof span::before{content:""; display:inline-block; width:8px; height:8px; background:var(--mint); margin-right:8px; transform:rotate(45deg) translateY(-2px)}
.st-helplink{display:inline-flex; align-items:center; gap:.5em; min-height:44px; margin-top:10px; padding:0; border:0; background:none; color:#fff; font:inherit; font-weight:700; cursor:pointer; text-decoration:underline; text-decoration-color:var(--coral); text-decoration-thickness:2px; text-underline-offset:4px}
.st-helplink .daisy{color:var(--coral); width:1.2em; height:1.2em}
.st-helplink:hover{color:var(--coral)}
.st-col{position:relative; width:100%; max-width:620px; aspect-ratio:1/1; margin-left:auto; animation:sb-rise-r 1s .1s var(--ease) both}
.st-col figure{position:absolute; margin:0; border:6px solid #fff; border-radius:14px; overflow:hidden; background:#fff; box-shadow:0 26px 50px -24px rgba(0,0,0,.75); transition:transform .35s var(--ease)}
.st-col figure:hover{transform:rotate(0) scale(1.03); z-index:2}
.st-col img{width:100%; height:100%; object-fit:cover}
.st-col .f1{left:0; top:3%; width:60%; height:52%; transform:rotate(-3deg)}
.st-col .f2{right:0; top:0; width:42%; height:40%; transform:rotate(3deg)}
.st-col .f3{right:1%; top:43%; width:45%; height:28%; transform:rotate(-1.5deg)}
.st-col .f4{left:2%; top:58%; width:36%; height:40%; transform:rotate(2.5deg)}
.st-col .f5{left:41%; top:73%; width:57%; height:27%; transform:rotate(-2deg)}
.st-col .sticker{position:absolute; z-index:3}
@media (max-width:900px){ .st-hero__grid{grid-template-columns:minmax(0,1fr)} .st-col{margin:0 auto; max-width:520px} }

/* pick a starting point */
.st-start{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,390px); grid-template-areas:"head aside" "path path"; gap:var(--head-gap) clamp(24px,4vw,56px); align-items:end}
.st-start__head{grid-area:head; min-width:0}
.st-start__head h2{margin:0}
.st-start__head .lede{margin:.55em 0 0}
.st-start .st-path{grid-area:path}
.st-aside{grid-area:aside; display:grid; grid-template-columns:minmax(0,1fr) auto; gap:2px 18px; align-items:center; padding:16px 16px 16px 22px; border-radius:16px; background:var(--slate); color:#fff; text-decoration:none; transition:transform .25s var(--ease)}
.st-aside:hover{transform:translateY(-3px)}
.st-aside b{font-family:var(--display); font-stretch:108%; font-size:1.15rem; line-height:1.2}
.st-aside small{grid-column:1; font-size:.92rem; line-height:1.4; color:rgba(255,255,255,.84)}
.st-aside .go{grid-row:1/3; grid-column:2; width:44px; height:44px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800; transition:transform .25s var(--ease)}
.st-aside:hover .go{transform:translateX(4px)}
@media (max-width:900px){.st-start{grid-template-columns:minmax(0,1fr); grid-template-areas:"head" "path" "aside"; gap:var(--gap)}}

/* certified peer educator: the slide player on a stage, beside what you get */
.st-cpet{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.st-stage{display:flex; flex-direction:column; min-width:0; background:var(--slate-deep); border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft)}
.st-stage__bar{flex:1 0 auto; min-height:52px; display:flex; align-items:center; justify-content:space-between; gap:8px 16px; flex-wrap:wrap; padding:10px 20px; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.st-stage__bar a{color:var(--mint); text-decoration:none; display:inline-flex; gap:.5em; align-items:center; min-height:32px}
.st-stage__bar a:hover{text-decoration:underline; text-underline-offset:4px}
.st-stage .player{flex:none; border-radius:0; box-shadow:none}
.st-cpet__card{min-width:0; display:flex; flex-direction:column; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.st-cpet__card .st-check li{font-size:1.04rem}
@media (min-width:1101px){
  .st-cpet__card{padding-top:calc(var(--pad-card) - 14px)}
  .st-cpet__card .st-check{flex:1; gap:0; align-content:stretch}
  .st-cpet__card .st-check li{display:flex; align-items:center; padding:14px 0 14px 40px; border-bottom:1px solid var(--line-dark)}
  .st-cpet__card .st-check li::before{top:50%; margin-top:-13px}
  .st-cpet__card .btns{margin-top:0}
}
.st-cpet__card .btns{margin-top:auto; padding-top:24px; display:grid; grid-template-columns:repeat(auto-fit,minmax(212px,1fr))}
.st-cpet__alt{margin:16px 0 0; font-size:.92rem; line-height:1.5; color:rgba(255,255,255,.82)}
.st-cpet__alt .link{color:var(--mint)}
@media (max-width:1100px){
  .st-cpet{grid-template-columns:minmax(0,1fr)}
  .st-cpet__card .st-check{grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px}
}
@media (max-width:760px){.st-cpet__card .st-check{grid-template-columns:minmax(0,1fr); gap:14px} .st-stage__bar a{min-height:44px}}

/* AI Literacy Training: the training's own paper, hand lettering and drawings */
.st-ai{--hand:"Balsamiq Sans","Comic Neue",var(--body); margin-top:clamp(28px,3.4vw,48px); display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(22px,2.8vw,34px) clamp(26px,4vw,60px); align-items:stretch; padding:clamp(22px,3.4vw,44px); border-radius:var(--r-xl); border:2px solid var(--slate); background-color:var(--aqua); background-image:radial-gradient(rgba(19,132,143,.22) 1.1px, transparent 1.5px); background-size:18px 18px; color:var(--slate)}
.st-ai__body{display:flex; flex-direction:column; min-width:0}
.st-ai__facts{display:flex; flex-wrap:wrap; gap:7px; margin:0 0 16px; padding:0; list-style:none}
.st-ai__facts li{margin:0; font-family:var(--hand); font-weight:700; font-size:.98rem; line-height:1; padding:7px 11px 8px; border-radius:10px; border:2px solid var(--slate); background:#fff}
.st-ai__facts li:first-child{background:var(--mint)}
.st-ai h2{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(2rem,3.5vw,3.1rem); line-height:1.12; letter-spacing:-.005em; margin:0 0 .45em}
.st-ai h2 .br{background:__BRUSH__ center/100% 100% no-repeat; color:#fff; padding:.02em .24em .1em; margin:0 -.06em; white-space:nowrap; -webkit-box-decoration-break:clone; box-decoration-break:clone}
.st-ai__body > p{font-size:1.06rem; line-height:1.6; margin:0 0 14px}
.st-ai__body > .st-ai__launch{font-family:var(--hand); font-size:clamp(1.08rem,1.4vw,1.22rem); line-height:1.7; margin:0 0 24px}
.st-loop{position:relative; display:inline-block; font-weight:700; margin:0 .4em; white-space:nowrap}
.st-loop__svg{position:absolute; left:-.6em; top:-.4em; width:calc(100% + 1.15em); height:calc(100% + .82em); color:var(--teal); overflow:visible; pointer-events:none}
.st-loop__svg path{stroke-dasharray:1; stroke-dashoffset:0; transition:stroke-dashoffset 1.2s .25s var(--ease)}
.js .st-ai__launch.reveal.pre .st-loop__svg path{stroke-dashoffset:1}
.st-ai .btns{margin-top:auto}
.st-ai .btn--ghost:hover{background:rgba(29,65,78,.08)}
.st-ai__fig{margin:0; position:relative; min-width:0; min-height:260px; transform:rotate(1.5deg)}
.st-ai__fig img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:12% 50%; border-radius:16px; border:2px solid var(--slate); box-shadow:7px 7px 0 var(--teal)}
.st-ai__fig figcaption{position:absolute; left:-10px; bottom:-12px; font-family:var(--hand); font-weight:700; font-size:.92rem; line-height:1; background:#fff; border:2px solid var(--slate); border-radius:8px; padding:6px 9px 7px; transform:rotate(-4deg)}
.st-ai__covers{grid-column:1/-1; min-width:0; padding-top:clamp(18px,2.2vw,26px); border-top:2px dashed rgba(29,65,78,.3)}
.st-ai__lbl{font-family:var(--hand); font-weight:700; font-size:1.08rem; margin:0 0 14px; color:var(--logo-teal)}
.st-ai__map{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:12px; position:relative; counter-reset:m}
.st-ai__map::before{content:""; position:absolute; left:8%; right:8%; top:16px; height:12px; background:__WAVE__ center/100% 100% no-repeat}
.st-ai__map li{position:relative; margin:0; display:flex; flex-direction:column; align-items:center; gap:9px; text-align:center; font-family:var(--hand); font-weight:700; font-size:1.02rem; line-height:1.22; counter-increment:m}
.st-ai__map li::before{content:counter(m); display:grid; place-items:center; width:44px; height:44px; border-radius:50%; border:2px solid var(--slate); background:#fff; font-size:1.12rem; transition:transform .25s var(--ease), background .25s}
.st-ai__map li:hover::before{transform:translateY(-3px) rotate(-6deg); background:var(--mint)}
@media (max-width:900px){
  .st-ai{grid-template-columns:minmax(0,1fr)}
  .st-ai__fig{order:-1; min-height:0; aspect-ratio:1200/834; width:min(100% - 14px,440px); margin:0 0 12px 8px}
  .st-ai__map{grid-template-columns:repeat(3,minmax(0,1fr)); row-gap:18px}
  .st-ai__map::before{display:none}
}
@media (max-width:480px){.st-ai__map{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* clubs */
.st-club{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); grid-template-rows:auto 1fr; grid-template-areas:"photo head" "photo body"; gap:0 clamp(26px,4vw,60px); align-items:stretch}
.st-club h2{grid-area:head; margin:0 0 .4em}
.st-club__photo{grid-area:photo; position:relative; margin:0; min-width:0; min-height:340px}
.st-club__photo img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:58% 50%; border-radius:var(--r-xl)}
.st-club__photo figcaption{position:absolute; left:0; right:0; bottom:0; padding:48px 22px 18px; border-radius:0 0 var(--r-xl) var(--r-xl); background:linear-gradient(180deg, rgba(8,24,30,0), rgba(8,24,30,.9)); color:#fff; font-size:.92rem; line-height:1.4; font-weight:500}
.st-club__photo .sticker{position:absolute; right:18px; top:-14px; z-index:1}
.st-club__body{grid-area:body; min-width:0; display:flex; flex-direction:column}
.st-club__body > p:first-child{color:rgba(255,255,255,.88)}
.st-club__body .chips{margin-bottom:24px}
.st-club__body .chip{font-size:.74rem}
.st-ways{display:grid; gap:10px; margin:0 0 24px}
.st-way{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:3px 16px; align-items:center; padding:15px 18px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); text-decoration:none; color:#fff; transition:background .2s, border-color .2s, transform .25s var(--ease)}
.st-club .st-way{color:#fff}
.st-way:hover{background:rgba(21,255,200,.1); border-color:var(--mint); transform:translateX(4px)}
.st-way b{font-family:var(--display); font-stretch:108%; font-size:1.18rem; line-height:1.2}
.st-way small{grid-column:1; color:rgba(255,255,255,.8); font-size:.95rem; line-height:1.4}
.st-way .go{grid-row:1/3; grid-column:2; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); font-weight:800}
.st-club__body .btns{margin-top:auto}
@media (max-width:900px){
  .st-club{grid-template-columns:minmax(0,1fr); grid-template-rows:none; grid-template-areas:"head" "photo" "body"; gap:0}
  .st-club__photo{min-height:0; aspect-ratio:3/2; margin:6px 0 24px}
}

/* Vibe Check: the question across the whole band, then demo and words side by side */
.st-vc__head{margin-bottom:clamp(34px,4vw,54px)}
.st-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.4rem; line-height:1; letter-spacing:0; color:var(--mint); margin:0 0 18px}
.st-vibe__mark .daisy{width:42px; height:42px}
.st-qs{display:grid; overflow:hidden; margin:0; padding-bottom:.1em}
.st-qs span{grid-area:1/1; align-self:end; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.5rem,5.2vw,4.7rem); line-height:.98; letter-spacing:-.025em; color:#fff; transform:translateY(112%); opacity:0; transition:transform .7s cubic-bezier(.2,.8,.2,1), opacity .7s}
.st-qs span.on{transform:none; opacity:1}
.st-qs span.out{transform:translateY(-112%); opacity:0}
.st-vibe{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4.4vw,64px); align-items:stretch}
.st-vibe__media{position:relative; align-self:start; min-width:0}
.st-vibe__media .vid{border-radius:var(--r-xl)}
.st-vibe__media .vid__label small{display:none}
.st-vibe__media .sticker{position:absolute; z-index:3; white-space:nowrap}
.st-vibe__s1{left:-10px; top:-16px}
.st-vibe__s2{left:150px; top:-14px}
.st-vibe__phone{position:absolute; right:-16px; bottom:-22px; width:min(168px,27%); aspect-ratio:600/1298; border-radius:22px; border:6px solid #0b1f25; overflow:hidden; box-shadow:0 30px 60px -20px rgba(0,0,0,.6); transform:rotate(5deg); z-index:2; background:#0b1f25}
.st-vibe__phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.st-vibe__body{display:flex; flex-direction:column; min-width:0}
.st-vibe__body p{color:#fff}
.st-vibe__body .lede{font-size:clamp(1.15rem,1.6vw,1.42rem); line-height:1.45}
.st-vibe__body .btns{margin-top:auto; padding-top:8px}
@media (max-width:1100px){.st-vibe{grid-template-columns:repeat(2,minmax(0,1fr))} .st-vibe__media{align-self:center}}
@media (max-width:900px){.st-vibe{grid-template-columns:minmax(0,1fr)} .st-vibe__media{align-self:start} .st-vibe__media{margin-bottom:22px} .st-vibe__media .sticker{font-size:.76rem} .st-vibe__s1{left:-6px; top:-14px} .st-vibe__s2{left:auto; right:8px; top:-13px} .st-vibe__phone{right:6px; bottom:-20px; width:min(118px,25%); border-radius:16px; border-width:4px}}

/* Skills Lab + Title IX: one anatomy, two colours */
.st-pair h2{font-size:clamp(1.8rem,3vw,2.6rem); margin:0 0 .4em}
.st-pair > p{font-size:1.04rem; margin:0}
.st-pair > .btns{display:grid; grid-template-columns:repeat(auto-fit,minmax(225px,1fr))}
.st-pair .btn{padding-inline:1em}
.st-tix{flex:1; display:grid; align-content:stretch; margin:22px 0 0; border-top:1px solid var(--line-dark)}
.st-tix > div{padding:14px 0; border-bottom:1px solid var(--line-dark)}
.st-tix h3{margin:0 0 4px; font-size:1.14rem; font-stretch:104%; line-height:1.2; color:var(--mint)}
.st-tix p{margin:0; font-size:.96rem; line-height:1.5; color:rgba(255,255,255,.86)}
.st-box--slate.st-pair > p{color:rgba(255,255,255,.88)}
.st-box--mint .st-tix,.st-box--mint .st-tix > div{border-color:rgba(29,65,78,.3)}
.st-box--mint .st-tix h3,.st-box--mint .st-tix p{color:var(--slate)}

/* fellows */
.st-fel{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(26px,4vw,60px); align-items:stretch}
.st-fel__text{display:flex; flex-direction:column; min-width:0}
.st-fel__text .btns{margin-top:auto; padding-top:6px}
.st-fel .st-fill > img{object-position:50% 22%}
@media (max-width:900px){.st-fel{grid-template-columns:minmax(0,1fr)}}
/* 27 portraits in two interlocking rows (14 over 13) that span the full width */
.st-faces{margin-top:clamp(28px,3.6vw,48px); display:grid; grid-template-columns:repeat(28,minmax(0,1fr))}
.st-faces a{grid-column:span 2; display:block; padding:4px; position:relative; transition:transform .25s var(--ease)}
.st-faces a:nth-child(15){grid-column:2 / span 2}
.st-faces a:nth-child(n+15){margin-top:-14%}
.st-faces a:hover{transform:scale(1.14); z-index:2}
.st-faces img{width:100%; height:auto; aspect-ratio:1; border-radius:50%; object-fit:cover; border:3px solid #fff; background:#fff; box-shadow:0 10px 22px -14px rgba(22,53,64,.6)}
@media (max-width:700px){
  .st-faces{grid-template-columns:repeat(10,minmax(0,1fr))}
  .st-faces a:nth-child(15){grid-column:span 2}
  .st-faces a:nth-child(9n+6){grid-column:2 / span 2}
  .st-faces a:nth-child(n+15){margin-top:0}
  .st-faces a:nth-child(n+6){margin-top:-14%}
  .st-faces a{padding:3px}
}

/* films: all eight at once, on the page grid */
.st-hub .fstrip{grid-auto-flow:row; grid-auto-columns:auto; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); overflow:visible; padding:0; scroll-snap-type:none}
.st-hub .fcard{aspect-ratio:4/3; border-radius:var(--r-xl); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.st-hub .fcard:hover{transform:translateY(-4px); box-shadow:0 24px 40px -24px rgba(0,0,0,.8)}
.st-hub .fcard img,.st-hub .fcard:hover img{filter:none}
.st-hub .fcard__shade{background:linear-gradient(180deg, rgba(8,24,30,0) 34%, rgba(8,24,30,.9))}
.st-hub .fcard__tag{font-size:.7rem; top:14px; left:14px; background:rgba(8,24,30,.78)}
.st-hub .fcard__title{left:18px; right:18px; bottom:46px}
.st-hub .fcard__go{left:18px; bottom:16px; font-size:.72rem}
.st-hub .fcard--know .fcard__title{font-size:clamp(1rem,1.75vw,1.35rem)}
.st-hub .fcard--red img{object-fit:contain; object-position:50% 44%; box-sizing:border-box; padding:0 5%}
.st-hub .fcard--red .fcard__shade{display:none}
.st-hub .fcard--red .fcard__title{width:1px; height:1px; overflow:hidden; clip-path:inset(50%); white-space:nowrap}
@media (max-width:1100px){.st-hub .fcard{aspect-ratio:1/1}}
@media (max-width:860px){.st-hub .fstrip{grid-template-columns:repeat(2,minmax(0,1fr))} .st-hub .fcard{aspect-ratio:4/3}}
@media (max-width:560px){
  .st-hub .fstrip{grid-auto-flow:column; grid-template-columns:none; grid-auto-columns:74%; overflow-x:auto; padding:4px 2px 16px; margin-right:calc(var(--gutter) * -1); padding-right:var(--gutter); scroll-snap-type:x mandatory; gap:12px}
  .st-hub .fcard{aspect-ratio:3/4}
}

/* support */
.st-support{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:stretch; background:#fff; border:3px solid var(--coral); border-radius:var(--r-xl); padding:clamp(22px,3.4vw,44px)}
.st-support > div:first-child{display:flex; flex-direction:column; min-width:0}
.st-support h2{font-size:clamp(1.7rem,3vw,2.5rem)}
.st-support .btns{margin-top:auto; padding-top:8px}
.st-lines{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:12px}
.st-line{background:var(--mist); border-radius:14px; padding:18px 20px; min-width:0}
.st-line b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; margin-bottom:8px}
.st-line span{display:block; font-family:var(--mono); font-weight:600; font-size:.92rem; line-height:1.5; color:var(--logo-teal)}
.st-line small{display:block; color:var(--ink-soft); font-size:.92rem; margin-top:8px; line-height:1.4}
@media (max-width:900px){.st-support{grid-template-columns:minmax(0,1fr)} .st-lines{grid-auto-rows:auto}}
@media (max-width:520px){.st-lines{grid-template-columns:minmax(0,1fr)}}

/* more from SafeBAE: six equal tiles */
.st-more{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.st-more a{display:grid; grid-template-columns:minmax(0,1fr) auto; grid-template-rows:auto 1fr; gap:10px 14px; align-items:start; padding:var(--pad-card); border-radius:var(--r-xl); border:1px solid var(--line); background:#fff; text-decoration:none; color:inherit; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.st-more a:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.st-more b{display:flex; flex-wrap:wrap; align-items:center; gap:8px 10px; min-height:40px; font-family:var(--display); font-stretch:106%; font-size:1.3rem; line-height:1.15; color:var(--logo-teal)}
.st-more a{position:relative}
.st-more .chip{position:absolute; top:-11px; left:calc(var(--pad-card) - 4px); font-size:.7rem; background:var(--mint); border:1.5px solid var(--slate)}
.st-more small{grid-column:1/-1; font-size:.96rem; line-height:1.5; color:var(--ink-soft)}
.st-more .go{width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .25s var(--ease)}
.st-more a:hover .go{background:var(--mint); transform:translateX(3px)}
@media (max-width:960px){.st-more{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.st-more{grid-template-columns:minmax(0,1fr)}}
'''.replace('__BRUSH__', _brush('#13848f', '0.88')).replace('__WAVE__', _wave('#1d414e'))

HUB_JS = '<script>\n(function(){' + PLAYER_JS + r'''
  /* the Vibe Check questions turn over twice, then rest on the first */
  var qs = document.querySelectorAll('.st-qs span'), i = 0, n = 0, reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(qs.length > 1 && !reduce){ var t = setInterval(function(){ var cur = qs[i]; cur.classList.remove('on'); cur.classList.add('out'); i = (i+1) % qs.length; var nx = qs[i]; nx.classList.remove('out'); void nx.offsetWidth; nx.classList.add('on'); setTimeout(function(){ cur.classList.remove('out'); }, 800); if(++n >= qs.length * 2) clearInterval(t); }, 2600); }
})();
</script>'''

F2025 = ['Adrian Alie', 'Alan Mejia', 'Armando Refcalbo', 'Ava Maldonado', 'Ava Ram', 'Brianna Benitev', 'Cayden Michaud', 'Cyra Wuthrich',
         'David Zamora', ('Dolly Barrat', 'dolly-barratt'), 'Edwinah Magloire', 'Elle Mone', ('Isaac Smith NJ', 'isaac-smith-nj'), 'Isabella Cabral', 'Jaclyn Verde',
         'Jada Davis', 'Jada Martinez', 'Luisa Palomares', 'Mimi Ndiaye', 'Molly Pines', 'Nick Niedbalski', 'Riley Devereaux', 'Skyla Vivar Rosado',
         'Sophia Nguyen', ('Summer Wilson NJ', 'summer-wilson-nj'), 'Sunny Brynildsen', 'Yareli Huerta']
F2025 = [(x, re.sub(r'[^a-z0-9]+', '-', x.lower())) if isinstance(x, str) else x for x in F2025]
assert len(F2025) == 27  # the portrait rows are laid out for exactly 27

def students():
    collage = f'''<div class="st-col">
      <figure class="f1">{img('1-000383-edited', 'SafeBAE students in tie-dye shirts crowd together for a group photo', loading='eager')}</figure>
      <figure class="f2">{img('clubhero', 'SafeBAE club members together at the beach', loading='eager')}</figure>
      <figure class="f3">{img('000398', 'Two students in SafeBAE tie-dye shirts', loading='eager')}</figure>
      <figure class="f4">{img('img-9509-1', 'Students making hand-lettered consent posters', loading='eager')}</figure>
      <figure class="f5">{img('img-6834', 'A group of SafeBAE youth leaders at sunset', loading='eager')}</figure>
      <span class="sticker" style="left:44%;top:1%">Youth-led</span>
      <span class="sticker sticker--coral sticker--r" style="left:1%;top:51%">Founded by teen survivors</span>
      <span class="sticker sticker--aqua" style="right:1%;top:67%">Free for students</span>
    </div>'''

    ways = [('Start a new chapter', 'If there’s nothing like this at your school yet', 'clubs.html#new'),
            ('Affiliate a club you already run', 'Student council, a wellness club, an affinity group', 'clubs.html#affiliate'),
            ('Restart last year’s chapter', 'If your school used to have one', 'clubs.html#restart')]
    way_html = ''.join(f'<a class="st-way" href="{h}"><b>{esc(t)}</b><small>{esc(s)}</small><span class="go" aria-hidden="true">&rarr;</span></a>' for t, s, h in ways)

    faces = ''.join(f'<a href="summer-institute.html#fellows" tabindex="-1">{img(sl, "")}</a>' for n, sl in F2025)

    resources = [
        ('Myths & Facts', 'Common myths about assault, paired with the research-backed facts that debunk them.', 'myths-facts.html'),
        ('Posters', 'Free downloadable prevention posters on consent, boundaries, and online harassment.', 'posters.html'),
        ('Podcasts', 'Episodes featuring SafeBAE founders, staff, and youth leaders. Free to listen and share.', 'library.html#podcasts'),
        ('Choking Hazard', 'There’s no safe way to choke someone. The evidence on sexual strangulation, myth vs. fact, and signs that need medical care.', 'choking-hazard.html'),
        ('Survivor Support', 'Resources for survivors and loved ones, including crisis lines, survivor-centered media, and disclosure guidance.', 'survivor-support.html'),
        ('Blog', 'Survivor stories, media analysis, and policy news from the SafeBAE community.', 'blog.html'),
    ]
    more = ''.join(f'<a href="{h}"><b>{esc(t)}{"<span class=chip>New</span>" if h == "choking-hazard.html" else ""}</b><span class="go" aria-hidden="true">&rarr;</span><small>{esc(d)}</small></a>' for t, d, h in resources)

    lines = ''.join(f'<div class="st-line"><b>{esc(n)}</b>' + ''.join(f'<span>{esc(x)}</span>' for x in num.split(' · ')) + f'<small>{esc(d)}</small></div>' for n, s, num, d, u in HOTLINES[:4])

    body = f'''
<section class="st-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap st-hero__grid">
    <div class="rise">
      {crumbs(('Students', None))}
      <h1 class="st-hero__title"><span>For students,</span><span><span class="mk">by students.</span></span></h1>
      <p class="lede">SafeBAE was founded by teen survivors who wanted their schools to change. Everything on this site was built by students, for you. Become a Certified Peer Educator, start a SafeBAE club at your school, push your district to fix its policies, or find information and support for yourself or a friend.</p>
      <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('Start a club', 'clubs.html', 'ghost')}</div>
      <div class="st-proof"><span>3,000+ Certified Peer Educators</span><span>Open to high school students anywhere</span></div>
      <button class="st-helplink" data-open-help><span class="daisy" aria-hidden="true"></span>Need support right now? See every hotline</button>
    </div>
    {collage}
  </div>
</section>

<section class="band band--mint band--tight" id="start">
  <div class="wrap st-start">
    <div class="st-start__head"><h2>Pick a starting point</h2><p class="lede lede--full">Wherever you start, you are part of a national movement of students working to end sexual violence in schools.</p></div>
    <a class="st-aside" href="college.html"><b>In college?</b><small>Mentor high schoolers or start a SafeBAE club on your campus.</small><span class="go" aria-hidden="true">&rarr;</span></a>
    {journey()}
  </div>
</section>

<section class="band band--paper" id="peer-educator">
  <div class="wrap">
    <div class="section-head"><div>{eyebrow('For Daisy: Before Anyone Else', True)}<h2>Become a Certified Peer Educator</h2><p class="lede lede--full">A free, self-paced training for students who want to lead prevention at their school. Sixteen online modules cover healthy relationships and boundaries, consent, bystander intervention, online safety, student rights under Title IX, how to support a survivor, and more.</p></div></div>
    <div class="st-cpet reveal">
      <div class="st-stage">
        <div class="st-stage__bar"><span>11 sample slides</span>{a('See all 16 modules <span aria-hidden="true">&rarr;</span>', 'peer-educator.html#modules')}</div>
        {cpet_player()}
      </div>
      <div class="st-cpet__card">
        {check_list(['Free, self-paced, and open to high school students anywhere', 'Support from our team and a community of other peer educators', 'Finish the modules and the after survey to earn your certificate'])}
        <div class="btns">{btn('Get registered', 'peer-educator.html#register', 'mint', arrow=True)}{btn('Resume training', RESUME, 'ghost')}</div>
        <p class="st-cpet__alt">Prefer Spanish? {a('Ver el entrenamiento en español', 'espanol.html', 'link')}</p>
      </div>
    </div>
    <div class="st-ai reveal" id="ai-literacy">
      <div class="st-ai__body">
        <ul class="st-ai__facts" aria-label="At a glance"><li>New</li><li>Free</li><li>Ages 13+</li></ul>
        <h2>SafeBAE <span class="br">AI Literacy</span> Training</h2>
        <p>Six free, self-paced modules for high school and college students. Anyone 13 or older can take it. Create a free account and your progress saves as you go.</p>
        <p class="st-ai__launch reveal">Launches during U.S. Media Literacy Week, <span class="st-loop">Oct 26&ndash;30, 2026{AI_LOOP}</span></p>
        <div class="btns">{btn('About the training', 'ai-literacy.html', 'slate', arrow=True)}{btn('Open the training', AI_URL, 'ghost')}</div>
      </div>
      <figure class="st-ai__fig">{img('ai-illo-hello', 'A drawing of a computer screen with a smiling face made of code and a name tag that reads “Hello, my name is AI.”')}<figcaption>From the training</figcaption></figure>
      <div class="st-ai__covers">
        <p class="st-ai__lbl">What it covers</p>
        <ol class="st-ai__map"><li>How AI works</li><li>How feeds and AI shape what we see and believe</li><li>AI and healthy relationships</li><li>Using AI well</li><li>Fake images</li><li>Sextortion</li></ol>
      </div>
    </div>
  </div>
</section>

<section class="band band--deep" id="clubs">
  <div class="wrap st-club">
    <h2>Start a club at your school</h2>
    <figure class="st-club__photo">{img('clubtabling', 'A SafeBAE club table with red, yellow, and green flags, Can I Kiss You? buttons, and Vibe Check cards')}<span class="sticker">Free to register</span><figcaption>A SafeBAE club table: red, yellow and green flags, “Can I Kiss You?” buttons and Vibe Check cards.</figcaption></figure>
    <div class="st-club__body">
      <p>A SafeBAE club focused on consent and dating violence prevention can help shift the culture among your peers and build a safer school community. Start a new club, or bring SafeBAE programming into a group you already belong to.</p>
      {chips(['Any school', 'Members-only Club Hub', 'Virtual training sessions'], 'mint')}
      <p class="st-label">Three ways to do it</p>
      <div class="st-ways">{way_html}</div>
      <div class="btns">{btn('Register your club', CLUB_FORM, 'mint')}{btn('How clubs work', 'clubs.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap">
    <div class="st-vc__head">
      <h2 class="st-vibe__mark"><span class="daisy" aria-hidden="true"></span>Vibe Check by SafeBAE</h2>
      <div class="st-qs" aria-hidden="true"><span class="on">Did I cross a line?</span><span>Was that consent?</span><span>Did I harm someone?</span><span>Did my friend cross a line?</span></div>
    </div>
    <div class="st-vibe reveal">
      <div class="st-vibe__media">
        {yt('Ng8S3w1eTRU', 'Vibe Check demo', label='Demo')}
        <div class="st-vibe__phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
        <span class="sticker st-vibe__s1">Anonymous</span>
        <span class="sticker sticker--white sticker--r st-vibe__s2">No account needed</span>
      </div>
      <div class="st-vibe__body">
        <p class="lede">A private, self-guided reflection tool for anyone questioning whether they, or a friend, may have crossed a line.</p>
        <p>Nothing is ever reported and no account is required. Vibe Check walks you through what happened and what to do next, and connects you with real resources on consent, communication and accountability.</p>
        <div class="btns">{btn('Open Vibe Check', VIBE, 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap st-duo reveal">
    <article class="st-box st-box--mint st-pair" id="skills-lab">
      <h2>BAE Skills Lab</h2>
      <p>Short interactive activities about consent, boundaries, and healthy relationships. Put your learning into practice and strengthen your skills as a peer educator and club leader.</p>
      <div class="st-tix">
        <div><h3>Boundary Flags</h3><p>Sort 25 real situations into green, yellow and red flags to identify and understand your own boundaries.</p></div>
        <div><h3>Supporting a Survivor: Helpful or Harmful?</h3><p>Sort things people actually say to survivors into what helps and what hurts.</p></div>
        <div><h3>SafeBAE Jeopardy</h3><p>A 25-question game show on consent and healthy relationships.</p></div>
      </div>
      <div class="btns">{btn('All activities', 'skills-lab.html', 'slate', arrow=True)}{btn('Open the Skills Lab', SKILLS, 'ghost')}</div>
    </article>
    <article class="st-box st-box--slate st-pair" id="title-ix">
      <h2>Title IX &amp; your school’s policy</h2>
      <p>Title IX is the federal law that bars sex discrimination, including sexual harassment and assault, at any school that takes federal funding.</p>
      <div class="st-tix">
        <div><h3>Know your rights</h3><p>Your right to report, to supportive measures like a schedule change, and to a prompt, fair investigation.</p></div>
        <div><h3>Find your coordinator</h3><p>Learn whether your school is covered by Title IX, and how to find your school’s Title IX Coordinator.</p></div>
        <div><h3>Understand and change your school’s policy</h3><p>What your school’s sexual misconduct policy says, what a strong one should include, and how to advocate for change.</p></div>
      </div>
      <div class="btns">{btn('Title IX basics', 'title-ix.html', 'mint', arrow=True)}{btn('Policy reform guide', 'reform-policy.html', 'ghost')}</div>
    </article>
  </div>
</section>

<section class="band band--aqua" id="institute">
  <div class="wrap">
    <div class="st-fel reveal">
      <div class="st-fel__text">
        <p class="eyebrow">Summer Activist Institute</p>
        <h2>Meet the fellows</h2>
        <p class="lede">Fellows from SafeBAE’s 2023, 2024 and 2025 Summer Activist Institutes. The 2024 institute covered theories of change, Title IX, sex education, policy reform, storytelling for change and engaging men in the conversation.</p>
        <div class="btns">{btn('Meet the 2025 fellows', 'summer-institute.html#fellows', 'slate', arrow=True)}{btn('See the 2024 schedule', 'summer-institute.html#schedule', 'ghost')}</div>
      </div>
      <figure class="st-fill">{img('sumact5', 'Summer Activist Institute fellows in a discussion circle')}<span class="sticker">27 fellows in 2025</span></figure>
    </div>
    <div class="st-faces reveal" aria-hidden="true">{faces}</div>
  </div>
</section>

<section class="band band--deep" id="films">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">The Library</p><h2>Films made by <span class="mk">young people</span></h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Short films written, directed and performed by young people, each paired with a ready-to-teach discussion guide.</p></div>{btn('Open the library', 'library.html#films', 'mint', arrow=True)}</div>
    {film_strip('reveal')}
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="st-support reveal" id="support">
      <div>
        <p class="eyebrow" style="color:var(--slate)"><span class="daisy" style="color:var(--coral)"></span>Support for you or a friend</p>
        <h2>If something happened, you don’t have to handle it alone.</h2>
        <p class="muted">Crisis lines, survivor-centered media, and guidance on how to tell someone, or how to respond when a friend tells you.</p>
        <div class="btns">{btn('Survivor support', 'survivor-support.html', 'slate', arrow=True)}<button class="btn btn--ghost" data-open-help>All hotlines</button></div>
      </div>
      <div class="st-lines">{lines}</div>
    </div>
    <div class="section-head" style="margin-top:clamp(44px,6vw,72px)"><div><h2>More from SafeBAE</h2></div></div>
    <div class="st-more reveal">{more}</div>
  </div>
</section>
{give_band()}
'''
    page('students.html', 'For Students · SafeBAE', 'Become a youth leader with SafeBAE. Join peer educator training, start a club, and help prevent sexual violence in your school and community.',
         body, active='students', body_class='st st-hub', fonts=film_font_link() + '&family=Balsamiq+Sans:wght@400;700', head_extra=f'<style>{CSS}{HUB_CSS}</style>', scripts=HUB_JS)


# ================================================================= peer-educator.html
MODULES = [
    ('Rape Culture & Creating a Culture of Respect', ('Watch: Rape Culture to Respect', 'film-rape-culture.html')),
    ('Sexual Harassment, Assault, & Rape Defined', None),
    ('Consent is BAE (Before <i>Anything</i> Else)', ('Watch: It’s Giving Red Flags', 'film-its-giving-red-flags.html')),
    ('Healthy Relationships & Boundaries', ('Practice: BAE Skills Lab', 'skills-lab.html')),
    ('Male Identified Youth & Sexual Violence', ('Watch: Theo’s Story', 'film-sexual-assault-of-men.html')),
    ('Myths, Facts & Statistics', ('Read: Myths & Facts', 'myths-facts.html')),
    ('Sexual Violence & Relationships in Media', None),
    ('Online Safety & Sending Nudes', ('Watch: #knowB4Unude', 'film-knowb4unude.html')),
    ('How to Support A Survivor', ('Read: Survivor Support', 'survivor-support.html')),
    ('Reporting Options & Investigation Requirements', None),
    ('Your Rights in School (Title IX & Beyond)', ('Read: Title IX', 'title-ix.html')),
    ('Healing After Sexual Assault', None),
    ('Dating After Experiencing Sexual Violence', ('Watch: Intimacy & Dating', 'film-dating-after-sexual-assault.html')),
    ('Bystander Intervention (The BAEcode)', ('Watch: BAEcode: Game On!', 'film-baecode-game-on.html')),
    ('How to Respond If You’ve Been Accused', ('Reflect: Vibe Check', 'vibe-check.html')),
    ('Public Speaking & Leading as a Peer Educator', None),
]

# one-line labels for the slide rail (the player's own caption carries the full wording)
CHAPTERS = ['Survivor-founded and youth-led', 'Why this training matters', 'Module 1: Rape culture to respect', 'Consent starts when you’re a kid', 'The 6 Pillars of Consent',
            'Foundation of a healthy relationship', 'BAEcode: real scripts for speaking up', 'Online safety & digital harassment', 'Supporting a partner who is a survivor',
            'Daisy Coleman’s words of wisdom', 'Become a Certified Peer Educator']

PE_CSS = '''
.st-pe .phero h1{font-size:clamp(2.3rem,4.7vw,4.3rem)}
/* the dedication closes the hero; on this page the hero's drawn daisy grows from it */
.st-pe .phero__wm{display:none}
.st-ded{position:relative; z-index:2; background:linear-gradient(90deg, var(--line-dark) 0, var(--line-dark) 52%, transparent 66%) top left/100% 1px no-repeat; animation:sb-rise .8s .3s var(--ease) both}
.st-ded__in{position:relative; max-width:var(--wrap); margin-inline:auto; padding:clamp(22px,2.6vw,32px) var(--gutter)}
.st-ded__txt{position:relative; z-index:1; width:min(100%, 64%); display:grid; gap:10px}
.st-ded__k{margin:0; font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.st-ded__t{margin:0; font-family:var(--display); font-weight:600; font-stretch:104%; font-size:clamp(1.08rem,1.5vw,1.34rem); line-height:1.36; color:#fff; text-wrap:pretty}
.st-ded__link{justify-self:start; display:inline-flex; align-items:center; gap:.45em; min-height:32px; font-family:var(--display); font-weight:800; font-stretch:106%; color:var(--mint); text-decoration:none}
.st-ded__link span{transition:transform .2s var(--ease)}
.st-ded__link:hover{text-decoration:underline; text-underline-offset:4px}
.st-ded__link:hover span{transform:translateX(4px)}
.st-ded .daisy-art{position:absolute; z-index:0; right:calc(var(--gutter) - 40px); bottom:-46%; width:min(40%,470px); color:var(--mint); opacity:.55; transform-origin:50% 55%; animation:sb-bloom 1.8s .2s var(--ease) both}
@media (max-width:860px){ .st-ded__txt{width:100%} .st-ded__link{min-height:44px} .st-ded__in{padding-bottom:clamp(120px,34vw,200px)} .st-ded .daisy-art{right:-6%; bottom:-28%; width:min(78%,420px)} }

.st-facts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0}
.st-facts > div{padding:6px 24px; border-left:2px solid rgba(29,65,78,.22); min-width:0}
.st-facts > div:first-child{border-left:0; padding-left:0}
.st-facts b{display:block; font-variant-numeric:tabular-nums; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.1rem,3.6vw,3.4rem); line-height:.95; letter-spacing:-.02em}
.st-facts span{display:block; font-weight:600; margin-top:8px; line-height:1.35}
@media (max-width:860px){.st-facts{grid-template-columns:1fr 1fr; row-gap:24px} .st-facts > div:nth-child(3){border-left:0; padding-left:0}}

/* what is the certification: words beside the photo, then what peer educators do */
.st-what{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(26px,4vw,60px); align-items:stretch}
.st-what__text{min-width:0; align-self:center}
.st-what__text p{font-size:1.08rem; line-height:1.65}
.st-what .st-fill > img{object-position:50% 38%}
.st-docard{grid-column:1/-1; display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:18px clamp(26px,4vw,60px); align-items:center; padding:clamp(24px,3.2vw,42px); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff}
.st-docard h3{font-size:clamp(1.5rem,2.4vw,2rem); margin:0 0 .45em}
.st-docard p{margin:0; color:rgba(255,255,255,.86)}
.st-do{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:0 clamp(18px,2.4vw,32px); border-top:1px solid var(--line-dark)}
.st-do li{display:flex; gap:14px; align-items:baseline; padding:14px 0; border-bottom:1px solid var(--line-dark); margin:0; font-weight:600; font-size:1.04rem; line-height:1.35}
.st-do li:last-child{grid-column:1/-1}
.st-do li::before{content:""; flex:none; width:10px; height:10px; background:var(--mint); transform:rotate(45deg)}
@media (max-width:900px){.st-docard{grid-template-columns:minmax(0,1fr)}}
@media (min-width:621px) and (max-width:900px){.st-what .st-fill{aspect-ratio:auto; min-height:240px}}
@media (max-width:620px){.st-what{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.st-do{grid-template-columns:minmax(0,1fr)}}

/* preview: the player and its slide rail are one height */
.st-prev{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch}
.st-chap{list-style:none; margin:0; padding:8px; display:grid; grid-template-rows:repeat(11,minmax(0,1fr)); gap:2px; min-width:0; border-radius:var(--r-xl); background:rgba(255,255,255,.04); border:1px solid var(--line-dark)}
.st-chap li{margin:0; min-width:0; min-height:0; display:flex}
.st-chap button{flex:1; min-width:0; display:grid; grid-template-columns:26px minmax(0,1fr); gap:8px; align-items:center; text-align:left; font:inherit; font-size:.94rem; font-weight:600; line-height:1.2; padding:2px 12px; border-radius:12px; border:0; background:transparent; color:rgba(255,255,255,.84); cursor:pointer; transition:background .15s, color .15s}
.st-chap .n{font-family:var(--mono); font-size:.74rem; color:var(--aqua)}
.st-chap .t{overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.st-chap button:hover{background:rgba(255,255,255,.08); color:#fff}
.st-chap button[aria-current="true"]{background:var(--mint); color:var(--slate)}
.st-chap button[aria-current="true"] .n{color:var(--slate)}
@media (max-width:1100px){
  .st-prev{grid-template-columns:minmax(0,1fr)}
  .st-chap{grid-template-rows:none; grid-template-columns:repeat(2,minmax(0,1fr)); gap:4px}
  .st-chap li:last-child{grid-column:1/-1}
  .st-chap button{min-height:44px; padding-block:6px}
  .st-chap .t{white-space:normal}
}
@media (max-width:620px){.st-chap{grid-template-columns:minmax(0,1fr)}}

/* the 16 modules, four by four */
.st-modwrap{margin-top:clamp(48px,6vw,80px); padding-top:clamp(36px,4vw,52px); border-top:1px solid var(--line-dark)}
.st-mods{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; list-style:none; padding:0; margin:0}
.st-mod{display:grid; grid-template-columns:2.6rem minmax(0,1fr); grid-template-rows:1fr auto; gap:10px 8px; align-items:start; padding:18px 18px 14px; border-radius:14px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); margin:0; min-width:0; transition:background .2s, border-color .2s}
.st-mod:hover{background:rgba(21,255,200,.08); border-color:rgba(21,255,200,.45)}
.st-mod__n{font-family:var(--display); font-stretch:112%; font-weight:900; color:var(--mint); font-size:1.55rem; line-height:1.05; letter-spacing:-.02em}
.st-mod__t{font-weight:700; line-height:1.3; font-size:1rem; padding-top:.12em}
.st-mod a{grid-column:1/-1; align-self:end; font-family:var(--mono); font-size:.74rem; letter-spacing:.03em; text-transform:uppercase; line-height:1.4; color:var(--aqua); text-decoration:none; padding:4px 0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.st-mod a:hover{color:var(--mint); text-decoration:underline; text-underline-offset:4px}
@media (max-width:1100px){.st-mods{grid-template-columns:repeat(2,minmax(0,1fr))} .st-mod a{grid-column:2}}
@media (max-width:520px){.st-mods{grid-template-columns:minmax(0,1fr)} .st-mod{padding-bottom:6px} .st-mod a{min-height:44px; display:flex; align-items:center} .st-mod:not(:has(a)){padding-bottom:18px}}

/* six steps: a connected track that ends in the certificate */
.st-steps6{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.st-steps6 li{position:relative; margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column; gap:8px; min-width:0}
.st-steps6 li:not(:nth-child(3n))::after{content:""; position:absolute; z-index:1; top:calc(var(--pad-card) + 22px); left:100%; width:var(--gap); height:4px; background:var(--teal)}
.st-steps6 .n{width:48px; height:48px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.4rem; flex:none}
.st-steps6 h3{font-size:1.3rem; margin:10px 0 0}
.st-steps6 p{margin:0; color:var(--ink-soft); font-size:.98rem; line-height:1.55}
.st-steps6 li.cert{background:var(--mint); border-color:transparent; box-shadow:var(--shadow-soft)}
.st-steps6 li.cert .n{background:var(--slate); color:var(--mint)}
.st-steps6 li.cert p{color:var(--slate)}
.st-seal{position:absolute; top:-20px; right:20px; width:80px; height:80px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center; box-shadow:0 0 0 5px var(--mint), 0 0 0 7px var(--slate), var(--shadow-soft); transform:rotate(-10deg)}
.st-seal .daisy{width:46px; height:46px}
@media (max-width:860px){
  .st-steps6{grid-template-columns:minmax(0,1fr); gap:14px}
  .st-steps6 li:not(:nth-child(3n))::after{display:none}
  .st-steps6 li:not(:last-child)::after{content:""; display:block; position:absolute; top:100%; left:calc(var(--pad-card) + 22px); width:4px; height:14px; background:var(--teal)}
}
.st-notes{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch; margin-top:var(--gap)}
.st-note{padding:var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); min-width:0}
.st-note b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; margin-bottom:6px}
.st-note p{margin:0; font-size:.98rem; color:var(--ink-soft)}
.st-notes .helpline{flex-wrap:nowrap}
.st-notes .helpline span{font-size:1rem; line-height:1.5}
.st-notes .helpline .btn{flex:none}
@media (max-width:520px){.st-notes .helpline{flex-wrap:wrap}}
@media (max-width:860px){.st-notes{grid-template-columns:minmax(0,1fr)}}

/* why peer education matters */
.st-why{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(26px,4vw,60px); align-items:stretch}
.st-why__text{min-width:0}
.st-why__text p{color:#fff}
.st-why .st-fill > img{object-position:55% 55%}
.st-why + .st-quote{margin-top:clamp(36px,5vw,60px)}
@media (max-width:900px){.st-why{grid-template-columns:minmax(0,1fr)}}

/* register: a call card until the form loads; with the live form, a sticky side column beside it */
.st-reg{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(26px,4vw,60px); align-items:stretch}
.st-reg__side{display:contents}
.st-reg__head{grid-column:1; grid-row:1; min-width:0; align-self:center}
.st-reg__head h2{margin-bottom:.35em}
.st-reg__head .lede{margin:0}
.st-reg__form{grid-column:2; grid-row:1; min-width:0; display:flex}
.st-reg__form .embed{flex:1; display:flex; min-width:0}
.st-reg__form .embed__fallback{flex:1; display:flex; flex-direction:column; align-items:flex-start; gap:10px; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--slate) var(--grain); color:#fff; box-shadow:var(--shadow-soft)}
.st-reg__form .embed__fallback h3{font-size:clamp(1.35rem,2vw,1.7rem); margin:0}
.st-reg__form .embed__fallback small{font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.st-reg__form .embed__fallback .btn{margin-top:auto}
.st-reg__links{grid-column:1/-1; grid-row:2; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.st-reg__link{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:4px 14px; align-items:center; padding:20px 22px; border-radius:16px; background:#fff; border:1px solid var(--line); text-decoration:none; color:inherit; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.st-reg__link:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.st-reg__link b{font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.2; color:var(--logo-teal)}
.st-reg__link small{grid-column:1; font-size:.95rem; line-height:1.4; color:var(--ink-soft)}
.st-reg__link .go{grid-row:1/3; grid-column:2; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .25s var(--ease)}
.st-reg__link:hover .go{background:var(--mint); transform:translateX(3px)}
.st-reg:has(iframe){grid-template-columns:minmax(0,4fr) minmax(0,8fr); align-items:start}
.st-reg:has(iframe) .st-reg__side{display:block; grid-column:1; grid-row:1; position:sticky; top:104px; min-width:0}
.st-reg:has(iframe) .st-reg__links{grid-template-columns:minmax(0,1fr); gap:10px; margin-top:26px}
.st-reg:has(iframe) .st-reg__form .embed{display:block; background:#fff; border-radius:var(--r-xl); border:1px solid var(--line); padding:6px; box-shadow:var(--shadow-soft)}
.st-reg:has(iframe) .st-reg__form iframe{display:block; border-radius:16px!important}
@media (max-width:900px){
  .st-reg,.st-reg:has(iframe){grid-template-columns:minmax(0,1fr)}
  .st-reg__head,.st-reg__form,.st-reg__links{grid-column:1; grid-row:auto}
  .st-reg__links{grid-template-columns:minmax(0,1fr); gap:10px; order:3}
  .st-reg__head{order:1} .st-reg__form{order:2}
  .st-reg:has(iframe) .st-reg__side{display:contents}
  .st-reg:has(iframe) .st-reg__links{margin-top:0}
}

/* after the training */
.st-ai-strip{margin-top:var(--gap); display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:18px clamp(22px,3vw,40px); align-items:center; padding:var(--pad-card); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark)}
.st-ai-strip__date{font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; color:var(--mint); font-size:clamp(1.7rem,2.8vw,2.5rem); line-height:.9; white-space:nowrap}
.st-ai-strip__date small{display:block; font-family:var(--mono); font-weight:600; font-stretch:100%; font-size:.74rem; letter-spacing:.1em; color:var(--aqua); margin-top:10px}
.st-ai-strip h3{margin:0 0 .3em; font-size:1.4rem}
.st-ai-strip p{margin:0; color:rgba(255,255,255,.84); font-size:.98rem}
@media (max-width:900px){.st-ai-strip{grid-template-columns:minmax(0,1fr)} .st-ai-strip .btn{justify-self:start}}
'''

PE_JS = '<script>\n(function(){' + PLAYER_JS + r'''
  /* the two counted facts run up once when the band comes into view */
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce && 'IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){ es.forEach(function(en){ if(!en.isIntersecting) return; io.unobserve(en.target); var el = en.target, n = +el.getAttribute('data-count'), suf = el.getAttribute('data-suffix') || '', t0 = null; function step(t){ if(!t0) t0 = t; var k = Math.min(1, (t - t0) / 800), v = Math.round(n * (1 - Math.pow(1 - k, 3))); el.textContent = v.toLocaleString('en-US') + suf; if(k < 1) requestAnimationFrame(step); } requestAnimationFrame(step); }); }, {threshold:.6});
    [].forEach.call(document.querySelectorAll('.st-facts [data-count]'), function(el){ io.observe(el); });
  }
  var p = document.querySelector('.st-prev [data-player]'); if(!p) return;
  var slides = [].slice.call(p.querySelectorAll('.player__slide')), btns = [].slice.call(document.querySelectorAll('.st-chap button')), nx = p.querySelector('[data-next]');
  function cur(){ for(var i=0;i<slides.length;i++){ if(slides[i].classList.contains('on')) return i; } return 0; }
  function mark(){ var c = cur(); btns.forEach(function(b, i){ b.setAttribute('aria-current', String(i === c)); }); }
  btns.forEach(function(b, i){ b.addEventListener('click', function(){ if(p.stStop) p.stStop(); var n = (i - cur() + slides.length) % slides.length; for(var k=0;k<n;k++){ nx.click(); } mark(); }); });
  if('MutationObserver' in window){ new MutationObserver(mark).observe(p, {subtree:true, attributes:true, attributeFilter:['class']}); }
  mark();
})();
</script>'''

def peer_educator():
    def mod_li(i, t, rel):
        link = ''
        if rel:
            ext = rel[1].startswith('http')
            link = a(esc(rel[0]) + (' &#8599;' if ext else ' &rarr;'), rel[1])
        return f'<li class="st-mod"><span class="st-mod__n">{i+1}</span><span class="st-mod__t">{t}</span>{link}</li>'
    mods = ''.join(mod_li(i, t, rel) for i, (t, rel) in enumerate(MODULES))
    chap = ''.join(f'<li><button type="button" aria-current="{str(i==0).lower()}" title="{esc(c)}"><span class="n">{i+1:02d}</span><span class="t">{esc(c)}</span></button></li>' for i, c in enumerate(CHAPTERS))
    steps = [
        ('Complete the registration form', f'Fill out a short interest form to get started. We’ll send you everything you need to begin the training. <a class="link" href="#register">Register below</a>'),
        ('Create your training portal account', 'Set up your secure account on Podia to unlock all 16 modules and additional resources.'),
        ('Complete 16 modules', 'Learn about consent, healthy relationships, digital safety, and more across 16 interactive modules, completed at your own pace.'),
        ('Complete the post-survey', 'Share feedback and reflect on what you’ve learned. Your responses help us improve the training and better support future Peer Educators.'),
        ('Earn your certificate', 'After completing all 16 modules and the post-training survey, you’ll receive your official SafeBAE Certified Peer Educator certificate.'),
        ('Start leading', f'Put your skills into action by leading presentations, organizing campaigns, or <a class="link" href="clubs.html">starting a SafeBAE Club</a>. You can also meet with the SafeBAE team to explore next steps.'),
    ]
    def step_li(i, t, d):
        cls = ' class="cert"' if i == 4 else ''
        seal = '<span class="st-seal" aria-hidden="true"><span class="daisy"></span></span>' if i == 4 else ''
        return f'<li{cls}>{seal}<span class="n">{i+1}</span><h3>{esc(t)}</h3><p>{d}</p></li>'
    steps_html = ''.join(step_li(i, t, d) for i, (t, d) in enumerate(steps))
    lede = 'SafeBAE’s Certified Peer Educator Training gives young people the knowledge, confidence and leadership skills to lead conversations about consent, healthy relationships and their lived experiences, and to drive prevention in their own schools and communities.'
    hero = phero_alt(phero('Certified <span class="mk">Peer Educator</span> Training', lede, crumbs=[('Home', 'index.html'), ('Resources', 'resources.html'), ('Peer Educator Training', None)],
                           media='dsc01134', sticker='Free · 16 modules',
                           actions=btn('Register here', '#register', 'mint', arrow=True) + btn('Ver en Español', 'espanol.html', 'ghost') + btn('Resume training', RESUME, 'ghost')),
                     'dsc01134', 'Certified Peer Educators in SafeBAE shirts gathered for a group photo')
    dedication = ('<div class="st-ded"><div class="st-ded__in"><span class="daisy-art" aria-hidden="true"></span><div class="st-ded__txt">'
                  '<p class="st-ded__k">For Daisy: Before Anyone Else</p>'
                  '<p class="st-ded__t">This training is offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission and youth nationwide.</p>'
                  + a('#ForDaisy<span aria-hidden="true">&rarr;</span>', 'fordaisy.html', 'st-ded__link') + '</div></div></div>')
    hero = hero[:hero.rindex('</section>')] + dedication + '</section>'
    reg_links = [('Already registered?', 'Pick up where you left off in the training portal.', RESUME),
                 ('Entrenamiento en español', 'The full training is also available in Spanish.', 'espanol.html'),
                 ('Questions about the training?', 'Reach the SafeBAE team.', 'contact.html')]
    reg_links_html = ''.join(f'<a class="st-reg__link" href="{esc(h)}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'><b>{esc(t)}</b><small>{esc(d)}</small><span class="go" aria-hidden="true">{"&#8599;" if h.startswith("http") else "&rarr;"}</span></a>' for t, d, h in reg_links)
    reg_form = (f'<div class="embed" data-embed="{esc(CPET_FORM + "?embedded=true")}" data-h="1400" data-title="Certified Peer Educator Training registration">'
                f'<div class="embed__fallback"><small>Student interest form</small><h3>Register for the Certified Peer Educator Training</h3>{btn("Open the form", CPET_FORM, "mint")}</div></div>')
    body = f'''
{hero}

<section class="band band--mint band--tight">
  <div class="wrap st-facts">
    <div><b data-count="16">16</b><span>interactive online modules</span></div>
    <div><b>$0</b><span>free for students, at their own pace</span></div>
    <div><b>1-on-1</b><span>support from SafeBAE’s team</span></div>
    <div><b data-count="3000" data-suffix="+">3,000+</b><span>young people certified</span></div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>What is the Peer Educator Certification?</h2><p class="lede lede--full">A free, self-paced training designed for high school students who want to lead sexual violence prevention in their schools and communities.</p></div></div>
    <div class="st-what reveal">
      <div class="st-what__text">
        <p>Trauma-informed and accessible from anywhere, the program equips students to educate peers, challenge harmful norms, and build safer school environments. The certification includes 16 interactive online modules, plus one-on-one support from SafeBAE’s team. Upon completion, students receive an official certification, along with access to ongoing leadership, organizing, and advocacy opportunities.</p>
        <p>Educators looking to bring youth-led programming into their school can use the training too: it shifts school culture from the inside out. {a('Bring SafeBAE to your school', 'request-a-program.html', 'link')}</p>
      </div>
      <figure class="st-fill">{img('20240627-171417-646d14-4', 'Students raising their hands during a SafeBAE training session')}</figure>
      <div class="st-docard">
        <div><h3>What peer educators do</h3><p>Peer educators become trusted voices in their schools. This training creates a clear pathway for young people to drive cultural change.</p></div>
        <ul class="st-do"><li>Facilitate classroom discussions</li><li>Lead school clubs</li><li>Organize events</li><li>Run social media campaigns</li><li>Model what consent culture looks like in practice</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--deep" id="preview">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">11 sample slides</p><h2>Preview the training</h2></div>{btn('Register here', '#register', 'mint', arrow=True)}</div>
    <div class="st-prev reveal">{cpet_player()}<ol class="st-chap" aria-label="Jump to a slide">{chap}</ol></div>
    <div class="st-modwrap" id="modules">
      <div class="section-head"><div><h2>What the 16 modules cover</h2><p class="lede lede--full" style="color:rgba(255,255,255,.85)">Consent, healthy relationships, digital safety, survivor support, your rights at school and more, completed at your own pace.</p></div></div>
      <ol class="st-mods reveal">{mods}</ol>
    </div>
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><h2>Six steps to your <span class="mk">certificate</span></h2><p class="lede lede--full">Becoming a Certified Peer Educator is simple, flexible, and fully supported. Students can register and complete the training entirely for free and at their own pace.</p></div></div>
    <ol class="st-steps6 reveal">{steps_html}</ol>
    <div class="st-notes reveal">
      <div class="st-note"><b>Before you start</b><p>The modules include sensitive content that may be triggering. The training is self-paced and available any time after you register, so take breaks when you need them.</p></div>
      {st_help()}
    </div>
  </div>
</section>

<section class="band band--teal">
  <div class="wrap">
    <div class="st-why reveal">
      <div class="st-why__text">
        <h2>Why peer education matters</h2>
        <p class="lede">Prevention only works when it feels real, and for most students, that means hearing it from someone they trust. Peer education brings authenticity, relatability, and lived experience into the conversation.</p>
        <p>When youth lead, their peers ask more honest questions. They take ownership. They change behavior because they saw someone like them modeling something better, not because they were told to.</p>
        <p>{a('See the data on youth-led prevention', 'impact.html', 'arrow-link')}</p>
      </div>
      <figure class="st-fill">{img('img-3755', 'A group of SafeBAE students in a school hallway')}<span class="sticker">Youth-led</span></figure>
    </div>
    <figure class="st-quote reveal"><blockquote class="quote">As I went on in the training, I felt like I could be a more helpful and supportive person and that I would know what to do if something happened to me or anyone I know. I feel confident that I can help people in all sorts of situations and I am more educated on the effects of rape culture.</blockquote><figcaption class="cite">SafeBAE Certified Peer Educator</figcaption></figure>
  </div>
</section>

<section class="band band--mist" id="register">
  <div class="wrap st-reg">
    <div class="st-reg__side">
      <div class="st-reg__head">
        <p class="eyebrow">Student registration</p>
        <h2>Register for the training</h2>
        <p class="lede">Fill out a short interest form to get started. We’ll send you everything you need to begin the training.</p>
      </div>
      <div class="st-reg__links">{reg_links_html}</div>
    </div>
    <div class="st-reg__form">{reg_form}</div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="section-head"><div><h2>Put the training to work</h2><p class="lede lede--full" style="color:rgba(255,255,255,.88)">Certified Peer Educators lead presentations, run campaigns and start clubs. In college? Certified students are prioritized when paid mentorship opportunities become available. {a('College students', 'college.html', 'link')}</p></div></div>
    {journey('Train')}
    <div class="st-ai-strip reveal">
      <div class="st-ai-strip__date">Oct 26&ndash;30<small>Launches 2026</small></div>
      <div><h3>New: SafeBAE AI Literacy Training</h3><p>Six free, self-paced modules for high school and college students on how AI works, how feeds and AI shape what we see and believe, AI and healthy relationships, using AI well, fake images, and sextortion. It launches during U.S. Media Literacy Week.</p></div>
      {btn('About the training', 'ai-literacy.html', 'mint', arrow=True)}
    </div>
  </div>
</section>
{give_band()}
'''
    page('peer-educator.html', 'Certified Peer Educator Training · SafeBAE', 'Become a certified peer educator with SafeBAE. Free, self-paced training for students to lead consent education and sexual violence prevention.',
         body, active='resources', body_class='st st-pe', head_extra=f'<style>{CSS}{PE_CSS}</style>', scripts=PE_JS)


def build():
    students()
    peer_educator()


if __name__ == '__main__':
    build()
