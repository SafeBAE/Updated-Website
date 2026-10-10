from films_common import *
import math

# Rape Culture & How to Shift to a Culture of Respect.
# A calm, light page built from the teaching guide: its slab headline face, Logo Teal, and one idea carried
# through the page: the thing you cross out (coral line) and the thing you build instead (mint).

CSS = '''
.film--rc{--slab:'Zilla Slab',Georgia,serif; --f-card:#fff; --f-line:var(--line); --f-ink:var(--slate); --f-ink2:var(--ink-soft); --f-acc:var(--teal); --f-acc-ink:#fff; --f-lab:var(--logo-teal); --f-disp:var(--slab); --f-dw:700; --f-ds:100%}
.film--rc main{background:#fff; color:var(--slate)}
.film--rc main :focus-visible{outline-color:var(--teal)}
.film--rc :is(.rc-hero,.rc-band--slate,.gpanel,.fvb) :focus-visible{outline-color:var(--mint)}
.film--rc h1,.film--rc h2,.film--rc h3,.film--rc h4{font-family:var(--slab); font-weight:700; font-stretch:100%; letter-spacing:-.01em}

/* hero: the title runs the full width, the film and its summary sit level under it */
.rc-hero{background:var(--logo-teal) var(--grain); color:#fff; --wm-o:.17}
.rc-hero .wm-daisy{right:-11%; bottom:-46%}
.rc-hero > .wrap{padding-block:clamp(36px,4.2vw,58px) clamp(48px,6vw,84px)}
.rc-hero .crumbs{color:rgba(255,255,255,.8)}
.rc-title{margin:0; font-size:clamp(3.1rem,9.2vw,8.2rem); line-height:.9; letter-spacing:-.02em}
.rc-x{position:relative; display:inline-block; white-space:nowrap; color:var(--aqua)}
.rc-x::after{content:""; position:absolute; left:-.05em; right:-.05em; top:64%; height:.1em; border-radius:99px; background:var(--coral); transform:rotate(-1.1deg); transform-origin:0 50%; animation:rc-strike .8s .6s var(--ease) both}
@keyframes rc-strike{from{transform:rotate(-1.1deg) scaleX(0)}}
.rc-to{display:block; font-size:.4em; line-height:1.08; letter-spacing:-.01em; margin-top:.4em; color:#fff}
.rc-title .mk{padding:0}
.rc-hero__row{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(28px,4vw,56px); align-items:stretch; margin-top:clamp(26px,3.2vw,42px)}
.rc-hero__txt{display:flex; flex-direction:column; min-width:0}
.rc-hero__txt .lede{color:rgba(255,255,255,.95); margin:0 0 1.3em}
.rc-hero__txt .lede a{color:#fff; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:.18em; transition:color .2s}
.rc-hero__txt .lede a:hover{color:var(--mint)}
.rc-hero__txt .btns{margin-top:auto; gap:10px}
.rc-hero__txt .btn{padding-inline:1em}
.rc-hero__vid{min-width:0; align-self:end}
.rc-hero__vid .vid{border-radius:var(--r-xl)}

/* bands and heads */
.rc-band{padding-block:var(--band); position:relative}
.rc-band--aqua{background:var(--aqua)}
.rc-band--slate{background:var(--slate) var(--grain); color:#fff}
.rc-band h2{font-size:clamp(2.1rem,4.4vw,3.6rem); line-height:1; margin:0}
.rc-band .eyebrow{color:var(--logo-teal)} .rc-band--slate .eyebrow{color:var(--mint)}
.rc-head{margin-bottom:var(--head-gap)}
.rc-head .lede{margin:.6em 0 0}
.rc-band--slate .rc-head .lede{color:rgba(255,255,255,.92)}
.rc-head--act{display:flex; align-items:end; justify-content:space-between; gap:20px 40px; flex-wrap:wrap}
.rc-head--act > div{flex:1 1 520px; min-width:0}

/* the definition */
.rc-def h2.eyebrow{font-family:var(--mono); font-weight:600; font-size:var(--fs-label); line-height:1.4; letter-spacing:.12em; margin:0 0 1.1rem}
.rc-define{font-family:var(--slab); font-weight:700; font-size:clamp(1.65rem,3.3vw,2.9rem); line-height:1.16; letter-spacing:-.01em; margin:0; text-wrap:balance}
.rc-define mark{background:none; color:inherit; text-decoration:underline; text-decoration-color:var(--teal); text-decoration-thickness:.1em; text-underline-offset:.15em; text-decoration-skip-ink:none}
.rc-def .lede{margin:.9em 0 0}
.rc-sub{display:flex; flex-wrap:wrap; align-items:baseline; gap:6px 28px; margin:clamp(36px,4.4vw,56px) 0 var(--head-gap); padding-top:clamp(24px,2.8vw,34px); border-top:2px solid rgba(29,90,102,.22)}
.rc-sub h3{margin:0; font-size:clamp(1.6rem,2.6vw,2.2rem); line-height:1.05; color:var(--logo-teal)}
.rc-sub p{margin:0; flex:1 1 420px; font-size:1.04rem; line-height:1.5}

/* six elements: the guide's diagram, one element open at a time */
.rc-elem{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:clamp(24px,4vw,56px); align-items:center}
.rc-orbit-wrap{min-width:0}
.rc-orbit{position:relative; width:100%; max-width:520px; aspect-ratio:1; margin-inline:auto}
.rc-orbit svg{position:absolute; inset:0; width:100%; height:100%}
.rc-orbit line{transition:stroke-width .3s, stroke-dasharray .3s}
.rc-orbit line.on{stroke:#1d5a66; stroke-width:1.1; stroke-dasharray:none}
.rc-orbit__c{position:absolute; inset:33%; border-radius:50%; background:var(--slate) var(--grain); color:#fff; display:grid; place-items:center; text-align:center; font-family:var(--slab); font-weight:700; font-size:clamp(1rem,1.7vw,1.35rem); line-height:1.1; padding:10px; box-shadow:0 0 0 8px rgba(29,65,78,.08)}
.rc-orbit button{position:absolute; width:27%; aspect-ratio:1; margin:-13.5% 0 0 -13.5%; border-radius:50%; border:3px solid var(--teal); background:#fff; color:var(--slate); font:inherit; font-family:var(--slab); font-weight:700; font-size:clamp(.9rem,1.25vw,1.08rem); line-height:1.1; cursor:pointer; padding:8px; transition:transform .25s var(--ease), background .25s, color .25s, box-shadow .25s}
.rc-orbit button:hover{transform:scale(1.06); box-shadow:0 10px 22px -14px rgba(29,65,78,.7)}
.rc-orbit button[aria-pressed="true"]{background:var(--logo-teal); border-color:var(--logo-teal); color:#fff; transform:scale(1.1); box-shadow:0 14px 30px -14px rgba(29,65,78,.7)}
.rc-orbit__credit{margin:14px 0 0; text-align:center; font-size:.9rem; color:var(--ink-soft)}
.rc-ep{display:flex; flex-direction:column; background:#fff; border:1px solid var(--line); box-shadow:var(--shadow-soft); border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.rc-ep .eyebrow{margin-bottom:.7rem}
.rc-ep h4{font-size:clamp(1.7rem,2.6vw,2.3rem); line-height:1.05; margin:0 0 .4em}
.rc-ep > p{margin:0 0 .85em; font-size:1.04rem; line-height:1.6}
.rc-ep ul{margin:0 0 1em; padding-left:1.15em; font-size:1rem; line-height:1.55}
.rc-ep li{margin:.3em 0}
.rc-ep li::marker{color:var(--teal)}
.rc-ep .rc-ep__q{margin:0 0 1em; padding:14px 18px; border-radius:14px; background:var(--mist); border:1px solid var(--line); font-weight:700; font-size:1.04rem; line-height:1.45}
.rc-ep__q b{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin-bottom:6px}
.rc-ep .rc-ch{margin:0 0 1em; padding:14px 18px; border-radius:14px; border:1px solid var(--line); font-size:.95rem; line-height:1.55; color:var(--ink-soft)}
.rc-ch .link{white-space:nowrap}
.rc-ch b{display:block; font-family:var(--slab); font-size:1.15rem; line-height:1.2; color:var(--slate); margin-bottom:2px}
.rc-ep__foot{display:flex; justify-content:flex-end; margin-top:auto; padding-top:16px; border-top:1px solid var(--line)}

/* myths and facts: wide cards that turn over */
.rc-mf{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.film--rc .flip{min-height:176px; border-radius:var(--r-xl); transition:transform .25s var(--ease)}
.film--rc .flip:hover{transform:translateY(-3px)}
.film--rc .flip__face{border-radius:var(--r-xl); padding:var(--pad-card); gap:12px}
.film--rc .flip__face--front{background:var(--slate) var(--grain)}
.film--rc .flip__face--back{background:var(--mint)}
.film--rc .flip__tag{font-size:.72rem}
.film--rc .flip__face--front .flip__tag{color:var(--aqua)}
.film--rc .flip__txt{font-family:var(--slab); font-weight:700; font-size:clamp(1.3rem,1.95vw,1.6rem); line-height:1.18; text-wrap:balance; margin-block:auto}
.film--rc .flip__face .hint{margin-top:0}
.film--rc .flip__face--back .flip__txt{font-family:var(--body); font-weight:600; font-size:1.04rem; line-height:1.5; text-wrap:pretty}
.film--rc .flip__face .hint{font-size:.875rem; font-weight:700; opacity:1; display:flex; align-items:center; gap:.5em}
.film--rc .flip__face .hint::after{content:"\\2192"; transition:transform .2s var(--ease)}
.film--rc .flip:hover .hint::after{transform:translateX(4px)}
@media (prefers-reduced-motion:no-preference){ .film--rc .flip[aria-pressed="true"] .flip__in{transform:rotateX(180deg)} .film--rc .flip__face--back{transform:rotateX(180deg)} }

/* interrupt it: a wall of everyday behavior, crossed out one brick at a time */
.rc-wall{display:flex; flex-wrap:wrap; gap:10px}
.rc-wall::after{content:""; flex:1000 1 0}
.rc-wall button{flex:1 1 auto; min-height:56px; font:inherit; font-family:var(--slab); font-weight:700; font-size:clamp(1.05rem,1.7vw,1.4rem); line-height:1.2; padding:12px 18px; border-radius:12px; border:2px solid rgba(255,255,255,.28); background:rgba(255,255,255,.04); color:#fff; cursor:pointer; text-decoration:line-through; text-decoration-color:transparent; text-decoration-thickness:4px; transition:color .3s, border-color .3s, background .3s, text-decoration-color .3s, transform .2s var(--ease)}
.rc-wall button:hover{border-color:var(--coral); transform:translateY(-2px)}
.rc-wall button[aria-pressed="true"]{color:rgba(255,255,255,.55); text-decoration-color:var(--coral); border-color:var(--coral); background:rgba(254,113,113,.08)}
.rc-wall__count{display:flex; align-items:center; gap:16px; margin:22px 0 0; font-family:var(--mono); font-size:.8rem; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--mint)}
.rc-wall__count span:first-child{flex:none}
.rc-meter{flex:1; height:8px; border-radius:99px; background:rgba(255,255,255,.14); overflow:hidden}
.rc-meter i{display:block; height:100%; width:0; border-radius:99px; background:var(--mint); transition:width .4s var(--ease)}

/* discussion prompts: four cards, labels and questions aligned across each row */
.rc-disc{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:var(--gap)}
.rc-q{margin:0; background:var(--mist); border:1px solid var(--line); border-radius:var(--r-xl); padding:var(--pad-card); min-width:0}
.rc-q b{display:block; font-family:var(--slab); font-size:1.4rem; line-height:1.15; color:var(--logo-teal); margin-bottom:.4em}
.rc-q p{margin:0; font-size:1.06rem; line-height:1.55; font-weight:500}

/* one small action: a checklist that remembers */
.rc-pledge{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px var(--gap)}
.rc-pl{display:grid; grid-template-columns:32px minmax(0,1fr); gap:14px; align-items:start; padding:18px 20px; border-radius:14px; border:2px solid transparent; background:#fff; cursor:pointer; transition:border-color .2s, background .2s, transform .2s var(--ease), box-shadow .2s}
.rc-pl:hover{transform:translateY(-2px); box-shadow:var(--shadow-soft)}
.rc-pl input{appearance:none; -webkit-appearance:none; width:32px; height:32px; border-radius:9px; border:2px solid var(--teal); margin:0; cursor:pointer; background:#fff; transition:background .2s, border-color .2s}
.rc-pl input:checked{background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' stroke='%231d414e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/20px no-repeat; border-color:var(--slate)}
.rc-pl b{display:block; font-family:var(--slab); font-size:1.22rem; line-height:1.2; margin-bottom:3px}
.rc-pl span span{display:block; font-size:.98rem; line-height:1.5; color:var(--ink-soft)}
.rc-pl:has(input:checked){border-color:var(--teal); background:#f2fffc}
.rc-pl:has(input:focus-visible){outline:3px solid var(--teal); outline-offset:3px}
.rc-pl input:focus-visible{outline:0}

@media (max-width:1100px){
  .rc-hero__row{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rc-hero__vid{align-self:center}
  .rc-hero__txt .btn{padding-inline:.8em; font-size:.94rem}
  .rc-hero__vid .vid__label{font-size:.95rem} .rc-hero__vid .vid__label small{display:none}
}
@media (max-width:1000px){
  .rc-elem{grid-template-columns:minmax(0,1fr)}
  .rc-orbit{max-width:480px}
}
@media (max-width:900px){
  .rc-hero__row{grid-template-columns:minmax(0,1fr)}
  .rc-hero__vid{order:-1}
  .rc-hero__txt .btns{margin-top:0}
}
@media (max-width:760px){
  .rc-mf, .rc-disc, .rc-pledge{grid-template-columns:minmax(0,1fr)}
  .rc-title{font-size:clamp(3.1rem,14.4vw,5.6rem)}
  .rc-to{font-size:.46em}
}
@media (max-width:560px){
  .rc-hero__vid .vid__label{font-size:.92rem; padding:9px 12px 10px} .rc-hero__vid .vid__label small{display:none}
}
@media (max-width:480px){
  .rc-orbit button{width:30%; margin:-15% 0 0 -15%; font-size:.875rem; padding:5px; border-width:2px}
  .rc-orbit__c{inset:34.5%; font-size:.95rem; padding:6px}
  .rc-wall button{font-size:1.05rem; padding:10px 14px}
}
'''

ELEMS = [
 ('Rape myths', 'Rape culture is reinforced by myths and stereotypes. These false beliefs excuse harmful actions, shift responsibility away from perpetrators, and silence survivors.', ['They shift blame from the perpetrator to the survivor.', 'They silence survivors, making them less likely to report or seek help.', 'They normalize violence, allowing harmful behavior to go unchallenged.'], 'How do these myths show up in your community, school or on social media? Who benefits when they’re believed?'),
 ('Media + algorithms', 'We absorb messages about relationships and sexuality from media, sometimes without noticing. Films, music, ads and games can send harmful signals about power and consent.', ['Movies that treat catcalling or harassment as a joke.', 'Music lyrics that normalize abuse or misogyny.', 'Pornography that depicts violence or non-consensual sex.', 'Male characters shown as always wanting sex and never taking “no” for an answer; female characters rarely shown asking for consent.', 'TV with no positive representation of LGBTQ+ or gender-diverse relationships.'], 'Have you noticed these patterns in what you watch, listen to or play? What impact do they have on real-life behavior?'),
 ('Peer influence', 'Peer pressure and group dynamics can make harmful behavior seem normal, or even expected.', ['Complacency: when friends laugh off harassment, it becomes easier to ignore or excuse.', '“Proving” manhood: fitting in can feel like it requires degrading others or mocking survivors.', 'Herd mentality: without someone willing to step up as an active bystander, harmful behavior spreads.'], 'When have you seen peer pressure, positive or negative, shape how people act? What changes when someone speaks up?'),
 ('Gender + sexuality beliefs', 'Cultural expectations about gender and sexuality suggest who is “available” or “deserving” of respect, and who is not.', ['Oversexualization: girls and women of color, LGBTQIA+ youth and people with disabilities are often portrayed as hypersexual or always available.', 'Unequal standards: stricter rules for girls, or leaving LGBTQ+ experiences out of sex education, send the message that some people’s safety matters less.'], 'Charlie talks about standards and pressures for men. How do these expectations affect everyone? How could you challenge this kind of talk?'),
 ('Victim blaming', 'Survivors are never at fault. Clothing, sobriety or past experiences don’t excuse assault. Responsibility always lies with the perpetrator.', ['When people believe rape myths, it makes it harder for survivors to come forward and easier for violence to continue.', 'Being under the influence never makes someone responsible for violence done to them.'], ''),
 ('Racial stereotypes', 'Racism, sexism, homophobia and ableism combine to put certain groups, especially Indigenous and Black girls and transgender youth, at the highest risk of sexual violence. Any solution has to address these inequities.', ['Take an intersectional approach: rape culture affects everyone, but not equally.', 'SafeBAE’s learning series Race, Rape Culture, and Resistance goes deeper.'], ''),
]
MYTHS = [('“Real rape” only happens with strangers.', 'Most rapes are committed by someone the survivor knows.'), ('People often make false rape reports.', 'False reports are rare (2–10%), about the same rate as other crimes. Many assaults are never reported at all.'),
         ('Only women can be raped.', 'People of all genders experience sexual assault. About 1 in 10 rape survivors are male, and nearly 1 in 2 transgender people will experience sexual assault.'), ('Clothing or behavior “invites” assault.', 'No one ever asks to be assaulted. The responsibility always lies with the perpetrator.'),
         ('If someone didn’t fight back, it wasn’t really rape.', 'Freezing or shutting down is a common survival response. Lack of resistance does not mean consent.'), ('If a person is drunk or high, they are to blame if assaulted.', 'Being under the influence never makes someone responsible for violence done to them. Consent can’t be given when someone is incapacitated.')]
STARTS = ['Rape jokes', 'Victim blaming', 'Catcalling', '“Locker room talk”', 'Not believing survivors', 'Teaching how not to get raped instead of how not to rape', 'Believing rape only happens to women', 'Rating people’s bodies', 'Stalking', 'Groping', 'Sending or sharing unsolicited nudes', 'Revenge porn', 'Using drugs or alcohol to get sex']
PLEDGE = [('Broaden your perspective', 'Rape culture isn’t just one man assaulting one woman. It includes child marriage, rape as a weapon of war, and “corrective rape” targeting LGBTQIA+ people.'), ('Practice enthusiastic consent', 'Consent should be clear, verbal and enthusiastic. Anything less is not consent.'),
          ('Challenge harmful beliefs', 'Don’t accept ideas that masculinity must be violent or dominant, or that femininity must be weak or passive.'), ('Redefine gender expectations', 'Reject the myth that men have to be sexually aggressive or that women should “play hard to get.”'),
          ('Stop victim blaming', 'Survivors are never at fault. Responsibility always lies with the perpetrator.'), ('Respect privacy', 'Never share intimate photos or messages without permission, and make it clear you won’t tolerate it from peers.'),
          ('Take an intersectional approach', 'Some groups face especially high risks. Solutions have to address those inequities.'), ('Believe survivors', 'When someone shares their experience, listen with compassion and affirm their truth.'),
          ('Challenge harmful humor', 'Don’t laugh at rape jokes or “locker room talk.” Let others know it’s not okay.'), ('Be an active bystander', 'If you see harassment or assault, step in safely or get help.')]
# After-the-film prompts: the guide gives each one a short label
DISCUSS = [('First reactions', 'What stood out to you in this video? How did it make you feel?'),
           ('Language in your community', 'Have you heard jokes, comments or phrases like the ones Charlie mentioned? How did people respond?'),
           ('Recognizing non-consent', 'What other signs, verbal or nonverbal, might show someone is uncomfortable or not giving consent?'),
           ('Gender expectations', 'Charlie talks about standards and pressures for men. How do these expectations affect not only men, but everyone? How might you challenge this kind of talk?')]

CH = '<p class="rc-ch"><b>Choking Hazard</b>SafeBAE’s campaign on sexual strangulation, which young people call “choking”. There’s no safe way to choke someone. The campaign has the evidence, myth vs. fact, and free warning posters. ' + a('See the campaign', 'choking-hazard.html', 'link') + '</p>'

def build():
    n = len(ELEMS)
    pos = []
    for i in range(n):
        ang = math.radians(-90 + i * 360 / n)
        pos.append((50 + 36 * math.cos(ang), 50 + 36 * math.sin(ang)))
    lines = '<circle cx="50" cy="50" r="36" fill="none" stroke="#13848f" stroke-width=".35" stroke-dasharray=".6 1.6" opacity=".7"/>' + ''.join(f'<line{" class=on" if i == 0 else ""} data-l="{i}" x1="50" y1="50" x2="{x:.1f}" y2="{y:.1f}" stroke="#13848f" stroke-width=".5" stroke-dasharray="1.5 1.5"/>' for i, (x, y) in enumerate(pos))
    nodes = ''.join(f'<button type="button" style="left:{x:.1f}%;top:{y:.1f}%" aria-pressed="{str(i==0).lower()}" aria-controls="rc-ep-{i}" data-e="{i}">{esc(t)}</button>' for i, ((t, *_r), (x, y)) in enumerate(zip(ELEMS, pos)))
    panels = []
    for i, (t, d, pts, q) in enumerate(ELEMS):
        nxt = ELEMS[(i + 1) % n][0]
        panels.append(
            f'<div class="rc-ep" id="rc-ep-{i}" data-ep="{i}"{"" if i == 0 else " hidden"}><p class="eyebrow">Element {i+1} of {n}</p><h4>{esc(t)}</h4><p>{esc(d)}</p>'
            f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in pts)}</ul>'
            + ('<p>' + a('Explore Race, Rape Culture, and Resistance', 'film-race-rape-culture-resistance.html', 'link') + '</p>' if i == 5 else '')
            + (f'<p class="rc-ep__q"><b>Ask your students</b>{esc(q)}</p>' if q else '')
            + (CH if i == 1 else '')
            + f'<div class="rc-ep__foot"><button class="btn btn--slate btn--sm" type="button" data-next-e="{(i + 1) % n}">Next: {esc(nxt)}<span class="arr" aria-hidden="true">&rarr;</span></button></div></div>')
    myths = ''.join(f'<button class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span><span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{esc(f)}</span><span class="hint">Tap to turn it back</span></span></span></button>' for m, f in MYTHS)
    wall = ''.join(f'<button type="button" aria-pressed="false">{esc(w)}</button>' for w in STARTS)
    pledge = ''.join(f'<label class="rc-pl"><input type="checkbox" id="pl-{i}" data-pl="{i}"><span><b>{esc(t)}</b><span>{esc(d)}</span></span></label>' for i, (t, d) in enumerate(PLEDGE))
    disc = ''.join(f'<li class="rc-q"><b>{esc(t)}</b><p>{esc(q)}</p></li>' for t, q in DISCUSS)
    body = f'''
<section class="rc-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      {film_crumbs('Rape Culture')}
      <p class="eyebrow">With Charlie Coleman &amp; Teen Vogue &middot; film + teaching guide</p>
      <h1 class="rc-title"><span class="rc-x">Rape culture</span> <span class="rc-to">&amp; how to shift to a <span class="mk">culture of respect</span></span></h1>
    </div>
    <div class="rc-hero__row">
      <div class="rc-hero__txt">
        <p class="lede">SafeBAE co-founder Charlie Coleman talks about rape culture and <a href="fordaisy.html">his sister Daisy’s</a> sexual assault, and invites men to examine their role in identifying and interrupting toxic masculinity. The guide gives students concrete steps for challenging harmful norms and building a culture rooted in equity, consent and accountability.</p>
        <div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=FsmycfJPWs4', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
      </div>
      <div class="rc-hero__vid" id="film">{yt('FsmycfJPWs4', 'Charlie Coleman on Rape Culture & His Sister Daisy’s Assault', label='SafeBAE x Teen Vogue')}</div>
    </div>
  </div>
</section>

<section class="rc-band rc-band--aqua" id="elements">
  <div class="wrap">
    <div class="rc-def">
      <h2 class="eyebrow">What is rape culture?</h2>
      <p class="rc-define">Rape culture is the values, attitudes, beliefs and everyday behaviors that <mark>make sexual violence seem normal, excusable, or less serious than it is.</mark></p>
      <p class="lede">When we excuse or ignore harmful behavior, sexual violence becomes more likely to happen and less likely to be challenged.</p>
    </div>
    <div class="rc-sub"><h3>Six elements of rape culture</h3><p>Where is this behavior learned? Choose an element to see how it shows up and the question to ask your students.</p></div>
    <div class="rc-elem">
      <div class="rc-orbit-wrap"><div class="rc-orbit" role="group" aria-label="Elements of rape culture"><svg viewBox="0 0 100 100" aria-hidden="true">{lines}</svg><div class="rc-orbit__c">Elements of rape culture</div>{nodes}</div><p class="rc-orbit__credit">Diagram credit: RUSSW-VAWC</p></div>
      <div>{''.join(panels)}</div>
    </div>
  </div>
</section>

<section class="rc-band">
  <div class="wrap">
    <div class="rc-head rc-head--act"><div><p class="eyebrow">Rape myths &amp; victim blaming</p><h2>Myths vs. facts</h2></div>{btn('More myths & facts', 'myths-facts.html', 'slate', arrow=True)}</div>
    <div class="rc-mf">{myths}</div>
  </div>
</section>

<section class="rc-band rc-band--slate">
  <div class="wrap">
    <div class="rc-head"><h2>Interrupt it.</h2>
    <p class="lede">Rape culture starts with everyday behavior that goes unchallenged. Tap each one you’re ready to call out.</p></div>
    <div class="rc-wall" role="group" aria-label="Everyday behavior to call out">{wall}</div>
    <p class="rc-wall__count"><span id="wallc" aria-live="polite">0 of {len(STARTS)} called out</span><span class="rc-meter" aria-hidden="true"><i id="wallm"></i></span></p>
  </div>
</section>

<section class="rc-band">
  <div class="wrap">
    <div class="rc-head"><p class="eyebrow">After the film</p><h2>Discuss</h2><p class="lede">Charlie points out that “no” isn’t the only way to show someone doesn’t consent.</p></div>
    <ul class="rc-disc">{disc}</ul>
  </div>
</section>

<section class="rc-band rc-band--aqua">
  <div class="wrap">
    <div class="rc-head"><h2>What is one small action you could take this week?</h2>
    <p class="lede">Changing culture starts with everyday choices. Check the ones you’ll commit to. Your choices stay on this device.</p></div>
    <div class="rc-pledge">{pledge}</div>
  </div>
</section>

{vibe_band('Charlie asks men to look at their own role. Vibe Check is a free, anonymous reflection tool for young people questioning whether they crossed a boundary or caused harm, with guided modules on rape culture and on men and masculinity.', 'Looking at your own behavior?')}
{teach_tail('rape-culture', 'rc-band', ['knowb4unude', 'male-survivors', 'rrcr'], 'rc-band rc-band--aqua', btn_kind='teal')}
'''
    js = r'''<script>
(function(){
  var d = document;
  /* six elements: one open at a time; the footer button walks to the next */
  var bs = [].slice.call(d.querySelectorAll('.rc-orbit button')), ps = d.querySelectorAll('[data-ep]'), ls = d.querySelectorAll('.rc-orbit line');
  function pick(b){ bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); }); ps.forEach(function(p){ p.hidden = p.dataset.ep !== b.dataset.e; }); ls.forEach(function(l){ l.classList.toggle('on', l.dataset.l === b.dataset.e); }); }
  bs.forEach(function(b){ b.addEventListener('click', function(){ pick(b); }); });
  d.querySelectorAll('[data-next-e]').forEach(function(n){ n.addEventListener('click', function(){ var b = bs[+n.dataset.nextE]; if(!b) return; pick(b); var p = d.querySelector('[data-ep="' + b.dataset.e + '"]'), nb = p && p.querySelector('[data-next-e]'); if(nb) nb.focus({preventScroll:true}); if(p){ var r = p.getBoundingClientRect(); if(r.top < 110) window.scrollTo({top: window.pageYOffset + r.top - 130, behavior:'smooth'}); } }); });
  /* interrupt it */
  var w = d.querySelectorAll('.rc-wall button'), wc = d.getElementById('wallc'), wm = d.getElementById('wallm');
  w.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); var n = d.querySelectorAll('.rc-wall [aria-pressed="true"]').length; wc.textContent = n + ' of ' + w.length + ' called out' + (n === w.length ? '. That’s a culture of respect.' : ''); if(wm) wm.style.width = (n / w.length * 100) + '%'; }); });
  /* one small action: remembered on this device */
  d.querySelectorAll('[data-pl]').forEach(function(c){ var k = 'sb-pledge-' + c.dataset.pl; try{ c.checked = localStorage.getItem(k) === '1'; }catch(e){} c.addEventListener('change', function(){ try{ localStorage.setItem(k, c.checked ? '1' : '0'); }catch(e){} }); });
})();
</script>'''
    film_page('film-rape-culture.html', 'Rape Culture & a Culture of Respect', 'SafeBAE’s film with Charlie Coleman and Teen Vogue and a teaching guide on recognizing rape culture and building a culture of respect.', body, 'rc', 'family=Zilla+Slab:wght@600;700', CSS, js)
