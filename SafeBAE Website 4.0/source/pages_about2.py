"""ABOUT group, part 2: partners-press.html and contact.html (about, team, impact and credits live in pages_about.py; #ForDaisy in pages_daisy.py)."""
from lib import *
from data import PODCASTS

PAPER = 'https://www.tandfonline.com/doi/full/10.1080/10538712.2024.2385468'


def pod(eid):
    return next(p for p in PODCASTS if p[0] == eid)


V2_CSS = """
main .eyebrow{color:var(--logo-teal)}
.v2-dark{position:relative; overflow:hidden; background-image:var(--grain)}
.v2-dark .eyebrow{color:var(--mint)}
.v2-dark .mk{background:none; color:var(--mint)}
.v2-dark > .wrap{position:relative; z-index:1}
"""


def css(*parts):
    return '<style>' + V2_CSS + ''.join(parts) + '</style>'


ARROW_NE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8.5 7H17v8.5"/></svg>'
ARROW_E = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_S = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'

# =====================================================================
# PARTNERS & PRESS
# =====================================================================
PP_CSS = '''
/* ---------- hero: 7/5, the collage beside the copy, the press strip as its floor ---------- */
.pp-hero{background-color:var(--slate-deep); color:#fff; --wm-o:.16}
.pp-hero .wm-daisy{right:-14%; bottom:-46%}
.pp-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(30px,3.6vw,44px)}
.pp-hero__grid{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); column-gap:var(--gap); align-items:center}
.pp-hero__grid > .rise{grid-column:span 7; min-width:0; padding-right:clamp(0px,2.4vw,34px)}
.pp-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.pp-hero .lede{max-width:none; color:rgba(255,255,255,.9)}
.pp-stack{grid-column:span 5; position:relative; aspect-ratio:1.18; min-width:0; animation:sb-rise-r 1s .1s var(--ease) both}
.pp-stack > *{position:absolute; display:block; overflow:hidden; box-shadow:0 26px 50px -24px rgba(0,0,0,.75); transition:transform .5s var(--ease)}
.pp-stack img{width:100%; height:100%; object-fit:cover}
.pp-stack__film{right:0; top:2%; width:82%; aspect-ratio:16/9; border-radius:var(--r-xl); transform:rotate(2.5deg)}
.pp-stack__c{width:37%; aspect-ratio:1; border-radius:14px; border:4px solid var(--slate-deep)}
.pp-stack__c:nth-of-type(2){left:0; bottom:4%; transform:rotate(-9deg)}
.pp-stack__c:nth-of-type(3){left:28%; bottom:0; transform:rotate(-1deg); z-index:2}
.pp-stack__c:nth-of-type(4){left:57%; bottom:6%; transform:rotate(8deg)}
.pp-stack:hover .pp-stack__c:nth-of-type(2){transform:rotate(-14deg) translate(-12px,-6px)}
.pp-stack:hover .pp-stack__c:nth-of-type(4){transform:rotate(13deg) translate(14px,-8px)}
.pp-stack:hover .pp-stack__film{transform:rotate(4deg) translateY(-8px)}
.pp-stack .sticker{position:absolute; left:6%; top:6%; overflow:visible; box-shadow:3px 3px 0 var(--slate); z-index:3}
.pp-strip{display:flex; flex-wrap:wrap; align-items:center; gap:10px clamp(22px,3.4vw,46px); margin-top:clamp(30px,3.6vw,48px); padding-top:22px; border-top:1px solid var(--line-dark)}
.pp-strip > span{font-family:var(--mono); font-size:.74rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.pp-strip a{display:flex; align-items:center; height:52px; opacity:.88; transition:opacity .2s, transform .2s var(--ease)}
.pp-strip a:hover{opacity:1; transform:translateY(-2px)}
.pp-strip img{height:var(--h); width:auto; filter:brightness(0) invert(1)}
@media (max-width:900px){
  .pp-hero__grid > .rise{grid-column:1/-1; padding-right:0}
  .pp-stack{grid-column:1/-1; grid-row:1; width:min(100%,460px); margin-bottom:26px}
}
@media (max-width:520px){ .pp-strip{gap:4px 24px} .pp-strip > span{flex:0 0 100%} .pp-strip a{height:46px} .pp-strip img{height:calc(var(--h) * .84)} }

/* ---------- press: one lead story and four clippings on the same anatomy ---------- */
.pp-press{display:grid; grid-template-columns:5fr 3.5fr 3.5fr; grid-auto-rows:1fr; gap:var(--gap)}
.pp-pr{display:flex; flex-direction:column; gap:16px; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); color:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.pp-pr:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft); border-color:rgba(29,65,78,.3)}
.pp-pr__top{display:flex; align-items:center; justify-content:space-between; gap:14px; height:46px}
.pp-pr__logo{display:flex; align-items:center; min-width:0; height:100%}
.pp-pr__logo img{height:var(--h); width:auto; max-width:100%; object-fit:contain; object-position:left center}
.pp-pr__go{flex:none; width:42px; height:42px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); transition:background .2s, transform .25s var(--ease)}
.pp-pr__go svg{width:17px; height:17px}
.pp-pr:hover .pp-pr__go{background:var(--mint); color:var(--slate); transform:translate(2px,-2px)}
.pp-pr h3{margin:0; font-size:clamp(1.2rem,1.55vw,1.4rem); line-height:1.16; color:var(--logo-teal); text-wrap:balance}
.pp-pr small{margin-top:auto; padding-top:4px; font-family:var(--mono); font-size:.74rem; line-height:1.5; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--ink-soft)}
.pp-pr--lead{grid-row:span 2; gap:20px; background-color:var(--slate); background-image:var(--grain); border-color:transparent; color:#fff; padding:clamp(24px,3vw,40px)}
.pp-pr--lead .pp-pr__top{height:64px}
.pp-pr--lead .pp-pr__logo img{filter:brightness(0) invert(1)}
.pp-pr--lead .pp-pr__go{width:50px; height:50px; background:var(--mint); color:var(--slate)}
.pp-pr--lead .pp-pr__go svg{width:20px; height:20px}
.pp-pr--lead h3{margin-block:auto; color:#fff; font-size:clamp(1.9rem,3.15vw,2.78rem); line-height:1.05; font-stretch:112%; letter-spacing:-.015em}
.pp-pr--lead small{margin-top:0; color:var(--mint); font-size:.8rem}
@media (max-width:1100px){
  .pp-press{grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:auto}
  .pp-pr--lead{grid-column:1/-1; grid-row:auto}
  .pp-pr--lead h3{margin-block:6px 10px}
}
@media (max-width:620px){ .pp-press{grid-template-columns:minmax(0,1fr)} }

/* ---------- podcasts: a now-playing deck beside the queue (the page's signature) ---------- */
.pp-listen{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.pp-deck{grid-column:1 / span 7; grid-row:1; min-width:0}
.pp-queue{grid-column:8 / span 5; grid-row:1; min-width:0; display:grid; grid-auto-rows:1fr; gap:10px}
.pp-q{display:grid; grid-template-columns:68px minmax(0,1fr) 40px; gap:14px; align-items:center; min-width:0; padding:10px 14px 10px 10px; border-radius:16px; background:rgba(255,255,255,.055); border:1px solid var(--line-dark); color:#fff; font:inherit; text-align:left; cursor:pointer; transition:background .2s, border-color .2s, transform .2s var(--ease)}
.pp-q:hover{background:rgba(255,255,255,.1); border-color:rgba(209,254,255,.42); transform:translateX(-3px)}
.pp-q img{width:68px; height:68px; border-radius:10px; object-fit:cover; background:var(--slate-deep)}
.pp-q small{display:block; margin-bottom:4px; font-family:var(--mono); font-size:.7rem; line-height:1.35; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.pp-q b{display:block; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.04rem; line-height:1.2}
.pp-q__ic{width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.12); color:#fff; transition:background .2s, color .2s}
.pp-q__ic svg{width:15px; height:15px; margin-left:2px}
.pp-q__ic .pp-eq{display:none}
.pp-q[aria-selected="true"]{background:var(--mint); border-color:var(--mint); color:var(--slate); transform:none}
.pp-q[aria-selected="true"] small{color:var(--slate)}
.pp-q[aria-selected="true"] .pp-q__ic{background:var(--slate); color:var(--mint)}
.pp-q[aria-selected="true"] .pp-q__ic svg, .pp-q[data-live] .pp-q__ic svg{display:none}
.pp-q[aria-selected="true"] .pp-eq, .pp-q[data-live] .pp-eq{display:flex}
.pp-q[data-live]:not([aria-selected="true"]) .pp-q__ic{background:var(--mint); color:var(--slate)}
.pp-eq{align-items:flex-end; gap:3px; height:16px}
.pp-eq i{width:3px; border-radius:2px; background:currentColor; height:100%; transform-origin:bottom; transform:scaleY(.55)}
.pp-eq i:nth-child(2){transform:scaleY(1)} .pp-eq i:nth-child(3){transform:scaleY(.4)} .pp-eq i:nth-child(4){transform:scaleY(.8)}
.pp-q[aria-selected="true"] .pp-eq i{animation:pp-eq .7s ease-in-out 3 alternate}
.pp-q[aria-selected="true"] .pp-eq i:nth-child(2){animation-delay:.12s} .pp-q[aria-selected="true"] .pp-eq i:nth-child(3){animation-delay:.24s} .pp-q[aria-selected="true"] .pp-eq i:nth-child(4){animation-delay:.36s}
@keyframes pp-eq{50%{transform:scaleY(.25)}}
.pp-ep{display:flex; flex-direction:column; gap:clamp(16px,1.8vw,22px); min-width:0; height:100%; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; color:var(--slate); box-shadow:var(--shadow-soft)}
.pp-ep :focus-visible{outline-color:var(--teal)}
.pp-ep[hidden]{display:flex!important}
.js .pp-deck{display:grid}
.js .pp-ep{grid-area:1/1}
.js .pp-ep[hidden]{visibility:hidden}
.js .pp-ep:not([hidden]) > *{animation:pp-in .5s var(--ease) both}
.js .pp-ep:not([hidden]) > *:nth-child(2){animation-delay:.05s} .js .pp-ep:not([hidden]) > *:nth-child(3){animation-delay:.1s}
@keyframes pp-in{from{transform:translateY(10px)}}
html:not(.js) .pp-ep + .pp-ep{margin-top:var(--gap)}
.pp-ep__top{display:grid; grid-template-columns:clamp(128px,15.5vw,208px) minmax(0,1fr); gap:clamp(16px,2vw,28px); align-items:center}
.pp-ep__cover{aspect-ratio:1; border-radius:14px; overflow:hidden; background:var(--mist); box-shadow:0 20px 36px -20px rgba(22,53,64,.7)}
.pp-ep__cover img{width:100%; height:100%; object-fit:cover}
.pp-ep__show{display:block; font-family:var(--mono); font-size:.76rem; line-height:1.4; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--teal)}
.pp-ep h3{margin:.4em 0 .55em; font-size:clamp(1.42rem,2.25vw,1.95rem); line-height:1.08; color:var(--logo-teal)}
.pp-ep__links{display:flex; flex-wrap:wrap; gap:6px 20px; font-weight:700; font-size:.98rem}
.pp-deck .pp-ep a:not(.btn){color:var(--logo-teal)}
.pp-ep__links a{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
.pp-ep__links a:hover{text-decoration-color:var(--teal)}
.pp-ep__desc{margin-block:auto; font-size:1rem; line-height:1.62; color:var(--slate)}
.pp-deck .pp-ep a.pp-ep__play:not(.btn){color:#fff}
.pp-ep__play{display:grid; grid-template-columns:auto minmax(0,1fr) auto; align-items:center; gap:16px; min-height:76px; padding:12px 20px 12px 14px; border-radius:16px; background-color:var(--slate); background-image:var(--grain); text-decoration:none; transition:transform .2s var(--ease), box-shadow .2s var(--ease)}
.pp-ep__play:hover{transform:translateY(-2px); box-shadow:0 14px 26px -16px rgba(22,53,64,.8)}
.pp-ep__dot{width:50px; height:50px; border-radius:50%; display:grid; place-items:center; background:var(--mint); color:var(--slate); transition:transform .2s var(--ease)}
.pp-ep__dot svg{width:18px; height:18px; margin-left:3px}
.pp-ep__play:hover .pp-ep__dot{transform:scale(1.08)}
.pp-ep__play b{display:block; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.08rem; line-height:1.2}
.pp-ep__play small{display:block; margin-top:2px; font-size:.875rem; color:var(--aqua)}
.pp-wave{width:clamp(90px,14vw,190px); height:34px; color:var(--mint); opacity:.7}
@media (max-width:1100px){ .pp-deck{grid-column:1 / span 6} .pp-queue{grid-column:7 / span 6} }
@media (max-width:900px){
  .pp-deck,.pp-queue{grid-column:1/-1; grid-row:auto}
  .js .pp-deck{display:block}
  .js .pp-ep[hidden]{display:none!important}
  .pp-ep{height:auto}
  .pp-queue{grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:auto}
  .pp-q:hover{transform:none}
}
@media (max-width:620px){
  .pp-queue{grid-template-columns:minmax(0,1fr); gap:8px}
  .pp-q{grid-template-columns:54px minmax(0,1fr) 36px; gap:12px; padding:8px 12px 8px 8px}
  .pp-q img{width:54px; height:54px}
  .pp-q__ic{width:36px; height:36px}
  .pp-ep__top{grid-template-columns:104px minmax(0,1fr); align-items:start}
  .pp-ep__play{grid-template-columns:auto minmax(0,1fr)}
  .pp-wave{display:none}
}

/* ---------- Torrey: copy 5, video over the gift 7 ---------- */
.pp-torrey{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.pp-torrey__txt{grid-column:span 5; min-width:0; display:flex; flex-direction:column; padding-right:clamp(0px,1.6vw,22px)}
.pp-torrey__txt h2{font-size:clamp(1.9rem,3.3vw,2.9rem)}
.pp-torrey__txt p{font-size:1.02rem}
.pp-torrey__txt .btns{margin-top:auto; padding-top:12px}
.pp-torrey__media{grid-column:span 7; min-width:0; display:flex; flex-direction:column; gap:var(--gap)}
.pp-torrey__media .vid{border-radius:var(--r-xl); flex:none}
.pp-money{flex:1 1 auto; container-type:inline-size; display:flex; flex-direction:column; justify-content:center; gap:clamp(8px,1vw,14px); padding:clamp(20px,2.4vw,30px) var(--pad-card); border-radius:var(--r-xl); background-color:var(--slate); background-image:var(--grain); color:#fff}
.pp-money b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2.6rem,18.4cqi,7.2rem); line-height:.86; letter-spacing:-.03em; color:var(--mint); font-variant-numeric:tabular-nums; white-space:nowrap}
.pp-money span{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.05rem,3.75cqi,1.42rem); line-height:1.2}
@media (max-width:1100px){
  .pp-torrey__txt,.pp-torrey__media{grid-column:1/-1}
  .pp-torrey__txt{padding-right:0}
  .pp-torrey__ps{columns:2; column-gap:var(--gap)}
  .pp-torrey__ps p{break-inside:avoid}
  .pp-torrey__txt .btns{padding-top:18px}
  .pp-torrey__media{display:grid; grid-template-columns:7fr 5fr; align-items:stretch}
  .pp-money b{font-size:clamp(2.6rem,19cqi,5.4rem)}
  .pp-money span{font-size:clamp(1.1rem,6.4cqi,1.5rem)}
}
@media (max-width:700px){
  .pp-torrey__ps{columns:1}
  .pp-torrey__media{grid-template-columns:minmax(0,1fr)}
  .pp-money b{font-size:clamp(2.4rem,18.6cqi,5.4rem)}
  .pp-money span{font-size:clamp(1.05rem,5cqi,1.4rem)}
}

/* ---------- partner films: three tiles over a feature that shares their column lines ---------- */
.pp-films{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.pp-film{min-width:0; display:flex; flex-direction:column}
.pp-film .vid, .pp-film__link{border-radius:var(--r-xl)}
.pp-film .vid__label{display:none}
.pp-film .vid__play span{width:66px; height:66px}
.pp-film .vid__play svg{width:24px; height:24px}
.pp-film__link{position:relative; display:block; aspect-ratio:16/9; overflow:hidden; box-shadow:0 26px 60px -30px rgba(0,0,0,.6)}
.pp-film__link img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.pp-film__link:hover img{transform:scale(1.03)}
.pp-film__link span{position:absolute; left:14px; bottom:14px; display:inline-flex; align-items:center; gap:8px; min-height:44px; padding:8px 16px; border-radius:999px; background:var(--mint); color:var(--slate); font-family:var(--display); font-weight:800; font-size:.98rem; box-shadow:0 10px 30px rgba(0,0,0,.45), 0 0 0 6px rgba(21,255,200,.18); transition:transform .2s var(--ease)}
.pp-film__link:hover span{transform:scale(1.06)}
.pp-film__link span svg{width:15px; height:15px}
.pp-film__cap{display:flex; align-items:baseline; justify-content:space-between; gap:14px; margin-top:16px}
.pp-film h3{margin:0; font-size:1.34rem; color:#fff}
.pp-film small{flex:none; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.pp-disf{display:grid; grid-template-columns:calc((100% - 2 * var(--gap)) / 3 * 2 + var(--gap)) minmax(0,1fr); margin-top:var(--gap); border-radius:var(--r-xl); overflow:hidden; background:#0b2027; border:1px solid var(--line-dark)}
.pp-disf__img{position:relative; display:block; min-height:100%; background:#000}
.pp-disf__img img{display:block; width:100%; aspect-ratio:16/9; object-fit:cover}
.pp-disf__body{min-width:0; display:flex; flex-direction:column; padding:clamp(22px,2vw,28px)}
.pp-disf__body .eyebrow{margin-bottom:.7rem}
.pp-disf__body h3{font-size:clamp(1.9rem,2.9vw,2.6rem); font-stretch:120%; font-weight:900; text-transform:uppercase; letter-spacing:-.015em; margin:0 0 .45em}
.pp-disf__body p{font-size:.95rem; line-height:1.52; color:rgba(255,255,255,.9)}
.pp-disf__body .btns{margin-top:auto; padding-top:10px}
@media (max-width:1180px){
  .pp-disf{grid-template-columns:minmax(0,1fr)}
  .pp-disf__txt{columns:2; column-gap:var(--gap)}
  .pp-disf__txt p{break-inside:avoid}
  .pp-disf__body .btns{padding-top:18px}
}
@media (max-width:700px){ .pp-films{grid-template-columns:minmax(0,1fr)} }
@media (max-width:620px){ .pp-disf__txt{columns:1} }
@media (min-width:701px) and (max-width:1000px){ .pp-film__cap{flex-direction:column; gap:4px} .pp-film h3{font-size:1.2rem} }

/* ---------- professionals: copy 7, photo 5, then the collaborator wall ---------- */
.pp-pro{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.pp-pro__txt{grid-column:span 7; min-width:0; display:flex; flex-direction:column; padding-right:clamp(0px,2vw,28px)}
.pp-pro__txt .lede{margin-bottom:.8em}
.pp-pro__txt .btns{margin-top:auto; padding-top:14px}
.pp-pro__img{grid-column:span 5; min-height:320px}
.pp-pro__img > img{object-position:60% 42%}
.pp-wall{margin-top:clamp(36px,4.4vw,60px)}
.pp-wall__h{display:flex; align-items:center; gap:18px; margin:0 0 18px}
.pp-wall__h .eyebrow{margin:0; flex:none}
.pp-wall__h::after{content:""; flex:1; height:1px; background:var(--line)}
.pp-logos{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff}
.pp-logo{margin:0; min-width:0; display:grid; grid-template-rows:112px auto; justify-items:center; gap:12px; padding:26px 18px 20px; border-right:1px solid var(--line); border-bottom:1px solid var(--line); transition:background .25s}
.pp-logo:nth-child(4n){border-right:0}
.pp-logo:nth-last-child(-n+4){border-bottom:0}
.pp-logo:hover{background:var(--mist)}
.pp-logo__mark{display:grid; place-items:center; width:100%; height:100%}
.pp-logo img{width:var(--w); max-width:100%; height:auto; max-height:112px; object-fit:contain; filter:grayscale(1) contrast(1.08); opacity:.84; transition:filter .3s, opacity .3s, transform .3s var(--ease)}
.pp-logo:hover img{filter:none; opacity:1; transform:scale(1.04)}
.pp-logo:nth-child(7) img{filter:grayscale(1) contrast(1.5) brightness(.82)}
.pp-logo:nth-child(7):hover img{filter:none}
.pp-logo span:last-child{min-height:2.7em; font-size:.9rem; font-weight:600; line-height:1.35; color:var(--ink-soft); text-align:center; text-wrap:balance}
.pp-news{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:20px clamp(24px,4vw,56px); align-items:center; margin-top:var(--gap); padding:clamp(24px,3.2vw,42px); border-radius:var(--r-xl); background-color:var(--slate); background-image:var(--grain); color:#fff; scroll-margin-top:120px}
.pp-news .eyebrow{color:var(--mint)}
.pp-news h2{font-size:clamp(1.6rem,2.7vw,2.3rem); margin:0 0 .4em}
.pp-news .lede{margin:0; color:rgba(255,255,255,.9)}
.pp-news__note{margin:10px 0 0; font-size:.9rem; color:rgba(255,255,255,.76)}
.pp-news .btns{flex-direction:column; align-items:stretch; gap:12px}
.pp-news .btn--ghost:hover{background:rgba(255,255,255,.1)}
.pp-news :focus-visible{outline-color:var(--mint)}
@media (max-width:760px){ .pp-news{grid-template-columns:minmax(0,1fr)} .pp-news .btns{flex-direction:row; flex-wrap:wrap; align-items:center} }
@media (max-width:900px){
  .pp-pro__txt,.pp-pro__img{grid-column:1/-1}
  .pp-pro__txt{padding-right:0}
  .pp-pro__img{aspect-ratio:16/9; min-height:0}
}
@media (max-width:760px){
  .pp-logos{grid-template-columns:repeat(2,minmax(0,1fr))}
  .pp-logo{grid-template-rows:92px auto; padding:20px 12px 16px}
  .pp-logo img{width:calc(var(--w) * .82); max-height:92px}
  .pp-logo:nth-child(4n){border-right:1px solid var(--line)}
  .pp-logo:nth-child(2n){border-right:0}
  .pp-logo:nth-last-child(-n+4){border-bottom:1px solid var(--line)}
  .pp-logo:nth-last-child(-n+2){border-bottom:0}
}
#press,#podcasts,#torrey,#films,#professionals{scroll-margin-top:76px}
'''

PP_JS = '''<script>(function(){
  var d = document, reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* the gift counts up once when it comes into view */
  var m = d.querySelector('[data-pp-count]');
  if(m && 'IntersectionObserver' in window && !reduce){
    var end = parseInt(m.getAttribute('data-pp-count'), 10), io = new IntersectionObserver(function(es){
      if(!es[0].isIntersecting) return;
      io.disconnect();
      var t0 = null;
      function step(t){ if(t0 === null) t0 = t; var p = Math.min(1, (t - t0) / 1100), e = 1 - Math.pow(1 - p, 3); m.firstChild.nodeValue = '$' + Math.round(end * e).toLocaleString('en-US'); if(p < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    }, {threshold:.6});
    io.observe(m);
  }
  /* podcast queue: mark the episode whose player is open, and keep the deck in view on small screens */
  var wrap = d.querySelector('.pp-listen');
  if(!wrap) return;
  var deck = wrap.querySelector('.pp-deck');
  deck.addEventListener('click', function(e){
    var a = e.target.closest('[data-spotify]');
    if(!a || !(window.SB && window.SB.canEmbed)) return;
    var p = a.closest('.pp-ep'), t = p && d.getElementById('tab-' + p.id);
    if(t) t.setAttribute('data-live', '');
  }, true);
  var tabs = Array.prototype.slice.call(wrap.querySelectorAll('[role="tab"]'));
  tabs.forEach(function(t, i){
    t.addEventListener('keydown', function(e){
      var n = e.key === 'ArrowDown' ? 1 : e.key === 'ArrowUp' ? -1 : 0;
      if(!n) return;
      e.preventDefault();
      var x = tabs[(i + n + tabs.length) % tabs.length]; x.click(); x.focus();
    });
    t.addEventListener('click', function(){
      if(window.innerWidth > 900) return;
      var r = deck.getBoundingClientRect();
      if(r.top > window.innerHeight * .55 || r.top < 0) window.scrollTo({top: window.pageYOffset + r.top - 96, behavior: reduce ? 'auto' : 'smooth'});
    });
  });
})();</script>'''


def pp_wave():
    hs = [10, 18, 26, 14, 30, 22, 12, 28, 34, 20, 14, 26, 32, 18, 10, 22, 30, 16, 24, 12, 28, 20, 14, 8]
    bars = ''.join(f'<rect x="{i * 8}" y="{(34 - h) / 2:.0f}" width="4" height="{h}" rx="2"/>' for i, h in enumerate(hs))
    return f'<svg class="pp-wave" viewBox="0 0 {len(hs) * 8 - 4} 34" preserveAspectRatio="xMaxYMid slice" fill="currentColor" aria-hidden="true">{bars}</svg>'


EQ = '<span class="pp-eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>'


def partners():
    # logo slug, outlet, headline, label, link, logo height in the clipping, logo height in the hero strip
    press = [
        ('the-guardian-logo-vector', 'The Guardian', 'Young people want to know whether they’ve perpetrated a sexual assault.', 'Read in The Guardian', 'https://www.theguardian.com/us-news/2026/may/06/sexual-consent-assault-online-tool', 112, 62),
        ('vox-logo-svg-1', 'Vox', 'Teen boys are using ChatGPT as their wingman. What could go wrong?', 'Read on Vox', 'https://www.vox.com/technology/481444/ai-chatgpt-teen-boys-teenagers-dating-relationships', 36, 32),
        ('trendwatching-logo', 'TrendWatching', 'When teens worry they crossed a boundary, Vibe Check helps them.', 'Read on TrendWatching', 'https://www.trendwatching.com/innovations/when-teens-worry-they-may-have-crossed-a-boundary-vibe-check-helps-them-think-it-through', 56, 52),
        ('pp-nyt-logo', 'The New York Times', 'Our Kids Cannot Learn About Sex Just From Squeamish Gym Teachers', 'Hillary Frank, New York Times Opinion', 'https://www.nytimes.com/2025/01/26/opinion/sex-education-consent-middle-school.html', 27, 27),
        ('pp-nyt-logo', 'The New York Times', 'The Most Important Lesson in Sex Ed Isn’t Actually Sex', 'New York Times Opinion podcast', 'https://www.nytimes.com/2025/02/27/opinion/sex-education-consent.html', 27, 27),
    ]
    press_html = ''.join(
        f'<a class="pp-pr{" pp-pr--lead" if k == 0 else ""}" href="{u}" target="_blank" rel="noopener">'
        f'<span class="pp-pr__top"><span class="pp-pr__logo" style="--h:{h}px">{img(im, outlet)}</span><span class="pp-pr__go" aria-hidden="true">{ARROW_NE}</span></span>'
        f'<h3>{esc(hd)}</h3><small>{esc(sub)}</small></a>'
        for k, (im, outlet, hd, sub, u, h, _hs) in enumerate(press))
    strip = ''.join(f'<a href="#press" style="--h:{hs}px" aria-label="{esc(outlet)}: see the coverage">{img(im, outlet, loading="eager")}</a>'
                    for im, outlet, _hd, _sub, _u, _h, hs in press[:4])

    episodes = [
        ('0v2G7MraWG1V2iyXgGKOUF', 'SafeBAE on The Longest Shortest Time', 'Preventing Teens from Joining the Manosphere',
         'SafeBAE returned to The Longest Shortest Time for a conversation with Hillary Frank about Vibe Check, SafeBAE’s free, anonymous reflection tool for young people who are worried they, or a friend, may have crossed a boundary or caused harm. Drew Davis, SafeBAE’s Director of Strategic Initiatives, talks about what happens when teens bring sensitive questions to Reddit, AI tools, or online spaces that can reinforce shame, denial, misogyny, or defensiveness, and how Vibe Check offers a different path toward reflection, accountability, and repair.',
         [('Episode page', 'https://longestshortesttime.com/episode-255-preventing-teens-from-joining-the-manosphere'), ('Vibe Check', 'vibe-check.html')]),
        ('042UsrG0aMabkTo66WQQWc', 'The She Matters Podcast', 'Centering Youth Voices: Youth-Led Prevention and Addressing Harm',
         'SafeBAE Founding Executive Director Shael Norris on youth-led sexual violence prevention, SafeBAE’s founding story, and what it means to meaningfully center young people in this work, including SafeBAE’s school-based prevention model, Certified Peer Educator Training, and Vibe Check.',
         [('Episode page', 'https://www.shematters.ca/podcasts/the-she-matters-podcast/episodes/2149218219'), ('Peer Educator Training', 'peer-educator.html')]),
        ('4jjztQt08zjUR9guFgJ56x', 'Shaping the national conversation', 'How to Not (Accidentally) Raise a Rapist',
         'The first episode of the relaunch of Hillary Frank’s parenting and culture podcast reframes one of her most downloaded episodes, <a href="https://longestshortesttime.com/episode-116-how-to-not-accidentally-raise-a-racist/" target="_blank" rel="noopener"><i>How to Not (Accidentally) Raise a Racist</i></a>, to spark dialogue about raising young people who respect boundaries and safety. Featuring Shael Norris, it explores what works when talking to teens about consent and how schools and parents can build a consent-conscious culture.',
         [('NYT Opinion piece', 'https://www.nytimes.com/2025/01/26/opinion/sex-education-consent-middle-school.html'), ('NYT podcast', 'https://www.nytimes.com/2025/02/27/opinion/sex-education-consent.html')]),
        ('0JfMJbj7ZvISm8m7gp39YS', 'The Measure of Everyday Life', 'Reducing Tolerance for Sexual Assault',
         'With host Dr. Brian Southwell, SafeBAE discussed the findings of our published research paper and announced the launch of CheckYourVibe.org, a free, anonymous reflection tool for young people who are questioning whether they may have caused harm.',
         [('The research', PAPER), ('Our data', 'impact.html')]),
        ('3ZUV9feb4NeuvydAQWdiao', 'The Totally Preventable Podcast', 'Blurred Lines, Parts 1 & 2',
         'A two-part conversation on the intersection of alcohol, drugs, and sexual assault with experts from RAINN, DanceSafe, Day One, and more. The podcast highlights local voices and prevention leaders working on behavioral health and social issues across Newport County, with insight, resources, and practical ways to support safer, healthier communities.',
         [('Listen to Part 2', 'https://open.spotify.com/episode/2itdYviCeALsZdo6SC64k8'), ('About the podcast', 'https://strategicprevention.org/totally-preventable/')]),
        ('5PzGRtkgUIBtCjVqhgstq7', 'Hosted by Freya Graf', 'Sexual Violence Prevention in Schools with SafeBAE',
         'A candid conversation about building authentic, youth-driven prevention and meeting young people where they are, and how partnering with students creates systemic change in school environments and fosters cultures of consent.',
         [('360° Schools', '360-schools.html')]),
    ]
    for eid, *_r in episodes:
        pod(eid)  # every episode here is also in the Library
    queue, deck = '', ''
    for k, (eid, show, title, desc, links) in enumerate(episodes):
        cov = 'sp640-' + eid.lower()
        pid = f'ep-{k + 1}'
        on = k == 0
        queue += (f'<button class="pp-q" type="button" role="tab" id="tab-{pid}" aria-controls="{pid}" aria-selected="{"true" if on else "false"}"{"" if on else " tabindex=\"-1\""}>'
                  f'{img(cov, "")}<span><small>{esc(show)}</small><b>{esc(title)}</b></span>'
                  f'<span class="pp-q__ic" aria-hidden="true">{ICON_PLAY}{EQ}</span></button>')
        lk = ''.join(a(esc(t) + (' &#8599;' if u.startswith('http') else ' &rarr;'), u) for t, u in links)
        deck += f'''<article class="pp-ep" role="tabpanel" id="{pid}" aria-labelledby="tab-{pid}"{"" if on else " hidden"}>
  <div class="pp-ep__top">
    <div class="pp-ep__cover">{img(cov, f"Cover art: {show}")}</div>
    <div><span class="pp-ep__show">{esc(show)}</span><h3>{esc(title)}</h3><div class="pp-ep__links">{lk}</div></div>
  </div>
  <p class="pp-ep__desc">{desc}</p>
  <a class="pp-ep__play" href="https://open.spotify.com/episode/{eid}" target="_blank" rel="noopener" data-spotify="episode/{eid}" aria-label="Listen: {esc(title)}"><span class="pp-ep__dot">{ICON_PLAY}</span><span><b>Play the episode</b><small>Opens the Spotify player</small></span>{pp_wave()}</a>
</article>'''

    films = [
        ('Share', 'FaiaD8wRNV8', 'share-hbo-1920x1080', 127, 'Partner film'),
        ('Raising Voices (Ni una más)', '3ku4DRWdsBI', 'raising-1920x1080', None, 'Partner film'),
    ]
    film_html = ''.join(f'<div class="pp-film">{yt(v, t, thumb=th, label="Watch", start=s)}<div class="pp-film__cap"><h3>{esc(t)}</h3><small>{esc(k)}</small></div></div>' for t, v, th, s, k in films)
    film_html += (f'<div class="pp-film"><a class="pp-film__link" href="https://www.lionsgate.com/movies/millers-girl" target="_blank" rel="noopener">'
                  f'{img("lionsgate-1920x1080", "Miller’s Girl resources page on Lionsgate, listing SafeBAE among partner organizations")}<span>Lionsgate{ARROW_NE}</span></a>'
                  f'<div class="pp-film__cap"><h3>Miller’s Girl</h3><small>Partner film</small></div></div>')

    # logo slug, name, rendered width (px) chosen so every mark carries about the same visual weight
    logos = [('ridoh-logo', 'Rhode Island Department of Health', 108), ('untitled-design-2023-07-29t212654-858-1920w', 'Illinois Coalition Against Sexual Assault (ICASA)', 164),
             ('logo-mahperd', 'MAHPERD', 138), ('pp-owl-mark', 'OWL Taking Flight', 68),
             ('nova-logo', 'NOVA', 180), ('blue-and-orange-logo-transparent-background', 'SIECUS: Sex Ed for Social Change', 178),
             ('sml-logo-tag-long', 'Share My Lesson', 222), ('vrlc-logo-final-rgb-for-posters-white-on-blue', 'Victim Rights Law Center', 56)]
    logo_html = ''.join(f'<li class="pp-logo" style="--w:{w}px"><span class="pp-logo__mark">{img(im, "")}</span><span>{esc(n)}</span></li>' for im, n, w in logos)

    body = f'''
<section class="pp-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="pp-hero__grid">
      <div class="rise">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Partners &amp; Press</span></nav>
        <h1>Partners &amp; <span class="mk">press</span></h1>
        <p class="lede">SafeBAE’s work is made possible by the partnerships we’ve built with schools, researchers, funders, creatives, and youth-serving organizations across the country. We’re proud to collaborate with those who share our commitment to ending sexual violence, amplifying youth leadership, and shifting culture through education, art, media, and policy.</p>
        <div class="btns">{btn('Request a program', 'request-a-program.html', 'mint', arrow=True)}{btn('Press contacts', 'contact.html#press', 'ghost')}</div>
      </div>
      <div class="pp-stack" aria-hidden="true">
        <span class="pp-stack__film">{img('disfluency-1920x1080', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp640-0v2g7mrawg1v2iyxggkouf', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp640-042usrg0amabkto66wqqwc', '', loading='eager')}</span>
        <span class="pp-stack__c">{img('sp640-0jfmjbj7zvism8m7gp39ys', '', loading='eager')}</span>
        <span class="sticker">On the air</span>
      </div>
    </div>
    <div class="pp-strip"><span>Featured in</span>{strip}</div>
  </div>
</section>

<section class="band band--paper" id="press">
  <div class="wrap">
    <div class="section-head"><div><h2>SafeBAE and Vibe Check in the press</h2></div><div class="section-head__act">{btn('About Vibe Check', 'vibe-check.html', 'slate', arrow=True)}</div></div>
    <div class="pp-press reveal">{press_html}</div>
  </div>
</section>

<section class="band band--slate" id="podcasts">
  <div class="wrap">
    <div class="section-head"><div><h2>Podcast features</h2></div><div class="section-head__act">{btn('All episodes in the Library', 'library.html#podcasts', 'mint', arrow=True)}</div></div>
    <div class="pp-listen reveal" data-tabs>
      <div class="pp-queue" role="tablist" aria-label="Podcast episodes featuring SafeBAE">{queue}</div>
      <div class="pp-deck">{deck}</div>
    </div>
  </div>
</section>

<section class="band band--mint" id="torrey">
  <div class="wrap pp-torrey">
    <div class="pp-torrey__txt">
      <p class="eyebrow">Streaming now</p>
      <h2>Torrey DeVitto on <i>Celebrity Name That Tune</i></h2>
      <div class="pp-torrey__ps"><p>Longtime SafeBAE partner and Board Member Torrey DeVitto competed on <i>Celebrity Name That Tune</i> (Season 5, Episode 12) on FOX and chose SafeBAE as the beneficiary of her winnings. Torrey donated $29,000 to support youth-led sexual violence prevention, bringing SafeBAE’s mission to a national television audience.</p>
      <p>Her win reflects an ongoing commitment to our work and shows what trusted advocates can do when they use their platforms to invest directly in prevention, care, and youth leadership. We’re deeply grateful to Torrey for continuing to show up for SafeBAE, both publicly and behind the scenes.</p></div>
      <div class="btns">{btn('Meet our board', 'team.html#board', 'slate', arrow=True)}</div>
    </div>
    <div class="pp-torrey__media reveal">
      {yt('XFQeOEDbN4M', 'Torrey DeVitto on Celebrity Name That Tune', label='FOX')}
      <div class="pp-money"><b data-pp-count="29000">$29,000</b><span>donated to youth-led sexual violence prevention</span></div>
    </div>
  </div>
</section>

<section class="band band--deep" id="films">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Media collaborations &amp; partner films</p><h2>Stories that center survivors</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">SafeBAE believes in the power of media and storytelling to advance prevention and end sexual assault and dating violence. We’re proud to collaborate on films and creative projects that center survivors and shift culture.</p></div></div>
    <div class="pp-films reveal">{film_html}</div>
    <div class="pp-disf reveal">
      <a class="pp-disf__img" href="https://www.disfluencymovie.com/" target="_blank" rel="noopener">{img('disfluency-1920x1080', 'Disfluency, the award-winning feature film, in partnership with SafeBAE')}</a>
      <div class="pp-disf__body">
        <p class="eyebrow">Feature film partner</p>
        <h3>Disfluency</h3>
        <div class="pp-disf__txt">
          <p><i>Disfluency</i> is an award-winning feature film written and directed by {a('Anna Baumgarten', 'https://www.annabaumgarten.com/', 'link')} that offers a survivor-centered portrayal of the aftermath of sexual assault, focusing on trauma, memory, and recovery without depicting the assault itself.</p>
          <p>SafeBAE partnered with the filmmakers to support the film’s educational impact, collaborating on school-based screenings and prevention and discussion resources for secondary and higher-education settings.</p>
        </div>
        <div class="btns">{btn('Visit the film’s site', 'https://www.disfluencymovie.com/', 'mint')}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="professionals">
  <div class="wrap">
    <div class="pp-pro">
      <div class="pp-pro__txt">
        <p class="eyebrow">Training &amp; education for professionals</p>
        <h2>We train the adults around young people, too</h2>
        <p class="lede">SafeBAE’s commitment to prevention extends beyond students. We regularly work with educators, legal advocates, service providers, parents, caregivers, and community leaders to share our youth-led model and equip adults to support survivors and embed prevention into everyday practice.</p>
        <p class="muted">Through keynote presentations, workshops, and national webinars, we provide concrete strategies for engaging youth as leaders, building consent-conscious environments, and sustaining systemic change.</p>
        <div class="btns">{btn('Faculty & staff training', 'professional-development.html', 'slate', arrow=True)}{btn('Request a program', 'request-a-program.html', 'ghost')}</div>
      </div>
      <div class="pp-pro__img fill-img reveal">{img('assembly-whiteboard', 'A woman writing the word “Respect” on a classroom whiteboard')}</div>
    </div>
    <div class="pp-wall">
      <div class="pp-wall__h"><p class="eyebrow">Selected collaborators</p></div>
      <ul class="pp-logos reveal">{logo_html}</ul>
    </div>
    <div class="pp-news" id="news">
      <div><h2>Read stories from survivors and updates from SafeBAE</h2>
        <p class="lede lede--full">Stay updated with SafeBAE, and share what you learn with your friends.</p>
        <p class="pp-news__note">Material posted may contain sensitive language. Reader discretion is advised.</p></div>
      <div class="btns">{btn('Read the blog', 'blog.html', 'mint', arrow=True)}{btn('Subscribe on Substack', 'https://substack.com/@safebae', 'ghost')}</div>
    </div>
  </div>
</section>
{give_band()}
'''
    page('partners-press.html', 'Partners & Press · SafeBAE', 'SafeBAE’s partnerships, press coverage, podcast features and partner films highlighting youth-led sexual violence prevention.',
         body, active='about', body_class='pg-partners', head_extra=css(PP_CSS), scripts=PP_JS)


# =====================================================================
# CONTACT
# =====================================================================
CT_CSS = '''
/* ---------- hero: copy 7, the postcard 5 ---------- */
.ct-hero{background:var(--teal); color:#fff; position:relative; overflow:hidden; --wm-o:.22}
.ct-hero .wm-daisy{color:var(--aqua); right:-16%; bottom:-52%}
.ct-hero .wrap{position:relative; z-index:1; padding-block:clamp(40px,5vw,72px) clamp(92px,9vw,132px); display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); column-gap:var(--gap); align-items:center}
.ct-hero .rise{grid-column:span 7; min-width:0; padding-right:clamp(0px,2.4vw,34px)}
.ct-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.ct-hero .mk{background:none; color:var(--aqua)}
.ct-hero .crumbs,.ct-hero .crumbs a{color:#fff}
.ct-hero .lede{color:#fff; max-width:none}
.ct-hero .btns{margin-top:6px}
.ct-hero :focus-visible{outline-color:#fff}
.ct-comp{grid-column:span 5; min-width:0; position:relative; padding:0 0 13% 9%; animation:sb-rise-r 1s .1s var(--ease) both}
.ct-comp > img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:50% 40%; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.55)}
.ct-post{position:absolute; left:0; bottom:0; width:min(404px,93%); background:#fff; color:var(--slate); border-radius:16px; padding:18px 20px 16px; transform:rotate(-3deg); box-shadow:0 26px 50px -22px rgba(0,0,0,.55); background-image:repeating-linear-gradient(90deg, transparent 0 calc(63% - 1px), var(--line) calc(63% - 1px) 63%, transparent 63% 100%); transition:transform .4s var(--ease)}
.ct-comp:hover .ct-post{transform:rotate(-1.5deg) translateY(-4px)}
.ct-post__to{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:0 0 6px}
.ct-post address{font-style:normal; font-family:var(--display); font-weight:800; font-stretch:104%; font-size:1.04rem; line-height:1.3; max-width:58%}
.ct-post .copy{margin-top:12px; font-size:.875rem}
.ct-stamp{position:absolute; right:16px; top:14px; width:58px; height:68px; background:var(--mint); border-radius:4px; display:grid; place-items:center; outline:3px dashed #fff; outline-offset:-6px}
.ct-stamp .daisy{width:36px; height:36px; color:var(--slate)}
.ct-postmark{position:absolute; right:46px; top:52px; width:104px; height:104px; border-radius:50%; border:2px solid rgba(29,65,78,.5); display:grid; place-items:center; text-align:center; font-family:var(--mono); font-size:.7rem; line-height:1.25; letter-spacing:.04em; text-transform:uppercase; color:rgba(29,65,78,.82); transform:rotate(14deg); font-weight:600; padding:10px}
@media (max-width:900px){
  .ct-hero .rise{grid-column:1/-1; padding-right:0}
  .ct-comp{grid-column:1/-1; grid-row:1; width:min(100%,520px); margin-bottom:30px}
}
@media (max-width:480px){.ct-postmark{display:none} .ct-post{width:92%; background-image:none} .ct-post address{max-width:70%}}

/* ---------- help first: a coral card that straddles the hero's floor ---------- */
.ct-help{position:relative; z-index:2; display:grid; grid-template-columns:auto minmax(0,1fr) auto; align-items:center; gap:14px clamp(20px,2.8vw,40px); margin-top:calc(-1 * clamp(46px,4.6vw,62px) - var(--band)); margin-bottom:clamp(40px,5vw,68px); padding:clamp(18px,2vw,24px) var(--pad-card); border-radius:var(--r-xl); background:var(--coral); color:var(--slate); box-shadow:0 26px 50px -30px rgba(22,53,64,.8)}
.ct-help__h small{display:block; margin-bottom:4px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600}
.ct-help h2{margin:0; font-size:clamp(1.5rem,2.2vw,1.9rem); font-stretch:114%; font-weight:900; white-space:nowrap}
.ct-help p{margin:0; font-size:1rem; line-height:1.45; font-weight:500}
.ct-help__nums{display:flex; flex-wrap:wrap; gap:2px 26px; margin-top:6px; font-weight:600; font-size:1.04rem; line-height:1.4}
.ct-help__nums span{white-space:nowrap}
.ct-help__btn{display:inline-flex; align-items:center; gap:.55em; min-height:48px; padding:.65em 1.15em; border:0; border-radius:10px; background:var(--slate); color:#fff; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1rem; line-height:1.1; white-space:nowrap; cursor:pointer; box-shadow:0 4px 0 rgba(0,0,0,.22); transition:transform .18s ease, box-shadow .18s ease}
.ct-help__btn:hover{transform:translateY(-2px); box-shadow:0 6px 0 rgba(0,0,0,.22)}
.ct-help__btn svg{width:16px; height:16px; transition:transform .18s ease}
.ct-help__btn:hover svg{transform:translateX(3px)}
.ct-help :focus-visible{outline-color:var(--slate)}
@media (max-width:1000px){ .ct-help{grid-template-columns:auto minmax(0,1fr)} .ct-help__btn{grid-column:2; justify-self:start} }
@media (max-width:700px){ .ct-help{grid-template-columns:minmax(0,1fr); gap:10px} .ct-help h2{white-space:normal} .ct-help__btn{grid-column:auto; margin-top:4px} }

/* ---------- route picker (the page's signature): routes 5, the answer and the form 7 ---------- */
.ct-pick{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ct-pick__nav{grid-column:span 5; min-width:0; display:flex; flex-direction:column; gap:10px}
.ct-pick__nav h2{margin:0 0 calc(var(--head-gap) - 10px)}
.ct-pick__panel{grid-column:span 7; min-width:0; display:flex; flex-direction:column; padding:clamp(22px,2.6vw,34px); border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); box-shadow:var(--shadow-soft); scroll-margin-top:110px}
.ct-tabs{flex:4 1 auto; display:grid; grid-auto-rows:1fr; gap:10px}
.ct-pick__nav > .ct-tab{flex:1 1 auto}
.ct-tab{display:grid; grid-template-columns:minmax(0,1fr) 40px; grid-template-rows:auto auto; align-content:center; align-items:center; gap:3px 16px; width:100%; min-height:102px; padding:13px 16px 13px 20px; border-radius:16px; background:#fff; border:1px solid var(--line); color:var(--slate); font:inherit; text-align:left; text-decoration:none; cursor:pointer; transition:background .2s, border-color .2s, color .2s, transform .2s var(--ease), box-shadow .2s var(--ease)}
.ct-tab:hover{border-color:var(--teal); transform:translateX(3px)}
.ct-tab b{grid-column:1; display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.22rem; line-height:1.15; color:var(--logo-teal)}
.ct-tab small{grid-column:1; display:block; font-size:.95rem; line-height:1.35; color:var(--ink-soft)}
.ct-tab i{grid-column:2; grid-row:1 / span 2; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; transition:background .2s, color .2s, transform .25s var(--ease)}
.ct-tab i svg{width:17px; height:17px}
.ct-tab:hover i{background:var(--mint); color:var(--slate)}
.ct-tab[aria-selected="true"]{background-color:var(--slate); background-image:var(--grain); border-color:var(--slate); color:#fff; transform:none; box-shadow:var(--shadow-soft)}
.ct-tab[aria-selected="true"] b{color:#fff}
.ct-tab[aria-selected="true"] small{color:rgba(255,255,255,.84)}
.ct-tab[aria-selected="true"] i{background:var(--mint); color:var(--slate)}
.ct-tab--jump{border-style:dashed; border-color:rgba(29,65,78,.34); background:transparent}
.ct-d h3{margin:0 0 .4em; font-size:1.5rem; color:var(--logo-teal)}
.ct-d p{margin:0 0 14px; font-size:1rem; line-height:1.55; color:var(--slate)}
.ct-d__row{display:flex; flex-wrap:wrap; align-items:flex-end; gap:12px 16px}
.ct-d .copy{font-size:.94rem; background:#fff; padding:7px 7px 7px 12px; border-radius:8px}
.ct-d .copy button{min-height:30px; padding:4px 10px; font-size:.78rem; border-radius:6px}
.ct-who{display:flex; flex-direction:column; align-items:flex-start; gap:5px}
.ct-who small{font-weight:700; font-size:.9rem; line-height:1.3}
.ct-d .link{font-size:.98rem; white-space:nowrap; min-height:44px; display:inline-flex; align-items:center}
.ct-d--press{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:0 clamp(18px,2.4vw,30px); align-items:start}
.ct-d--press[hidden]{display:none}
.ct-d--press h3{grid-column:1/-1}
.ct-d--press .ct-d__row{flex-direction:column; align-items:flex-start; gap:10px}
@media (max-width:1200px){ .ct-d--press{grid-template-columns:minmax(0,1fr)} .ct-d--press .ct-d__row{flex-direction:row; align-items:flex-end; gap:12px 18px; margin-top:14px} }
html:not(.js) .ct-pick .ct-d[hidden]{display:block!important; margin-top:22px}
.ct-d:not([hidden]){animation:ct-in .45s var(--ease) both}
@keyframes ct-in{from{transform:translateY(8px)}}
.ct-form{flex:1 1 auto; display:flex; flex-direction:column; margin-top:clamp(18px,2.2vw,26px); padding-top:clamp(18px,2.2vw,26px); border-top:1px solid var(--line)}
.ct-form__h{display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:6px 16px; margin-bottom:14px}
.ct-form__h h3{margin:0; font-size:1.5rem; color:var(--logo-teal)}
.ct-form__h p{margin:0; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--ink-soft)}
.ct-form__h p b{color:var(--logo-teal); font-weight:600}
.ct-form .form{flex:1 1 auto; display:flex; flex-direction:column}
.ct-form .ct-grow{flex:1 1 auto; display:flex; flex-direction:column}
.ct-form .ct-grow textarea{flex:1 1 auto; min-height:120px}
.ct-form__foot{display:flex; flex-wrap:wrap; align-items:center; gap:10px 18px}
.ct-form__foot .form__note{margin:0; flex:1 1 240px}
.ct-two{display:grid; grid-template-columns:1fr 1fr; gap:14px}
.pg-contact .copy a{color:inherit; text-decoration:none}
.pg-contact .copy a:hover{text-decoration:underline; text-decoration-color:var(--teal); text-decoration-thickness:2px; text-underline-offset:3px}
@media (max-width:520px){.ct-two{grid-template-columns:1fr}}
@media (pointer:coarse){ .pg-contact .copy button{min-height:44px; padding-inline:12px} }
@media (max-width:900px){
  .ct-pick{grid-template-columns:minmax(0,1fr)}
  .ct-pick__nav{display:contents}
  .ct-pick__nav h2{order:1; margin:0}
  .ct-tabs{order:2; grid-template-columns:repeat(2,minmax(0,1fr)); margin-top:calc(-1 * var(--gap) + 18px)}
  .ct-pick__panel{order:3; grid-column:auto}
  .ct-pick__nav > .ct-tab{order:4}
  .ct-tab:hover{transform:none}
}
@media (max-width:560px){
  .ct-tabs .ct-tab{min-height:64px; padding:10px 12px 10px 14px; grid-template-columns:minmax(0,1fr) 30px; gap:2px 8px}
  .ct-tabs .ct-tab small{display:none}
  .ct-tabs .ct-tab b{font-size:1.04rem}
  .ct-tabs .ct-tab i{width:30px; height:30px; grid-row:1}
  .ct-tabs .ct-tab i svg{width:14px; height:14px}
}

/* ---------- program request: mirrors the picker (copy 5, form 7) ---------- */
.ct-req{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.ct-req__txt{grid-column:span 5; min-width:0; display:flex; flex-direction:column; padding-right:clamp(0px,1.6vw,22px)}
.ct-req__txt h2{font-size:clamp(1.9rem,3.4vw,3rem)}
.ct-req__txt .btns{margin-top:auto}
.ct-req .form{grid-column:span 7; min-width:0; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:clamp(20px,2.6vw,30px); display:flex; flex-direction:column}
.ct-req .form .ct-grow{flex:1 1 auto; display:flex; flex-direction:column}
.ct-req .form .ct-grow textarea{flex:1 1 auto; min-height:120px}
.ct-req label{color:#fff}
.ct-req .field input,.ct-req .field textarea{border-color:transparent}
.ct-req .form__note{color:rgba(255,255,255,.76)}
.ct-offer{display:flex; flex-wrap:wrap; gap:8px; margin:4px 0 26px; padding:0; list-style:none}
.ct-offer li{margin:0; padding:8px 14px; border-radius:999px; background:rgba(21,255,200,.12); border:1px solid rgba(21,255,200,.4); color:var(--aqua); font-weight:700; font-size:.95rem}
@media (max-width:900px){ .ct-req__txt,.ct-req .form{grid-column:1/-1} .ct-req__txt{padding-right:0} }

/* ---------- address, social, newsletter: three peers on one anatomy ---------- */
.ct-info{grid-template-columns:repeat(3,minmax(0,1fr))}
.ct-info > div{background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); gap:10px}
.ct-info h3{font-size:1.3rem; margin:0; color:var(--logo-teal)}
.ct-info address{font-style:normal; font-weight:600; line-height:1.5; font-size:1.02rem}
.ct-info p{margin:0; font-size:.98rem; line-height:1.5; color:var(--ink-soft)}
.ct-info__floor{padding-top:10px; display:flex; flex-wrap:wrap; gap:7px; align-items:center; min-height:56px}
.ct-info__floor .btn--sm{min-height:44px}
.ct-info .copy{background:#fff; font-size:.9rem; padding:7px 7px 7px 12px; border-radius:8px}
.ct-info .copy button{min-height:30px; padding:4px 10px; font-size:.78rem; border-radius:6px}
.ct-soc{display:flex; flex-wrap:wrap; gap:7px}
.ct-soc a{width:44px; height:44px; border-radius:50%; display:grid; place-items:center; background:#fff; border:1px solid var(--line); color:var(--logo-teal); transition:background .2s, color .2s, border-color .2s, transform .2s var(--ease)}
.ct-soc a:hover{background:var(--slate); color:var(--mint); border-color:var(--slate); transform:translateY(-3px)}
.ct-soc svg{width:19px; height:19px}
@media (max-width:860px){.ct-info{grid-template-columns:minmax(0,1fr)}}
#request{scroll-margin-top:76px}
'''

CT_JS = '''<script>(function(){
  var d = document, wrap = d.querySelector('.ct-pick');
  if(!wrap) return;
  var form = wrap.querySelector('form'), msg = d.getElementById('ct-msg'), about = wrap.querySelector('[data-ct-about]'), panel = wrap.querySelector('.ct-pick__panel');
  var R = {
    general: ['Message from safebae.org', ''],
    press: ['Press inquiry from safebae.org', 'Your outlet, topic, and deadline'],
    partnerships: ['Partnership inquiry from safebae.org', 'A short description of your organization and what you have in mind'],
    clubs: ['Club support question from safebae.org', 'Your questions, challenges or event ideas']
  };
  function sync(){
    var t = wrap.querySelector('[role="tab"][aria-selected="true"]');
    if(!t) return;
    var r = R[t.getAttribute('aria-controls')];
    if(!r) return;
    form.setAttribute('data-subject', r[0]);
    msg.placeholder = r[1];
    if(about) about.textContent = t.querySelector('b').textContent;
  }
  if('MutationObserver' in window) new MutationObserver(sync).observe(wrap.querySelector('[role="tablist"]'), {attributes:true, subtree:true, attributeFilter:['aria-selected']});
  sync();
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tabs = Array.prototype.slice.call(wrap.querySelectorAll('[role="tab"]'));
  tabs.forEach(function(t, i){
    t.addEventListener('keydown', function(e){
      var n = e.key === 'ArrowDown' ? 1 : e.key === 'ArrowUp' ? -1 : 0;
      if(!n) return;
      e.preventDefault();
      var x = tabs[(i + n + tabs.length) % tabs.length]; x.click(); x.focus();
    });
    t.addEventListener('click', function(){
      if(window.innerWidth > 900) return;
      var r = panel.getBoundingClientRect();
      if(r.top > window.innerHeight * .6 || r.top < 0) window.scrollTo({top: window.pageYOffset + r.top - 96, behavior: reduce ? 'auto' : 'smooth'});
    });
  });
})();</script>'''


def copy_email(e):
    return f'<span class="copy"><a href="mailto:{esc(e)}">{esc(e)}</a><button type="button" data-copy="{esc(e)}" aria-label="Copy {esc(e)}">Copy</button></span>'


def contact():
    routes = [
        ('general', 'General inquiries', 'We respond within 2 to 3 business days'),
        ('press', 'Press &amp; media', 'Send your outlet, topic and deadline'),
        ('partnerships', 'Partnerships', 'Schools, districts, nonprofits, brands, and funders'),
        ('clubs', 'Club support', 'For students and faculty advisors'),
    ]
    tabs = ''.join(
        f'<button class="ct-tab" type="button" role="tab" id="tab-{k}" aria-controls="{k}" aria-selected="{"true" if n == 0 else "false"}"{"" if n == 0 else " tabindex=\"-1\""}>'
        f'<b>{t}</b><small>{s}</small><i aria-hidden="true">{ARROW_E}</i></button>'
        for n, (k, t, s) in enumerate(routes))
    soc_names = ['Instagram', 'TikTok', 'LinkedIn', 'YouTube', 'Facebook']
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="SafeBAE on {n}" title="{n}">{svg}</a>'
                  for want in soc_names for n, u, svg in SOCIAL if n == want)

    body = f'''
<section class="ct-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Contact</span></nav>
      <h1><span class="mk">Contact</span> us</h1>
      <p class="lede">We respond to general inquiries within 2 to 3 business days. Journalists on deadline can reach our leadership directly.</p>
      <div class="btns">{btn('Write to the team', '#message', 'white', arrow=True)}{btn('Press contacts', '#press', 'ghost')}</div>
    </div>
    <div class="ct-comp">
      {img('img-6834', 'A group of SafeBAE youth leaders smiling together outdoors', loading='eager')}
      <div class="ct-post">
        <p class="ct-post__to">Write to</p>
        <address>SafeBAE<br>7 Evelyn Drive<br>Bristol, RI 02809</address>
        {copy_email('info@safebae.org')}
        <span class="ct-stamp" aria-hidden="true">{daisy()}</span>
        <span class="ct-postmark" aria-hidden="true">Replies in 2–3 business days</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--paper" id="reach">
  <div class="wrap">
    <div class="ct-help">
      <div class="ct-help__h"><small>Free &amp; confidential</small><h2>Need help now?</h2></div>
      <div class="ct-help__txt"><p>Hotlines for survivors, friends and anyone in crisis, most open 24/7. If you are in danger, call 911.</p>
        <div class="ct-help__nums"><span>Text <strong>LOVEIS</strong> to 22522</span><span>Call <strong>800-656-HOPE</strong> (4673)</span></div></div>
      <button class="ct-help__btn" type="button" data-open-help>Open support resources{ARROW_E}</button>
    </div>
    <div class="ct-pick" data-tabs>
      <div class="ct-pick__nav">
        <h2>Reach the right person</h2>
        <div class="ct-tabs" role="tablist" aria-label="What you are writing about">{tabs}</div>
        <a class="ct-tab ct-tab--jump" href="#request"><b>Bring SafeBAE to your school</b><small>Student presentations, staff trainings, parent nights and club chapter support</small><i aria-hidden="true">{ARROW_S}</i></a>
      </div>
      <div class="ct-pick__panel" id="message">
        <div class="ct-d" role="tabpanel" id="general" aria-labelledby="tab-general"><h3>General inquiries</h3><p>Email us or use the message form. We respond within 2 to 3 business days.</p><div class="ct-d__row">{copy_email('info@safebae.org')}</div></div>
        <div class="ct-d ct-d--press" role="tabpanel" id="press" aria-labelledby="tab-press" hidden><h3>Press &amp; media</h3>
          <div><p>Email info@safebae.org with your outlet, topic, and deadline, or use the form. If you are on deadline, you can reach our leadership directly.</p>{copy_email('info@safebae.org')}</div>
          <div class="ct-d__row"><div class="ct-who"><small>Shael Norris, Executive Director</small>{copy_email('shael@safebae.org')}</div><div class="ct-who"><small>Drew Davis, Director of Strategic Initiatives</small>{copy_email('drew@safebae.org')}</div></div></div>
        <div class="ct-d" role="tabpanel" id="partnerships" aria-labelledby="tab-partnerships" hidden><h3>Partnerships</h3><p>We partner with schools, districts, nonprofits, brands, and funders. Email us a short description of your organization and what you have in mind.</p><div class="ct-d__row">{copy_email('info@safebae.org')}</div></div>
        <div class="ct-d" role="tabpanel" id="clubs" aria-labelledby="tab-clubs" hidden><h3>Club support</h3><p>Questions about starting, registering or running a SafeBAE club, or the Club Hub. Students and faculty advisors can email clubsupport@safebae.org with questions, challenges or event ideas. You can also book a virtual meeting with our programming team.</p>
          <div class="ct-d__row">{copy_email('clubsupport@safebae.org')}<a class="link" href="https://calendly.com/clubsupport-safebae/30min" target="_blank" rel="noopener">Book a meeting &#8599;</a></div></div>
        <div class="ct-form">
          <div class="ct-form__h"><h3>Send us a message</h3><p>About: <b data-ct-about>General inquiries</b></p></div>
          <form class="form" data-static data-mailto="info@safebae.org" data-subject="Message from safebae.org">
            <div class="ct-two"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="Name" autocomplete="name" required></div>
            <div class="field"><label for="ct-email">Email address</label><input id="ct-email" name="Email" type="email" autocomplete="email" required></div></div>
            <div class="field ct-grow"><label for="ct-msg">Message</label><textarea id="ct-msg" name="Message" required></textarea></div>
            <div class="ct-form__foot"><button class="btn btn--slate" type="submit">Send message</button><p class="form__note">Messages sent here reach the same team as info@safebae.org.</p></div>
            <p class="form__done" role="status">Thank you. Your message is on its way to the SafeBAE team.</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate" id="request">
  <div class="wrap ct-req">
    <div class="ct-req__txt">
      <h2>Bring SafeBAE to your school or community</h2>
      <p class="lede" style="color:rgba(255,255,255,.9)">Want SafeBAE at your school or in your community? Fill out the form to tell us what you’d like to book or learn more about.</p>
      <ul class="ct-offer"><li>Student presentations</li><li>Staff trainings</li><li>Parent nights</li><li>Club chapter support</li></ul>
      <div class="btns">{btn('See programs & pricing', 'request-a-program.html', 'mint', arrow=True)}{btn('How 360° Schools works', '360-schools.html', 'ghost')}</div>
    </div>
    <form class="form" data-static data-mailto="info@safebae.org" data-subject="Program request from safebae.org">
      <div class="ct-two"><div class="field"><label for="rq-name">Name</label><input id="rq-name" name="Name" autocomplete="name" required></div>
      <div class="field"><label for="rq-org">School or organization</label><input id="rq-org" name="School or organization" autocomplete="organization" required></div></div>
      <div class="ct-two"><div class="field"><label for="rq-email">Email address</label><input id="rq-email" name="Email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="rq-phone">Cell phone</label><input id="rq-phone" name="Cell phone" type="tel" autocomplete="tel"></div></div>
      <div class="field ct-grow"><label for="rq-msg">What are you hoping to book or learn more about?</label><textarea id="rq-msg" name="Request" placeholder="Share what you’re hoping to book or learn more about…" required></textarea></div>
      <div><button class="btn btn--mint" type="submit">Submit request</button></div>
      <p class="form__done" role="status">Thank you. Our team will be in touch about your request.</p>
    </form>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap level ct-info">
    <div><h3>Mailing address</h3><address>SafeBAE<br>7 Evelyn Drive, <span style="white-space:nowrap">Bristol, RI 02809</span></address><p>A registered <span style="white-space:nowrap">501(c)(3)</span> nonprofit.</p>
      <div class="ct-info__floor"><span class="copy">EIN 81-5451147<button type="button" data-copy="81-5451147" aria-label="Copy the EIN, 81-5451147">Copy</button></span></div></div>
    <div><h3>Follow us</h3><p>New resources, campaigns, and youth organizing updates.</p>
      <div class="ct-info__floor ct-soc">{soc}</div></div>
    <div><h3>Newsletter</h3><p>Stories, analysis and news from SafeBAE, in your inbox.</p>
      <div class="ct-info__floor">{btn('Subscribe on Substack', 'https://substack.com/@safebae', 'slate', 'sm')}</div></div>
  </div>
</section>
{give_band()}
'''
    page('contact.html', 'Contact · SafeBAE', 'Contact SafeBAE: general inquiries, press and media, partnerships, club support, and requests to bring SafeBAE to your school or community.',
         body, active='about', body_class='pg-contact', head_extra=css(CT_CSS), scripts=CT_JS)


def build():
    partners()
    contact()


if __name__ == '__main__':
    build()
