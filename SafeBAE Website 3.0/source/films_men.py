from films_common import *

# Sexual Assault of Men: Theo's story.
# A calm, dark page. The title plate is taken from the teaching guide's cover (wide spaced capitals on a
# SafeBAE Teal block); Theo's testimony sits beside it in its original colour. The stencil face appears in
# one place only: "the rules boys are taught", which the reader crosses out.

CSS = '''
.film--men{--st:'Saira Stencil One',var(--display); --m-bg:#13303a; --m-deep:#0e252d; --m-card:rgba(255,255,255,.05); --m-line:rgba(255,255,255,.14);
  --f-card:#0e252d; --f-line:rgba(255,255,255,.12); --f-ink:#fff; --f-ink2:rgba(255,255,255,.84); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint);
  --f-disp:var(--display); --f-dw:800; --f-dt:uppercase; --f-dl:.035em; --f-ds:118%}
.film--men main{background:var(--m-bg) var(--grain); color:#fff}

/* hero: Theo's testimony and the cover's title plate hang level; the summary and the actions sit under them */
.mn-hero{--wm-o:.13}
.mn-hero .wm-daisy{right:-12%; bottom:-50%}
.mn-hero__g{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); grid-template-areas:"crumbs crumbs" "vid head" "txt act"; gap:clamp(22px,2.6vw,34px) clamp(28px,4vw,56px); align-items:start; padding-block:clamp(36px,4.4vw,60px) clamp(48px,6vw,84px)}
.mn-hero__crumbs{grid-area:crumbs; min-width:0; margin-bottom:-8px}
.mn-hero__crumbs .crumbs{margin:0; color:rgba(255,255,255,.66)}
.mn-hero__head{grid-area:head; align-self:stretch; display:flex; flex-direction:column; min-width:0; container-type:inline-size}
.mn-hero__vid{grid-area:vid; min-width:0}
.mn-hero__act{grid-area:act; min-width:0}
.mn-hero__txt{grid-area:txt; min-width:0}
.mn-hero .eyebrow{margin:0 0 1.1rem}
.mn-plate{flex:1; display:flex; flex-direction:column; justify-content:center; margin:0; padding:clamp(22px,2.6vw,34px) 32px; border-radius:var(--r-xl); background:var(--teal); color:#fff; box-shadow:inset 0 0 0 6px rgba(14,37,45,.5), 0 30px 60px -34px rgba(0,0,0,.7);
  font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; letter-spacing:.09em; font-size:min(4.2rem, calc((100cqi - 64px) / 6.85)); line-height:1.04}
.mn-plate span{display:block}
.mn-plate .mk{padding:0; background:none; color:var(--mint)}
/* Theo is named in the film's own lower third, so the player's title bar is not drawn over it */
.mn-hero__vid .vid{border-radius:var(--r-xl)}
.mn-hero__vid .vid__label{display:none}
.mn-hero__vid .vid__play{place-items:end; padding:clamp(14px,2vw,24px)}
.mn-hero__vid .vid__play span{width:72px; height:72px}
.mn-hero .lede{color:rgba(255,255,255,.94); margin:0}
.mn-hero__act .btns{flex-direction:column; align-items:stretch; gap:12px}

/* bands and heads */
.mn-band{padding-block:var(--band); position:relative}
.mn-band--alt{background:var(--m-deep) var(--grain)}
.mn-band--mint{background:var(--mint); color:var(--slate); padding-block:clamp(40px,5vw,68px)}
.mn-band h2{font-family:var(--display); font-weight:800; font-stretch:118%; text-transform:uppercase; letter-spacing:.035em; font-size:clamp(1.75rem,3.4vw,2.8rem); line-height:1.06; margin:0}
.mn-band .eyebrow{color:var(--mint)}
.film--men .gpanel h2{font-size:clamp(1.75rem,3.4vw,2.8rem); line-height:1.06}
.mn-head{margin-bottom:var(--head-gap)}
.mn-head .lede{margin:.7em 0 0; color:rgba(255,255,255,.92)}
.mn-ask{display:grid; grid-template-columns:auto minmax(0,1fr); gap:6px 24px; align-items:center; margin:var(--gap) 0 0; padding:20px var(--pad-card); border-radius:var(--r-xl); border:1.5px solid rgba(21,255,200,.5); background:rgba(21,255,200,.06)}
.mn-ask b{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--mint)}
.mn-ask span{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.15rem; line-height:1.4}
.mn-ask small{grid-column:2; font-size:.95rem; line-height:1.55; color:rgba(255,255,255,.84)}

/* one in six */
.mn-six{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:center}
.mn-six__n{margin:0; font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(4.4rem,9.6vw,8.6rem); line-height:.84; letter-spacing:-.03em; white-space:nowrap}
.mn-six__fig{display:flex; gap:clamp(8px,1.2vw,16px); margin-top:clamp(16px,2vw,24px); max-width:440px}
.mn-six__fig svg{flex:1 1 0; min-width:0; height:auto; fill:none; stroke:var(--slate); stroke-width:3.5; stroke-linejoin:round; overflow:visible}
.mn-six__fig svg:first-child{fill:var(--slate)}
.mn-six__lead{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:clamp(1.5rem,2.9vw,2.5rem); line-height:1.12; margin:0 0 .5em; text-wrap:balance}
.mn-six__txt p:last-child{margin:0; font-size:var(--fs-lede); line-height:1.5; font-weight:600}

/* after the film: prompts beside the poster, ending level */
.mn-disc{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.mn-qs{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:12px}
.mn-qs li{flex:1 1 auto; display:flex; align-items:center; margin:0; padding:14px 22px; border-radius:16px; background:var(--m-card); border:1px solid var(--m-line); font-weight:600; font-size:1.02rem; line-height:1.5}
.mn-poster{margin:0; min-width:0; display:flex; flex-direction:column; gap:12px}
.mn-poster button{display:block; width:100%; aspect-ratio:1; border:0; padding:0; border-radius:var(--r-xl); overflow:hidden; background:var(--teal); cursor:zoom-in; box-shadow:0 30px 60px -34px rgba(0,0,0,.7); transition:transform .3s var(--ease)}
.mn-poster button:hover{transform:translateY(-4px)}
.mn-poster img{width:100%; height:100%; object-fit:cover}
.mn-poster figcaption{display:flex; justify-content:space-between; align-items:baseline; gap:8px 20px; flex-wrap:wrap; margin-top:auto; font-size:.95rem; color:rgba(255,255,255,.84)}
.mn-poster figcaption a{color:var(--mint); font-weight:800}

/* myth or fact: wide cards that turn over */
.mn-myth{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.film--men .flip{min-height:168px; border-radius:var(--r-xl); transition:transform .25s var(--ease)}
.film--men .flip:hover{transform:translateY(-3px)}
.film--men .flip__face{border-radius:var(--r-xl); padding:var(--pad-card); gap:12px}
.film--men .flip__face--front{background:var(--m-bg); border:2px solid rgba(21,255,200,.4)}
.film--men .flip__face--back{background:var(--mint)}
.film--men .flip__tag{font-size:.72rem}
.film--men .flip__face--front .flip__tag{color:var(--mint)}
.film--men .flip__txt{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(1.25rem,1.8vw,1.5rem); line-height:1.2; margin-block:auto; text-wrap:balance}
.film--men .flip__face--back .flip__txt{font-family:var(--body); font-stretch:100%; font-weight:600; font-size:1.04rem; line-height:1.5; text-wrap:pretty}
.film--men .flip__face .hint{margin-top:0; font-size:.875rem; font-weight:700; opacity:1; display:flex; align-items:center; gap:.5em}
.film--men .flip__face .hint::after{content:"\\2192"; transition:transform .2s var(--ease)}
.film--men .flip:hover .hint::after{transform:translateX(4px)}
@media (prefers-reduced-motion:no-preference){ .film--men .flip[aria-pressed="true"] .flip__in{transform:rotateX(180deg)} .film--men .flip__face--back{transform:rotateX(180deg)} }

/* the rules boys are taught: stencilled on, then crossed out */
.mn-rules{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.mn-rules__col{display:flex; flex-direction:column; gap:10px; min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--m-deep); border:1px solid var(--m-line)}
.mn-rules__col h3{font-family:var(--mono); font-weight:600; font-stretch:100%; font-size:.8rem; line-height:1.4; letter-spacing:.12em; text-transform:uppercase; color:var(--mint); margin:0 0 6px}
.mn-rules__col ul{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:10px}
.mn-rules__col:first-child ul{flex:1} .mn-rules__col:first-child li{flex:1 1 auto}
.mn-rules__col li{display:flex; align-items:center; min-height:72px; margin:0; padding:12px 18px; border-radius:12px; background:rgba(255,255,255,.05); font-family:var(--st); font-weight:400; font-size:clamp(1.1rem,1.65vw,1.42rem); line-height:1.16; letter-spacing:.04em; text-transform:uppercase; transition:color .4s}
.mn-rules__col li em{font-style:normal; background:linear-gradient(var(--coral),var(--coral)) no-repeat 0 54%/0 4px; -webkit-box-decoration-break:clone; box-decoration-break:clone; transition:background-size .45s var(--ease)}
.mn-rules.challenged li{color:rgba(255,255,255,.5)}
.mn-rules.challenged li em{background-size:100% 4px}
.mn-rules.challenged .mn-rules__col:nth-child(1) li:nth-child(2) em{transition-delay:.12s} .mn-rules.challenged .mn-rules__col:nth-child(1) li:nth-child(3) em{transition-delay:.24s} .mn-rules.challenged .mn-rules__col:nth-child(1) li:nth-child(4) em{transition-delay:.36s} .mn-rules.challenged .mn-rules__col:nth-child(1) li:nth-child(5) em{transition-delay:.48s}
.mn-rules.challenged .mn-rules__col:nth-child(2) li:nth-child(1) em{transition-delay:.6s} .mn-rules.challenged .mn-rules__col:nth-child(2) li:nth-child(2) em{transition-delay:.72s} .mn-rules.challenged .mn-rules__col:nth-child(2) li:nth-child(3) em{transition-delay:.84s}
.mn-chal{flex:1; display:flex; min-height:154px}
.mn-chal__go{flex:1; display:flex; align-items:center; justify-content:space-between; gap:16px; padding:18px 24px; border:0; border-radius:12px; background:var(--mint); color:var(--slate); cursor:pointer; font-family:var(--st); font-weight:400; font-size:clamp(1.3rem,2.1vw,1.85rem); line-height:1.1; letter-spacing:.04em; text-transform:uppercase; text-align:left; box-shadow:0 5px 0 rgba(0,0,0,.28); transition:transform .18s var(--ease), box-shadow .18s var(--ease)}
.mn-chal__go:hover{transform:translateY(-2px); box-shadow:0 7px 0 rgba(0,0,0,.28)}
.mn-chal__go:active{transform:translateY(2px); box-shadow:0 2px 0 rgba(0,0,0,.28)}
.mn-chal__go i{flex:none; position:relative; width:54px; height:54px; border-radius:50%; background:var(--slate)}
.mn-chal__go i::before{content:""; position:absolute; left:13px; right:13px; top:50%; height:5px; margin-top:-2.5px; border-radius:9px; background:var(--coral); transform:rotate(-12deg)}
.mn-chal__after{flex:1; display:flex; flex-direction:column; align-items:flex-start; justify-content:center; gap:12px; padding:16px 20px; border-radius:12px; border:2px solid var(--mint); background:rgba(21,255,200,.07)}
.mn-chal__after p{margin:0; font-size:1rem; line-height:1.5; font-weight:600}

/* know the terms: a four-row glossary */
.mn-defs{margin:0; border-top:1px solid var(--m-line)}
.mn-defs div{display:grid; grid-template-columns:minmax(0,4fr) minmax(0,8fr); gap:6px clamp(24px,4vw,56px); align-items:baseline; padding:20px 0; border-bottom:1px solid var(--m-line)}
.mn-defs dt{font-family:var(--display); font-weight:800; font-stretch:114%; letter-spacing:.03em; text-transform:uppercase; font-size:clamp(1.2rem,1.9vw,1.55rem); line-height:1.12; color:var(--mint)}
.mn-defs dd{margin:0; color:rgba(255,255,255,.92); font-size:1.06rem; line-height:1.55}

/* your role: seven ways to respond, and where to read more */
.mn-respond{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.mn-respond > *{display:flex; flex-direction:column; gap:8px; min-width:0; padding:22px 22px 24px; border-radius:var(--r-xl); background:var(--m-card); border:1px solid var(--m-line); color:#fff}
.mn-respond b{display:block; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.25rem; line-height:1.15}
.mn-respond p{margin:0; font-size:.98rem; line-height:1.5; color:rgba(255,255,255,.86)}
.mn-tick{width:30px; height:30px; border-radius:9px; background:var(--mint); display:grid; place-items:center; margin-bottom:6px}
.mn-tick::after{content:""; width:7px; height:13px; border:solid var(--slate); border-width:0 3px 3px 0; transform:translateY(-2px) rotate(45deg)}
.mn-respond a{background:var(--mint); border-color:var(--mint); color:var(--slate); text-decoration:none; transition:transform .25s var(--ease), box-shadow .25s var(--ease)}
.mn-respond a:hover{transform:translateY(-4px); box-shadow:var(--shadow-soft)}
.mn-respond a p{color:var(--slate)}
.mn-respond a .mn-tick{background:var(--slate)}
.mn-respond a .mn-tick::after{width:9px; height:9px; border-color:var(--mint); border-width:3px 3px 0 0; transform:translateX(-2px) rotate(45deg)}
.mn-respond a i{font-style:normal; font-weight:800; font-size:.95rem; margin-top:auto; padding-top:6px; display:inline-flex; gap:.45em}
.mn-respond a i::after{content:"\\2192"; transition:transform .2s var(--ease)}
.mn-respond a:hover i::after{transform:translateX(4px)}
@supports (grid-template-rows:subgrid){ @media (min-width:1001px){ .mn-respond > *{display:grid; grid-template-rows:subgrid; grid-row:span 3; row-gap:8px; align-content:start} .mn-respond a{grid-template-rows:auto auto 1fr; display:flex} } }

/* different identities */
.mn-stats{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.mn-stats div{min-width:0; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--m-card); border:1px solid var(--m-line)}
.mn-stats b{display:block; font-family:var(--display); font-weight:900; font-stretch:122%; font-size:clamp(2.4rem,4vw,3.5rem); color:var(--mint); line-height:1; letter-spacing:-.02em}
.mn-stats p{margin:12px 0 0; font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.88)}

@media (max-width:1140px){
  .mn-disc{grid-template-columns:minmax(0,1fr)}
  .mn-poster{display:grid; grid-template-columns:minmax(0,132px) minmax(0,1fr); align-items:center; gap:20px; padding:14px 22px 14px 14px; border-radius:var(--r-xl); background:var(--m-card); border:1px solid var(--m-line)}
  .mn-poster button{border-radius:12px; box-shadow:none}
  .mn-poster figcaption{margin-top:0; font-size:1rem}
}
@media (max-width:1000px){
  .mn-respond, .mn-stats{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:960px){
  .mn-hero__g{grid-template-columns:minmax(0,1fr); grid-template-areas:"crumbs" "head" "vid" "txt" "act"}
  .mn-plate{padding-block:clamp(26px,6vw,44px)}
  .mn-hero__act .btns{flex-direction:row; flex-wrap:wrap}
}
@media (max-width:760px){
  .mn-six, .mn-myth, .mn-rules, .mn-defs div{grid-template-columns:minmax(0,1fr)}
  .mn-ask{grid-template-columns:minmax(0,1fr)} .mn-ask small{grid-column:1}
  .mn-chal{min-height:104px}
}
@media (max-width:560px){
  .mn-respond, .mn-stats{grid-template-columns:minmax(0,1fr)}
  .mn-poster{grid-template-columns:minmax(0,96px) minmax(0,1fr); gap:16px; padding-right:16px}
  .mn-rules__col li{min-height:60px}
}
'''

MYTHS = [('Men are too strong to be assaulted.', 'Strength does not prevent sexual violence. At least one in six men will experience sexual abuse or assault.'),
         ('Only gay men commit sexual violence.', 'Sexual violence is about power and control, not sexual orientation. Survivors and perpetrators can be of any gender or identity.'),
         ('Men always want sex and welcome all sexual advances.', 'Sexual assault is never wanted. It is a traumatic experience for any survivor, regardless of gender.'),
         ('Men abused by women “got lucky.”', 'Sexual violence is never a privilege. Women can and do sexually abuse or assault boys and men. Survivors are not “lucky”; they are harmed and exploited.')]

PROMPTS = ['What are your initial thoughts or feelings after watching the video?', 'Can you think of examples in the media where victims were not believed because of their gender?', 'Which cultural norms or stereotypes fuel the belief that men cannot be victims of sexual violence? For example, the idea that men are always open to sex, or that they can always defend themselves.', 'How can we work together to reduce stigma and increase support for male survivors?', 'How might race, sexuality, gender identity or disability shape men’s experiences of sexual violence and disclosure?']

RESPOND = [('Believe them', 'Take their words seriously. Doubt can cause deep harm.'), ('Listen', 'Let them share at their own pace. Don’t push for details.'), ('Don’t dismiss it', 'Avoid minimizing or questioning their feelings, especially because of gender.'), ('Allow their emotions', 'Give space for anger, fear, sadness or relief.'), ('Don’t pressure them to report', 'Whether to report is their choice.'), ('Review options together', 'Share resources, and let them decide what feels right.'), ('Keep showing up', 'Check in, stay present, and keep connecting them with help when they’re ready.')]

FIG = '<svg viewBox="0 0 44 78" aria-hidden="true" focusable="false"><circle cx="22" cy="13" r="10.5"/><path d="M4 76V48a18 18 0 0 1 36 0v28z"/></svg>'

def build():
    myths = ''.join(f'<button class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span><span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{esc(f)}</span><span class="hint">Tap to turn it back</span></span></span></button>' for m, f in MYTHS)
    rh = ''.join(f'<div><span class="mn-tick" aria-hidden="true"></span><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in RESPOND)
    rh += '<a href="survivor-support.html#when-someone-tells-you"><span class="mn-tick" aria-hidden="true"></span><b>More on supporting a survivor</b><p>What to say, and what to avoid.</p><i>Survivor Support</i></a>'
    qs = ''.join(f'<li>{esc(q)}</li>' for q in PROMPTS)
    poster_cap = 'Statistically, guys are more likely to be sexually assaulted than they are to be falsely accused of rape.'
    body = f'''
<section class="mn-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap mn-hero__g">
    <div class="mn-hero__crumbs">{film_crumbs('Supporting Male Survivors')}</div>
    <div class="mn-hero__head rise">
      <p class="eyebrow">Theo’s story &middot; testimony + teaching guide</p>
      <h1 class="mn-plate"><span>Sexual</span> <span>assault</span> <span class="mk">of men</span></h1>
    </div>
    <div class="mn-hero__vid" id="film">{yt('J50PuImLUV4', 'Male Survivors of Sexual Assault: Theo’s Story', label='Testimony')}</div>
    <div class="mn-hero__act"><div class="btns">{btn('Watch Theo’s story', 'https://www.youtube.com/watch?v=J50PuImLUV4', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div></div>
    <div class="mn-hero__txt"><p class="lede">Survivor and SafeBAE Board Member Theo Hutt shares his story, challenging the stigma and myths that keep male survivors silent. The guide helps educators unpack masculinity norms, explore barriers to healing, and build classroom dialogue that validates survivors of all genders.</p></div>
  </div>
</section>

<section class="mn-band mn-band--mint">
  <div class="wrap mn-six">
    <div><p class="mn-six__n">1 in 6</p><div class="mn-six__fig" aria-hidden="true">{FIG * 6}</div></div>
    <div class="mn-six__txt"><p class="mn-six__lead">At least one in six men will experience sexual abuse or assault.</p><p>Ending sexual violence requires the active engagement of all genders.</p></div>
  </div>
</section>

<section class="mn-band" id="discuss">
  <div class="wrap">
    <div class="mn-head"><p class="eyebrow">After the film</p><h2>Discuss</h2></div>
    <div class="mn-disc">
      <ul class="mn-qs">{qs}</ul>
      <figure class="mn-poster" data-gallery><button type="button" data-src="{imgsrc('poster-male-survivors')}" data-cap="{esc(poster_cap)}">{img('poster-male-survivors', 'SafeBAE poster: ' + poster_cap)}</button><figcaption><span>From SafeBAE’s free poster set</span>{a('Posters (.zip)', POSTERS_ZIP)}</figcaption></figure>
    </div>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <div class="mn-head"><h2>Myth or fact?</h2>
    <p class="lede">People of all genders can be vulnerable to sexual violence. People of all genders can perpetrate it. And not all men commit assault.</p></div>
    <div class="mn-myth">{myths}</div>
  </div>
</section>

<section class="mn-band" id="rules">
  <div class="wrap">
    <div class="mn-head"><p class="eyebrow">Toxic masculinity</p><h2>The rules boys are taught</h2>
    <p class="lede">Toxic masculinity is the set of rigid expectations about how men are “supposed” to behave. These norms discourage vulnerability and empathy and promote control, dominance and aggression. Some of them, like entitlement to sex, directly contribute to sexual violence.</p></div>
    <div class="mn-rules" id="mn-rules">
      <div class="mn-rules__col"><h3>Young men are often taught not to</h3><ul><li><span><em>Be vulnerable or ask for help</em></span></li><li><span><em>Show emotions or “weakness”</em></span></li><li><span><em>Be too kind or gentle</em></span></li><li><span><em>Lose, give up control, or take “no” for an answer</em></span></li><li><span><em>Speak out against friends or teammates</em></span></li></ul></div>
      <div class="mn-rules__col"><h3>Instead, they’re pressured to</h3><ul><li><span><em>Always be dominating</em></span></li><li><span><em>Always appear powerful</em></span></li><li><span><em>Always act aggressively</em></span></li></ul>
        <div class="mn-chal"><button class="mn-chal__go" type="button" id="challenge"><span>Challenge these rules</span><i aria-hidden="true"></i></button>
        <div class="mn-chal__after" id="challenged" aria-live="polite" hidden><p>These expectations are harmful for everyone. Challenging them means making space for all genders to express vulnerability, ask for help, and build healthy, respectful relationships.</p><button class="btn btn--ghost btn--sm" type="button" id="unchallenge">Show the rules again</button></div></div>
      </div>
    </div>
    <p class="mn-ask"><b>Ask students</b><span>How do these messages show up in your school, media or sports culture?</span></p>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <div class="mn-head"><p class="eyebrow">What is sexual violence?</p><h2>Know the terms</h2>
    <p class="lede">At its core, sexual violence is the use of power and control to harm, exploit and oppress.</p></div>
    <dl class="mn-defs"><div><dt>Sexual harassment</dt><dd>Unwelcome sexual advances, requests for sexual favors, or verbal or physical harassment of a sexual nature, often in schools or workplaces.</dd></div><div><dt>Sexual assault</dt><dd>Any sexual contact or behavior that happens without the clear, voluntary consent of everyone involved.</dd></div><div><dt>Rape</dt><dd>Legally defined with variations across states, often as sexual penetration without consent.</dd></div><div><dt>Sexual abuse</dt><dd>Sexual contact a person experiences or is made to perform through force, threats, fear or deception, or when legal consent can’t be given. Often used for adult-to-child victimization.</dd></div></dl>
  </div>
</section>

<section class="mn-band">
  <div class="wrap">
    <div class="mn-head"><p class="eyebrow">If a friend tells you they’ve been assaulted</p><h2>Your role: listen, believe, offer care.</h2>
    <p class="lede">The first person a survivor talks to can shape their healing. Your role isn’t to investigate or judge.</p></div>
    <div class="mn-respond">{rh}</div>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <div class="mn-head"><p class="eyebrow">Different identities &amp; sexual violence</p><h2>Not every man’s experience is the same</h2>
    <p class="lede">Men of color, transgender men and queer men experience higher rates of victimization and often face added stigma when seeking support.</p></div>
    <div class="mn-stats"><div><b>4&times;</b><p>Transgender people experience sexual victimization more than four times as often as cisgender people (86.2 vs. 21.7 per 1,000 in 2017–2018).</p></div><div><b>12%</b><p>of Black men reported being survivors of sexual violence in a 2010 study, compared to 7.5% of white men.</p></div><div><b>~4&times;</b><p>LGBT people are nearly four times more likely to experience violent victimization than non-LGBT people.</p></div><div><b>Higher</b><p>Individuals with disabilities are at significantly higher risk of sexual victimization than people without disabilities.</p></div></div>
    <p class="mn-ask"><b>Ask students</b><span>How might identity affect whether someone feels safe to come forward?</span><small>We encourage extending these conversations beyond health class, into advisory, literature, history and other spaces.</small></p>
  </div>
</section>

{begin('mn-band', 'These conversations can surface strong emotions and may lead to disclosures of abuse.')}
{tail('male-survivors', ['dating', 'rape-culture', 'rrcr'], 'mn-band mn-band--alt')}
'''
    js = r'''<script>
(function(){
  var go = document.getElementById('challenge'), after = document.getElementById('challenged'), undo = document.getElementById('unchallenge'), r = document.getElementById('mn-rules');
  if(!go || !after || !r) return;
  function set(on, focus){ r.classList.toggle('challenged', on); go.hidden = on; after.hidden = !on; if(focus) (on ? undo : go).focus({preventScroll:true}); }
  go.addEventListener('click', function(){ set(true, true); });
  undo.addEventListener('click', function(){ set(false, true); });
})();
</script>'''
    film_page('film-sexual-assault-of-men.html', 'Supporting Male Survivors', 'Theo Hutt’s story and SafeBAE’s teaching guide on the sexual assault of men, masculinity norms, and supporting survivors of all genders.', body, 'men', 'family=Saira+Stencil+One', CSS, js)
