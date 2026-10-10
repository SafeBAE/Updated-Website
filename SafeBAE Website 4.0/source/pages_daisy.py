"""#ForDaisy: remembering Daisy Coleman (fordaisy.html) and Tattoos & Healing (fordaisy-tattoos.html).

The two pages share one identity: the hand-drawn line daisy the client supplied, a lighter condensed
heading voice than the rest of the site, and a quiet light hero. The daisy never spins; it blooms once."""
from lib import *
from data import PODCASTS
import json


def pod(eid):
    return next(p for p in PODCASTS if p[0] == eid)


def css(*parts):
    return '<style>' + ''.join(parts) + '</style>'


def fl(cls=''):
    """The drawn daisy. Weights: default bold line (60-160px), --line (large art), --mark (under 56px)."""
    return f'<span class="dz-fl{(" " + cls) if cls else ""}" aria-hidden="true"></span>'


# =====================================================================
# shared #ForDaisy identity (both pages)
# =====================================================================
DZ_BASE_CSS = '''
.pg-daisy{--dz-ink:#1d414e; --dz-soft:#46646e; --dz-bg:#f6fefe}
main .eyebrow{color:var(--logo-teal)}

/* the drawn daisy: line art over a mint heart */
.dz-fl{position:relative; display:block; flex:none; width:var(--fl-w,120px); aspect-ratio:1100/852; color:var(--logo-teal); pointer-events:none}
.dz-fl::before{content:""; position:absolute; left:36.4%; top:34.4%; width:25.2%; height:25.4%; border-radius:50%; background:var(--fl-heart,var(--mint)); rotate:-8deg}
.dz-fl::after{content:""; position:absolute; inset:0; background:currentColor; -webkit-mask:var(--fl-art,url(assets/img/daisy-line-bold.svg)) center/contain no-repeat; mask:var(--fl-art,url(assets/img/daisy-line-bold.svg)) center/contain no-repeat}
.dz-fl--line{--fl-art:url(assets/img/daisy-line.svg)}
.dz-fl--mark{--fl-art:url(assets/img/daisy-line-mark.svg)}
@keyframes dzBloom{from{opacity:0; transform:rotate(-10deg) scale(.86)}}
@keyframes dzOpen{from{clip-path:circle(0% at 49% 47%)} to{clip-path:circle(80% at 49% 47%)}}

/* headings: lighter and condensed, the quiet voice of these two pages */
.dz-h2{font-weight:600; font-stretch:84%}
.band--paper .dz-h2,.band--mist .dz-h2,.band--aqua .dz-h2{color:var(--logo-teal)}
.dz-mark{display:flex; align-items:center; gap:12px; font-family:var(--mono); font-size:.74rem; letter-spacing:.14em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:0 0 16px}
.dz-mark .dz-fl{--fl-w:52px}

/* light hero shared by both pages */
.dz-hero{position:relative; overflow:hidden; background:var(--dz-bg); color:var(--dz-ink); border-bottom:1px solid var(--line)}
.dz-hero__grid{position:relative; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:32px clamp(28px,5vw,72px); align-items:center; padding-block:clamp(36px,4.6vw,64px) clamp(44px,5.4vw,76px)}
.dz-hero__grid > *{min-width:0}
.dz-hero .crumbs{color:var(--dz-soft)} .dz-hero .crumbs a{color:var(--logo-teal)} .dz-hero .crumbs a:hover{color:var(--teal)}
.dz-hero h1{font-weight:500; font-stretch:78%; letter-spacing:-.025em; color:var(--logo-teal)}
.dz-hero .lede{color:var(--dz-ink); font-weight:450; font-size:clamp(1.08rem,1.36vw,1.26rem)}
.dz-hero .lede a{color:var(--logo-teal); font-weight:600; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
.dz-hero .lede a:hover{color:var(--teal)}
.dz-hero :focus-visible{outline-color:var(--teal)}
.dz-hero__art{position:absolute; z-index:0; --fl-heart:transparent; color:var(--teal); opacity:.5; animation:dzBloom 1.6s .15s var(--ease) both; transform-origin:49% 47%; --fade:linear-gradient(90deg, transparent 3%, #000 17%); -webkit-mask-image:var(--fade); mask-image:var(--fade)}
@media (max-width:1240px){.dz-hero__art{--fade:linear-gradient(90deg, transparent 11%, #000 27%)}}

@media (max-width:900px){
  .dz-hero__grid{display:flex; flex-direction:column; align-items:stretch; gap:0}
  .dz-hero__grid > .rise{display:contents}
  .dz-hero__grid > .rise > .lede{order:3}
  .dz-hero__grid > .rise > .btns{order:4}
  .dz-hero__media{order:2; align-self:center; margin:6px 0 30px}
  .dz-hero__art{-webkit-mask-image:none; mask-image:none}
}

'''

# =====================================================================
# #FORDAISY
# =====================================================================
DZ_CSS = '''
/* ---- hero ---- */
.pg-fordaisy .dz-hero h1{font-size:clamp(3.2rem,7.6vw,7.2rem); line-height:.9; margin:0 0 .22em}
.dz-dates{font-family:var(--display); font-stretch:88%; font-weight:600; font-size:clamp(1.15rem,2vw,1.55rem); letter-spacing:.01em; margin:0 0 1em; color:var(--dz-ink)}
.dz-dates span{color:var(--teal); padding:0 .35em}
.dz-portrait{position:relative; justify-self:end; width:min(100%,410px)}
.dz-portrait__frame{position:relative; z-index:1; border-radius:999px 999px var(--r-xl) var(--r-xl); overflow:hidden; aspect-ratio:5/6; background:var(--aqua); box-shadow:0 40px 80px -40px rgba(22,53,64,.55); animation:sb-rise-r 1s .1s var(--ease) both}
.dz-portrait__frame img{width:100%; height:100%; object-fit:cover; object-position:61% 30%}
.dz-portrait .dz-hero__art{width:178%; left:-37%; top:-15%}
.dz-dates b{font-weight:inherit; white-space:nowrap}
@media (max-width:900px){
  .dz-portrait{width:min(74%,340px)}
  .pg-fordaisy .dz-dates{margin-bottom:.6em}
}
@media (max-width:480px){.dz-dates b{display:block} .dz-dates span{display:none}}

/* ---- The Cut ---- */
.dz-cut{margin:0}
.dz-cut blockquote{margin:0; font-family:var(--display); font-weight:500; font-stretch:88%; font-size:clamp(1.42rem,2.75vw,2.3rem); line-height:1.2; color:#fff; text-wrap:pretty; text-indent:-.42em; padding-left:.42em}
.dz-cut blockquote b{font-weight:700; color:var(--aqua)}
.dz-cut figcaption{display:flex; flex-wrap:wrap; gap:8px 28px; align-items:center; justify-content:space-between; margin-top:clamp(18px,2.2vw,28px); padding-top:16px; border-top:1px solid var(--line-dark)}
.dz-cut figcaption span{font-family:var(--mono); font-size:.76rem; letter-spacing:.14em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.dz-cut figcaption a{color:var(--mint); font-weight:700}

/* ---- more than her advocacy ---- */
.dz-life{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap) clamp(28px,4.4vw,64px); align-items:stretch}
.dz-life__txt{display:flex; flex-direction:column; min-width:0}
.dz-life__txt p{font-size:1.08rem; line-height:1.7}
.dz-life__pics{display:grid; grid-template-columns:1fr 1fr; gap:var(--gap); min-width:0}
.dz-ph{position:relative; margin:0; min-height:340px; border-radius:var(--r-xl); overflow:hidden; background:var(--mist)}
.dz-ph img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.dz-ph figcaption{position:absolute; left:12px; bottom:12px; right:12px; width:fit-content; max-width:calc(100% - 24px); font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; font-weight:500; line-height:1.35; color:#fff; background:rgba(22,53,64,.86); padding:6px 10px; border-radius:8px}
.dz-teaser{display:grid; grid-template-columns:112px minmax(0,1fr) auto; gap:16px; align-items:center; margin-top:auto; padding:12px 16px 12px 12px; border-radius:var(--r-xl); background:var(--mist); border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.dz-teaser:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); border-color:var(--teal)}
.dz-teaser img{width:112px; height:112px; object-fit:cover; object-position:54% 12%; border-radius:14px}
.dz-teaser small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.dz-teaser b{display:block; font-family:var(--display); font-weight:700; font-stretch:88%; font-size:1.5rem; line-height:1.1; color:var(--logo-teal); margin:3px 0 4px}
.dz-teaser span span{display:block; color:var(--ink-soft); font-size:.95rem; line-height:1.4}
.dz-teaser .go{width:42px; height:42px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .2s var(--ease)}
.dz-teaser:hover .go{background:var(--mint); transform:translateX(3px)}
.dz-life__txt p:last-of-type{margin-bottom:1.5em}
@media (max-width:900px){.dz-life{grid-template-columns:1fr} .dz-ph{min-height:0; aspect-ratio:3/4}}
@media (max-width:480px){.dz-teaser{grid-template-columns:84px minmax(0,1fr)} .dz-teaser img{width:84px; height:84px} .dz-teaser .go{display:none}}

/* ---- tribute wall ---- */
.dz-wallband{position:relative; overflow:hidden}
.dz-wallband > .wrap{position:relative; z-index:1}
.dz-wallband__art{position:absolute; z-index:0; --fl-w:min(66vw,800px); --fl-heart:transparent; right:-170px; top:-300px; color:var(--mint); opacity:.22}
.dz-wallhead{display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:20px 48px; margin-bottom:clamp(20px,2.4vw,30px)}
.dz-wallhead h2{font-weight:600; font-stretch:82%; font-size:clamp(2.3rem,4.8vw,4rem); color:#fff; line-height:.95; margin:0}
.dz-wallhead .eyebrow{margin-bottom:.9rem}
.dz-count{display:flex; align-items:center; gap:14px; margin:0}
.dz-count b{font-family:var(--display); font-weight:600; font-stretch:80%; font-size:clamp(3.4rem,6vw,5rem); line-height:.82; color:var(--mint)}
.dz-count span{font-weight:600; color:#fff; line-height:1.3; max-width:15em}
.dz-wallintro{display:grid; grid-template-columns:1fr 1fr; gap:14px var(--gap); margin-bottom:var(--head-gap); padding-top:clamp(18px,2.2vw,26px); border-top:1px solid var(--line-dark)}
.dz-wallintro p{margin:0; color:rgba(255,255,255,.88); font-size:1.04rem; line-height:1.65}
@media (max-width:860px){.dz-wallintro{grid-template-columns:1fr}}

.dz-wall{columns:4 250px; column-gap:14px}
.dz-wall.is-cols{columns:auto; display:flex; align-items:flex-start; gap:14px; overflow:hidden; padding:4px; margin:-4px}
.dz-col{flex:1 1 0; min-width:0}
.dz-wall.has-more{-webkit-mask-image:linear-gradient(#000 calc(100% - 190px), transparent calc(100% - 16px)); mask-image:linear-gradient(#000 calc(100% - 190px), transparent calc(100% - 16px))}
.dz-wall.has-more.no-fade{-webkit-mask-image:none; mask-image:none}
.dz-wall.no-fade + .dz-wall__foot{margin-top:clamp(18px,2.4vw,28px)}
.dz-card{break-inside:avoid; margin:0 0 14px; background:#fff; border-radius:14px; padding:20px 20px 18px; position:relative; box-shadow:0 18px 40px -28px rgba(0,0,0,.9); transition:box-shadow .35s var(--ease), transform .35s var(--ease)}
.dz-card:hover{transform:translateY(-2px); box-shadow:0 0 0 2px var(--mint), 0 22px 40px -26px rgba(0,0,0,.9)}
.dz-card.is-long{background:var(--aqua)}
.dz-card p{margin:0; font-size:.98rem; line-height:1.6; color:var(--dz-ink); white-space:pre-line; overflow-wrap:anywhere}
.dz-card.is-long p{max-height:9.6em; overflow:hidden; -webkit-mask-image:linear-gradient(#000 58%, transparent); mask-image:linear-gradient(#000 58%, transparent)}
.dz-card.is-long.open p{max-height:none; -webkit-mask-image:none; mask-image:none}
.dz-card button{display:inline-flex; align-items:center; min-height:44px; margin:2px 0 -10px; background:none; border:0; padding:0; font:inherit; font-size:.9rem; font-weight:700; color:var(--logo-teal); cursor:pointer; text-decoration:underline; text-decoration-color:var(--teal); text-decoration-thickness:2px; text-underline-offset:3px}
.dz-card button:hover{color:var(--teal)}
.dz-card button:focus-visible,.dz-add :focus-visible{outline-color:var(--teal)}
.dz-card.is-new{animation:dzIn .7s var(--ease) both}
@keyframes dzIn{from{opacity:0; transform:translateY(12px)}}
.dz-wall__foot{position:relative; display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; justify-content:center; margin-top:clamp(18px,2.4vw,28px)}
.dz-wall.has-more + .dz-wall__foot{margin-top:-6px}
.dz-wall__foot > span{flex:0 0 100%; text-align:center; font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}

/* ---- add your message ---- */
#add,#wall{scroll-margin-top:110px}
.dz-add{position:relative; overflow:hidden; display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap) clamp(24px,4vw,56px); align-items:stretch; background:#fff; border-radius:var(--r-xl); padding:clamp(24px,3.6vw,44px); border:1px solid var(--line); box-shadow:var(--shadow-soft)}
.dz-add > *{position:relative; z-index:1; min-width:0}
.dz-add h2{font-weight:600; font-stretch:82%; color:var(--logo-teal); font-size:clamp(2rem,3.6vw,3rem)}
.dz-add__txt p{font-size:1.06rem; line-height:1.6; max-width:26em}
.dz-add > .dz-add__art{position:absolute; z-index:0; left:-64px; bottom:-190px; width:440px; aspect-ratio:1100/852}
.dz-add__art .dz-fl{position:absolute; inset:0; width:auto; --fl-art:url(assets/img/daisy-line.svg)}
.dz-add__art .dz-fl:first-child{--fl-heart:transparent; color:var(--teal); opacity:.3}
.dz-add__art .dz-fl + .dz-fl{color:var(--teal); visibility:hidden}
.dz-add.is-sent .dz-add__art .dz-fl + .dz-fl{visibility:visible; animation:dzOpen 1.5s var(--ease) both}
.dz-add.is-sent .dz-add__art .dz-fl:first-child{opacity:0; transition:opacity .9s .5s}
.dz-add .form{align-content:start}
.dz-add textarea{min-height:226px; font-size:1.02rem}
.dz-add__send{display:flex; flex-wrap:wrap; align-items:center; gap:12px 18px}
.dz-add .form__done{display:none; flex:1 1 220px; margin:0; padding:12px 16px; border-radius:10px; background:var(--aqua); font-weight:700; line-height:1.35}
.dz-add .form.sent .form__done{display:block; animation:dzIn .6s .2s var(--ease) both}
@media (max-width:860px){
  .dz-add{grid-template-columns:1fr}
  .dz-add__txt{padding-right:112px; min-height:132px}
  .dz-add__txt p{max-width:none}
  .dz-add > .dz-add__art{left:auto; bottom:auto; right:-62px; top:-44px; width:240px}
}

/* ---- remembering: statement, support, recordings and photos (one slate section) ---- */
.dz-mem .section-head .lede{color:rgba(255,255,255,.88)}
.dz-mem .dz-h2{color:#fff}
.dz-letter{background:#fff; color:var(--dz-ink); border-radius:var(--r-xl); border:1px solid var(--line); box-shadow:var(--shadow-soft); overflow:hidden}
.dz-letter summary{list-style:none; cursor:pointer; padding:clamp(16px,2vw,22px) clamp(20px,2.8vw,32px); display:grid; grid-template-columns:auto minmax(0,1fr) auto; align-items:center; gap:clamp(14px,2vw,24px); transition:background .2s}
.dz-letter summary:hover{background:var(--dz-bg)}
.dz-letter summary::-webkit-details-marker{display:none}
.dz-letter summary .dz-fl{--fl-w:84px}
.dz-letter summary b{font-family:var(--display); font-weight:600; font-stretch:86%; font-size:clamp(1.3rem,2.4vw,1.85rem); line-height:1.15; color:var(--logo-teal)}
.dz-letter summary i{font-style:normal; flex:none; width:44px; height:44px; border-radius:50%; background:var(--aqua); display:grid; place-items:center; font-size:1.4rem; line-height:1; color:var(--slate); transition:transform .3s var(--ease), background .2s}
.dz-letter[open] summary i{transform:rotate(45deg); background:var(--mint)}
.dz-letter summary:focus-visible{outline:3px solid var(--mint); outline-offset:-3px}
.dz-letter__body{padding:0 clamp(20px,2.8vw,32px) clamp(28px,4vw,52px); border-top:1px solid var(--line)}
.dz-letter__body > *{max-width:690px; margin-inline:auto}
.dz-letter__head{text-align:center; padding:clamp(26px,3.4vw,40px) 0 clamp(14px,2vw,22px)}
.dz-letter__head h3{font-family:var(--display); font-weight:600; font-stretch:80%; font-size:clamp(2rem,4vw,3rem); letter-spacing:.06em; margin:0; color:var(--slate)}
.dz-letter__body p{font-size:1.06rem; line-height:1.78; margin-bottom:1.1em}
.dz-letter__body .dz-letter__head p{font-family:var(--mono); font-size:.8rem; line-height:1.4; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin:8px 0 0}
.dz-letter__body p.dz-sign{font-family:var(--display); font-stretch:86%; font-weight:600; font-size:1.25rem; line-height:1.4; margin-bottom:0}
.dz-care{display:flex; flex-wrap:wrap; gap:12px 28px; align-items:center; justify-content:space-between; margin-top:14px; padding:16px clamp(20px,2.8vw,32px); border-radius:var(--r-xl); background:rgba(255,255,255,.06); border:1px solid var(--line-dark); color:#fff}
.dz-care p{margin:0; font-size:1.02rem; flex:1 1 420px; color:rgba(255,255,255,.9)}
.dz-care b{color:var(--mint)}
.dz-care button{font:inherit; font-weight:800; min-height:44px; background:var(--aqua); color:var(--slate); border:0; border-radius:10px; padding:9px 16px; cursor:pointer; transition:background .2s}
.dz-care button:hover{background:var(--mint)}
.dz-vids{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin-top:clamp(28px,3.4vw,44px)}
.dz-vids .vid{border-radius:var(--r-xl)}
.dz-vids .vid__label{display:none}
.dz-vids h3{font-weight:600; font-stretch:88%; font-size:1.35rem; margin:16px 0 4px; color:#fff}
.dz-vids small{display:block; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
.dz-photos{margin-top:clamp(40px,4.6vw,64px); padding-top:clamp(28px,3.2vw,40px); border-top:1px solid var(--line-dark); scroll-margin-top:110px}
.dz-photos__head{display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:8px 28px; margin-bottom:clamp(18px,2.2vw,26px)}
.dz-photos__head h3{font-family:var(--display); font-weight:600; font-stretch:84%; font-size:clamp(1.6rem,2.6vw,2.2rem); line-height:1.1; margin:0; color:#fff}
.dz-photos__head span{font-family:var(--mono); font-size:.76rem; letter-spacing:.1em; text-transform:uppercase; color:var(--aqua)}
.dz-photos__foot{display:flex; justify-content:center; margin-top:clamp(18px,2.2vw,26px)}
.dz-gal.is-short button:nth-child(n+14){display:none}
@media (max-width:860px){.dz-vids{grid-template-columns:1fr} .dz-letter summary .dz-fl{--fl-w:60px}}
@media (max-width:480px){.dz-letter summary{grid-template-columns:minmax(0,1fr) auto} .dz-letter summary .dz-fl{display:none}}

/* ---- photos ---- */
.dz-gal.gallery{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); grid-auto-rows:auto; grid-auto-flow:row dense; gap:12px}
.dz-gal.gallery button{position:relative; display:block; width:100%; height:100%; aspect-ratio:1; margin:0; border-radius:14px; background:rgba(255,255,255,.06)}
.dz-gal.gallery button.is-wide{grid-column:span 2; aspect-ratio:auto}
.dz-gal.gallery button.is-big{grid-column:span 2; grid-row:span 2; aspect-ratio:auto}
.dz-gal.gallery button img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
.dz-gal.gallery button:focus-visible{outline:3px solid var(--mint); outline-offset:3px}
.dz-gal.gallery button::after{content:""; position:absolute; inset:0; border-radius:inherit; box-shadow:inset 0 0 0 0 var(--mint); transition:box-shadow .25s var(--ease)}
.dz-gal.gallery button:hover::after{box-shadow:inset 0 0 0 3px var(--mint)}
@media (max-width:760px){.dz-gal.gallery{grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px} .dz-gal.gallery button{border-radius:10px}}

/* ---- closing: her voice (two podcasts) and the training offered in her memory ---- */
.dz-legacy{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap); align-items:stretch}
.dz-legacy__pods{display:grid; grid-template-rows:1fr 1fr; gap:var(--gap); min-width:0}
.dz-pod{display:flex; flex-direction:column; min-width:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft)}
.dz-pod .audio{border-radius:0; background:var(--slate) var(--grain); padding:16px}
.dz-pod .audio img{width:84px; height:84px; border-radius:12px}
.dz-pod .audio b{font-size:1.14rem}
.dz-pod .audio small{font-size:.88rem; line-height:1.35; display:block; margin-top:3px}
.dz-pod .audio .playdot{transition:transform .2s var(--ease)}
.dz-pod .audio:hover .playdot{transform:scale(1.08)}
.dz-pod p{flex:1; display:flex; align-items:center; margin:0; padding:16px var(--pad-card) 18px; font-size:1rem; line-height:1.6; color:var(--dz-ink)}
.dz-ded{position:relative; overflow:hidden; display:flex; flex-direction:column; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--logo-teal); color:#fff}
.dz-ded > .dz-fl{--fl-w:132px; color:var(--aqua); margin:-6px 0 14px -8px}
.dz-ded .eyebrow{color:var(--mint); margin-bottom:.5rem}
.dz-ded h3{font-weight:600; font-stretch:86%; font-size:1.6rem; line-height:1.1; margin:0 0 .4em; color:#fff}
.dz-ded p:not(.eyebrow){margin:0 0 18px; color:rgba(255,255,255,.88); font-size:1rem; line-height:1.55}
.dz-ded .btns{margin-top:auto}
@media (max-width:860px){.dz-legacy{grid-template-columns:minmax(0,1fr)} .dz-legacy__pods{grid-template-rows:none}}
'''

DZ_JS = r'''<script>(function(){
  var wall = document.getElementById('dz-wall'), more = document.getElementById('dz-more'), shown = document.getElementById('dz-shown'), data = [];
  try { data = JSON.parse(document.getElementById('dz-data').textContent); } catch(e) { data = []; }
  var narrow = window.matchMedia && window.matchMedia('(max-width: 640px)').matches;
  var STEP = narrow ? 10 : 24, LONG = 300, cards = [], cols = [], cur = 0;
  var trim = function(){};
  function wire(card){ var b = card.querySelector('button'); if(!b) return; b.addEventListener('click', function(){ var o = card.classList.toggle('open'); b.textContent = o ? 'Show less' : 'Read the full message'; b.setAttribute('aria-expanded', String(o)); trim(); }); }
  function make(t){
    var f = document.createElement('figure'); f.className = 'dz-card is-new' + (t.length > LONG ? ' is-long' : '');
    var p = document.createElement('p'); p.textContent = t; f.appendChild(p);
    if(t.length > LONG){ var b = document.createElement('button'); b.type = 'button'; b.textContent = 'Read the full message'; b.setAttribute('aria-expanded','false'); f.appendChild(b); }
    wire(f); return f;
  }
  /* columns that only ever grow: a new message goes to the shortest column, so nothing already on the wall moves */
  function count(){ var w = wall.clientWidth; return w >= 1000 ? 4 : w >= 720 ? 3 : w >= 500 ? 2 : 1; }
  function place(card){ var best = cols[0]; for(var i = 1; i < cols.length; i++){ if(cols[i].offsetHeight < best.offsetHeight - 2) best = cols[i]; } best.appendChild(card); }
  function layout(){
    var k = count(); if(k === cur) return; cur = k; cols = [];
    wall.textContent = ''; wall.classList.add('is-cols');
    for(var i = 0; i < k; i++){ var c = document.createElement('div'); c.className = 'dz-col'; wall.appendChild(c); cols.push(c); }
    cards.forEach(place);
  }
  /* while more messages remain, the wall is cut level at its shortest column and fades out */
  trim = function(){
    wall.style.maxHeight = ''; wall.classList.remove('no-fade');
    if(!wall.classList.contains('has-more') || !cols.length) return;
    var lo = Infinity, hi = 0; cols.forEach(function(c){ lo = Math.min(lo, c.offsetHeight); hi = Math.max(hi, c.offsetHeight); });
    var cut = Math.max(cols.length > 1 ? lo - 2 : hi + 8, 360), top = wall.getBoundingClientRect().top, deep = 0;
    Array.prototype.forEach.call(wall.querySelectorAll('.dz-card.open'), function(c){ deep = Math.max(deep, c.getBoundingClientRect().bottom - top); });
    /* a message someone has opened is never left under the fade */
    if(deep > cut - 200){ wall.classList.add('no-fade'); return; }
    wall.style.maxHeight = cut + 'px';
  };
  function update(){
    var done = cards.length >= data.length;
    if(shown) shown.textContent = 'Showing ' + cards.length + ' of ' + data.length + ' messages';
    if(more) more.hidden = done;
    wall.classList.toggle('has-more', !done);
    trim();
  }
  if(wall){
    cards = Array.prototype.slice.call(wall.children);
    if(narrow && cards.length > 8) cards = cards.slice(0, 8);
    cards.forEach(wire);
    layout(); update();
    var again = function(){ cur = 0; layout(); trim(); };
    if(document.fonts && document.fonts.ready) document.fonts.ready.then(again);
    window.addEventListener('load', again);
    var rt; window.addEventListener('resize', function(){ clearTimeout(rt); rt = setTimeout(function(){ layout(); trim(); }, 160); });
    if(more) more.addEventListener('click', function(){
      var end = Math.min(cards.length + STEP, data.length);
      for(var i = cards.length, k = 0; i < end; i++, k++){ var c = make(data[i]); c.style.animationDelay = Math.min(k * 30, 540) + 'ms'; cards.push(c); place(c); }
      update();
    });
  }
  /* photos: the first rows show; the rest open on request (the lightbox steps through all of them either way) */
  var gal = document.querySelector('.dz-gal'), all = document.getElementById('dz-allphotos');
  if(gal && all){ var lbl = all.textContent; all.addEventListener('click', function(){ var short = gal.classList.toggle('is-short'); all.setAttribute('aria-expanded', String(!short)); all.textContent = short ? lbl : 'Show fewer photos'; if(short){ var r = gal.getBoundingClientRect(); if(r.top < 0) window.scrollTo({top: window.pageYOffset + r.top - 140}); } }); }
  /* when someone sends a message, the drawn daisy in the panel opens once */
  var form = document.querySelector('.dz-add form'), panel = document.querySelector('.dz-add');
  if(form && panel) form.addEventListener('submit', function(){ setTimeout(function(){ if(form.classList.contains('sent')) panel.classList.add('is-sent'); }, 0); });
})();</script>'''

GALLERY_ALT = {
    1: 'Daisy smiling beside a tall window', 2: 'Daisy seated in an auditorium before a talk', 3: 'Daisy with SafeBAE team members in front of a student audience',
    4: 'Daisy smiling at a school event', 5: 'Daisy standing in a school gym during an event', 6: 'Daisy smiling and making a peace sign',
    7: 'Daisy with a group outdoors at dusk', 9: 'Daisy sitting outside against a white wall', 10: 'Daisy at a table with a cake',
    11: 'Daisy in a lecture hall', 12: 'Daisy with two others in a lecture hall', 13: 'Daisy on a bridge on a sunny day',
    14: 'Daisy laughing on a bridge on a sunny day', 15: 'Daisy in a rowboat on a lake', 16: 'Daisy smiling in a blue winter coat',
    17: 'Daisy smiling in a close-up photo with another person', 18: 'Daisy standing against a plain wall', 19: 'Daisy in a selfie under pink light',
    20: 'Daisy leaning against a tree beside a stone wall', 21: 'Daisy with two people, one wearing a SafeBAE shirt', 22: 'Daisy on set during a film shoot',
    23: 'Daisy leaning in a window frame', 24: 'Daisy with a large group of young advocates at an event', 25: 'Daisy at a tattoo studio',
    26: 'Daisy posing with a woman in a white top', 27: 'Daisy outside a comedy club at night', 28: 'Daisy tattooing a client',
    29: 'Daisy standing in a plaza lined with flags', 30: 'A selfie of Daisy and two others in a plaza lined with flags', 31: 'Daisy and two others in front of a Zero Tolerance for Sexual Exploitation and Abuse backdrop',
    32: 'Daisy with a woman in a formal hall',
}

# Gallery: 31 photos on a 6-column grid of square cells. Two 2x2 portraits and five 2x1 group shots bring the
# count to 42 cells, which fills 7 rows of 6 and 14 rows of 3 with no hole. (id, shape, object-position)
GALLERY = [
    (1, 'big', '18% 30%'), (16, '', '60% 30%'), (28, '', '62% 30%'), (3, 'wide', '50% 38%'),
    (9, '', '55% 30%'), (5, '', '50% 22%'), (17, '', '50% 40%'), (23, '', '58% 30%'),
    (2, '', '40% 25%'), (26, '', '45% 30%'), (12, 'wide', '50% 30%'), (20, '', '58% 42%'), (11, '', '66% 35%'),
    (15, 'wide', '52% 62%'), (13, '', '50% 35%'), (18, '', '50% 18%'), (6, 'big', '50% 28%'),
    (10, '', '45% 14%'), (4, '', '45% 30%'), (22, '', '22% 30%'), (19, '', '55% 22%'),
    (7, '', '45% 45%'), (24, 'wide', '50% 46%'), (14, '', '52% 35%'), (21, '', '50% 28%'), (25, '', '54% 12%'),
    (29, '', '50% 62%'), (31, '', '50% 58%'), (32, '', '50% 30%'), (27, '', '55% 62%'), (30, 'wide', '50% 62%'),
]


def _thumb(i, shape):
    """Grid thumbnail for a gallery photo (the lightbox opens the full image). Made once, sized for a 2x screen."""
    import os
    from PIL import Image
    name = f'fordaisy{i}-t'
    out = f'{SITE}/assets/img/{name}.webp'
    if not os.path.exists(out):
        im = Image.open(f'{SITE}/assets/img/fordaisy{i}.webp').convert('RGB')
        side = {'big': 780, 'wide': 540}.get(shape, 400)
        k = side / min(im.size)
        if k < 1:
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        im.save(out, 'WEBP', quality=80, method=6)
    return name


def fordaisy():
    tributes = json.load(open('/home/claude/crawl/tributes.json'))
    tributes = [t.strip() for t in tributes if t and t.strip()]
    first = 16
    LONG = 300

    def card(t):
        long_ = len(t) > LONG
        return (f'<figure class="dz-card{" is-long" if long_ else ""}"><p>{esc(t)}</p>'
                + ('<button type="button" aria-expanded="false">Read the full message</button>' if long_ else '') + '</figure>')
    wall = ''.join(card(t) for t in tributes[:first])
    data_json = json.dumps(tributes, ensure_ascii=False).replace('</', '<\\/')

    assert sorted(g[0] for g in GALLERY) == [i for i in range(1, 33) if i != 8]

    def gal(i, shape, pos):
        alt = GALLERY_ALT.get(i, 'Daisy Coleman')
        cls = f' class="is-{shape}"' if shape else ''
        return (f'<button type="button"{cls} data-src="assets/img/fordaisy{i}.webp" data-cap="{esc(alt)}" aria-label="Open photo: {esc(alt)}">'
                f'{img(_thumb(i, shape), alt, style="object-position:" + pos)}</button>')
    gallery = ''.join(gal(*g) for g in GALLERY)

    vids = [('UcEcU6i6UdY', 'In Memory of Daisy Coleman', 'daisy4', 'Remembrance'),
            ('U1Lt7fK1UWk', 'Daisy’s Virtual Memorial Service', 'yt-u1lt7fk1uwk', 'August 18, 2020'),
            ('O-FPZphiDSc', 'Photos for Remembrance', 'yt-o-fpzphidsc', 'Picture collection, 2020')]
    vid_html = ''.join(f'<div>{yt(v, t, thumb=th, label="Watch")}<h3>{esc(t)}</h3><small>{esc(s)}</small></div>' for v, t, th, s in vids)

    gwf = pod('4A7XFCTULig0ZyOKaW3A9o')
    ngz = pod('3sIH5lMCEkeU0e298AsQe0')
    pods = ''.join(f'<article class="dz-pod">{spotify(p[0], p[1], p[2])}<p>{esc(p[4])}</p></article>' for p in (gwf, ngz))

    body = f'''
<section class="dz-hero">
  <div class="wrap dz-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>#ForDaisy</span></nav>
      <p class="dz-mark">{fl('dz-fl--mark')}In memoriam</p>
      <h1>#For<span class="mk">Daisy</span></h1>
      <p class="dz-dates"><b>Daisy Coleman</b><span>&middot;</span><b>March 30, 1997 – August 4, 2020</b></p>
      <p class="lede">This August marks six years since the passing of Daisy Coleman, SafeBAE’s co-founder. As a teenage survivor, Daisy shared her story in the documentary <i>Audrie &amp; Daisy</i>, speaking openly about what had happened to her and bringing the realities facing young survivors to a national audience. Her vision became <a href="about.html">the foundation of SafeBAE</a> and helped ignite our youth-led movement.</p>
      <div class="btns">{btn('Read the tribute wall', '#wall', 'slate')}{btn('Add your message', '#add', 'ghost')}</div>
    </div>
    <div class="dz-portrait dz-hero__media">
      {fl('dz-fl--line dz-hero__art')}
      <div class="dz-portrait__frame">{img('fordaisy16', 'Daisy Coleman smiling in a blue winter coat', loading='eager')}</div>
    </div>
  </div>
</section>

<section class="band band--slate band--tight">
  <div class="wrap">
    <figure class="dz-cut">
      <blockquote><b>“All the organizing that happened after Daisy spoke out may not necessarily be a direct result but is certainly a ripple effect:</b> the new campus anti-rape movement, followed by the backlash over Brock Turner, followed by the sudden ubiquity of MeToo as both a hashtag and a rallying cry.”</blockquote>
      <figcaption><span>The Cut</span>{a('Read “What Daisy Coleman Changed” in The Cut &#8599;', 'https://www.thecut.com/2020/12/what-daisy-coleman-changed.html')}</figcaption>
    </figure>
  </div>
</section>

<section class="band band--paper" id="daisy">
  <div class="wrap dz-life">
    <div class="dz-life__txt">
      <h2 class="dz-h2">Daisy was more than her advocacy.</h2>
      <p>She was a tattoo artist whose work people still carry with them, and she was loved deeply by her family and friends.</p>
      <p>Her example still guides how we show up for students, and her story is carried forward by us and by communities across the country.</p>
      <a class="dz-teaser" href="fordaisy-tattoos.html">{img('fordaisy25', '')}<span><small>#ForDaisy</small><b>Tattoos &amp; Healing</b><span>Daisy’s art, and tattoos as one path some survivors take to reclaim their bodies.</span></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="dz-life__pics">
      <figure class="dz-ph">{img('fordaisy28', 'Daisy Coleman tattooing a client', style='object-position:60% 30%')}<figcaption>Daisy at work as a tattoo artist</figcaption></figure>
      <figure class="dz-ph">{img('fordaisy21', 'Daisy Coleman with two people, one wearing a SafeBAE shirt', style='object-position:50% 30%')}</figure>
    </div>
  </div>
</section>

<section class="band band--deep dz-wallband" id="wall">
  {fl('dz-fl--line dz-wallband__art')}
  <div class="wrap">
    <div class="dz-wallhead">
      <div>
        <p class="eyebrow">#ForDaisy Memorial Tribute Wall</p>
        <h2>Daisy reached people she never met.</h2>
      </div>
      <p class="dz-count"><b>700+</b><span>tribute messages collected at her memorial service</span></p>
    </div>
    <div class="dz-wallintro">
      <p>Survivors who saw themselves in her story, students who felt less alone because she spoke first, parents and educators who changed how they show up for young people because of her. When she passed, we collected tribute messages at her memorial service, more than 700 of them, and we have held them close ever since.</p>
      <p>Her reach hasn’t stopped. Every year, hundreds of people still find their way to SafeBAE through Daisy’s story and tell us she is the reason they came to this work. Six years later, she is still bringing people in. This year we brought those messages together in one place.</p>
    </div>
    <div class="dz-wall has-more" id="dz-wall">{wall}</div>
    <div class="dz-wall__foot"><span id="dz-shown">Showing {first} of {len(tributes)} messages</span><button class="btn btn--mint" type="button" id="dz-more">Show more messages</button>{btn('Add your message', '#add', 'ghost')}</div>
    <script type="application/json" id="dz-data">{data_json}</script>
  </div>
</section>

<section class="band band--aqua" id="add">
  <div class="wrap">
    <div class="dz-add">
      <span class="dz-add__art" aria-hidden="true">{fl()}{fl()}</span>
      <div class="dz-add__txt">
        <h2>If Daisy touched your life</h2>
        <p>If you knew her, or knew her only through her work, we invite you to add your own message for Daisy.</p>
      </div>
      <form class="form" data-static data-mailto="info@safebae.org" data-subject="#ForDaisy tribute message">
        <div class="field"><label for="dz-msg">Your message</label><textarea id="dz-msg" name="Message for Daisy" placeholder="Write your message for Daisy…" required></textarea></div>
        <div class="dz-add__send"><button class="btn btn--slate" type="submit">Send message</button><p class="form__done" role="status">Thank you for sharing your message for Daisy.</p></div>
      </form>
    </div>
  </div>
</section>

<section class="band band--slate dz-mem" id="remembering">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Remembering Daisy</p><h2 class="dz-h2">The words and images from those days</h2>
      <p class="lede lede--full">Here is the statement we shared with our community on the day Daisy passed, with the recordings and photos from those days, including her virtual memorial service. Together they hold both the grief and the celebration of her life. We’ve kept everything here for anyone who wants to return to it, including people who are only now finding Daisy’s story.</p></div></div>
    <details class="dz-letter">
      <summary>{fl()}<b>Read the statement we shared after Daisy’s passing</b><i aria-hidden="true">+</i></summary>
      <div class="dz-letter__body">
        <div class="dz-letter__head"><h3>DAISY COLEMAN</h3><p>March 30th, 1997 – August 4th, 2020</p></div>
        <p>Through our shock and sadness, we are releasing a statement about our loss of Daisy. As all of our supporters know, Daisy has fought for many years to both heal from her assault and prevent future sexual violence among teens. She was our sister in this work and much of the driving force behind it. We were not just a non-profit team, but a family. We are shattered and shocked by her passing from suicide. She had been in EMDR therapy for 2 years, working on her triggers and healing from the many traumas in her life. She had many coping demons and had been facing and overcoming them all, but as many of you know, healing is not a straight path or any easy one. She fought longer and harder than we will ever know. But we want to be mindful of all the young survivors who looked up to her. Please know that above ALL ELSE, she did this work for you. She loved talking to young people about changing the culture and taking care of one another. Much of her healing came from each of you. She was so proud of the work we’ve done and loved seeing so many fierce young activists push for change in their schools and among their friends.</p>
        <p>She would want young survivors to know they are heard, they matter, they are loved, and there are places for them to get the help they need. And she would want everyone else – peer allies, educators, parents, legislators, religious leaders – to come together to help stop sexual violence and help save teen lives.</p>
        <p>As advocates we know survivors of sexual assault are 10 times more likely to attempt suicide than those who haven’t experienced sexual assault, and that is why we will keep dedicating ourselves to this work in her legacy. There’s no question that she would want that.</p>
        <p class="dz-sign">All of our love,<br>SafeBAE</p>
      </div>
    </details>
    <div class="dz-care"><p>If you are struggling, you are heard and you matter. <b>Call or text 988</b> any time, or text HOME to 741741.</p><button type="button" data-open-help>See all free, confidential support</button></div>
    <div class="dz-vids">{vid_html}</div>
    <div class="dz-photos" id="photos">
      <div class="dz-photos__head"><h3>Daisy, in the pictures people gathered in her honor</h3><span>{len(GALLERY)} photos &middot; tap any photo to enlarge</span></div>
      <div class="gallery dz-gal is-short" data-gallery>{gallery}</div>
      <div class="dz-photos__foot"><button class="btn btn--ghost" type="button" id="dz-allphotos" aria-expanded="false">Show all {len(GALLERY)} photos</button></div>
    </div>
  </div>
</section>

<section class="band band--paper" id="podcasts">
  <div class="wrap">
    <div class="section-head"><div><h2 class="dz-h2">Daisy’s voice, and her legacy</h2></div></div>
    <div class="dz-legacy">
      <div class="dz-legacy__pods">{pods}</div>
      <div class="dz-ded">
        {fl()}
        <p class="eyebrow">For Daisy: Before Anyone Else</p>
        <h3>Certified Peer Educator Training</h3>
        <p>The training is offered in memory of our co-founder, Daisy Coleman, whose vision and leadership continue to inspire SafeBAE’s mission and young people nationwide.</p>
        <div class="btns">{btn('Become a Peer Educator', 'peer-educator.html', 'mint', arrow=True)}{btn('About SafeBAE', 'about.html', 'ghost')}</div>
      </div>
    </div>
  </div>
</section>
'''
    page('fordaisy.html', '#ForDaisy · Remembering Daisy Coleman · SafeBAE', 'Remembering SafeBAE co-founder Daisy Coleman (1997–2020): the #ForDaisy tribute wall, her memorial service, and photos gathered in her honor.',
         body, active='fordaisy', body_class='pg-daisy pg-fordaisy', head_extra=css(DZ_BASE_CSS, DZ_CSS), scripts=DZ_JS)


# =====================================================================
# #FORDAISY: TATTOOS & HEALING
# =====================================================================
TT_SOURCES = [
    ('maxwell', 'Maxwell, D., Leat, S. R., Thomas, J., Thomas, S. A., &amp; Coad, S. (2023). The tattoo environment as a therapeutic healing space for sexual assault survivors. <i>Deviant Behavior</i>.', 'https://doi.org/10.1080/01639625.2023.2250052', 'doi:10.1080/01639625.2023.2250052'),
    ('branco', 'Branco, P. (2017, April 3). Reclaiming the body after trauma: Can body art help abuse survivors heal? VAWnet, National Resource Center on Domestic Violence.', 'https://vawnet.org/news/reclaiming-body-after-trauma-can-body-art-help-abuse-survivors-heal', 'vawnet.org'),
    ('fletcher', 'Fletcher, A. A. (2026, March 2). Reclaiming the body after trauma. <i>Psychology Today</i>.', 'https://www.psychologytoday.com/us/blog/keeping-it-real-and-resilient/202603/reclaiming-the-body-after-trauma', 'psychologytoday.com'),
    ('weisenberger', 'Weisenberger, C. (2025, May 20). How to: Trauma-informed tattooing. Kingpin Tattoo Supply.', 'https://www.kingpintattoosupply.com/blogs/stories-and-articles/how-to-trauma-informed-tattooing', 'kingpintattoosupply.com'),
    ('npr', 'Nungesser, J. (2025, April 29). Ohio tattoo shop helps trauma and abuse survivors transform scars into art. Ideastream Public Media for NPR.', 'https://www.npr.org/2025/04/29/nx-s1-5342586/ohio-tattoo-shop-helps-trauma-and-abuse-survivors-transform-scars-into-art', 'npr.org'),
    ('olr', 'Connecticut Office of Legislative Research. (2013). Report 2013-R-0231 on state laws restricting tattooing of minors, citing the National Conference of State Legislatures.', 'https://www.cga.ct.gov/2013/rpt/2013-R-0231.htm', 'cga.ct.gov'),
]
TT_N = {k: i + 1 for i, (k, *_r) in enumerate(TT_SOURCES)}


def cite(*keys):
    return ''.join(f'<sup class="tt-cite"><a href="#src-{k}" aria-label="Source {TT_N[k]}">{TT_N[k]}</a></sup>' for k in keys)


# line motifs for the research cards, drawn for this page in the brand colours (the daisy is the client's drawing)
TT_ICONS = {
    'heart': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 54C18 44 8 35 8 23.5 8 15.5 14 10 21 10c5 0 8.6 2.8 11 6.6C34.4 12.8 38 10 43 10c7 0 13 5.5 13 13.5C56 35 46 44 32 54z"/><path d="M20 22c1-3 3-5 6-5.5"/></g></svg>',
    'sun': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8 46h48M14 54h36"/><path d="M18 46a14 14 0 0 1 28 0"/><path d="M32 18v8M17 25l5 5M47 25l-5 5M10 38h6M48 38h6"/></g></svg>',
    'vine': '<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8 50c8-10 16-14 24-14s14 6 24-2"/><path d="M20 41c-1-6 3-10 8-10-1 6-4 9-8 10zM38 38c5-3 10-1 12 4-6 1-9-1-12-4z"/><path d="M10 26c6-3 10-2 14 1M40 22c5-4 10-4 15-1" stroke-dasharray="2 5"/></g></svg>',
}

TT_CSS = '''
/* ---- hero ---- */
.pg-tattoo .dz-hero h1{font-size:clamp(3rem,6.8vw,6.4rem); line-height:.92; margin:0 0 .32em}
.tt-comp{position:relative; justify-self:end; width:min(100%,440px); padding:0 12% 9% 0}
.tt-comp__main{position:relative; z-index:1; border-radius:999px 999px var(--r-xl) var(--r-xl); overflow:hidden; aspect-ratio:5/6; background:var(--aqua); box-shadow:0 40px 80px -40px rgba(22,53,64,.55); animation:sb-rise-r 1s .1s var(--ease) both}
.tt-comp__main img{width:100%; height:100%; object-fit:cover; object-position:62% 32%}
.tt-comp__sub{position:absolute; z-index:2; right:0; bottom:0; width:44%; aspect-ratio:1; border-radius:18px; overflow:hidden; border:6px solid var(--dz-bg); box-shadow:var(--shadow-soft); transform:rotate(3deg); animation:sb-rise-r 1s .25s var(--ease) both}
.tt-comp__sub img{width:100%; height:100%; object-fit:cover; object-position:56% 11%}
.tt-comp .sticker{position:absolute; z-index:3; left:-14px; top:20%}
.tt-comp .dz-hero__art{width:168%; left:-42%; top:14%; --fade:linear-gradient(90deg, transparent 6%, #000 21%)}
@media (max-width:1240px){.tt-comp .dz-hero__art{--fade:linear-gradient(90deg, transparent 16%, #000 32%)}}
@media (max-width:900px){
  .tt-comp{width:min(82%,380px); margin-bottom:44px}
  .tt-comp .dz-hero__art{width:172%; left:-40%; top:-9%}
  .tt-comp .sticker{left:-8px}
}

.tt-cite{font-size:.7em; line-height:0; margin-left:1px}
.tt-cite a{text-decoration:none; font-weight:700; color:inherit; padding:0 3px; border-radius:4px; background:rgba(21,255,200,.25)}
.tt-cite a:hover{background:var(--mint); color:var(--slate)}
.tt-cite a{position:relative}
.tt-cite a::after{content:""; position:absolute; inset:-14px -9px}
.band--paper .tt-cite a,.band--mist .tt-cite a,.band--aqua .tt-cite a{color:var(--logo-teal); background:var(--aqua)}
.tt-notes .tt-cite a{color:var(--logo-teal); background:var(--aqua)}

/* ---- the people who carry her work: three groups, then the hoped-for tattoos beside the stencil daisy ---- */
.tt-carried{display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:var(--gap)}
.tt-carried > *{grid-column:span 4; min-width:0}
.tt-carried > .tt-g--row{grid-column:span 8}
.tt-stencil{position:relative; display:grid; place-items:center; min-height:220px; padding:22px; border-radius:var(--r-xl); background:var(--dz-bg)}
.tt-stencil::before{content:""; position:absolute; inset:10px; border:1.5px dashed rgba(29,90,102,.45); border-radius:13px}
.tt-stencil .dz-fl{--fl-w:min(82%,300px); color:var(--slate)}
.js .tt-stencil .dz-fl{clip-path:circle(0% at 49% 47%)}
.js .tt-carried.is-in .tt-stencil .dz-fl{animation:dzOpen 1.9s .15s var(--ease) both}
.tt-g{display:flex; flex-direction:column; min-width:0; margin:0; padding:var(--pad-card); border-radius:var(--r-xl); border:1px solid var(--line-dark); background:rgba(255,255,255,.045)}
.tt-g__h{display:flex; align-items:center; gap:12px; margin:0 0 4px; font-family:var(--mono); font-size:.76rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.tt-g__h::after{content:""; flex:1; border-top:1.5px dashed rgba(21,255,200,.4)}
.tt-g blockquote{flex:1 1 auto; display:flex; align-items:center; margin:0; padding:14px 0; border-bottom:1.5px dashed rgba(209,254,255,.2); font-family:var(--display); font-weight:500; font-stretch:90%; font-size:clamp(1.14rem,1.5vw,1.34rem); line-height:1.3; color:#fff; text-wrap:pretty}
.tt-g blockquote:last-child{border-bottom:0; padding-bottom:0}
.tt-g--row .tt-g__q{flex:1; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:0 var(--gap)}
.tt-g--row blockquote{align-items:flex-start; padding:14px 0}
.tt-g--row blockquote:nth-child(n+3){border-bottom:0; padding-bottom:0}
.tt-from{display:flex; flex-wrap:wrap; gap:10px 20px; align-items:center; justify-content:space-between; margin-top:var(--gap); padding-top:18px; border-top:1px solid var(--line-dark); font-size:.95rem; color:rgba(255,255,255,.82)}
.tt-from a{color:var(--mint); font-weight:700}
@media (max-width:1000px){
  .tt-carried > *{grid-column:span 6}
  .tt-carried > .tt-stencil{order:1}
  .tt-carried > .tt-g--row{grid-column:1/-1; order:2}
}
@media (max-width:700px){
  .tt-carried > *, .tt-carried > .tt-stencil{grid-column:1/-1}
  .tt-stencil{min-height:0; padding:28px 22px} .tt-stencil .dz-fl{--fl-w:min(64%,240px)}
  .tt-g--row .tt-g__q{display:block}
  .tt-g--row blockquote, .tt-g--row blockquote:nth-child(n+3){padding:14px 0; border-bottom:1.5px dashed rgba(209,254,255,.2)}
  .tt-g--row blockquote:last-child{border-bottom:0; padding-bottom:0}
}

/* ---- what survivors and researchers describe ---- */
.tt-flash{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.tt-f{display:flex; flex-direction:column; padding:var(--pad-card); border-radius:var(--r-xl); border:1.5px dashed rgba(29,90,102,.4); background:#fff}
.tt-f__head{display:flex; align-items:center; gap:16px; margin-bottom:14px}
.tt-f__icon{flex:none; width:68px; height:68px; border-radius:50%; background:var(--aqua); color:var(--logo-teal); display:grid; place-items:center}
.tt-f__icon svg{width:42px; height:42px}
.tt-f__icon .dz-fl{--fl-w:50px}
.tt-f h3{font-size:1.4rem; margin:0}
.tt-f p{margin:0 0 .5em; color:var(--dz-ink); font-size:1.02rem; line-height:1.62}
.tt-f p:last-child{margin:0}
.tt-cover{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin-top:var(--gap); scroll-margin-top:96px}
.tt-cover > *{min-width:0}
.tt-cover__lead{display:flex; flex-direction:column; gap:14px}
.tt-cover__lead .tt-f{flex:1}
.tt-cover__note{margin:0; padding:16px 18px; border-radius:16px; background:var(--mist); border:1px solid var(--line); font-size:.97rem; line-height:1.55; color:var(--dz-ink)}
.tt-cover__note b{color:var(--logo-teal)}
@media (max-width:1000px){.tt-flash{grid-template-columns:repeat(2,minmax(0,1fr))} .tt-flash > :last-child{grid-column:1/-1} .tt-cover{grid-template-columns:repeat(2,minmax(0,1fr))} .tt-cover__lead{grid-column:1/-1}}
@media (max-width:700px){.tt-flash,.tt-cover{grid-template-columns:1fr}}

/* ---- before you decide, then the consultation checklist (one slate section) ---- */
.tt-decideband .dz-h2{color:#fff}
.tt-decide{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap); align-items:stretch}
.tt-decide__l{display:flex; flex-direction:column; min-width:0}
.tt-decide__l .dz-h2{margin:0 0 .5em}
.tt-decide__l .tt-pull{flex:1}
.tt-pull{container-type:inline-size; position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:center; min-width:0; margin:0; padding:clamp(24px,2.8vw,36px); border-radius:var(--r-xl); background:var(--slate-deep) var(--grain); border:1px solid var(--line-dark); color:#fff}
.tt-pull .dz-fl{position:absolute; --fl-w:112cqw; --fl-art:url(assets/img/daisy-line.svg); --fl-heart:transparent; right:-34cqw; bottom:-43cqw; color:var(--mint); opacity:.3}
.tt-pull blockquote{position:relative; margin:0; font-family:var(--display); font-weight:500; font-stretch:86%; font-size:clamp(1.7rem,2.9vw,2.5rem); line-height:1.12; color:#fff; text-wrap:balance}
.tt-pull figcaption{position:relative; margin-top:18px; font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; line-height:1.5; color:var(--aqua)}
.tt-notes{display:flex; flex-direction:column; min-width:0; background:#fff; color:var(--slate); border-radius:var(--r-xl); overflow:hidden}
.tt-notes > div{flex:1 1 auto; display:grid; grid-template-columns:minmax(0,4fr) minmax(0,7fr); gap:6px 24px; align-items:start; padding:clamp(16px,1.9vw,22px) var(--pad-card); border-bottom:1px solid var(--line)}
.tt-notes > div:last-child{border-bottom:0}
.tt-notes h3{font-size:1.28rem; margin:0; color:var(--slate)}
.tt-notes > .tt-minor{background:var(--dz-bg)}
.tt-notes > .tt-minor h3{font-weight:600; font-stretch:84%; font-size:1.6rem; line-height:1; color:var(--logo-teal)}
.tt-notes :focus-visible,.tt-check :focus-visible{outline-color:var(--teal)}
.tt-notes p{margin:0; font-size:1.02rem; line-height:1.6}
.tt-consult{margin-top:clamp(44px,5vw,72px); padding-top:clamp(32px,3.6vw,48px); border-top:1px solid var(--line-dark); scroll-margin-top:96px}
.tt-consult__h{font-family:var(--display); font-weight:600; font-stretch:84%; font-size:clamp(1.8rem,3vw,2.6rem); line-height:1.05; color:#fff; margin:0 0 .3em}
.tt-consult__lede{margin:0 0 var(--head-gap); font-size:var(--fs-lede); line-height:1.55; font-weight:500; color:rgba(255,255,255,.88)}
@media (max-width:1100px){.tt-notes > div{grid-template-columns:1fr}}
@media (max-width:900px){.tt-decide{grid-template-columns:1fr} .tt-pull{padding-bottom:max(150px,34cqw)} .tt-pull .dz-fl{--fl-w:min(112cqw,460px); right:-90px; bottom:auto; top:calc(100% - 132px)}}

/* ---- consultation checklist ---- */
.tt-check{background:#fff; color:var(--slate); border:1px solid var(--line); border-radius:var(--r-xl); box-shadow:var(--shadow-soft); overflow:hidden}
.tt-check__head{display:flex; flex-wrap:wrap; gap:8px 28px; align-items:center; justify-content:space-between; padding:18px var(--pad-card); background:var(--mist); border-bottom:1px solid var(--line)}
.tt-check__head b{font-family:var(--display); font-weight:700; font-stretch:92%; font-size:1.45rem; line-height:1.1; color:var(--logo-teal)}
.tt-check__head p{flex:1 1 420px; margin:0; font-size:1rem; line-height:1.5; color:var(--dz-ink)}
.tt-check__head span{font-family:var(--mono); font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; color:var(--slate); font-weight:600; background:var(--aqua); padding:7px 12px; border-radius:8px; white-space:nowrap}
.tt-check ol{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr}
.tt-check li{margin:0; border-bottom:1px solid var(--line)}
.tt-check li:nth-child(odd){border-right:1px solid var(--line)}
.tt-check li:nth-last-child(-n+2){border-bottom:0}
.tt-check label{display:grid; grid-template-columns:30px minmax(0,1fr); gap:16px; height:100%; padding:20px var(--pad-card); cursor:pointer; transition:background .2s}
.tt-check label:hover{background:var(--dz-bg)}
.tt-check label:has(input:checked){background:var(--mist)}
.tt-check input{appearance:none; -webkit-appearance:none; width:30px; height:30px; margin:1px 0 0; border-radius:9px; border:2px solid var(--logo-teal); display:grid; place-items:center; cursor:pointer; background:#fff; transition:background .2s, border-color .2s}
.tt-check input::after{content:""; width:13px; height:7px; border-left:3px solid var(--slate); border-bottom:3px solid var(--slate); transform:rotate(-45deg) translate(1px,-1px) scale(0); transition:transform .2s var(--ease)}
.tt-check input:checked{background:var(--mint); border-color:var(--mint)}
.tt-check input:checked::after{transform:rotate(-45deg) translate(1px,-1px) scale(1)}
.tt-check input:focus-visible{outline:3px solid var(--teal); outline-offset:3px}
.tt-check strong{display:block; font-family:var(--display); font-weight:700; font-stretch:102%; font-size:1.1rem; line-height:1.35}
.tt-check em{display:block; font-style:normal; margin-top:8px; color:var(--dz-ink); font-size:1rem; line-height:1.5}
.tt-check em::before{content:"Ask: "; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.tt-check__foot{display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center; justify-content:space-between; padding:14px var(--pad-card); border-top:1px solid var(--line); background:var(--mist); font-size:.92rem; color:var(--ink-soft)}
@media (max-width:820px){.tt-check ol{grid-template-columns:1fr} .tt-check li:nth-child(odd){border-right:0} .tt-check li:nth-last-child(2){border-bottom:1px solid var(--line)}}

/* ---- cover-up programs: two reports beside the "covering a reminder" reason ---- */
.tt-ex{display:flex; flex-direction:column; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--slate); background-image:var(--grain); color:#fff}
.tt-ex .eyebrow{margin-bottom:.6rem; color:var(--mint)}
.tt-ex h3{font-size:1.36rem; margin:0 0 .5em; color:#fff}
.tt-ex p:not(.eyebrow){color:rgba(255,255,255,.9); font-size:1rem; line-height:1.6; margin:0 0 .7em}
.tt-ex ul{margin:0 0 .8em; padding-left:1.1em; color:rgba(255,255,255,.9); font-size:1rem; line-height:1.55}
.tt-ex ul li::marker{color:var(--mint)}
.tt-ex small{display:block; margin-top:auto; padding-top:12px; border-top:1px solid var(--line-dark); font-family:var(--mono); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; color:var(--aqua)}

/* ---- closing: other ways to heal, back to #ForDaisy, sources ---- */
.tt-heal{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(24px,4vw,56px); align-items:center}
.tt-heal .dz-h2{color:#fff; margin:0 0 .4em}
.tt-heal .lede{margin:0; color:rgba(255,255,255,.9)}
.tt-heal__box{display:flex; flex-direction:column; justify-content:center; gap:16px; background:var(--mist); color:var(--slate); border-radius:var(--r-xl); padding:var(--pad-card)}
.tt-heal__box p{margin:0; font-size:1.08rem; line-height:1.55}
.tt-heal__box .btns{display:grid; grid-template-columns:1fr}
.tt-heal__box p b{display:block; font-family:var(--display); font-weight:600; font-stretch:86%; font-size:1.7rem; line-height:1.1; color:var(--logo-teal); margin-bottom:6px}
.tt-heal__box :focus-visible{outline-color:var(--teal)}
.tt-back{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:16px clamp(20px,3vw,36px); align-items:center; margin-top:clamp(36px,4vw,56px); padding:clamp(18px,2.2vw,26px) 0; border-block:1px solid var(--line-dark)}
.tt-back .dz-fl{--fl-w:96px; color:var(--aqua)}
.tt-back p{margin:0; font-size:1.08rem; line-height:1.55; color:rgba(255,255,255,.9)}
.tt-back p a{color:var(--mint); font-weight:700}
.tt-sources{margin-top:clamp(28px,3.2vw,40px)}
.tt-sources h2{font-family:var(--mono); font-size:.76rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; font-stretch:100%; color:var(--mint); margin:0 0 16px}
.tt-src{margin:0; padding:0; list-style:none; counter-reset:src; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,auto); grid-auto-flow:column; gap:10px var(--gap)}
.tt-src li{margin:0; counter-increment:src; display:grid; grid-template-columns:28px minmax(0,1fr); gap:12px; padding:4px; font-size:.92rem; line-height:1.5; color:rgba(255,255,255,.84); scroll-margin-top:130px; border-radius:10px}
.tt-src li::before{content:counter(src); font-family:var(--mono); font-weight:600; color:var(--slate); background:var(--aqua); border-radius:8px; height:26px; display:grid; place-items:center; font-size:.8rem}
.tt-src li:target{background:rgba(255,255,255,.08); box-shadow:0 0 0 2px var(--mint)}
.tt-src a{color:var(--mint); font-weight:600; word-break:break-word}
@media (max-width:860px){.tt-heal{grid-template-columns:1fr} .tt-back{grid-template-columns:auto minmax(0,1fr)} .tt-back .btns{grid-column:1/-1}}
@media (max-width:820px){.tt-src{grid-template-columns:1fr; grid-template-rows:none; grid-auto-flow:row}}
@media (max-width:480px){.tt-back{grid-template-columns:1fr} .tt-back .dz-fl{--fl-w:80px}}

@media print{
  body *{visibility:hidden}
  .tt-check, .tt-check *{visibility:visible}
  .tt-check{position:absolute; left:0; top:0; width:100%; box-shadow:none}
  .tt-check__foot{display:none}
}
'''

TT_JS = r'''<script>(function(){
  var KEY = 'sb-tattoo-check', box = document.querySelector('.tt-check');
  if(box){
    var inputs = box.querySelectorAll('input[type=checkbox]'), out = box.querySelector('[data-count]');
    var save = function(){ var v = []; inputs.forEach(function(i, k){ if(i.checked) v.push(k); }); try{ localStorage.setItem(KEY, JSON.stringify(v)); }catch(e){} if(out) out.textContent = v.length + ' of ' + inputs.length + ' checked'; };
    try{ var v = JSON.parse(localStorage.getItem(KEY) || '[]'); v.forEach(function(k){ if(inputs[k]) inputs[k].checked = true; }); }catch(e){}
    inputs.forEach(function(i){ i.addEventListener('change', save); });
    save();
    var p = box.querySelector('[data-print]'); if(p) p.addEventListener('click', function(){ window.print(); });
    var r = box.querySelector('[data-reset]'); if(r) r.addEventListener('click', function(){ inputs.forEach(function(i){ i.checked = false; }); save(); });
  }
  /* the drawn daisy behind the tribute quotes opens once, when the section comes into view */
  var c = document.querySelector('.tt-carried');
  if(c){
    if('IntersectionObserver' in window){ var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ c.classList.add('is-in'); io.disconnect(); } }); }, {threshold:.25}); io.observe(c); }
    else c.classList.add('is-in');
  }
})();</script>'''


def fordaisy_tattoos():
    # excerpts from the tribute wall, quoted as written, grouped by what the writer describes
    carried = [
        ('Carried on skin', '', [
            '…you’ll always be in my heart and a piece of you forever tattooed on my hip.',
            '…look down at the tattoos you’ve put on my body, I’m constantly reminded of you and the impact just you as a person has put on my life.']),
        ('In her honor', '', [
            '…when she died I got a tattoo of a daisy in her honor',
            'I wanted to meet you and get a tattoo from you someday. now I will design a tattoo in your honor for myself.']),
        ('Her other art', '', [
            "she painted a picture of my cat for me and my cat has passed since. it's such a beautiful bittersweet piece of art!",
            'You gave me strength, you made me laugh, you leveled me with your art and the magic you carried with you.']),
        ('Hoped to be tattooed by her', 'row', [
            'I miss you daisy. I always wanted to be tattooed by you',
            'I dreamt of one day being tatted by you.',
            'I still wish to get the tattoo I planned to get done by you, in your memory.',
            'I wish I had gotten the chance to meet you and be tattooed by you.']),
    ]

    def group(tag, kind, qs):
        quotes = ''.join(f'<blockquote>“{esc(q)}”</blockquote>' for q in qs)
        if kind == 'row':
            quotes = f'<div class="tt-g__q">{quotes}</div>'
        return f'<figure class="tt-g{(" tt-g--" + kind) if kind else ""}"><figcaption class="tt-g__h">{esc(tag)}</figcaption>{quotes}</figure>'
    carried_html = ''.join(group(*g) for g in carried)

    flash = [
        ('daisy', 'Choice over your own body', [
            f'Trauma can take away a person’s control over their body, and healing often involves restoring choice. A tattoo is a sensation the person chose, for a set length of time, that they can pause or stop.{cite("fletcher")}',
            f'In interviews with survivors and tattoo artists, researchers found the tattoo setting supported survivors’ autonomy.{cite("maxwell")}']),
        ('heart', 'Ritual and belonging', [
            f'Researchers analyzed interviews with 10 survivors of sexual trauma and 7 tattoo artists. Rapport with the artist and the ritual of getting tattooed helped survivors feel they belonged, and the look and feel of the studio helped it feel comfortable and safe.{cite("maxwell")}']),
        ('sun', 'Marking a new chapter', [
            f'Some survivors describe a tattoo as a way to mark a new chapter. A survivor quoted by the National Resource Center on Domestic Violence put it this way: “My first tattoo gave me the strength to leave an abusive marriage.”{cite("branco")}']),
        ('vine', 'Covering a reminder', [
            f'Some marks are painful reminders, such as a scar, an abuser’s name or a brand used by traffickers. Artists can cover them or turn them into new art, and tattoo removal is another option.{cite("branco", "npr")}']),
    ]

    def icon(ic):
        return fl('dz-fl--mark') if ic == 'daisy' else TT_ICONS[ic]
    def fcard(ic, t, ps, tag='article', cls='tt-f'):
        return (f'<{tag} class="{cls}"><div class="tt-f__head"><span class="tt-f__icon" aria-hidden="true">{icon(ic)}</span><h3>{esc(t)}</h3></div>'
                + ''.join(f'<p>{p}</p>' for p in ps) + f'</{tag}>')
    flash_html = ''.join(fcard(*f) for f in flash[:3])
    cover_card = fcard(*flash[3], tag='div', cls='tt-f tt-f--cover')

    checks = [
        ('The artist doesn’t ask whether you’ve experienced trauma. You decide if, how and when to share anything personal.', 'Do you need to know anything about me before we start?'),
        ('They explain what they’re about to do and ask before touching, adjusting or moving you.', 'Will you tell me before you touch me or move my arm?'),
        ('They check in during the session and remind you that you can pause, stop or speak up at any time.', 'Can we take a break whenever I need one?'),
        ('They offer privacy: a private room if there is one, or sheets or coverings so only the area being tattooed is exposed.', 'Is there a private space, or a way to keep the rest of me covered?'),
        ('They avoid edgy jokes with clients they don’t know well, steer clear of topics like politics or religion, and never assume your boundaries or comfort level.', 'Can I tell you what I’m comfortable talking about?'),
        ('They let you warm up to them, without forcing a connection.', 'Is it okay if I’m quiet during the session?'),
    ]
    check_html = ''.join(f'<li><label><input type="checkbox" name="tt-{k}"><span><strong>{esc(t)}</strong><em>{esc(q)}</em></span></label></li>' for k, (t, q) in enumerate(checks))

    src_html = ''.join(f'<li id="src-{k}"><span>{text} <a href="{u}" target="_blank" rel="noopener">{esc(lbl)} &#8599;</a></span></li>' for k, text, u, lbl in TT_SOURCES)

    body = f'''
<section class="dz-hero">
  <div class="wrap dz-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="fordaisy.html">#ForDaisy</a><span>/</span><span>Tattoos &amp; Healing</span></nav>
      <p class="dz-mark">{fl('dz-fl--mark')}#ForDaisy</p>
      <h1>Tattoos &amp; <span class="mk">healing</span></h1>
      <p class="lede">Daisy Coleman, <a href="about.html">SafeBAE’s co-founder</a>, was a tattoo artist whose work people still carry with them. Some survivors of sexual violence describe getting tattooed as one way to reclaim their bodies. It is one path among many, and it isn’t right for everyone.</p>
      <div class="btns">{btn('What survivors describe', '#describe', 'slate')}{btn('Questions for a consultation', '#consultation', 'ghost')}</div>
    </div>
    <div class="tt-comp dz-hero__media">
      {fl('dz-fl--line dz-hero__art')}
      <div class="tt-comp__main">{img('fordaisy28', 'Daisy Coleman tattooing a client', loading='eager')}</div>
      <div class="tt-comp__sub">{img('fordaisy25', 'Daisy Coleman holding up her tattooed hand', loading='eager')}</div>
      <span class="sticker sticker--aqua">Daisy at work</span>
    </div>
  </div>
</section>

<section class="band band--deep" id="carried">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">From the #ForDaisy tribute wall</p><h2 class="dz-h2">The people who carry her work</h2>
      <p class="lede lede--full" style="color:rgba(255,255,255,.88)">In their messages for Daisy, people wrote about tattoos she gave them and tattoos they got in her honor. Others wrote about the tattoo they had hoped she would give them.</p></div></div>
    <div class="tt-carried">{carried_html}<div class="tt-stencil" aria-hidden="true">{fl('dz-fl--line')}</div></div>
    <div class="tt-from"><span>Excerpts from messages on the #ForDaisy Memorial Tribute Wall, quoted as written.</span>{a('Read the tribute wall &rarr;', 'fordaisy.html#wall')}</div>
  </div>
</section>

<section class="band band--paper" id="describe">
  <div class="wrap">
    <div class="section-head"><div><h2 class="dz-h2">What survivors and researchers describe</h2>
      <p class="lede lede--full muted">Research on tattooing and healing after sexual violence is limited.{cite("branco")} Survivors, tattoo artists and researchers describe a few reasons it can matter.</p></div></div>
    <div class="tt-flash">{flash_html}</div>
    <div class="tt-cover" id="cover-ups">
      <div class="tt-cover__lead">{cover_card}
        <p class="tt-cover__note"><b>Cover-up programs in the news.</b> Some artists offer free or low-cost cover-ups for survivors. These are examples from reporting, not SafeBAE partners. Programs change, so check current details directly with any studio before you make plans.</p></div>
      <article class="tt-ex">
        <p class="eyebrow">Amherst, Ohio &middot; reported 2025</p>
        <h3>Phoenix Ink &amp; Beauty: the Art of Healing program</h3>
        <p>Co-owner Angelique Agnew’s studio covers scars from self-harm or surgery, and works with survivors of human trafficking.{cite("npr")}</p>
        <ul><li>People apply; if accepted, they pay only for the ink and tattooing supplies.</li><li>Artists donate their time and art.</li></ul>
        <small>Source: Ideastream Public Media for NPR</small>
      </article>
      <article class="tt-ex">
        <p class="eyebrow">Reported 2017</p>
        <h3>Artists covering marks left by abuse</h3>
        <p>A 2017 overview from the National Resource Center on Domestic Violence described artists offering free cover-ups to survivors, such as Flavia Carvalho in Brazil, and Sacred Transformations, a Chicago organization that turns scars or marks left by abuse, neglect, rape or trafficking into art.{cite("branco")}</p>
        <small>Source: VAWnet</small>
      </article>
    </div>
  </div>
</section>

<section class="band band--slate tt-decideband" id="one-path">
  <div class="wrap">
    <div class="tt-decide">
      <div class="tt-decide__l"><h2 class="dz-h2">Before you decide</h2>
      <figure class="tt-pull">{fl()}<blockquote>“Tattoos are neither inherently pathological nor inherently therapeutic.”</blockquote><figcaption>Adrian A. Fletcher, Psy.D., <i>Psychology Today</i>{cite("fletcher")}</figcaption></figure></div>
      <div class="tt-notes">
        <div><h3>It isn’t a treatment</h3><p>Tattoos should never be prescribed as treatment.{cite("fletcher")} Body art is one of many ways people heal, and it isn’t right for everyone.{cite("branco")}</p></div>
        <div><h3>Readiness matters</h3><p>Before getting tattooed, weigh medical safety, whether you feel ready, and whether you understand what you are agreeing to.{cite("fletcher")} A tattoo is permanent, so there is no rush.</p></div>
        <div><h3>Some marks hurt</h3><p>A tattoo can also become a painful reminder. If you carry one, covering it up or having it removed are options.{cite("branco")}</p></div>
        <div class="tt-minor"><h3>Under 18?</h3><p>Tattoo laws for minors differ from state to state. In a 2013 review, 17 states banned tattooing anyone under 18 and 28 allowed it only with a parent’s consent.{cite("olr")} Check your state’s rules before you plan anything.</p></div>
      </div>
    </div>
    <div class="tt-consult" id="consultation">
      <h3 class="tt-consult__h">What trauma-informed tattooing looks like</h3>
      <p class="tt-consult__lede">Tattoo artist Cora Weisenberger describes practices artists can use with every client.{cite("weisenberger")}</p>
      <div class="tt-check">
        <div class="tt-check__head"><b>Before you book</b><p>Take this list to a consultation. Tick off what the studio already does, and use the questions to ask about the rest. Your ticks stay on this device.</p><span data-count>0 of {len(checks)} checked</span></div>
        <ol>{check_html}</ol>
        <div class="tt-check__foot"><span>Source: Weisenberger (2025), Kingpin Tattoo Supply.</span><span class="btns"><button class="btn btn--slate btn--sm" type="button" data-print>Print this list</button><button class="btn btn--ghost btn--sm" type="button" data-reset>Clear</button></span></div>
      </div>
    </div>
  </div>
</section>

<section class="band band--logo" id="other-ways">
  <div class="wrap">
    <div class="tt-heal">
      <div>
        <h2 class="dz-h2">If a tattoo isn’t right for you, or not right now</h2>
        <p class="lede">Healing is long, nonlinear, and personal, and there is no right or wrong way to do it. Many survivors find strength in connection with peers, support groups, or professionals, and in practices that help them reconnect with their bodies and feelings.</p>
      </div>
      <div class="tt-heal__box">
        <p><b>Talk to someone now.</b> Free, confidential hotlines, most open 24/7.</p>
        <div class="btns"><button class="btn btn--slate" type="button" data-open-help>See support hotlines</button>{btn('Survivor support', 'survivor-support.html', 'ghost', arrow=True)}</div>
      </div>
    </div>
    <div class="tt-back">
      {fl()}
      <p>Read the messages people wrote for Daisy, or add your own. SafeBAE’s {a('Certified Peer Educator Training', 'peer-educator.html')} is offered in her memory.</p>
      <div class="btns">{btn('Read the tribute wall', 'fordaisy.html#wall', 'mint', arrow=True)}{btn('Add your message', 'fordaisy.html#add', 'ghost')}</div>
    </div>
    <div class="tt-sources" id="sources">
      <h2>Sources</h2>
      <ol class="tt-src">{src_html}</ol>
    </div>
  </div>
</section>
'''
    page('fordaisy-tattoos.html', 'Tattoos & Healing · #ForDaisy · SafeBAE', 'Daisy Coleman was a tattoo artist whose work people still carry with them. Tattoos as one path some survivors take to reclaim their bodies, and what trauma-informed tattooing looks like.',
         body, active='fordaisy', body_class='pg-daisy pg-tattoo', head_extra=css(DZ_BASE_CSS, TT_CSS), scripts=TT_JS)


def build():
    fordaisy()
    fordaisy_tattoos()


if __name__ == '__main__':
    build()
