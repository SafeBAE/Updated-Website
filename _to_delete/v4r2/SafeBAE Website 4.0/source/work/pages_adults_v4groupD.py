"""Adults group (v3): adults.html and parents.html.
Content carried from the live safebae.org pages (get-involved, parents), the Check Their Vibe
adult guide PDF and the site FAQ answers already in data.py.
(educators, college, request, donate, chip-in and fundraise build from pages_adults2 / pages_programs.)
v4: adults.html is a hub (router, schools band with the two new programs, films, Vibe Check adults' guide);
parents.html keeps 7 sections. The full adults' guide to Vibe Check lives on vibe-check.html#adults."""
from lib import *
from data import FAQ, PODCASTS, WP
from pages_home import FILMS, film_font_link

GUIDE_PDF = WP + '2026/03/Check-Their-Vibe-A-Guide-to-Vibe-Check.pdf'
CH_URL = 'https://chokinghazard.org'


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
.ad-prog em{display:block; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint); margin-bottom:6px}
.ad-prog--360{background:var(--mint); border-color:var(--mint)}
.ad-prog--360 b{color:var(--slate)} .ad-prog--360 small{color:var(--slate)}
.ad-prog--360 i{background:var(--slate); color:var(--mint)}
.ad-prog--360:hover{background:var(--aqua); border-color:var(--aqua)}
.ad-prog--360:hover i{background:var(--slate); color:var(--mint)}
@media (max-width:900px){.ad-book{grid-template-columns:minmax(0,1fr)} .ad-book__photo{grid-column:auto; min-height:0; aspect-ratio:16/9} .ad-book__grid{grid-column:auto}}
@media (max-width:620px){.ad-book__grid{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto} .ad-prog{min-height:0}}

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

/* early conversations (slate): the text, with the podcast as a feature beside it */
.ad-early__top{align-items:stretch}
.ad-early h2{margin-bottom:.35em}
.ad-early .lede{margin-bottom:1.1em}
.ad-early .ad-checks li{color:rgba(255,255,255,.9)}
.ad-hl{background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:20px 24px; margin-top:auto}
.ad-early__txt .ad-checks{margin-bottom:26px}
.ad-hl b{font-family:var(--display); font-stretch:108%; font-size:1.25rem; line-height:1.15; display:block; margin-bottom:6px}
.ad-hl p{margin:0}
.ad-pod{display:flex; flex-direction:column; gap:18px; background:var(--slate-deep); border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:var(--pad-card); box-shadow:0 30px 60px -36px rgba(0,0,0,.7)}
.ad-pod__head{display:grid; grid-template-columns:120px minmax(0,1fr); gap:18px; align-items:end}
.ad-pod__head .ad-mini{line-height:1.45}
.ad-pod__head img{width:100%; aspect-ratio:1; object-fit:cover; border-radius:14px; box-shadow:0 16px 30px -18px rgba(0,0,0,.8)}
.ad-pod h3{font-size:clamp(1.45rem,2.1vw,1.85rem); line-height:1.08; margin:0; color:#fff; text-wrap:balance}
.ad-pod > p{margin:0; color:rgba(255,255,255,.88); line-height:1.55}
.ad-pod__foot{margin-top:auto; display:flex; flex-direction:column; align-items:flex-start; gap:10px; padding-top:18px; border-top:1px solid var(--line-dark)}
.ad-play{display:inline-flex; align-items:center; gap:14px; padding:9px 24px 9px 9px; border-radius:999px; background:var(--mint); text-decoration:none; box-shadow:0 4px 0 rgba(0,0,0,.22); transition:transform .18s var(--ease), box-shadow .18s}
.ad .ad-pod .ad-play{color:var(--slate)}
.ad-play:hover{transform:translateY(-2px); box-shadow:0 6px 0 rgba(0,0,0,.22)}
.ad-play__dot{flex:none; width:46px; height:46px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center}
.ad-play__dot svg{width:20px; height:20px; margin-left:3px}
.ad-play b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.05rem; line-height:1.15}
.ad-play small{display:block; font-size:.9rem; font-weight:600; line-height:1.3}
.ad-pod__play:has(iframe){flex:1 1 100%}
.ad-pod__links{display:flex; flex-wrap:wrap; gap:0 16px; font-weight:700; font-size:.9rem}
.ad-pod__links a{display:inline-flex; align-items:center; min-height:44px}
/* early ways to teach consent: mirrors the row above (5 | 7) */
.ad-ways{margin-top:clamp(40px,5vw,64px); align-items:stretch}
.ad-ways__poster{display:flex}
.ad-ways__poster .ad-zoom{display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; background:var(--aqua); border-radius:var(--r-xl); padding:clamp(18px,2.4vw,30px) clamp(18px,2.4vw,30px) 20px; height:100%; text-align:center}
.ad-ways__poster img{width:min(100%,290px); height:auto; border-radius:8px; box-shadow:0 24px 40px -22px rgba(22,53,64,.6); transform:rotate(-2.5deg)}
.ad-ways__poster .ad-zoom:hover img{transform:rotate(-1deg) scale(1.02)}
.ad-ways__poster small{margin:0; color:var(--logo-teal)}
.ad-ways__body{display:flex; flex-direction:column}
.ad-ways h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin-bottom:.3em; color:#fff}
.ad-ways__lede{margin:0 0 18px; font-size:1.08rem; color:rgba(255,255,255,.88)}
.ad-ways__list{margin:0; border-top:1px solid var(--line-dark); display:flex; flex-direction:column; flex:1 1 auto}
.ad-ways__list > div{flex:1 1 auto; display:grid; grid-template-columns:minmax(0,15em) minmax(0,1fr); gap:6px var(--gap); align-content:center; padding:16px 0; border-bottom:1px solid var(--line-dark)}
.ad-ways__list dt{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.2rem; line-height:1.18; color:var(--mint)}
.ad-ways__list dd{margin:0; color:rgba(255,255,255,.86); line-height:1.55}
.ad-ways__end{margin:20px 0 0; font-weight:600; font-size:1.06rem; line-height:1.5; color:#fff}
@media (max-width:900px){.ad-ways__poster img{width:min(60%,220px)} .ad-early .ad-pod{margin-top:28px} .ad-hl{margin-top:0}}
@media (max-width:620px){.ad-ways__list > div{grid-template-columns:minmax(0,1fr); gap:6px}}
@media (max-width:520px){.ad-pod__head{grid-template-columns:84px minmax(0,1fr); gap:14px}}

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
.ad-signs .chip{white-space:normal; background:#fff; font-size:.875rem; padding:.45em .75em; line-height:1.3; letter-spacing:.01em; text-transform:none; font-family:var(--body); font-weight:600}
.ad-signs > div:last-child .chip{background:rgba(255,255,255,.12); color:#fff}
@media (max-width:900px){.ad-topic .ad-film__img{min-height:0; aspect-ratio:16/9; flex:none}}
@media (max-width:620px){.ad-signs{grid-template-columns:minmax(0,1fr)}}

/* Choking Hazard: one compact band that sends parents on */
.ad-choke{align-items:center}
.ad-choke__sign{padding-right:clamp(0px,2.4vw,34px)}
.ad-choke__sign .ad-hzbox{width:100%; padding:10px 14px 4px 6px}
.ad-choke h2{margin-bottom:.3em}
.ad-cstat{display:flex; align-items:center; gap:22px; margin:22px 0 0; padding:16px 0; border-block:1px solid var(--line-dark)}
.ad-cstat b{flex:none; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(3.2rem,5vw,4.4rem); line-height:.85; letter-spacing:-.02em; color:var(--mint)}
.ad-cstat span{color:rgba(255,255,255,.92); font-weight:600; font-size:1.06rem; line-height:1.45}
.ad-cstat cite{display:block; margin-top:4px; font-style:normal; font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; font-weight:500; color:rgba(209,254,255,.78)}
.ad-choke .btns{margin-top:24px}
@media (max-width:900px){.ad-choke__sign{padding-right:0; max-width:440px}}

/* if your child tells you (paper): what to do first, then the options */
.ad-acts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); background:var(--mist); border:1px solid var(--line); border-top:6px solid var(--mint); border-radius:var(--r-xl); overflow:hidden}
.ad-acts > div{padding:24px 26px 26px; border-left:1px solid var(--line); min-width:0}
.ad-acts > div:first-child{border-left:0}
.ad-acts b{display:block; font-family:var(--display); font-stretch:110%; font-weight:900; font-size:1.45rem; line-height:1.08; color:var(--logo-teal); margin-bottom:8px}
.ad-acts p{margin:0; color:var(--ink-soft); line-height:1.55; font-size:.98rem}
.ad-helpbar{margin-top:var(--gap); display:grid; grid-template-columns:minmax(0,1fr) auto auto; gap:16px clamp(20px,3vw,44px); align-items:center; background:var(--coral); color:var(--slate); border-radius:var(--r-xl); padding:20px var(--pad-card)}
.ad-helpbar > div > b{display:block; font-family:var(--display); font-stretch:110%; font-weight:900; font-size:1.4rem; line-height:1.1; margin-bottom:4px}
.ad-helpbar > div > span{display:block; font-weight:600; line-height:1.45}
.ad-helpbar ul{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,auto); gap:12px 28px}
.ad-helpbar li{margin:0; padding-left:18px; border-left:2px solid rgba(29,65,78,.35)}
.ad-helpbar li small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600}
.ad-helpbar li strong{display:block; white-space:nowrap; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.18rem; line-height:1.2; margin-top:2px}
.ad-report{margin-top:clamp(40px,5vw,64px); align-items:stretch}
.ad-report h3{font-size:clamp(1.5rem,2.4vw,2.1rem); margin-bottom:.35em}
.ad-report__txt > p{margin:0 0 20px; font-size:1.06rem}
.ad-opts{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); border:1px solid var(--line); border-top:6px solid var(--mint); border-radius:var(--r-xl); background:#fff; overflow:hidden}
.ad-opt{padding:20px 24px; min-width:0; border-left:1px solid var(--line)}
.ad-opt:nth-child(odd){border-left:0}
.ad-opt:nth-child(n+3){border-top:1px solid var(--line)}
.ad-opt b{display:block; font-family:var(--display); font-stretch:110%; font-weight:800; font-size:1.3rem; color:var(--logo-teal); line-height:1.1; margin-bottom:6px}
.ad-opt p{margin:0; color:var(--ink-soft); line-height:1.5}
.ad-report__more{margin:auto 0 0!important; padding-top:18px; display:flex; flex-wrap:wrap; gap:6px 28px}
.ad-report__more .arrow-link{min-height:44px}
.ad-alt{display:flex; flex-direction:column; background:var(--aqua); border-radius:var(--r-xl); padding:clamp(24px,2.8vw,36px)}
.ad-alt .ad-mini{margin-bottom:10px}
.ad-alt h3{font-size:clamp(1.4rem,2vw,1.75rem)}
.ad-alt p{margin:0 0 .8em}
.ad-alt .btns{margin-top:auto; padding-top:10px}
@media (max-width:1100px){.ad-helpbar{grid-template-columns:minmax(0,1fr) auto} .ad-helpbar ul{grid-column:1/-1; grid-row:2; justify-content:start}}
@media (max-width:1100px){.ad-acts{grid-template-columns:repeat(2,minmax(0,1fr))} .ad-acts > div:nth-child(3){border-left:0} .ad-acts > div:nth-child(n+3){border-top:1px solid var(--line)}}
@media (max-width:900px){.ad-alt{margin-top:var(--gap)}}
@media (max-width:620px){.ad-acts{grid-template-columns:minmax(0,1fr)} .ad-acts > div{border-left:0} .ad-acts > div + div{border-top:1px solid var(--line)}}
@media (max-width:560px){.ad-opts{grid-template-columns:minmax(0,1fr)} .ad-opt{border-left:0} .ad-opt + .ad-opt{border-top:1px solid var(--line)} .ad-helpbar{grid-template-columns:minmax(0,1fr)} .ad-helpbar ul{grid-template-columns:minmax(0,1fr); grid-row:auto} .ad-helpbar li strong{white-space:normal} .ad-helpbar .btn{justify-self:start}}

/* Vibe Check on the parents page: what it is, and the three steps that matter most */
.ad-vsteps{list-style:none; margin:24px 0 0; padding:0; border-top:1px solid rgba(255,255,255,.28)}
.ad-vsteps li{margin:0; display:grid; grid-template-columns:52px minmax(0,1fr); column-gap:16px; padding:16px 0; border-bottom:1px solid rgba(255,255,255,.28)}
.ad-vsteps__n{grid-row:1/3; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:2.5rem; line-height:.95; color:var(--mint)}
.ad-vsteps h3{font-size:1.25rem; margin:0 0 .25em; color:#fff}
.ad-vsteps p{margin:0; line-height:1.55}
.ad-phonewrap{position:relative; width:min(100%,400px); margin-inline:auto}
.ad-phone{position:relative; width:86%; margin-inline:auto; aspect-ratio:390/800; border-radius:46px; border:11px solid #0b1f25; background:#0b1f25; box-shadow:0 50px 90px -30px rgba(0,0,0,.6); overflow:hidden; transform:rotate(4deg)}
.ad-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.ad-phonewrap .sticker{position:absolute; z-index:2}
@media (max-width:900px){.ad-phonewrap{width:min(78%,300px)}}
@media (max-width:480px){.ad-vsteps li{grid-template-columns:40px minmax(0,1fr); column-gap:12px} .ad-vsteps__n{font-size:2.1rem}}

/* connect your student (compact) */
.ad-involve{align-items:stretch}
.ad-involve__lead{display:flex; flex-direction:column}
.ad-involve__lead .lede{margin-bottom:1.2em}
.ad-involve .ad-shot{flex:1 1 auto; min-height:200px}
.ad-involve .ad-shot img{object-position:50% 45%}
.ad-involve .rows{align-content:stretch}
.ad-involve .row{padding-block:16px}
.ad-involve .row b{font-size:1.2rem}
.ad-involve .row small{font-size:.95rem; line-height:1.5; margin-top:4px}
.ad-involve .row .go{width:40px; height:40px}
@media (max-width:900px){.ad-involve .ad-shot{flex:none; aspect-ratio:16/10; min-height:0; margin-bottom:10px}}
'''

HEAD = f'<style>{CSS}</style>'

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
      <div class="btns">{btn('Bring SafeBAE to your school', 'request-a-program.html', 'mint', arrow=True)}{btn('Adults’ guide to Vibe Check', 'vibe-check.html#adults', 'ghost')}</div>
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
      <div class="btns">{btn('Read the adults’ guide', 'vibe-check.html#adults', 'mint', arrow=True)}{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'white')}</div>
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

    # the three steps from the Check Their Vibe guide that matter most; the full guide is on vibe-check.html#adults
    steps = [('Pick the right moment, not the charged one', 'Wait until things have cooled down. Good windows: a car ride, a casual one-on-one moment, a follow-up conversation after things have settled.'),
             ('Lead with curiosity, not direction', 'If it sounds like a punishment or an assignment, they won’t engage honestly. Offer it as something genuinely useful, not something you’re making them do.'),
             ('Make the privacy real', 'Send them the link and step away. Don’t ask to see what they wrote or what path they took, and make it clear they can stop at any point.')]
    sh = ''.join(f'<li><span class="ad-vsteps__n" aria-hidden="true">{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(steps))

    involve = [('Certified Peer Educator Training', 'Free, virtual and self-paced: students learn to educate peers on consent, bystander intervention and digital safety.', 'peer-educator.html'),
               ('SafeBAE AI Literacy Training', 'Six free, self-paced modules for anyone 13 or older. Launches October 26–30, 2026.', 'ai-literacy.html'),
               ('Start a school club', 'Students can register a new SafeBAE chapter, affiliate a club they already run, or restart last year’s.', 'clubs.html'),
               ('Summer Activist Institute', 'An annual leadership program that prepares youth to lead prevention and advocacy in their communities.', 'summer-institute.html'),
               ('Bring SafeBAE to your school', 'Ask your school to partner with us through the SafeBAE 360° whole-school model.', 'request-a-program.html')]
    ih = ''.join(row(t, d, h) for t, d, h in involve)
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

<section class="band band--slate ad-early" id="early">
  <div class="wrap">
    <div class="ad-g ad-early__top">
      <div class="ad-c8 ad-pr ad-col ad-early__txt">
        <h2>Start early, and keep talking</h2>
        <p class="lede ad-lede-light">Even if it doesn’t always feel like it, young people look to the adults in their lives for cues about healthy relationships, boundaries, and safety. Starting conversations at home, supporting youth leaders in your community, and advocating for safer schools all make a lasting difference.</p>
        <ul class="ad-checks">
          <li>Begin practicing lessons of bodily autonomy and respect from the earliest ages.</li>
          <li>Use everyday opportunities (TV shows, news stories, or social media) to spark conversations before harm happens.</li>
          <li>Model open, judgment-free dialogue so your child feels safe confiding in you if something does happen.</li>
        </ul>
        <div class="ad-hl"><b>Create a “safe call” policy.</b><p>Assure your child they can call you anytime they feel unsafe. Safety comes before punishment, no matter what.</p></div>
      </div>
      <aside class="ad-c4 ad-pod" aria-label="Podcast: How to Not (Accidentally) Raise a Rapist">
        <div class="ad-pod__head">{img('sp-' + pod[0].lower(), 'The Longest Shortest Time podcast artwork')}<span class="ad-mini">Listen<br>The Longest Shortest Time</span></div>
        <h3>How to Not (Accidentally) Raise a Rapist</h3>
        <p>SafeBAE’s Executive Director Shael Norris on the award-winning parenting podcast with Hillary Frank: what works when talking to teens about consent, and how schools and parents can build a consent-conscious culture.</p>
        <div class="ad-pod__foot">
          <div class="ad-pod__play"><a class="ad-play" href="{sp_url}" target="_blank" rel="noopener" data-spotify="episode/{pod[0]}" aria-label="Listen: {esc(pod[1])}"><span class="ad-play__dot">{ICON_PLAY}</span><span><b>Play the episode</b><small>Spotify &middot; February 2025</small></span></a></div>
          <div class="ad-pod__links">{a('NYT Opinion', pod[7][0][1], 'ext', attrs=' aria-label="NYT Opinion piece"')}{a('NYT podcast', pod[7][1][1], 'ext', attrs=' aria-label="NYT companion podcast"')}</div>
        </div>
      </aside>
    </div>
    <div class="ad-g ad-ways reveal">
      <div class="ad-c4 ad-ways__poster" data-gallery><button class="ad-zoom" data-src="{imgsrc('baby-consent-print-materials-1')}" data-cap="SafeBAE poster: smile, high five, fist bump, handshake or hug">{img('baby-consent-print-materials-1', 'SafeBAE poster offering greetings to choose from: smile, high five, fist bump, handshake or hug')}<small>A SafeBAE poster of greetings to choose from. Tap to enlarge.</small></button></div>
      <div class="ad-c8 ad-pl ad-ways__body">
        <h3>Early ways to teach consent</h3>
        <p class="ad-ways__lede">Teaching consent can start at the youngest ages, through simple, everyday choices that reinforce respect and bodily autonomy.</p>
        <dl class="ad-ways__list">{ei}</dl>
        <p class="ad-ways__end">As children grow, lessons about consent should grow with them. SafeBAE provides age-appropriate tools and resources to help families and educators build on these early conversations year after year.</p>
      </div>
    </div>
  </div>
</section>

<section class="band band--mist" id="talk">
  <div class="wrap">
    <div class="section-head"><div><h2>Topics to talk through with your teen</h2>
      <p class="lede lede--full">TV shows, news stories and social media all open the door to these conversations. Watching one of SafeBAE’s short, youth-made films together is another way in.</p></div></div>
    <div data-tabs="parents-topics"><div class="ad-tabs" role="tablist" aria-label="Topics">{ttabs}</div>{tpanels}</div>
  </div>
</section>

<section class="band band--deep" id="choking">
  <div class="wrap ad-g ad-g--m ad-choke">
    <div class="ad-c4 ad-media ad-choke__sign">{hz_box()}</div>
    <div class="ad-c8 ad-txt">
      <h2>What parents should know about “choking”</h2>
      <p class="lede ad-lede-light">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking.” There’s no safe way to choke someone, and prevention has to start early, before the behavior does.</p>
      <p class="ad-cstat"><b>15</b><span>is the average age students first heard about choking during sex.<cite>Herbenick et al., 2025</cite></span></p>
      <div class="btns">{btn('What parents should know', 'choking-hazard.html', 'mint', arrow=True)}{btn('Go to chokinghazard.org', CH_URL, 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--paper ad-support" id="support">
  <div class="wrap">
    <div class="section-head"><div><h2>If your child tells you something happened</h2>
      <p class="lede lede--full">Learning that your child has experienced sexual violence can be overwhelming, frightening, and heartbreaking. You may feel shock, anger, sadness, or even guilt, and all of these are normal reactions. In this moment, the most important thing you can do is to center your child’s needs. Believe your child and reassure them that the assault was not their fault.</p></div></div>
    <div class="ad-acts reveal">{ah}</div>
    <div class="ad-helpbar"><div><b>Talk to someone now</b><span>Free, confidential support for survivors and the people who love them, open 24/7.</span></div>
      <ul><li><small>RAINN</small><strong>Call 800-656-HOPE (4673)</strong></li><li><small>love is respect</small><strong>Text LOVEIS to 22522</strong></li></ul>
      <button class="btn btn--slate" data-open-help>All hotlines</button></div>
    <div class="ad-g ad-report" id="reporting">
      <div class="ad-c7 ad-pr ad-col ad-report__txt">
        <h3>Listen to your child’s wishes first</h3>
        <p>Your instinct may be to report immediately. Instead, listen to your child’s wishes. If they do choose to report, connect first with an advocate. Reporting options may include:</p>
        <div class="ad-opts">{oh}</div>
        <p class="ad-report__more">{a('Know your rights under Title IX', 'title-ix.html', 'arrow-link')}{a('How to support a survivor', 'survivor-support.html#when-someone-tells-you', 'arrow-link')}</p>
      </div>
      <div class="ad-c5 ad-alt" id="alternative-justice">
        <h3>Accountability outside a formal investigation</h3>
        <p>Some survivors want to avoid a full Title IX or police investigation but still hope for accountability. They may wish for the person who harmed them to reflect on their actions and understand the impact.</p>
        <p>This pathway offers an opportunity for individuals who have caused harm to more fully learn about consent, accountability, and the unintended consequences of their behavior, outside of a formal investigation process.</p>
        <div class="btns">{btn('Accountability Training', 'accountability-training.html', 'slate', arrow=True)}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--teal" id="vibe-check">
  <div class="wrap ad-g ad-g--m ad-vibe">
    <div class="ad-c7 ad-pr ad-txt">
      <div class="ad-vmark"><span class="daisy"></span>Vibe Check by SafeBAE</div>
      <h2>Sharing Vibe Check with your child</h2>
      <p class="lede">Vibe Check is a free, private, self-guided reflection tool for young people navigating moments of sexual uncertainty. We built it to support kids in asking vulnerable questions, navigating relationships, and being the best partners they can be.</p>
      <ol class="ad-vsteps" id="share" aria-label="Three steps from the adults’ guide">{sh}</ol>
      <div class="btns">{btn('Read the full adults’ guide', 'vibe-check.html#adults', 'mint', arrow=True)}{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'white')}</div>
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

<section class="band band--paper" id="involved">
  <div class="wrap ad-g ad-involve">
    <div class="ad-c5 ad-pr ad-involve__lead">
      <h2>Connect your student with SafeBAE</h2>
      <p class="lede">One of the most powerful things you can do as a parent or caregiver is to connect your student with SafeBAE’s programs.</p>
      <figure class="ad-shot fill-img">{img('img-6834', 'A group of SafeBAE student leaders smiling together at sunset')}</figure>
    </div>
    <div class="ad-c7 rows">{ih}</div>
  </div>
</section>
'''
    page('parents.html', 'Parents & Caregivers · SafeBAE', 'Guidance for parents and caregivers on talking with teens about consent and healthy relationships, supporting a survivor, reporting options, and sharing Vibe Check.',
         body, active='adults', fonts=film_font_link(), head_extra=HEAD, body_class='ad')


def build():
    adults()
    parents()


if __name__ == '__main__':
    build()
