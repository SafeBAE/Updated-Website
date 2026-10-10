from films_common import *

CSS = '''
/* It's Giving Red Flags: a neon sign on a night wall. Coral tubes for red flags, mint tubes for consent, and a tube that runs red to green. */
.film--red{--night:#0c1d22; --lift:#11272e; --neon:#fe7171; --neon2:#15ffc8; --mid:#9fb3b8; --f-card:#152f37; --f-line:rgba(255,255,255,.12); --f-ink:#fff; --f-ink2:rgba(255,255,255,.84); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint);
  --f-disp:'Tilt Neon',var(--display); --f-dw:400; --f-dt:uppercase; --f-dl:.02em; --f-ds:100%;
  --glow-r:0 0 2px #fff, 0 0 9px var(--neon), 0 0 24px var(--neon), 0 0 54px rgba(254,113,113,.7);
  --glow-g:0 0 2px #fff, 0 0 9px var(--neon2), 0 0 24px rgba(21,255,200,.85), 0 0 54px rgba(21,255,200,.5);
  --glow-soft:0 0 1px rgba(255,255,255,.9), 0 0 14px rgba(254,113,113,.5), 0 0 34px rgba(254,113,113,.28)}
.film--red main{background:var(--night) var(--grain); color:#fff}
.rf-r{color:#fff3f3; text-shadow:var(--glow-r)}
.rf-g{color:#eafffa; text-shadow:var(--glow-g)}
.rf-flag{display:inline-block; width:.8em; height:1em; flex:none; overflow:visible}

/* hero: the sign and the screen hang level, their text sits under them */
.rf-hero{position:relative; overflow:hidden; --wm-o:.13; background:radial-gradient(60% 70% at 18% 38%, rgba(254,113,113,.17), transparent 70%), radial-gradient(46% 60% at 88% 96%, rgba(21,255,200,.1), transparent 70%)}
.rf-hero .wm-daisy{right:-13%; bottom:-58%}
.rf-hero__g{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7.4fr); grid-template-areas:"head vid" "act txt"; gap:clamp(26px,3vw,40px) clamp(28px,4vw,56px); align-items:start; padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,84px)}
.rf-hero__head{grid-area:head; align-self:end; min-width:0}
.rf-hero__vid{grid-area:vid; align-self:end; min-width:0}
.rf-hero__txt{grid-area:txt; min-width:0}
.rf-hero__act{grid-area:act; min-width:0}
.rf-hero .crumbs{color:rgba(255,255,255,.62)}
.rf-hero .eyebrow{color:var(--neon2); margin-bottom:1.1rem}
.rf-hero .lede{color:rgba(255,255,255,.92); margin:0}
.rf-hero__act .btns{gap:10px}
.rf-hero__act .btn{padding-inline:.95em; font-size:.95rem}
.rf-hero__note{margin:18px 0 0; font-size:.95rem; line-height:1.55; color:rgba(255,255,255,.74)}
.rf-sign{font-family:'Tilt Neon',sans-serif; font-weight:400; text-transform:uppercase; font-size:clamp(3.4rem,9.5vw,8.5rem); line-height:.9; letter-spacing:.02em; margin:0; width:fit-content; max-width:100%}
.rf-sign > span{display:block}
.rf-sign__a{font-size:.335em; line-height:1; letter-spacing:.3em; margin:0 0 .5em .06em; color:#ffe4e4; text-shadow:0 0 2px #fff, 0 0 10px var(--neon), 0 0 26px rgba(254,113,113,.75); white-space:nowrap}
.rf-sign .mk{background:none; padding:0; color:#fff5f5; text-shadow:var(--glow-r)}
.rf-sign .mk > span{display:flex; align-items:center; gap:.2em}
.rf-sign .rf-flag{width:.62em; height:.78em; color:#fff5f5; stroke-width:2.4; filter:drop-shadow(0 0 3px var(--neon)) drop-shadow(0 0 12px var(--neon)) drop-shadow(0 0 26px rgba(254,113,113,.7)); margin-top:-.06em}
.rf-sign__tube{position:relative; display:block; height:.058em; min-height:5px; border-radius:99px; margin:.2em .03em 0; background:linear-gradient(90deg,#ffe3e3,#fff 50%,#dcfff6)}
.rf-sign__tube::before{content:""; position:absolute; inset:-4px 0; border-radius:99px; background:linear-gradient(90deg,var(--neon),var(--mid) 50%,var(--neon2)); filter:blur(9px); z-index:-1}
.rf-sign__tube::after{content:""; position:absolute; inset:-14px -6px; border-radius:99px; background:linear-gradient(90deg,var(--neon),transparent 46%,transparent 54%,var(--neon2)); filter:blur(26px); opacity:.55; z-index:-2}
@keyframes rf-flick{0%,17%,23%,27%,52%,58%,100%{opacity:1} 20%,25%,55%{opacity:.28}}
.rf-sign .mk > span:last-child{animation:rf-flick 2.4s .7s 1 both}
.rf-vid{border:2px solid rgba(254,113,113,.7); border-radius:var(--r-xl); box-shadow:0 0 0 6px rgba(254,113,113,.08), 0 0 26px rgba(254,113,113,.35), 0 0 80px rgba(254,113,113,.22)}

/* bands and section heads */
.rf-band{padding-block:var(--band); position:relative}
.rf-band--lift{background:var(--lift) var(--grain)}
.rf-head{margin-bottom:var(--head-gap)}
.rf-head--act{display:flex; align-items:end; justify-content:space-between; gap:20px 40px; flex-wrap:wrap}
.rf-head--act > div{flex:1 1 520px; min-width:0}
.rf-band h2, .film--red .fx-h{font-family:'Tilt Neon',sans-serif; font-weight:400; text-transform:uppercase; letter-spacing:.02em; font-stretch:100%; line-height:1.02}
.rf-band h2{font-size:clamp(2rem,4.3vw,3.5rem); margin:0; color:#fff; text-shadow:var(--glow-soft)}
.rf-band .frel h2, .rf-band.frel h2, .rf-band.fbegin h2{text-shadow:var(--glow-soft)}
.rf-band .eyebrow{color:var(--neon)}
.rf-band .eyebrow.is-g{color:var(--neon2)}
.rf-head .lede{margin:.65em 0 0; color:rgba(255,255,255,.88)}
.rf-head .lede + p{margin:.9em 0 0; color:rgba(255,255,255,.8)}
.rf-band h2 .rf-r{text-shadow:var(--glow-r)} .rf-band h2 .rf-g{text-shadow:var(--glow-g)}
.rf-box{background:var(--f-card); border:1px solid var(--f-line); border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.rf-box h3{font-size:1.3rem; margin:0 0 .55em}
.rf-box p{margin:0; font-size:.98rem; line-height:1.6; color:rgba(255,255,255,.84)}

/* before you press play: two ideas, one question, the run of show */
.rf-prep{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-areas:"a b run" "q q run"; gap:var(--gap)}
.rf-prep__a{grid-area:a} .rf-prep__b{grid-area:b} .rf-prep__q{grid-area:q} .rf-run{grid-area:run}
.rf-ask{display:grid; grid-template-columns:auto minmax(0,1fr); gap:6px 22px; align-items:center; border-radius:var(--r-xl); padding:var(--pad-card); border:1.5px solid rgba(21,255,200,.5); background:rgba(21,255,200,.07); box-shadow:0 0 30px rgba(21,255,200,.1), inset 0 0 24px rgba(21,255,200,.05)}
.rf-ask b{font-family:'Tilt Neon',sans-serif; font-weight:400; text-transform:uppercase; font-size:1.5rem; line-height:1.05; letter-spacing:.02em; color:#eafffa; text-shadow:var(--glow-g); max-width:5.2em}
.rf-ask p{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.18rem; line-height:1.4}
.rf-run{display:flex; flex-direction:column}
.rf-run ol{list-style:none; margin:0 0 4px; padding:0; counter-reset:run; display:flex; flex-direction:column; flex:1}
.rf-run li{margin:0; flex:1; display:flex; border-top:1px solid var(--f-line)}
.rf-run li a{counter-increment:run; flex:1; display:grid; grid-template-columns:2.1rem minmax(0,1fr) auto; align-items:center; gap:8px; min-height:48px; padding:8px 4px; color:#fff; text-decoration:none; font-weight:700; font-size:.98rem; line-height:1.3; border-radius:8px; transition:background .2s, padding .2s var(--ease)}
.rf-run li a::before{content:counter(run); font-family:'Tilt Neon',sans-serif; font-size:1.7rem; line-height:1; color:#eafffa; text-shadow:var(--glow-g)}
.rf-run li a::after{content:"\\2192"; color:var(--neon2); font-weight:800; transition:transform .2s var(--ease)}
.rf-run li a:hover{background:rgba(21,255,200,.08); padding-inline:10px 8px}
.rf-run li a:hover::after{transform:translateX(3px)}
.rf-run__foot{border-top:1px solid var(--f-line); padding-top:16px; font-size:.95rem!important; color:rgba(255,255,255,.78)!important}
.rf-run__foot b{color:#fff}
.rf-run__foot a{color:var(--neon2); font-weight:800; white-space:nowrap}

/* MOVERS: six letters, one lit at a time */
.movers{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:clamp(8px,1vw,14px); margin:0 0 clamp(10px,1.2vw,16px)}
.movers button{position:relative; font:inherit; cursor:pointer; background:var(--lift); border:2px solid rgba(255,255,255,.14); border-radius:18px; padding:20px 8px 16px; color:#fff; display:flex; flex-direction:column; align-items:center; gap:8px; transition:border-color .25s, background .25s, box-shadow .25s, transform .25s var(--ease)}
.movers button b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:clamp(2.6rem,5.6vw,4.8rem); line-height:1; color:rgba(234,255,250,.4); transition:color .25s, text-shadow .25s}
.movers button span{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:rgba(255,255,255,.7)}
.movers button:hover{border-color:rgba(21,255,200,.55); transform:translateY(-2px)}
.movers button:hover b{color:rgba(234,255,250,.8)}
.movers button[aria-selected="true"]{border-color:var(--neon2); background:#143038; box-shadow:0 0 0 4px rgba(21,255,200,.1), 0 0 34px rgba(21,255,200,.22)}
.movers button[aria-selected="true"] b{color:#eafffa; text-shadow:var(--glow-g)}
.movers button[aria-selected="true"] span{color:#fff}
.movers button[aria-selected="true"]::after{content:""; position:absolute; left:50%; bottom:-11px; width:16px; height:16px; margin-left:-8px; background:#143038; border-right:2px solid var(--neon2); border-bottom:2px solid var(--neon2); transform:rotate(45deg); border-radius:0 0 4px 0}
.pillar{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(22px,4vw,56px); background:var(--f-card); border-radius:var(--r-xl); padding:clamp(22px,3vw,38px); border:1px solid var(--f-line)}
.pillar .pillar__k{font-family:var(--mono); font-size:.74rem; line-height:1.4; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--neon2); margin:0 0 .8rem}
.pillar h3{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:clamp(2.2rem,3.6vw,3rem); line-height:1; letter-spacing:.02em; text-transform:uppercase; color:#eafffa; text-shadow:var(--glow-g); margin:0 0 .45em}
.pillar p{color:rgba(255,255,255,.9); margin:0; font-size:1.04rem; line-height:1.6}
.pillar .link{color:var(--neon2)}
.film--red .qa{--qa-line:rgba(255,255,255,.14)}
.film--red .qa summary{font-size:1.04rem; padding-right:84px}
.film--red .qa summary::after{font-size:.72rem; font-weight:600; color:var(--neon2); opacity:1; top:19px}
.film--red .qa .ans{color:rgba(255,255,255,.86); font-size:.98rem; line-height:1.6}
.rf-ch{display:flex; gap:14px 28px; align-items:center; flex-wrap:wrap; margin-top:var(--gap); padding:20px var(--pad-card); border-radius:var(--r-xl); border:1px solid rgba(254,113,113,.45); background:rgba(254,113,113,.07); color:#fff; text-decoration:none; transition:background .25s, border-color .25s, box-shadow .25s}
.rf-ch:hover{background:rgba(254,113,113,.13); border-color:var(--neon); box-shadow:0 0 30px rgba(254,113,113,.18)}
.rf-ch b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:1.6rem; line-height:1; text-transform:uppercase; color:#fff3f3; text-shadow:var(--glow-r); flex:none}
.rf-ch span{flex:1 1 380px; min-width:0; color:rgba(255,255,255,.9); font-size:.98rem; line-height:1.5}
.rf-ch i{font-style:normal; font-weight:800; color:var(--neon2); flex:none}

/* the submissions: three posts from The Ref, one discussion panel */
.feed{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin-bottom:clamp(12px,1.4vw,18px)}
.post{position:relative; display:flex; flex-direction:column; background:var(--f-card); border:1.5px solid var(--f-line); border-radius:var(--r-xl); cursor:pointer; transition:border-color .25s, box-shadow .25s, transform .25s var(--ease); min-width:0}
.post:hover{transform:translateY(-3px); border-color:rgba(254,113,113,.5)}
.post.on{border-color:var(--neon); box-shadow:0 0 0 4px rgba(254,113,113,.09), 0 0 36px rgba(254,113,113,.2)}
.post.on::after{content:""; position:absolute; left:50%; bottom:-11px; width:16px; height:16px; margin-left:-8px; background:var(--f-card); border-right:1.5px solid var(--neon); border-bottom:1.5px solid var(--neon); transform:rotate(45deg); border-radius:0 0 4px 0}
.post__head{display:flex; gap:12px; align-items:center; padding:18px 20px 12px}
.post__av{width:46px; height:46px; border-radius:50%; flex:none; display:grid; place-items:center; background:var(--night); border:2px solid var(--neon); color:#fff3f3; font-family:'Tilt Neon',sans-serif; font-size:1.02rem; text-shadow:0 0 8px var(--neon); box-shadow:0 0 14px rgba(254,113,113,.5)}
.post__who{min-width:0}
.post__who b{display:block; font-size:.98rem; line-height:1.25}
.post__who small{display:block; color:rgba(255,255,255,.66); font-size:.875rem}
.post__scene{margin-left:auto; flex:none; font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--neon2)}
.post__text{padding:0 20px 20px; font-size:1rem; line-height:1.58; color:rgba(255,255,255,.9); margin:0}
.post__text b{font-family:'Tilt Neon',sans-serif; font-weight:400; color:#fff3f3; text-shadow:0 0 10px rgba(254,113,113,.7); font-size:1.55rem; line-height:1.1; display:block; margin-bottom:8px; text-transform:uppercase; letter-spacing:.02em}
.flag{display:inline-flex; align-items:center; gap:6px; font-size:.875rem; line-height:1.2; font-weight:700; padding:6px 11px 6px 9px; border-radius:999px; background:rgba(254,113,113,.14); color:#ffd2d2; border:1px solid rgba(254,113,113,.4)}
.flag .rf-flag{width:11px; height:14px; color:var(--neon); stroke-width:4}
.post__tab{margin-top:auto; display:flex; align-items:center; justify-content:space-between; gap:12px; width:100%; min-height:54px; padding:14px 20px; background:none; border:0; border-top:1px solid var(--f-line); border-radius:0 0 var(--r-xl) var(--r-xl); font:inherit; font-weight:800; font-size:.98rem; color:var(--neon2); cursor:pointer; text-align:left}
.post__tab i{flex:none; font-style:normal; min-width:30px; height:30px; padding:0 8px; border-radius:99px; display:grid; place-items:center; font-family:var(--mono); font-size:.8rem; font-weight:600; border:1.5px solid rgba(21,255,200,.5); color:var(--neon2); transition:background .25s, color .25s, border-color .25s}
.post.on .post__tab{color:#fff}
.post.on .post__tab i{background:var(--neon); border-color:var(--neon); color:var(--slate)}
@supports (grid-template-rows:subgrid){ @media (min-width:1101px){ .post{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:0} .post__tab{margin-top:0} } }
.rf-disc{background:var(--f-card); border:1px solid var(--f-line); border-radius:var(--r-xl); padding:clamp(20px,2.6vw,34px)}
.rf-disc__head{display:flex; align-items:baseline; justify-content:space-between; gap:8px 24px; flex-wrap:wrap; margin-bottom:14px}
.rf-disc__flags{display:flex; flex-wrap:wrap; align-items:center; gap:7px; margin-bottom:20px; padding-bottom:20px; border-bottom:1px solid var(--f-line)}
.rf-disc__flags b{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:rgba(255,255,255,.74); margin-right:8px}
.rf-disc__head h3{font-size:1.35rem; margin:0}
.rf-disc__head p{margin:0; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--neon)}
.rf-disc .qa{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; align-items:stretch}
.rf-disc .qa details{border:1px solid var(--f-line)!important; border-radius:16px; background:rgba(255,255,255,.035); padding:0 18px; transition:border-color .2s, background .2s}
.rf-disc .qa details[open]:not(.q-only){border-color:rgba(21,255,200,.45)!important; background:rgba(21,255,200,.05)}
.rf-disc .qa summary{padding:16px 0 44px; font-size:1rem; line-height:1.45; min-height:100%}
.rf-disc .qa details[open] summary{min-height:0}
.rf-disc .qa summary::after{top:auto; bottom:16px; left:0; right:auto; content:"Show answer"}
.rf-disc .qa details[open] summary::after{content:"Hide answer"}
.rf-disc .qa .q-only summary{cursor:default}
.rf-disc .qa details.q-only summary::after, .rf-disc .qa details.q-only[open] summary::after{content:"Open question"; color:rgba(255,255,255,.66)}
.rf-disc .qa .ans{padding:0 0 18px}
.note-f{margin:14px 0 0; padding:18px 20px; border-radius:16px; background:rgba(21,255,200,.07); border:1px solid rgba(21,255,200,.3); font-size:.98rem; line-height:1.6; color:rgba(255,255,255,.9)}
.note-f b{color:var(--neon2)}

/* grounding: five tubes to light */
.g54321{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:var(--gap)}
.g54321 button{font:inherit; cursor:pointer; min-height:clamp(150px,15vw,200px); border-radius:var(--r-xl); border:2px solid rgba(255,255,255,.14); background:var(--lift); color:#fff; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:10px; padding:18px 10px; transition:border-color .3s, background .3s, box-shadow .3s, transform .25s var(--ease)}
.g54321 button b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:clamp(3.4rem,7vw,6rem); line-height:.9; color:rgba(234,255,250,.38); transition:color .3s, text-shadow .3s}
.g54321 button span{font-size:1rem; line-height:1.25; font-weight:700; text-align:center; color:rgba(255,255,255,.82)}
.g54321 button:hover{border-color:rgba(21,255,200,.55); transform:translateY(-2px)}
.g54321 button[aria-pressed="true"]{background:rgba(21,255,200,.1); border-color:var(--neon2); box-shadow:0 0 0 4px rgba(21,255,200,.1), 0 0 34px rgba(21,255,200,.22)}
.g54321 button[aria-pressed="true"] b{color:#eafffa; text-shadow:var(--glow-g)}
.g54321 button[aria-pressed="true"] span{color:#fff}
.rf-count{margin:16px 0 0; min-height:1.5em; font-family:var(--mono); font-size:.78rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:rgba(255,255,255,.74); text-align:center}
.rf-count.is-done{color:var(--neon2)}

/* red to green: plant the flags */
.spec{position:relative; padding-top:50px; margin-bottom:clamp(22px,2.6vw,34px)}
.spec-bar{position:relative; height:14px; border-radius:999px; background:linear-gradient(90deg,var(--neon),var(--mid) 50%,var(--neon2)); opacity:.5; transition:opacity .6s, box-shadow .6s}
.spec.lit .spec-bar{opacity:1; box-shadow:0 0 22px rgba(255,255,255,.2)}
.spec-glow{position:absolute; left:0; right:0; top:44px; height:26px; border-radius:99px; background:linear-gradient(90deg,var(--neon),var(--mid) 50%,var(--neon2)); filter:blur(18px); opacity:0; transition:opacity .8s; pointer-events:none}
.spec.lit .spec-glow{opacity:.7}
.spec-pin{position:absolute; bottom:6px; width:34px; margin-left:-9px; display:flex; flex-direction:column; align-items:flex-start; color:var(--c); transform-origin:9px 100%; transform:scale(0) rotate(-14deg); opacity:0; transition:transform .5s var(--ease), opacity .3s}
.spec-pin.on{transform:none; opacity:1}
.spec-pin .rf-flag{width:34px; height:44px; stroke-width:2.6; filter:drop-shadow(0 0 3px var(--c)) drop-shadow(0 0 10px var(--c))}
.spec-pin b{position:absolute; left:13px; top:7px; width:17px; text-align:center; font-family:var(--mono); font-size:.72rem; line-height:1; font-weight:600; color:#fff}
.spec-legend{display:grid; grid-template-columns:1fr 1fr 1fr; margin:12px 0 0; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase}
.spec-legend span:nth-child(1){color:var(--neon)} .spec-legend span:nth-child(2){text-align:center; color:rgba(255,255,255,.8)} .spec-legend span:nth-child(3){text-align:right; color:var(--neon2)}
.spec .rf-count{margin-top:10px}
.scen{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap)}
.sc{background:var(--f-card); border:1px solid var(--f-line); border-radius:var(--r-xl); padding:clamp(18px,1.7vw,24px); display:flex; flex-direction:column; gap:16px; min-width:0; transition:border-color .3s}
.sc__s{display:grid; grid-template-columns:auto minmax(0,1fr); gap:14px; align-items:start; margin:0}
.sc__n{width:34px; height:34px; border-radius:50%; display:grid; place-items:center; border:1.5px solid rgba(255,255,255,.3); font-family:'Tilt Neon',sans-serif; font-size:1.15rem; line-height:1; color:#fff; transition:border-color .3s, box-shadow .3s, color .3s}
.sc__q{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.2rem; line-height:1.3}
.sc__pick{display:flex; flex-direction:column; gap:12px; margin-top:auto}
.sc .opts{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px}
.sc .opts button{font:inherit; font-size:.875rem; line-height:1.15; font-weight:800; min-height:46px; padding:8px 2px; border-radius:10px; border:2px solid rgba(255,255,255,.22); background:transparent; color:#fff; cursor:pointer; transition:background .2s, border-color .2s, color .2s, box-shadow .2s}
.sc .opts button[data-v="0"]{--c:var(--neon)} .sc .opts button[data-v="1"]{--c:var(--mid)} .sc .opts button[data-v="2"]{--c:var(--neon2)}
.sc .opts button:hover{border-color:var(--c)}
.sc .opts button[aria-pressed="true"]{background:var(--c); border-color:var(--c); color:var(--slate)}
.sc.done .opts button.is-ans{border-color:var(--c); box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 22%, transparent), 0 0 18px color-mix(in srgb, var(--c) 40%, transparent)}
.sc .mini{position:relative; height:8px; border-radius:99px; background:linear-gradient(90deg,var(--neon),var(--mid) 50%,var(--neon2)); opacity:.3; transition:opacity .4s}
.sc .mini i{position:absolute; top:50%; left:50%; width:18px; height:18px; margin:-9px 0 0 -9px; border-radius:50%; background:#fff; border:3px solid var(--night); transform:scale(0); transition:transform .4s var(--ease), left .5s var(--ease)}
.sc.done .mini{opacity:1}
.sc.done .mini i{transform:scale(1)}
.sc.done[data-ans="0"]{--c:var(--neon)} .sc.done[data-ans="1"]{--c:var(--mid)} .sc.done[data-ans="2"]{--c:var(--neon2)}
.sc.done{border-color:color-mix(in srgb, var(--c) 55%, transparent)}
.sc.done .sc__n{border-color:var(--c); color:var(--c); box-shadow:0 0 14px color-mix(in srgb, var(--c) 45%, transparent)}
.sc .why{font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.9); margin:0; display:none}
.sc.done .why{display:block}
.sc .why b{color:var(--c)}
@supports (grid-template-rows:subgrid){ @media (min-width:641px){ .sc{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:0} .sc__s{margin-bottom:16px} .sc__pick{margin-top:0; align-self:end} .sc.done .why{margin-top:16px} } }

/* posters hung at their own proportions */
.rf-wall{display:flex; gap:var(--gap); align-items:stretch}
.rf-wall button{flex:var(--ar) 1 0; aspect-ratio:var(--ar); min-width:0; border:0; padding:0; background:var(--lift); cursor:zoom-in; border-radius:var(--r-xl); overflow:hidden; outline:2px solid color-mix(in srgb, var(--c) 75%, transparent); outline-offset:0; box-shadow:0 0 0 6px color-mix(in srgb, var(--c) 9%, transparent), 0 0 44px color-mix(in srgb, var(--c) 24%, transparent); transition:transform .3s var(--ease), box-shadow .3s}
.rf-wall button:hover{transform:translateY(-4px); box-shadow:0 0 0 6px color-mix(in srgb, var(--c) 14%, transparent), 0 0 60px color-mix(in srgb, var(--c) 38%, transparent)}
.rf-wall button:focus-visible{outline:3px solid #fff}
.rf-wall button img{width:100%; height:100%; object-fit:cover; display:block}

@media (max-width:1100px){
  .rf-prep{grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-areas:"a b" "q q" "run run"}
  .rf-run ol{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); column-gap:var(--gap)} .rf-run li:last-child{grid-column:1/-1}
  .rf-disc .qa{grid-template-columns:repeat(2,minmax(0,1fr))} .rf-disc .qa details:last-child:nth-child(odd){grid-column:1/-1}
  .feed{grid-template-columns:minmax(0,1fr)}
  .post.on::after{display:none}
  .post{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,2.3fr); grid-template-areas:"head text" "tab tab"}
  .post__head{grid-area:head; align-items:flex-start; flex-wrap:wrap; padding:22px 8px 20px 22px} .post__scene{margin-left:58px; flex-basis:100%}
  .post__text{grid-area:text; padding:22px 24px 22px 12px} .post__tab{grid-area:tab}
  .scen{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:960px){
  .rf-hero__g{grid-template-columns:minmax(0,1fr); grid-template-areas:"head" "vid" "txt" "act"}
  .rf-sign{font-size:clamp(3.4rem,24vw,10rem)}
  .pillar{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:760px){
  .movers{grid-template-columns:repeat(3,minmax(0,1fr))}
  .movers button[aria-selected="true"]::after{display:none}
  .g54321{grid-template-columns:repeat(5,minmax(0,1fr)); gap:8px}
  .g54321 button{min-height:132px; padding:14px 4px; border-radius:16px}
  .g54321 button span{font-size:.875rem}
  .rf-wall{flex-direction:column} .rf-wall button{flex:none; width:100%}
  .rf-ask{grid-template-columns:minmax(0,1fr)} .rf-ask b{max-width:none}
}
@media (max-width:640px){
  .rf-prep{grid-template-columns:minmax(0,1fr); grid-template-areas:"a" "b" "q" "run"}
  .rf-run ol{display:flex}
  .scen, .rf-disc .qa{grid-template-columns:minmax(0,1fr)}
  .post{display:flex} .post__head{flex-wrap:nowrap; align-items:center; padding:18px 20px 12px} .post__scene{margin-left:auto; flex-basis:auto} .post__text{padding:0 20px 20px}
  .g54321{grid-template-columns:repeat(6,minmax(0,1fr))} .g54321 button{grid-column:span 2} .g54321 button:nth-child(4){grid-column:2 / span 2}
  .spec-pin{width:26px; margin-left:-7px} .spec-pin .rf-flag{width:26px; height:34px} .spec-pin b{left:9px; top:5px; width:14px; font-size:.7rem}
}
'''

SCENES = [
 ('DJ', 'Scene 1', 'Dylan & Jen', 'Jen lets herself into the bathroom uninvited, blocks Dylan from leaving, and tells him a “real man” wouldn’t refuse her. She’s been drinking, and she threatens to spread rumors if he says no.',
  ['Invasion of privacy', 'Blocking an exit', '“A real man wouldn’t…”', 'Threatening rumors', 'Drinking'],
  [('What are some of Jen’s red flags?', 'She lets herself into the bathroom uninvited (an invasion of privacy), blocks Dylan from leaving the room, says a “real man” wouldn’t refuse her, threatens to spread rumors, and she’s been drinking.'),
   ('What were some ways Dylan tried to set boundaries, physically, verbally and non-verbally?', 'He told her he wasn’t interested, rolled his eyes, and tried to leave the situation.'),
   ('What is Dylan afraid of if he doesn’t agree to hook up with Jen? What might push him to give in?', 'He fears she will spread rumors about him, such as saying he doesn’t like women or that something is “wrong” with him, which pressures him into compliance.'),
   ('What do you think happens after the scene ends?', 'Dylan ultimately agrees to hook up with her, but it is not consensual.'),
   ('Why can’t this hookup be considered consensual?', 'Jen has been drinking, and Dylan is being pressured, threatened and guilted.'),
   ('How could Dylan’s friend have reacted better? Why was his friend’s behavior a red flag?', 'His friend could have believed Dylan, asked if he was okay, and supported him. Instead, the friend minimized and dismissed (gaslighted) Dylan’s concerns, which is a red flag because it normalizes harmful behavior.'),
   ('Does Jen being a woman affect how Dylan or his friend perceive the harmful behavior?', 'Yes. They assume it isn’t assault because the perpetrator is a girl, which reflects a harmful stereotype about who can commit assault.'),
   ('How should Dylan’s friend have reacted when Dylan confided in him?', 'He should have created space for Dylan to talk openly about his experience and assured him that his feelings were valid.'),
   ('Without naming anyone, what are other examples you’ve heard of someone violating boundaries in this way?', None)],
  'Abuse is still abuse when alcohol is involved. Even though Jen is impaired, she uses threats and verbal and emotional abuse to keep power and control over Dylan. If someone is too drunk to drive safely, they are too drunk to be intimate.'),
 ('KB', 'Scene 2', 'Kevin & Brian', 'Brian pushes Kevin to hook up using guilt and the threat of breaking up. Kevin hesitates out loud and with his body language. Brian’s mom knows about their relationship, and no adults are around.',
  ['Guilt-tripping', 'Threat of a breakup', 'Ignoring hesitation', 'Pushing past a no'],
  [('What are some red flags or harmful behaviors that Brian displays? How does he manipulate Kevin?', 'Brian pressures Kevin through guilt, emotional manipulation and the threat of breaking up. That coercion makes Kevin feel like he has no real choice, which means he is not freely consenting.'),
   ('What were some ways that Kevin tried to set boundaries?', 'Kevin expressed hesitation both verbally and through body language, showing he was not comfortable. Despite this, Brian kept pushing.'),
   ('Does the openness of their relationship with Brian’s mom, combined with the lack of parental supervision, affect Kevin’s experience of pressure? Why?', 'Yes. Being “out” in front of a parent, combined with little adult oversight, may have made Kevin feel even more pressure to go along with Brian’s demands.')],
  'LGBTQIA+ youth experience relationship violence at higher rates than their cisgender and heterosexual peers, along with higher rates of suicidal ideation (The Trevor Project, 2019). Being open about sexual orientation or identity does not mean someone is “open” to sex. Consent is always required. Share The Trevor Project: text START to 678-678 or call 1-866-488-7386.'),
 ('NA', 'Scene 3', 'Nessa & Anthony', 'Anthony shares intimate videos of Nessa without her knowledge. When she finds out, Nessa has a panic attack and uses a grounding technique to calm herself.',
  ['Sharing images without consent', 'Technology-based sexual abuse'],
  [('What are some red flags or harmful behaviors that Anthony displays?', 'Anthony uses technology without Nessa’s consent, sharing intimate videos of her without her knowledge. This is a form of technology-based sexual abuse.'),
   ('What impact does Anthony’s behavior have on Nessa?', 'Non-consensual use of technology can seriously harm someone’s mental health. After learning her videos were shared, Nessa experiences a panic attack and turns to a grounding technique to calm herself.'),
   ('Looking across all three scenarios, which red flags stood out most to you? How comfortable are you recognizing red flags and setting boundaries in your own relationships?', None)],
  'Consent applies online as much as in person. Non-consensual image sharing is a growing form of sexual violence, and violating digital boundaries can cause lasting trauma.'),
]

PILLARS = [
 ('M', 'Mutual', 'All parties must agree to any level of intimacy. Consent is a shared decision, not something assumed or one-sided.',
  [('Who knows a sophomore who has dated a senior?', 'Power imbalances can be significant between partners of different ages or levels of experience. A younger or less experienced person may feel pressure to agree in order to seem more mature. There can even be a power imbalance if one person cares more about the relationship. Healthy partners invite the other person to set the pace, check in often, and reassure them that nothing has to happen until both are truly ready.')]),
 ('O', 'Ongoing', 'Consent is not a one-time “yes.” It has to be given throughout every step of an interaction, not just at the start. Think of intimacy as a series of check-ins where both partners stay comfortable.', []),
 ('V', 'Voluntary', 'Consent means saying “yes” because you want to, not because of pressure, guilt or obligation. No one owes intimacy in return for a gift, attention or persistence. Asking repeatedly, wearing someone down, or making a partner feel guilty are coercion.',
  [('What are some other reasons people think they may “owe” a partner sexually?', 'For example, a common myth is that someone will experience physical pain if intimacy doesn’t “follow through.” That is untrue, and no one is ever obligated to provide sex or intimacy for any reason.')]),
 ('E', 'Enthusiastic', 'Consent should be clear, energetic and mutual, with all partners equally engaged. Sometimes a person may not have the words to say no or may not feel safe speaking up. If your partner seems hesitant, distracted or isn’t matching your energy, pause, check in, and reassure them there’s no rush.',
  [('What are some non-verbal cues that can show someone’s consent or lack of consent?', 'Leaning in, making eye contact and actively participating when they want to continue; pulling away, avoiding eye contact, tensing up or going quiet when they don’t.'),
   ('What is the best and safest way to make sure you have enthusiastic consent?', 'Verbal consent is the clearest form of consent, combined with continuous check-ins.')]),
 ('R', 'Revocable', 'Consent can be withdrawn at any time, for any reason. It doesn’t matter if something has happened before, if you already started being intimate, or how far things have gone. Anyone can stop.', []),
 ('S', 'Sober', 'Consent can’t be given if someone is under the influence of alcohol or drugs. Everyone recognizes the danger of driving under the influence, and the same principle applies to sexual activity: if a person is too impaired to drive, they are too impaired to consent.',
  [('Why do alcohol or drugs complicate consent?', 'Substances impair judgment, communication and awareness. Even if someone says “yes,” the ability to freely decide is compromised.'),
   ('Why might people excuse harmful behavior if the perpetrator was drunk?', 'Some people assume being intoxicated lessens responsibility or that the person “didn’t mean it.” Alcohol does not excuse harmful actions. Abuse is still abuse, and the impact on the survivor is the same.')]),
]

SCEN = [
 ('They’ve both been drinking, but they both said yes.', 0, 'Sober', 'If someone isn’t sober, they can’t consent, even if they say yes. Too impaired to drive means too impaired to consent.'),
 ('We hooked up last weekend, so tonight is a yes.', 0, 'Ongoing · Revocable', 'Consent is never assumed from past behavior. People who have hooked up before still need to give clear consent every time.'),
 ('They keep asking until the other person finally gives in.', 0, 'Voluntary', 'Asking repeatedly and wearing someone down is coercion, not consent.'),
 ('Their partner goes quiet, pulls away and won’t make eye contact.', 0, 'Enthusiastic', 'Hesitation is a signal to stop, check in, and reassure them there’s no rush. Silence is not consent.'),
 ('A senior is dating a sophomore who doesn’t want to seem immature.', 1, 'Mutual', 'A power imbalance is a red flag. Healthy partners invite the other person to set the pace and check in often.'),
 ('They talk first, check in as things go, and stop the moment either one hesitates.', 2, 'Ongoing · Enthusiastic · Revocable', 'This is what consent looks like: verbal, continuous and freely given, with either person able to stop at any time.'),
]

FLAG = '<svg class="rf-flag" viewBox="0 0 32 40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 4v33"/><path d="M7 6h20l-5.5 7 5.5 7H7"/></svg>'

# the lesson's run of show (from the teaching guide), each step linked to its part of the page
RUN = [('Introduce the six pillars of consent.', '#movers'), ('Watch the full film.', '#film'), ('Recap each scene and discuss.', '#scenes'),
       ('Practice grounding together.', '#ground'), ('Finish with Red to Green.', '#red-to-green')]

def build():
    posts, discs = [], []
    for i, (av, sc, who, text, flags, qs, note) in enumerate(SCENES):
        n = len(qs)
        posts.append(f'''<div class="post{" on" if i == 0 else ""}" role="presentation" data-post="{i}"><div class="post__head"><span class="post__av" aria-hidden="true">Ref</span><span class="post__who"><b>@itsgivingredflags</b><small>Submitted anonymously</small></span><span class="post__scene">{sc}</span></div>
<p class="post__text"><b>{esc(who)}</b>{esc(text)}</p>
<button class="post__tab" type="button" role="tab" id="sc-{i}" aria-controls="scp-{i}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><span>Discussion prompts &amp; answers</span><i aria-label="{n} prompts">{n}</i></button></div>''')
        discs.append(f'''<div class="rf-disc" role="tabpanel" id="scp-{i}" aria-labelledby="sc-{i}"{"" if i == 0 else " hidden"}><div class="rf-disc__head"><h3>{esc(who)}: discussion prompts &amp; answers</h3><p>{sc} &middot; {n} prompts</p></div><div class="rf-disc__flags"><b>Red flags in this scene</b>{''.join(f'<span class="flag">{FLAG}{esc(f)}</span>' for f in flags)}</div>{qa(qs)}<p class="note-f"><b>Facilitator note.</b> {esc(note)}</p></div>''')
    movers = ''.join(f'<button type="button" role="tab" id="mv-{i}" aria-controls="mvp-{i}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><b>{L}</b><span>{esc(n)}</span></button>' for i, (L, n, *_r) in enumerate(PILLARS))
    try_it = '<p class="pillar__k">Try it</p><p>Put this pillar to work in the <a class="link" href="#red-to-green">Red to Green activity</a>: the example “We hooked up last weekend, so tonight is a yes.” turns on it.</p>'
    pill_panels = ''.join(f'<div class="pillar" role="tabpanel" id="mvp-{i}" aria-labelledby="mv-{i}"{"" if i == 0 else " hidden"}><div><p class="pillar__k">Pillar {i+1} of 6</p><h3>{esc(n)}</h3><p>{esc(t)}</p></div><div>{("<p class=pillar__k>Ask the group</p>" + qa(qs)) if qs else try_it}</div></div>' for i, (L, n, t, qs) in enumerate(PILLARS))
    cnt = {0: 0, 1: 0, 2: 0}; pos = []
    for _s, v, _p, _w in SCEN:
        base = {0: 4, 1: 50, 2: 96}[v]; step = {0: 6.5, 1: 6.5, 2: -6.5}[v]
        pos.append(base + cnt[v] * step); cnt[v] += 1
    col = {0: 'var(--neon)', 1: 'var(--mid)', 2: 'var(--neon2)'}
    pins = ''.join(f'<span class="spec-pin" data-pin="{i}" style="left:{x}%;--c:{col[SCEN[i][1]]}">{FLAG}<b>{i+1}</b></span>' for i, x in enumerate(pos))
    scen = ''.join(f'''<div class="sc" data-ans="{v}" data-i="{i}"><p class="sc__s"><span class="sc__n" aria-hidden="true">{i+1}</span><span class="sc__q">“{esc(s)}”</span></p><div class="sc__pick"><div class="opts" role="group" aria-label="Where does this fall?"><button type="button" data-v="0" aria-pressed="false">Not consent</button><button type="button" data-v="1" aria-pressed="false">Unsure</button><button type="button" data-v="2" aria-pressed="false">Consent</button></div><div class="mini" aria-hidden="true"><i></i></div></div><p class="why" aria-live="polite"><b>{esc(p)}.</b> {esc(w)}</p></div>''' for i, (s, v, p, w) in enumerate(SCEN))
    ground = [('5', 'things you can see'), ('4', 'things you can touch'), ('3', 'things you can hear'), ('2', 'things you can smell'), ('1', 'thing you can taste')]
    gbtns = ''.join(f'<button type="button" aria-pressed="false"><b>{n}</b><span>{t}</span></button>' for n, t in ground)
    run = ''.join(f'<li><a href="{h}"><span>{esc(t)}</span></a></li>' for t, h in RUN)
    wall = f'''<div class="rf-wall" data-gallery><button type="button" style="--ar:{1000/772:.4f};--c:var(--neon2)" data-src="{imgsrc('no-means-no-pdf')}" data-cap="No means no, but so does…">{img('no-means-no-pdf', 'Poster: No means no, but so does silence, maybe later, I’m not sure, being drunk')}</button><button type="button" style="--ar:{1600/605:.4f};--c:var(--neon)" data-src="{imgsrc('screen-shot-2023-01-23-at-5-56-30-pm-1')}" data-cap="No doesn’t mean convince me">{img('screen-shot-2023-01-23-at-5-56-30-pm-1', 'Graphic: No doesn’t mean convince me')}</button></div>'''
    body = f'''
<section class="rf-hero fhero fhero--dark">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap rf-hero__g">
    <div class="rf-hero__head rise">
      {film_crumbs('It’s Giving Red Flags')}
      <p class="eyebrow">A SafeBAE short film + teaching guide</p>
      <h1 class="rf-sign" aria-label="It’s Giving Red Flags"><span class="rf-sign__a" aria-hidden="true">It’s giving</span><span class="mk" aria-hidden="true"><span>Red{FLAG}</span><span>Flags</span></span><i class="rf-sign__tube" aria-hidden="true"></i></h1>
    </div>
    <div class="rf-hero__vid" id="film">{yt('ETt8BnLbWwg', 'It’s Giving Red Flags', cls='rf-vid', label='Full film')}</div>
    <div class="rf-hero__txt"><p class="lede">Nessa anonymously runs a social media page called <i>It’s Giving Red Flags</i> under the name “The Ref.” As she sorts through her peers’ relationship stories, calling out manipulative and controlling behavior, she starts to recognize red flags in her own relationship.</p></div>
    <div class="rf-hero__act"><div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=ETt8BnLbWwg', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
      <p class="rf-hero__note">The film highlights scenarios that are often left out of mainstream, heteronormative portrayals of consent, and shows how easily harmful dynamics can be missed in real life.</p></div>
  </div>
</section>

<section class="rf-band rf-band--lift">
  <div class="wrap">
    <div class="rf-head"><p class="eyebrow">Before you press play</p><h2><span class="rf-r">Red flag</span> or a violation of consent?</h2>
    <p class="lede">This guide helps students tell the difference between early warning signs and behavior that rises to coercion, harassment or assault.</p></div>
    <div class="rf-prep">
      <div class="rf-box rf-prep__a"><h3>Unintentional harm is still harm</h3><p>Violations of consent aren’t always intentional, and harm can happen without malicious intent. Intention does not erase the harm, which is why clear, thoughtful discussion of consent matters.</p></div>
      <div class="rf-box rf-prep__b"><h3>Impact matters more than intent</h3><p>Sexual harassment and assault are judged by how the survivor experiences the behavior, not by what the other person meant to do. Assault can happen through emotional manipulation or coercion, not only physical force.</p></div>
      <div class="rf-ask rf-prep__q"><b>Ask the group</b><p>Why is it important to focus on the impact of someone’s actions rather than their intent when talking about consent and harm?</p></div>
      <div class="rf-box rf-run"><h3>How to run it</h3><ol>{run}</ol><p class="rf-run__foot"><b>Before you begin.</b> Tell your counselors first, make it okay to step out, and be clear about mandated reporting. <a href="#begin">Read the checklist &rarr;</a></p></div>
    </div>
  </div>
</section>

<section class="rf-band" id="movers">
  <div class="wrap">
    <div class="rf-head"><p class="eyebrow is-g">Step 1 &middot; The pillars of consent</p>
    <h2>Watch the film with <span class="rf-g">MOVERS</span> in mind.</h2>
    <p class="lede">Establish the six pillars before you show the film, then keep coming back to them. Ask students to notice where consent is missing or can’t be present.</p></div>
    <div data-tabs="rf-movers"><div class="movers" role="tablist" aria-label="Pillars of consent">{movers}</div>
    {pill_panels}</div>
    <a class="rf-ch" href="choking-hazard.html"><b>Choking Hazard</b><span>Choking can’t meet these pillars: there’s no safe way to choke someone. SafeBAE’s campaign on sexual strangulation, which young people call “choking”, has the evidence and free warning posters.</span><i>Read the campaign &rarr;</i></a>
  </div>
</section>

<section class="rf-band rf-band--lift" id="scenes">
  <div class="wrap">
    <div class="rf-head"><p class="eyebrow">Step 3 &middot; Recap the scenes</p>
      <h2>The submissions</h2>
      <p class="lede">After the film, recap each scene and work through the prompts. Brief answers are included for facilitators.</p></div>
    <div data-tabs="rf-scenes"><div class="feed" role="tablist" aria-label="Scenes">{''.join(posts)}</div>
    {''.join(discs)}</div>
  </div>
</section>

<section class="rf-band" id="ground">
  <div class="wrap">
    <div class="rf-head"><p class="eyebrow is-g">Step 4 &middot; Bonus scene: grounding</p>
      <h2>Do what <span class="rf-g">Nessa</span> does.</h2>
      <p class="lede">After a high-stress moment, Nessa uses the 5-4-3-2-1 technique to bring herself back to the present. Remind students it is always okay to take a break when they feel activated, in class or in real life.</p>
      <p>Try it together: tap each number as you notice those things around you. You can also guide a body scan, five slow breaths (in through the nose, out through the mouth), or a supportive phrase repeated five times, such as “I deserve to be loved and happy.”</p></div>
    <div class="g54321" role="group" aria-label="5-4-3-2-1 grounding">{gbtns}</div>
    <p class="rf-count" id="gdone" aria-live="polite">0 of 5 noticed</p>
  </div>
</section>

<section class="rf-band rf-band--lift" id="red-to-green">
  <div class="wrap">
    <div class="rf-head"><p class="eyebrow">Step 5 &middot; Activity</p>
    <h2>Consent: <span class="rf-r">Red</span> to <span class="rf-g">Green</span></h2>
    <p class="lede">In class, students write their own anonymous red-flag and green-flag examples and place them on the spectrum. You can also use printed examples. Here are six to sort together.</p></div>
    <div class="spec" id="spec"><span class="spec-glow" aria-hidden="true"></span><div class="spec-bar" aria-hidden="true">{pins}</div>
      <div class="spec-legend"><span>100% not consent</span><span>Unsure</span><span>100% consent</span></div>
      <p class="rf-count" id="speccount" aria-live="polite">0 of 6 sorted</p></div>
    <div class="scen">{scen}</div>
  </div>
</section>

{vibe_band("Nessa begins to recognize red flags in her own relationship once she looks at it honestly. Vibe Check gives young people a private place to do the same: a free, anonymous reflection tool for anyone worried they crossed a line or caused harm.")}

{teach_tail('red-flags', 'rf-band', ['knowb4unude', 'male-survivors', 'baecode'], 'rf-band rf-band--lift',
  help_extra='<span>LGBTQ+ youth: The Trevor Project, text START to 678-678</span>',
  posters=('Put it on the wall.', wall))}
'''
    js = r'''<script>
(function(){
  var d = document;
  /* the submissions: the whole post selects its discussion panel */
  var posts = [].slice.call(d.querySelectorAll('.post'));
  function syncPosts(){ posts.forEach(function(p){ p.classList.toggle('on', p.querySelector('.post__tab').getAttribute('aria-selected') === 'true'); }); }
  posts.forEach(function(p){
    var t = p.querySelector('.post__tab');
    p.addEventListener('click', function(e){ if(!e.target.closest('.post__tab')) t.click(); var pn = d.getElementById(t.getAttribute('aria-controls')); if(pn){ var r = pn.getBoundingClientRect(); if(r.top > window.innerHeight - 140) window.scrollTo({top: window.pageYOffset + r.top - 150, behavior: 'smooth'}); } });
    new MutationObserver(syncPosts).observe(t, {attributes:true, attributeFilter:['aria-selected']});
  });
  syncPosts();
  /* red to green: plant a flag for each example sorted */
  var spec = d.getElementById('spec'), sc = d.getElementById('speccount'), cards = [].slice.call(d.querySelectorAll('.sc'));
  cards.forEach(function(c){
    var ans = c.dataset.ans, btns = [].slice.call(c.querySelectorAll('.opts button'));
    btns.forEach(function(b){ if(b.dataset.v === ans) b.classList.add('is-ans'); b.addEventListener('click', function(){
      btns.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); });
      c.classList.add('done'); c.querySelector('.mini i').style.left = ({0:6, 1:50, 2:94})[ans] + '%';
      var pin = d.querySelector('[data-pin="' + c.dataset.i + '"]'); if(pin) pin.classList.add('on');
      var n = d.querySelectorAll('.sc.done').length;
      if(sc){ sc.textContent = n + ' of 6 sorted' + (n === 6 ? '. Only one belongs at the green end.' : ''); sc.classList.toggle('is-done', n === 6); }
      if(spec) spec.classList.toggle('lit', n === 6);
    }); });
  });
  /* grounding: light the five numbers */
  var g = d.querySelectorAll('.g54321 button'), gd = d.getElementById('gdone');
  g.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); var n = d.querySelectorAll('.g54321 [aria-pressed="true"]').length; gd.textContent = n === 5 ? 'Take one more slow breath. You’re here.' : n + ' of 5 noticed'; gd.classList.toggle('is-done', n === 5); }); });
})();
</script>'''
    film_page('film-its-giving-red-flags.html', 'It’s Giving Red Flags', 'A SafeBAE short film and teaching guide about red flags, the pillars of consent, and unhealthy relationships.',
              body, 'red', 'family=Tilt+Neon', CSS, js)
