"""ABOUT group: about, team, impact, photo credits."""
from lib import *
from data import PODCASTS
import json, os, re, glob

WP = 'https://www.safebae.org/wp-content/uploads/'
PAPER = 'https://www.tandfonline.com/doi/full/10.1080/10538712.2024.2385468'


def pod(eid):
    return next(p for p in PODCASTS if p[0] == eid)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


# Shared by the four pages: dark custom heroes, the 12-column feature rows (7/5 and 5/7), light eyebrows.
V2_CSS = """
main .eyebrow{color:var(--logo-teal)}
.v2-dark{position:relative; overflow:hidden; background-image:var(--grain); --wm-o:.16}
.v2-dark .eyebrow{color:var(--mint)}
.v2-dark .mk{background:none; color:var(--mint)}
.v2-dark > .wrap{position:relative; z-index:1}
.ab-row{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.ab-row--57{grid-template-columns:minmax(0,5fr) minmax(0,7fr)}
.ab-row > *{min-width:0}
.ab-col{display:flex; flex-direction:column}
.ab-col > .ab-floor{margin-top:auto}
@media (max-width:900px){ .ab-row,.ab-row--57{grid-template-columns:minmax(0,1fr)} }
"""


def css(*parts):
    return '<style>' + V2_CSS + ''.join(parts) + '</style>'

# =====================================================================
# ABOUT
# =====================================================================
ABOUT_CSS = '''
/* hero: 7/5, headline sized to its column */
.ab-hero{background-color:var(--slate); color:#fff}
.ab-hero__grid{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center; padding-block:clamp(44px,6vw,84px) clamp(56px,7vw,96px)}
.ab-hero h1{font-size:clamp(2.3rem,5.3vw,4.8rem); line-height:.9; font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:-.02em; margin:0 0 .45em}
.ab-hero h1 > span{display:block; white-space:nowrap}
.ab-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.ab-hero .crumbs{margin-bottom:18px}
.ab-collage{position:relative; padding:0 0 17% 0}
.ab-collage__main img{width:100%; aspect-ratio:5/4; object-fit:cover; object-position:50% 30%; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7)}
.ab-collage__sub{position:absolute; right:-14px; bottom:0; width:52%; border:6px solid var(--slate); border-radius:16px; overflow:hidden; transform:rotate(2.5deg); box-shadow:0 20px 40px -20px rgba(0,0,0,.6)}
.ab-collage__sub img{width:100%; aspect-ratio:4/3; object-fit:cover}
.ab-collage .sticker{position:absolute; left:-12px; top:20px; z-index:2}
.ab-collage__cap{position:absolute; left:0; bottom:0; width:44%; margin:0; padding-bottom:6px; font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; line-height:1.5; color:var(--aqua)}
@media (max-width:900px){.ab-hero__grid{grid-template-columns:minmax(0,1fr)} .ab-collage{max-width:600px}}
@media (max-width:480px){.ab-collage__sub{right:-6px} .ab-collage .sticker{left:-6px}}

/* B / A / E */
.ab-bae{background:var(--mint); color:var(--slate); padding-block:clamp(40px,5vw,72px)}
.ab-bae__row{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); align-items:end}
.ab-bae__l{display:block; font-family:var(--display); font-weight:900; font-size:clamp(5rem,15vw,13rem); line-height:.8; letter-spacing:-.03em; font-stretch:125%; transition:font-stretch 1.2s cubic-bezier(.2,.8,.2,1), letter-spacing 1.2s}
.js .ab-bae:not(.in) .ab-bae__l{font-stretch:62%; letter-spacing:-.06em}
.ab-bae__w{display:block; font-family:var(--display); font-weight:800; font-stretch:110%; font-size:clamp(1.1rem,2.4vw,2rem); text-transform:uppercase; border-top:4px solid var(--slate); padding-top:10px; margin-top:12px}
.ab-bae__row > div:nth-child(2) .ab-bae__l{transition-delay:.12s} .ab-bae__row > div:nth-child(3) .ab-bae__l{transition-delay:.24s}
.ab-bae p{margin:clamp(20px,3vw,34px) 0 0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.12rem,1.6vw,1.44rem); line-height:1.3; text-wrap:balance}

/* story: head + lede full width, then 7/5 text and photo, then the quote */
.ab-story__text{align-self:center}
.ab-story__text p{font-size:1.06rem; line-height:1.7}
.ab-story__fig{margin:0; min-height:360px}
.ab-story__fig > img{object-position:74% 40%}
.ab-story__fig figcaption{position:absolute; left:14px; bottom:14px; font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; color:#fff; background:rgba(22,53,64,.82); padding:6px 10px; border-radius:6px}
.ab-drop::first-letter{font-family:var(--display); font-weight:900; font-stretch:125%; float:left; font-size:4.3em; line-height:.78; margin:.06em .1em 0 0; color:var(--teal)}
.ab-pull{position:relative; overflow:hidden; margin:clamp(28px,4vw,52px) 0 0; padding:clamp(26px,3.4vw,46px) clamp(24px,3.6vw,52px); background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl)}
.ab-pull .daisy-art{position:absolute; right:-56px; top:50%; width:min(40%,430px); color:var(--mint); opacity:.34; transform:translateY(-46%) rotate(-8deg)}
.ab-pull blockquote{position:relative; margin:0; padding-right:min(24%,270px); font-family:var(--display); font-weight:800; font-stretch:106%; font-size:clamp(1.3rem,2.5vw,2.1rem); line-height:1.2; text-wrap:pretty}
.ab-pull blockquote::before{content:"\\201C"; display:block; font-size:2.6em; line-height:.62; font-stretch:125%; color:var(--mint); margin-bottom:.02em}
.ab-pull figcaption{position:relative; display:block; margin-top:16px; font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:900px){.ab-story__fig{min-height:0; aspect-ratio:16/10}}
@media (max-width:640px){.ab-pull blockquote{padding-right:0} .ab-pull .daisy-art{opacity:.2; width:70%; right:-30%}}

/* how we began: head full width, then the film (7) beside the account and the names (5) */
.ab-began .lede{color:rgba(255,255,255,.9)}
.ab-began .ab-row > :first-child{align-self:center}
.ab-began__txt{justify-content:space-between; gap:clamp(18px,2.2vw,28px)}
.ab-began__txt p{margin:0; font-size:1.14rem; line-height:1.7; color:rgba(255,255,255,.9)}
.ab-names{display:flex; flex-wrap:wrap; gap:8px; margin:0; padding:clamp(18px,2.2vw,28px) 0 0; list-style:none; border-top:1px solid var(--line-dark)}
.ab-names li{margin:0; display:inline-flex; align-items:center; gap:7px; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1rem; line-height:1.1; padding:9px 15px; border-radius:999px; border:1.5px solid rgba(209,254,255,.35); color:#fff}
.ab-names li .daisy{width:1.05em; height:1.05em; color:var(--mint)}

/* co-founders: four cards on shared rows */
.ab-founders{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0 var(--gap)}
.ab-f{display:flex; flex-direction:column; min-width:0; text-decoration:none; color:var(--slate); background:#fff; border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ab-f:hover{transform:translateY(-5px); box-shadow:0 30px 54px -30px rgba(22,53,64,.6)}
.ab-f__img{position:relative; aspect-ratio:3/4; overflow:hidden; background:var(--slate)}
.ab-f__img img{width:100%; height:100%; object-fit:cover; object-position:50% 22%; transition:transform .6s var(--ease)}
.ab-f:hover .ab-f__img img{transform:scale(1.04)}
.ab-f__badge{position:absolute; top:12px; right:12px; width:46px; height:46px; border-radius:50%; background:var(--slate); display:grid; place-items:center}
.ab-f__badge .daisy{width:30px; height:30px; color:var(--mint)}
.ab-f__body{padding:18px 18px 20px; display:flex; flex-direction:column; flex:1; min-width:0}
.ab-f__body small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.ab-f__body b{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.2rem,1.5vw,1.36rem); line-height:1.08; margin-top:6px}
.ab-f__body span{margin-top:auto; padding-top:14px; font-size:.95rem; line-height:1.4; font-weight:700; color:var(--logo-teal)}
.ab-f__body span::after{content:"\\00a0\\2192"}
@supports (grid-template-rows:subgrid){
  .ab-f{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:0}
  .ab-f__body{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:0}
  .ab-f__body span{margin-top:0; align-self:start}
}
@media (max-width:960px){.ab-founders{grid-template-columns:repeat(2,minmax(0,1fr))} .ab-f:nth-child(n+3){margin-top:var(--gap)}}
@media (max-width:520px){
  .ab-founders{grid-template-columns:minmax(0,1fr); gap:12px}
  .ab-f:nth-child(n+3){margin-top:0}
  .ab-f,.ab-f__body{display:flex; grid-row:auto}
  .ab-f{flex-direction:row}
  .ab-f__img{flex:0 0 38%; aspect-ratio:auto; min-height:150px}
  .ab-f__body{justify-content:center; padding:14px 16px}
  .ab-f__body span{padding-top:8px}
  .ab-f__badge{top:8px; right:8px; width:36px; height:36px} .ab-f__badge .daisy{width:23px; height:23px}
}

/* executive director: portrait (5) fills the height of the text (7) */
.ab-ed__img{min-height:420px}
.ab-ed__img > img{object-position:50% 24%}
.ab-ed__txt{justify-content:center}
.ab-ed h2{margin-bottom:.15em}
.ab-ed__role{font-family:var(--mono); font-size:.8rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin:0 0 18px; font-weight:600}
.ab-ed__txt > p:not(.lede):not(.ab-ed__role){font-size:1.04rem; line-height:1.7}
@media (max-width:900px){.ab-ed__img{min-height:0; aspect-ratio:4/3; max-width:520px}}

/* milestones: a line that fills as you read, and stays filled */
.ab-tlw{position:relative; --p:1}
.ab-tl{position:relative; margin:0; padding:0 0 clamp(26px,3vw,40px); list-style:none}
.ab-tl::before{content:""; position:absolute; left:50%; top:26px; bottom:0; width:4px; margin-left:-2px; background:rgba(21,255,200,.16); border-radius:4px}
.ab-tl::after{content:""; position:absolute; left:50%; top:26px; width:4px; margin-left:-2px; height:calc(var(--p) * (100% - 26px)); background:var(--mint); border-radius:4px; box-shadow:0 0 14px rgba(21,255,200,.55)}
.ab-tl li{position:relative; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:0 clamp(48px,6vw,80px); align-items:start; margin:0 0 clamp(16px,2vw,26px)}
.ab-tl li:last-child{margin-bottom:0}
.ab-tl li::before{content:""; position:absolute; z-index:1; left:50%; top:17px; width:20px; height:20px; margin-left:-10px; border-radius:50%; background:var(--slate); border:4px solid #2c6a70; transition:border-color .4s var(--ease), background .4s var(--ease), box-shadow .4s var(--ease)}
.ab-tl li.lit::before{border-color:var(--mint)}
.ab-tl li.lit.is-key::before{background:var(--mint); box-shadow:0 0 0 7px rgba(21,255,200,.2)}
.ab-tl__y{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2rem,3.8vw,3.3rem); line-height:1; letter-spacing:-.01em; color:var(--mint); text-align:right; padding-top:3px; white-space:nowrap; transition:opacity .5s var(--ease)}
.js .ab-tl li:not(.lit) .ab-tl__y{opacity:.35}
.ab-tl__c{background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:14px; padding:16px 20px 18px; transition:border-color .4s var(--ease), background .4s var(--ease)}
.ab-tl li.lit.is-key .ab-tl__c{border-color:rgba(21,255,200,.55); background:rgba(21,255,200,.07)}
.ab-tl__c h3{font-size:1.2rem; margin:0 0 .3em; color:#fff}
.ab-tl__c p{margin:0; color:rgba(255,255,255,.84); font-size:.98rem; line-height:1.55}
.ab-tl__c a{color:var(--mint); font-weight:700; white-space:nowrap}
.ab-tl li:nth-child(even) .ab-tl__y{order:2; text-align:left}
.ab-tl li:nth-child(even) .ab-tl__c{order:1}
.ab-tl__cap{position:absolute; left:50%; bottom:0; z-index:2; width:52px; height:52px; margin:0 0 -26px -26px; border-radius:50%; display:grid; place-items:center; background:var(--slate); border:4px solid #2c6a70; color:#2c6a70; transition:border-color .5s var(--ease), color .5s var(--ease), box-shadow .5s var(--ease), transform .5s var(--ease)}
.ab-tl__cap .daisy{width:30px; height:30px}
.ab-tlw.done .ab-tl__cap, html:not(.js) .ab-tl__cap{border-color:var(--mint); color:var(--mint); box-shadow:0 0 0 8px rgba(21,255,200,.16); transform:rotate(30deg)}
#milestones .wrap{padding-bottom:26px}
@media (max-width:760px){
  #milestones .section-head--center{align-items:flex-start; text-align:left}
  .ab-tl::before,.ab-tl::after{left:10px}
  .ab-tl li{grid-template-columns:minmax(0,1fr); gap:8px; padding-left:40px}
  .ab-tl li::before{left:10px; top:9px}
  .ab-tl__y,.ab-tl li:nth-child(even) .ab-tl__y{order:0; text-align:left; white-space:normal}
  .ab-tl li:nth-child(even) .ab-tl__c{order:1}
  .ab-tl__cap{left:10px}
}

/* what we do: Vibe Check leads in teal; four photo tiles; two matching tiles for the newest work */
.ab-bento{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ab-vc{grid-column:span 2; grid-row:span 2; position:relative; isolation:isolate; overflow:hidden; display:flex; flex-direction:column; justify-content:space-between; gap:24px; min-height:520px; padding:clamp(24px,3vw,38px); border-radius:var(--r-xl); background:var(--teal); color:#fff; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ab-vc:hover{transform:translateY(-4px); box-shadow:0 30px 54px -30px rgba(22,53,64,.7)}
.ab-vc__mark{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.15rem; color:#fff}
.ab-vc__mark .daisy{width:34px; height:34px; color:var(--mint)}
.ab-vc__txt{max-width:57%}
.ab-vc h3{font-size:clamp(2rem,3.4vw,3rem); font-stretch:120%; line-height:.96; margin:0 0 .4em}
.ab-vc p{margin:0; font-size:1.02rem; line-height:1.55; color:#fff}
.ab-vc .btn{margin-top:20px; white-space:nowrap}
.ab-vc__phone{position:absolute; z-index:-1; right:clamp(18px,2.6vw,38px); top:clamp(64px,6vw,88px); width:min(36%,230px); border-radius:30px; border:8px solid #0b1f25; overflow:hidden; transform:rotate(4deg); box-shadow:0 30px 60px -20px rgba(0,0,0,.55); transition:transform .5s var(--ease)}
.ab-vc:hover .ab-vc__phone{transform:rotate(2deg) translateY(-6px)}
.ab-vc__phone img{width:100%; display:block}
.ab-tile{position:relative; isolation:isolate; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-end; min-height:300px; padding:20px 22px 22px; border-radius:var(--r-xl); background:var(--slate); color:#fff; text-decoration:none}
.ab-tile > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:-2; transition:transform .6s var(--ease)}
.ab-tile::after{content:""; position:absolute; inset:0; z-index:-1; background:linear-gradient(180deg, rgba(22,53,64,0) 14%, rgba(22,53,64,.74) 46%, rgba(22,53,64,.97) 76%)}
.ab-tile:hover > img{transform:scale(1.05)}
.ab-tile .chip{position:absolute; top:16px; left:16px}
.ab-tile h3{font-size:1.32rem; line-height:1.1; margin:0 0 .35em}
.ab-tile p{margin:0; font-size:.95rem; line-height:1.45; color:rgba(255,255,255,.92)}
.ab-new{grid-column:span 2; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,30%); grid-template-rows:auto 1fr; gap:16px clamp(16px,2.2vw,30px); align-items:center; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--aqua); color:var(--slate); border:1px solid var(--line); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.ab-new:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.ab-new__head{display:flex; flex-direction:column; gap:10px; min-width:0}
.ab-new__body{grid-column:1 / -1; align-self:stretch; display:flex; flex-direction:column; gap:10px; min-width:0}
.ab-new .chip{align-self:flex-start; white-space:normal; line-height:1.35}
.ab-new h3{font-size:clamp(1.5rem,2.2vw,1.95rem); margin:0; line-height:1.08; color:var(--logo-teal)}
.ab-new p{margin:0; font-size:.98rem; line-height:1.5}
.ab-new p.ab-new__line{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1.1rem,1.5vw,1.3rem); line-height:1.2; color:var(--slate)}
.ab-new__go{margin-top:auto; padding-top:6px; font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--logo-teal)}
.ab-new__go::after{content:"\\00a0\\2192"}
.ab-new:hover .ab-new__go{text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:4px}
.ab-new__art{min-width:0}
.ab-new__art img{width:100%; border-radius:12px; transform:rotate(2.5deg); box-shadow:0 16px 30px -18px rgba(22,53,64,.6)}
.ab-new__art .hz{transform:rotate(-3deg)}
.ab-loop{position:relative; display:inline-block; padding:0 .12em; margin:0 .3em}
.ab-loop svg{position:absolute; left:-34%; top:-38%; width:168%; height:176%; color:var(--teal); pointer-events:none; overflow:visible}
.ab-loop svg path{stroke-width:2.4}
@supports (grid-template-rows:subgrid){ @media (min-width:961px){
  .ab-bento{grid-template-rows:repeat(2, minmax(150px,1fr) auto auto) auto}
  .ab-vc{grid-row:1 / span 6; min-height:0}
  .ab-tile{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:0; min-height:0}
  .ab-tile h3{grid-row:2; align-self:end}
  .ab-tile p{grid-row:3}
} }
@media (max-width:960px){
  .ab-bento{grid-template-columns:repeat(2,minmax(0,1fr))}
  .ab-vc{grid-row:auto; min-height:440px}
  .ab-tile{min-height:280px}
  .ab-new{grid-column:auto}
}
@media (max-width:620px){
  .ab-bento{grid-template-columns:minmax(0,1fr)}
  .ab-vc{grid-column:auto}
  .ab-vc{min-height:0; padding-bottom:0}
  .ab-vc__txt{max-width:none}
  .ab-vc__phone{position:relative; z-index:0; right:auto; top:auto; align-self:center; width:190px; margin-bottom:-90px; transform:rotate(3deg)}
  .ab-tile{min-height:240px}
}

/* meet the people and the work */
.ab-more{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.ab-more a{display:grid; grid-template-rows:auto 1fr; min-width:0; text-decoration:none; color:var(--slate); background:#fff; border-radius:var(--r-xl); overflow:hidden; transition:transform .2s var(--ease), box-shadow .2s}
.ab-more a:hover{transform:translateY(-4px); box-shadow:var(--shadow)}
.ab-more__img{overflow:hidden; aspect-ratio:16/10; background:var(--slate)}
.ab-more img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.ab-more a:hover img{transform:scale(1.05)}
.ab-more span{padding:18px 20px 20px; display:block}
.ab-more b{display:block; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.25rem; line-height:1.15; color:var(--logo-teal)}
.ab-more b::after{content:"\\00a0\\2192"}
.ab-more small{display:block; color:var(--ink-soft); font-size:.95rem; line-height:1.45; margin-top:6px}
@media (max-width:960px){.ab-more{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.ab-more{grid-template-columns:minmax(0,1fr); gap:12px} .ab-more a{grid-template-columns:116px minmax(0,1fr); grid-template-rows:none} .ab-more__img{aspect-ratio:auto; min-height:112px} .ab-more span{padding:14px 16px; align-self:center}}
'''

ABOUT_JS = '''<script>(function(){
  var el = document.querySelector('.ab-bae'); if(!el) return;
  if(!('IntersectionObserver' in window)){ el.classList.add('in'); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ el.classList.add('in'); io.disconnect(); } }); }, {threshold:.35});
  io.observe(el);
})();
(function(){
  /* the milestone line fills as the list passes the reading line, and never empties again */
  var w = document.querySelector('.ab-tlw'), tl = w && w.querySelector('.ab-tl'); if(!tl) return;
  var items = tl.querySelectorAll('li'), ticking = false, best = 0;
  function upd(){ ticking = false; var mark = window.innerHeight * 0.62, r = tl.getBoundingClientRect();
    var p = Math.min(1, Math.max(0, (mark - r.top - 26) / (r.height - 26))); if(p > best) best = p;
    w.style.setProperty('--p', best.toFixed(4));
    for(var i = 0; i < items.length; i++){ if((items[i].offsetTop + 1) / (r.height - 26) <= best) items[i].classList.add('lit'); }
    if(best >= .999) w.classList.add('done'); }
  window.addEventListener('scroll', function(){ if(!ticking){ ticking = true; requestAnimationFrame(upd); } }, {passive:true});
  window.addEventListener('resize', upd); upd();
})();</script>'''


def about():
    founders = [
        ('Daisy Coleman', '8b5afefa-96d9-4520-9c75-48c07b648528', 'fordaisy.html', '#ForDaisy: remembering Daisy', True),
        ('Jada Smith', 'ddaf06be-f4a9-4097-affa-e0e361779475', 'film-race-rape-culture-resistance.html', 'Watch Jada’s Story', False),
        ('Ella Fairon', 'df8aca6d-675e-4a1c-8258-3c343c189d6d-1', 'film-dating-after-sexual-assault.html', 'Watch Ella in Intimacy & Dating After Sexual Assault', False),
        ('Charlie Coleman', 'caa82df2-41d5-48e8-aa8e-de750350486e', 'film-rape-culture.html', 'Watch Charlie on rape culture and respect', False),
    ]
    fcards = ''.join(
        f'<a class="ab-f reveal" href="{h}"><div class="ab-f__img">{img(im, "Portrait of SafeBAE co-founder " + n)}{'<span class="ab-f__badge">' + daisy() + '</span>' if d else ""}</div>'
        f'<div class="ab-f__body"><small>Co-Founder</small><b>{esc(n)}</b><span>{esc(lk)}</span></div></a>'
        for n, im, h, lk, d in founders)

    tl = [
        ('1999–2016', 'At V-Day', 'As a founding staffer at V-Day, Shael Norris oversees global productions of <i>The Vagina Monologues</i>.', False),
        ('2007', 'Campus Accountability Project', 'Shael launches the Campus Accountability Project to push for stronger prevention and response efforts on college campuses.', False),
        ('2015', 'SafeBAE is founded', 'Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman found SafeBAE with Shael Norris, to bring prevention to middle and high school students.', True),
        ('2020', 'We lose Daisy', 'Co-founder Daisy Coleman passes away on August 4, 2020. More than 700 tribute messages are collected at her memorial service. <a href="fordaisy.html">#ForDaisy</a>', False),
        ('2020–23', 'National School Sexual Violence Climate Survey', 'SafeBAE surveys 849 students in 45 states about safety, support systems and accountability at their schools. <a href="impact.html#climate">See the findings</a>', False),
        ('2023', 'Peer Educator Training evaluated', '1,057 students take part in the Certified Peer Educator Training evaluated in SafeBAE’s 2023 efficacy data. <a href="impact.html#training">See the results</a>', False),
        ('2025', 'Youth Leading', 'The 2025 Annual Report, <i>SafeBAE’s Expanding Network for Change</i>, documents youth leaders creating safer schools across the country. <a href="impact.html#reports">Read the reports</a>', False),
        ('2026', 'Six years #ForDaisy', 'SafeBAE brings the tribute messages for Daisy together in one place, on the #ForDaisy Memorial Tribute Wall.', True),
    ]
    tl_html = ''.join(f'<li class="reveal{" is-key" if k else ""}"><div class="ab-tl__y">{y}</div><div class="ab-tl__c"><h3>{esc(t)}</h3><p>{d}</p></div></li>' for y, t, d, k in tl)

    more = [
        ('Our Team', 'team.html', 'dsc01134', 'Staff, our youth media team and a board that is at least two-thirds youth.', '50% 30%'),
        ('Data & Impact', 'impact.html', 'img-3947', 'Published research, our climate survey, training data and annual reports.', '50% 50%'),
        ('Partners & Press', 'partners-press.html', 'p1002709', 'Podcasts, press coverage and the films we partner on.', '50% 40%'),
        ('#ForDaisy', 'fordaisy.html', 'daisy-coleman', 'Remembering our co-founder, Daisy Coleman.', '70% 20%'),
    ]
    more_html = ''.join(f'<a href="{h}"><div class="ab-more__img">{img(im, "", style="object-position:" + pos)}</div><span><b>{esc(t)}</b><small>{esc(d)}</small></span></a>' for t, h, im, d, pos in more)

    body = f'''
<section class="ab-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap ab-hero__grid">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>About</span></nav>
      <p class="eyebrow">Our mission</p>
      <h1><span>Survivor-</span><span>founded.</span><span><span class="mk">Youth-led.</span></span></h1>
      <p class="lede">SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. We equip young people with the tools to prevent harm, support their peers, and drive generational culture change, strengthening mental health, uplifting youth leadership, and creating safer school communities.</p>
      <div class="btns">{btn('Support our work', 'donate.html', 'mint', arrow=True)}{btn('See all resources', 'resources.html', 'ghost')}</div>
    </div>
    <div class="ab-collage">
      <div class="ab-collage__main">{img('safebae-executive-director-shael-norris', 'SafeBAE co-founders Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman with Executive Director Shael Norris', loading='eager')}</div>
      <div class="ab-collage__sub">{img('founding-members-get-inovlved-page', 'SafeBAE founding members on a film set in front of a #QuitThisShit sign', loading='eager')}</div>
      <span class="sticker">Founded 2015</span>
      <p class="ab-collage__cap">The co-founders with Executive Director Shael Norris</p>
    </div>
  </div>
</section>

<section class="ab-bae" aria-label="What BAE stands for">
  <div class="wrap">
    <div class="ab-bae__row" aria-hidden="true">
      <div><span class="ab-bae__l">B</span><span class="ab-bae__w">Before</span></div>
      <div><span class="ab-bae__l">A</span><span class="ab-bae__w">Anyone</span></div>
      <div><span class="ab-bae__l">E</span><span class="ab-bae__w">Else</span></div>
    </div>
    <p>The “BAE” in SafeBAE stands for Before Anyone Else, because we know prevention has to start early.</p>
  </div>
</section>

<section class="band band--paper" id="story">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Our story</p>
      <h2>We built the education we <span class="mk">never had.</span></h2>
      <p class="lede lede--full">At SafeBAE, we believe rape culture and sexual assault are among the most dangerous and life-altering issues facing young people today, compounded by a growing youth mental health crisis. Rates of sexual violence among youth are higher than any other age group, yet our schools continue to offer little in the way of education or tools to prevent it.</p></div></div>
    <div class="ab-row">
      <div class="ab-story__text">
        <p class="ab-drop">We founded SafeBAE in 2015 because we knew that had to change. Daisy, Ella, and Jada, teen survivors of sexual assault, came together with Daisy’s brother, Charlie, and our Executive Director, Shael, to build something we never had: a way to stop what happened to us from happening to anyone else.</p>
        <p>The idea for SafeBAE began during the filming of the Peabody Award-winning Netflix documentary {a('<i>Audrie &amp; Daisy</i>', 'https://en.wikipedia.org/wiki/Audrie_%26_Daisy', 'link')}. As we shared our stories, one devastating truth became clear: none of us had ever received meaningful education about consent, Title IX, or how to recognize and prevent sexual violence. That knowledge gap was the common thread in our experiences, and it’s exactly what we set out to change.</p>
        <p>We knew the work couldn’t wait until college. It had to begin earlier, in middle and high school, when beliefs about intimacy, boundaries, and safety are just beginning to form. SafeBAE exists to fill that gap: to reach young people before harm happens, and when it does, to make sure they have access to survivor-centered care, community, and lasting support.</p>
      </div>
      <figure class="ab-story__fig fill-img">{img('dsc04560', 'Daisy Coleman and others speaking to an audience from a panel table')}<figcaption>Daisy Coleman speaking on a panel</figcaption></figure>
    </div>
    <figure class="ab-pull reveal"><span class="daisy-art" aria-hidden="true"></span><blockquote>None of us had ever received meaningful education about consent, Title IX, or how to recognize and prevent sexual violence.</blockquote><figcaption>SafeBAE’s founders</figcaption></figure>
  </div>
</section>

<section class="band band--deep ab-began" id="how-we-began">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">How we began</p>
      <h2>Survivors and their families, together.</h2>
      <p class="lede lede--full">These survivors and their families came together during the filming of the Netflix documentary <i>Audrie &amp; Daisy</i> to help prevent what happened to them from happening to anyone else.</p></div></div>
    <div class="ab-row">
      <div>{yt('oKq44GSBSQU', 'SafeBAE overview', label='Watch')}</div>
      <div class="ab-col ab-began__txt">
        <p>Daisy Coleman, Ella Fairon, Jada Smith and Charlie Coleman have bravely spoken out about their sexual assaults, the public sharing of the assaults over social media, the community backlash they received, their schools’ mishandling of their ongoing harassment, and how they have fought for necessary change.</p>
        <ul class="ab-names"><li>{daisy()}Daisy Coleman</li><li>Ella Fairon</li><li>Jada Smith</li><li>Charlie Coleman</li><li>Shael Norris</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="co-founders">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Founded 2015</p><h2>The co-founders</h2></div></div>
    <div class="ab-founders">{fcards}</div>
  </div>
</section>

<section class="band band--paper" id="executive-director">
  <div class="wrap ab-row ab-row--57 ab-ed">
    <div class="ab-ed__img fill-img">{img('82bc8566-88a9-4a05-b13a-f02df3e64af9', 'Portrait of Shael Norris')}</div>
    <div class="ab-col ab-ed__txt">
      <h2>Shael Norris</h2>
      <p class="ab-ed__role">Co-Founder &middot; Executive Director</p>
      <p class="lede">Shael Norris has dedicated her career to ending sexual violence. She is passionate about helping young people become change agents in preventing violence.</p>
      <p>She was a founding staffer of V-Day, overseeing the College and Community Campaigns for 19 years. After decades of work focused on college sexual assault, she sought a grant to establish SafeBAE to focus specifically on younger students. Her three children and her dedication to making schools safer were the driving force behind the creation of SafeBAE.</p>
      <div class="btns" style="margin-top:22px">{btn('Meet the whole team', 'team.html', 'slate', arrow=True)}{btn('Shael on LinkedIn', 'https://www.linkedin.com/in/shaelnorris/', 'ghost')}</div>
    </div>
  </div>
</section>

<section class="band band--slate" id="milestones">
  <div class="wrap">
    <div class="section-head section-head--center"><div><p class="eyebrow">Milestones, 1999–2026</p><h2>From one documentary to a national movement</h2></div></div>
    <div class="ab-tlw"><ol class="ab-tl">{tl_html}</ol><span class="ab-tl__cap" aria-hidden="true">{daisy()}</span></div>
  </div>
</section>

<section class="band band--paper" id="what-we-do">
  <div class="wrap">
    <div class="section-head"><div><h2>Prevention led by young people, in their own schools</h2>
      <p class="lede lede--full muted">Our programs are free for students.</p></div></div>
    <div class="ab-bento">
      <a class="ab-vc" href="vibe-check.html">
        <div class="ab-vc__mark">{daisy()}Vibe Check by SafeBAE</div>
        <div class="ab-vc__txt"><h3>Not sure if you crossed a line?</h3><p>CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they may have crossed a boundary or caused harm. Nothing is stored.</p>
        <span class="btn btn--mint btn--sm">How Vibe Check works<span class="arr" aria-hidden="true">&rarr;</span></span></div>
        <div class="ab-vc__phone">{img('vc-screen', 'The Vibe Check home screen')}</div>
      </a>
      <a class="ab-tile" href="peer-educator.html">{img('1-000383-edited', '', style='object-position:50% 22%')}<span class="chip chip--mint">Free</span><h3>Certified Peer Educator Training</h3><p>Self-paced training that prepares students to lead conversations about consent and healthy relationships at their schools.</p></a>
      <a class="ab-tile" href="clubs.html">{img('clubtabling', '', style='object-position:50% 30%')}<span class="chip">Students</span><h3>SafeBAE Clubs</h3><p>Start, affiliate or restart a chapter and run prevention campaigns with your peers.</p></a>
      <a class="ab-tile" href="360-schools.html">{img('066', '', style='object-position:50% 20%')}<span class="chip">Schools</span><h3>SafeBAE 360° Schools</h3><p>Peer education, a consent curriculum, staff training and policy support in one whole-school model.</p></a>
      <a class="ab-tile" href="library.html">{img('gameon8', '', style='object-position:60% 18%')}<span class="chip">Library</span><h3>Films, podcasts &amp; guides</h3><p>Youth-made films with ready-to-teach guides, plus conversations with SafeBAE leaders.</p></a>
      <a class="ab-new ab-new--ai" href="ai-literacy.html">
        <div class="ab-new__head"><span class="chip chip--slate">New &middot; launches Oct 26–30, 2026</span>
        <h3>SafeBAE <span class="ab-loop">AI<svg viewBox="0 0 120 60" aria-hidden="true"><path d="M14 36C10 20 34 7 62 7c28 0 50 11 50 25 0 15-26 24-54 23C30 54 8 46 10 31 12 19 34 11 66 10" fill="none" stroke="currentColor" stroke-linecap="round"/></svg></span> Literacy Training</h3></div>
        <div class="ab-new__art">{img('ai-illo-hello', '')}</div>
        <div class="ab-new__body"><p>Six free, self-paced modules on how AI works, how feeds shape what we believe, AI and healthy relationships, fake images and sextortion. For high school and college students; anyone 13 or older can take it.</p>
        <span class="ab-new__go">About the training</span></div>
      </a>
      <a class="ab-new ab-new--ch" href="choking-hazard.html">
        <div class="ab-new__head"><span class="chip chip--slate">Campaign</span>
        <h3>Choking Hazard</h3>
        <p class="ab-new__line">“There’s no safe way to choke someone.”</p></div>
        <div class="ab-new__art">{hz_label()}</div>
        <div class="ab-new__body"><p>SafeBAE’s campaign on sexual strangulation, which young people call “choking”: the evidence, myths and facts, signs that need medical care, and free warning posters.</p>
        <span class="ab-new__go">About the campaign</span></div>
      </a>
    </div>
  </div>
</section>

<section class="band band--deep band--tight" id="more">
  <div class="wrap">
    <div class="section-head"><div><h2>Meet the people and the work</h2></div>{btn('Contact us', 'contact.html', 'mint', arrow=True, attrs=' data-act')}</div>
    <div class="ab-more">{more_html}</div>
  </div>
</section>
{give_band()}
'''
    body = body.replace('class="btn btn--mint" data-act', 'class="btn btn--mint section-head__act"')
    page('about.html', 'About SafeBAE · Survivor-founded, youth-led', 'SafeBAE is the only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide. Founded in 2015 by teen survivors.',
         body, active='about', body_class='pg-about', head_extra=css(ABOUT_CSS), scripts=ABOUT_JS)


# =====================================================================
# TEAM
# =====================================================================
TEAM_CSS = '''
/* hero: text (5) beside the clickable mosaic (7), every face cropped to one scale */
.tm-hero{background-color:var(--logo-teal); color:#fff}
.tm-hero .wrap{padding-block:clamp(44px,5.5vw,80px); display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,4vw,56px); align-items:center}
.tm-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.tm-hero .lede{color:rgba(255,255,255,.92); max-width:none; margin:0}
.tm-hint{display:flex; align-items:center; justify-content:flex-end; gap:.7em; margin:14px 0 0; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--aqua)}
.tm-hint::before{content:""; width:26px; height:2px; background:var(--mint); border-radius:2px}
.tm-mosaic{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:clamp(6px,.8vw,12px); margin:0; padding:0; list-style:none}
.tm-mosaic li{margin:0; aspect-ratio:1; min-width:0; animation:sb-rise .7s var(--ease) both}
.tm-mosaic a,.tm-mosaic .tm-tile{position:relative; display:block; width:100%; height:100%; border-radius:14px; overflow:hidden; background:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.tm-mosaic img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.tm-mosaic a::after{content:attr(data-name); position:absolute; left:0; right:0; bottom:0; padding:18px 6px 7px; font-size:.74rem; font-weight:700; line-height:1.15; text-align:center; color:#fff; background:linear-gradient(transparent, rgba(22,53,64,.94)); opacity:0; transform:translateY(6px); transition:opacity .25s, transform .25s var(--ease)}
.tm-mosaic a:hover,.tm-mosaic a:focus-visible{transform:translateY(-3px) scale(1.05); box-shadow:0 0 0 3px var(--mint), 0 18px 30px -16px rgba(0,0,0,.6); z-index:2}
.tm-mosaic a:hover::after,.tm-mosaic a:focus-visible::after{opacity:1; transform:none}
.tm-mosaic a:hover img{transform:scale(1.06)}
.tm-tile{display:grid!important; place-items:center; text-align:center; font-family:var(--display); font-weight:900; font-stretch:122%; line-height:.95}
.tm-tile--daisy{background:var(--mint)!important; color:var(--slate)}
.tm-tile--daisy .daisy{width:62%; height:62%}
.tm-tile--third{background:var(--slate)!important; color:var(--mint); font-size:clamp(1.5rem,2.9vw,2.6rem)}
.tm-tile--year{background:var(--aqua)!important; color:var(--slate); font-size:clamp(1.05rem,1.9vw,1.7rem)}
.tm-tile small{display:block; font-family:var(--mono); font-weight:600; font-stretch:100%; font-size:.7rem; letter-spacing:.06em; line-height:1.2; text-transform:uppercase}
.tm-tile--third small{color:var(--aqua); margin-top:5px}
.tm-tile--year small{margin-bottom:4px}
.tm-mosaic li:nth-child(3n+2){animation-delay:.05s} .tm-mosaic li:nth-child(3n){animation-delay:.1s} .tm-mosaic li:nth-child(n+13){animation-duration:.9s}
@media (max-width:900px){.tm-hero .wrap{grid-template-columns:minmax(0,1fr)}}
@media (max-width:520px){.tm-mosaic{grid-template-columns:repeat(5,minmax(0,1fr))} .tm-mosaic a,.tm-mosaic .tm-tile{border-radius:10px}}
/* arriving from the mosaic: the person you picked is marked */
@keyframes tm-ping{from{box-shadow:0 0 0 0 rgba(21,255,200,.85)} to{box-shadow:0 0 0 18px rgba(21,255,200,0)}}
.tm-card:target{border-color:var(--teal); box-shadow:0 0 0 3px var(--mint), var(--shadow-soft)}
.tm-media .person:target img,.tm-bp:target .tm-bp__pic{outline:4px solid var(--mint); outline-offset:3px; animation:tm-ping 1s var(--ease) 2}
.tm-media .person:target img{outline-color:var(--teal)}

/* leadership: four full rows, portrait (4) beside the bio (8); the full bio opens underneath in two columns */
.tm-lead{display:grid; gap:var(--gap)}
.tm-card{--px:clamp(22px,3.2vw,44px); --py:clamp(22px,2.8vw,34px); position:relative; display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; scroll-margin-top:130px; transition:box-shadow .3s var(--ease), border-color .3s}
.tm-card__img{position:relative; min-height:300px; background:var(--mist)}
.tm-card__img img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 28%}
.tm-card__body{min-width:0; padding:var(--py) var(--px) calc(var(--py) + 58px)}
.tm-card__top{display:flex; align-items:flex-start; justify-content:space-between; gap:12px 20px; margin-bottom:16px}
.tm-card h3{font-size:clamp(1.5rem,2.3vw,2rem); margin:0 0 .25em}
.tm-role{font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:0; line-height:1.4}
.tm-li{flex:none; display:inline-flex; align-items:center; min-height:44px; padding:0 14px; border-radius:10px; border:1.5px solid var(--line); font-family:var(--display); font-stretch:106%; font-weight:800; font-size:.9rem; color:var(--logo-teal); text-decoration:none; transition:background .2s, border-color .2s}
.tm-li::after{content:"\\2197"; margin-left:6px; font-family:var(--body)}
.tm-li:hover{background:var(--aqua); border-color:transparent}
.tm-card p{font-size:1rem; line-height:1.65}
.tm-card__body > p:last-child{margin-bottom:0}
.tm-more{grid-column:1 / -1; position:relative; min-width:0}
.tm-more summary{position:absolute; left:calc(100% / 3 + var(--px)); bottom:calc(100% + var(--py) - 4px); list-style:none; cursor:pointer; display:inline-flex; align-items:center; gap:10px; min-height:44px; font-weight:800; font-family:var(--display); font-stretch:106%; color:var(--logo-teal)}
.tm-more summary::-webkit-details-marker{display:none}
.tm-more summary::before{content:"+"; display:grid; place-items:center; width:28px; height:28px; border-radius:50%; background:var(--aqua); font-size:1.1rem; line-height:1; transition:background .2s}
.tm-more summary:hover::before{background:var(--mint)}
.tm-more[open] summary::before{content:"\\2013"; background:var(--mint)}
.tm-more[open] summary span:first-child{display:none} .tm-more:not([open]) summary span:last-child{display:none}
.tm-more > div{columns:2 300px; column-gap:clamp(28px,4vw,56px); padding:var(--py) var(--px); border-top:1px solid var(--line); background:var(--mist)}
.tm-more > div p:last-child{margin-bottom:0}
@media (max-width:760px){.tm-card{grid-template-columns:minmax(0,1fr)} .tm-card__img{min-height:0; aspect-ratio:5/4} .tm-card__img img{object-position:50% 22%} .tm-more summary{left:var(--px)}}
@media (max-width:480px){.tm-card__top{flex-direction:column}}

/* youth media: seven round portraits on one row */
.tm-media{display:flex; flex-wrap:wrap; justify-content:center; gap:24px 16px}
.tm-media .person{width:calc((100% - 6*16px)/7); min-width:0; scroll-margin-top:130px; text-align:center}
.tm-media .person img{border-radius:50%; margin-bottom:14px; filter:none; box-shadow:0 0 0 4px #fff, var(--shadow-soft)}
.tm-media .person b{font-size:1.05rem}
.tm-media .person small{font-size:.9rem; line-height:1.35; color:var(--slate); margin-top:4px}
@media (max-width:1100px){.tm-media .person{width:calc((100% - 3*16px)/4)}}
@media (max-width:620px){
  .tm-media{display:grid; grid-template-columns:minmax(0,1fr); gap:0; border-top:1px solid rgba(29,65,78,.18)}
  .tm-media .person{width:auto; display:grid; grid-template-columns:64px minmax(0,1fr); grid-template-rows:auto auto; column-gap:16px; align-items:center; padding:12px 0; border-bottom:1px solid rgba(29,65,78,.18); text-align:left}
  .tm-media .person img{grid-row:span 2; width:64px; height:64px; margin:0; box-shadow:0 0 0 3px #fff}
  .tm-media .person b{align-self:end} .tm-media .person small{align-self:start; margin-top:0}
}

/* board: the two-thirds rule as a figure, then eighteen portraits on shared rows */
.tm-third{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch; margin-bottom:clamp(32px,4vw,52px)}
.tm-third .lede{margin:0; color:rgba(255,255,255,.9); align-self:center}
.tm-third__fig{margin:0; display:flex; flex-direction:column; gap:14px; padding:16px 18px 18px; border:1px solid var(--line-dark); border-radius:var(--r-xl); background:rgba(255,255,255,.04)}
.tm-third__bar{flex:1; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px; min-height:66px}
.tm-third__bar span{border-radius:10px; display:flex; align-items:flex-end; padding:10px 12px; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.tm-third__bar span:nth-child(-n+2){background:var(--mint); color:var(--slate)}
.tm-third__bar span:nth-child(3){border:2px dashed rgba(209,254,255,.45)}
.tm-third__big{display:flex; align-items:center; gap:14px; margin:0}
.tm-third__big b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(2.6rem,4.4vw,3.6rem); line-height:.9; color:var(--mint)}
.tm-third__big span{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:clamp(1rem,1.3vw,1.14rem); line-height:1.2}
@media (max-width:900px){.tm-third{grid-template-columns:minmax(0,1fr)}}
.tm-board{--rg:clamp(28px,3vw,40px); display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:0 16px; margin-bottom:calc(-1 * var(--rg))}
.tm-bp{display:flex; flex-direction:column; min-width:0; padding-bottom:var(--rg); scroll-margin-top:130px}
.tm-bp__pic{display:block; aspect-ratio:1; border-radius:14px; overflow:hidden; background:var(--slate-deep); margin-bottom:12px}
.tm-bp__pic img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
a.tm-bp__pic:hover img{transform:scale(1.05)}
.tm-bp b{display:block; font-family:var(--display); font-stretch:104%; font-size:1.04rem; line-height:1.2; color:#fff}
.tm-board .tm-bp b a{color:#fff; text-decoration:none}
.tm-board .tm-bp b a:hover{color:var(--mint); text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:3px}
.tm-bp small{display:block; font-size:.9rem; line-height:1.3; color:var(--aqua); margin-top:4px}
.tm-board .tm-x{display:block; margin-top:4px; padding-block:5px; font-size:.9rem; line-height:1.3; font-weight:700; color:var(--mint); text-decoration:none}
.tm-board .tm-x:hover{text-decoration:underline}
@supports (grid-template-rows:subgrid){ .tm-bp{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:0; align-content:start} }
@media (max-width:900px){.tm-board{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:520px){.tm-board{grid-template-columns:repeat(2,minmax(0,1fr)); gap:0 14px}}

/* ways to join */
.tm-join{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.tm-join a{display:flex; flex-direction:column; gap:8px; padding:var(--pad-card); border-radius:var(--r-xl); text-decoration:none; color:var(--slate); background:#fff; border:1px solid var(--line); transition:transform .2s var(--ease), box-shadow .2s}
.tm-join a:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.tm-join a b{font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.3rem; line-height:1.15; color:var(--logo-teal)}
.tm-join a b::after{content:"\\00a0\\2192"}
.tm-join a span{color:var(--ink-soft); font-size:.98rem; line-height:1.5}
@media (max-width:860px){.tm-join{grid-template-columns:minmax(0,1fr)}}
'''

LEADERS = [
    dict(name='Shael Norris', role='Co-Founder & Executive Director', img='82bc8566-88a9-4a05-b13a-f02df3e64af9', link='https://www.linkedin.com/in/shaelnorris/', id='shael-norris',
         lead=['Shael Norris is the Founding Executive Director of SafeBAE, the only national, survivor-founded and youth-led organization in the U.S. dedicated to preventing sexual violence among teens. A lifelong advocate, she began her career as a founding staffer at V-Day, where she oversaw global productions of <i>The Vagina Monologues</i> from 1999 to 2016.'],
         more=['In 2007, she launched the Campus Accountability Project to push for stronger prevention and response efforts on college campuses. Recognizing the need for early, youth-led intervention, Shael founded SafeBAE in 2015 in partnership with Daisy and Charlie Coleman, Ella Fairon, and Jada Smith. She continues to lead the organization’s national efforts in youth leadership, consent education, and mental health advocacy.']),
    dict(name='Drew Davis', role='Director of Strategic Initiatives', img='4cec0cfb-2d16-47d1-9aaa-8b797dd2ae15', link='https://www.linkedin.com/in/drewthomasdavis/', id='drew-davis',
         lead=['Drew Davis is an applied researcher and development strategist dedicated to advancing survivor justice and dismantling systems of harm through youth-led, community-driven approaches. As Director of Strategic Initiatives at SafeBAE, Drew leads development and organizational strategy, building the infrastructure that sustains youth-led programs and expands the organization’s national impact.'],
         more=['He oversees major initiatives in prevention education and youth development, with a focus on rigorous data collection, program evaluation, and long-term sustainability, ensuring all initiatives are research-informed and responsive to young people’s needs.',
               'Drew holds a Master of Public Health and a Master of Public Affairs from Brown University, where he concentrated in Black Feminist Health Science Studies, and a B.A. in Individualized Studies and Women’s, Gender, and Sexuality Studies, along with a Graduate Certificate in WGS, from Miami University of Ohio.',
               'He is a fellow of the Vermont Network’s Amplify Leadership Lab and serves as an advisor to The Every Voice Coalition, shaping state policy and strengthening support systems for survivors nationwide. Drew has also held roles with Know Your IX, Visible &amp; Resilient, and the National Coalition for Sexual Health. His work on survivor justice and Title IX has been featured in <i>USA Today</i>, <i>YES! Magazine</i>, <i>Inside Higher Ed</i>, and <i>Governing</i>.']),
    dict(name='Aela Mansmann', role='Director of Programs', img='90fc1a20-9104-456b-a0ef-df7f495a3f3f', link='https://www.linkedin.com/in/aela-mansmann-a14706180/', id='aela-mansmann',
         lead=['Aela Mansmann is the Director of Programs and Outreach at SafeBAE, where she leads national prevention initiatives, strengthens partnerships with schools across the country, and mentors young leaders to create lasting culture change. With nearly a decade of experience in youth advocacy and nonprofit leadership, she brings a track record of building sustainable initiatives that amplify student voices.'],
         more=['At SafeBAE, Aela has expanded digital resources reaching more than 86,000 students, spearheaded peer-led prevention campaigns, and coordinated programming that embeds consent education into school communities nationwide. A two-term Student Body President at Manhattanville University, she revitalized and expanded the Student Government Association, fostering a culture of inclusion, representation, and student-led problem solving on campus.',
               'Her work is grounded in the belief that education, empathy, and grassroots empowerment are the foundation of safer, more equitable communities. She is dedicated to giving young people the tools, platforms, and confidence to lead the change they wish to see.']),
    dict(name='Val Odiembo', role='Youth Engagement Manager', img='e281116a-608f-4812-8e62-40567538668e', link='https://www.linkedin.com/in/vespr000/', id='val-odiembo',
         lead=['Val Odiembo is a first-year student at Rhode Island College, pursuing a double major in Nursing and Criminal Justice with a passion for public health and violence prevention. A longtime SafeBAE leader, Val is a SafeBAE Youth Board Member and serves as SafeBAE’s Youth Engagement Manager.'],
         more=['In that role she supports the Director of Programs in strengthening youth leadership, expanding student involvement, and supporting SafeBAE club leaders across the country. Val has led SafeBAE clubs at both the Rhode Island Nurses Institute and RIC, presented at statewide health education conferences, and facilitated workshops through the Rhode Island Community Justice Program. Currently, she is organizing a training seminar for Sexual Assault Nurse Examiners (SANEs), deepening her commitment to survivor-centered care and systems change.']),
]

MEDIA = [
    ('Bailey Brewer', 'Community Engagement Coordinator', 'b-brewerheadshot'),
    ('Miwako Miki', 'Social Media Coordinator', 'composite'),
    ('Inanna Balkin', 'Staff Writer', '72295171-981d-4bfa-925b-5d7b6ec8e535-1-201-a-1-1'),
    ('Mikayla Murphy', 'Social Media', 'dsc02351-1'),
    ('Ava Legeay', 'Social Media', 'img-7608-1'),
    ('Isa Ocejo', 'Social Media', 'img-3246'),
    ('Jack Quinn', 'Social Media', 'img-0956'),
]

BOARD = [
    ('Justine Wentzell-Chang', 'Co-Chair', 'justine-wentzell-chang', 'https://www.linkedin.com/in/justine-wentzell-chang/', None),
    ('Aela Mansmann', 'Co-Chair', '90fc1a20-9104-456b-a0ef-df7f495a3f3f', 'https://www.linkedin.com/in/aela-mansmann-a14706180/', None),
    ('Len Eschweiler', 'Co-Chair', 'b71bf627-c760-48ca-9aae-6c43b1867b9c', 'https://www.linkedin.com/in/leneschweiler/', None),
    ('Michelle Hope', '', '59178f58-dc22-4d34-80cf-5240a08d9304-1', 'https://www.linkedin.com/in/missmichellehope/', None),
    ('Dorie McNamara', '', 'b0f0eb55-23cd-4dac-89eb-aff4bbc3ed3a', None, None),
    ('Joy Gorman Wettels', '', '36ff738f-68ee-4dee-8f50-1c70b4b9b011-1', 'https://www.linkedin.com/in/joy-gorman-wettels-3556a18b/', None),
    ('Arturo Rosado Taveras', '', '6585feed-8f00-43b2-83b0-5504d57e223c-1', 'https://www.linkedin.com/in/arturo-rosado-9455a82a1/', None),
    ('Theo Hutt', '', 'b9338b3f-75f1-4457-ab2c-efded5be05f0-1', 'https://www.linkedin.com/in/theo-hutt-2401a8125/', ('Watch Theo’s story', 'film-sexual-assault-of-men.html')),
    ('Apollo Knapp', '', 'apollo-knapp-headshot', None, None),
    ('Torrey DeVitto', '', '35d9e43e-01d6-4059-a4d5-1f8442813ee7-1', 'https://www.imdb.com/name/nm1722914/', ('On Celebrity Name That Tune', 'partners-press.html#torrey')),
    ('Hector Jaco', '', '7bb97e5a-79d6-47d3-b1c4-942e51144247-1', 'https://www.linkedin.com/in/hector-jaco-b51b51283/', None),
    ('Ari Zeitlin', '', 'ariz', 'https://www.linkedin.com/in/ari-zeitlin/', None),
    ('Joyce Onana', '', 'unnamed', 'https://www.linkedin.com/in/joyce-onana-mfege-/', None),
    ('Vanessa Boudewyns', '', 'vanessa-headshot-vanessa-boudewyns', 'https://www.linkedin.com/in/vboudewyns/', None),
    ('Samar Rafiqzad', '', '9ea5aa47-ab94-4190-aa9e-e4aa869eafa8-1', 'https://www.linkedin.com/in/samarrafiqzad/', None),
    ('Lisa Hoopis', '', '1517523645026', 'https://www.linkedin.com/in/lisa-hoopis-0093a343/', None),
    ('Val Odiembo', 'Youth Board Member', 'e281116a-608f-4812-8e62-40567538668e', 'https://www.linkedin.com/in/vespr000/', None),
    ('Will Rivera', '', '1735567805828', 'https://www.linkedin.com/in/riverawd/', None),
]


def hs(name):
    """Square headshot cropped around the face at one scale (made by work/about_headshots.py)."""
    return 'hs-' + slugify(name)


def team():
    # mosaic: every person once, linking to their entry
    faces, seen = [], set()
    for L in LEADERS:
        faces.append((L['name'], '#' + L['id'])); seen.add(L['name'])
    for n, r, im in MEDIA:
        faces.append((n, '#' + slugify(n)))
    for n, r, im, lk, x in BOARD:
        if n not in seen:
            faces.append((n, '#board-' + slugify(n)))
    tiles = [f'<li><a href="{h}" data-name="{esc(n)}" aria-label="{esc(n)}">{img(hs(n), "", loading="eager")}</a></li>' for n, h in faces]
    brand = {4: f'<li aria-hidden="true"><span class="tm-tile tm-tile--daisy">{daisy()}</span></li>',
             14: '<li aria-hidden="true"><span class="tm-tile tm-tile--third"><span>⅔<small>youth<br>board</small></span></span></li>',
             25: '<li aria-hidden="true"><span class="tm-tile tm-tile--year"><span><small>Since</small>2015</span></span></li>'}
    for i in sorted(brand):
        tiles.insert(i, brand[i])
    face_html = ''.join(tiles)

    lead_html = ''
    for L in LEADERS:
        lead = ''.join(f'<p>{p}</p>' for p in L['lead'])
        more = ''.join(f'<p>{p}</p>' for p in L['more'])
        lead_html += f'''<article class="tm-card" id="{L['id']}">
  <div class="tm-card__img">{img('ld-' + L['id'], 'Portrait of ' + L['name'])}</div>
  <div class="tm-card__body">
    <div class="tm-card__top"><div><h3>{esc(L['name'])}</h3><p class="tm-role">{esc(L['role'])}</p></div><a class="tm-li" href="{L['link']}" target="_blank" rel="noopener" aria-label="{esc(L['name'])} on LinkedIn">LinkedIn</a></div>
    {lead}
  </div>
  <details class="tm-more"><summary><span>Read full bio</span><span>Show less</span></summary><div>{more}</div></details>
</article>'''

    media_html = ''.join(f'<div class="person" id="{slugify(n)}">{img(hs(n), "Portrait of " + n)}<b>{esc(n)}</b><small>{esc(r)}</small></div>' for n, r, im in MEDIA)

    board_html = ''
    for n, r, im, lk, x in BOARD:
        pic = img(hs(n), 'Portrait of ' + n)
        role = f'<small>{esc(r)}</small>' if r else '<small>Board Member</small>'
        if lk:
            pic = f'<a class="tm-bp__pic" href="{lk}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">{pic}</a>'
            name = f'<b><a href="{lk}" target="_blank" rel="noopener">{esc(n)}</a></b>'
        else:
            pic = f'<span class="tm-bp__pic">{pic}</span>'
            name = f'<b>{esc(n)}</b>'
        extra = f'<a class="tm-x" href="{x[1]}">{esc(x[0])} &rarr;</a>' if x else ''
        board_html += f'<div class="tm-bp" id="board-{slugify(n)}">{pic}{name}{role}{extra}</div>'

    body = f'''
<section class="tm-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Our Team</span></nav>
      <p class="eyebrow">Youth leaders, staff &amp; board</p>
      <h1>Our <span class="mk">team</span></h1>
      <p class="lede">SafeBAE is led by a committed team of youth leaders, staff, and board members who bring together lived experience, professional expertise, and a shared dedication to ending sexual violence. As a survivor-founded, youth-led organization, we center the leadership of young people while fostering cross-generational collaboration and advancing cultural change.</p>
    </div>
    <div><ul class="tm-mosaic" aria-label="Jump to a team member">{face_html}</ul>
      <p class="tm-hint" aria-hidden="true">Select a face to find that person below</p></div>
  </div>
</section>

<section class="band band--paper" id="leadership">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Leadership team</p><h2>The staff who run SafeBAE day to day</h2>
      <p class="lede lede--full muted">Our team includes students, educators, advocates, and professionals with backgrounds in public health, education, policy, research, media, and communications. Together, we work to create communities where safety and consent come first, before anything else.</p></div></div>
    <div class="tm-lead">{lead_html}</div>
  </div>
</section>

<section class="band band--aqua" id="youth-media">
  <div class="wrap">
    <div class="section-head"><div><h2>Youth media &amp; communications team</h2></div><a class="btn btn--slate section-head__act" href="https://www.instagram.com/safe_bae/" target="_blank" rel="noopener">Follow @safe_bae<span aria-hidden="true">&nbsp;&#8599;</span></a></div>
    <div class="tm-media">{media_html}</div>
  </div>
</section>

<section class="band band--slate" id="board">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Board of Directors</p><h2>A board that answers to young people</h2></div></div>
    <div class="tm-third">
      <p class="lede">SafeBAE’s Board is intentionally composed of at least ⅔ youth, reflecting our deep commitment to youth leadership. This structure ensures that SafeBAE remains accountable to the young people leading this work, with youth playing a central role in all aspects of our governance, strategic planning, and decision-making.</p>
      <figure class="tm-third__fig" aria-hidden="true">
        <div class="tm-third__bar"><span>Youth</span><span>Youth</span><span>&nbsp;</span></div>
        <figcaption class="tm-third__big"><b>⅔</b><span>of the board, at minimum, is youth</span></figcaption>
      </figure>
    </div>
    <div class="tm-board">{board_html}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>Ways to join this work</h2></div></div>
    <div class="tm-join">
      <a href="peer-educator.html"><b>Become a Peer Educator</b><span>Free, self-paced certification for high school students.</span></a>
      <a href="clubs.html"><b>Lead a SafeBAE club</b><span>Start, affiliate or restart a chapter at your school.</span></a>
      <a href="contact.html"><b>Contact the team</b><span>Reach our staff about programs, press or partnerships.</span></a>
    </div>
  </div>
</section>
{give_band()}
'''
    page('team.html', 'Our Team · SafeBAE', 'Meet SafeBAE’s leadership team, youth media team and board of directors, a team of youth leaders and professionals working to end sexual violence.',
         body, active='about', body_class='pg-team', head_extra=css(TEAM_CSS))


# =====================================================================
# IMPACT
# =====================================================================
IMPACT_CSS = '''
/* hero: text (7), photo with a data card (5), then three count-up figures on shared rows */
.im-hero{background-color:var(--slate-deep); color:#fff}
.im-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(40px,5vw,64px)}
.im-hero__top{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center}
.im-hero h1{font-size:clamp(2.3rem,4.4vw,4rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.im-hero .lede{color:rgba(255,255,255,.9); max-width:none; margin:0}
.im-hero .eyebrow{color:var(--mint)}
.im-fig{position:relative; margin:0 0 26px; animation:sb-rise-r 1s .1s var(--ease) both}
.im-fig > img{width:100%; aspect-ratio:4/3; object-fit:cover; object-position:50% 40%; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7)}
.im-fig .sticker{position:absolute; left:-12px; top:18px}
.im-datacard{position:absolute; right:-14px; bottom:-26px; width:min(300px,72%); background:#fff; color:var(--slate); border-radius:16px; padding:16px 18px; box-shadow:var(--shadow-soft), 0 10px 30px -12px rgba(0,0,0,.45)}
.im-datacard small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.im-datacard b{display:block; font-family:var(--display); font-weight:900; font-stretch:120%; font-size:2.5rem; line-height:1; margin:5px 0 3px; color:var(--slate)}
.im-datacard span{display:block; font-size:.9rem; font-weight:600; line-height:1.35}
.im-datacard i{display:block; height:10px; border-radius:5px; background:var(--mist); margin-top:10px; overflow:hidden}
.im-datacard i::before{content:""; display:block; height:100%; width:70%; background:var(--coral); border-radius:0 5px 5px 0}
@media (max-width:900px){.im-hero__top{grid-template-columns:minmax(0,1fr)} .im-fig{max-width:560px; margin-bottom:40px} .im-datacard{right:8px}}
.im-kpis{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0 var(--gap); margin-top:clamp(30px,3.4vw,46px)}
.im-kpi{display:flex; flex-direction:column; min-width:0; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); border-radius:var(--r-xl); padding:22px 24px}
.im-kpi b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(2.6rem,4.8vw,4.2rem); line-height:.95; color:var(--mint); letter-spacing:-.02em; font-variant-numeric:tabular-nums}
.im-kpi span{display:block; margin-top:10px; font-weight:600; font-size:1rem; color:rgba(255,255,255,.92); line-height:1.4}
.im-kpi small{display:block; margin-top:auto; padding-top:12px; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@supports (grid-template-rows:subgrid){ .im-kpi{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:0} .im-kpi small{margin-top:0; align-self:end} }
@media (max-width:760px){.im-kpis{grid-template-columns:minmax(0,1fr); gap:12px} .im-kpi{display:flex; grid-row:auto} .im-kpi small{align-self:auto}}

/* text columns in the 5/7 rows */
.im-txt > p:not(.eyebrow):not(.lede){font-size:1.04rem; line-height:1.7}
.im-txt > .lede{margin-bottom:1em}
.im-txt .eyebrow{align-self:flex-start}
.im-txt .ab-floor{padding-top:10px}
.im-note{margin:10px 0 0; font-size:.9rem}
.im-acts{display:inline-grid; gap:10px}
.im-acts .btn{width:100%}

/* published research */
.im-paper__img{position:relative; margin:0 0 clamp(26px,3vw,36px)}
.im-paper__img img{width:100%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.im-paper__img .sticker{position:absolute; left:-10px; bottom:-14px}
.im-authors{margin:0; padding:0; list-style:none; border-top:1px solid var(--line)}
.im-authors li{margin:0; display:grid; grid-template-columns:12px minmax(0,1fr); gap:2px 14px; align-items:start; padding:12px 0; border-bottom:1px solid var(--line)}
.im-authors li::before{content:""; grid-row:span 2; width:12px; height:12px; margin-top:5px; border-radius:50%; background:var(--mint); box-shadow:0 0 0 3px var(--aqua)}
.im-authors b{font-family:var(--display); font-stretch:106%; font-size:1.08rem; line-height:1.2; color:var(--logo-teal)}
.im-authors small{color:var(--ink-soft); font-size:.92rem; line-height:1.35}
.im-paper .audio{margin-top:22px}
.im-paper .eyebrow{margin-bottom:.7rem}

/* survey facts beside a section head */
.im-meta{display:flex; flex-wrap:wrap; gap:8px; margin:4px 0 22px}
.im-meta span{font-family:var(--mono); font-size:.76rem; letter-spacing:.06em; text-transform:uppercase; font-weight:600; padding:8px 12px; border-radius:8px; border:1.5px solid rgba(209,254,255,.5); color:var(--aqua)}

/* the charts: one panel, one axis, source underneath */
.im-chart{--vw:clamp(92px,8.6vw,124px); --bar-card:rgba(255,255,255,.05); --bar-line:var(--line-dark); --bar-num:#fff; --bar-k:var(--aqua); --bar-track:rgba(255,255,255,.12); --bar-tick:rgba(255,255,255,.55); --bar-fill:var(--coral); --bar-soft:rgba(255,255,255,.72);
  margin:0; min-width:0; border-radius:var(--r-xl); border:1px solid var(--bar-line); background:var(--bar-card); padding:clamp(18px,2.2vw,28px) clamp(18px,2.4vw,30px)}
.im-light{--vw:clamp(104px,10.6vw,152px); --bar-card:#fff; --bar-line:var(--line); --bar-num:var(--logo-teal); --bar-k:var(--logo-teal); --bar-track:var(--mist); --bar-tick:rgba(29,65,78,.42); --bar-fill:var(--teal); --bar-soft:var(--ink-soft); box-shadow:var(--shadow-soft)}
.im-chart__head{display:flex; justify-content:space-between; align-items:center; gap:10px 20px; flex-wrap:wrap; padding-bottom:14px; border-bottom:1px solid var(--bar-line)}
.im-chart__head b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.15rem; line-height:1.2}
.im-chart__head > span{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--bar-k)}
.im-chart__head .tabs{margin:0}
.im-chart__head .tab{min-height:44px}
.im-bars{list-style:none; margin:0; padding:0}
.im-bars li{position:relative; margin:0; display:grid; grid-template-columns:var(--vw) minmax(0,1fr); gap:7px 18px; align-items:center; padding:12px 0 13px; border-bottom:1px solid var(--bar-line)}
.im-bars__v{grid-row:span 2; font-family:var(--display); font-weight:900; font-stretch:118%; font-size:clamp(1.9rem,3vw,2.6rem); white-space:nowrap; line-height:1; letter-spacing:-.02em; color:var(--bar-num); font-variant-numeric:tabular-nums}
.im-bars__t{font-weight:600; font-size:.98rem; line-height:1.4}
.im-bars__k{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--bar-k); margin-bottom:2px}
.im-bars__track{height:14px; border-radius:7px; overflow:hidden; background:var(--bar-track)}
.im-bars li::after{content:""; position:absolute; left:calc(var(--vw) + 18px + (100% - var(--vw) - 18px) / 2 - 1px); bottom:9px; width:2px; height:22px; border-radius:2px; background:var(--bar-tick)}
.im-bars__track i{display:block; height:100%; width:calc(var(--v) * 1%); background:var(--bar-fill); border-radius:0 7px 7px 0; transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.js .im-bars:not(.in) .im-bars__track i{width:0}
.im-bars li:nth-child(2) i{transition-delay:.08s} .im-bars li:nth-child(3) i{transition-delay:.16s} .im-bars li:nth-child(4) i{transition-delay:.24s} .im-bars li:nth-child(5) i{transition-delay:.32s} .im-bars li:nth-child(6) i{transition-delay:.4s} .im-bars li:nth-child(7) i{transition-delay:.48s}
.im-scale{display:grid; grid-template-columns:1fr auto 1fr; font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; color:var(--bar-k); margin:9px 0 0 calc(var(--vw) + 18px)}
.im-scale span:last-child{text-align:right}
.im-chart__src{margin:16px 0 0; font-size:.9rem; line-height:1.45; color:var(--bar-soft)}
.im-chart__src b{color:var(--bar-num); font-weight:700}
.im-train{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:18px 0 0}
.im-train div{background:var(--mist); border-radius:14px; padding:16px 18px}
.im-train b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(1.8rem,2.8vw,2.4rem); line-height:1; color:var(--logo-teal)}
.im-train span{display:block; margin-top:6px; font-size:.95rem; font-weight:600; color:var(--slate); line-height:1.35}
@media (max-width:560px){.im-chart{--vw:84px} .im-train{grid-template-columns:minmax(0,1fr)} .im-meta span{font-size:.72rem; padding:7px 10px}}

/* what students said: the shorter quote takes 5, the longer one 7 */
.im-quotes{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap); margin-top:clamp(30px,4vw,48px)}
.im-q{margin:0; min-width:0; background:var(--slate) var(--grain); color:#fff; border-radius:var(--r-xl); padding:var(--pad-card); display:flex; flex-direction:column}
.im-q p{font-family:var(--display); font-weight:700; font-stretch:103%; font-size:clamp(1.05rem,1.45vw,1.22rem); line-height:1.42; margin:0}
.im-q p::before{content:"\\201C"; display:block; font-size:3.4em; line-height:.6; color:var(--mint); font-stretch:125%; margin-bottom:.12em}
.im-q figcaption{margin-top:auto; padding-top:16px; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua)}
@media (max-width:860px){.im-quotes{grid-template-columns:minmax(0,1fr)}}

/* film */
.im-film__txt{justify-content:center}
.im-film__txt .lede{color:rgba(255,255,255,.9)}

/* reports: this year's as the feature, past years on a shelf, earlier survey data as three cards */
.im-annual{display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr); gap:clamp(24px,4vw,56px); align-items:center; background:var(--teal); color:#fff; border-radius:var(--r-xl); padding:clamp(28px,4vw,52px); position:relative; overflow:hidden}
.im-annual__cover{position:relative; overflow:hidden; aspect-ratio:8.5/11; max-width:300px; width:100%; margin-inline:auto; background:var(--mint); color:var(--slate); border-radius:8px; padding:24px 22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 30px 60px -20px rgba(0,0,0,.5); transform:rotate(-3deg); transition:transform .5s var(--ease)}
.im-annual:hover .im-annual__cover{transform:rotate(-1deg) translateY(-4px)}
.im-annual__cover .daisy-art{position:absolute; right:-34%; top:9%; width:118%; color:var(--slate); opacity:.22}
.im-annual__cover > :not(.daisy-art){position:relative}
.im-annual__cover b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3.4rem,6.4vw,5rem); line-height:.85; letter-spacing:-.03em; margin-top:auto}
.im-annual__cover span{font-family:var(--display); font-weight:800; font-stretch:110%; text-transform:uppercase; font-size:1.2rem; line-height:1.05; margin-top:10px}
.im-annual__cover small{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.im-annual .eyebrow{color:#fff}
.im-annual h3{font-size:clamp(1.7rem,3vw,2.6rem); margin:.1em 0 .4em}
.im-annual p{color:#fff; font-size:1.06rem; line-height:1.65}
@media (max-width:1180px){.im-annual .btns{display:inline-grid; gap:10px} .im-annual .btns .btn{width:100%}}
@media (max-width:760px){.im-annual{grid-template-columns:minmax(0,1fr)} .im-annual__cover{max-width:210px; margin-inline:0}}
.im-sub{margin:clamp(40px,5vw,64px) 0 clamp(20px,2.4vw,30px); font-size:var(--fs-h3)}
h2.im-sub{font-size:var(--fs-h2)}
.im-shelf{display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:12px; align-items:end}
.im-book{display:flex; flex-direction:column; justify-content:space-between; text-decoration:none; color:#fff; background:var(--slate); border-radius:8px 8px 3px 3px; padding:16px 14px; min-height:232px; position:relative; transition:transform .25s var(--ease); box-shadow:inset -7px 0 0 rgba(0,0,0,.16), inset 3px 0 0 rgba(255,255,255,.08)}
.im-book:hover,.im-book:focus-visible{transform:translateY(-10px)}
.im-book b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(1.7rem,2.7vw,2.4rem); line-height:.9; writing-mode:vertical-rl; transform:rotate(180deg); align-self:flex-start; letter-spacing:.02em; color:var(--mint)}
.im-book span{font-family:var(--mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; line-height:1.4; font-weight:600}
.im-book span::after{content:" \\2193"}
.im-book:nth-child(odd){background:var(--logo-teal)}
.im-book:nth-child(1){min-height:252px} .im-book:nth-child(2){min-height:236px} .im-book:nth-child(3){min-height:264px} .im-book:nth-child(4){min-height:240px} .im-book:nth-child(5){min-height:256px} .im-book:nth-child(6){min-height:232px} .im-book:nth-child(7){min-height:248px}
.im-shelf-base{height:12px; border-radius:0 0 6px 6px; background:var(--gray); box-shadow:0 14px 20px -14px rgba(22,53,64,.5)}
@media (max-width:960px){.im-shelf{grid-template-columns:repeat(4,minmax(0,1fr)); gap:18px 10px} .im-book{min-height:190px!important; border-bottom:8px solid var(--gray); border-radius:8px 8px 0 0} .im-shelf-base{display:none}}
@media (max-width:520px){.im-shelf{grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px} .im-book{min-height:0!important; flex-direction:row; align-items:center; gap:10px; padding:14px; border-bottom:0; border-radius:10px} .im-book b{writing-mode:horizontal-tb; transform:none; font-size:1.6rem; align-self:center} .im-book span{text-align:right} .im-book:last-child{grid-column:1 / -1}}
.im-docs{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:0 var(--gap)}
.im-doc{display:flex; flex-direction:column; gap:8px; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:#fff; border:1px solid var(--line); color:var(--slate); text-decoration:none; transition:transform .2s var(--ease), box-shadow .2s}
.im-doc:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.im-doc .chip{align-self:flex-start; justify-self:start}
.im-doc b{font-family:var(--display); font-weight:800; font-stretch:106%; font-size:1.25rem; line-height:1.18; color:var(--logo-teal)}
.im-doc b::after{content:"\\00a0\\2197"; font-family:var(--body); font-weight:600; font-size:.8em}
.im-doc small{font-size:.96rem; line-height:1.5; color:var(--ink-soft)}
@supports (grid-template-rows:subgrid){ .im-doc{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:8px} }
@media (max-width:860px){.im-docs{grid-template-columns:minmax(0,1fr); gap:12px} .im-doc{display:flex; grid-row:auto}}
'''

IMPACT_JS = '''<script>(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce) document.querySelectorAll('[data-count]').forEach(function(el, k){
    var n = +el.getAttribute('data-count'), pre = el.getAttribute('data-prefix') || '', suf = el.getAttribute('data-suffix') || '', t0 = null, dur = 1400 + k * 150;
    function fmt(v){ return pre + Math.round(v).toLocaleString('en-US') + suf; }
    el.textContent = fmt(0);
    function step(t){ if(t0 === null) t0 = t; var q = Math.min(1, (t - t0) / dur); el.textContent = fmt(n * (1 - Math.pow(1 - q, 3))); if(q < 1) requestAnimationFrame(step); }
    setTimeout(function(){ requestAnimationFrame(step); }, 350);
  });
})();
(function(){
  var els = document.querySelectorAll('.im-bars'); if(!els.length) return;
  if(!('IntersectionObserver' in window)){ els.forEach(function(e){ e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {threshold:.2});
  els.forEach(function(e){ io.observe(e); });
})();</script>'''


def bars(items):
    li = ''.join(f'<li style="--v:{v}" title="{esc(lbl)}: {esc(shown)}"><span class="im-bars__v">{esc(shown)}</span><span class="im-bars__t"><span class="im-bars__k">{esc(k)}</span>{esc(t)}</span><span class="im-bars__track" aria-hidden="true"><i></i></span></li>'
                 for v, shown, k, t, lbl in items)
    return f'<ul class="im-bars">{li}</ul><div class="im-scale" aria-hidden="true"><span>0%</span><span>50%</span><span>100%</span></div>'


def impact():
    climate = [
        (53, '53%', 'Sexual violence', 'Agreed that sexual violence was a serious problem at their school', 'Sexual violence'),
        (59, '59%', 'Rape culture', 'Agreed that when students reported being assaulted, their peers didn’t believe them', 'Rape culture'),
        (33.3, '1/3', 'Support', 'Of students agreed that school staff didn’t help students who’d been assaulted', 'One third of students'),
        (56, '56%', 'Reporting', 'Agreed their school didn’t adequately teach them where or how to report sexual violence', 'Reporting'),
        (70, '70%', 'Title IX', 'Agreed that their school didn’t adequately teach their Title IX rights', 'Title IX'),
        (57, '57%', 'Bystander intervention', 'Agreed that their school didn’t adequately teach bystander intervention', 'Bystander intervention'),
        (20, '20%', 'Dress code', 'Agreed that their school’s dress code was applied unfairly', 'Dress code'),
    ]
    know = [
        (81, '+81%', 'Title IX', 'Increase in understanding Title IX rights', 'Title IX rights'),
        (66, '+66%', 'Bystander intervention', 'Increase in understanding how to be an active bystander', 'Active bystander'),
        (56, '+56%', 'Healing', 'Increase in understanding healing options after experiencing sexual violence', 'Healing options'),
        (43, '+43%', 'Reporting', 'Increase in understanding how to report sexual violence', 'Reporting'),
        (39, '+39%', 'Supporting a peer', 'Increase in understanding how to respond to a peer disclosing sexual violence', 'Responding to a disclosure'),
    ]
    act = [
        (38, '+38%', 'Pressure', 'Increase in stopping a partner who was pressuring sexually', 'Stopping a partner'),
        (30, '+30%', 'Unhealthy relationships', 'Increase in understanding steps to safely leave an unhealthy relationship', 'Leaving safely'),
        (26, '+26%', 'Rape culture', 'Increase in understanding all of the elements that contribute to rape culture', 'Rape culture'),
        (20, '+20%', 'Consent', 'Increase in discussing consent with a partner', 'Discussing consent'),
        (17, '+17%', 'Media', 'Increase in identifying negative actions, relationship models, or how sex is portrayed in the media', 'Media literacy'),
    ]
    reports = [
        ('2025', 'Midyear report', WP + '2025/08/2025-Mid-Year-Impact-Report-11.pdf'),
        ('2024', 'Annual report', WP + '2025/08/2024-Annual-Report-6.pdf'),
        ('2023', 'Annual report', WP + '2025/08/2023-Annual-Report-5.pdf'),
        ('2022', 'Annual report', WP + '2025/08/2022-Annual-Report-2.pdf'),
        ('2019', 'Annual report', WP + '2025/08/2019-annual-report-1.pdf'),
        ('2018', 'Annual report', WP + '2025/08/2018-annual-report-1.pdf'),
        ('2017', 'Annual report', WP + '2025/08/2017-annual-report-1-1.pdf'),
    ]
    shelf = ''.join(f'<a class="im-book" href="{u}" target="_blank" rel="noopener" aria-label="{y} {t.lower()} (PDF)"><b>{y}</b><span>{t}<br>PDF</span></a>' for y, t, u in reports)
    data_docs = ''.join(f'<a class="im-doc" href="{u}" target="_blank" rel="noopener"><span class="chip">Google Doc</span><b>{esc(t)}</b><small>{esc(d)}</small></a>' for t, d, u in [
        ('2020 Virtual Summit Data', 'Findings gathered at SafeBAE’s 2020 virtual summit.', 'https://docs.google.com/document/d/1qjbGD9T-Vkvn4hCD6VNke9pGmvPMIqjr9owY0m5QCD4/edit'),
        ('2019 Student Survey Data Reports', 'Student survey results from 2019.', 'https://docs.google.com/document/d/1pLleAP3Cr2VWxoDQKCs5RTO2BgEjyM-KoQchHuDuoJc/edit'),
        ('2017/2018 Student Survey Data Report', 'Student survey results from the 2017/2018 school year.', 'https://docs.google.com/document/d/1dsZOUKgcveqjQzKrh7LUF8mr-d0QBewDPo-WJxr8RXM/edit'),
    ])
    p = pod('0JfMJbj7ZvISm8m7gp39YS')

    body = f'''
<section class="im-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="im-hero__top">
      <div class="rise">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Data &amp; Impact</span></nav>
        <h1><span class="mk">Data,</span> findings &amp; learning</h1>
        <p class="lede">At SafeBAE, we believe sexual violence prevention should always be youth-led and evidence-driven. We collect data to understand our impact and to make sure we’re reaching students, shifting school culture, and building the skills and confidence young people need to create safer communities. Our findings come from ongoing evaluations, youth-designed surveys, internal assessments, and published research.</p>
      </div>
      <figure class="im-fig">{img('img-2400', 'Students and SafeBAE facilitators sitting in a circle during a workshop', loading='eager')}<span class="sticker">Youth-designed surveys</span>
        <figcaption class="im-datacard"><small>Climate survey, 2020–23</small><b>70%</b><span>agreed their school didn’t adequately teach their Title IX rights</span><i aria-hidden="true"></i></figcaption>
      </figure>
    </div>
    <div class="im-kpis">
      <div class="im-kpi"><b data-count="849">849</b><span>students in 45 states answered our school climate survey</span><small>2020–23</small></div>
      <div class="im-kpi"><b data-count="3000" data-suffix="+">3,000+</b><span>young people certified as Peer Educators</span><small>Certified Peer Educator Training</small></div>
      <div class="im-kpi"><b data-count="81" data-prefix="+" data-suffix="%">+81%</b><span>increase in students’ understanding of their Title IX rights after the training</span><small>2023 efficacy data</small></div>
    </div>
  </div>
</section>

<section class="band band--paper im-paper" id="research">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Journal of Child Sexual Abuse</p><h2>SafeBAE’s research, published</h2></div></div>
    <div class="ab-row">
      <div class="ab-col im-txt">
        <p>Most school-based sexual violence prevention programs are not evidence-based, and even fewer are designed with or by young people. SafeBAE’s prevention is rooted in youth leadership, survivor-centered programming, and real-world data. Our evaluation efforts make sure our model is effective, equitable, and responsive to the communities we serve.</p>
        <p>That commitment to rigor led to our research being published in the <i>Journal of Child Sexual Abuse</i>. Co-authored by our Executive Director, Shael Norris, with Dr. Lindsay Orchowski and Dr. Prachi Bhuptani of Brown University, Rhode Island Hospital, and Lifespan Hospital, the study shows that SafeBAE’s approach to preventing sexual violence is effective and transformative.</p>
        <div class="btns">{btn('Read the study', PAPER, 'slate')}{btn('Who we work with', 'partners-press.html', 'ghost', arrow=True)}</div>
        <div class="ab-floor">{spotify(p[0], 'Listen: ' + p[1], p[2])}</div>
      </div>
      <div class="ab-col">
        <figure class="im-paper__img">{img('empowering-educators-2', 'Graphic: SafeBAE’s approach to preventing dating violence backed by newly published research')}<span class="sticker">Published research</span></figure>
        <div class="ab-floor">
          <p class="eyebrow">Co-authors</p>
          <ul class="im-authors">
            <li><b>Shael Norris</b><small>Executive Director, SafeBAE</small></li>
            <li><b>Dr. Lindsay Orchowski</b><small>Brown University, Rhode Island Hospital &amp; Lifespan</small></li>
            <li><b>Dr. Prachi Bhuptani</b><small>Brown University, Rhode Island Hospital &amp; Lifespan</small></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band band--aqua band--tight" id="efficacy">
  <div class="wrap">
    <p class="eyebrow">2023 program efficacy data</p>
    <h2>What we measure, and what we found</h2>
    <p class="lede lede--full" style="margin:0">Since our founding in 2015, SafeBAE has collected and analyzed data across all programs and projects. With the guidance of our research partners, we have published dedicated evaluations and shared qualitative insights in our annual reports. Our most recent evaluation of the Certified Peer Educator Training shows its impact on both the knowledge and the actions of participating students.</p>
  </div>
</section>

<section class="band band--deep" id="climate">
  <div class="wrap">
    <div class="ab-row ab-row--57">
      <div class="ab-col im-txt">
        <p class="eyebrow">Climate survey</p>
        <h2>What students told us about their schools</h2>
        <div class="im-meta"><span>849 students surveyed</span><span>45 US states</span><span>2020–23</span></div>
        <p class="lede" style="color:rgba(255,255,255,.92)">Since 2015, our work with thousands of students has confirmed what the data now makes undeniable: sexual violence is at crisis levels for teens across the country. The {a('CDC’s Youth Risk Behavior Survey', 'https://www.cdc.gov/yrbs/results/2023-yrbs-results.html', 'link')} underscores the severity of this issue, and SafeBAE set out to learn how it plays out in schools every day.</p>
        <p style="color:rgba(255,255,255,.88)">Through the <b>SafeBAE National School Sexual Violence Climate Survey (2020–23)</b>, we partnered with students and schools to capture the lived realities of school culture, focusing on safety, support systems, and institutional accountability. The findings reveal the dangerous environments many secondary students face, and provide evidence to drive system-level change and strengthen prevention.</p>
        <div class="ab-floor">
          <div class="btns">{btn('Download the climate survey', WP + '2023/06/climate-survey-data.pdf', 'mint')}</div>
          <p class="im-note" style="color:rgba(255,255,255,.72)">PDF, 159.69 KB</p>
        </div>
      </div>
      <figure class="im-chart">
        <figcaption class="im-chart__head"><b>Students who agreed</b><span>% of students surveyed</span></figcaption>
        {bars(climate)}
        <p class="im-chart__src">Source: <b>SafeBAE National School Sexual Violence Climate Survey</b>, 2020–23. 849 students in 45 states.</p>
      </figure>
    </div>
  </div>
</section>

<section class="band band--paper" id="training">
  <div class="wrap">
    <div class="ab-row ab-row--57">
      <div class="ab-col im-txt">
        <p class="eyebrow">Peer Educator Training data</p>
        <h2>Evidence that students learn, and act</h2>
        <p>As troubling as our Climate Survey findings are, the results from our {a('Certified Peer Educator Training', 'peer-educator.html', 'link')} offer hope and clear evidence of impact. More than 2,000 students across 45 states have completed the training, showing measurable growth in knowledge, attitudes, and confidence around consent and prevention.</p>
        <p>Grounded in youth experiences and aligned with the National Health Education Standards (NHES), the curriculum reflects best practices for school-based prevention while staying student-driven and survivor-centered. Developed over eight years, it has become one of the most comprehensive and authentic prevention resources available, endorsed by both students and educators.</p>
        <div class="ab-floor">
          <div class="im-acts">{btn('Download the training data', WP + '2023/06/2023-BAE-training-data-top-sheet-1.pdf', 'slate')}{btn('Take the training', 'peer-educator.html', 'ghost', arrow=True)}</div>
          <p class="im-note muted">PDF, 178.39 KB</p>
        </div>
      </div>
      <figure class="im-chart im-light" data-tabs="impact-training">
        <figcaption class="im-chart__head">
          <div class="tabs" role="tablist" aria-label="Training results">
            <button class="tab" role="tab" id="tab-knowledge" aria-controls="panel-knowledge" aria-selected="true" tabindex="0">Knowledge</button>
            <button class="tab" role="tab" id="tab-actions" aria-controls="panel-actions" aria-selected="false" tabindex="-1">Actions &amp; results</button>
          </div>
          <span>2023 efficacy data</span>
        </figcaption>
        <div role="tabpanel" id="panel-knowledge" aria-labelledby="tab-knowledge">{bars(know)}</div>
        <div role="tabpanel" id="panel-actions" aria-labelledby="tab-actions" hidden>{bars(act)}</div>
        <div class="im-train"><div><b>1,057</b><span>students took part in the training evaluated in 2023</span></div><div><b>179</b><span>of them completed both pre- and post-surveys</span></div></div>
      </figure>
    </div>
    <div class="im-quotes">
      <figure class="im-q reveal"><p>As I went on in the training, I felt like I could be a more helpful and supportive person and that I would know what to do if something happened to me or anyone I know. I feel confident that I can help people in all sorts of situations and I am more educated on the effects of rape culture.</p><figcaption>Student participant</figcaption></figure>
      <figure class="im-q reveal"><p>This is an amazing experience and it was so beneficial for me. Your program has helped me know how to help my friend who experienced sexual assault, set boundaries with my own boyfriend and provoked some conversations about consent that we might not have had otherwise, and I have shared your program with my classmates and club members because I believe your program is something everyone should do.</p><figcaption>Student participant</figcaption></figure>
    </div>
  </div>
</section>

<section class="band band--slate" id="video">
  <div class="wrap ab-row ab-row--57">
    <div class="ab-col im-film__txt">
      <p class="eyebrow">Peer Education Data Report, 2020–2022</p>
      <h2>Does prevention work?</h2>
      <p class="lede">A look at the findings of SafeBAE’s Peer Education Data Report (2020–2022) and what the data shows about the impact of peer-to-peer education.</p>
      <div class="btns">{btn('More films in the Library', 'library.html#films', 'ghost', arrow=True)}</div>
    </div>
    <div>{yt('BmLIDyPsQz4', 'Does Prevention Work? SafeBAE’s Data & Impact Report', label='Watch')}</div>
  </div>
</section>

<section class="band band--paper" id="reports">
  <div class="wrap">
    <div class="im-annual">
      <div class="im-annual__cover" aria-hidden="true"><span class="daisy-art"></span><small>SafeBAE Annual Report</small><b>2025</b><span>Youth<br>Leading</span></div>
      <div>
        <p class="eyebrow">Youth Leading: 2025 Annual Report</p>
        <h3>SafeBAE’s Expanding Network for Change</h3>
        <p>See how SafeBAE youth leaders created safer schools, supported their peers and shifted culture across the country this year. Read the full annual report and see how you can support the next decade of SafeBAE’s work.</p>
        <div class="btns" style="margin-top:22px">{btn('Download the 2025 report', WP + '2026/01/2025-Annual-Report.pdf', 'mint')}{btn('Support the next decade', 'donate.html', 'white', arrow=True)}</div>
      </div>
    </div>
    <h2 class="im-sub">Past annual reports</h2>
    <div class="im-shelf">{shelf}</div>
    <div class="im-shelf-base" aria-hidden="true"></div>
    <h3 class="im-sub">Earlier survey data</h3>
    <div class="im-docs">{data_docs}</div>
  </div>
</section>
{give_band()}
'''
    page('impact.html', 'Data & Impact · SafeBAE', 'SafeBAE’s published research, National School Sexual Violence Climate Survey, Certified Peer Educator Training efficacy data and annual reports.',
         body, active='about', body_class='pg-impact', head_extra=css(IMPACT_CSS), scripts=IMPACT_JS)


# =====================================================================
# PHOTO CREDITS
# =====================================================================
CR_CSS = '''
.cr-hero{background-color:var(--logo-teal); color:#fff}
.cr-hero .wrap{padding-block:clamp(44px,5.5vw,80px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,4vw,56px); align-items:center}
.cr-hero h1{font-size:var(--fs-h1); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.92; letter-spacing:-.02em; margin:0 0 .35em}
.cr-hero .lede{color:rgba(255,255,255,.92); max-width:none; margin:0}
.cr-sheet{position:relative; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; padding:28px 16px 36px; background:#0f2a33; border-radius:var(--r-xl); box-shadow:0 30px 60px -30px rgba(0,0,0,.7); transform:rotate(-1.5deg); animation:sb-rise-r 1s .1s var(--ease) both}
.cr-sheet::before,.cr-sheet::after{content:""; position:absolute; left:16px; right:16px; height:8px; background:repeating-linear-gradient(90deg, rgba(209,254,255,.28) 0 10px, transparent 10px 22px); border-radius:2px}
.cr-sheet::before{top:10px} .cr-sheet::after{bottom:10px}
.cr-frame{position:relative; display:block; aspect-ratio:4/3; overflow:hidden; border-radius:4px; background:#000}
.cr-frame img{width:100%; height:100%; object-fit:cover}
.cr-frame i{position:absolute; left:7px; bottom:5px; font-style:normal; font-family:var(--mono); font-size:.7rem; font-weight:600; color:#fff; text-shadow:0 1px 3px rgba(0,0,0,.9)}
.cr-loop{position:absolute; left:calc(33.3% + 2px); top:16px; width:calc(33.3% + 14px); height:calc(50% + 2px); color:var(--mint); overflow:visible; pointer-events:none; filter:drop-shadow(0 0 6px rgba(21,255,200,.45))}
.cr-sheet__label{position:absolute; right:18px; bottom:-16px; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; background:var(--mint); color:var(--slate); padding:6px 10px; border-radius:6px; font-weight:600; transform:rotate(1.5deg)}
@media (max-width:900px){.cr-hero .wrap{grid-template-columns:minmax(0,1fr)} .cr-sheet{max-width:560px}}
/* credit cards: equal cells on shared rows; a short last row is centred */
.cr-grid{--n:4; --g:var(--gap); display:flex; flex-wrap:wrap; justify-content:center; gap:var(--g)}
.cr-grid--3{--n:3}
.cr{margin:0; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; display:flex; flex-direction:column; width:calc((100% - (var(--n) - 1) * var(--g)) / var(--n)); min-width:0}
.cr img{width:100%; aspect-ratio:4/3; object-fit:cover; background:var(--mist)}
.cr figcaption{padding:16px 18px 18px; font-size:.95rem; line-height:1.45; display:flex; flex-direction:column; gap:10px; flex:1}
.cr figcaption > span{min-height:2.9em}
.cr figcaption a{color:var(--logo-teal); font-weight:700}
.cr small{font-family:var(--mono); font-size:.72rem; letter-spacing:.05em; text-transform:uppercase; line-height:1.5; color:var(--ink-soft); padding-top:10px; border-top:1px solid var(--line)}
.cr small a{color:var(--ink-soft); font-weight:600}
@media (max-width:1000px){.cr-grid{--n:3}}
@media (max-width:720px){.cr-grid{--n:2}}
@media (max-width:420px){.cr-grid{--n:1}}
.cr-note{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.cr-note > div{border-top:4px solid var(--teal); padding-top:18px}
.cr-note h3{font-size:1.3rem; color:var(--logo-teal)}
.cr-note p{margin:0; color:var(--ink-soft); font-size:.98rem; line-height:1.55}
@media (max-width:860px){.cr-note{grid-template-columns:minmax(0,1fr); gap:26px}}
'''

def _page_label(fn):
    if os.path.basename(fn) == 'index.html':
        return 'Home'
    try:
        t = re.search(r'<title>(.*?)</title>', open(fn, encoding='utf-8').read(), re.S).group(1)
        t = html_unescape(t).split(' · ')[0].strip()
        return t or os.path.basename(fn)
    except Exception:
        return os.path.basename(fn)


def html_unescape(s):
    import html as _h
    return _h.unescape(s)


def credits():
    P = '/home/claude/v3/build/credits.jsonl'
    entries = {}
    if os.path.exists(P):
        for line in open(P, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get('slug'):
                entries[d['slug']] = d
    # where each photo is used (scan built pages)
    pages = sorted(glob.glob(f'{SITE}/*.html'))
    used = {s: [] for s in entries}
    page_txt = {}
    for fn in pages:
        if fn.endswith('credits.html'):
            continue
        try:
            t = open(fn, encoding='utf-8').read()
            i, j = t.find('<main'), t.find('</main>')
            page_txt[fn] = t[i:j] if i >= 0 and j > i else t
        except Exception:
            pass
    for s in entries:
        for fn, t in page_txt.items():
            if f'assets/img/{s}.webp' in t:
                used[s].append(os.path.basename(fn))
    cards = []
    for s, d in sorted(entries.items(), key=lambda kv: (kv[1].get('name', '').lower(), kv[0])):
        has = os.path.exists(f'{SITE}/assets/img/{s}.webp') or s in MANIFEST
        pic = img(s, f'Photo by {d.get("name", "")}') if has else ''
        where = ''
        if used.get(s):
            where = '<small>Used on: ' + ', '.join(f'<a href="{u}">{esc(_page_label(os.path.join(SITE, u)))}</a>' for u in used[s][:4]) + ('…' if len(used[s]) > 4 else '') + '</small>'
        cards.append(f'<figure class="cr">{pic}<figcaption><span>Photo by <a href="{esc(d.get("profile", "https://unsplash.com"))}" target="_blank" rel="noopener">{esc(d.get("name", "Unknown"))}</a> on <a href="{esc(d.get("page", "https://unsplash.com"))}" target="_blank" rel="noopener">Unsplash</a></span>{where}</figcaption></figure>')
    n = len(cards)
    # rows of four, unless that would leave one card alone on the last row
    cols = 3 if (n % 4 == 1 and n % 3 != 1) else 4
    grid = f'<div class="cr-grid{" cr-grid--3" if cols == 3 else ""}">{"".join(cards)}</div>' if cards else '<p class="note">No stock photography is in use on this site.</p>'
    sheet = ''.join(f'<span class="cr-frame">{img(x, "", loading="eager")}<i>{k + 1:02d}</i></span>' for k, x in enumerate(['1-000383-edited', 'clubtabling', '2023-institute-selfie', 'img-1286', 'sumact5', '000398']))

    body = f'''
<section class="cr-hero v2-dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="about.html">About</a><span>/</span><span>Photo credits</span></nav>
      <h1>Photo <span class="mk">credits</span></h1>
      <p class="lede">Most photographs on this site come from SafeBAE’s own programs, events and partners. Where a page needed a photo we didn’t have, we used images from Unsplash, credited here with thanks to the photographers.</p>
    </div>
    <div class="cr-sheet" aria-hidden="true">
      {sheet}
      <svg class="cr-loop" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M12 52C8 26 30 9 54 9c24 0 38 16 36 38-2 24-24 42-48 41C20 87 6 72 9 50 11 33 27 18 48 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
      <span class="cr-sheet__label">SafeBAE &middot; programs &amp; events</span>
    </div>
  </div>
</section>
<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Unsplash photography</p><h2>{n} photo{"s" if n != 1 else ""} from Unsplash</h2></div><a class="btn btn--ghost section-head__act" href="https://unsplash.com/license" target="_blank" rel="noopener">About the Unsplash License<span aria-hidden="true">&nbsp;&#8599;</span></a></div>
    {grid}
  </div>
</section>
<section class="band band--mist band--tight">
  <div class="wrap cr-note">
    <div><h3>SafeBAE photos</h3><p>Photos of SafeBAE students, clubs, events, staff and board come from SafeBAE and the young people and families we work with. Please ask before reusing them: {a('info@safebae.org', 'mailto:info@safebae.org', 'link')}.</p></div>
    <div><h3>Partner films &amp; media</h3><p>Film stills, video thumbnails and podcast artwork belong to the films, channels and shows they come from.</p></div>
    <div><h3>Logos</h3><p>Logos of partners, schools and publications belong to their organizations and appear to identify them.</p></div>
  </div>
</section>
'''
    page('credits.html', 'Photo credits · SafeBAE', 'Credits for the photography used on safebae.org, including photos from Unsplash.',
         body, active='about', body_class='pg-credits', head_extra=css(CR_CSS))


def build():
    about()
    team()
    impact()


if __name__ == '__main__':
    build()
