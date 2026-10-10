from films_common import *

# #knowB4Unude has its own look, taken from the campaign's posters and teaching guide:
# lavender field, electric mint, coral frame, black, white; peach and eggplant emoji as graphic
# elements; Polaroid frames; the block logo; a heavy Didone serif (Abril Fatface) for headlines.
# Lavender (--kl) is this campaign's colour and is used on this page only.

CSS = '''
.film--know{--kl:#d592f8; --kl-soft:#f6e9fe; --kk:#17110f; --kserif:"Abril Fatface","Bodoni 72","Didot",Georgia,serif; --kemoji:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif;
  --kgap:clamp(24px,3.4vw,48px);
  --f-card:#fff; --f-line:rgba(23,17,15,.2); --f-ink:var(--kk); --f-ink2:rgba(23,17,15,.8); --f-acc:var(--kk); --f-acc-ink:var(--mint); --f-lab:var(--kk); --f-disp:var(--kserif); --f-dw:400; --f-ds:100%; --f-dl:0em; --f-bw:2px}
.film--know main{color:var(--kk)}
.film--know main :focus-visible{outline-color:var(--kk)}
.film--know :is(.kb-psa,.kb-sx,.fvb) :focus-visible{outline-color:var(--mint)}
.film--know .fx-h, .kb-h2{font-family:var(--kserif); font-weight:400; font-stretch:100%; letter-spacing:0; line-height:1.04}
.kb-h2{font-size:clamp(2.1rem,4.3vw,3.7rem); margin:0}
.film--know .fhead h2{font-size:clamp(2.1rem,4.3vw,3.7rem)}
.film--know main .eyebrow{color:var(--kk)}
.kb-band{position:relative; padding-block:var(--band)}
.kb-band > .wrap{position:relative; z-index:1}
.film--know .btn--kb{--b:var(--kk); --t:var(--mint)}
.film--know .btn--ghost{border-width:2px}

/* emoji as graphic elements (decorative, aria-hidden) */
.kb-e{position:absolute; z-index:0; display:flex; align-items:center; justify-content:center; width:1em; height:1em; font-family:var(--kemoji); font-size:var(--s,160px); font-style:normal; font-weight:400; line-height:1; white-space:nowrap; transform:rotate(var(--r,0deg)); pointer-events:none; user-select:none; -webkit-user-select:none; transition:translate .6s var(--ease)}
.kb-ei{display:inline-flex; align-items:center; justify-content:center; width:1.15em; height:1.15em; font-family:var(--kemoji); font-style:normal; font-weight:400; line-height:1; white-space:nowrap; flex:none}

/* ---------- hero: the lavender poster ---------- */
.kb-hero{position:relative; overflow:hidden; isolation:isolate; background:var(--kl); color:var(--kk)}
.kb-hero > .wrap{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--kgap); align-items:center; padding-block:clamp(40px,5.4vw,76px) clamp(64px,8vw,112px)}
.kb-hero .crumbs{color:var(--kk)} .kb-hero .crumbs a{color:var(--kk); text-decoration:underline; text-decoration-color:rgba(23,17,15,.35)} .kb-hero .crumbs a:hover{color:var(--kk); text-decoration-color:var(--kk)}
.kb-hero .eyebrow{font-weight:700}
.kb-logo{margin:0 0 clamp(18px,2.4vw,30px); line-height:0}
.kb-logo img{width:min(520px,100%); height:auto; margin-left:-6px}
.kb-hero .lede{color:var(--kk); font-size:clamp(1.06rem,1.32vw,1.24rem); margin-bottom:1.4em}
.kb-hero .btn--ghost:hover{background:rgba(23,17,15,.08)}
.kb-hero .kb-e{animation:kb-pop .9s var(--ease) both}
.kb-hero .kb-e:nth-of-type(2){animation-delay:.08s} .kb-hero .kb-e:nth-of-type(3){animation-delay:.16s} .kb-hero .kb-e:nth-of-type(4){animation-delay:.24s} .kb-hero .kb-e:nth-of-type(5){animation-delay:.32s}
@keyframes kb-pop{from{opacity:0; scale:.5; rotate:-24deg}}
.kb-e--1{--s:clamp(120px,15vw,214px); --r:16deg; right:-3.2%; top:5%}
.kb-e--2{--s:clamp(110px,13.5vw,196px); --r:-34deg; left:50%; top:-64px}
.kb-e--3{--s:clamp(130px,16vw,232px); --r:38deg; right:-4.4%; bottom:-6%}
.kb-e--4{--s:clamp(110px,14vw,204px); --r:-18deg; left:-3.6%; bottom:-88px}
.kb-e--5{--s:clamp(100px,12.5vw,180px); --r:22deg; left:45%; bottom:-78px}
/* the phone */
.kb-stage{position:relative; display:grid; justify-items:center}
.kb-phone{position:relative; width:min(336px,100%); border-radius:48px; border:11px solid var(--kk); background:#fff; color:var(--kk); padding:36px 14px 16px; display:flex; flex-direction:column; gap:10px; min-height:540px; box-shadow:14px 16px 0 var(--mint); transform:rotate(2.4deg)}
.kb-phone::before{content:""; position:absolute; top:9px; left:50%; width:84px; height:20px; margin-left:-42px; border-radius:20px; background:var(--kk)}
.kb-phone__top{display:flex; align-items:center; gap:10px; padding:6px 6px 12px; border-bottom:1px solid rgba(23,17,15,.12); margin-bottom:4px}
.kb-phone__top i{width:38px; height:38px; border-radius:50%; background:var(--kl); display:grid; place-items:center; font-style:normal; font-family:var(--kserif); font-size:1.2rem; flex:none}
.kb-phone__top b{display:block; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1rem; line-height:1.2}
.kb-phone__top small{display:block; font-size:.78rem; color:rgba(23,17,15,.7)}
.kb-msg{max-width:86%; margin:0; padding:10px 14px; border-radius:20px; font-size:.97rem; line-height:1.36; font-weight:500; animation:kb-msg .5s var(--ease) both}
.kb-msg--in{align-self:flex-start; background:#efe6f5; border-bottom-left-radius:5px}
.kb-msg--out{align-self:flex-end; background:var(--mint); border-bottom-right-radius:5px; font-weight:700}
.kb-msg--e{background:none; padding:2px 4px; font-size:2.5rem; line-height:1}
.kb-msg:nth-of-type(1){animation-delay:.4s} .kb-msg:nth-of-type(2){animation-delay:1s} .kb-msg:nth-of-type(3){animation-delay:1.7s} .kb-msg:nth-of-type(4){animation-delay:2.5s} .kb-msg:nth-of-type(5){animation-delay:3.3s}
@keyframes kb-msg{from{opacity:0; transform:translateY(10px) scale(.96)}}
.kb-typing{align-self:flex-start; display:flex; gap:5px; padding:13px 15px; background:#efe6f5; border-radius:20px; border-bottom-left-radius:5px; animation:kb-msg .5s 4.7s var(--ease) both}
.kb-compose{margin-top:auto; display:flex; align-items:center; justify-content:space-between; gap:10px; padding:5px 5px 5px 16px; border:1.5px solid rgba(23,17,15,.28); border-radius:999px; font-size:.92rem; color:rgba(23,17,15,.72)}
.kb-compose i{width:32px; height:32px; border-radius:50%; background:var(--kk); color:var(--mint); display:grid; place-items:center; font-style:normal; font-weight:800; font-size:1rem; line-height:1}
.kb-typing i{width:8px; height:8px; border-radius:50%; background:rgba(23,17,15,.55); animation:kb-dot 1.2s 5s 6} .kb-typing i:nth-child(2){animation-delay:5.2s} .kb-typing i:nth-child(3){animation-delay:5.4s}
@keyframes kb-dot{50%{opacity:.25; transform:translateY(-3px)}}
@media (prefers-reduced-motion:reduce){.kb-msg,.kb-typing,.kb-typing i,.kb-hero .kb-e{animation:none}}

/* tilted tag strip between the hero and the PSA */
.kb-break{position:relative; z-index:3; overflow:hidden; margin-block:-34px; padding-block:22px; pointer-events:none}
.kb-strip{background:var(--mint); color:var(--kk); border-block:3px solid var(--kk); transform:rotate(-1.4deg) scale(1.03); white-space:nowrap; overflow:hidden; padding:.42em 0 .5em}
.kb-strip__t{display:inline-flex; align-items:center; gap:.7em; padding-left:.7em; font-family:var(--kserif); font-size:clamp(1.1rem,1.9vw,1.6rem); line-height:1.1}
@keyframes kb-slide{to{transform:translateX(-9%)}}
@supports (animation-timeline:view()){ @media (prefers-reduced-motion:no-preference){ .kb-strip__t{animation:kb-slide linear both; animation-timeline:view(); animation-range:entry 0% exit 100%} } }

/* ---------- the PSA + quote ---------- */
.kb-psa{background:var(--kk) var(--grain); color:#fff}
.kb-psa__g{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--kgap); align-items:center}
/* the PSA sits in a Polaroid frame; the still keeps its original colour */
.film--know .kb-psa .vid{aspect-ratio:auto; border-radius:5px; border:solid #fff; border-width:14px 14px 0; background:#fff; box-shadow:12px 13px 0 var(--kl); margin:0 14px 14px 0; overflow:hidden; transition:transform .4s var(--ease), box-shadow .3s var(--ease)}
.film--know .kb-psa .vid[data-yt]{transform:rotate(-1.3deg)}
.film--know .kb-psa .vid[data-yt]:hover{transform:rotate(0deg) translateY(-4px)}
.film--know .kb-psa .vid img{aspect-ratio:16/9; height:auto; border-radius:2px; opacity:1}
.film--know .kb-psa .vid:hover img{opacity:1; transform:none}
.film--know .kb-psa .vid__play{inset:0 0 62px 0; place-items:end start; padding:0 0 18px 18px}
.film--know .kb-psa .vid__play span{width:76px; height:76px; background:var(--mint); color:var(--kk); border:3px solid var(--kk); box-shadow:4px 5px 0 var(--kk)}
.film--know .kb-psa .vid__label{position:static; min-height:62px; padding:12px 4px 14px; align-items:baseline; background:#fff; color:var(--kk); font-family:var(--kserif); font-weight:400; font-stretch:100%; font-size:1.3rem}
.film--know .kb-psa .vid__label small{color:var(--kk); opacity:1; font-size:.74rem}
.film--know .kb-psa .vid:not([data-yt]){aspect-ratio:16/9; border-width:14px}
.kb-quote{margin:0}
.kb-quote blockquote{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.12rem,1.5vw,1.36rem); line-height:1.42; color:#fff; text-wrap:pretty}
.kb-quote blockquote::before{content:"\\201C"; display:block; height:.46em; font-family:var(--kserif); font-weight:400; font-size:7.4rem; line-height:1; color:var(--kl)}
.kb-quote mark{background:none; color:var(--mint)}
.kb-quote figcaption{margin-top:18px; font-family:var(--mono); font-size:.76rem; line-height:1.5; letter-spacing:.06em; text-transform:uppercase; font-weight:500; color:var(--kl)}

/* ---------- stats: Polaroids on electric mint, inside the coral frame ---------- */
.kb-stats{overflow-x:clip; background:var(--mint); color:var(--kk); padding-block:calc(var(--band) + 10px); box-shadow:inset 0 0 0 clamp(9px,1.1vw,15px) var(--coral)}
.kb-stats .kb-h2{margin-bottom:var(--head-gap)}
.kb-src{display:flex; align-items:center; gap:14px; margin:0 0 20px; font-family:var(--mono); font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.kb-src::after{content:""; flex:1; height:2px; background:var(--kk); opacity:.3}
.kb-polas{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin-bottom:clamp(40px,4.6vw,60px)}
.kb-pola{position:relative; margin:0; display:flex; flex-direction:column; min-width:0; background:#fff; padding:14px 14px 0; border-radius:5px; box-shadow:9px 10px 0 var(--kk); transform:rotate(var(--rot,0deg)); transition:transform .35s var(--ease)}
.kb-pola:hover{transform:rotate(0deg) translateY(-4px)}
.kb-pola__ph{display:grid; gap:14px; align-content:start; background:var(--kk); color:#fff; padding:clamp(16px,2vw,26px); border-radius:2px}
.kb-pola__n{display:block; font-family:var(--kserif); font-weight:400; font-size:clamp(4.2rem,7.6vw,6.8rem); line-height:.86; letter-spacing:-.01em}
.kb-pola__n small{font-size:.56em; color:var(--mint); margin-left:.04em}
.kb-dots{display:grid; grid-template-columns:repeat(20,minmax(0,1fr)); gap:4px}
.kb-dots i{aspect-ratio:1; border-radius:50%; background:rgba(255,255,255,.2)}
.kb-dots i.on{background:var(--mint); transition:background .3s calc(var(--i,0) * 22ms)}
.js .kb-dots.reveal.pre i.on{background:rgba(255,255,255,.2)}
.kb-pola__k{font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:500; color:rgba(255,255,255,.85)}
.kb-pola figcaption{flex:1; display:grid; place-items:center; min-height:5.3em; padding:12px 6px 16px; text-align:center; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.14rem; line-height:1.25; text-wrap:balance}
.kb-e--s1{--s:clamp(96px,12vw,172px); --r:14deg; right:4%; top:calc(clamp(96px,12vw,172px) * -.36)}
.kb-e--s2{--s:clamp(84px,9.5vw,136px); --r:-32deg; right:-2.2%; top:clamp(40px,5vw,72px)}
.kb-finds{display:grid; gap:14px}
.kb-find{display:grid; grid-template-columns:clamp(130px,15vw,196px) minmax(0,1fr); gap:var(--gap); align-items:center; min-width:0; background:var(--kk); color:#fff; padding:clamp(18px,2vw,26px) var(--pad-card); border-radius:var(--r-xl) var(--r-xl) var(--r-xl) 6px}
.kb-find__n{font-family:var(--kserif); font-weight:400; font-size:clamp(3.2rem,5.4vw,4.8rem); line-height:.9; color:var(--kl); text-align:center}
.kb-find p{margin:0; font-size:1.1rem; line-height:1.55; color:#fff}
.kb-find p b{color:var(--mint)}

/* ---------- start the conversation (quiet) ---------- */
.kb-talk{background:#fff}
.kb-talk__g{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--kgap); align-items:stretch}
.kb-talk__l{display:flex; flex-direction:column; min-width:0}
.kb-talk__l .kb-h2{margin-bottom:.45em}
.kb-talk__l .lede{margin-bottom:24px}
.kb-note{margin-top:auto; background:var(--kl); color:var(--kk); border-radius:var(--r-xl); padding:var(--pad-card); font-weight:600; line-height:1.55}
.film--know .prompts{gap:10px; height:100%; align-content:space-between}
.film--know .prompts li{position:relative; margin:0; padding:15px 20px 15px 62px; background:var(--kl-soft); border:0; border-radius:22px 22px 22px 6px; font-weight:600; font-size:1.03rem; line-height:1.45}
.film--know .prompts li::before{content:"?"; position:absolute; left:16px; top:13px; width:32px; height:32px; border-radius:50%; background:var(--kk); color:var(--mint); display:grid; place-items:center; font-family:var(--kserif); font-weight:400; font-size:1.15rem; line-height:1}

/* ---------- what would you do? ---------- */
.kb-wyd{background:var(--kl); overflow:hidden}
.kb-wyd .section-head{margin-bottom:var(--head-gap)}
.kb-wyd__g{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--kgap); align-items:stretch}
.kb-tabs{display:grid; gap:14px; grid-auto-rows:1fr; min-width:0}
.kb-tabs button{font:inherit; text-align:left; cursor:pointer; display:grid; grid-template-columns:auto minmax(0,1fr); gap:2px 16px; align-items:center; align-content:center; min-height:64px; padding:16px 20px; border-radius:18px; border:3px solid var(--kk); background:#fff; color:var(--kk); transition:transform .2s var(--ease), box-shadow .2s var(--ease), background .2s, color .2s}
.kb-tabs .kb-ei{grid-row:span 2; font-size:2.1rem}
.kb-tabs small{align-self:end; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600}
.kb-tabs b{align-self:start; font-family:var(--display); font-stretch:104%; font-weight:800; font-size:1.1rem; line-height:1.3}
.kb-tabs button:hover:not([aria-selected="true"]){transform:translate(-2px,-2px); box-shadow:5px 5px 0 var(--kk)}
.kb-tabs button[aria-selected="true"]{background:var(--kk); color:#fff; box-shadow:7px 7px 0 var(--mint)}
.kb-tabs button[aria-selected="true"] small{color:var(--mint)}
.kb-panels{display:grid; min-width:0}
.kb-panel{position:relative; overflow:hidden; display:flex; flex-direction:column; gap:20px; min-height:372px; background:var(--kk); color:#fff; border-radius:var(--r-xl); padding:clamp(22px,3vw,38px)}
.kb-panel > :not(.kb-e){position:relative; z-index:1}
.kb-panel__t{max-width:calc(100% - 150px); min-height:92px}
.kb-panel .kb-panel__t{margin:0; font-family:var(--kserif); font-weight:400; font-size:clamp(1.35rem,2.1vw,1.8rem); line-height:1.16; text-wrap:balance}
.kb-checks{list-style:none; padding:0; margin:0; display:grid; gap:12px}
.kb-checks li{display:grid; grid-template-columns:28px minmax(0,1fr); gap:12px; align-items:start; margin:0; font-size:1.05rem; line-height:1.45; font-weight:500}
.kb-checks li::before{content:""; width:28px; height:28px; border-radius:8px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' stroke='%2317110f' stroke-width='3.2' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/17px no-repeat}
.kb-panel__note{margin:auto 0 0; padding-top:4px; font-weight:700; color:var(--kl)}
.kb-panel .kb-e{--s:112px; --r:14deg; right:24px; top:18px}

/* ---------- Vibe Check keeps the site's own teal look ---------- */
.film--know .fvb{color:#fff}
.film--know .fvb .fx-h{font-family:var(--display); font-weight:800; font-stretch:112%; letter-spacing:-.01em; line-height:1.02}

/* ---------- sextortion + laws ---------- */
.kb-sx{background:var(--kk) var(--grain); color:#fff}
.kb-sx__g{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:var(--gap); align-items:stretch}
.kb-sx__g > *{min-width:0; border-radius:var(--r-xl)}
.kb-warn{background:var(--coral); color:var(--kk); padding:clamp(24px,3.4vw,46px)}
.kb-warn h2{font-family:var(--kserif); font-weight:400; font-stretch:100%; letter-spacing:0; font-size:clamp(1.65rem,2.9vw,2.5rem); line-height:1.1; margin:0 0 .55em}
.kb-warn p{margin:0 0 1em} .kb-warn p:last-child{margin:0}
.kb-talkto{display:flex; flex-direction:column; background:#fff; color:var(--kk); padding:var(--pad-card)}
.kb-talkto h3{font-family:var(--kserif); font-weight:400; font-stretch:100%; letter-spacing:0; font-size:1.6rem; line-height:1.1; margin:0 0 14px}
.film--know .kb-talkto .rows{flex:1; grid-auto-rows:1fr; border-color:var(--f-line)}
.film--know .kb-talkto .row{padding:12px 2px; border-color:var(--f-line); gap:12px}
.film--know .kb-talkto .row:hover{background:var(--kl-soft)}
.film--know .kb-talkto .row:last-child{border-bottom:0; padding-bottom:0}
.film--know .kb-talkto .row b{color:var(--kk); font-size:1.08rem}
.film--know .kb-talkto .row small{color:rgba(23,17,15,.8); font-size:.92rem}
.film--know .kb-talkto .row .go{background:var(--kk); color:var(--mint)}
.film--know .kb-talkto .row:hover .go{background:var(--kk)}
.kb-rules{display:grid; align-content:space-between; gap:16px; background:#fff; color:var(--kk); padding:var(--pad-card)}
.kb-rules hr{width:100%; height:2px; margin:0; border:0; background:var(--f-line)}
.kb-rules h3{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.3rem; line-height:1.15; margin:0 0 .4em}
.kb-new h3{font-family:var(--kserif); font-weight:400; font-stretch:100%; letter-spacing:0; font-size:1.6rem; line-height:1.1; margin:0 0 .5em}
.kb-rules p, .kb-new p{margin:0; font-size:1rem; line-height:1.58}
.film--know .kb-sx .arrow-link{color:var(--kk); text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:4px; min-height:44px}
.kb-rules .arrow-link{margin-top:6px}
.kb-new{display:flex; flex-direction:column; align-items:flex-start; background:var(--mint); color:var(--kk); padding:var(--pad-card)}
.kb-new .sticker{background:var(--kl); border-color:var(--kk); box-shadow:3px 3px 0 var(--kk); color:var(--kk); margin-bottom:16px}
.kb-new .arrow-link{margin-top:auto; padding-top:10px}

/* ---------- teach it: the guide, the notes and the campaign posters on the lavender field ---------- */
.kb-teach{background:var(--kl); overflow:hidden}
.kb-teach .eyebrow{font-weight:700}
.kb-pgrid{display:flex; gap:var(--gap); align-items:stretch}
.kb-pgrid > *{flex:var(--a) 1 0; min-width:0}
.kb-pgrid button{display:block; width:100%; min-width:0; padding:0; border:3px solid var(--kk); border-radius:14px; overflow:hidden; background:var(--kk); cursor:zoom-in; box-shadow:7px 8px 0 var(--kk); transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.kb-pgrid button:hover{transform:translate(-3px,-4px) rotate(-.7deg); box-shadow:11px 13px 0 var(--kk)}
.kb-pgrid img{display:block; width:100%; height:100%; object-fit:cover}
.kb-pgrid > button{aspect-ratio:var(--a)}
.kb-pstack{display:flex; flex-direction:column; gap:var(--gap)}
.kb-pstack .kb-psq{aspect-ratio:1; flex:none}
.kb-pstack .kb-plg{flex:1; min-height:0}
.kb-pstack .kb-plg img{object-fit:contain; padding:6% 8%}
.kb-teach .kb-e--a{--s:clamp(120px,15vw,220px); --r:-22deg; left:-4%; bottom:-70px}
.kb-teach .kb-e--b{--s:clamp(110px,13vw,190px); --r:28deg; right:-3.4%; top:30%}
.film--know .teach__prep{box-shadow:7px 8px 0 var(--kk); border-color:var(--kk)}
.film--know .teach__help{color:var(--kk)}
.film--know .teach__cover::before{background:var(--mint); border:2px solid var(--kk)}
.film--know .teach__pic{border:2px solid var(--kk)}
.film--know .teach__cover .sticker{border-color:var(--kk); color:var(--kk); box-shadow:3px 3px 0 var(--kk)}
.film--know .teach__note{color:var(--kk)}
.film--know .teach__note a{color:var(--kk); text-decoration-color:var(--kk)}
.film--know .teach .btn--ghost:hover{background:rgba(23,17,15,.08)}

/* ---------- related (shared part, this page's surfaces) ---------- */
.kb-rel{background:#fff}
.film--know .fcard{box-shadow:none}
.film--know .fcard:hover{box-shadow:7px 8px 0 var(--kk); transform:translate(-3px,-4px)}

/* ---------- smaller screens ---------- */
@media (max-width:1100px){
  .kb-panel .kb-e{--s:96px; right:16px; top:14px}
  .kb-panel__t{max-width:calc(100% - 120px); min-height:78px}
  .kb-talk__g{grid-template-columns:minmax(0,4fr) minmax(0,7fr)}
  .kb-new p{font-size:1.08rem}
  .kb-sx__g{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
}
@media (max-width:960px){
  .kb-sx__g{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:860px){
  .kb-hero > .wrap, .kb-psa__g, .kb-talk__g, .kb-wyd__g{grid-template-columns:minmax(0,1fr)}
  .kb-hero > .wrap{gap:40px; padding-bottom:84px}
  .kb-e--2{left:auto; right:14%; top:-58px} .kb-e--5{left:54%} .kb-e--1{top:auto; bottom:36%} .kb-e--3{bottom:-3%}
  .kb-note{margin-top:0}
  .film--know .prompts{height:auto}
  .kb-tabs{grid-auto-rows:auto}
  .kb-panel{min-height:0}
}
@media (max-width:700px){
  .kb-polas{grid-template-columns:minmax(0,1fr); max-width:520px; margin-inline:auto; gap:32px}
  .kb-pola{transform:rotate(calc(var(--rot,0deg) * .5))}
  .kb-pola figcaption{min-height:0; padding:16px 6px 18px}
  .kb-pgrid{display:grid; grid-template-columns:repeat(2,minmax(0,1fr))}
  .kb-pgrid > button:first-child{grid-column:1 / -1}
  .kb-pstack{display:contents}
  .kb-pstack .kb-plg{aspect-ratio:1}
}
@media (max-width:560px){
  .film--know .kb-psa .vid{border-width:10px 10px 0; margin:0 10px 10px 0; box-shadow:9px 10px 0 var(--kl)}
  .film--know .kb-psa .vid:not([data-yt]){border-width:10px}
  .film--know .kb-psa .vid__play span{width:62px; height:62px}
  .kb-e--2, .kb-e--s2{display:none}
  .kb-polas{padding-inline:2px 10px}
  .kb-find{grid-template-columns:minmax(0,1fr); gap:8px} .kb-find__n{text-align:left} .kb-find p{font-size:1.02rem}
  .kb-phone{min-height:0; transform:rotate(1.4deg); box-shadow:10px 12px 0 var(--mint)}
  .kb-stats{padding-block:calc(var(--band) + 4px)}
  .kb-src{align-items:flex-start} .kb-src::after{display:none}
  .kb-panel .kb-e{--s:76px; right:12px; top:12px}
  .kb-panel__t{max-width:calc(100% - 84px); min-height:68px}
  .kb-tabs button{padding:14px 16px}
  .film--know .prompts li{padding:14px 16px 14px 56px; font-size:1rem}
  .film--know .prompts li::before{left:12px}
  .kb-pgrid button{box-shadow:5px 6px 0 var(--kk)}
}
'''

SCEN = [
 ('Someone you know', 'sends you an unsolicited nude of themselves', '🍆', ['Let them know this is not okay and ask them not to do it again.', 'Report it to a trusted adult or school official if it continues.', 'Report it on the social media platform, if it was sent online.', 'Block them if necessary.']),
 ('Someone you don’t know', 'sends you a nude by random number, AirDrop, social media or a dating app', '📱', ['Report the account to the app or platform if possible.', 'Block them immediately.']),
 ('Someone sends or shows you', 'a nude of another person', '👀', ['Tell them clearly that sharing without consent is not okay.', 'If you know the person in the image, let them know what happened.', 'Report it to a trusted adult or school official.', 'Report it on the social media platform, if it was shared online.']),
]

JS = r'''<script>
(function(){
  var hero = document.querySelector('.kb-hero'); if(!hero) return;
  var mm = window.matchMedia;
  if(!mm || mm('(prefers-reduced-motion: reduce)').matches || !mm('(hover:hover) and (pointer:fine)').matches) return;
  var es = [].slice.call(hero.querySelectorAll('.kb-e')), raf = 0, tx = 0, ty = 0;
  hero.addEventListener('pointermove', function(e){
    var r = hero.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width - .5; ty = (e.clientY - r.top) / r.height - .5;
    if(raf) return;
    raf = requestAnimationFrame(function(){ raf = 0; es.forEach(function(el, i){ var d = (i % 3 + 1) * 10; el.style.translate = (-tx * d).toFixed(1) + 'px ' + (-ty * d).toFixed(1) + 'px'; }); });
  });
  hero.addEventListener('pointerleave', function(){ es.forEach(function(el){ el.style.translate = ''; }); });
})();
</script>'''


def e(ch, cls='', style=''):
    """A decorative emoji set as a graphic element."""
    st = f' style="{style}"' if style else ''
    return f'<span class="kb-e {cls}" aria-hidden="true"{st}>{ch}</span>'


def ei(ch):
    return f'<span class="kb-ei" aria-hidden="true">{ch}</span>'


def build():
    tabs = ''.join(
        f'<button role="tab" id="wy-{i}" aria-controls="wyp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{ei(em)}<small>{esc(a_)}</small><b>{esc(b)}</b></button>'
        for i, (a_, b, em, _s) in enumerate(SCEN))
    panels = ''.join(
        f'<div class="kb-panel" role="tabpanel" id="wyp-{i}" aria-labelledby="wy-{i}"{"" if i==0 else " hidden"}>'
        f'<h3 class="kb-panel__t">If {esc(a_[0].lower() + a_[1:])} {esc(b)}</h3>'
        f'<ul class="kb-checks">{"".join(f"<li>{esc(x)}</li>" for x in st)}</ul>'
        f'<p class="kb-panel__note">Protect both yourself and the person in the image.</p>{e(em)}</div>'
        for i, (a_, b, em, st) in enumerate(SCEN))

    posters = [('kb-poster-lavender', 'Have you ever gotten a nude you didn’t want?', '1'),
               ('kb-poster-trust', 'Do you trust the person you send nudes to?', '.647'),
               ('kb-poster-teacher', 'Did you know that if a teacher catches you sharing nudes, they’re required to tell the police?', '.647')]
    ph = ''.join(f'<button type="button" style="--a:{a_}" data-src="{imgsrc(n)}" data-cap="{esc(c)}" aria-label="Open poster: {esc(c)}">{img(n, "Poster: " + c)}</button>' for n, c, a_ in posters)
    ph += (f'<div class="kb-pstack" style="--a:.6">'
           f'<button class="kb-psq" type="button" data-src="{imgsrc("kb-poster-polaroid")}" data-cap="Do you #knowB4Unude?" aria-label="Open poster: Do you #knowB4Unude?">{img("kb-poster-polaroid", "Poster: a Polaroid of a peach emoji with the words do you #knowB4Unude")}</button>'
           f'<button class="kb-plg" type="button" data-src="{imgsrc("untitled-design-2020-02-12t110716-010-3")}" data-cap="#knowB4Unude campaign graphic" aria-label="Open the #knowB4Unude campaign graphic">{img("untitled-design-2020-02-12t110716-010-3", "#knowB4Unude campaign graphic")}</button>'
           f'</div>')

    stats = [(15, 'of teens under 18 report that they send nudes', '-1.6deg'), (27, 'receive them', '1.2deg'), (12, 'forward them', '-.9deg')]
    polas = ''.join(
        f'<figure class="kb-pola" style="--rot:{rot}"><div class="kb-pola__ph"><b class="kb-pola__n">{n}<small>%</small></b>'
        f'<div class="kb-dots reveal" aria-hidden="true">{"".join(f"<i class=on style=--i:{k}></i>" if k < n else "<i></i>" for k in range(100))}</div>'
        f'<span class="kb-pola__k">{n} in every 100 teens</span></div><figcaption>{esc(t)}</figcaption></figure>'
        for n, t, rot in stats)

    finds = [
        ('2/3', 'An analysis of <b>500 accounts from girls ages 12 to 18</b> about negative experiences sexting found that two-thirds had been asked to provide explicit images, and the requests often progressed from promises of affection to “anger displays, harassment and threats.”'),
        ('&lt;8%', '<b>Less than 8% of girls</b> shared explicit pictures because they wanted to. The rest did so out of a desire to please, acquiesce to, or avoid conflict with a boy.'),
        ('4&times;', 'Girls and boys both send nude photos, but <b>boys are nearly four times as likely to pressure girls</b> to do so than the reverse. In relationships it was often normalized with claims like “everyone else has a picture of their girlfriend.”'),
    ]
    fcards = ''.join(f'<div class="kb-find"><b class="kb-find__n">{n}</b><p>{t}</p></div>' for n, t in finds)

    qs = ['Did any of the scenes feel familiar or similar to situations you’ve heard about?', 'Have you ever known someone who felt pressured to send a nude? What impact did that have on them?', 'Have you heard of a nude being shared at school without the person’s permission? What happened afterward? Did people gossip or shame the person in the photo?', 'Were there any consequences for the person who shared it without consent?', 'Before watching, did you know that sharing nudes of anyone under 18 is against the law? Does that change how you think about your own choices?', 'If someone were being harassed with nudes at your school, who would be a safe adult you could turn to?']

    strip = ''.join(f'<span>do you #knowB4Unude ???</span>{ei(c)}' for c in ('🍑', '🍆') * 7)

    body = f'''
<section class="kb-hero">
  {e('🍑', 'kb-e--1')}{e('🍆', 'kb-e--2')}{e('🍆', 'kb-e--3')}{e('🍑', 'kb-e--4')}{e('🍑', 'kb-e--5')}
  <div class="wrap">
    <div class="rise">
      {film_crumbs('#KnowB4UNude')}
      <p class="eyebrow">A public service announcement + teaching guide</p>
      <h1 class="kb-logo">{img('kb-logo-cut', '#knowB4Unude', loading='eager')}</h1>
      <p class="lede">Youth explore the pressures, risks and consequences of sending nudes, and push back on the oversimplified “just don’t do it” message adults usually give. Sexting has become a cultural norm, so this PSA and its guide start a non-judgmental conversation about consent, digital safety, image-based harm, and how peers can support each other without shame.</p>
      <div class="btns">{btn('Watch the PSA', 'https://www.youtube.com/watch?v=iNAVcRO22S0', 'kb')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div class="kb-stage">
      <div class="kb-phone" role="img" aria-label="A phone showing a message thread from an unknown number: hey. Do you trust the person you send nudes to? Have you ever gotten a nude you didn’t want? Reply: Know the risks before you send.">
        <div class="kb-phone__top" aria-hidden="true"><i>?</i><span><b>Unknown</b><small>now</small></span></div>
        <p class="kb-msg kb-msg--in" aria-hidden="true">hey</p>
        <p class="kb-msg kb-msg--in kb-msg--e" aria-hidden="true">{ei('👀')}</p>
        <p class="kb-msg kb-msg--in" aria-hidden="true">Do you trust the person you send nudes to?</p>
        <p class="kb-msg kb-msg--in" aria-hidden="true">Have you ever gotten a nude you didn’t want?</p>
        <p class="kb-msg kb-msg--out" aria-hidden="true">Know the risks before you send.</p>
        <span class="kb-typing" aria-hidden="true"><i></i><i></i><i></i></span>
        <div class="kb-compose" aria-hidden="true"><span>Text message</span><i>&uarr;</i></div>
      </div>
    </div>
  </div>
</section>
<div class="kb-break" aria-hidden="true"><div class="kb-strip"><div class="kb-strip__t">{strip}</div></div></div>

<section class="kb-band kb-psa">
  <div class="wrap kb-psa__g">
    <div>{yt('iNAVcRO22S0', '#knowB4Unude', label='PSA')}</div>
    <figure class="kb-quote">
      <blockquote>“Most of the information we get about online communication is ‘just don’t send nudes.’ But this approach is <mark>unrealistic, victim blaming, and doesn’t address the real problem.</mark> We are not here to shame kids for sending nudes. We want to offer them the opportunity to learn about the risks and talk about the pressures that surround sending and forwarding explicit pictures.”</blockquote>
      <figcaption>Molly Gallenberg, SafeBAE Youth Ambassador and #KnowB4Unude Associate Producer</figcaption>
    </figure>
  </div>
</section>

<section class="kb-band kb-stats">
  {e('🍆', 'kb-e--s2')}{e('🍑', 'kb-e--s1')}
  <div class="wrap">
    <h2 class="kb-h2">It’s more common than adults think.</h2>
    <p class="kb-src">JAMA Pediatrics, March 2018</p>
    <div class="kb-polas">{polas}</div>
    <p class="kb-src">Sarah Thomas, Northwestern University, February 2019</p>
    <div class="kb-finds">{fcards}</div>
  </div>
</section>

<section class="kb-band kb-talk">
  <div class="wrap kb-talk__g">
    <div class="kb-talk__l">
      <p class="eyebrow">After the PSA</p>
      <h2 class="kb-h2">Start the conversation.</h2>
      <p class="lede">This guide is not meant to shame or judge people for sending nudes; it’s an opportunity to talk openly about the risks, pressures, and potential outcomes so that everyone can make informed decisions.</p>
      <p class="kb-note">Some of the most vulnerable ages for harm related to nudes are in middle school, so encourage older students to share what they learn with younger siblings and through peer mentoring.</p>
    </div>
    <div>{prompts(qs)}</div>
  </div>
</section>

<section class="kb-band kb-wyd">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Three scenarios</p><h2 class="kb-h2">What would you do?</h2></div></div>
    <div class="kb-wyd__g" data-tabs="kb"><div class="kb-tabs" role="tablist" aria-label="Scenarios">{tabs}</div><div class="kb-panels">{panels}</div></div>
  </div>
</section>

{vibe_band('Forwarded a nude, or pressured someone to send one, and not sure what that means? Vibe Check is a free, anonymous reflection tool for young people questioning whether they crossed a boundary or caused harm. One of its guided modules covers digital safety and image consent.', 'Sent or forwarded one?')}

<section class="kb-band kb-sx">
  <div class="wrap kb-sx__g">
    <div class="kb-warn">
      <p class="eyebrow">Sextortion &amp; online predators</p>
      <h2>If someone you don’t know starts pressuring you online, block them and tell a trusted adult.</h2>
      <p>There has been a sharp increase in adults pretending to be young people on apps, social media and gaming platforms. Their goal is often to pressure teens into sending nudes, then threaten to make the image public unless they send money or more images. This is called sextortion. The stress of these threats has tragically led some young people to take their own lives.</p>
      <p><b>If your nudes are shared without permission, it is never your fault.</b> No one deserves to have their images used against them. School officials are mandated reporters, so they may need to inform parents depending on the situation.</p>
    </div>
    <div class="kb-talkto">
      <h3>Who can I talk to?</h3>
      <div class="rows">{row('Talk to someone you trust', 'A close friend, a trusted adult or a school counselor.', 'survivor-support.html')}{row('DM @safe_bae', 'We’ll help you find local services.', 'https://www.instagram.com/safe_bae/')}{row('Take It Down (NCMEC)', 'A free service that helps remove nude images of people under 18 from participating platforms.', 'https://takeitdown.ncmec.org/')}{row('love is respect', 'Text LOVEIS to 22522 or call 1-866-331-9474, 24/7.', 'https://www.loveisrespect.org')}</div>
    </div>
    <div class="kb-rules">
      <div><h3>State laws</h3><p>Intimate-image laws differ from state to state. With your students, look up what the law says in your state and discuss the possible consequences for people who share images without consent, at any age.</p></div>
      <hr>
      <div><h3>School policies</h3><p>Review your district’s student handbook or ask a counselor what the rules are. Every school handles this differently. If yours doesn’t have clear rules, consider advocating with your school board to create them.</p><a class="arrow-link" href="reform-policy.html">Reform your school’s policy</a></div>
    </div>
    <div class="kb-new">
      <span class="sticker">New</span>
      <h3>Fake images and sextortion</h3>
      <p>The later modules of the free SafeBAE AI Literacy Training cover both. It has six self-paced modules for high school and college students, and anyone 13 or older can take it.</p>
      <a class="arrow-link" href="ai-literacy.html">AI Literacy Training</a>
    </div>
  </div>
</section>

{teach_tail('knowb4unude', 'kb-band kb-teach', ['rape-culture', 'male-survivors', 'online-harassment'], 'kb-band kb-rel', btn_kind='kb',
  posters=('Share the campaign.', f'<div class="kb-pgrid" data-gallery>{ph}</div>'), deco=e('🍑', 'kb-e--a') + e('🍆', 'kb-e--b'))}
'''
    film_page('film-knowb4unude.html', '#knowB4Unude', '#knowB4Unude is SafeBAE’s PSA and teaching guide on the pressures, risks and consequences of sending nudes.', body, 'know', 'family=Abril+Fatface', CSS, JS)
