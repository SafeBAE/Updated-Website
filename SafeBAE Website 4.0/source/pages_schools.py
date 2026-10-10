"""SafeBAE 360° Schools (360-schools.html): the whole-school approach behind every program
a school can request. The four 360 sub-pages build from pages_schools2.py."""
from lib import *
from pages_home import ring_svg
from pages_schools2 import closing, CLOSE_CSS
import math

CAL = 'https://calendly.com/shaelnorris/60min'
PODIA = 'https://safebae.podia.com/'
PILOT_PDF = 'https://www.safebae.org/wp-content/uploads/2025/06/SafeBAE-360-Schools-Pilot-Data.pdf'
REES_LOGIN = 'https://safebae.reessecureus.com/en/Login'
VC = 'https://checkyourvibe.org/'
REQ = 'request-a-program.html'

_SVG, RCOMPS = ring_svg()   # (title, href, fill, ink)
SHORT = ['Peer Educator Training', 'Consent Curriculum', 'Faculty & Staff Training', 'Policy Support', 'Anonymous Reporting (REES)', 'Accountability Resources']

# ------------------------------------------------------------------ shared bits
def seg_path(i, cx, cy, R, r, gap):
    a0 = math.radians(-90 + i * 60 + gap / 2); a1 = math.radians(-90 + (i + 1) * 60 - gap / 2)
    p = lambda rad, ang: (cx + rad * math.cos(ang), cy + rad * math.sin(ang))
    x0, y0 = p(R, a0); x1, y1 = p(R, a1); x2, y2 = p(r, a1); x3, y3 = p(r, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z'

def mini_ring(cls='', inner=22):
    segs = [f'<path d="{seg_path(i, 50, 50, 49, inner, 4)}" fill="{fill}"/>' for i, (t, h, fill, ink) in enumerate(RCOMPS)]
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{"".join(segs)}</svg>'

def crumbs(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(a(esc(t), h) if h else f'<span>{esc(t)}</span>' for t, h in items) + '</nav>'

def checks(items, cls='s3-checks'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

# ------------------------------------------------------------------ CSS
CSS = '''
/* ---- eyebrows: Logo Teal on light, mint on dark, white on teal ---- */
.s3 main .eyebrow{color:var(--logo-teal)}
.s3 main :is(.band--slate,.band--deep,.band--logo,.s3-cta) .eyebrow{color:var(--mint)}
.s3 main .band--teal .eyebrow{color:#fff}
.s3 main .s3-ev .eyebrow{color:var(--slate)}
.s3 main .section-head{margin-bottom:var(--head-gap)}
.s3-hx{position:relative; overflow:hidden}
.s3-hx > .wrap{position:relative; z-index:1}

@media (max-width:860px){.s3 main .arrow-link{min-height:44px} .s3 main .btn--sm{min-height:44px}}
.s3-hero .crumbs a{padding-block:13px; margin-block:-13px}

/* ---- hero ---- */
.s3-hero{color:#fff; --wm-o:.2}
.s3-hero .wm-daisy{left:auto; right:-11%; bottom:auto; top:-9%; width:min(64vw,860px)}
.s3-hero__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,60px); align-items:stretch; padding-block:clamp(40px,5vw,68px) clamp(28px,3.2vw,44px)}
.s3-hero__txt{align-self:center; min-width:0}
.s3-hero .crumbs{margin-bottom:18px}
.s3-hero .eyebrow{margin-bottom:.9rem}
.s3-hero h1{font-weight:900; font-stretch:122%; text-transform:uppercase; line-height:.88; letter-spacing:-.02em; font-size:clamp(2.3rem,4.4vw,4rem); margin:0 0 .4em}
.s3-hero h1 span{display:block}
.s3-hero h1 .big{font-size:2.3em; font-stretch:125%; line-height:.84; letter-spacing:-.035em; margin:.02em 0 .04em}
.s3-hero__sub{font-family:var(--display); font-stretch:108%; font-weight:700; font-size:clamp(1.15rem,1.7vw,1.45rem); line-height:1.25; color:var(--aqua); margin:0 0 .7em}
.s3-hero .lede{color:rgba(255,255,255,.9); font-size:clamp(1rem,1.2vw,1.12rem); margin-bottom:1.3em}
.s3-mosaic{position:relative; display:grid; grid-template-columns:1fr 1fr; gap:12px; min-height:480px; animation:sb-rise-r 1s .1s var(--ease) both}
.s3-mosaic__col{display:flex; flex-direction:column; gap:12px; min-width:0}
.s3-mosaic__col:first-child{padding-bottom:44px}
.s3-mosaic__col:last-child{padding-top:44px}
.s3-ph{position:relative; flex:1 1 0; min-height:0; margin:0; border-radius:var(--r-xl); overflow:hidden; background:var(--slate-deep)}
.s3-ph--t{flex-grow:1.3}
.s3-ph img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-orb{position:absolute; left:50%; top:50%; width:clamp(128px,13vw,176px); aspect-ratio:1; transform:translate(-50%,-50%); border-radius:50%; background:var(--slate); box-shadow:0 0 0 10px var(--slate), 0 24px 60px -10px rgba(0,0,0,.6); display:grid; place-items:center; z-index:2}
.s3-orb svg{position:absolute; inset:6px; width:calc(100% - 12px); height:calc(100% - 12px); animation:s3turn 1.8s .25s var(--ease) both}
.s3-orb span{position:relative; font-family:var(--display); font-weight:900; font-stretch:125%; color:#fff; font-size:clamp(1.6rem,2.3vw,2.2rem); letter-spacing:-.02em}
@keyframes s3turn{from{transform:rotate(-220deg) scale(.7); opacity:0}}
.s3-mosaic .sticker{position:absolute; z-index:3}
.s3-proof{position:relative; z-index:1; display:flex; flex-wrap:wrap; gap:8px clamp(20px,3vw,44px); margin:0; padding:16px 0 clamp(26px,3vw,40px); list-style:none; border-top:1px solid var(--line-dark); font-weight:600; font-size:.95rem; color:var(--aqua)}
.s3-proof li{margin:0; display:flex; align-items:center; gap:10px}
.s3-proof li::before{content:""; flex:none; width:9px; height:9px; background:var(--mint); transform:rotate(45deg)}
@media (max-width:900px){
  .s3-hero__grid{grid-template-columns:1fr; gap:0}
  .s3-hero__txt{display:contents}
  .s3-hero__txt > *{order:1}
  .s3-hero__txt > .s3-hero__sub{order:3; margin-top:1.3rem}
  .s3-hero__txt > .lede, .s3-hero__txt > .btns{order:3}
  .s3-mosaic{order:2; width:100%; min-height:0; aspect-ratio:16/11; margin-top:.4rem}
  .s3-hero .wm-daisy{top:1%; bottom:auto; right:-34%; width:min(112vw,640px)}
}
@media (max-width:520px){.s3-mosaic__col:first-child{padding-bottom:28px} .s3-mosaic__col:last-child{padding-top:28px} .s3-mosaic{gap:8px; aspect-ratio:1/1.02} .s3-mosaic__col{gap:8px} .s3-proof{flex-direction:column; gap:8px}}

/* ---- the 360 dial: ring + detail as one unit ---- */
.s3-dial{scroll-margin-top:96px; --c:#15ffc8; --ci:#1d414e; display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff; box-shadow:var(--shadow-soft)}
.s3-dial__tabs{grid-column:1/-1; display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); border-bottom:1px solid var(--line)}
.s3-dial__tabs button{position:relative; font:inherit; display:flex; align-items:center; gap:10px; min-height:68px; padding:12px 14px; border:0; border-right:1px solid var(--line); background:#fff; color:var(--slate); text-align:left; cursor:pointer; min-width:0; transition:background .25s var(--ease), color .25s var(--ease)}
.s3-dial__tabs button:last-child{border-right:0}
.s3-dial__tabs button b{flex:none; width:32px; height:32px; border-radius:50%; display:grid; place-items:center; background:var(--c); color:var(--ci); font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1rem; line-height:1; transition:transform .3s var(--ease), box-shadow .25s}
.s3-dial__tabs button span{font-family:var(--display); font-weight:800; font-stretch:104%; font-size:.95rem; line-height:1.15; min-width:0}
.s3-dial__tabs button::after{content:""; position:absolute; left:0; right:0; bottom:0; height:5px; background:var(--c); transform:scaleX(0); transform-origin:left; transition:transform .4s var(--ease)}
.s3-dial__tabs button:hover{background:var(--mist)}
.s3-dial__tabs button:hover b{transform:scale(1.12)}
.s3-dial__tabs button:focus-visible{outline-offset:-4px}
.s3-dial__tabs button[aria-pressed="true"]:focus-visible{outline-color:var(--mint)}
.s3-dial__tabs button[aria-pressed="true"]{background:var(--slate); color:#fff}
.s3-dial__tabs button[aria-pressed="true"] b{box-shadow:0 0 0 2px rgba(255,255,255,.55)}
.s3-dial__tabs button[aria-pressed="true"]::after{transform:scaleX(1)}
.s3-dial__stage{position:relative; display:grid; place-items:center; padding:clamp(24px,2.6vw,34px); background:var(--mist); min-width:0}
.s3-dial__ring{position:relative; width:100%; max-width:416px; container-type:inline-size}
.s3-dial .ring{display:block; width:100%; height:auto; overflow:visible; transform:rotate(var(--rot,0deg)); transition:transform 1s var(--ease)}
.s3-dial .ring > text{display:none}
.s3-dial .seg{cursor:pointer; outline:none; transition:transform .5s var(--ease)}
.s3-dial .seg path{transition:filter .25s; stroke-linejoin:round}
.s3-dial .seg text{transform-box:fill-box; transform-origin:center; transform:rotate(calc(var(--rot,0deg) * -1)); transition:transform 1s var(--ease); pointer-events:none}
.s3-dial .seg:hover path, .s3-dial .seg.hot path{filter:brightness(1.1) saturate(1.1)}
.s3-dial .seg:hover text, .s3-dial .seg.hot text{transform:rotate(calc(var(--rot,0deg) * -1)) scale(1.22)}
.s3-dial .seg.on{transform:translate(var(--tx,0px), var(--ty,0px))}
.s3-dial .seg.on path{filter:drop-shadow(0 6px 10px rgba(22,53,64,.28))}
.s3-dial .seg.on text{transform:rotate(calc(var(--rot,0deg) * -1)) scale(1.4)}
.s3-dial .seg:focus-visible path{stroke:#1d414e; stroke-width:5}
.s3-dial .seg[data-seg="3"]:focus-visible path, .s3-dial .seg[data-seg="2"]:focus-visible path{stroke:#15ffc8}
.s3-dial__hub{position:absolute; inset:0; display:grid; place-items:center; pointer-events:none}
.s3-dial__hub::before{content:""; position:absolute; left:50%; top:50%; width:53cqi; aspect-ratio:1; translate:-50% -50%; border-radius:50%; background:#fff; box-shadow:0 14px 34px -16px rgba(22,53,64,.45), 0 0 0 1px rgba(29,65,78,.06)}
.s3-dial__hub b{position:relative; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:15.5cqi; line-height:1; letter-spacing:-.03em; color:var(--slate); translate:0 -5cqi}
.s3-dial__hub span{position:absolute; left:50%; top:calc(50% + 5.5cqi); width:46cqi; translate:-50% 0; text-align:center; font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; line-height:1.3; color:var(--ink-soft); transition:color .2s}
.s3-dial__hub span.is-pre{color:var(--slate)}
.s3-dial__hint{position:absolute; left:clamp(16px,2vw,24px); top:clamp(14px,1.8vw,20px); margin:0; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--ink-soft)}
.s3-dial__nav{position:absolute; bottom:clamp(14px,1.8vw,22px); width:46px; height:46px; border-radius:50%; border:2px solid var(--slate); background:#fff; color:var(--slate); cursor:pointer; display:grid; place-items:center; font:inherit; font-size:1.15rem; font-weight:800; line-height:1; transition:background .2s, color .2s, transform .2s var(--ease)}
.s3-dial__nav--prev{left:clamp(14px,1.8vw,22px)} .s3-dial__nav--next{right:clamp(14px,1.8vw,22px)}
.s3-dial__nav:hover{background:var(--slate); color:var(--mint)}
.s3-dial__nav--next:hover{transform:translateX(3px)} .s3-dial__nav--prev:hover{transform:translateX(-3px)}
.s3-dial__detail{scroll-margin-top:84px; position:relative; display:flex; min-width:0; padding:clamp(24px,2.8vw,38px) clamp(24px,3.2vw,44px); border-left:8px solid var(--c); transition:border-color .5s var(--ease)}
.s3-dial__detail::before{content:""; position:absolute; left:-23px; top:50%; width:16px; height:32px; margin-top:-16px; background:var(--c); clip-path:polygon(100% 0, 0 50%, 100% 100%); transition:background .5s var(--ease)}
.s3-comps{display:grid; flex:1; min-width:0}
.s3-comp{display:flex; flex-direction:column; min-width:0}
.s3-comp + .s3-comp{margin-top:36px}
.js .s3-comp + .s3-comp{margin-top:0}
.js .s3-comp{grid-area:1/1; visibility:hidden; opacity:0; transform:translateX(18px); transition:opacity .3s var(--ease), transform .4s var(--ease), visibility 0s .3s}
.js .s3-comp.on{visibility:visible; opacity:1; transform:none; transition:opacity .5s .14s var(--ease), transform .6s .14s var(--ease), visibility 0s}
.s3-comp > .s3-comp__k{display:flex; align-items:center; gap:10px; margin:0 0 14px; font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}
.s3-comp__top{display:flex; gap:16px; align-items:center; margin-bottom:14px}
.s3-comp__n{flex:none; width:60px; height:60px; border-radius:50%; display:grid; place-items:center; background:var(--pc); color:var(--pi); font-family:var(--display); font-weight:900; font-stretch:125%; font-size:1.9rem; line-height:1}
.s3-comp__top h3{margin:0; font-size:clamp(1.4rem,2.2vw,1.95rem)}
.s3-comp > p{color:var(--ink-soft); margin:0 0 16px; font-size:1rem}
.s3-comp .s3-checks{margin:0 0 20px}
.s3-comp__links{margin-top:auto; padding-top:16px; border-top:1px solid var(--line); display:flex; flex-wrap:wrap; gap:8px 26px}
.s3-comp__links .arrow-link{min-height:32px}
.s3 .arrow-link--ext::after{content:"\\2197"}
.s3-rees-x{scroll-margin-top:min(500px,56vh); display:flex; align-items:center; gap:18px; margin:-4px 0 18px; padding:10px 16px; border-radius:14px; background:var(--mist); border:1px solid var(--line)}
.s3-rees-x img{flex:none; width:104px; height:auto}
.s3-rees-x p{margin:0; padding-left:18px; border-left:1px solid var(--line); font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.08rem; line-height:1.25; color:var(--slate)}
@media (max-width:460px){.s3-rees-x{flex-direction:column; align-items:flex-start; gap:10px} .s3-rees-x p{padding-left:0; border-left:0}}
@media (min-width:861px) and (max-width:1100px){
  /* mid widths: the six names move under the ring so the left column is as tall as the detail */
  .s3-dial{grid-template-rows:auto 1fr}
  .s3-dial__stage{grid-column:1; grid-row:1; height:356px; padding:26px}
  .s3-dial__ring{max-width:286px}
  .s3-dial__tabs{grid-column:1; grid-row:2; display:flex; flex-direction:column; border-bottom:0; border-top:1px solid var(--line); background:var(--mist)}
  .s3-dial__tabs button{flex:1 1 auto; min-height:46px; padding:6px 20px; border-right:0; border-bottom:1px solid var(--line); background:transparent}
  .s3-dial__tabs button:last-child{border-bottom:0}
  .s3-dial__tabs button:hover{background:#fff}
  .s3-dial__tabs button[aria-pressed="true"]{background:var(--slate)}
  .s3-dial__tabs button::after{right:auto; top:0; width:5px; height:auto; transform:scaleY(0); transform-origin:top}
  .s3-dial__tabs button[aria-pressed="true"]::after{transform:scaleY(1)}
  .s3-dial__detail{grid-column:2; grid-row:1 / span 2}
  .s3-dial__detail::before{top:178px}
}
@media (max-width:860px){
  .s3-dial{grid-template-columns:1fr}
  .s3-dial__tabs{display:flex; overflow-x:auto; scrollbar-width:none; scroll-snap-type:x proximity; -webkit-overflow-scrolling:touch}
  .s3-dial__tabs::-webkit-scrollbar{display:none}
  .s3-dial__tabs button{flex:0 0 auto; flex-direction:row; align-items:center; gap:10px; min-height:60px; padding:10px 16px; white-space:nowrap; scroll-snap-align:center}
  .s3-dial__tabs button:last-child{border-right:1px solid var(--line)}
  .s3-dial__stage{padding:44px 20px 30px}
  .s3-dial__ring{max-width:300px}
  .s3-dial__detail{border-left:0; border-top:8px solid var(--c); padding:26px 20px 22px}
  .s3-dial__detail::before{left:50%; top:-23px; width:32px; height:16px; margin:0 0 0 -16px; clip-path:polygon(0 100%, 50% 0, 100% 100%)}
  .js .s3-comp{display:none; transform:none}
  .js .s3-comp.on{display:flex; animation:s3in .5s var(--ease)}
}
@keyframes s3in{from{opacity:0; transform:translateY(-10px)}}
@media (max-width:400px){.s3-dial__ring{max-width:264px} .s3-dial__nav{width:44px; height:44px}}

.s3-checks{list-style:none; padding:0; margin:0; display:grid; gap:8px}
.s3-checks li{position:relative; padding-left:30px; margin:0; font-weight:600; line-height:1.4}
.s3-checks li::before{content:""; position:absolute; left:0; top:.12em; width:20px; height:20px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/13px no-repeat}
.s3-checks--2{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px 22px}
@media (max-width:620px){.s3-checks--2{grid-template-columns:1fr}}

/* ---- how schools adopt: young people lead, then four steps ---- */
.s3-how{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap) clamp(28px,5vw,72px); align-items:stretch}
.s3-how__side{display:flex; flex-direction:column; gap:var(--gap); min-width:0}
.s3-lead{border-radius:var(--r-xl); padding:var(--pad-card); background:var(--mint); color:var(--slate); display:flex; flex-direction:column; gap:14px}
.s3 .s3-lead .s3-lead__h{margin:0; font-family:var(--display); font-weight:900; font-stretch:116%; text-transform:uppercase; font-size:clamp(1.5rem,2.35vw,2.2rem); line-height:.95; letter-spacing:-.015em; color:var(--slate); overflow-wrap:anywhere}
.s3-lead > p:not(.s3-lead__h){margin:0; font-size:1.06rem; font-weight:500; line-height:1.5}
.s3 .s3-lead .arrow-link{color:var(--slate); margin-top:auto}
.s3-lead :focus-visible{outline-color:var(--slate)}
.s3-how__note{margin-top:auto; border-radius:var(--r-xl); padding:var(--pad-card); background:rgba(255,255,255,.06); border:1px solid var(--line-dark)}
.s3-how__note b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.3rem; line-height:1.15; color:var(--mint); margin-bottom:8px}
.s3-how__note p{margin:0 0 14px; color:rgba(255,255,255,.88); font-size:1rem}
.s3-how__steps{list-style:none; margin:0; padding:0; display:grid; gap:clamp(20px,2.4vw,30px); align-content:space-between}
.s3-how__steps li{position:relative; margin:0; display:grid; grid-template-columns:56px minmax(0,1fr); gap:clamp(16px,2vw,24px); align-items:start}
.s3-how__steps li:not(:last-child)::before{content:""; position:absolute; left:27px; top:62px; bottom:calc(-1 * clamp(20px,2.4vw,30px) + 6px); width:2px; border-radius:2px; background:rgba(21,255,200,.38)}
.s3-how__n{width:56px; height:56px; border-radius:50%; border:2px solid var(--mint); display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:1.5rem; color:var(--mint); line-height:1}
.s3-how__steps h3{margin:.45em 0 .3em; font-size:clamp(1.25rem,1.8vw,1.5rem); color:#fff}
.s3-how__steps p{margin:0; color:rgba(255,255,255,.86); font-size:1rem}
.s3 .s3-how__steps .link{color:var(--mint)}
@media (max-width:900px){.s3-how{grid-template-columns:1fr} .s3-how__side{display:contents} .s3-lead{order:1} .s3-how__steps{order:2; margin-block:8px} .s3-how__note{order:3; margin-top:0}}
@media (max-width:460px){.s3-how__steps li{grid-template-columns:44px minmax(0,1fr); gap:14px} .s3-how__n{width:44px; height:44px; font-size:1.2rem} .s3-how__steps li:not(:last-child)::before{left:21px; top:50px} .s3-how__steps h3{margin-top:.25em}}

/* ---- roles ---- */
.s3-roles__tabs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap); margin-bottom:var(--gap)}
.s3-roles__tab{font:inherit; text-align:left; padding:14px 18px; border-radius:14px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; display:flex; flex-direction:column; gap:3px; min-width:0; transition:border-color .2s, background .2s, color .2s, transform .2s var(--ease)}
.s3-roles__tab small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal)}
.s3-roles__tab span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.15rem; line-height:1.15}
.s3-roles__tab:hover{border-color:var(--teal); transform:translateY(-2px)}
.s3-roles__tab[aria-selected="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.s3-roles__tab[aria-selected="true"] small{color:var(--mint)}
.s3-roles__panel{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.s3-roles__img{position:relative; border-radius:var(--r-xl); overflow:hidden; min-height:320px; margin:0}
.s3-roles__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.s3-roles__body{min-width:0; display:flex; flex-direction:column; padding-left:clamp(0px,1.4vw,18px)}
.s3-roles__body h3{font-size:clamp(1.4rem,2.2vw,1.9rem); margin-bottom:.35em}
.s3-roles__body > p{margin:0 0 16px}
.s3-roles__body .rows{margin-top:auto}
.s3-roles__body .row{padding-block:14px}
.s3-roles__body .row > span:first-child{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:3px 14px; align-items:center; min-width:0}
.s3-roles__body .row b{grid-column:1; font-size:1.14rem}
.s3-roles__body .row small{grid-column:1/-1; grid-row:2; margin:0; font-size:.93rem}
.s3-roles__body .row__meta{grid-column:2; grid-row:1; margin:0; flex-wrap:nowrap}
@media (max-width:900px){.s3-roles__tabs{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px} .s3-roles__panel{grid-template-columns:1fr} .s3-roles__img{min-height:0; aspect-ratio:16/10} .s3-roles__body{padding-left:0}}
@media (max-width:560px){.s3-roles__body .row > span:first-child{grid-template-columns:minmax(0,1fr)} .s3-roles__body .row small{grid-row:auto} .s3-roles__body .row__meta{grid-column:1; grid-row:auto; margin-top:6px; flex-wrap:wrap}}
@media (max-width:420px){.s3-roles__tab{padding:12px 12px} .s3-roles__tab span{font-size:1.02rem}}

/* ---- evidence ---- */
.s3-evtabs{display:flex; gap:8px; flex-wrap:wrap; margin:0 0 16px}
.s3-evtabs button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1rem; min-height:46px; padding:10px 20px; border-radius:999px; border:2px solid var(--slate); background:transparent; color:var(--slate); cursor:pointer; transition:background .2s, color .2s}
.s3-evtabs button:hover{background:rgba(29,65,78,.1)}
.s3-evtabs button[aria-selected="true"]{background:var(--slate); color:#fff}
.s3-evlead{font-weight:600; font-size:1.06rem; margin:0 0 16px}
.s3-stats{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.s3-stat{background:#fff; border-radius:14px; padding:20px 22px 22px; min-width:0; display:flex; flex-direction:column; gap:10px; box-shadow:0 10px 24px -20px rgba(22,53,64,.5)}
.s3-stat__n{display:flex; align-items:baseline; gap:12px; flex-wrap:wrap}
.s3-stat__n b{font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(2.4rem,3.7vw,3.3rem); line-height:.9; letter-spacing:-.02em; color:var(--logo-teal); font-variant-numeric:tabular-nums}
.s3-stat .k{font-family:var(--mono); font-size:.74rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.s3-meter{display:block; height:6px; border-radius:6px; background:rgba(29,65,78,.12); overflow:hidden}
.s3-meter i{display:block; height:100%; border-radius:6px; background:var(--teal); width:calc(var(--v) / 60 * 100%); transition:width 1.1s var(--ease)}
.js .s3-stats:not(.in) .s3-meter i{width:0}
.s3-stat p{margin:0; font-size:.97rem; line-height:1.45; font-weight:500}
.s3-stat--wide{grid-column:1/-1; display:grid; grid-template-columns:auto minmax(0,1fr); gap:10px clamp(20px,3vw,40px); align-items:center; background:var(--slate); color:#fff; padding:24px 28px}
.s3-stat--wide .s3-stat__n{flex-direction:column; align-items:flex-start; gap:8px}
.s3-stat--wide .s3-stat__n b{color:var(--mint); font-size:clamp(3.4rem,6.6vw,5.6rem)}
.s3-stat--wide .k{color:var(--aqua)}
.s3-stat--wide p{font-size:clamp(1.08rem,1.6vw,1.34rem); font-weight:600; line-height:1.35}
.s3-stat--wide .s3-stat__n{grid-column:1; grid-row:1} .s3-stat--wide p{grid-column:2; grid-row:1}
.s3-stat--wide .s3-meter{grid-column:1/-1; grid-row:2; background:rgba(255,255,255,.16)} .s3-stat--wide .s3-meter i{background:var(--mint)}
.s3-evfoot{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:14px 40px; margin-top:var(--gap)}
.s3-evfoot p{margin:0; font-size:.97rem; font-weight:500; flex:1 1 520px; min-width:0}
.s3-evfoot .btns{flex:0 1 auto; min-width:0}
.s3-evrow{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch; margin-top:clamp(28px,3.2vw,44px); padding-top:clamp(28px,3.2vw,44px); border-top:2px solid rgba(29,65,78,.2)}
.s3-evvid{margin:0; min-width:0; display:flex; flex-direction:column; gap:12px}
.s3-evvid .vid{border-radius:var(--r-xl)}
.s3-evvid figcaption{font-size:.97rem; font-weight:500; line-height:1.45}
.s3-voices{display:grid; grid-template-rows:1fr 1fr; gap:var(--gap); min-width:0}
.s3-voice{background:rgba(255,255,255,.62); border-radius:var(--r-xl); padding:var(--pad-card); margin:0; display:flex; flex-direction:column; justify-content:center; gap:12px}
.s3-voice p{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.12rem,1.6vw,1.38rem); line-height:1.26; margin:0}
.s3-voice cite{display:block; font-style:normal; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.s3-partners{margin-top:clamp(28px,3.2vw,44px)}
.s3-partners__head{display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:8px 28px; margin-bottom:16px}
.s3-partners__head h3{margin:0; font-size:clamp(1.3rem,2vw,1.6rem)}
.s3 .s3-partners__head .arrow-link{color:var(--slate)}
@media (max-width:860px){.s3-stats{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-evrow{grid-template-columns:1fr} .s3-voices{grid-template-rows:none}}
@media (max-width:560px){.s3-stats{grid-template-columns:1fr; gap:12px} .s3-stat{display:grid; grid-template-columns:96px minmax(0,1fr); gap:12px 14px; align-items:start; padding:16px 18px 18px} .s3-stat__n{flex-direction:column; align-items:flex-start; gap:8px} .s3-stat__n{grid-column:1; grid-row:1} .s3-stat__n b{font-size:2.2rem} .s3-stat p{grid-column:2; grid-row:1} .s3-stat .s3-meter{grid-column:1/-1; grid-row:2}
  .s3-stat--wide{grid-template-columns:1fr; padding:20px 18px} .s3-stat--wide .s3-stat__n b{font-size:3.6rem} .s3-stat--wide p{grid-column:1; grid-row:2} .s3-stat--wide .s3-meter{grid-row:3}}

/* ---- partner schools ---- */
.s3-logos{display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); background:#fff; border-radius:var(--r-xl); box-shadow:0 10px 24px -20px rgba(22,53,64,.5); overflow:hidden}
.s3-logo{display:grid; place-items:center; height:120px; padding:12px 10px; min-width:0}
.s3-logo + .s3-logo{border-left:1px solid var(--line)}
.s3-logo img{width:calc(var(--w,160px) * var(--k,.68)); max-width:94%; height:auto}
@media (max-width:1100px){.s3-logos{grid-template-columns:repeat(4,minmax(0,1fr))} .s3-logo{--k:.7} .s3-logo:nth-child(4n+1){border-left:0} .s3-logo:nth-child(n+5){border-top:1px solid var(--line)}}
@media (max-width:560px){.s3-logos{grid-template-columns:repeat(2,minmax(0,1fr))} .s3-logo{height:96px; --k:.66} .s3-logo:nth-child(odd){border-left:0} .s3-logo:nth-child(even){border-left:1px solid var(--line)} .s3-logo:nth-child(n+3){border-top:1px solid var(--line)}}
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
       gets=['A secure, encrypted record, kept at a student’s own pace', 'Anonymous or named reports to the school', 'School-specific resources and support', 'A reporting system customized to your community'],
       extra='rees',
       links=[('Become a partner school', REQ), ('Student access', REES_LOGIN)]),
  dict(text='A suite of tools designed for students who have caused harm, supporting education, accountability, and behavior change. It includes our structured Accountability Training and Vibe Check, a self-assessment tool that helps students recognize unhealthy relationship behaviors and warning signs in themselves. Rooted in prevention, healing, and restorative justice rather than punishment, these resources give schools a trauma-informed, developmentally appropriate alternative to traditional disciplinary responses.',
       gets=['Structured Accountability Training', 'Vibe Check self-assessment', 'Rooted in restorative justice', 'Developmentally appropriate'],
       links=[('Accountability Training', 'accountability-training.html'), ('About Vibe Check', 'vibe-check.html'), ('Open Vibe Check', VC)]),
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
    num = n.rstrip('%'); dec = len(num.split('.')[1]) if '.' in num else 0
    return (f'<div class="s3-stat {cls}"><div class="s3-stat__n"><b data-n="{num}" data-d="{dec}">{esc(n)}</b><span class="k">{esc(k)}</span></div>'
            f'<span class="s3-meter" aria-hidden="true" style="--v:{num}"><i></i></span><p>{esc(d)}</p></div>')

# ------------------------------------------------------------------ page
def p360():
    comps = RCOMPS
    # ---- hero
    def ph(name, alt, tall, pos):
        return f'<figure class="s3-ph{" s3-ph--t" if tall else ""}">{img(name, alt, loading="eager", style=f"object-position:{pos}")}</figure>'
    mosaic = f'''<div class="s3-mosaic">
      <div class="s3-mosaic__col">{ph('1-000383-edited', 'SafeBAE youth leaders in tie-dye shirts posing together', True, '50% 40%')}{ph('1-9035c3ab-2096-403f-9e8d-56238bfde8a1', 'Two students and a SafeBAE staff member holding SafeBAE t-shirts', False, '50% 30%')}</div>
      <div class="s3-mosaic__col">{ph('1-54982e7a-41f6-4540-a03d-2bd16547a2fa', 'Students holding up SafeBAE water bottles outdoors', False, '50% 55%')}{ph('1-7c1d4302-803a-4154-b18a-3a64432a6c76', 'Five young SafeBAE leaders standing together on a campus walkway', True, '50% 35%')}</div>
      <div class="s3-orb" aria-hidden="true">{mini_ring()}<span>360&deg;</span></div>
      <span class="sticker" style="left:-10px;top:7%">Youth-led</span>
      <span class="sticker sticker--white sticker--r" style="right:-6px;bottom:9%">Survivor-centered</span>
    </div>'''
    hero = f'''<section class="s3-hero s3-hx band--slate">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap s3-hero__grid">
    <div class="rise s3-hero__txt">
      {crumbs([('Home', 'index.html'), ('Request a Program', REQ), ('SafeBAE 360° Schools', None)])}
      <p class="eyebrow">SafeBAE&rsquo;s whole-school approach</p>
      <h1 aria-label="SafeBAE 360° Schools"><span>SafeBAE</span><span class="big mk">360&deg;</span><span>Schools</span></h1>
      <p class="s3-hero__sub">Tools, training and youth leadership to build safer school communities, together.</p>
      <p class="lede">SafeBAE 360° is the comprehensive, survivor-centered prevention model behind every program a school can request. Created by and for young people, it reimagines how schools address sexual and dating violence and builds lasting infrastructure for prevention across education, leadership, policy, reporting and accountability, so that every student has access to support and every school has the tools to respond.</p>
      <div class="btns">{btn('Request a program', REQ, 'mint', arrow=True)}{btn('Book a 60-minute meeting', CAL, 'ghost')}</div>
    </div>
    {mosaic}
  </div>
  <div class="wrap"><ul class="s3-proof"><li>Six components</li><li>Start with one or build the whole model</li><li>Sliding scale pricing</li></ul></div>
</section>'''

    # ---- six components: the dial
    tabs = ''.join(f'<button type="button" data-pick="{i}" data-name="{esc(SHORT[i])}" aria-pressed="{str(i==0).lower()}" style="--c:{c[2]}; --ci:{c[3]}"><b>{i+1}</b><span>{esc(SHORT[i])}</span></button>' for i, c in enumerate(comps))
    panels = []
    for i, (t, h, fill, ink) in enumerate(comps):
        d = COMP_DATA[i]
        links = ''.join(a(esc(lbl), hh, 'arrow-link' + (' arrow-link--ext' if hh.startswith('http') else '')) for lbl, hh in d['links'])
        extra = (f'<div class="s3-rees-x" id="rees">{img("logo-horiz-rgb", "REES")}<p>Nothing is shared without the student’s consent.</p></div>'
                 if d.get('extra') == 'rees' else '')
        panels.append(f'''<div class="s3-comp{' on' if i==0 else ''}" id="component-{i+1}" style="--pc:{fill}; --pi:{ink}">
        <p class="s3-comp__k">Component {i+1} of 6</p>
        <div class="s3-comp__top"><span class="s3-comp__n">{i+1}</span><h3>{esc(t)}</h3></div>
        <p>{esc(d['text'])}</p>
        {checks([esc(x) for x in d['gets']], 's3-checks s3-checks--2')}
        {extra}
        <div class="s3-comp__links">{links}</div>
      </div>''')
    ring = f'''<section class="band band--paper" id="components">
  <div class="wrap">
    <div class="section-head"><div><h2>Six components that work together</h2>
      <p class="lede lede--full muted">SafeBAE 360° includes six core components that create lasting, schoolwide culture change, where prevention, support, and accountability are embedded in everyday life. Each component can also be implemented on its own, depending on a school’s needs.</p></div></div>
    <div class="s3-dial reveal">
      <div class="s3-dial__tabs" role="group" aria-label="Choose a component">{tabs}</div>
      <div class="s3-dial__stage">
        <p class="s3-dial__hint">Select a segment</p>
        <div class="s3-dial__ring">{_SVG}<div class="s3-dial__hub" aria-hidden="true"><b>360&deg;</b><span data-hub>Six components</span></div></div>
        <button type="button" class="s3-dial__nav s3-dial__nav--prev" data-step="-1" aria-label="Previous component">&larr;</button>
        <button type="button" class="s3-dial__nav s3-dial__nav--next" data-step="1" aria-label="Next component">&rarr;</button>
      </div>
      <div class="s3-dial__detail"><div class="s3-comps" aria-live="polite">{''.join(panels)}</div></div>
    </div>
  </div>
</section>'''

    # ---- how schools adopt (young people lead every implementation)
    steps = [
      ('Start the conversation', f'Send {a("a program request", REQ, "link")} telling us what you’re looking for and how to follow up, or {a("book a 60-minute meeting", CAL, "link")} with the SafeBAE team.'),
      ('Choose a starting point', f'Some partners begin with {a("a single assembly", "assemblies.html", "link")} or awareness event. Others start a deeper collaboration right away. Every component can be delivered on its own.'),
      ('Adapt it to your school', 'Each implementation is adapted to your school’s context, prioritizing cultural relevance, sustainability, and the needs of those most impacted.'),
      ('Build over time', 'Youth leaders help shape implementation as components are added, building toward the collective and sustained change that real prevention requires.'),
    ]
    steps_html = ''.join(f'<li><span class="s3-how__n">{i+1}</span><div><h3>{esc(t)}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))
    how = f'''<section class="band band--slate" id="how">
  <div class="wrap">
    <div class="section-head"><div><h2>How schools adopt SafeBAE 360°</h2>
      <p class="lede lede--full">Schools can implement SafeBAE 360° in full or one component at a time. Either way, it rests on the belief that real prevention requires collective and sustained change.</p></div></div>
    <div class="s3-how">
      <div class="s3-how__side">
        <div class="s3-lead reveal">
          <p class="s3-lead__h">Young people lead every implementation.</p>
          <p>Rather than treating students as passive recipients of adult-designed interventions, SafeBAE 360° equips young people to lead.</p>
          <a class="arrow-link" href="peer-educator.html">Peer Educator Training</a>
        </div>
        <div class="s3-how__note"><b>Starting with an assembly?</b><p>SafeBAE assemblies and school events are always co-presented with youth leaders and tailored to be age-appropriate. They often become the starting place for longer-term collaboration.</p><a class="arrow-link" href="assemblies.html">About assemblies</a></div>
      </div>
      <ol class="s3-how__steps">{steps_html}</ol>
    </div>
  </div>
</section>'''

    # ---- where each role starts
    roles = [
      ('leaders', 'District &amp; school', 'Leaders &amp; administrators', '066', 'SafeBAE staff and youth leaders in front of a full gym of students at a school assembly', '50% 45%',
       'Strengthen policy, train staff and give students a lasting role in prevention',
       'Start with the piece your school needs most and add components as capacity grows. Pricing is on a sliding scale.',
       [('School Policy Reform Guide', 'A step-by-step resource for strengthening sexual misconduct policies beyond the federal minimum.', 'policy-reform-guide.html', ['Administrators', 'Districts']),
        ('Faculty & Staff Training', 'Trauma-informed professional development, in person or virtual.', 'professional-development.html', ['PD']),
        ('Healthy Relationship & Consent Curriculum', '15 lessons aligned with the National Health Education Standards.', 'consent-curriculum.html', ['NHES']),
        ('Talk through scope and pricing', 'Sliding scale pricing based on program scope, number of speakers and travel.', CAL, ['60 min'])]),
      ('counselors', 'Counselors &amp;', 'Title IX staff', 'img-2395', 'Two SafeBAE facilitators leading a discussion in front of a classroom whiteboard', '50% 40%',
       'Give students safe ways to come forward and a path to accountability',
       'Students can document harm privately and report to your school on their terms. Students who have caused harm get structured education, while survivors keep the choice of how to proceed.',
       [('Accountability Training', 'A multi-lesson virtual program for students who have harmed another student.', 'accountability-training.html', ['Respondents']),
        ('Anonymous reporting with REES', 'Students document incidents privately and can report anonymously or by name.', '#rees', ['Partner schools']),
        ('Responding to disclosures', 'Staff training on trauma-informed responses to disclosures of harm.', 'professional-development.html', ['PD']),
        ('Vibe Check', 'A free, anonymous reflection tool for students worried they crossed a line.', 'vibe-check.html', ['Anonymous'])]),
      ('teachers', 'Health &amp;', 'Classroom teachers', 'img-3947', 'A SafeBAE lesson projected at the front of a classroom while students watch', '50% 50%',
       'Teach consent and healthy relationships with ready-made lessons',
       'Teach the curriculum yourself, co-teach with Certified Peer Educators, or have the SafeBAE team deliver it.',
       [('Healthy Relationship & Consent Curriculum', '15 lessons of 45 to 60 minutes with slides, facilitator guides and knowledge checks.', 'consent-curriculum.html', ['15 lessons']),
        ('Films & teaching guides', 'Youth-made films, each with a free teaching guide for short, meaningful discussions.', 'library.html#guides', ['Free']),
        ('Peer educators as co-teachers', 'Certified Peer Educators co-facilitate curriculum sessions.', 'peer-educator.html', ['Youth-led']),
        ('Free prevention posters', 'For classrooms, counseling offices, hallways and wellness centers.', 'posters.html', ['Download'])]),
      ('students', 'For', 'Students', 'safebae-consent-summits', 'A group of SafeBAE youth leaders in SafeBAE shirts at a consent summit by the water', '50% 60%',
       'Lead prevention at your school',
       'Youth leaders help shape implementation, lead presentations, co-facilitate curriculum sessions and organize campaigns through SafeBAE Clubs. Everything for students is free.',
       [('Certified Peer Educator Training', 'Free, self-paced, 16 online modules and an official certificate.', 'peer-educator.html', ['Free']),
        ('Start or join a SafeBAE club', 'Register a new chapter, affiliate a club you already run, or restart last year’s.', 'clubs.html', ['Clubs']),
        ('Reform your school’s policy', 'The student guide to advocating for safer, survivor-centered policies.', 'reform-policy.html', ['Student guide'])]),
    ]
    rtabs = ''.join(f'<button class="s3-roles__tab" role="tab" id="role-{k}" aria-controls="rolep-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{pre}</small><span>{lbl}</span></button>' for i, (k, pre, lbl, *_r) in enumerate(roles))
    rpanels = ''.join(f'''<div class="s3-roles__panel" role="tabpanel" id="rolep-{k}" aria-labelledby="role-{k}"{'' if i==0 else ' hidden'}>
      <figure class="s3-roles__img">{img(im, alt, style=f"object-position:{pos}")}</figure>
      <div class="s3-roles__body"><h3>{esc(h)}</h3><p class="muted">{esc(p)}</p><div class="rows">{''.join(row(t, dd, u, m) for t, dd, u, m in rws)}</div></div></div>''' for i, (k, pre, lbl, im, alt, pos, h, p, rws) in enumerate(roles))
    who = f'''<section class="band band--paper" id="who">
  <div class="wrap">
    <div class="section-head"><div><h2>Where each role starts</h2></div></div>
    <div data-tabs="s3-roles"><div class="s3-roles__tabs" role="tablist" aria-label="Choose your role">{rtabs}</div>{rpanels}</div>
  </div>
</section>'''

    # ---- what the pilot found: the numbers, then the people and the partner schools behind them
    st_students = ''.join(stat(*x) for x in STUDENT_STATS)
    st_teachers = stat(*TEACHER_STATS[0], cls='s3-stat--wide') + ''.join(stat(*x) for x in TEACHER_STATS[1:])
    # (image, name, display width in px): widths set so the visible marks carry the same weight despite different canvases
    logos = [('rini-color-01cbb034', 'Rhode Island Nurses Institute Middle College', 204), ('chatgpt-image-dec-10-2025-08-34-32-am', 'Paul Cuffee School', 207),
             ('alliance-logo-color-vertical', 'Alliance College-Ready Public Schools', 121), ('walogolg-3', 'Worcester Academy', 212),
             ('header-logo-stacked-3', 'Central Catholic High School', 106), ('6716423ef4c1138196fb7101-phillips-exeter-academy-lion', 'Phillips Exeter Academy', 101),
             ('9e389524-a5f5-4c66-aee6-395723e59586', 'Flintridge Prep', 110), ('63750970-0a6d-4483-b1d7-351445fc2a67', 'Harvard-Westlake School', 174)]
    logo_html = ''.join(f'<div class="s3-logo" style="--w:{w}px" title="{esc(nm)}">{img(n, nm + " logo")}</div>' for n, nm, w in logos)
    ev = f'''<section class="band band--mint s3-ev" id="evidence">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Pilot data &middot; 2023&ndash;24 school year</p><h2>What the 360° pilot found</h2>
      <p class="lede lede--full">We believe prevention should always be youth-led and evidence-driven. {esc(PILOT_LINE)}</p></div></div>
    <div data-tabs="s3-pilot">
      <div class="s3-evtabs" role="tablist" aria-label="Pilot results"><button role="tab" id="pilot-students" aria-controls="pilotp-students" aria-selected="true" tabindex="0">Students</button><button role="tab" id="pilot-teachers" aria-controls="pilotp-teachers" aria-selected="false" tabindex="-1">Teachers</button></div>
      <div role="tabpanel" id="pilotp-students" aria-labelledby="pilot-students"><p class="s3-evlead">Students who took part in SafeBAE’s programs were more prepared to step in when they witnessed harmful or potentially harmful actions.</p><div class="s3-stats">{st_students}</div></div>
      <div role="tabpanel" id="pilotp-teachers" aria-labelledby="pilot-teachers" hidden><p class="s3-evlead">Teachers who took part in SafeBAE’s programs were more likely to believe that their school policies could protect students from violence and thoroughly respond if violence occurs.</p><div class="s3-stats">{st_teachers}</div></div>
    </div>
    <div class="s3-evfoot">
      <p>Source: SafeBAE 360° Schools Pilot Data, 2023–24 school year. Our findings come from ongoing evaluations, youth-designed surveys, internal assessments, and published research, including a study in the <i>Journal of Child Sexual Abuse</i>.</p>
      <div class="btns">{btn('Download data report', PILOT_PDF, 'slate')}{btn('Data & impact', 'impact.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="s3-evrow">
      <figure class="s3-evvid">{yt('ur2b6V1Pipk', 'SafeBAE at Alliance Ted K. Tajima High School', label='Watch')}
        <figcaption>Araceli Martinez, Community Schools Coordinator at Alliance Ted K. Tajima High School, reflects on why she brings SafeBAE to her campus and what she’s seen students gain from it.</figcaption></figure>
      <div class="s3-voices">
        <blockquote class="s3-voice"><p>“I like the focus on empowering students and making them central to the work.”</p><cite>Pilot participant</cite></blockquote>
        <blockquote class="s3-voice"><p>“[SafeBAE] works collaboratively with students to promote healthier relationships and a positive dating culture in and out of school.”</p><cite>Teacher, pilot school</cite></blockquote>
      </div>
    </div>
    <div class="s3-partners">
      <div class="s3-partners__head"><h3>Recent partner schools</h3><a class="arrow-link" href="partners-press.html">Partners &amp; press</a></div>
      <div class="s3-logos reveal">{logo_html}</div>
    </div>
  </div>
</section>'''

    body = hero + ring + how + who + ev + closing(
        'Bring SafeBAE 360° to your school',
        f'Start with {a("an assembly", "assemblies.html", "link")}, a single component or the full model. Wherever you begin, we can help you take actionable steps toward a safer, more supportive school.',
        'dsc01134', 'SafeBAE youth leaders in SafeBAE shirts', sticker='Created by and for young people', ask=REQ,
        extra=btn('Shop educational products', PODIA, 'ghost', 'sm'))

    js = r'''<script>(function(){
  /* the 360 dial: the ring turns so the chosen component faces its detail */
  var dial = document.querySelector('.s3-dial'); if(!dial) return;
  function all(s){ return Array.prototype.slice.call(dial.querySelectorAll(s)); }
  var ring = dial.querySelector('.ring'), segs = all('.seg'), tabs = all('[data-pick]'), panels = all('.s3-comp'),
      hub = dial.querySelector('[data-hub]'), strip = dial.querySelector('.s3-dial__tabs');
  var names = tabs.map(function(b){ return b.getAttribute('data-name'); });
  var mq = window.matchMedia ? window.matchMedia('(max-width:860px)') : {matches: false};
  var cur = 0, rot = 0, idle = hub.textContent, live = false;
  segs.forEach(function(s){ var ang = (-60 + 60 * +s.getAttribute('data-seg')) * Math.PI / 180;
    s.style.setProperty('--tx', (13 * Math.cos(ang)).toFixed(2) + 'px'); s.style.setProperty('--ty', (13 * Math.sin(ang)).toFixed(2) + 'px'); });
  function target(n){ return (mq.matches ? 90 : 0) - (-60 + 60 * n); }
  function turn(n){ var d = ((target(n) - rot) % 360 + 540) % 360 - 180; rot += d; ring.style.setProperty('--rot', rot + 'deg'); }
  function seg(n){ return segs.filter(function(s){ return +s.getAttribute('data-seg') === n; })[0]; }
  function pick(n){
    n = (n + 6) % 6; cur = n;
    panels.forEach(function(p, i){ p.classList.toggle('on', i === n); p.setAttribute('aria-hidden', String(i !== n)); });
    segs.forEach(function(s){ var on = +s.getAttribute('data-seg') === n; s.classList.toggle('on', on); s.setAttribute('aria-pressed', String(on)); });
    tabs.forEach(function(b, i){ b.setAttribute('aria-pressed', String(i === n)); });
    dial.style.setProperty('--c', tabs[n].style.getPropertyValue('--c'));
    if(live) turn(n);
    if(strip.scrollWidth > strip.clientWidth + 4){ var b = tabs[n]; try{ strip.scrollTo({left: b.offsetLeft - (strip.clientWidth - b.offsetWidth) / 2, behavior: live ? 'smooth' : 'auto'}); }catch(e){ strip.scrollLeft = b.offsetLeft; } }
  }
  function preview(n){ var on = n !== null && n !== cur; hub.textContent = on ? names[n] : idle; hub.classList.toggle('is-pre', on); segs.forEach(function(s){ s.classList.toggle('hot', on && +s.getAttribute('data-seg') === n); }); }
  segs.forEach(function(s){ var n = +s.getAttribute('data-seg');
    s.addEventListener('click', function(){ pick(n); preview(null); });
    s.addEventListener('keydown', function(e){
      if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); pick(n); preview(null); }
      else if(e.key === 'ArrowRight' || e.key === 'ArrowDown'){ e.preventDefault(); pick(cur + 1); seg(cur).focus(); }
      else if(e.key === 'ArrowLeft' || e.key === 'ArrowUp'){ e.preventDefault(); pick(cur - 1); seg(cur).focus(); }
    });
    s.addEventListener('mouseenter', function(){ preview(n); }); s.addEventListener('mouseleave', function(){ preview(null); });
    s.addEventListener('focus', function(){ preview(n); }); s.addEventListener('blur', function(){ preview(null); });
  });
  tabs.forEach(function(b, i){
    b.addEventListener('click', function(){ pick(i); preview(null); });
    b.addEventListener('mouseenter', function(){ preview(i); }); b.addEventListener('mouseleave', function(){ preview(null); });
  });
  all('[data-step]').forEach(function(b){ b.addEventListener('click', function(){ pick(cur + (+b.getAttribute('data-step'))); }); });
  function fromHash(){ var m = /^#component-([1-6])$/.exec(location.hash), n = m ? +m[1] : (location.hash === '#rees' ? 5 : 0); if(!n) return false; pick(n - 1); return true; }
  var hashed = fromHash(); if(!hashed) pick(0);
  function reveal(){ (mq.matches ? dial.querySelector('.s3-dial__detail') : dial).scrollIntoView({block: 'start'}); }
  window.addEventListener('hashchange', function(){ if(fromHash()) reveal(); });
  /* first view: the ring turns into place once */
  rot = target(cur) - 150; ring.style.setProperty('--rot', rot + 'deg');
  function go(){ if(live) return; live = true; turn(cur); }
  if('IntersectionObserver' in window && !hashed){
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ io.disconnect(); go(); } }); }, {threshold: .3});
    io.observe(dial.querySelector('.s3-dial__stage'));
  } else { go(); }
  function relay(){ if(live) turn(cur); }
  if(mq.addEventListener) mq.addEventListener('change', relay); else if(mq.addListener) mq.addListener(relay);
})();
(function(){
  /* pilot numbers count up and their meters fill the first time each set is seen */
  var groups = Array.prototype.slice.call(document.querySelectorAll('.s3-stats')); if(!groups.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function run(g){
    if(g.classList.contains('in')) return; g.classList.add('in'); if(reduce || !window.requestAnimationFrame) return;
    Array.prototype.forEach.call(g.querySelectorAll('[data-n]'), function(el){
      var to = +el.getAttribute('data-n'), dec = +el.getAttribute('data-d') || 0, t0 = null;
      function step(t){ if(t0 === null) t0 = t; var k = Math.min(1, (t - t0) / 1000), e = 1 - Math.pow(1 - k, 3); el.textContent = (to * e).toFixed(dec) + '%'; if(k < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    });
  }
  if(!('IntersectionObserver' in window)){ groups.forEach(run); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ io.unobserve(e.target); run(e.target); } }); }, {threshold: .2});
  groups.forEach(function(g){ io.observe(g); });
})();</script>'''
    page('360-schools.html', '360° Schools · SafeBAE',
         'SafeBAE 360 is a whole-school approach to preventing sexual and dating violence, with six components that put youth in the lead on lasting culture change.',
         body, active='programs', body_class='s3 s3-360', head_extra=f'<style>{CSS}{CLOSE_CSS}</style>', scripts=js)


def build():
    p360()


if __name__ == '__main__':
    build()
