from lib import *
from data import *
import json

LIB_CSS = '''
/* ---------- hero: search on the left, the three formats on the right ---------- */
.libhero{background:var(--slate-deep) var(--grain); color:#fff; position:relative; overflow:hidden; --wm-o:.12}
.libhero .wm-daisy{right:-16%; bottom:-46%}
.libhero__g{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:stretch; padding-block:clamp(40px,5vw,68px) clamp(44px,5.4vw,76px)}
.libhero__txt{display:flex; flex-direction:column; min-width:0}
.libhero .mk{background:none; color:var(--mint)}
.libhero h1{font-size:clamp(3.2rem,8vw,7.2rem); font-stretch:125%; font-weight:900; text-transform:uppercase; line-height:.84; letter-spacing:-.03em; margin:0 0 .26em}
.libhero h1 span{display:block}
.libhero .lede{color:rgba(255,255,255,.92); margin:0 0 1.3em}
.lsearch{display:flex; align-items:center; gap:12px; margin-top:auto; background:#fff; border-radius:16px; padding:7px 7px 7px 20px; box-shadow:var(--shadow-soft); border:2px solid transparent; transition:border-color .2s, box-shadow .2s}
.lsearch:focus-within{border-color:var(--mint); box-shadow:0 0 0 5px rgba(21,255,200,.2), var(--shadow-soft)}
.lsearch svg{width:24px; height:24px; color:var(--teal); flex:none}
.lsearch input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.15rem; font-weight:500; padding:13px 0; color:var(--slate); background:transparent}
.lsearch input::placeholder{color:var(--ink-soft); opacity:1}
.lsearch .btn{box-shadow:none; min-height:50px}
/* the three ways in */
.lways{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:minmax(0,1.12fr) minmax(0,1fr); gap:14px; min-width:0}
.lway{position:relative; display:flex; flex-direction:column; min-width:0; min-height:0; border-radius:var(--r-xl); overflow:hidden; background:var(--slate); color:#fff; text-decoration:none; box-shadow:0 0 0 1px rgba(209,254,255,.16), var(--shadow-soft); transition:transform .25s var(--ease), box-shadow .25s}
.lway:hover{transform:translateY(-4px); box-shadow:0 0 0 2px var(--mint), var(--shadow-soft)}
.lway--films{grid-column:1 / -1}
.lway__media{position:relative; flex:1 1 0; min-height:118px; overflow:hidden; background:#0d2228}
.lway__media > img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform .6s var(--ease)}
.lway:hover .lway__media > img{transform:scale(1.04)}
.lway--films .lway__media > img{object-position:50% 30%}
.lway__play{position:absolute; right:14px; bottom:14px; width:46px; height:46px; border-radius:50%; background:var(--mint); color:var(--slate); display:grid; place-items:center; box-shadow:0 8px 20px rgba(0,0,0,.35)}
.lway__play svg{width:18px; height:18px; margin-left:3px}
.lway__mosaic{position:absolute; inset:0; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr}
.lway__mosaic img{width:100%; height:100%; object-fit:cover; min-height:0}
.lway--guides .lway__media{background:var(--aqua)}
.lway__fan{position:absolute; inset:14px 0 0; display:flex; justify-content:center; align-items:flex-start}
.lway__fan img{width:38%; height:auto; border-radius:5px; box-shadow:0 10px 24px -8px rgba(22,53,64,.5); transition:transform .4s var(--ease)}
.lway__fan img:nth-child(1){transform:translate(18%,10px) rotate(-8deg)}
.lway__fan img:nth-child(2){position:relative; z-index:1}
.lway__fan img:nth-child(3){transform:translate(-18%,10px) rotate(8deg)}
.lway:hover .lway__fan img:nth-child(1){transform:translate(10%,8px) rotate(-11deg)} .lway:hover .lway__fan img:nth-child(3){transform:translate(-10%,8px) rotate(11deg)}
.lway__foot{flex:none; display:flex; align-items:center; gap:10px; padding:11px 14px 11px 16px; background:var(--slate); min-height:56px}
.lway__foot b{font-family:var(--display); font-weight:900; font-stretch:112%; font-size:1.9rem; line-height:1; color:var(--mint)}
.lway__foot span{font-family:var(--display); font-weight:800; font-stretch:104%; font-size:.98rem; line-height:1.15; min-width:0}
.lway__foot i{margin-left:auto; flex:none; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; background:rgba(209,254,255,.12); color:var(--mint); font-style:normal; font-weight:800; transition:background .2s, color .2s, transform .2s var(--ease)}
.lway:hover .lway__foot i{background:var(--mint); color:var(--slate); transform:translateX(3px)}

/* ---------- filter bar ---------- */
.lbar{position:sticky; top:calc(76px + env(safe-area-inset-top,0px)); z-index:20; background:rgba(255,255,255,.96); backdrop-filter:blur(8px); border-bottom:1px solid var(--line)}
.lbar .wrap{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; justify-content:space-between; padding-block:12px}
.fmt{display:flex; gap:4px; background:var(--mist); border:1px solid var(--line); border-radius:12px; padding:4px}
.fmt button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:106%; font-size:.98rem; border:0; background:transparent; min-height:44px; padding:8px 16px; border-radius:9px; cursor:pointer; color:var(--slate); white-space:nowrap; scroll-margin-top:120px; transition:background .18s, color .18s}
.fmt button:hover{background:rgba(29,65,78,.08)}
.fmt button[aria-pressed="true"]{background:var(--slate); color:#fff}
.fmt button em{font-style:normal}
.fmt button span{font-family:var(--mono); font-size:.74rem; font-weight:600; opacity:.75; margin-left:6px}
.lsel{display:flex; gap:8px; flex-wrap:wrap}
.lsel select{font:inherit; font-size:.92rem; font-weight:600; min-height:44px; padding:9px 12px; border-radius:10px; border:2px solid var(--line); background:#fff; color:var(--slate); cursor:pointer}
.lsel select:hover{border-color:var(--teal)}
.lmain{padding-top:22px}
.ltopics{padding-bottom:22px; border-bottom:1px solid var(--line)}
.ltopics__k{display:block; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--logo-teal); margin-bottom:10px}
.topics{display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); gap:8px}
.topics button{font:inherit; font-size:.875rem; line-height:1.2; font-weight:700; min-height:52px; padding:6px 8px; border-radius:12px; border:1.5px solid var(--line); background:#fff; cursor:pointer; color:var(--slate); text-wrap:balance; transition:border-color .18s, background .18s, transform .18s var(--ease)}
.topics button:hover{border-color:var(--teal); transform:translateY(-1px)}
.topics button[aria-pressed="true"]{background:var(--mint); border-color:var(--mint)}
.topics button[data-topic=""][aria-pressed="true"]{background:var(--slate); border-color:var(--slate); color:#fff}
.lstatus{display:flex; justify-content:space-between; align-items:center; gap:12px; min-height:44px; margin:14px 0 18px; flex-wrap:wrap}
.lstatus p{margin:0; font-weight:700}
.lstatus button{font:inherit; font-weight:700; min-height:44px; color:var(--logo-teal); background:none; border:0; cursor:pointer; text-decoration:underline; text-decoration-thickness:2px; text-decoration-color:var(--mint); text-underline-offset:3px}

/* ---------- shelves and grids: rows of three; a remainder is taken up by a first row (or two) of two large cards ---------- */
.lshelf{margin-bottom:clamp(44px,5vw,64px)}
.lshelf:last-child{margin-bottom:0}
.lshelf__head{margin-bottom:22px}
.lshelf__head h2{font-size:clamp(1.7rem,2.8vw,2.4rem); margin:0}
.lshelf__head p{margin:.4em 0 0; color:var(--ink-soft)}
.lgrid{display:grid; grid-template-columns:minmax(0,1fr); gap:var(--gap)}
.item{position:relative; display:flex; flex-direction:column; text-align:left; font:inherit; color:var(--slate); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; cursor:pointer; text-decoration:none; padding:0; min-width:0; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.item:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft); border-color:rgba(19,132,143,.5)}
.item:focus-visible{outline:3px solid var(--teal); outline-offset:3px}
.item__media{position:relative; display:block; aspect-ratio:16/9; background:var(--slate); overflow:hidden}
.item__media > img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.item:hover .item__media > img{transform:scale(1.04)}
.item__kind{position:absolute; left:12px; top:12px; display:flex; flex-wrap:wrap; gap:5px}
.item__kind span{font-family:var(--mono); font-size:.7rem; line-height:1.3; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:4px 8px; border-radius:5px; background:rgba(13,34,40,.84); color:#fff}
.item__kind span.g{background:var(--mint); color:var(--slate)}
.item__kind span.w{background:var(--coral); color:var(--slate)}
.item__play{position:absolute; right:12px; bottom:12px; width:42px; height:42px; border-radius:50%; background:var(--mint); color:var(--slate); display:grid; place-items:center; box-shadow:0 6px 16px rgba(0,0,0,.3); transition:transform .2s var(--ease)}
.item:hover .item__play{transform:scale(1.08)}
.item__play svg{width:16px; height:16px; margin-left:2px}
.item__body{padding:18px 20px 20px; display:flex; flex-direction:column; gap:7px; flex:1; min-width:0}
.item__t{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.2rem; line-height:1.2; text-wrap:pretty}
.item__s{color:var(--logo-teal); font-size:.875rem; line-height:1.35; font-weight:700}
.item__d{font-size:.95rem; color:var(--ink-soft); margin:0; line-height:1.52; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden}
.item__foot{display:flex; flex-wrap:wrap; align-items:center; gap:6px; margin-top:auto; padding-top:8px}
.item__foot span{font-family:var(--mono); font-size:.7rem; line-height:1.3; letter-spacing:.02em; text-transform:uppercase; font-weight:600; background:var(--mist); border:1px solid var(--line); border-radius:5px; padding:4px 6px; white-space:nowrap}
.item__go{display:none; margin-left:auto; font-weight:800; font-size:.95rem; color:var(--logo-teal); white-space:nowrap}
.item__go i{font-style:normal; display:inline-block; margin-left:.35em; transition:transform .2s var(--ease)}
.item:hover .item__go i{transform:translateX(4px)}
/* podcast: the cover as a record sleeve, the show beside it */
.item--podcast .item__media{display:grid; grid-template-columns:56.25% minmax(0,1fr); grid-template-rows:minmax(0,1fr); background:var(--slate) var(--grain); color:#fff}
.item__cov{display:block; overflow:hidden; min-height:0; min-width:0}
.item__cov img{width:100%; height:100%; object-fit:cover; transition:transform .5s var(--ease)}
.item:hover .item__cov img{transform:scale(1.04)}
.item__pod{position:relative; display:flex; flex-direction:column; justify-content:flex-end; gap:6px; padding:12px 12px 14px 14px; min-width:0}
.item__pod .item__kind{position:static; margin-bottom:auto}
.item__pod b{font-size:.875rem; line-height:1.3; font-weight:700; display:-webkit-box; -webkit-line-clamp:4; -webkit-box-orient:vertical; overflow:hidden}
.item__pod small{font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--mint)}
.item--podcast .item__play{width:36px; height:36px; right:10px; top:10px; bottom:auto}
/* guide: the cover on an aqua shelf */
.item--guide .item__media{background:var(--aqua); display:flex; align-items:flex-end; justify-content:center; padding-top:18px}
.item--guide .item__media > img{width:auto; height:100%; max-width:64%; object-fit:cover; object-position:top; border-radius:6px 6px 0 0; box-shadow:0 -10px 30px -10px rgba(0,0,0,.35)}
.item--land .item__media > img{width:76%; max-width:none; height:auto; aspect-ratio:16/9; object-position:center}
/* wide card: a single result, the adult guide, or the odd first card on a two-column grid */
.item--wide .item__body, .item--big .item__body{gap:8px}
@media (min-width:600px){
  .lgrid--one > .item{flex-direction:row}
  .lgrid--one > .item .item__media{flex:0 0 min(42%,470px); aspect-ratio:16/9; align-self:stretch; height:auto}
  .lgrid--one > .item .item__body{justify-content:center; padding:24px 30px}
  .lgrid--one > .item .item__t{font-size:1.6rem}
  .lgrid--one > .item .item__d{-webkit-line-clamp:5; font-size:1rem}
  .lgrid--one > .item .item__go{display:inline-block}
  .lgrid--one > .item .item__foot{margin-top:8px}
}
@media (min-width:600px) and (max-width:1179px){
  .lgrid:not(.lgrid--one){grid-template-columns:repeat(2,minmax(0,1fr))}
  .lgrid[data-m2="1"] > .item:first-child{grid-column:1 / -1; flex-direction:row}
  .lgrid[data-m2="1"] > .item:first-child .item__media{flex:0 0 50%; aspect-ratio:16/9; align-self:stretch; height:auto}
  .lgrid[data-m2="1"] > .item:first-child .item__body{justify-content:center; padding:20px 24px}
  .lgrid[data-m2="1"] > .item:first-child .item__t{font-size:1.4rem}
  .lgrid[data-m2="1"] > .item:first-child .item__d{-webkit-line-clamp:4}
  .lgrid[data-m2="1"] > .item:first-child .item__go{display:inline-block}
  .lgrid[data-m2="1"] > .item:first-child .item__foot{margin-top:6px}
}
@media (min-width:1180px){
  .lgrid:not(.lgrid--one){grid-template-columns:repeat(6,minmax(0,1fr))}
  .lgrid:not(.lgrid--one) > .item{grid-column:span 2}
  .lgrid:not(.lgrid--one) > .item--big{grid-column:span 3}
  .lgrid > .item--big .item__body{padding:22px 26px 24px}
  .lgrid:not(.lgrid--one) > .item--big .item__t{font-size:1.55rem}
  .lgrid:not(.lgrid--one) > .item--big .item__d{font-size:1rem}
  .lgrid > .item--big .item__go{display:inline-block}
  .lgrid > .item--big .item__pod{padding:18px 18px 20px 20px} .lgrid > .item--big .item__pod b{font-size:1.05rem}
  .lgrid > .item--big.item--podcast .item__play{width:46px; height:46px; right:16px; top:16px}
}
@supports (grid-template-rows:subgrid){
  @media (min-width:600px){
    .lgrid:not(.lgrid--one) > .item{display:grid; grid-template-rows:subgrid; grid-row:span 5; row-gap:0}
    .lgrid:not(.lgrid--one) > .item .item__body{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:7px; align-content:start}
    .lgrid:not(.lgrid--one) > .item .item__foot{margin-top:0; align-self:end}
  }
  @media (min-width:600px) and (max-width:1179px){
    .lgrid[data-m2="1"] > .item:first-child{display:flex; grid-row:auto}
    .lgrid[data-m2="1"] > .item:first-child .item__body{display:flex; grid-row:auto}
    .lgrid[data-m2="1"] > .item:first-child .item__foot{margin-top:6px; align-self:auto}
  }
}
.lempty{padding:clamp(36px,5vw,64px) 24px; text-align:center; border:2px dashed var(--line); border-radius:var(--r-xl); background:var(--mist)}
.lempty h3{margin:0 0 .35em; font-size:1.6rem}
.lempty p{margin:0 auto; max-width:60ch}
.lempty__try{display:flex; flex-wrap:wrap; justify-content:center; gap:8px; margin-top:20px}
.lempty__try button{font:inherit; font-weight:700; font-size:.95rem; min-height:44px; padding:8px 16px; border-radius:999px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer}
.lempty__try button:hover{border-color:var(--teal)}
.lempty__try button.is-clear{background:var(--slate); border-color:var(--slate); color:#fff}

/* ---------- item drawer ---------- */
.ldrawer{position:fixed; inset:0; z-index:96; display:none}
.ldrawer.open{display:block}
.ldrawer__panel{position:absolute; right:0; top:0; bottom:0; width:min(620px,100%); background:#fff; overflow:auto; padding:calc(18px + env(safe-area-inset-top,0px)) clamp(18px,3vw,32px) calc(30px + env(safe-area-inset-bottom,0px)); box-shadow:-30px 0 60px rgba(0,0,0,.3)}
.ldrawer__panel h2{font-size:clamp(1.6rem,3vw,2.2rem); margin:16px 0 .3em}
.ldrawer__sub{font-weight:700; color:var(--logo-teal); margin:0}
.ldrawer .vid{margin:18px 0; border-radius:var(--r-xl)}
.ldrawer .vid img{opacity:1}
.ldrawer .audio{margin:18px 0; border-radius:var(--r-xl)}
.ldrawer .chips{gap:8px; margin-top:4px}
.ldrawer .chip{font-size:.74rem; min-height:44px; padding:.4em .9em}
.ldrawer__links{display:grid; gap:0; margin-top:20px}

/* ---------- more from SafeBAE: two campaigns in their own look, three plain doors ---------- */
.lmore h2{font-size:clamp(1.7rem,2.8vw,2.4rem); margin:0 0 var(--head-gap)}
.lmore__two{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap); align-items:stretch; margin-bottom:var(--gap)}
.lmore__card{display:grid; grid-template-columns:clamp(120px,13vw,168px) minmax(0,1fr) auto; gap:clamp(16px,2vw,24px); align-items:center; padding:20px 22px 20px 20px; text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease); min-width:0}
.lmore__card:hover{transform:translateY(-3px)}
.lmore__txt{min-width:0}
.lmore__txt b{display:block; font-size:1.3rem; line-height:1.15; margin-bottom:6px}
.lmore__txt small{display:block; font-size:.95rem; line-height:1.5}
.lmore__card .go{width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:800; transition:transform .2s var(--ease)}
.lmore__card:hover .go{transform:translateX(3px)}
.lmore--ai{background-color:#fff; background-image:radial-gradient(rgba(19,132,143,.22) 1.1px, transparent 1.5px); background-size:16px 16px; color:var(--slate); border:2px solid var(--slate); border-radius:16px; box-shadow:6px 6px 0 var(--mint)}
.lmore--ai:hover{box-shadow:8px 9px 0 var(--mint)}
.lmore--ai b{font-family:"Balsamiq Sans","Comic Neue",var(--body); font-weight:700; font-size:1.4rem}
.lmore--ai small{color:var(--ink-soft)}
.lmore--ai .go{background:var(--slate); color:var(--mint)}
.lmore__fig img{width:100%; aspect-ratio:1200/834; object-fit:cover; border-radius:10px; border:2px solid var(--slate); transform:rotate(-2deg)}
.lmore--ch{background-color:var(--slate); background-image:var(--grain); color:#fff; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.lmore--ch b{font-family:var(--display); font-weight:900; font-stretch:112%}
.lmore--ch small{color:rgba(255,255,255,.86)}
.lmore--ch .go{background:var(--mint); color:var(--slate)}
.lb-label{display:block; container-type:inline-size; background:#FFD600; color:#0d0d0d; border-radius:8px; padding:3.5%; transform:rotate(-3deg); box-shadow:0 14px 26px -16px rgba(0,0,0,.8)}
.lb-label > span{display:flex; flex-direction:column; align-items:center; text-align:center; border:2px solid #0d0d0d; border-radius:5px; padding:7cqi 5cqi 6cqi; font-family:var(--display); font-weight:900; text-transform:uppercase; line-height:1; white-space:nowrap}
.lb-label__w{display:flex; align-items:center; gap:3cqi; font-size:15cqi; font-stretch:104%}
.lb-label__w svg{width:.95em; height:.84em; flex:none}
.lb-label__a{font-size:7.3cqi; margin-top:5cqi; font-stretch:100%}
.lb-label__c{font-size:6.4cqi; margin-top:5cqi; text-transform:none; font-weight:800}
.libfoot{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.ldoor{display:grid; grid-template-columns:minmax(0,1fr) auto; grid-template-rows:auto 1fr; gap:10px 16px; align-items:center; padding:var(--pad-card); background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); color:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s}
.ldoor:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft); border-color:rgba(19,132,143,.5)}
.ldoor h3{margin:0; font-size:1.18rem; line-height:1.2; text-wrap:normal}
.ldoor p{grid-column:1 / -1; align-self:start; margin:0; font-size:.95rem; line-height:1.5; color:var(--ink-soft)}
.ldoor .go{grid-column:2; grid-row:1; width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-weight:800; transition:background .2s, transform .2s var(--ease)}
.ldoor:hover .go{background:var(--mint); transform:translateX(3px)}

@media (max-width:1180px){ .lway:not(.lway--films) .lway__foot i{display:none} }
@media (max-width:960px){
  .libhero__g{grid-template-columns:minmax(0,1fr)}
  .lsearch{margin-top:0}
  .lways{grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-rows:auto}
  .lway--films{grid-column:auto}
  .lway__foot i{display:none}
  .lway__media{flex:none; aspect-ratio:4/3; min-height:0}
  .lmore__two{grid-template-columns:minmax(0,1fr)}
  .libfoot{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:899px){
  .topics{grid-template-columns:repeat(4,minmax(0,1fr))}
}
@media (max-width:599px){
  .ltopics{border-bottom:0; padding-bottom:6px}
  .ltopics__k{margin-bottom:4px}
  .topics{display:flex; flex-wrap:nowrap; overflow-x:auto; scrollbar-width:none; margin-inline:calc(var(--gutter) * -1); padding:4px var(--gutter) 10px; -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 44px),transparent); mask-image:linear-gradient(90deg,#000 calc(100% - 44px),transparent)}
  .topics::-webkit-scrollbar{display:none}
  .topics button{flex:none; white-space:nowrap; min-height:44px; padding:6px 14px; border-radius:999px}
}
@media (max-width:700px){
  .lbar{position:static}
  .fmt{width:100%} .fmt button{flex:1 1 auto; min-width:0; padding:8px 5px; font-size:.9rem} .fmt button span{margin-left:4px} .fmt button em{display:none}
  .lsel{width:100%} .lsel select{flex:1 1 0; min-width:0}
  .lway__play{width:34px; height:34px; right:8px; bottom:8px} .lway__play svg{width:13px; height:13px}
  .lway__foot{flex-direction:column; align-items:flex-start; gap:2px; padding:10px 12px 12px; min-height:0}
  .lway__foot b{font-size:1.6rem} .lway__foot span{font-size:.875rem} .lway__foot i{display:none}
  .lways{gap:10px}
  .lsearch{padding:6px 6px 6px 14px; gap:8px} .lsearch input{font-size:1rem} .lsearch .btn{padding-inline:.9em}
  .lmore__card{grid-template-columns:96px minmax(0,1fr) auto; gap:14px; padding:16px}
}
'''

# podcast covers are cropped square: keep the subject in frame
POD_POS = {'sp-3h2vvayco9q0bkyphcasa3': '4% 50%;transform:scale(1.72);transform-origin:40% 44%', 'us-velasquez-mic': '74% 50%', 'daisy-coleman': '38% 30%'}

def lib_json():
    out = []
    for it in library_items():
        g = it.get('guide')
        th = it.get('thumb')
        imgsrc(th)
        if g and g.get('cover'): imgsrc(g['cover'])
        out.append({k: v for k, v in dict(
            id=it['id'], k=it['kind'], t=it['title'], s=it.get('sub', ''), d=it.get('desc', ''), y=it.get('year'), date=it.get('date'),
            top=it.get('topics', []), aud=it.get('aud', []), kw=it.get('kw', ''), th=f'assets/img/{th}.webp', h=it.get('href'), op=POD_POS.get(th),
            yt=it.get('yt'), sp=it.get('spotify'), url=it.get('url'), g=({'pdf': g['pdf'], 'pages': g.get('pages'), 'cover': f'assets/img/{g["cover"]}.webp', 'label': g.get('label')} if g else None),
            links=it.get('links', []), note=it.get('note'), f=it.get('feat')).items() if v not in (None, [], '')})
    return out

def library():
    data = lib_json()
    with open(f'{SITE}/assets/js/library-data.js', 'w') as fh:
        fh.write('window.SB_LIB=' + json.dumps(data, ensure_ascii=False) + ';window.SB_TOPICS=' + json.dumps(TOPICS) + ';')
    n_vid = sum(1 for d in data if d['k'] in ('film', 'video', 'series'))
    n_pod = sum(1 for d in data if d['k'] == 'podcast')
    n_gui = sum(1 for d in data if d.get('g') and d.get('k') != 'guide')   # teaching guides that go with a film or series
    n_gall = sum(1 for d in data if d.get('g'))                              # everything the Guides filter shows
    mosaic = ''.join(img(n, '', loading='eager') for n in ['sp-5xoykkksc9qzgegggo9wqw', 'sp-0jfmjbj7zvism8m7gp39ys', 'sp-4jjztqt08zjur9gufgj56x', 'sp-042usrg0amabkto66wqqwc'])
    fan = ''.join(img(n, '', loading='eager') for n in ['guide-knowb4unude', 'guide-red-flags', 'guide-dating'])
    body = f'''
<section class="libhero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap libhero__g">
    <div class="libhero__txt rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="resources.html">Resources</a><span>/</span><span>Library</span></nav>
      <h1><span>The</span><span class="mk">Library</span></h1>
      <p class="lede">Since 2015, SafeBAE has built a collection of youth-led media to spark honest conversations about consent, relationships and prevention. Every film is envisioned, written, directed and performed by young people, and most come with a ready-to-teach guide. Search everything in one place.</p>
      <form class="lsearch" role="search" id="lform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><label class="sr-only" for="lq">Search the library</label><input id="lq" type="search" placeholder="Search by topic, title, speaker or keyword" autocomplete="off"><button class="btn" type="submit">Search</button></form>
    </div>
    <nav class="lways" aria-label="Browse by format">
      <a class="lway lway--films" href="#films" data-go="films"><span class="lway__media">{img('knowb4unude', '', loading='eager')}<span class="lway__play" aria-hidden="true">{ICON_PLAY}</span></span><span class="lway__foot"><b>{n_vid}</b><span>Films &amp; videos</span><i aria-hidden="true">&rarr;</i></span></a>
      <a class="lway lway--pods" href="#podcasts" data-go="podcasts"><span class="lway__media"><span class="lway__mosaic">{mosaic}</span></span><span class="lway__foot"><b>{n_pod}</b><span>Podcasts</span><i aria-hidden="true">&rarr;</i></span></a>
      <a class="lway lway--guides" href="#guides" data-go="guides"><span class="lway__media"><span class="lway__fan">{fan}</span></span><span class="lway__foot"><b>{n_gui}</b><span>Teaching guides</span><i aria-hidden="true">&rarr;</i></span></a>
    </nav>
  </div>
</section>
<div class="lbar" id="lbar">
  <div class="wrap">
    <div class="fmt" role="group" aria-label="Format">
      <button aria-pressed="true" data-fmt="all">All<span>{len(data)}</span></button><button aria-pressed="false" data-fmt="films" id="films">Films<em> &amp; videos</em><span>{n_vid}</span></button><button aria-pressed="false" data-fmt="podcasts" id="podcasts">Podcasts<span>{n_pod}</span></button><button aria-pressed="false" data-fmt="guides" id="guides">Guides<span>{n_gall}</span></button>
    </div>
    <div class="lsel">
      <label class="sr-only" for="laud">Audience</label><select id="laud"><option value="">For anyone</option><option>Students</option><option>Educators</option><option>Parents</option></select>
      <label class="sr-only" for="lsort">Sort</label><select id="lsort"><option value="feat">Featured first</option><option value="new">Newest first</option><option value="az">A to Z</option></select>
    </div>
  </div>
</div>
<section class="band band--paper lmain">
  <div class="wrap">
    <div class="ltopics"><span class="ltopics__k" id="ltopics-k">Topics</span><div class="topics" role="group" aria-labelledby="ltopics-k" id="ltopics"></div></div>
    <div class="lstatus"><p id="lcount" aria-live="polite"></p><button id="lclear" hidden>Clear all filters</button></div>
    <div id="lout"></div>
  </div>
</section>
<section class="band band--aqua lmore" aria-labelledby="lmore-h">
  <div class="wrap">
    <h2 id="lmore-h">More from SafeBAE</h2>
    <div class="lmore__two">
      <a class="lmore__card lmore--ai" href="ai-literacy.html"><span class="lmore__fig">{img('ai-illo-hello', '')}</span><span class="lmore__txt"><b>SafeBAE AI Literacy Training</b><small>Six free, self-paced modules for anyone 13 or older. Launches during U.S. Media Literacy Week, October 26–30, 2026.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="lmore__card lmore--ch" href="choking-hazard.html"><span class="lb-label" aria-hidden="true"><span><span class="lb-label__w"><svg viewBox="0 0 48 42" aria-hidden="true"><path d="M24 4 45 39H3Z" fill="none" stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><rect x="21.6" y="14.5" width="4.8" height="13.5" rx="1.2" fill="currentColor"/><circle cx="24" cy="33" r="2.8" fill="currentColor"/></svg>Warning</span><span class="lb-label__a">Choking is a hazard</span><span class="lb-label__c">chokinghazard.org</span></span></span><span class="lmore__txt"><b>Choking Hazard</b><small>SafeBAE’s campaign on sexual strangulation. There’s no safe way to choke someone.</small></span><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="libfoot">
      <a class="ldoor" href="posters.html"><h3>Prevention posters</h3><p>Free downloadable posters on consent, boundaries and online harassment.</p><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="ldoor" href="consent-curriculum.html"><h3>The Consent Curriculum</h3><p>15 lessons with slides, facilitator guides and assessments, aligned with NHES.</p><span class="go" aria-hidden="true">&rarr;</span></a>
      <a class="ldoor" href="contact.html"><h3>Suggest a topic</h3><p>Looking for a topic we don’t cover yet? Tell us what would help in your classroom.</p><span class="go" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>
<div class="ldrawer" id="ldrawer" aria-hidden="true"><div class="drawer__scrim" data-lclose></div><div class="ldrawer__panel" role="dialog" aria-label="Library item"><div class="drawer__head"><p class="eyebrow" style="margin:0" id="ldk"></p><button class="close-x" data-lclose aria-label="Close">&times;</button></div><div id="ldbody"></div></div></div>
'''
    page('library.html', 'The Library · SafeBAE', 'Every SafeBAE film, podcast and teaching guide in one searchable library.', body, active='resources',
         fonts='family=Balsamiq+Sans:wght@700', head_extra=f'<style>{LIB_CSS}</style>', scripts='<script src="assets/js/library-data.js"></script><script src="assets/js/library.js"></script>')

LIB_JS = r'''
(function(){
  var L = window.SB_LIB || [], T = window.SB_TOPICS || [], d = document;
  var st = { q:'', fmt:'all', topic:'', aud:'', sort:'feat' };
  var PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>';
  function esc(s){ return String(s||'').replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function norm(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[’']/g,'').replace(/[^a-z0-9#+ ]/g,' '); }
  var hay = {}; L.forEach(function(it){ hay[it.id] = { t: norm(it.t), all: norm([it.t, it.s, it.d, (it.top||[]).join(' '), it.kw, (it.aud||[]).join(' ')].join(' ')) }; });
  function score(it, terms){ var h = hay[it.id], s = 0; for(var i=0;i<terms.length;i++){ var q = terms[i]; if(h.t.indexOf(q)>=0) s += 6; else if(h.all.indexOf(q)>=0) s += 2; else return 0; } return s; }
  function fmtOK(it){ if(st.fmt==='all') return true; if(st.fmt==='films') return it.k==='film'||it.k==='video'||it.k==='series'; if(st.fmt==='podcasts') return it.k==='podcast'; if(st.fmt==='guides') return !!it.g; return true; }
  function dateOf(it){ return it.date || (it.y ? it.y + '-06-01' : '0000'); }
  function kindLabel(it){ return {film:'Film', video:'Video', podcast:'Podcast', series:'Series', guide:'Guide'}[it.k]; }
  function fmtDate(s){ if(!s) return ''; var p = s.split('-'); var m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][+p[1]-1]; return m + ' ' + (+p[2]) + ', ' + p[0]; }
  function isPage(it){ return it.h && !/^https?:/.test(it.h) && (it.k==='film'||it.k==='series'); }
  function goLabel(it, guideMode){ if(it.k==='podcast') return 'Listen'; if(it.k==='guide') return 'Open the guide'; if(guideMode) return 'Get the guide'; if(it.k==='series') return 'Open the series'; if(isPage(it)) return 'Watch and teach'; return 'Watch'; }
  /* one card anatomy: media, title, source line, text, topics (+ action on the large cards) */
  function card(it, mode, big){
    var guideMode = (mode==='guides' && it.g) || it.k==='guide';
    var tag = isPage(it) ? 'a' : 'button';
    var attrs = tag==='a' ? ' href="' + it.h + '"' : ' type="button" data-open="' + it.id + '"';
    var media;
    if(it.k==='podcast'){
      media = '<span class="item__media"><span class="item__cov"><img src="' + it.th + '" alt="" loading="lazy"' + (it.op ? ' style="object-position:' + it.op + '"' : '') + '></span><span class="item__pod"><span class="item__kind"><span>Podcast</span></span><b>' + esc(it.s) + '</b>' + (it.date ? '<small>' + fmtDate(it.date) + '</small>' : '') + '</span><span class="item__play">' + PLAY + '</span></span>';
    } else if(guideMode){
      media = '<span class="item__media"><img src="' + it.g.cover + '" alt="" loading="lazy"><span class="item__kind"><span class="g">' + (it.k==='series' ? 'Four lessons' : it.k==='guide' ? 'Guide for adults' : 'Teaching guide') + (it.g.pages ? ' · ' + it.g.pages + ' pp' : '') + '</span></span></span>';
    } else {
      var chips = '<span>' + kindLabel(it) + '</span>' + (it.g && it.k!=='guide' ? '<span class="g">' + (it.k==='series' ? '4 lessons' : 'Guide' + (it.g.pages ? ' · ' + it.g.pages + ' pp' : '')) + '</span>' : '') + (it.note ? '<span class="w">' + esc(it.note) + '</span>' : '');
      media = '<span class="item__media"><img src="' + it.th + '" alt="" loading="lazy"><span class="item__kind">' + chips + '</span>' + (it.yt ? '<span class="item__play">' + PLAY + '</span>' : '') + '</span>';
    }
    var tops = (it.top||[]).slice(0, 2).map(function(t){ return '<span>' + esc(t) + '</span>'; }).join('');
    var cls = 'item' + (big ? ' item--big' : '') + (it.k==='podcast' ? ' item--podcast' : '') + (guideMode ? ' item--guide' : '') + (guideMode && it.k==='series' ? ' item--land' : '');
    var sub = it.k==='podcast' ? '' : esc(it.s);
    return '<' + tag + ' class="' + cls + '"' + attrs + '>' + media + '<span class="item__body"><b class="item__t">' + esc(it.t) + '</b><span class="item__s">' + sub + '</span><span class="item__d">' + esc(it.d) + '</span><span class="item__foot">' + tops + '<span class="item__go" style="background:none;border:0;padding:0;font-family:inherit;font-size:.95rem;letter-spacing:0;text-transform:none">' + goLabel(it, guideMode) + '<i aria-hidden="true">' + (it.k==='guide' ? '↗' : '→') + '</i></span></span></span></' + tag + '>';
  }
  /* rows of three; two large cards open the grid when the count leaves a remainder, so no card sits alone */
  function grid(items, mode){
    var n = items.length;
    if(n===1) return '<div class="lgrid lgrid--one">' + card(items[0], mode, true) + '</div>';
    var bigs = n % 3 === 2 ? 2 : (n % 3 === 1 ? 4 : 0);
    return '<div class="lgrid" data-m2="' + (n % 2) + '">' + items.map(function(it, i){ return card(it, mode, i < bigs); }).join('') + '</div>';
  }
  function sortList(a){
    if(st.sort==='az') return a.sort(function(x,y){ return x.t.replace(/[^a-z0-9]/ig,'').localeCompare(y.t.replace(/[^a-z0-9]/ig,'')); });
    if(st.sort==='new') return a.sort(function(x,y){ return dateOf(y).localeCompare(dateOf(x)); });
    return a.sort(function(x,y){ return (x.f||99)-(y.f||99) || ({film:0,series:0,video:1,guide:2,podcast:3}[x.k]-{film:0,series:0,video:1,guide:2,podcast:3}[y.k]) || dateOf(y).localeCompare(dateOf(x)); });
  }
  var out = d.getElementById('lout'), count = d.getElementById('lcount'), clear = d.getElementById('lclear'), q = d.getElementById('lq');
  function render(){
    var terms = norm(st.q).split(/\s+/).filter(Boolean);
    var list = L.filter(function(it){ return fmtOK(it) && (!st.topic || (it.top||[]).indexOf(st.topic)>=0) && (!st.aud || (it.aud||[]).indexOf(st.aud)>=0); });
    var scored = terms.length ? list.map(function(it){ return [score(it, terms), it]; }).filter(function(x){ return x[0]>0; }) : list.map(function(it){ return [0, it]; });
    var res = terms.length && st.sort==='feat' ? scored.sort(function(a,b){ return b[0]-a[0]; }).map(function(x){ return x[1]; }) : sortList(scored.map(function(x){ return x[1]; }));
    var filtered = terms.length || st.topic || st.aud || st.fmt!=='all';
    clear.hidden = !filtered;
    count.textContent = res.length + (res.length===1 ? ' result' : ' results') + (st.q ? ' for “' + st.q + '”' : '') + (st.topic ? ' in ' + st.topic : '') + (st.aud ? ' for ' + st.aud.toLowerCase() : '');
    if(!res.length){
      out.innerHTML = '<div class="lempty"><h3>Nothing matches yet.</h3><p class="muted">Try a broader word like <b>consent</b>, or clear the filters. You can also <a class="link" href="contact.html">tell us what you were looking for</a>.</p><div class="lempty__try"><button type="button" data-try="consent">consent</button><button type="button" data-try="bystander">bystander</button><button type="button" data-try="Title IX">Title IX</button><button type="button" class="is-clear" data-try="">Clear all filters</button></div></div>';
      return;
    }
    if(!filtered && st.sort==='feat'){
      var shelves = [
        ['Films with teaching guides', 'Each film is paired with a ready-to-teach guide for short, meaningful discussions.', res.filter(function(i){ return i.k==='film'||i.k==='series'; })],
        ['Podcasts', 'Conversations SafeBAE’s founders, staff and student leaders were invited into. Want to feature SafeBAE on your show or in your reporting? Email <a class="link" href="mailto:info@safebae.org">info@safebae.org</a>.', res.filter(function(i){ return i.k==='podcast'; })],
        ['More videos', 'Explainers, campaigns and moments from the SafeBAE community.', res.filter(function(i){ return i.k==='video'; })],
        ['Guides for adults', '', res.filter(function(i){ return i.k==='guide'; })]
      ];
      out.innerHTML = shelves.filter(function(s){ return s[2].length; }).map(function(s){ return '<div class="lshelf"><div class="lshelf__head"><h2>' + s[0] + '</h2>' + (s[1] ? '<p>' + s[1] + '</p>' : '') + '</div>' + grid(s[2], '') + '</div>'; }).join('');
    } else {
      out.innerHTML = grid(res, st.fmt);
    }
  }
  /* topics */
  var tw = d.getElementById('ltopics');
  tw.innerHTML = '<button type="button" aria-pressed="true" data-topic="">All topics</button>' + T.map(function(t){ return '<button type="button" aria-pressed="false" data-topic="' + esc(t) + '">' + esc(t) + '</button>'; }).join('');
  tw.addEventListener('click', function(e){ var b = e.target.closest('[data-topic]'); if(!b) return; st.topic = st.topic===b.dataset.topic ? '' : b.dataset.topic; syncTopics(); render(); });
  function syncTopics(){ tw.querySelectorAll('button').forEach(function(b){ var on = b.dataset.topic===st.topic; b.setAttribute('aria-pressed', String(on)); if(on && b.scrollIntoView && tw.scrollWidth > tw.clientWidth) tw.scrollLeft = Math.max(0, b.offsetLeft - tw.offsetLeft - 40); }); }
  d.querySelectorAll('[data-fmt]').forEach(function(b){ b.addEventListener('click', function(){ st.fmt = b.dataset.fmt; syncFmt(); render(); }); });
  function syncFmt(){ d.querySelectorAll('[data-fmt]').forEach(function(x){ x.setAttribute('aria-pressed', String(x.dataset.fmt===st.fmt)); }); }
  d.getElementById('laud').addEventListener('change', function(){ st.aud = this.value; render(); });
  d.getElementById('lsort').addEventListener('change', function(){ st.sort = this.value; render(); });
  var bar = d.getElementById('lbar');
  function toResults(smooth){ var hd = d.querySelector('.site-header'), off = hd ? hd.offsetHeight : 76; var y = bar.getBoundingClientRect().top + window.pageYOffset - off + 1; window.scrollTo({top: Math.max(0, y), behavior: smooth ? 'smooth' : 'auto'}); }
  var t;
  q.addEventListener('input', function(){ clearTimeout(t); t = setTimeout(function(){ st.q = q.value.trim(); render(); }, 120); });
  d.getElementById('lform').addEventListener('submit', function(e){ e.preventDefault(); st.q = q.value.trim(); render(); toResults(true); });
  function reset(){ st = { q:'', fmt:'all', topic:'', aud:'', sort:st.sort }; q.value=''; d.getElementById('laud').value=''; }
  function clearAll(){ reset(); syncFmt(); syncTopics(); render(); }
  clear.addEventListener('click', clearAll);
  /* hero doors: Films, Podcasts, Guides */
  d.querySelectorAll('[data-go]').forEach(function(a){ a.addEventListener('click', function(e){ e.preventDefault(); reset(); st.fmt = a.dataset.go; syncFmt(); syncTopics(); render(); try{ history.replaceState(null, '', '#' + a.dataset.go); }catch(err){} toResults(true); }); });
  /* drawer */
  var dr = d.getElementById('ldrawer'), db = d.getElementById('ldbody'), last;
  function openItem(id){
    var it = L.filter(function(x){ return x.id===id; })[0]; if(!it) return; last = d.activeElement;
    d.getElementById('ldk').textContent = kindLabel(it) + (it.date ? ' · ' + fmtDate(it.date) : '');
    var media = '';
    if(it.yt) media = '<a class="vid" href="https://www.youtube.com/watch?v=' + it.yt + '" target="_blank" rel="noopener" data-yt="' + it.yt + '"><img src="' + it.th + '" alt=""><span class="vid__play"><span>' + PLAY + '</span></span><span class="vid__label"><span>' + esc(it.t) + '</span><small>Watch</small></span></a>';
    else if(it.sp) media = '<a class="audio" href="https://open.spotify.com/episode/' + it.sp + '" target="_blank" rel="noopener" data-spotify="episode/' + it.sp + '"><img src="' + it.th + '" alt=""' + (it.op ? ' style="object-position:' + it.op + '"' : '') + '><span><b>' + esc(it.t) + '</b><small>' + esc(it.s) + '</small></span><span class="playdot">' + PLAY + '</span></a>';
    else if(it.url) media = '<a class="audio" href="' + it.url + '" target="_blank" rel="noopener"><img src="' + it.th + '" alt=""' + (it.op ? ' style="object-position:' + it.op + '"' : '') + '><span><b>' + esc(it.t) + '</b><small>' + esc(it.s) + '</small></span><span class="playdot">' + PLAY + '</span></a>';
    var links = (it.links||[]).map(function(l){ var ext = /^https?:/.test(l[1]); return '<a class="row" href="' + l[1] + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '><span><b>' + esc(l[0]) + '</b></span><span class="go">' + (ext ? '↗' : '→') + '</span></a>'; });
    if(it.h){ var ext = /^https?:/.test(it.h); links.unshift('<a class="row" href="' + it.h + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '><span><b>' + (it.k==='guide' ? 'Open the guide (PDF)' : 'Go to the related page') + '</b>' + (it.g ? '<small>Teaching guide, discussion questions and activities</small>' : '') + '</span><span class="go">' + (ext ? '↗' : '→') + '</span></a>'); }
    db.innerHTML = '<h2>' + esc(it.t) + '</h2><p class="ldrawer__sub">' + esc(it.s) + '</p>' + media + (it.note ? '<p class="note note--coral small"><b>Content note:</b> this video uses real messages survivors received and includes explicit language. A non-explicit version is in the library.</p>' : '') + '<p>' + esc(it.d) + '</p><div class="chips">' + (it.top||[]).map(function(t){ return '<button class="chip" style="border:0;cursor:pointer" data-jump="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') + '</div>' + (links.length ? '<div class="ldrawer__links rows">' + links.join('') + '</div>' : '');
    dr.classList.add('open'); dr.setAttribute('aria-hidden','false'); d.body.style.overflow='hidden';
    db.querySelectorAll('[data-jump]').forEach(function(b){ b.addEventListener('click', function(){ st.topic = b.dataset.jump; syncTopics(); render(); closeItem(); toResults(true); }); });
    setTimeout(function(){ dr.querySelector('.close-x').focus(); }, 30);
  }
  function closeItem(){ dr.classList.remove('open'); dr.setAttribute('aria-hidden','true'); d.body.style.overflow=''; if(last && last.focus) last.focus(); }
  out.addEventListener('click', function(e){
    var b = e.target.closest('[data-open]'); if(b){ openItem(b.dataset.open); return; }
    var tr = e.target.closest('[data-try]'); if(tr){ var v = tr.dataset.try; clearAll(); if(v){ st.q = v; q.value = v; render(); } }
  });
  dr.querySelectorAll('[data-lclose]').forEach(function(b){ b.addEventListener('click', closeItem); });
  d.addEventListener('keydown', function(e){ if(e.key==='Escape' && dr.classList.contains('open')){ e.stopPropagation(); closeItem(); } }, true);
  /* initial state from hash or session: #films, #podcasts and #guides set the format, #q-word runs a search, #topic-slug picks a topic */
  function fromHash(){
    var h = decodeURIComponent(location.hash.slice(1)).toLowerCase();
    if(h==='films'||h==='podcasts'||h==='guides'){ st.fmt = h; return true; }
    if(h.indexOf('q-')===0){ st.q = h.slice(2); return true; }
    if(h){ var tp = T.filter(function(x){ return norm(x).replace(/ /g,'-').replace(/-+/g,'-').indexOf(h)===0 || norm(x).indexOf(h)>=0; })[0]; if(tp){ st.topic = tp; return true; } }
    return false;
  }
  var sq = null; try{ sq = sessionStorage.getItem('libq'); sessionStorage.removeItem('libq'); }catch(e){}
  var hit = fromHash();
  if(sq){ st.q = sq; hit = true; }
  q.value = st.q; syncFmt(); syncTopics(); render();
  if(hit){ var go = function(){ toResults(false); }; if(d.readyState==='complete') setTimeout(go, 60); else window.addEventListener('load', function(){ setTimeout(go, 60); }); }
  window.addEventListener('hashchange', function(){ var keep = st; reset(); if(fromHash()){ q.value = st.q; syncFmt(); syncTopics(); render(); toResults(true); } else { st = keep; q.value = st.q; d.getElementById('laud').value = st.aud; } });
})();
'''

def build():
    with open(f'{SITE}/assets/js/library.js', 'w') as fh:
        fh.write(LIB_JS)
    library()
