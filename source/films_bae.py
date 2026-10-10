from films_common import *

CSS = '''
.film--bae{--ind:#102c35; --ind2:#1d414e; --pink:#fe7171; --px:'Silkscreen',monospace}
.film--bae main{background:var(--ind); color:#fff; position:relative}
.film--bae main::after{content:""; position:fixed; inset:0; pointer-events:none; z-index:1; background:repeating-linear-gradient(0deg, rgba(255,255,255,.025) 0 1px, transparent 1px 3px); mix-blend-mode:screen}
.film--bae main > *{position:relative; z-index:2}
.px{font-family:var(--px); text-transform:uppercase; letter-spacing:.02em}
.bae-hero .wrap:not(.hudwrap){display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px)}
.bae-title{font-family:var(--px); font-size:clamp(4rem,10vw,9rem); line-height:.88; color:var(--pink); text-shadow:6px 6px 0 #15ffc8, 12px 12px 0 rgba(21,255,200,.25); margin:0 0 .25em; letter-spacing:-.02em}
.bae-sub{font-family:var(--px); font-size:clamp(1rem,1.6vw,1.3rem); color:#15ffc8; margin-bottom:18px}
.bae-hero .lede{color:rgba(255,255,255,.88)}
.bae-hero .crumbs{color:rgba(255,255,255,.6)}
.press{font-family:var(--px); animation:blink 1.1s steps(2) infinite}
@keyframes blink{50%{opacity:.35}}
.arcade{padding:18px; border-radius:22px; background:linear-gradient(145deg,#1d5a66,#0b2128); box-shadow:0 0 0 3px #15ffc8, 0 30px 70px -20px rgba(0,0,0,.7)}
.arcade .vid{border-radius:10px}
.arcade__lbl{display:flex; justify-content:space-between; font-family:var(--px); font-size:.8rem; color:#15ffc8; margin-top:12px}
.hud{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); border:3px solid #15ffc8; border-radius:4px; background:#0b2128}
.hud div{padding:18px 20px; border-left:3px solid #15ffc8}
.hud div:first-child{border-left:0}
.hud b{display:block; font-family:var(--px); font-size:clamp(2rem,4vw,3.4rem); color:var(--pink); line-height:1}
.hud span{display:block; font-size:.92rem; margin-top:6px; color:rgba(255,255,255,.88)}
.hud small{display:block; font-family:var(--mono); font-size:.68rem; color:#15ffc8; margin-top:6px; letter-spacing:.06em; text-transform:uppercase}
@media (max-width:760px){.bae-title{margin-bottom:.45em} .hud{grid-template-columns:1fr} .hud div{border-left:0; border-top:3px solid #15ffc8} .hud div:first-child{border-top:0} .bae-hero .wrap:not(.hudwrap){grid-template-columns:minmax(0,1fr)}}
.bae-band{padding-block:var(--band)}
.bae-band--alt{background:var(--ind2)}
.bae-band h2{font-family:var(--px); font-weight:400; font-size:clamp(1.8rem,4vw,3.2rem); text-transform:uppercase; line-height:1.05; letter-spacing:0}
.bae-band .eyebrow{color:#15ffc8}
.term{background:#071a20; border:2px solid #15ffc8; border-radius:10px; padding:20px clamp(16px,3vw,28px); font-family:var(--mono); box-shadow:0 0 40px rgba(21,255,200,.12)}
.term__bar{display:flex; gap:6px; margin-bottom:14px}
.term__bar i{width:12px; height:12px; border-radius:50%; background:var(--pink)} .term__bar i:nth-child(2){background:#fff} .term__bar i:nth-child(3){background:#15ffc8}
.term p{margin:0 0 12px; font-size:clamp(.95rem,1.4vw,1.15rem); line-height:1.5; color:#d9fff6}
.term p::before{content:"> "; color:#15ffc8}
.term p.cmt{color:rgba(255,255,255,.55)} .term p.cmt::before{content:"// "}
.lvls{display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:8px; margin:26px 0 16px}
.lvl{font:inherit; cursor:pointer; text-align:left; background:#0b2128; color:#fff; border:3px solid rgba(21,255,200,.35); border-radius:6px; padding:12px 10px; display:flex; flex-direction:column; gap:6px; min-height:120px}
.lvl small{font-family:var(--px); font-size:.7rem; color:#15ffc8}
.lvl span{font-weight:800; font-size:.9rem; line-height:1.2}
.lvl[aria-selected="true"]{border-color:var(--pink); background:#1d5a66; box-shadow:0 0 0 3px rgba(254,113,113,.3)}
.lvl[aria-selected="true"] small{color:var(--pink)}
.lvlpanel{background:#0b2128; border:3px solid var(--pink); border-radius:6px; padding:clamp(18px,3vw,32px); display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(18px,3vw,40px)}
.lvlpanel h3{font-family:var(--px); font-weight:400; text-transform:uppercase; color:var(--pink); font-size:1.6rem}
.lvlpanel h4{font-family:var(--px); font-weight:400; text-transform:uppercase; color:#15ffc8; font-size:.95rem; margin:16px 0 8px}
.lvlpanel ul{margin:0; padding-left:1.1em} .lvlpanel li{color:rgba(255,255,255,.9)}
.lvlpanel .clip{display:flex; gap:10px; align-items:baseline; font-size:.88rem; color:#d9fff6; margin:0 0 12px; padding-left:10px; border-left:3px solid #15ffc8} .lvlpanel .clip b{font-family:var(--px); font-weight:400; font-size:.72rem; color:#15ffc8; text-transform:uppercase}
@media (max-width:1000px){.lvls{grid-template-columns:repeat(4,minmax(0,1fr))}} @media (max-width:760px){.lvls{grid-template-columns:repeat(2,minmax(0,1fr))} .lvls > :last-child:nth-child(odd){grid-column:1/-1} .lvlpanel{grid-template-columns:1fr}}
.ds{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.d{background:#0b2128; border:3px solid #15ffc8; border-radius:6px; padding:18px; display:flex; flex-direction:column; gap:10px}
.d b{font-family:var(--px); font-size:2.6rem; line-height:1; color:#15ffc8}
.d h3{font-family:var(--px); font-weight:400; text-transform:uppercase; font-size:1.3rem; margin:0}
.d p{margin:0; font-size:.93rem; color:rgba(255,255,255,.85)}
.bub{background:#fff; color:var(--ind); border-radius:14px 14px 14px 4px; padding:10px 12px; font-weight:700; font-size:.9rem}
.bub:nth-of-type(2){background:#15ffc8}
@media (max-width:960px){.ds{grid-template-columns:1fr 1fr}} @media (max-width:560px){.ds{grid-template-columns:1fr}}
.barriers{display:flex; flex-wrap:wrap; gap:10px}
.barriers span{font-family:var(--mono); font-size:.92rem; padding:10px 14px; border:2px dashed rgba(254,113,113,.6); border-radius:6px; color:#ffd5d5}
.harm{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.harm div{background:#0b2128; border-radius:6px; padding:16px; border-top:4px solid var(--pink)}
.harm h3{font-family:var(--px); font-weight:400; font-size:1.05rem; text-transform:uppercase; color:var(--pink)}
.harm ul{margin:0; padding-left:1.1em; font-size:.92rem; color:rgba(255,255,255,.88)}
@media (max-width:960px){.harm{grid-template-columns:1fr 1fr}} @media (max-width:560px){.harm{grid-template-columns:1fr}}
.stills{display:grid; grid-template-columns:2fr 1fr 1fr; grid-template-rows:auto auto; gap:10px}
.stills button{border:0; padding:0; cursor:zoom-in; border-radius:6px; overflow:hidden; background:#000}
.stills button img{width:100%; height:100%; object-fit:cover; aspect-ratio:16/10}
.stills button:first-child{grid-row:span 2} .stills button:first-child img{aspect-ratio:auto; height:100%}
@media (max-width:760px){.stills{grid-template-columns:1fr 1fr} .stills button:first-child{grid-column:span 2; grid-row:auto}}
.film--bae .gpanel{--g-bg:#0b2128}
.film--bae .before{--b-bg:#0b2128; --b-line:rgba(21,255,200,.3)}
.film--bae .card{background:#0b2128; color:#fff; border-color:rgba(21,255,200,.3)} .film--bae .card__body p{color:rgba(255,255,255,.75)}
.film--bae .qa{--qa-line:rgba(255,255,255,.15)}
.quote-ella{font-family:var(--px); font-size:clamp(1.1rem,2vw,1.6rem); line-height:1.4; color:#fff; margin:0}
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
    tabs = ''.join(f'<button class="lvl" role="tab" id="lv-{i}" aria-controls="lvp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(a_)}</small><span>{esc(t)}</span></button>' for i, (a_, t, *_r) in enumerate(LEVELS))
    panels = ''.join(f'''<div class="lvlpanel" role="tabpanel" id="lvp-{i}" aria-labelledby="lv-{i}"{"" if i==0 else " hidden"}><div><p class="clip"><b>Clip</b>{esc(clip)}</p><h3>{esc(a_)}: {esc(t)}</h3><p style="color:rgba(255,255,255,.85)">{esc(obj)}</p><h4>Discussion questions</h4><ul>{"".join(f"<li>{esc(q)}</li>" for q in qs)}</ul></div><div><h4>Key teaching points</h4><ul>{"".join(f"<li>{esc(k)}</li>" for k in keys)}</ul></div></div>''' for i, (a_, t, obj, clip, qs, keys) in enumerate(LEVELS))
    ds = [('Distract', 'Divert attention to give someone a safe chance to exit. It avoids direct confrontation and can de-escalate quickly.', ['Hey, come to the bathroom with me.', 'We need to leave, we have a big game tomorrow.']),
          ('Delegate', 'Ask someone else for help if you don’t feel comfortable stepping in alone: a friend, coach, staff member or parent.', ['Will you come check on Tanya with me?', 'Call or text for backup.']),
          ('Direct', 'Address the behavior directly by naming it or telling the person to stop.', ['They’ve had enough. Leave them alone.', 'This isn’t okay. You need to stop. Now.']),
          ('Delay', 'If you can’t step in during the moment, you can always follow up afterward.', ['Hey, you seemed upset. Are you okay?', 'Do you need me to call someone for you?'])]
    dhtml = ''.join(f'<div class="d"><b>D{i+1}</b><h3>{esc(n)}</h3><p>{esc(t)}</p>' + ''.join(f'<span class="bub">“{esc(x)}”</span>' for x in ex) + '</div>' for i, (n, t, ex) in enumerate(ds))
    barriers = ['It’s none of my business.', 'Someone else will step in.', 'I’m not sure if what I’m seeing is really crossing the line.', 'I don’t want people to be mad at me.', 'If I say something, it might start a fight.', 'I don’t know what to say.', 'I don’t want to cause a scene.', 'I don’t like how they’re acting, but I’ll just stay out of it.']
    harm = [('Verbal', ['Spreading rumors', 'Catcalling', 'Making offensive jokes', 'Name-calling or insulting language', 'Pressuring someone', 'Repeatedly asking someone out after they’ve said no']),
            ('Cyber', ['Posting harmful content on social media', 'Sending unwanted or harassing texts', 'Sending harassing or threatening emails', 'Sharing pictures without consent', 'Pressuring someone to send nude photos']),
            ('Nonverbal', ['Making obscene gestures', 'Writing sexually explicit things about someone', 'Intimidating someone to stop them from reporting harm']),
            ('Physical', ['Unwanted touching or kissing', 'Following or stalking someone', 'Taking someone’s picture without permission'])]
    hhtml = ''.join(f'<div><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in xs)}</ul></div>' for t, xs in harm)
    stills = [('gameon8', 'Game On!'), ('image-4', 'Choose your path'), ('image-3', 'GAME ON! Because stepping in should be everyone’s game'), ('gameon1', 'Game On! still'), ('gameon3', 'Game On! still')]
    sh = ''.join(f'<button data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c in stills)
    body = f'''
<section class="bae-hero">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>BAEcode: Game On!</span></nav>
      <p class="bae-sub">BAEcode: Teaching Bystander Intervention</p>
      <h1 class="bae-title">Game<br>On!</h1>
      <p class="lede">Because stepping in should be everyone’s game. Created with teens, for teens by SafeBAE co-founder Ella Fairon, this short film shows everyday situations and gives young people simple, practical strategies to step in, in person or online. The entire production team, from writing and directing to casting, was high school and college students.</p>
      <div class="btns"><a class="btn btn--coral press" href="#film">Press start</a>{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div class="arcade" id="film">{yt('BCqkJSXCu-E', 'GAME ON!', thumb='gameon5', label='Full film')}<div class="arcade__lbl"><span>Player 1: Jamie</span><span>Insert coin: free</span></div></div>
  </div>
  <div class="wrap hudwrap" style="padding-bottom:clamp(40px,5vw,72px)">
    <div class="hud"><div><b>44%</b><span>The presence of a bystander makes a completed rape 44% less likely.</span><small>Clay-Warner, 2002</small></div><div><b>17%</b><span>Sexual violence rates fell by 17% on U.S. campuses that trained students in bystander intervention.</span><small>Green Dot</small></div><div><b>30%</b><span>A bystander is present in roughly 30% of sexual assaults, including threats of rape or unwanted sexual contact.</span><small>Associated Press</small></div></div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap split split--top">
    <div>
      <p class="eyebrow">What is BAEcode?</p>
      <h2>Flip the Bro Code.</h2>
      <p style="color:rgba(255,255,255,.88)">“Bro code” means protecting your friend above all else, even at someone else’s expense. BAEcode flips that script. Instead of loyalty to a small circle, it’s a commitment to look out for anyone who might need help, whether or not they’re your friend.</p>
      <p style="color:rgba(255,255,255,.88)">SafeBAE launched the campaign during Sexual Assault Awareness Month in 2018 to give teens the tools and confidence to practice bystander intervention, and to prevent sexual harassment and assault within their own peer groups.</p>
      <blockquote style="margin:26px 0 0"><p class="quote-ella">“The idea is simple: many cases of sexual violence can be prevented or stopped if an alert bystander intervenes in time.”</p><span class="cite" style="color:#15ffc8">Ella Fairon, Director</span></blockquote>
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
</section>

<section class="bae-band" id="missions">
  <div class="wrap">
    <p class="eyebrow">Level select</p>
    <h2>Play it mission by mission.</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">Watch the full film once and gather first reactions: What stood out? What felt realistic, and what didn’t? What makes stepping in hard? Then replay each clip and work through the mission.</p>
    <div data-tabs="baecode"><div class="lvls" role="tablist" aria-label="Missions">{tabs}</div>{panels}</div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap">
    <p class="eyebrow">Power-ups</p>
    <h2>The Four D’s</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">Jamie uses distraction, but it isn’t the only tool. BAEstanders have four strategies, and bystander intervention works best when friends share the responsibility.</p>
    <div class="ds">{dhtml}</div>
  </div>
</section>

<section class="bae-band">
  <div class="wrap">
    <div class="split split--top">
      <div><p class="eyebrow">Obstacles</p><h2>Why people don’t step in</h2><p style="color:rgba(255,255,255,.88)">Without talking about it or giving people easy strategies, most bystanders do nothing. Intervening can be intimidating even for adults, and young people face extra social pressure. Research shows that when teens learn practical strategies, harassment and sexual assault go down.</p></div>
      <div class="barriers">{''.join(f'<span>“{esc(b)}”</span>' for b in barriers)}</div>
    </div>
    <h3 class="px" style="margin:48px 0 16px; color:#15ffc8; font-weight:400">Know what to look for</h3>
    <div class="harm">{hhtml}</div>
  </div>
</section>

<section class="bae-band bae-band--alt">
  <div class="wrap">
    <p class="eyebrow">Behind the scenes</p><h2>Made by students</h2>
    <div class="stills" data-gallery>{sh}</div>
    <details class="note" style="margin-top:28px;background:#0b2128;border-color:rgba(21,255,200,.3);color:#fff"><summary style="cursor:pointer;font-weight:800">Alcohol, consent and Game On!</summary><p style="margin-top:12px">SafeBAE does not condone, encourage or endorse underage drinking. In a recent national survey, 10% of 8th graders and 35% of 12th graders reported drinking in the past 30 days. Youth who drink are more likely to experience sexual assault, and about half of adolescent sexual assault victims seen in emergency departments report that alcohol or other substances were used immediately before the assault. SafeBAE developed GAME ON! using a reality-based education model, because bystander education has to be honest, relatable and comprehensive.</p></details>
  </div>
</section>

<section class="bae-band"><div class="wrap"><p class="eyebrow">Before you begin</p><h2>Set up the room</h2>{before_you_begin()}<div style="margin-top:18px">{help_inline()}</div></div></section>
{guide_panel('baecode')}
<section class="bae-band bae-band--alt"><div class="wrap"><p class="eyebrow">Go deeper</p><h2>Teach these next</h2>{related(['dating', 'rape-culture', 'red-flags'])}</div></section>
'''
    film_page('film-baecode-game-on.html', 'BAEcode: Game On!', 'BAEcode: Game On! is SafeBAE’s bystander intervention film and teaching guide, made by high school and college students.', body, 'bae', 'family=Silkscreen', CSS)
