"""Adults group (v3): adults.html and parents.html.
Content carried from the live safebae.org pages (get-involved, parents), the Check Their Vibe
adult guide PDF and the site FAQ answers already in data.py.
(educators, college, request, donate, chip-in and fundraise build from pages_adults2 / pages_programs.)"""
from lib import *
from data import FAQ, PODCASTS, WP
from pages_home import FILMS, film_font_link

GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
AI_URL = 'https://ai-literacy.safebae.org'
CH_URL = 'https://chokinghazard.org'
AI_TOPICS = 'how AI works, how feeds and AI shape what we see and believe, AI and healthy relationships, using AI well, fake images, and sextortion'


def faq(q):
    for _, items in FAQ:
        for qq, aa, link in items:
            if qq == q:
                return aa, link
    raise KeyError(q)


def film(key):
    return next(f for f in FILMS if f[1] == key)


def film_card(key, go='Film + guide', cls=''):
    """A film still in its original colour, with the title set in the film's own typeface on a caption bar."""
    href, k, title, im, tag = film(key)
    return (f'<a class="ad-film ad-film--{k} {cls}" href="{href}"><span class="ad-film__img">{img(im, "")}</span>'
            f'<span class="ad-film__cap"><span class="ad-film__tag">{esc(tag)}</span><span class="ad-film__title">{esc(title)}</span>'
            f'<span class="ad-film__go">{go}<i aria-hidden="true">&rarr;</i></span></span></a>')


CSS = '''
/* ---------- grid: 12 columns inside the wrap ---------- */
.ad-g{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap)}
.ad-g > *{min-width:0}
.ad-c3{grid-column:span 3} .ad-c4{grid-column:span 4} .ad-c5{grid-column:span 5} .ad-c6{grid-column:span 6} .ad-c7{grid-column:span 7} .ad-c8{grid-column:span 8} .ad-c9{grid-column:span 9}
.ad-pr{padding-right:clamp(0px,calc(6vw - 46px),40px)}
.ad-pl{padding-left:clamp(0px,calc(6vw - 46px),40px)}
.ad-col{display:flex; flex-direction:column}
.ad-col > .btns:last-child{margin-top:auto; padding-top:22px}
@media (max-width:900px){
  .ad-g{grid-template-columns:minmax(0,1fr)} .ad-g > *{grid-column:auto} .ad-pr{padding-right:0} .ad-pl{padding-left:0}
  /* small screens: heading, then media, then text, then actions */
  .ad-g.ad-g--m{display:flex; flex-direction:column; align-items:stretch; gap:0}
  .ad-g--m > .ad-txt{display:contents}
  .ad-g--m > .ad-txt > *{order:3}
  .ad-g--m > .ad-txt > :is(.crumbs,.eyebrow,h1,h2,.ad-vmark){order:1}
  .ad-g--m > .ad-txt > .eyebrow{align-self:flex-start}
  .ad-g--m > .ad-media{order:2; margin-block:10px 26px}
}

/* ---------- shared pieces ---------- */
.ad main .eyebrow{color:var(--logo-teal)}
.ad main :is(.band--slate,.band--deep,.ad-hub) .eyebrow{color:var(--mint)}
.ad main .band--teal .eyebrow{color:#fff}
.ad-lede-light{color:rgba(255,255,255,.9)}
.ad-mini{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); display:block}
:is(.band--slate,.band--deep) .ad-mini,.ad-dark .ad-mini{color:var(--mint)}
.ad-shot{margin:0}
.ad-shot .sticker{position:absolute; left:16px; bottom:18px; z-index:1; font-size:clamp(.74rem,1.05vw,.9rem); max-width:calc(100% - 32px)}
.ad-checks{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.ad-checks li{position:relative; padding-left:28px; margin:0}
.ad-checks li::before{content:""; position:absolute; left:2px; top:.5em; width:11px; height:11px; background:var(--teal); transform:rotate(45deg); border-radius:2px}
:is(.band--slate,.band--deep,.band--teal) .ad-checks li::before{background:var(--mint)}
.ad-tabs{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:var(--gap)}
.ad-tabs .tab{min-height:46px; padding:10px 18px; transition:background .2s, border-color .2s, color .2s}
.ad-zoom{position:relative; border:0; padding:0; background:none; cursor:zoom-in; display:block; width:100%; color:inherit; font:inherit; text-align:left}
.ad-zoom img{width:100%; transition:transform .35s var(--ease)}
.ad-zoom:hover img{transform:scale(1.015)}
.ad-zoom small{display:block; margin-top:10px; font-size:.9rem; font-weight:600; line-height:1.4}

@media (max-width:900px){.ad main .btn--sm{min-height:44px}}

/* film card: the still stays in its original colour; the title sits on its own bar in the film's typeface */
.ad-film{display:flex; flex-direction:column; border-radius:var(--r-xl); overflow:hidden; background:#0e252c; color:#fff; text-decoration:none; min-width:0; box-shadow:var(--shadow-soft); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ad .ad-film{color:#fff}
.ad-film:hover{transform:translateY(-5px); box-shadow:0 28px 50px -28px rgba(22,53,64,.75)}
.ad-film__img{display:block; position:relative; aspect-ratio:16/10; overflow:hidden; background:#000; flex:none}
.ad-film__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transform:scale(var(--z,1)); transform-origin:var(--zo,50% 50%); transition:transform .6s var(--ease)}
.ad-film:hover .ad-film__img img{transform:scale(calc(var(--z,1) * 1.05))}
.ad-film__cap{display:flex; flex-direction:column; gap:9px; padding:16px 18px 17px; flex:1; border-top:3px solid var(--mint)}
.ad-film__tag{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua); line-height:1.3}
.ad-film__title{font-size:calc(var(--fs,1.42rem) * var(--ft,1)); line-height:1.06; text-wrap:balance}
.ad-film__go{margin-top:auto; padding-top:4px; display:inline-flex; gap:.5em; align-items:center; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint)}
.ad-film__go i{font-style:normal; transition:transform .2s var(--ease)}
.ad-film:hover .ad-film__go i{transform:translateX(4px)}
.ad-film--red .ad-film__title{font-family:'Tilt Neon',sans-serif; text-transform:uppercase; color:#ffd9d9; text-shadow:0 0 6px #fe7171, 0 0 18px #fe7171, 0 0 34px rgba(254,113,113,.7); --fs:1.5rem}
.ad-film--bae .ad-film__title{font-family:'Silkscreen',monospace; color:#ffd2d2; text-shadow:2px 2px 0 var(--teal); --fs:1.24rem; line-height:1.15}
.ad-film--know .ad-film__title{font-family:'Rubik Mono One',sans-serif; color:var(--mint); --fs:1.16rem; line-height:1.15; overflow-wrap:anywhere}
.ad-film--date .ad-film__title{font-family:'Nunito',sans-serif; font-weight:800; color:var(--aqua); text-transform:lowercase; --fs:1.5rem}
.ad-film--oh .ad-film__title{font-family:'DotGothic16',sans-serif; color:var(--mint); text-transform:uppercase; --fs:1.2rem; line-height:1.12}
.ad-film--rc .ad-film__title{font-family:'Zilla Slab',serif; font-weight:700; --fs:1.5rem}
.ad-film--men .ad-film__title{font-family:'Saira Stencil One',sans-serif; letter-spacing:.05em; text-transform:uppercase; --fs:1.3rem; line-height:1.1}
.ad-film--rrcr .ad-film__title{font-family:'DM Serif Display',serif; --fs:1.5rem}
.ad-film--rrcr .ad-film__img img{object-position:50% 20%}
.ad-film--date .ad-film__img{--z:1.26; --zo:50% 0%}
.ad-film--rc .ad-film__img img{object-position:72% 30%}
.ad-film--men .ad-film__img img{object-position:22% 30%}

/* Vibe Check: full teal band */
.ad-vibe{align-items:center}
.ad-vmark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:#fff; margin-bottom:16px}
.ad-vmark .daisy{width:38px; height:38px; color:var(--mint)}
.ad-vibe h2{font-size:clamp(2.1rem,4vw,3.5rem); font-stretch:112%; font-weight:900; letter-spacing:-.02em; overflow-wrap:break-word}
.ad-vibe .lede{color:#fff}
.ad-vibe p{color:#fff}
.ad-vibe .btns{margin-top:26px}
.ad-vibe .arrow-link{color:#fff; min-height:48px; padding-inline:6px}
.ad-vibe .arrow-link::after{color:var(--mint)}
@media (max-width:520px){.ad-vibe h2{font-size:1.95rem; font-stretch:108%}}

/* =====================================================================
   adults.html
   ===================================================================== */
.ad-hub{background:var(--slate) var(--grain); color:#fff; position:relative; overflow:hidden}
.ad-hub > .wrap{position:relative; z-index:1; padding-block:clamp(48px,6vw,88px); align-items:stretch}
.ad-hub .wm-daisy{right:-12%; bottom:-40%}
.ad-hub .crumbs{margin-bottom:20px}
.ad-hub__txt{display:flex; flex-direction:column; justify-content:center; padding-right:clamp(0px,1.4vw,20px)}
.ad-h1{font-size:clamp(2.4rem,4.4vw,4rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .4em}
.ad-hub .mk{background:none; color:var(--mint); white-space:nowrap}
.ad-hub .lede{margin-bottom:1.4em}
.ad-mosaic{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:minmax(0,1.4fr) minmax(0,1fr); gap:12px; min-height:clamp(380px,35vw,500px)}
.ad-mosaic a{position:relative; display:block; border-radius:16px; overflow:hidden; background:var(--slate-deep); min-height:0; box-shadow:0 30px 60px -34px rgba(0,0,0,.7)}
.ad-mosaic a:first-child{grid-column:1/3}
.ad-mosaic img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.ad-mosaic a:hover img{transform:scale(1.05)}
.ad-mosaic a:nth-child(1) img{object-position:50% 24%}
.ad-mosaic a:nth-child(2) img{object-position:62% 30%}
.ad-mosaic a:nth-child(3) img{object-position:50% 40%}
.ad-mosaic .sticker{position:absolute; left:12px; bottom:14px; font-size:.8rem; transition:transform .25s var(--ease)}
.ad-mosaic a:hover .sticker{transform:rotate(0) translateY(-2px)}
@media (max-width:900px){.ad-mosaic{min-height:0; height:clamp(300px,74vw,440px)}}
@media (max-width:520px){.ad-h1{font-size:clamp(1.8rem,8.6vw,2.4rem)}}

/* role cards: rows shared across the three cards (subgrid), so labels, titles, text, links and buttons line up */
.ad-routes{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-rows:repeat(6,auto); gap:0 var(--gap)}
.ad-route{display:grid; grid-template-rows:subgrid; grid-row:span 6; row-gap:0; border-radius:var(--r-xl); overflow:hidden; background:#fff; border:1px solid var(--line); box-shadow:var(--shadow-soft); min-width:0; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ad-route:hover{transform:translateY(-4px); box-shadow:0 30px 54px -30px rgba(22,53,64,.6)}
.ad-route__img{display:block; position:relative; aspect-ratio:3/2; overflow:hidden; background:var(--slate)}
.ad-route__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.ad-route:hover .ad-route__img img{transform:scale(1.04)}
.ad-route__body{display:grid; grid-template-rows:subgrid; grid-row:span 5; row-gap:0; padding:22px var(--pad-card) var(--pad-card); min-width:0}
.ad-route__body .ad-mini{margin-bottom:8px}
.ad-route__body h3{margin:0 0 10px; font-size:clamp(1.3rem,1.7vw,1.5rem)}
.ad-route__body h3 a{text-decoration:none; color:inherit}
.ad-route__body > p{margin:0 0 16px; color:var(--ink-soft); font-size:.98rem; line-height:1.55}
.ad-route__links{list-style:none; padding:0; margin:0; border-top:1px solid var(--line); align-self:start}
.ad-route__links li{margin:0}
.ad-route__links a{display:flex; justify-content:space-between; gap:12px; align-items:center; min-height:46px; padding:9px 2px; border-bottom:1px solid var(--line); text-decoration:none; font-weight:700; font-size:.95rem; line-height:1.3; color:var(--logo-teal); transition:background .15s, padding .2s var(--ease)}
.ad-route__links a::after{content:"\\2192"; color:var(--teal); transition:transform .2s var(--ease)}
.ad-route__links a:hover{background:var(--mist); padding-inline:8px}
.ad-route__links a:hover::after{transform:translateX(3px)}
.ad-route__foot{padding-top:20px; align-self:end}
@media (max-width:1000px){
  .ad-routes{grid-template-columns:minmax(0,1fr); grid-template-rows:none; gap:var(--gap)}
  .ad-route{grid-template-rows:none; grid-row:auto; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)}
  .ad-route__img{aspect-ratio:auto; min-height:280px}
  .ad-route__body{grid-template-rows:none; grid-row:auto; display:flex; flex-direction:column}
  .ad-route__foot{margin-top:auto; align-self:flex-start}
}
@media (max-width:620px){.ad-route{grid-template-columns:minmax(0,1fr)} .ad-route__img{aspect-ratio:16/10; min-height:0}}

/* what a school can book */
.ad-book{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.ad-book__photo{grid-column:1; margin:0}
.ad-book__photo img{object-position:50% 40%}
.ad-book__grid{grid-column:2/4; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:var(--gap)}
.ad-prog{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:14px; align-items:center; padding:18px 20px 18px 22px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); text-decoration:none; min-height:104px; transition:background .2s, border-color .2s, transform .2s var(--ease)}
.ad-prog b{display:block; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.28rem; line-height:1.15; color:#fff}
.ad-prog small{display:block; margin-top:5px; font-size:.95rem; line-height:1.4; color:rgba(255,255,255,.82)}
.ad-prog i{font-style:normal; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:rgba(209,254,255,.14); color:var(--mint); font-weight:800; transition:background .2s, color .2s, transform .2s var(--ease)}
.ad-prog:hover{background:rgba(21,255,200,.1); border-color:var(--mint); transform:translateY(-2px)}
.ad-prog:hover i{background:var(--mint); color:var(--slate); transform:translateX(3px)}
.ad-prog--360{background:var(--mint); border-color:var(--mint)}
.ad-prog--360 b{color:var(--slate)} .ad-prog--360 small{color:var(--slate)}
.ad-prog--360 i{background:var(--slate); color:var(--mint)}
.ad-prog--360:hover{background:var(--aqua); border-color:var(--aqua)}
.ad-prog--360:hover i{background:var(--slate); color:var(--mint)}
.ad-book__note{margin:var(--gap) 0 0; color:rgba(255,255,255,.82)}
@media (max-width:900px){.ad-book{grid-template-columns:minmax(0,1fr)} .ad-book__photo{grid-column:auto; min-height:0; aspect-ratio:16/9} .ad-book__grid{grid-column:auto}}
@media (max-width:620px){.ad-book__grid{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto} .ad-prog{min-height:0}}

/* new-program cards */
.ad-new{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.ad-new__card{display:flex; flex-direction:column; border-radius:var(--r-xl); overflow:hidden; background:#fff; border:1px solid var(--line); box-shadow:var(--shadow-soft); min-width:0}
.ad-new__media{position:relative; height:clamp(200px,18vw,250px); overflow:hidden; background:var(--slate-deep) var(--grain); display:grid; place-items:center; flex:none}
.ad-new__media > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.ad-new__media .ad-hzbox{width:min(62%,340px)}
.ad-date{position:absolute; left:18px; top:18px; width:92px; border-radius:14px; overflow:hidden; text-align:center; background:#fff; color:var(--slate); border:2.5px solid var(--slate); box-shadow:4px 4px 0 var(--slate); transform:rotate(-3deg)}
.ad-date b{display:block; background:var(--slate); color:var(--mint); font-family:var(--mono); font-size:.74rem; letter-spacing:.14em; padding:5px 0 4px}
.ad-date span{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.55rem; line-height:1; padding:10px 4px 11px; letter-spacing:-.02em}
.ad-new__body{padding:var(--pad-card); display:flex; flex-direction:column; gap:12px; flex:1}
.ad-new__body h3{font-size:clamp(1.4rem,2vw,1.7rem); margin:0}
.ad-new__body p{margin:0; color:var(--ink-soft)}
.ad-new__body .btns{margin-top:auto; padding-top:10px}
.ad-new__body .btn{padding-inline:.95em; font-size:.96rem}
@media (max-width:860px){.ad-new{grid-template-columns:minmax(0,1fr)}}

/* adults' guide cover */
.ad-q{margin:22px 0 0; padding-left:18px; border-left:4px solid var(--mint); font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.15rem; line-height:1.4}
.ad-q cite{display:block; margin-top:8px; font-style:normal; font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase}
.ad-guidecover{position:relative; width:min(100%,400px); margin-inline:auto}
.ad-guidecover a{display:block}
.ad-guidecover img{width:100%; border-radius:8px; box-shadow:0 40px 70px -30px rgba(0,0,0,.6); transform:rotate(3deg); background:#fff; transition:transform .4s var(--ease)}
.ad-guidecover a:hover img{transform:rotate(1deg) translateY(-6px)}
.ad-guidecover .sticker{position:absolute; left:-14px; bottom:34px}
@media (max-width:900px){.ad-guidecover{width:min(78%,330px)} .ad-guidecover .sticker{font-size:.76rem; left:-10px}}

/* film grid */
.ad-films{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
@media (max-width:1180px){.ad-films{--ft:.8} .ad-films .ad-film__cap{padding-inline:15px}}
@media (max-width:960px){.ad-films{grid-template-columns:repeat(2,minmax(0,1fr)); --ft:1}}
@media (max-width:520px){
  .ad-films{grid-template-columns:minmax(0,1fr); gap:12px}
  .ad-films .ad-film{flex-direction:row; border-radius:16px}
  .ad-films .ad-film__img{aspect-ratio:auto; width:38%; min-height:124px}
  .ad-films .ad-film__cap{border-top:0; border-left:3px solid var(--mint); padding:13px 14px; gap:6px}
  .ad-films{--ft:.82}
  .ad-films .ad-film--red .ad-film__img img{object-fit:contain}
}
.ad-also{display:flex; flex-wrap:wrap; align-items:center; gap:8px 10px; margin-top:var(--gap)}
.ad-also .ad-mini{margin-right:6px}
.ad-also a{display:inline-flex; align-items:center; min-height:44px; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:.98rem; text-decoration:none; padding:8px 16px; border-radius:999px; border:2px solid var(--line); color:var(--logo-teal); background:#fff; transition:border-color .2s, background .2s}
.ad-also a:hover{border-color:var(--teal); background:var(--mist)}

/* =====================================================================
   parents.html
   ===================================================================== */
.ad-phero.phero--split .wrap{grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ad-phero h1{font-size:clamp(2.4rem,5.2vw,4.7rem)}
.ad-phero :focus-visible{outline-color:var(--teal)}
.ad-phero .ad-txt{display:flex; flex-direction:column; justify-content:center}
.ad-phero .ad-txt > p:not(.lede){max-width:none}
.ad-phero .lede{text-wrap:balance}
.ad-phero .btns{margin-top:10px}
.ad-phero .phero__media{position:relative; align-self:center; aspect-ratio:1/1}
.ad-phero.phero--split .phero__media img{position:absolute; inset:0; width:100%; height:100%; aspect-ratio:auto; object-fit:cover; object-position:64% 40%}
.ad-phero.phero--split .phero__media .sticker{left:-14px; bottom:26px}
.ad-phero .phero__wm{right:-14%; bottom:-46%}
@media (max-width:900px){
  .ad-phero.phero--split .wrap{display:flex; flex-direction:column; gap:0}
  .ad-phero .ad-txt{display:contents}
  .ad-phero .ad-txt > *{order:3}
  .ad-phero .ad-txt > :is(.crumbs,h1){order:1}
  .ad-phero.phero--split .phero__media{order:2; align-self:stretch; width:100%; max-width:none; min-height:0; aspect-ratio:4/3; margin-block:6px 26px}
  .ad-phero.phero--split .phero__media .sticker{left:10px}
}

/* podcast */
.ad-pod{grid-template-columns:minmax(0,270px) minmax(0,1fr); gap:clamp(24px,3.6vw,52px); align-items:center}
.ad-pod > *{grid-column:auto}
.ad-pod__art img{width:100%; aspect-ratio:1; object-fit:cover; border-radius:var(--r-xl); box-shadow:0 30px 50px -26px rgba(0,0,0,.75)}
.ad-pod h2{font-size:clamp(1.7rem,3vw,2.5rem); margin-bottom:.35em}
.ad-pod__txt > p:not(.eyebrow){color:rgba(255,255,255,.88); margin:0}
.ad-pod__row{display:flex; flex-wrap:wrap; align-items:center; gap:14px 24px; margin-top:22px}
.ad-pod__play{flex:0 1 auto; min-width:0}
.ad-pod__play:has(iframe){flex:1 1 100%}
.ad-play{display:inline-flex; align-items:center; gap:14px; padding:9px 24px 9px 9px; border-radius:999px; background:var(--mint); text-decoration:none; box-shadow:0 4px 0 rgba(0,0,0,.22); transition:transform .18s var(--ease), box-shadow .18s}
.ad .ad-pod .ad-play{color:var(--slate)}
.ad-play:hover{transform:translateY(-2px); box-shadow:0 6px 0 rgba(0,0,0,.22)}
.ad-play__dot{flex:none; width:46px; height:46px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center}
.ad-play__dot svg{width:20px; height:20px; margin-left:3px}
.ad-play b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.05rem; line-height:1.15}
.ad-play small{display:block; font-size:.9rem; font-weight:600; line-height:1.3}
.ad-pod__links{display:flex; flex-wrap:wrap; gap:8px 18px; font-weight:700; font-size:.95rem}
.ad-pod__links a{display:inline-flex; align-items:center; min-height:44px}
@media (max-width:900px){.ad-pod{grid-template-columns:150px minmax(0,1fr); gap:22px; align-items:start}}
@media (max-width:560px){.ad-pod{grid-template-columns:minmax(0,1fr)} .ad-pod__art{max-width:132px}}

/* early conversations */
.ad-early .lede{margin-bottom:1em}
.ad-hl{background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:20px 24px; margin-top:24px}
.ad-hl b{font-family:var(--display); font-stretch:108%; font-size:1.25rem; line-height:1.15; display:block; margin-bottom:6px}
.ad-hl p{margin:0}
.ad-early .ad-shot img{object-position:70% 60%}
.ad-ways{margin-top:clamp(36px,5vw,64px); align-items:stretch}
.ad-ways__poster{display:flex}
.ad-ways__poster .ad-zoom{display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; background:var(--aqua); border-radius:var(--r-xl); padding:clamp(18px,2.4vw,30px) clamp(18px,2.4vw,30px) 20px; height:100%; text-align:center}
.ad-ways__poster img{width:min(100%,300px); height:auto; border-radius:8px; box-shadow:0 24px 40px -22px rgba(22,53,64,.6); transform:rotate(-2.5deg)}
.ad-ways__poster .ad-zoom:hover img{transform:rotate(-1deg) scale(1.02)}
.ad-ways__poster small{margin:0; color:var(--logo-teal)}
.ad-ways h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin-bottom:.3em}
.ad-ways__lede{margin:0 0 20px; font-size:1.08rem; color:var(--ink-soft)}
.ad-ways__list{margin:0; border-top:1px solid var(--line)}
.ad-ways__body{display:flex; flex-direction:column}
.ad-ways__list{display:flex; flex-direction:column; flex:1 1 auto}
.ad-ways__list > div{flex:1 1 auto; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,2fr); gap:var(--gap); align-content:center; padding:18px 0; border-bottom:1px solid var(--line)}
.ad-ways__list dt{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.22rem; line-height:1.18; color:var(--logo-teal)}
.ad-ways__list dd{margin:0; color:var(--ink-soft); line-height:1.55}
.ad-ways__end{margin:var(--gap) 0 0; padding:20px var(--pad-card); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); font-weight:600; font-size:1.08rem}
@media (max-width:900px){.ad-ways__poster img{width:min(60%,220px)}}
@media (max-width:620px){.ad-ways__list > div{grid-template-columns:minmax(0,1fr); gap:6px}}

/* Choking Hazard */
.ad-choke{align-items:center}
.ad-inside{margin:22px 0 0; padding:18px 0 0; border-top:1px solid var(--line-dark)}
.ad-inside .ad-mini{margin-bottom:12px}
.ad-inside ul{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px var(--gap); font-weight:600}
.ad-choke .btns{margin-top:26px}
.ad-choke__sign{display:grid; gap:clamp(22px,2.6vw,34px); justify-items:start; padding-left:clamp(0px,2vw,28px)}
.ad-choke__sign .ad-hzbox{width:100%; padding:10px 14px 0 6px}
.ad-hz__line{margin:0; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.6rem,2.7vw,2.3rem); line-height:1.04; letter-spacing:-.01em; color:#fff}
@media (max-width:900px){.ad-choke__sign{padding-left:0; max-width:460px}}
@media (max-width:480px){.ad-inside ul{grid-template-columns:minmax(0,1fr)}}

/* topics */
.ad-topic{background:#fff; border-radius:var(--r-xl); padding:var(--pad-card); border:1px solid var(--line); box-shadow:var(--shadow-soft)}
.ad-topic__txt{display:flex; flex-direction:column}
.ad-topic__txt .ad-mini{margin-bottom:10px}
.ad-topic h3{font-size:clamp(1.35rem,2vw,1.7rem); margin-bottom:.45em}
.ad-topic__txt p{margin:0 0 .9em}
.ad-subq{font-size:1.2rem; color:var(--logo-teal); margin:.5em 0 .4em}
.ad-topic__more{margin:auto 0 0!important; padding-top:10px}
.ad-topic__more .arrow-link{min-height:44px}
.ad-topic .ad-film{height:100%; box-shadow:none}
.ad-topic .ad-film:hover{transform:translateY(-3px)}
.ad-topic .ad-film__img{aspect-ratio:auto; flex:1 1 auto; min-height:170px}
.ad-topic .ad-film__cap{flex:none}
.ad-signs{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); margin-top:var(--gap)}
.ad-signs > div{border-radius:14px; padding:20px 22px 22px; background:var(--mist); border:1px solid var(--line)}
.ad-signs > div:last-child{background:var(--slate); color:#fff; border-color:var(--slate)}
.ad-signs h4{margin:0 0 12px; font-size:1.15rem}
.ad-signs .chips{gap:8px}
.ad-signs .chip{white-space:normal; background:#fff; font-size:.74rem; padding:.5em .75em; line-height:1.3}
.ad-signs > div:last-child .chip{background:rgba(255,255,255,.12); color:#fff}
@media (max-width:900px){.ad-topic .ad-film__img{min-height:0; aspect-ratio:16/9; flex:none}}
@media (max-width:620px){.ad-signs{grid-template-columns:minmax(0,1fr)}}

/* supporting a survivor */
.ad-support__top{align-items:center}
.ad-support .btns{margin-top:24px}
.ad-support__side .ad-zoom img{border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.ad-support__side .ad-zoom small{color:var(--aqua)}
.ad-acts{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); margin-top:clamp(32px,4vw,52px)}
.ad-acts > div{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,8fr); gap:8px 20px; align-items:start; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-left:5px solid var(--mint); border-radius:14px; padding:20px 24px}
.ad-acts b{display:block; font-family:var(--display); font-stretch:110%; font-weight:900; font-size:1.45rem; line-height:1.08; color:var(--mint)}
.ad-acts p{margin:0; color:rgba(255,255,255,.9); line-height:1.5}
.ad-helpbar{margin-top:var(--gap); display:grid; grid-template-columns:minmax(0,1fr) auto auto; gap:16px clamp(20px,3vw,44px); align-items:center; background:var(--coral); color:var(--slate); border-radius:var(--r-xl); padding:22px var(--pad-card)}
.ad-helpbar > div > b{display:block; font-family:var(--display); font-stretch:110%; font-weight:900; font-size:1.5rem; line-height:1.1; margin-bottom:4px}
.ad-helpbar > div > span{display:block; font-weight:600; line-height:1.45}
.ad-helpbar ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,auto); gap:12px 28px}
.ad-helpbar li{margin:0; padding-left:18px; border-left:2px solid rgba(29,65,78,.35)}
.ad-helpbar li small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600}
.ad-helpbar li strong{display:block; white-space:nowrap; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.18rem; line-height:1.2; margin-top:2px}
@media (max-width:1100px){.ad-helpbar{grid-template-columns:minmax(0,1fr) auto} .ad-helpbar ul{grid-column:1/-1; grid-row:2; justify-content:start}}
@media (max-width:760px){.ad-acts{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.ad-acts > div{grid-template-columns:minmax(0,1fr)} .ad-helpbar{grid-template-columns:minmax(0,1fr)} .ad-helpbar ul{grid-template-columns:minmax(0,1fr); grid-row:auto} .ad-helpbar li strong{white-space:normal} .ad-helpbar .btn{justify-self:start}}

/* reporting options */
.ad-opts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); border:1px solid var(--line); border-top:6px solid var(--mint); border-radius:var(--r-xl); background:var(--mist); overflow:hidden}
.ad-opt{padding:var(--pad-card); border-left:1px solid var(--line); min-width:0}
.ad-opt:first-child{border-left:0}
.ad-opt b{display:block; font-family:var(--display); font-stretch:110%; font-weight:800; font-size:1.4rem; color:var(--logo-teal); line-height:1.1; margin-bottom:8px}
.ad-opt p{margin:0; color:var(--ink-soft); line-height:1.5}
@media (max-width:900px){.ad-opts{grid-template-columns:repeat(2,minmax(0,1fr))} .ad-opt:nth-child(3){border-left:0} .ad-opt:nth-child(n+3){border-top:1px solid var(--line)}}
@media (max-width:520px){.ad-opts{grid-template-columns:minmax(0,1fr)} .ad-opt{border-left:0} .ad-opt + .ad-opt{border-top:1px solid var(--line)}}
.ad-alt{margin-top:var(--gap); align-items:center; background:var(--aqua); border-radius:var(--r-xl); padding:clamp(22px,3.2vw,44px)}
.ad-alt h3{font-size:clamp(1.45rem,2.2vw,1.9rem)}
.ad-alt .btns{margin-top:20px}
.ad-alt .ad-zoom img{border-radius:14px; box-shadow:0 20px 40px -24px rgba(22,53,64,.5); background:#fff}
.ad-alt .ad-zoom small{color:var(--logo-teal)}
@media (max-width:900px){.ad-alt .ad-zoom{max-width:380px}}

/* Vibe Check on the parents page */
.ad-vfeats{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:24px 0 0}
.ad-vfeats div{background:var(--slate-deep); border-radius:14px; padding:16px 18px}
.ad-vfeats b{display:block; color:var(--mint); font-family:var(--display); font-stretch:108%; font-size:1.12rem; margin-bottom:3px}
.ad-vfeats span{font-size:.95rem; color:#fff; line-height:1.45; display:block}
.ad-phonewrap{position:relative; width:min(100%,400px); margin-inline:auto}
.ad-phone{position:relative; width:86%; margin-inline:auto; aspect-ratio:390/800; border-radius:46px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6); overflow:hidden; transform:rotate(4deg)}
.ad-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.ad-phonewrap .sticker{position:absolute; z-index:2}
@media (max-width:900px){.ad-phonewrap{width:min(78%,300px)}}
@media (max-width:520px){.ad-vfeats{grid-template-columns:minmax(0,1fr)}}

/* sharing Vibe Check */
.ad-share{align-items:stretch}
.ad-steps{list-style:none; margin:0; padding:0 var(--pad-card); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); display:flex; flex-direction:column}
.ad-steps li{flex:1 1 auto; margin:0; display:grid; grid-template-columns:56px minmax(0,1fr); column-gap:16px; align-content:center; padding:20px 0; border-top:1px solid var(--line)}
.ad-steps li:first-child{border-top:0}
.ad-steps__n{grid-row:1/3; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.7rem; line-height:.95; color:var(--teal)}
.ad-steps h3{font-size:1.25rem; margin:0 0 .3em; align-self:end}
.ad-steps p{margin:0; color:var(--ink-soft); line-height:1.55; align-self:start}
.ad-say{display:flex; flex-direction:column; gap:var(--gap)}
.ad-say > div{border-radius:var(--r-xl); padding:var(--pad-card)}
.ad-say__try{flex:1 1 auto; background:#fff; border:1px solid var(--line); display:flex; flex-direction:column; gap:12px}
.ad-bubble{margin:0; background:var(--mist); border:1px solid var(--line); border-radius:20px 20px 20px 5px; padding:16px 18px; font-family:var(--display); font-stretch:104%; font-weight:600; font-size:1.08rem; line-height:1.45}
.ad-say__try .ad-bubble + .ad-mini{margin-top:8px}
.ad-say__avoid{background:var(--slate); color:#fff}
.ad-say__avoid .ad-mini{margin-bottom:12px; color:var(--mint)}
.ad-say__avoid ul{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.ad-say__avoid li{margin:0; padding:11px 14px; border-radius:16px 16px 16px 4px; background:rgba(255,255,255,.08); font-weight:600; line-height:1.45; color:rgba(255,255,255,.9)}
.ad-say__avoid li span{background:linear-gradient(var(--coral),var(--coral)) no-repeat 0 58% / 100% 2px; -webkit-box-decoration-break:clone; box-decoration-break:clone; transition:background-size .7s var(--ease)}
.js .ad-say__avoid:not(.in) li span{background-size:0% 2px}
.ad-say__avoid li:nth-child(2) span{transition-delay:.18s} .ad-say__avoid li:nth-child(3) span{transition-delay:.36s} .ad-say__avoid li:nth-child(4) span{transition-delay:.54s}
.ad-starters{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.ad-starter{background:#fff; border-radius:var(--r-xl); padding:var(--pad-card); border:1px solid var(--line)}
.ad-starter h3{font-size:1.3rem; margin-bottom:.7em}
.ad-starter ul{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.ad-starter li{margin:0; padding:13px 16px; background:var(--mist); border:1px solid var(--line); border-radius:18px 18px 18px 5px; font-weight:600; line-height:1.45}
.ad-reminder{margin-top:var(--gap); display:flex; gap:16px 28px; align-items:center; justify-content:space-between; flex-wrap:wrap; background:var(--slate); color:#fff; border-radius:var(--r-xl); padding:22px var(--pad-card)}
.ad-reminder p{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.15rem; line-height:1.4; flex:1 1 420px; min-width:0}
@media (max-width:760px){.ad-starters{grid-template-columns:minmax(0,1fr)}}
@media (max-width:480px){.ad-steps li{grid-template-columns:42px minmax(0,1fr); column-gap:12px} .ad-steps__n{font-size:2.2rem}}

/* connect your student */
.ad-involve{align-items:stretch}
.ad-involve__lead{display:flex; flex-direction:column}
.ad-involve__lead .lede{color:rgba(255,255,255,.9); margin-bottom:1.3em}
.ad-involve .ad-shot{flex:1 1 auto; min-height:280px}
.ad-involve .ad-shot img{object-position:50% 45%}
.ad-involve .rows{align-content:space-between}
.ad-involve .row{padding-block:18px}
.ad-involve .row b{font-size:1.2rem}
.ad-involve .row small{font-size:.95rem; line-height:1.5; margin-top:4px}
.ad-involve .row .go{width:40px; height:40px}
@media (max-width:900px){.ad-involve .ad-shot{flex:none; aspect-ratio:16/10; min-height:0; margin-bottom:10px}}
'''

HEAD = f'<style>{CSS}</style>'

# the coral strike draws through each "avoid" line when the card scrolls into view
PARENTS_JS = r'''<script>(function(){
  var el = document.querySelector('.ad-say__avoid'); if(!el) return;
  if(!('IntersectionObserver' in window)){ el.classList.add('in'); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ el.classList.add('in'); io.disconnect(); } }); }, {threshold: .45});
  io.observe(el);
})();</script>'''


def hz_box(cls='hz--tilt'):
    return f'<div class="ad-hzbox">{hz_label(cls)}</div>'


# =====================================================================
# adults.html
# =====================================================================
def adults():
    routes = [
        ('us-reis-parent', 'For families', 'Parents & caregivers',
         'Start conversations about consent and boundaries early, know what to do if your child tells you something happened, and understand reporting and alternative justice options.',
         [('Early conversations about consent', 'parents.html#early'), ('If your child tells you', 'parents.html#support'), ('Sharing Vibe Check', 'parents.html#share')],
         'parents.html', 'For parents', '50% 35%'),
        ('img-3947', 'For teachers & staff', 'Educators',
         'Educators are asked to do a great deal in any given day, so SafeBAE offers tools for every level of use, from one class discussion to a whole-school model.',
         [('Films and teaching guides', 'library.html#guides'), ('Classroom posters', 'posters.html'), ('Consent Curriculum', 'consent-curriculum.html')],
         'educators.html', 'For educators', '60% 40%'),
        ('us-colah-campus', 'For college students', 'College students',
         'Mentor high school students, start a SafeBAE club on your own campus, and become a Certified Peer Educator.',
         [('Become a college mentor', 'college.html#mentor'), ('Start a campus club', 'clubs.html'), ('Certified Peer Educator Training', 'peer-educator.html')],
         'college.html', 'For college students', '60% 70%'),
    ]
    rc = ''
    for im, tag, h, p, links, href, lbl, pos in routes:
        lk = ''.join(f'<li>{a(esc(t), u)}</li>' for t, u in links)
        rc += f'''<article class="ad-route"><a class="ad-route__img" href="{href}" tabindex="-1" aria-hidden="true">{img(im, '', style='object-position:' + pos)}</a>
  <div class="ad-route__body"><span class="ad-mini">{esc(tag)}</span><h3>{a(esc(h), href)}</h3><p>{esc(p)}</p>
  <ul class="ad-route__links">{lk}</ul><div class="ad-route__foot">{btn(lbl, href, 'slate', 'sm', arrow=True)}</div></div></article>'''

    # the two new programs sit in the same grid, flagged with their launch dates
    progs = [
        ('Assemblies', 'Awareness events, always co-presented with youth leaders', 'assemblies.html', '', ''),
        ('Consent Curriculum', '15 modules aligned with the National Health Education Standards', 'consent-curriculum.html', '', ''),
        ('Faculty & Staff Training', 'Trauma-informed professional development', 'professional-development.html', '', ''),
        ('Policy Reform Guide', 'For administrators and districts', 'policy-reform-guide.html', '', ''),
        ('Accountability Training', 'For students who have caused harm', 'accountability-training.html', '', ''),
        ('Sexual Strangulation Prevention', 'On sexual strangulation, which young people call “choking”', 'choking-hazard.html#schools', ' ad-prog--new', 'New &middot; November 2026'),
        ('AI Literacy Training', 'Six free, self-paced modules for anyone 13 or older', 'ai-literacy.html', ' ad-prog--new', 'New &middot; Oct 26&ndash;30, 2026'),
        ('How 360° Schools works', 'The whole-school approach behind every program', '360-schools.html', ' ad-prog--360', ''),
    ]
    ph = ''.join(f'<a class="ad-prog{c}" href="{h}"><span>{f"<em>{n}</em>" if n else ""}<b>{esc(t)}</b><small>{esc(d)}</small></span><i aria-hidden="true">&rarr;</i></a>' for t, d, h, c, n in progs)
    films = ''.join(film_card(k, 'Four lessons' if k == 'rrcr' else 'Film + guide') for _h, k, *_r in FILMS)

    body = f'''
<section class="ad-hub">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap ad-g ad-g--m">
    <div class="ad-c7 ad-txt ad-hub__txt rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>Adults</span></nav>
      <h1 class="ad-h1">For adults who support <span class="mk">young people</span></h1>
      <p class="lede ad-lede-light">Parents, caregivers and trusted adults play a critical role in shaping how young people understand safety, consent and relationships. SafeBAE’s work is youth-led, and prevention is a whole-community commitment. There’s more than one way to be part of it.</p>
      <div class="btns">{btn('Bring SafeBAE to your school', 'request-a-program.html', 'mint', arrow=True)}{btn('Adult guide to Vibe Check', GUIDE_PDF, 'ghost')}</div>
    </div>
    <div class="ad-c5 ad-media ad-mosaic">
      <a href="parents.html">{img('us-sometale-parent', 'A mother and her teenage son walking together', loading='eager')}<span class="sticker">Parents</span></a>
      <a href="educators.html">{img('img-2395', 'SafeBAE educators leading a classroom presentation', loading='eager')}<span class="sticker sticker--aqua sticker--r">Educators</span></a>
      <a href="college.html">{img('1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'A group of college-age SafeBAE supporters', loading='eager')}<span class="sticker sticker--white">College</span></a>
    </div>
  </div>
</section>

<section class="band band--paper" id="roles">
  <div class="wrap">
    <div class="section-head"><div><h2>Find what fits your role</h2></div></div>
    <div class="ad-routes reveal">{rc}</div>
  </div>
</section>

<section class="band band--slate" id="programs">
  <div class="wrap">
    <div class="section-head"><div><h2>Bring SafeBAE to your school, campus or community</h2>
      <p class="lede lede--full ad-lede-light">Many school partners start with an {a('assembly', 'assemblies.html')} or awareness event, always co-presented with youth leaders. SafeBAE 360° Schools builds lasting prevention infrastructure across the whole school community, and every component can start small and grow over time. Pricing is on a flexible sliding scale, because cost should never be a barrier to prevention.</p></div>{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}</div>
    <div class="ad-book reveal">
      <figure class="ad-book__photo ad-shot fill-img">{img('066', 'SafeBAE presenters with students in a school auditorium after an assembly')}<span class="sticker">Youth co-presenters</span></figure>
      <div class="ad-book__grid">{ph}</div>
    </div>
  </div>
</section>

<section class="band band--paper" id="library">
  <div class="wrap">
    <div class="section-head"><div><h2>Youth-made films with ready-to-teach guides</h2>
      <p class="lede lede--full">Every film is paired with a teaching guide. Use them in a classroom, a club meeting or at home.</p></div>{btn('Open the Library', 'library.html', 'mint', arrow=True)}</div>
    <div class="ad-films reveal">{films}</div>
    <div class="ad-also"><span class="ad-mini">Also in the Library</span><a href="library.html#films">Films &amp; videos</a><a href="library.html#guides">Teaching guides</a><a href="library.html#podcasts">Podcasts</a><a href="posters.html">Posters</a></div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-g ad-g--m ad-vibe">
    <div class="ad-c7 ad-txt">
      <div class="ad-vmark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <h2>Check Their Vibe: an adults’ guide to Vibe Check</h2>
      <p class="lede">Vibe Check is a free, private, self-guided reflection tool for young people navigating moments of sexual uncertainty. The guide helps you introduce it thoughtfully, follow up with care, and understand what it actually contains.</p>
      <p>Vibe Check is designed to be used privately and voluntarily. It should never be assigned. No accounts, no names, and nothing is stored.</p>
      <blockquote class="ad-q">“As the founding Executive Director of SafeBAE and a mom, this might be the most important tool we’ve developed.”<cite>Shael Norris</cite></blockquote>
      <div class="btns">{btn('Read the adults’ guide', 'vibe-check.html#adults', 'mint', arrow=True)}{btn('Download the PDF', GUIDE_PDF, 'white')}{a('Open Vibe Check', 'https://checkyourvibe.org/', 'arrow-link')}</div>
    </div>
    <div class="ad-c5 ad-media"><div class="ad-guidecover"><a href="{GUIDE_PDF}" target="_blank" rel="noopener" aria-label="Open Check Their Vibe, the adults’ guide to Vibe Check (PDF)">{img('guide-vibe-check', 'Cover of Check Their Vibe: An Adults’ Guide to Vibe Check')}</a><span class="sticker sticker--white">For parents &amp; adult allies</span></div></div>
  </div>
</section>
'''
    page('adults.html', 'For Adults · SafeBAE', 'Tools for parents, caregivers, educators and college students who support young people: conversations, classroom resources, mentoring and programs for schools.',
         body, active='adults', fonts=film_font_link(), head_extra=HEAD, body_class='ad')


# =====================================================================
# parents.html
# =====================================================================
def parents():
    pod = next(p for p in PODCASTS if p[0] == '4jjztQt08zjUR9guFgJ56x')
    early_items = [
        ('Offer alternatives to hugs', 'Encourage toddlers to greet adults in ways that feel comfortable to them: waving, blowing a kiss, or saying hello. This builds a lifelong foundation of bodily autonomy.'),
        ('Normalize consent in classrooms', 'Teachers can give elementary students options for how they’d like to be greeted, showing that personal boundaries matter everywhere.'),
        ('Use accurate words for anatomy', 'Avoid “cute” or made-up words. Real terms help children understand there is no shame in their bodies and equip them to clearly communicate if something inappropriate happens.'),
    ]
    ei = ''.join(f'<div><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in early_items)

    # topics to talk through together (answers are SafeBAE's FAQ text)
    c1, _l1 = faq('What is consent?'); c2, _ = faq('Can someone give consent if they’re drunk or high?')
    n1, _l3 = faq('What are the risks of sending nudes?')
    b1, _l4 = faq('What is bystander intervention?')
    healthy = ['Open communication', 'Mutual respect', 'Trust', 'Shared decisions', 'Feeling safe', 'Healthy boundaries', 'Respectful disagreements', 'Enjoying time apart', 'Inspiring each other']
    warning = ['Guilt trips', 'Isolating you from family and friends', 'Unreasonable jealousy', 'Constant put-downs', '“If you love me, you will…”', 'Threats', 'Intimidation', 'Manipulation', 'Gaslighting', 'Love-bombing']
    signs = f'''<div class="ad-signs"><div><h4>Healthy signs</h4><div class="chips">{''.join(f'<span class="chip">{esc(x)}</span>' for x in healthy)}</div></div>
         <div><h4>Warning signs</h4><div class="chips">{''.join(f'<span class="chip">{esc(x)}</span>' for x in warning)}</div></div></div>'''
    topics = [
        ('consent', 'Consent', 'What is consent?', f'<p>{esc(c1)}</p><h4 class="ad-subq">Can someone give consent if they’re drunk or high?</h4><p>{esc(c2)}</p>', 'faq.html#q-what-is-consent', 'rc', ''),
        ('relationships', 'Healthy vs. unhealthy relationships', 'What does a healthy relationship look like, and what are the warning signs?',
         '<p>In a healthy relationship, partners respect each other and stay independent people. Look at the whole relationship, not one good or bad moment.</p>'
         '<p>Abuse can be physical, sexual, psychological, emotional, or financial. One out of three teens will be in an abusive relationship.</p>',
         'faq.html#q-what-are-the-signs-of-an-unhealthy-or-abusive-relationship', 'red', signs),
        ('nudes', 'Nudes & online safety', 'What are the risks of sending nudes?', f'<p>{esc(n1)}</p>', 'faq.html#q-what-are-the-risks-of-sending-nudes', 'know', ''),
        ('bystander', 'Speaking up', 'What is bystander intervention?', f'<p>{esc(b1)}</p>', 'faq.html#q-what-is-bystander-intervention', 'bae', ''),
    ]
    ttabs = ''.join(f'<button class="tab" role="tab" id="tt-{k}" aria-controls="tp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(lbl)}</button>' for i, (k, lbl, *_r) in enumerate(topics))
    tpanels = ''.join(f'''<div role="tabpanel" id="tp-{k}" aria-labelledby="tt-{k}"{'' if i==0 else ' hidden'}><div class="ad-topic">
      <div class="ad-g"><div class="ad-c8 ad-pr ad-topic__txt"><span class="ad-mini">From the SafeBAE FAQ</span><h3>{esc(q)}</h3>{ans}<p class="ad-topic__more">{a('Read the full answer in the FAQ', link, 'arrow-link')}</p></div>
      <div class="ad-c4">{film_card(fk, 'Watch together')}</div></div>{extra}</div></div>''' for i, (k, lbl, q, ans, link, fk, extra) in enumerate(topics))

    acts = [('Believe first.', 'Validate their disclosure and let them know you are there for them unconditionally.'),
            ('Avoid blame.', 'Resist questions that shift responsibility onto your child (“Why were you there?” “What were you wearing?”).'),
            ('Seek support.', 'Connect with a rape crisis advocate, counselor, or support group to guide you and your child through options for care, reporting, and healing.'),
            ('Care for yourself.', 'Supporting a survivor can be emotionally heavy. Finding your own support system will strengthen your ability to show up for your child.')]
    ah = ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in acts)

    opts = [('Confidential', 'Speaking with an advocate or peer educator.'),
            ('Anonymous', 'To flag harm without formal investigation.'),
            ('Law enforcement', 'Filing a police report.'),
            ('Title IX', 'Filing a school complaint for investigation and safety planning.')]
    oh = ''.join(f'<div class="ad-opt"><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in opts)

    steps = [('Pick the right moment, not the charged one', 'Wait until things have cooled down. Good windows: a car ride, a casual one-on-one moment, a follow-up conversation after things have settled.'),
             ('Lead with curiosity, not direction', 'If it sounds like a punishment or an assignment, they won’t engage honestly. Offer it as something genuinely useful, not something you’re making them do.'),
             ('Make the privacy real', 'Send them the link and step away. Don’t ask to see what they wrote or what path they took, and make it clear they can stop at any point.'),
             ('Tell them what it actually is', '“It’s not a test. You can’t get it ‘wrong.’ It asks you questions about a situation and how you’re feeling, and then shows you some tools and information based on that. Nothing gets saved anywhere. It disappears when you close it.”'),
             ('Give them space, and keep the door open', '“If anything comes up when you go through it — questions, things you want to talk through — I’m around. But you don’t have to tell me anything.”')]
    sh = ''.join(f'<li><span class="ad-steps__n" aria-hidden="true">{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(steps))
    starters = [('Opening the conversation', ['“Did you get a chance to look at that thing I sent? No worries if not — just wondering what you thought.”', '“Is there anything from it that stuck with you, or anything you want to talk about?”', '“Did anything surprise you or feel off?”']),
                ('If they seem uncomfortable', ['“You don’t have to tell me anything about it. I just wanted to check in that you’re okay.”', '“If something came up that felt heavy, I want you to know you can talk to me — or someone else you trust.”', '“Sometimes that stuff brings up more questions than answers. That’s fine — it’s actually a good sign.”']),
                ('Going deeper, if they’re open', ['“What does consent actually mean to you? What do you think it looks like in real life?”', '“Have you ever been in a situation where you weren’t sure if someone was into it? What did you do?”', '“How do you think you’d react if a friend told you they’d been in a situation where someone didn’t stop when asked?”']),
                ('If they didn’t use it', ['“That’s okay — I’ll leave the link with you. It’s there whenever you want it.”', '“Is there a reason it felt weird? I can explain what it actually is if that would help.”', '“Even without the tool — is there anything on your mind about what we talked about?”'])]
    sth = ''.join(f'<div class="ad-starter"><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in xs)}</ul></div>' for t, xs in starters)

    involve = [('Certified Peer Educator Training', 'Encourage your student to enroll in our free, virtual, self-paced training that equips them to educate peers on consent, bystander intervention, and digital safety.', 'peer-educator.html', ['Free', 'Virtual', 'Self-paced']),
               ('Bring SafeBAE to your school', 'Ask your school to partner with us through our SafeBAE 360° whole-school model, which includes curriculum, peer educator training, staff development, and policy support.', 'request-a-program.html', ['Request a program']),
               ('Summer Activist Institute', 'Support your student to apply for our annual Summer Activist Institute, an intensive leadership program that prepares youth to lead prevention and advocacy efforts in their own communities.', 'summer-institute.html', ['Annual']),
               ('Start a school club', 'Students can register a new SafeBAE chapter, affiliate a club they already run, or restart last year’s.', 'clubs.html', ['Clubs']),
               ('SafeBAE AI Literacy Training', 'Six free, self-paced modules: how AI works, how feeds and AI shape what we see and believe, AI and healthy relationships, using AI well, fake images, and sextortion. Anyone 13 or older can take it. Launches during U.S. Media Literacy Week, October 26–30, 2026.', 'ai-literacy.html', ['New', 'Free', 'Ages 13+'])]
    ih = ''.join(row(t, d, h, m) for t, d, h, m in involve)

    vfeats = [('Completely private', 'No accounts, no tracking, no history. Nothing is saved or sent anywhere.'),
              ('Non-punitive tone', 'Designed to build awareness and accountability, not to condemn, label, or shame.'),
              ('Self-paced & self-guided', 'There are no right or wrong answers and no pressure to finish.'),
              ('Practical next steps', 'Interactive activities, guided lessons, grounding exercises, and support resources.')]
    vf = ''.join(f'<div><b>{esc(t)}</b><span>{esc(d)}</span></div>' for t, d in vfeats)
    sp_url = f'https://open.spotify.com/episode/{pod[0]}'

    body = f'''
<section class="phero phero--aqua phero--split ad-phero">
  <span class="phero__wm" aria-hidden="true"></span>
  <div class="wrap">
    <div class="ad-c7 ad-pr ad-txt">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="adults.html">Adults</a><span>/</span><span>Parents &amp; Caregivers</span></nav>
      <h1>Parents &amp; <span class="mk">caregivers</span></h1>
      <p class="lede">Support the young people in your life and in your community.</p>
      <p>Parents, caregivers, and trusted adults play a critical role in shaping how young people understand safety, consent, and relationships. While SafeBAE’s work is youth-led, prevention is a whole-community commitment. These tools, resources and guidance can help you feel prepared to support the teens in your life.</p>
      <div class="btns">{btn('Start the conversation early', '#early', 'slate', arrow=True)}{btn('If your child tells you', '#support', 'ghost')}</div>
    </div>
    <div class="ad-c5 phero__media">{img('us-reis-parent', 'A parent and teenager talking at a table', loading='eager')}<span class="sticker">Whole-community prevention</span></div>
  </div>
</section>

<section class="band band--slate band--tight" aria-label="Podcast">
  <div class="wrap ad-g ad-pod">
    <div class="ad-pod__art">{img('sp-' + pod[0].lower(), 'The Longest Shortest Time podcast artwork')}</div>
    <div class="ad-pod__txt">
      <p class="eyebrow">Listen &middot; The Longest Shortest Time</p>
      <h2>How to Not (Accidentally) Raise a Rapist</h2>
      <p>SafeBAE’s Executive Director Shael Norris on the award-winning parenting podcast with Hillary Frank: what works when talking to teens about consent, and how schools and parents can build a consent-conscious culture.</p>
      <div class="ad-pod__row">
        <div class="ad-pod__play"><a class="ad-play" href="{sp_url}" target="_blank" rel="noopener" data-spotify="episode/{pod[0]}" aria-label="Listen: {esc(pod[1])}"><span class="ad-play__dot">{ICON_PLAY}</span><span><b>Play the episode</b><small>{esc(pod[2])}</small></span></a></div>
        <div class="ad-pod__links">{a('NYT Opinion piece', pod[7][0][1], 'ext')}{a('NYT companion podcast', pod[7][1][1], 'ext')}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="early">
  <div class="wrap">
    <div class="ad-g ad-g--m ad-early">
      <div class="ad-c8 ad-pr ad-txt">
        <p class="eyebrow">Prevention &amp; early conversations</p>
        <h2>Start early, and keep talking</h2>
        <p class="lede">Even if it doesn’t always feel like it, young people look to the adults in their lives for cues about healthy relationships, boundaries, and safety. Starting conversations at home, supporting youth leaders in your community, and advocating for safer schools all make a lasting difference.</p>
        <ul class="ad-checks">
          <li>Begin practicing lessons of bodily autonomy and respect from the earliest ages.</li>
          <li>Use everyday opportunities (TV shows, news stories, or social media) to spark conversations before harm happens.</li>
          <li>Model open, judgment-free dialogue so your child feels safe confiding in you if something does happen.</li>
        </ul>
        <div class="ad-hl"><b>Create a “safe call” policy.</b><p>Assure your child they can call you anytime they feel unsafe. Safety comes before punishment, no matter what.</p></div>
      </div>
      <figure class="ad-c4 ad-media ad-shot fill-img">{img('us-annaselle-parent', 'Two teenagers relaxing and talking on a couch')}<span class="sticker">Safety before punishment</span></figure>
    </div>
    <div class="ad-g ad-ways reveal">
      <div class="ad-c4 ad-ways__poster" data-gallery><button class="ad-zoom" data-src="{imgsrc('baby-consent-print-materials-1')}" data-cap="SafeBAE poster: smile, high five, fist bump, handshake or hug">{img('baby-consent-print-materials-1', 'SafeBAE poster offering greetings to choose from: smile, high five, fist bump, handshake or hug')}<small>A SafeBAE poster of greetings to choose from. Tap to enlarge.</small></button></div>
      <div class="ad-c8 ad-pl ad-ways__body">
        <h3>Early ways to teach consent</h3>
        <p class="ad-ways__lede">Teaching consent can start at the youngest ages, through simple, everyday choices that reinforce respect and bodily autonomy.</p>
        <dl class="ad-ways__list">{ei}</dl>
      </div>
    </div>
    <p class="ad-ways__end">As children grow, lessons about consent should grow with them. SafeBAE provides age-appropriate tools and resources to help families and educators build on these early conversations year after year.</p>
  </div>
</section>

<section class="band band--deep" id="choking">
  <div class="wrap ad-g ad-g--m ad-choke">
    <div class="ad-c7 ad-pr ad-txt">
      <p class="eyebrow">New SafeBAE campaign</p>
      <h2>What parents should know about “choking”</h2>
      <p class="lede">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” It is written for young people, parents and educators, and its warning posters are free to share.</p>
      <div class="ad-inside"><span class="ad-mini">Inside</span><ul class="ad-checks"><li>The evidence</li><li>Myth vs. fact</li><li>Signs that need medical care</li><li>Free warning posters</li></ul></div>
      <div class="btns">{btn('What parents should know', 'choking-hazard.html', 'mint', arrow=True)}{btn('ChokingHazard.org', CH_URL, 'ghost')}</div>
    </div>
    <div class="ad-c5 ad-media ad-choke__sign">{hz_box()}<p class="ad-hz__line">There’s no safe way to choke someone.</p></div>
  </div>
</section>

<section class="band band--mist" id="talk">
  <div class="wrap">
    <div class="section-head"><div><h2>Topics to talk through with your teen</h2>
      <p class="lede lede--full">TV shows, news stories and social media all open the door to these conversations. Watching one of SafeBAE’s short, youth-made films together is another way in.</p></div></div>
    <div data-tabs="parents-topics"><div class="ad-tabs" role="tablist" aria-label="Topics">{ttabs}</div>{tpanels}</div>
  </div>
</section>

<section class="band band--slate ad-support" id="support">
  <div class="wrap">
    <div class="ad-g ad-g--m ad-support__top">
      <div class="ad-c6 ad-pr ad-txt">
        <p class="eyebrow">Supporting a survivor</p>
        <h2>If your child tells you something happened</h2>
        <p class="lede ad-lede-light">Learning that your child has experienced sexual violence can be overwhelming, frightening, and heartbreaking. You may feel shock, anger, sadness, or even guilt, and all of these are normal reactions. In this moment, the most important thing you can do is to center your child’s needs.</p>
        <p class="muted">Believe your child and reassure them that the assault was not their fault. Help them access the healing services and support they need, and remember that you, too, may need community and resources to process your own feelings.</p>
        <div class="btns">{btn('Support a survivor', 'survivor-support.html', 'mint', arrow=True)}{btn('Healing resources', 'survivor-support.html', 'ghost')}</div>
      </div>
      <div class="ad-c6 ad-media ad-support__side" data-gallery><button class="ad-zoom" data-src="{imgsrc('8x8-what-not-to-say-poster-pdf')}" data-cap="What to say vs. what not to say to a friend who shares they have been assaulted">{img('8x8-what-not-to-say-poster-pdf', 'SafeBAE poster: what to say and what not to say to someone who shares they have been assaulted. Say: I’m so sorry this happened to you. You are not alone. How can I support you? It’s not your fault. I’m glad you felt safe to tell me. Avoid: Why were you there? It’s going to be fine. Were you drinking? What were you wearing?')}<small>What to say, and what not to say. Tap to enlarge.</small></button></div>
    </div>
    <div class="ad-acts reveal">{ah}</div>
    <div class="ad-helpbar"><div><b>Talk to someone now</b><span>Free, confidential support for survivors and the people who love them, open 24/7.</span></div>
      <ul><li><small>RAINN</small><strong>Call 800-656-HOPE (4673)</strong></li><li><small>love is respect</small><strong>Text LOVEIS to 22522</strong></li></ul>
      <button class="btn btn--slate" data-open-help>All hotlines</button></div>
  </div>
</section>

<section class="band band--paper" id="reporting">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Navigating reporting &amp; rights</p><h2>Listen to your child’s wishes first</h2>
      <p class="lede lede--full">Your instinct may be to report immediately. Instead, listen to your child’s wishes. If they do choose to report, connect first with an advocate. Reporting options may include:</p></div>{btn('Title IX rights', 'title-ix.html', 'slate', arrow=True)}</div>
    <div class="ad-opts reveal">{oh}</div>
    <div class="ad-g ad-alt" id="alternative-justice">
      <div class="ad-c8 ad-pr">
        <p class="eyebrow">Alternative justice approaches</p>
        <h3>Accountability outside a formal investigation</h3>
        <p>Some survivors want to avoid a full Title IX or police investigation but still hope for accountability. They may wish for the person who harmed them to reflect on their actions and understand the impact.</p>
        <p>This pathway offers an opportunity for individuals who have caused harm to more fully learn about consent, accountability, and the unintended consequences of their behavior, outside of a formal investigation process.</p>
        <div class="btns">{btn('Accountability Training', 'accountability-training.html', 'slate', arrow=True)}</div>
      </div>
      <div class="ad-c4" data-gallery><button class="ad-zoom" data-src="{imgsrc('untitled-design')}" data-cap="Types and degrees of restorative justice practice (credit: www.iirp.edu)">{img('untitled-design', 'Diagram of the types and degrees of restorative justice practice, showing survivor reparations, communities of care and offender responsibility overlapping at restorative justice')}<small>Types and degrees of restorative justice practice. Tap to enlarge.</small></button></div>
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-g ad-g--m ad-vibe">
    <div class="ad-c7 ad-pr ad-txt">
      <div class="ad-vmark"><span class="daisy"></span>Introducing Vibe Check</div>
      <h2>CheckYourVibe.org</h2>
      <p class="lede">As parents and caregivers, we all find ourselves worrying and trying our best to make this world safe for our children. But society, technology, and social media messaging can sometimes make that feel impossible.</p>
      <p>We all struggled to navigate our childhoods, and our kids are no different. The measure of our character is not that we never make a mistake, but how we respond to learning that we have caused unintended harm. Intimacy is one of the hardest things for anyone to navigate, and we need as many tools as possible to help this generation do it better. That’s why we built Vibe Check: to support kids in asking vulnerable questions, navigating relationships, and being the best partners they can be.</p>
      <div class="ad-vfeats">{vf}</div>
      <div class="btns">{btn('Explore the tool', 'https://checkyourvibe.org/', 'mint')}{btn('Parent guide (PDF)', GUIDE_PDF, 'white')}{a('How it works', 'vibe-check.html', 'arrow-link')}</div>
    </div>
    <div class="ad-c5 ad-media">
      <div class="ad-phonewrap">
        <div class="ad-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div>
        <span class="sticker" style="left:-4%;top:17%">No account. No names.</span>
        <span class="sticker sticker--white sticker--r" style="right:-2%;bottom:17%">Nothing is stored</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="share">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From the Check Their Vibe guide</p><h2>Sharing Vibe Check with your child</h2>
      <p class="lede lede--full">The most common mistake is introducing a tool like this in a moment of frustration. The best time is before anything has happened at all, as part of a talk about dating or sex.</p></div>{btn('Read the full guide (PDF)', GUIDE_PDF, 'slate')}</div>
    <div data-tabs="parents-share">
      <div class="ad-tabs" role="tablist" aria-label="Sharing Vibe Check"><button class="tab" role="tab" id="st-before" aria-controls="sp-before" aria-selected="true">How to bring it up</button><button class="tab" role="tab" id="st-after" aria-controls="sp-after" aria-selected="false" tabindex="-1">Talking about it afterward</button></div>
      <div role="tabpanel" id="sp-before" aria-labelledby="st-before">
        <div class="ad-g ad-share">
          <ol class="ad-c7 ad-steps">{sh}</ol>
          <div class="ad-c5 ad-say">
            <div class="ad-say__try"><span class="ad-mini">Try saying something like</span><p class="ad-bubble">“Hey, I came across this thing — it’s not a lecture, it’s more like a self-reflection tool. Private, nothing gets saved. I thought it might be useful to go through on your own when you have a minute. No pressure, but I think it’s worth a look.”</p><span class="ad-mini">Or, for a younger person</span><p class="ad-bubble">“There’s a tool I want to show you — it’s like a private check-in for yourself about relationships and situations. You don’t have to share anything with me. I just thought it might be helpful.”</p></div>
            <div class="ad-say__avoid"><span class="ad-mini">Avoid framing it as</span><ul><li><span>“You need to do this because of what happened.”</span></li><li><span>“This will help you understand why you were wrong.”</span></li><li><span>“We’re going to go through this together.”</span></li><li><span>“I want to see your answers afterward.”</span></li></ul></div>
          </div>
        </div>
      </div>
      <div role="tabpanel" id="sp-after" aria-labelledby="st-after" hidden>
        <div class="ad-starters">{sth}</div>
        <div class="ad-reminder"><p>If a young person comes to you after using it, receive that with curiosity, not judgment. Your reaction to the first vulnerable thing they share determines whether they share anything again.</p><button class="btn btn--mint btn--sm" data-open-help>If it’s a crisis: hotlines</button></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--deep" id="involved">
  <div class="wrap ad-g ad-involve">
    <div class="ad-c5 ad-pr ad-involve__lead">
      <h2>Connect your student with SafeBAE</h2>
      <p class="lede">One of the most powerful things you can do as a parent or caregiver is to connect your student with SafeBAE’s programs. These opportunities allow young people to build leadership skills, learn about consent and healthy relationships, and create change in their schools and communities.</p>
      <figure class="ad-shot fill-img">{img('img-6834', 'A group of SafeBAE student leaders smiling together at sunset')}<span class="sticker sticker--aqua">Youth-led</span></figure>
    </div>
    <div class="ad-c7 rows">{ih}</div>
  </div>
</section>
{give_band()}
'''
    page('parents.html', 'Parents & Caregivers · SafeBAE', 'Guidance for parents and caregivers on talking with teens about consent and healthy relationships, supporting a survivor, reporting options, and sharing Vibe Check.',
         body, active='adults', fonts=film_font_link(), head_extra=HEAD, body_class='ad', scripts=PARENTS_JS)


def build():
    adults()
    parents()


if __name__ == '__main__':
    build()
