from films_common import *

CSS = '''
/* BAEcode: Game On! An arcade title screen: pixel type, mint HUD frames, the film on a cabinet screen, missions with an XP bar. */
.film--bae{--ind:#102c35; --ind2:#1d414e; --deep:#0b2128; --pink:#fe7171; --px:'Silkscreen',monospace; --f-card:#0b2128; --f-line:rgba(21,255,200,.4); --f-ink:#fff; --f-ink2:rgba(255,255,255,.84); --f-acc:#15ffc8; --f-acc-ink:var(--slate); --f-lab:#15ffc8; --f-r:8px; --f-bw:3px; --f-disp:var(--px); --f-dw:400; --f-dt:uppercase; --f-dl:0; --f-ds:100%}
.film--bae main{background:var(--ind); color:#fff; position:relative}
.film--bae main::after{content:""; position:fixed; inset:0; pointer-events:none; z-index:1; background:repeating-linear-gradient(0deg, rgba(255,255,255,.025) 0 1px, transparent 1px 3px); mix-blend-mode:screen}
.film--bae main > *{position:relative; z-index:2}

/* hero: title screen. Row 1 is the title and the cabinet, row 2 the briefing and the stats. */
.bae-hero{--wm-o:.1}
.bae-hero .wm-daisy{right:-14%; bottom:-60%}
.bae-hero__g{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); grid-template-areas:"head cab" "txt hud"; gap:clamp(26px,3vw,40px) clamp(28px,4vw,56px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,84px)}
.bae-hero__head{grid-area:head; min-width:0}
.bae-hero__cab{grid-area:cab; min-width:0}
.bae-hero__txt{grid-area:txt; min-width:0; align-self:stretch; display:flex; flex-direction:column; justify-content:space-between; gap:22px}
.bae-hero__hud{grid-area:hud; min-width:0; align-self:stretch}
.bae-hero .crumbs{color:rgba(255,255,255,.62)}
.bae-sub{font-family:var(--px); font-size:clamp(.95rem,1.35vw,1.15rem); line-height:1.35; text-transform:uppercase; color:#15ffc8; margin:0 0 20px}
.bae-title{font-family:var(--px); font-weight:700; font-size:clamp(4rem,9.6vw,8.6rem); line-height:.86; color:#fff; text-shadow:.045em .045em 0 var(--teal), .09em .09em 0 rgba(19,132,143,.4); margin:0 0 .26em; letter-spacing:-.03em; text-transform:uppercase; transform:skewX(-6deg); transform-origin:0 100%; margin-left:-.1em}
.bae-title span{display:block}
.bae-title .mk{padding:0; background:none; color:#15ffc8}
.bae-tag{font-family:var(--px); font-size:clamp(.95rem,1.35vw,1.15rem); line-height:1.4; text-transform:uppercase; color:#fff; margin:0}
.bae-tag::before{content:"\\25B6"; color:#15ffc8; margin-right:.6em; font-size:.8em}
.bae-hero .lede{color:rgba(255,255,255,.92); margin:0}
.bae-hero__txt .btns{gap:10px}
.bae-hero__txt .btn{padding-inline:.95em; font-size:.95rem}
.press{font-family:var(--px); text-transform:uppercase; animation:bae-blink 1s steps(2) 4}
.press:hover{animation:bae-blink .5s steps(2) 2}
@keyframes bae-blink{50%{opacity:.4}}
/* the cabinet */
.cab{padding:14px 16px 0; border-radius:20px 20px 12px 12px; background:linear-gradient(160deg,#1d5a66,#0b2128 70%); box-shadow:0 0 0 3px #15ffc8, 0 0 0 9px rgba(21,255,200,.1), 0 34px 70px -24px rgba(0,0,0,.75)}
.cab__top{display:flex; justify-content:space-between; align-items:center; gap:12px; font-family:var(--px); font-size:.8rem; text-transform:uppercase; color:#15ffc8; padding:0 4px 11px}
.cab__lives{display:flex; gap:6px}
.cab__lives i{width:14px; height:12px; background:var(--pink); clip-path:polygon(0 17%,14% 17%,14% 0,43% 0,43% 17%,57% 17%,57% 0,86% 0,86% 17%,100% 17%,100% 50%,86% 50%,86% 67%,71% 67%,71% 83%,57% 83%,57% 100%,43% 100%,43% 83%,29% 83%,29% 67%,14% 67%,14% 50%,0 50%)}
.cab .vid{border-radius:8px; box-shadow:0 0 0 3px #071a20, 0 0 0 5px rgba(21,255,200,.35)}
.cab__deck{display:flex; align-items:center; gap:clamp(14px,2vw,26px); margin:14px -16px 0; padding:14px 22px 16px; border-top:3px solid #15ffc8; background:#0b2128; border-radius:0 0 12px 12px}
.cab__stick{position:relative; width:46px; height:44px; flex:none}
.cab__stick::before{content:""; position:absolute; left:50%; bottom:0; width:42px; height:13px; margin-left:-21px; border-radius:50%; background:#1d414e; box-shadow:inset 0 -3px 0 #071a20}
.cab__stick::after{content:""; position:absolute; left:50%; bottom:6px; width:6px; height:22px; margin-left:-3px; background:#9fb3b8; border-radius:3px}
.cab__stick i{position:absolute; left:50%; top:0; z-index:1; width:22px; height:22px; margin-left:-11px; border-radius:50%; background:var(--pink); box-shadow:inset -3px -4px 0 rgba(0,0,0,.2), inset 3px 3px 0 rgba(255,255,255,.3)}
.cab__btns{display:flex; gap:10px; flex:none}
.cab__btns i{width:26px; height:26px; border-radius:50%; background:#15ffc8; box-shadow:inset 0 -4px 0 rgba(0,0,0,.28), 0 3px 0 #071a20}
.cab__btns i:nth-child(2){background:#fff; transform:translateY(-6px)} .cab__btns i:nth-child(3){background:#d1feff}
.cab__slot{margin-left:auto; display:flex; align-items:center; gap:10px; font-family:var(--px); font-size:.8rem; text-transform:uppercase; color:#15ffc8; text-align:right}
.cab__slot::after{content:""; width:12px; height:30px; flex:none; border-radius:3px; background:#071a20; border:2px solid #15ffc8; box-shadow:inset 0 0 0 3px #0b2128}
/* the stats HUD */
.hud{display:grid; grid-template-rows:repeat(3,auto); align-content:space-between; height:100%; border:3px solid #15ffc8; border-radius:8px; background:#0b2128}
.hud div{display:grid; grid-template-columns:clamp(5.6rem,9vw,7.6rem) minmax(0,1fr); gap:6px clamp(12px,1.6vw,22px); align-items:center; padding:13px clamp(14px,1.8vw,22px); border-top:3px solid #15ffc8; flex:1}
.hud div:first-child{border-top:0}
.hud b{display:block; font-family:var(--px); font-weight:400; font-size:clamp(2.1rem,3.3vw,3rem); color:#15ffc8; line-height:1; text-shadow:3px 3px 0 var(--teal)}
.hud p{margin:0; font-size:.98rem; line-height:1.45; color:rgba(255,255,255,.92)}
.hud small{font-family:var(--mono); font-size:.72rem; font-weight:600; color:#15ffc8; letter-spacing:.08em; text-transform:uppercase; white-space:nowrap; margin-left:.5em}

/* bands */
.bae-band{padding-block:var(--band)}
.bae-band--alt{background:var(--ind2)}
.bae-band h2{font-family:var(--px); font-weight:400; font-size:clamp(1.8rem,4vw,3.2rem); text-transform:uppercase; line-height:1.05; letter-spacing:0; margin:0}
.bae-band .eyebrow{color:#15ffc8}
.bae-head{margin-bottom:var(--head-gap)}
.bae-head .lede{margin:.7em 0 0; color:rgba(255,255,255,.9)}
.bae-sub2{font-family:var(--px); font-weight:400; font-size:clamp(1.3rem,2.2vw,1.8rem); text-transform:uppercase; line-height:1.1; color:#15ffc8; margin:clamp(34px,4vw,54px) 0 var(--head-gap)}

/* what is BAEcode */
.bae-code{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.bae-code__txt h2{margin-bottom:.55em}
.bae-code__txt p:not(.eyebrow){color:rgba(255,255,255,.9); font-size:1.04rem; line-height:1.65}
.term{display:flex; flex-direction:column; background:#071a20; border:3px solid #15ffc8; border-radius:8px; padding:20px clamp(16px,3vw,28px) 22px; font-family:var(--mono); box-shadow:0 0 40px rgba(21,255,200,.12)}
.term__bar{display:flex; gap:6px; margin-bottom:14px}
.term__bar i{width:12px; height:12px; border-radius:50%; background:var(--pink)} .term__bar i:nth-child(2){background:#fff} .term__bar i:nth-child(3){background:#15ffc8}
.term p{margin:0 0 12px; font-size:clamp(.98rem,1.3vw,1.1rem); line-height:1.5; color:#d9fff6}
.term p::before{content:"> "; color:#15ffc8}
.term p.cmt{color:rgba(255,255,255,.62)} .term p.cmt::before{content:"// "}
.term p:last-child{margin:auto 0 0; padding-top:4px}
/* a quote set as a game dialogue box */
.dlg{position:relative; margin:clamp(34px,4vw,48px) 0 0; padding:clamp(30px,3.4vw,42px) clamp(20px,3.4vw,44px) clamp(24px,3vw,36px); background:#071a20; border:3px solid #fff; border-radius:8px; box-shadow:0 0 0 3px #071a20, 0 0 0 6px #15ffc8, 0 26px 50px -26px rgba(0,0,0,.7)}
.dlg__who{position:absolute; left:clamp(16px,3vw,40px); top:0; transform:translateY(-58%); font-family:var(--px); font-size:.85rem; text-transform:uppercase; padding:7px 12px 6px; background:#15ffc8; color:var(--slate); border:3px solid #071a20; border-radius:6px}
.quote-ella{font-family:var(--px); font-size:clamp(1.1rem,2.1vw,1.7rem); line-height:1.4; color:#fff; margin:0; text-transform:uppercase}
.dlg::after{content:""; position:absolute; right:22px; bottom:16px; border:8px solid transparent; border-top:11px solid #15ffc8; border-bottom:0}

/* missions */
.lvls{display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:10px; margin:0 0 16px}
.lvl{font:inherit; cursor:pointer; text-align:left; background:#0b2128; color:#fff; border:3px solid rgba(21,255,200,.35); border-radius:8px; padding:13px 12px 12px; display:flex; flex-direction:column; gap:7px; min-height:132px; transition:border-color .2s, background .2s, transform .2s var(--ease), box-shadow .2s}
.lvl small{font-family:var(--px); font-size:.72rem; text-transform:uppercase; color:#15ffc8}
.lvl span{font-weight:800; font-size:.95rem; line-height:1.22}
.lvl i{margin-top:auto; font-style:normal; font-family:var(--px); font-size:.7rem; text-transform:uppercase; color:rgba(255,255,255,.5)}
.lvl i::before{content:"\\25CB  to play"}
.lvl.done i{color:#15ffc8} .lvl.done i::before{content:"\\2713  played"}
.lvl[aria-selected="true"] i{color:#fff} .lvl[aria-selected="true"] i::before{content:"\\25B6  playing"}
.lvl:hover{border-color:rgba(21,255,200,.75); transform:translateY(-2px)}
.lvl[aria-selected="true"]{border-color:#15ffc8; background:#1d5a66; box-shadow:0 0 0 3px rgba(21,255,200,.25), 0 0 26px rgba(21,255,200,.25)}
.lvl[aria-selected="true"] small{color:#fff}
.xp{display:flex; align-items:center; gap:14px; margin:0 0 16px; font-family:var(--px); font-size:.8rem; text-transform:uppercase; color:#15ffc8}
.xp__bar{flex:1; height:14px; border:3px solid #15ffc8; border-radius:4px; background:#0b2128; overflow:hidden}
.xp__bar i{display:block; height:100%; width:0; background:repeating-linear-gradient(90deg, #15ffc8 0 10px, transparent 10px 13px); transition:width .4s steps(7)}
.lvlpanel{background:#0b2128; border:3px solid #15ffc8; border-radius:8px; padding:clamp(20px,3vw,36px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(20px,2.6vw,30px) clamp(24px,4.4vw,64px)}
.lvlpanel__top{grid-column:1 / -1; padding-bottom:clamp(18px,2.4vw,26px); border-bottom:3px solid rgba(21,255,200,.3)}
.lvlpanel__col{min-width:0}
.lvlpanel__col + .lvlpanel__col{position:relative}
.lvlpanel__col + .lvlpanel__col::before{content:""; position:absolute; left:calc(clamp(24px,4.4vw,64px) / -2); top:4px; bottom:4px; width:3px; background:rgba(21,255,200,.18)}
.lvlpanel__foot{grid-column:1 / -1; display:flex; justify-content:flex-end; padding-top:clamp(16px,2vw,22px); border-top:3px solid rgba(21,255,200,.3)}
.lvlpanel h3{font-family:var(--px); font-weight:400; text-transform:uppercase; color:#fff; font-size:clamp(1.3rem,2.2vw,1.9rem); line-height:1.15; margin:0 0 .4em}
.lvlpanel h4{font-family:var(--px); font-weight:400; text-transform:uppercase; color:#15ffc8; font-size:.95rem; margin:0 0 10px}
.lvlpanel__top p:last-child{color:rgba(255,255,255,.9); margin:0; font-size:1.08rem}
.lvlpanel ul{margin:0; padding-left:1.15em} .lvlpanel li{color:rgba(255,255,255,.92); font-size:1rem; line-height:1.55; margin:.4em 0}
.lvlpanel li::marker{color:#15ffc8}
.lvlpanel .clip{display:flex; gap:10px; align-items:baseline; font-size:.95rem; color:#d9fff6; margin:0 0 16px; padding:2px 0 2px 12px; border-left:3px solid #15ffc8} .lvlpanel .clip b{font-family:var(--px); font-weight:400; font-size:.74rem; color:#15ffc8; text-transform:uppercase}

/* the Four D's: pick a move */
.ds{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.d{position:relative; background:#0b2128; border:3px solid #15ffc8; border-radius:8px; padding:20px; display:flex; flex-direction:column; gap:12px; min-width:0; transition:transform .2s var(--ease), box-shadow .2s}
.d:hover{transform:translateY(-3px); box-shadow:0 0 0 3px rgba(21,255,200,.2), 0 0 28px rgba(21,255,200,.2)}
.d h3{font-family:var(--px); font-weight:400; text-transform:uppercase; font-size:clamp(1.4rem,2.1vw,1.9rem); line-height:1; color:#15ffc8; margin:0; display:flex; align-items:center; gap:.4em}
.d h3::before{content:"\\25B6"; font-size:.5em; color:#fff; opacity:.35; transition:opacity .2s, transform .2s var(--ease)}
.d:hover h3::before{opacity:1; transform:translateX(3px)}
.d p{margin:0; font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.9)}
.bub{display:block; align-self:start; width:100%; background:#fff; color:var(--ind); border-radius:14px 14px 14px 4px; padding:11px 14px; font-weight:700; font-size:.95rem; line-height:1.35}
.bub + .bub{background:#15ffc8; border-radius:14px 14px 4px 14px}
@supports (grid-template-rows:subgrid){ @media (min-width:561px){ .d{display:grid; grid-template-rows:subgrid; grid-row:span 4; row-gap:12px} } }

/* why people don't step in */
.barriers{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.barriers span{display:flex; align-items:center; min-height:96px; font-family:var(--mono); font-size:.98rem; line-height:1.45; padding:16px 18px; border:2px dashed rgba(255,255,255,.4); border-radius:8px; color:#fff; background:rgba(7,26,32,.35)}
.harm{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.harm div{background:#0b2128; border-radius:8px; padding:20px 22px 22px; border-top:4px solid var(--pink); min-width:0}
.harm h3{font-family:var(--px); font-weight:400; font-size:1.15rem; text-transform:uppercase; color:var(--pink); margin:0 0 12px}
.harm ul{margin:0; padding:0; list-style:none; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px 24px; font-size:.98rem; line-height:1.4; color:rgba(255,255,255,.92)}
.harm li{margin:0; padding-left:18px; position:relative}
.harm li::before{content:""; position:absolute; left:0; top:.48em; width:7px; height:7px; background:var(--pink)}

/* stills */
.stills{display:grid; grid-template-columns:2fr 1fr 1fr; grid-template-rows:auto auto; gap:12px}
.stills button{border:0; padding:0; cursor:zoom-in; border-radius:8px; overflow:hidden; background:#000; box-shadow:0 0 0 3px rgba(21,255,200,.35); transition:box-shadow .2s, transform .2s var(--ease)}
.stills button:hover{box-shadow:0 0 0 3px #15ffc8; transform:translateY(-2px)}
.stills button img{width:100%; height:100%; object-fit:cover; aspect-ratio:16/10}
.stills button:first-child{grid-row:span 2} .stills button:first-child img{aspect-ratio:auto; height:100%}
.bae-note{margin-top:var(--gap); background:#0b2128; border:3px solid rgba(21,255,200,.4); border-radius:8px; color:#fff}
.bae-note summary{list-style:none; cursor:pointer; display:flex; align-items:center; justify-content:space-between; gap:14px; min-height:56px; padding:14px 20px; font-family:var(--px); font-size:.95rem; text-transform:uppercase}
.bae-note summary::-webkit-details-marker{display:none}
.bae-note summary::after{content:"+"; font-size:1.3rem; color:#15ffc8}
.bae-note[open] summary::after{content:"\\2013"}
.bae-note p{margin:0; padding:0 20px 20px; font-size:1rem; line-height:1.65; color:rgba(255,255,255,.9)}
.film--bae .qa{--qa-line:rgba(255,255,255,.15)}

@media (max-width:1100px){
  .lvls{grid-template-columns:repeat(12,minmax(0,1fr))} .lvl{grid-column:span 3; min-height:112px} .lvl:nth-child(n+5){grid-column:span 4}
  .barriers{grid-template-columns:repeat(2,minmax(0,1fr))} .barriers span{min-height:76px}
  .ds{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:960px){
  .bae-hero__g{grid-template-columns:minmax(0,1fr); grid-template-areas:"head" "cab" "txt" "hud"}
  .bae-title{font-size:clamp(4rem,22.5vw,8.6rem)}
  .bae-code{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:760px){
  .lvlpanel{grid-template-columns:minmax(0,1fr)} .lvlpanel__col + .lvlpanel__col::before{display:none} .lvlpanel__foot{justify-content:flex-start}
  .hud div{grid-template-columns:4.6rem minmax(0,1fr); align-items:start} .hud b{font-size:1.9rem; padding-top:4px} .hud small{display:block; margin:6px 0 0; white-space:normal}
  .lvls{grid-template-columns:repeat(2,minmax(0,1fr))} .lvl, .lvl:nth-child(n+5){grid-column:auto} .lvls > :last-child{grid-column:1/-1; min-height:0}
  .harm{grid-template-columns:minmax(0,1fr)}
  .stills{grid-template-columns:1fr 1fr} .stills button:first-child{grid-column:span 2; grid-row:auto} .stills button:first-child img{aspect-ratio:16/10}
}
@media (max-width:560px){
  .ds, .barriers{grid-template-columns:minmax(0,1fr)} .barriers span{min-height:0}
  .harm ul{grid-template-columns:minmax(0,1fr)}
  .cab{padding:10px 10px 0} .cab__deck{margin-inline:-10px; padding:12px 14px 14px} .cab__top{font-size:.72rem} .cab__slot{font-size:.72rem}
}
'''

LEVELS = [
 ('Pregame', 'The Safety Plan', 'Talk about safety in the car, before the party.', 'Play the clip of Jamie and her friends in the car',
  ['Have you ever been a BAEstander, or seen someone else step in? What happened?', 'There are usually assumptions about what’s going to happen at a party. How can looking out for one another be part of that conversation?', 'The group already has a designated driver. What else can they do to take care of themselves and each other once they arrive?'],
  ['Create an action plan together: “If this happens, then…”', 'Choose a code word or signal that means “I need help.”', 'Check in with at least one person before going upstairs, outside, or leaving.', 'Talk openly about how alcohol and drugs affect consent. If you aren’t sober, you cannot consent. If they aren’t sober, they cannot consent. Period.']),
 ('Mission 1', 'Take Notice & Identify Problems', 'Jamie starts keeping an eye on her friends.', 'Play the clip of Jamie watching out for her friends at the party',
  ['If Jamie knows Ryan and the other student have hooked up before, should she just let it go? Why or why not?', 'If all of Jamie’s distraction attempts had failed, what other D’s could she have used? Which ones feel most realistic for you in your school or social settings?', 'What are other simple distraction techniques you could use at school, at parties or on the bus?', 'If the guy Ryan was going upstairs with resisted Jamie’s distraction, what else could she have done?'],
  ['Hook up, make out, fool around and sex can mean different things to different people. Saying yes to one thing does not mean agreeing to something more.', 'Consent should never be assumed from past sexual behavior. People who have hooked up before still need to give clear consent every time.', 'Distraction ideas: ask a random question (“I love that shirt, where’d you get it?”), pause the music, ask about homework or a game, “accidentally” bump into someone, show them something on your phone.']),
 ('Mission 2', 'Buy Some Time to Exit', 'Jamie steps in for Grace.', 'Play the next clip and ask which “D” Jamie used',
  ['What do you think Grace is thinking and feeling in this scene? How can you tell?', 'What about the guy? What cues do you notice?', 'What are some verbal or physical ways to find out if someone is actually interested in sexual activity?', 'Could the group have kept intervening as the guy shifted his attention to Michelle? What else might they have done?'],
  ['“No” or “I’m not sure” is not an invitation to keep trying. Pushing after someone hesitates is coercive.', 'Consent requires honesty and clarity. Both people must have the same understanding of what’s happening.', 'Consent is reversible. Once someone changes their mind, the activity must stop immediately, with no guilting and no pressure.', 'Without clear verbal consent, unwanted sexual activity is sexual assault.']),
 ('Bonus', 'From BroCode to BAEcode', 'David decides to step in.', 'Play the clip of David and his teammate',
  ['Why do you think David decides to intervene? Why not the other guy?', 'What has David learned from watching Jamie throughout the evening?', 'Was it risky for David to step in, physically or socially?', 'David uses humor but doesn’t directly address the problem. What’s the missing conversation with his teammate?', 'Should David make sure his teammate is confronted so he doesn’t repeat the behavior with someone else?'],
  ['David notices his teammate is intentionally trying to get someone drunk, a clear warning sign.', 'Alcohol affects communication and can increase aggression. It can’t be blamed for “causing” assault, but it often plays a major role in unsafe encounters.', 'Your own safety always comes first. If a situation turns violent or heated, call for help from a trusted friend, an adult or the authorities.']),
 ('Mission 3', 'Get Samantha Out', 'Jamie uses her phone to get a friend out of the party.', 'Play the clip of Jamie and Samantha',
  ['Why do you think Jamie decides to take a video of Samantha instead of ignoring her?', 'What “evidence” is Jamie referring to, and why does she see the situation as a problem?', 'What are the positive and negative sides of using a phone as an intervention tool?'],
  ['Warning signs like intoxication or isolation are often precursors to sexual violence. Jamie decided it was better to be safe and get her friend out.', 'Once something is online, it’s nearly impossible to erase. Jamie used the video to remind her friend that digital evidence is permanent.', 'Phones can help by documenting concerns or creating a distraction, but videos can also be shared without consent and used to shame or re-traumatize survivors.']),
 ('Side quest', 'Consent Doesn’t Have to Be Awkward', 'David asks Jamie.', 'Play the clip of David and Jamie',
  ['What body language do you notice between David and Jamie?', 'How does it feel when someone asks permission? How does it feel when they don’t?', 'Brainstorm: how can you ask for enthusiastic consent without “ruining the mood”?'],
  ['If someone says “yes” but their body language says “maybe,” step back, slow down or stop.', 'Asking directly communicates care and respect. The ability to ask for and honor consent is always appealing.', 'Silence is not consent. The absence of a “no” is not consent. Buying dinner, giving someone a ride, or going to someone’s room is not consent.']),
 ('Postgame', 'Reflections', 'Take it home.', 'Wrap up the session',
  ['How will you share what you’ve learned with your friends?', 'What does being a BAEstander look like for you from now on?'],
  ['You may not be able to help in every situation, and you might never know whether your actions worked. Bystanders need to forgive themselves for not solving every problem.', 'Your choice to act can make you a role model. Each time you step up, it becomes more likely that others will too.', 'After an assault, a BAEstander listens, responds with kindness, asks what they need, and helps connect them to resources without pressure.']),
]

def build():
    tabs = ''.join(f'<button class="lvl" role="tab" id="lv-{i}" aria-controls="lvp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(a_)}</small><span>{esc(t)}</span><i aria-hidden="true"></i></button>' for i, (a_, t, *_r) in enumerate(LEVELS))
    panels = ''.join(f'''<div class="lvlpanel" role="tabpanel" id="lvp-{i}" aria-labelledby="lv-{i}"{"" if i==0 else " hidden"}><div class="lvlpanel__top"><p class="clip"><b>Clip</b>{esc(clip)}</p><h3>{esc(a_)}: {esc(t)}</h3><p>{esc(obj)}</p></div><div class="lvlpanel__col"><h4>Discussion questions</h4><ul>{"".join(f"<li>{esc(q)}</li>" for q in qs)}</ul></div><div class="lvlpanel__col"><h4>Key teaching points</h4><ul>{"".join(f"<li>{esc(k)}</li>" for k in keys)}</ul></div>{f'<div class="lvlpanel__foot"><button class="btn btn--mint btn--sm lvlnext" type="button" data-next-lvl="{i+1}">Next: {esc(LEVELS[i+1][0])}<span class="arr" aria-hidden="true">&rarr;</span></button></div>' if i+1 < len(LEVELS) else ''}</div>''' for i, (a_, t, obj, clip, qs, keys) in enumerate(LEVELS))
    ds = [('Distract', 'Divert attention to give someone a safe chance to exit. It avoids direct confrontation and can de-escalate quickly.', ['Hey, come to the bathroom with me.', 'We need to leave, we have a big game tomorrow.']),
          ('Delegate', 'Ask someone else for help if you don’t feel comfortable stepping in alone: a friend, coach, staff member or parent.', ['Will you come check on Tanya with me?', 'Call or text for backup.']),
          ('Direct', 'Address the behavior directly by naming it or telling the person to stop.', ['They’ve had enough. Leave them alone.', 'This isn’t okay. You need to stop. Now.']),
          ('Delay', 'If you can’t step in during the moment, you can always follow up afterward.', ['Hey, you seemed upset. Are you okay?', 'Do you need me to call someone for you?'])]
    dhtml = ''.join(f'<div class="d"><h3>{esc(n)}</h3><p>{esc(t)}</p>' + ''.join(f'<span class="bub">“{esc(x)}”</span>' for x in ex) + '</div>' for i, (n, t, ex) in enumerate(ds))
    barriers = ['It’s none of my business.', 'Someone else will step in.', 'I’m not sure if what I’m seeing is really crossing the line.', 'I don’t want people to be mad at me.', 'If I say something, it might start a fight.', 'I don’t know what to say.', 'I don’t want to cause a scene.', 'I don’t like how they’re acting, but I’ll just stay out of it.']
    harm = [('Verbal', ['Spreading rumors', 'Catcalling', 'Making offensive jokes', 'Name-calling or insulting language', 'Pressuring someone', 'Repeatedly asking someone out after they’ve said no']),
            ('Cyber', ['Posting harmful content on social media', 'Sending unwanted or harassing texts', 'Sending harassing or threatening emails', 'Sharing pictures without consent', 'Pressuring someone to send nude photos']),
            ('Nonverbal', ['Making obscene gestures', 'Writing sexually explicit things about someone', 'Intimidating someone to stop them from reporting harm']),
            ('Physical', ['Unwanted touching or kissing', 'Following or stalking someone', 'Taking someone’s picture without permission'])]
    hhtml = ''.join(f'<div><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in xs)}</ul></div>' for t, xs in harm)
    stills = [('gameon8', 'Game On!'), ('image-4', 'Choose your path'), ('image-3', 'GAME ON! Because stepping in should be everyone’s game'), ('gameon1', 'Game On! still'), ('gameon3', 'Game On! still')]
    sh = ''.join(f'<button type="button" data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c in stills)
    body = f'''
<section class="bae-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap bae-hero__g">
    <div class="bae-hero__head rise">
      {film_crumbs('BAEcode: Game On!')}
      <p class="bae-sub">BAEcode: Teaching Bystander Intervention</p>
      <h1 class="bae-title"><span>Game</span><span class="mk">On!</span></h1>
      <p class="bae-tag">Because stepping in should be everyone’s game.</p>
    </div>
    <div class="bae-hero__cab"><div class="cab" id="film"><div class="cab__top"><span>Player 1: Jamie</span><span class="cab__lives" aria-hidden="true"><i></i><i></i><i></i></span></div>{yt('BCqkJSXCu-E', 'GAME ON!', thumb='gameon5', label='Full film')}<div class="cab__deck"><span class="cab__stick" aria-hidden="true"><i></i></span><span class="cab__btns" aria-hidden="true"><i></i><i></i><i></i></span><span class="cab__slot">Insert coin: free</span></div></div></div>
    <div class="bae-hero__txt">
      <p class="lede">Created with teens, for teens by SafeBAE co-founder Ella Fairon, this short film shows everyday situations and gives young people simple, practical strategies to step in, in person or online.</p>
      <div class="btns"><a class="btn btn--mint press" href="#film">Press start</a>{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div class="bae-hero__hud"><div class="hud"><div><b>44%</b><p>The presence of a bystander makes a completed rape 44% less likely. <small>Clay-Warner, 2002</small></p></div><div><b>17%</b><p>Sexual violence rates fell by 17% on U.S. campuses that trained students in bystander intervention. <small>Green Dot</small></p></div><div><b>30%</b><p>A bystander is present in roughly 30% of sexual assaults, including threats of rape or unwanted sexual contact. <small>Associated Press</small></p></div></div></div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap">
    <div class="bae-code">
      <div class="bae-code__txt">
        <p class="eyebrow">What is BAEcode?</p>
        <h2>Flip the Bro Code.</h2>
        <p>“Bro code” means protecting your friend above all else, even at someone else’s expense. BAEcode flips that script. Instead of loyalty to a small circle, it’s a commitment to look out for anyone who might need help, whether or not they’re your friend.</p>
        <p>SafeBAE launched the campaign during Sexual Assault Awareness Month in 2018 to give teens the tools and confidence to practice bystander intervention, and to prevent sexual harassment and assault within their own peer groups.</p>
      </div>
      <div class="term" role="list" aria-label="The BAEcode">
        <div class="term__bar" aria-hidden="true"><i></i><i></i><i></i></div>
        <p class="cmt">baecode.txt</p>
        <p role="listitem">Watch out for everyone’s safety, not just your close friends.</p>
        <p role="listitem">Never pressure someone into sexual activity of any kind.</p>
        <p role="listitem">Don’t ever send unrequested nude photos.</p>
        <p role="listitem">Always get enthusiastic consent before and during any sexual activity.</p>
        <p class="cmt">anyone can learn to de-escalate a situation where consent has not, or cannot, be given</p>
      </div>
    </div>
    <figure class="dlg"><figcaption class="dlg__who">Ella Fairon, Director</figcaption><blockquote style="margin:0"><p class="quote-ella">“The idea is simple: many cases of sexual violence can be prevented or stopped if an alert bystander intervenes in time.”</p></blockquote></figure>
  </div>
</section>

<section class="bae-band" id="missions">
  <div class="wrap">
    <div class="bae-head"><p class="eyebrow">Seven clips, one mission at a time</p>
    <h2>Play it mission by mission.</h2>
    <p class="lede">Watch the full film once and gather first reactions: What stood out? What felt realistic, and what didn’t? What makes stepping in hard? Then replay each clip and work through the mission.</p></div>
    <div data-tabs="baecode"><div class="lvls" role="tablist" aria-label="Missions">{tabs}</div><div class="xp" aria-hidden="true"><span id="xpl">Clip 1 of 7</span><span class="xp__bar"><i id="xpb"></i></span></div>{panels}</div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap">
    <div class="bae-head"><p class="eyebrow">Bystander strategies</p>
    <h2>The Four D’s</h2>
    <p class="lede">Jamie uses distraction, but it isn’t the only tool. BAEstanders have four strategies, and bystander intervention works best when friends share the responsibility.</p></div>
    <div class="ds">{dhtml}</div>
  </div>
</section>

<section class="bae-band">
  <div class="wrap">
    <div class="bae-head"><h2>Why people don’t step in</h2><p class="lede">Without talking about it or giving people easy strategies, most bystanders do nothing. Intervening can be intimidating even for adults, and young people face extra social pressure. Research shows that when teens learn practical strategies, harassment and sexual assault go down.</p></div>
    <div class="barriers">{''.join(f'<span>“{esc(b)}”</span>' for b in barriers)}</div>
    <h3 class="bae-sub2">Know what to look for</h3>
    <div class="harm">{hhtml}</div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap">
    <div class="bae-head"><p class="eyebrow">From the film and campaign</p><h2>Made by students</h2>
    <p class="lede">The entire production team, from writing and directing to casting, was high school and college students.</p></div>
    <div class="stills" data-gallery>{sh}</div>
    <details class="bae-note"><summary>Alcohol, consent and Game On!</summary><p>SafeBAE does not condone, encourage or endorse underage drinking. In a recent national survey, 10% of 8th graders and 35% of 12th graders reported drinking in the past 30 days. Youth who drink are more likely to experience sexual assault, and about half of adolescent sexual assault victims seen in emergency departments report that alcohol or other substances were used immediately before the assault. SafeBAE developed GAME ON! using a reality-based education model, because bystander education has to be honest, relatable and comprehensive.</p></details>
  </div>
</section>

{begin('bae-band', 'These conversations can surface strong emotions and may lead to disclosures of abuse.')}
{tail('baecode', ['dating', 'rape-culture', 'red-flags'], 'bae-band bae-band--alt')}
'''
    js = r'''<script>
(function(){
  var tabs = [].slice.call(document.querySelectorAll('.lvl')), l = document.getElementById('xpl'), b = document.getElementById('xpb');
  function upd(){ var i = 0; tabs.forEach(function(t, k){ if(t.getAttribute('aria-selected')==='true'){ i = k; t.classList.add('done'); } }); if(l) l.textContent = 'Clip ' + (i+1) + ' of ' + tabs.length; if(b) b.style.width = ((i+1)/tabs.length*100) + '%'; }
  var mo = new MutationObserver(upd); tabs.forEach(function(t){ mo.observe(t, {attributes:true, attributeFilter:['aria-selected']}); }); upd();
  document.querySelectorAll('[data-next-lvl]').forEach(function(n){ n.addEventListener('click', function(){ var t = tabs[+n.dataset.nextLvl]; if(t){ t.click(); t.focus({preventScroll:true}); var top = document.querySelector('.lvls').getBoundingClientRect().top + window.scrollY - 120; if(window.scrollY > top) window.scrollTo({top: top, behavior: 'smooth'}); } }); });
})();
</script>'''
    film_page('film-baecode-game-on.html', 'BAEcode: Game On!', 'BAEcode: Game On! is SafeBAE’s bystander intervention film and teaching guide, made by high school and college students.', body, 'bae', 'family=Silkscreen:wght@400;700', CSS, js)
