from films_common import *

CSS = '''
.film--red{--night:#0c1d22; --neon:#fe7171; --neon2:#15ffc8; --f-card:#152f37; --f-line:rgba(255,255,255,.1); --f-ink:#fff; --f-ink2:rgba(255,255,255,.8); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint)}
.film--red main{background:var(--night); color:#fff}
.rf-neon{font-family:'Tilt Neon',sans-serif; font-weight:400; color:#ffe3e3; text-transform:uppercase; text-shadow:0 0 4px #fff, 0 0 10px var(--neon), 0 0 22px var(--neon), 0 0 44px var(--neon), 0 0 80px rgba(254,113,113,.6); letter-spacing:.02em}
.rf-hero{position:relative; overflow:hidden}
.rf-hero__bg{position:absolute; inset:0}
.rf-hero__bg img{width:100%; height:100%; object-fit:cover; opacity:.18; filter:grayscale(.4)}
.rf-hero__bg::after{content:""; position:absolute; inset:0; background:radial-gradient(ellipse at 30% 40%, rgba(12,29,34,.4), var(--night) 72%)}
.rf-hero .wrap{position:relative; display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(28px,5vw,70px); align-items:center; padding-block:clamp(48px,7vw,100px)}
.rf-title{font-size:clamp(3.4rem,8.4vw,8rem); line-height:.92; margin:0 0 .3em}
.rf-title span{display:block}
.rf-title .mk{width:fit-content; background:none; color:inherit; padding:0 0 .16em; position:relative}
.rf-title .mk > span:first-child{color:#fff; text-shadow:0 0 4px #fff, 0 0 12px var(--neon), 0 0 30px var(--neon), 0 0 70px var(--neon)}
.rf-title .mk::after{content:""; position:absolute; left:.04em; right:.04em; bottom:0; height:.075em; border-radius:99px; background:#d9fff5; box-shadow:0 0 4px #fff, 0 0 12px var(--neon2), 0 0 28px var(--neon2), 0 0 56px rgba(21,255,200,.45)}
@keyframes flick{0%,18%,22%,25%,53%,57%,100%{opacity:1} 20%,24%,55%{opacity:.25}}
.rf-title > span:nth-child(2){animation:flick 2.6s 0.6s 1 both}
.rf-hero .lede{color:rgba(255,255,255,.88)}
.rf-hero .crumbs{color:rgba(255,255,255,.6)}
.rf-vid{border:2px solid rgba(254,113,113,.55); box-shadow:0 0 0 6px rgba(254,113,113,.08), 0 0 60px rgba(254,113,113,.28)}
.rf-band{padding-block:var(--band)}
.rf-band--lift{background:#11272e}
.rf-band h2{font-size:clamp(2rem,4.4vw,3.6rem)}
.rf-band .eyebrow{color:var(--neon)}
.feedwrap{display:grid; grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr); gap:clamp(24px,4vw,56px); align-items:start}
.feed{display:grid; gap:18px}
.post{background:#152f37; border:1px solid rgba(255,255,255,.1); border-radius:var(--r-xl); overflow:hidden}
.post__head{display:flex; gap:12px; align-items:center; padding:16px 18px 10px}
.post__av{width:44px; height:44px; border-radius:50%; display:grid; place-items:center; background:var(--night); border:2px solid var(--neon); color:var(--neon); font-family:'Tilt Neon',sans-serif; font-size:1.05rem; box-shadow:0 0 14px rgba(254,113,113,.5)}
.post__who b{display:block; font-size:.95rem}
.post__who small{color:rgba(255,255,255,.6); font-size:.8rem}
.post__scene{margin-left:auto; font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--neon2)}
.post__text{padding:0 18px 14px; font-size:1.06rem; line-height:1.55}
.post__text b{font-family:'Tilt Neon',sans-serif; font-weight:400; color:#ffd0d0; font-size:1.35rem; display:block; margin-bottom:4px}
.post__flags{display:flex; flex-wrap:wrap; gap:6px; padding:0 18px 14px}
.flag{display:inline-flex; align-items:center; gap:6px; font-size:.78rem; font-weight:700; padding:5px 10px 5px 8px; border-radius:999px; background:rgba(254,113,113,.14); color:#ffc9c9; border:1px solid rgba(254,113,113,.35)}
.flag::before{content:""; width:10px; height:12px; background:linear-gradient(var(--neon),var(--neon)) left/2px 100% no-repeat, linear-gradient(var(--neon),var(--neon)) 2px 0/8px 7px no-repeat}
.post .qa{--qa-line:rgba(255,255,255,.1); padding:0 18px}
.post details.qa-wrap{border-top:1px solid rgba(255,255,255,.1)}
.post details.qa-wrap > summary{list-style:none; cursor:pointer; padding:14px 18px; font-weight:800; color:var(--neon2); display:flex; justify-content:space-between}
.post details.qa-wrap > summary::-webkit-details-marker{display:none}
.post details.qa-wrap > summary::after{content:"+"; font-size:1.2rem}
.post details.qa-wrap[open] > summary::after{content:"\\2013"}
.post .note-f{margin:4px 18px 18px; padding:14px; border-radius:12px; background:rgba(21,255,200,.08); border:1px solid rgba(21,255,200,.25); font-size:.92rem}
.side{position:sticky; top:110px; display:grid; gap:14px}
.side__card{background:#152f37; border:1px solid rgba(255,255,255,.1); border-radius:var(--r-xl); padding:20px}
.side__card h3{font-size:1.2rem}
.side__card p,.side__card li{color:rgba(255,255,255,.82); font-size:.93rem}
@media (max-width:960px){.feedwrap,.rf-hero .wrap{grid-template-columns:1fr} .side{position:static}}
/* MOVERS */
.movers{display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:10px; margin:28px 0 22px}
.movers button{font:inherit; cursor:pointer; background:#11272e; border:2px solid rgba(254,113,113,.3); border-radius:16px; padding:18px 8px 14px; color:#fff; display:flex; flex-direction:column; align-items:center; gap:6px; transition:border-color .2s, background .2s}
.movers button b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:clamp(2.4rem,5vw,4.2rem); line-height:1; color:#ffe3e3; text-shadow:0 0 8px var(--neon), 0 0 24px var(--neon)}
.movers button span{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:rgba(255,255,255,.75)}
.movers button[aria-pressed="true"]{border-color:var(--neon); background:#1a3640}
.movers button[aria-pressed="false"] b{text-shadow:0 0 6px rgba(254,113,113,.5); color:#ffb3b3}
.pillar{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(20px,4vw,48px); background:#152f37; border-radius:var(--r-xl); padding:clamp(20px,3vw,34px); border:1px solid rgba(255,255,255,.1)}
.pillar h3{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:2.2rem; color:#ffe3e3; text-shadow:0 0 10px var(--neon); text-transform:uppercase}
.pillar p{color:rgba(255,255,255,.88)}
.pillar .qa{--qa-line:rgba(255,255,255,.12)}
@media (max-width:760px){.movers{grid-template-columns:repeat(3,minmax(0,1fr))} .pillar{grid-template-columns:1fr}}
/* red to green */
.spec-legend{display:grid; grid-template-columns:1fr 1fr 1fr; text-align:center; font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; margin:20px 0 8px}
.spec-bar{position:relative; height:14px; border-radius:999px; background:linear-gradient(90deg, var(--neon), #9fb3b8 50%, var(--neon2))}
.spec-bar i{position:absolute; top:50%; width:22px; height:22px; margin:-11px 0 0 -11px; border-radius:50%; background:#fff; border:4px solid var(--night); box-shadow:0 0 0 2px rgba(255,255,255,.5), 0 0 16px rgba(255,255,255,.5); transform:scale(0); transition:transform .45s var(--ease)}
.spec-bar i.on{transform:scale(1)}
.spec-count{margin:12px 0 0; font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:rgba(255,255,255,.7); text-align:center}
.rf-ch{display:flex; gap:14px 26px; align-items:center; flex-wrap:wrap; margin-top:16px; padding:18px 22px; border-radius:18px; border:1px solid rgba(254,113,113,.4); background:rgba(254,113,113,.07); color:#fff; text-decoration:none; transition:background .25s, border-color .25s}
.rf-ch:hover{background:rgba(254,113,113,.13); border-color:var(--neon)}
.rf-ch b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:1.6rem; line-height:1; text-transform:uppercase; color:#ffe3e3; text-shadow:0 0 8px var(--neon), 0 0 22px var(--neon); flex:none}
.rf-ch span{flex:1 1 360px; min-width:0; color:rgba(255,255,255,.88)}
.rf-ch i{font-style:normal; font-weight:800; color:var(--neon2); flex:none}
.scen{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; margin-top:26px}
.sc{background:#152f37; border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:18px; display:flex; flex-direction:column; gap:12px}
.sc p.s{font-weight:700; font-size:1.08rem; margin:0}
.sc .opts{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:6px}
.sc .opts button{font:inherit; font-size:.8rem; font-weight:800; padding:9px 6px; border-radius:8px; border:2px solid rgba(255,255,255,.18); background:transparent; color:#fff; cursor:pointer}
.sc .opts button[data-v="0"]:hover,.sc .opts button[data-v="0"][aria-pressed="true"]{background:var(--neon); border-color:var(--neon); color:var(--slate)}
.sc .opts button[data-v="1"]:hover,.sc .opts button[data-v="1"][aria-pressed="true"]{background:#9fb3b8; border-color:#9fb3b8; color:var(--slate)}
.sc .opts button[data-v="2"]:hover,.sc .opts button[data-v="2"][aria-pressed="true"]{background:var(--neon2); border-color:var(--neon2); color:var(--slate)}
.sc .mini{position:relative; height:8px; border-radius:99px; background:linear-gradient(90deg, var(--neon), #9fb3b8 50%, var(--neon2)); opacity:.35}
.sc .mini i{position:absolute; top:50%; width:18px; height:18px; margin:-9px 0 0 -9px; border-radius:50%; background:#fff; border:3px solid var(--night); display:none}
.sc.done .mini{opacity:1}
.sc.done .mini i{display:block}
.sc .why{display:none; font-size:.93rem; color:rgba(255,255,255,.88); margin:0}
.sc.done .why{display:block}
.sc .why b{color:var(--neon2)}
@media (max-width:760px){.scen{grid-template-columns:1fr}}
/* grounding */
.ground{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(20px,4vw,56px); align-items:center}
@media (max-width:760px){.ground{grid-template-columns:minmax(0,1fr)}}
.g54321{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:8px}
.g54321 button{font:inherit; cursor:pointer; aspect-ratio:3/4; border-radius:14px; border:2px solid rgba(21,255,200,.3); background:#11272e; color:#fff; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:6px; padding:6px; transition:all .25s}
.g54321 button b{font-family:'Tilt Neon',sans-serif; font-weight:400; font-size:clamp(2rem,4vw,3.4rem); color:#c9fff1; text-shadow:0 0 12px var(--neon2); line-height:1}
.g54321 button span{font-size:.78rem; font-weight:700; text-align:center}
.g54321 button[aria-pressed="true"]{background:rgba(21,255,200,.12); border-color:var(--neon2)}
.posters2{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px}
.posters2 button{border:0; padding:14px; background:#11272e; cursor:zoom-in; border-radius:14px; overflow:hidden; aspect-ratio:1; display:grid; place-items:center} .posters2 button img{max-height:100%; width:auto; object-fit:contain; border-radius:6px}
.film--red .prompts{--p-bg:#152f37}
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

def build():
    posts = []
    for av, sc, who, text, flags, qs, note in SCENES:
        posts.append(f'''<article class="post"><div class="post__head"><span class="post__av">Ref</span><span class="post__who"><b>@itsgivingredflags</b><small>Submitted anonymously</small></span><span class="post__scene">{sc}</span></div>
<div class="post__text"><b>{esc(who)}</b>{esc(text)}</div><div class="post__flags">{''.join(f'<span class="flag">{esc(f)}</span>' for f in flags)}</div>
<details class="qa-wrap"><summary>Discussion prompts &amp; answers</summary>{qa(qs)}<p class="note-f"><b>Facilitator note.</b> {esc(note)}</p></details></article>''')
    movers = ''.join(f'<button aria-pressed="{str(i==0).lower()}" data-p="{i}"><b>{L}</b><span>{esc(n)}</span></button>' for i, (L, n, *_r) in enumerate(PILLARS))
    pill_panels = ''.join(f'<div class="pillar" data-panel="{i}"{"" if i==0 else " hidden"}><div><p class="eyebrow">Pillar {i+1} of 6</p><h3>{esc(n)}</h3><p>{esc(t)}</p></div><div>{qa(qs) if qs else "<p>Put this pillar to work in the <a class=\"link\" href=\"#red-to-green\">Red to Green activity</a>: the example “We hooked up last weekend, so tonight is a yes.” turns on it.</p>"}</div></div>' for i, (L, n, t, qs) in enumerate(PILLARS))
    cnt = {0:0, 1:0, 2:0}; pos = []
    for _s, v, _p, _w in SCEN:
        base = {0:5, 1:50, 2:95}[v]; step = {0:6, 1:6, 2:-6}[v]
        pos.append(base + cnt[v]*step); cnt[v] += 1
    pins = ''.join(f'<i data-pin="{i}" style="left:{x}%"></i>' for i, x in enumerate(pos))
    scen = ''.join(f'''<div class="sc" data-ans="{v}" data-i="{i}"><p class="s">“{esc(s)}”</p><div class="opts" role="group" aria-label="Where does this fall?"><button data-v="0" aria-pressed="false">Not consent</button><button data-v="1" aria-pressed="false">Unsure</button><button data-v="2" aria-pressed="false">Consent</button></div><div class="mini"><i></i></div><p class="why"><b>{esc(p)}.</b> {esc(w)}</p></div>''' for i, (s, v, p, w) in enumerate(SCEN))
    ground = [('5', 'things you can see'), ('4', 'things you can touch'), ('3', 'things you can hear'), ('2', 'things you can smell'), ('1', 'thing you can taste')]
    gbtns = ''.join(f'<button aria-pressed="false"><b>{n}</b><span>{t}</span></button>' for n, t in ground)
    body = f'''
<section class="rf-hero fhero fhero--dark">
  <div class="rf-hero__bg">{img('yt-ett8bnlbwwg', '', loading='eager')}</div><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>It’s Giving Red Flags</span></nav>
      <p class="eyebrow" style="color:var(--neon2)">A SafeBAE short film + teaching guide</p>
      <h1 class="rf-title rf-neon" aria-label="It's Giving Red Flags"><span>It’s</span><span>Giving</span><span class="mk"><span>Red</span><span>Flags</span></span></h1>
      <p class="lede">Nessa anonymously runs a social media page called <i>It’s Giving Red Flags</i> under the name “The Ref.” As she sorts through her peers’ relationship stories, calling out manipulative and controlling behavior, she starts to recognize red flags in her own relationship.</p>
      <div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=ETt8BnLbWwg', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div>{yt('ETt8BnLbWwg', 'It’s Giving Red Flags', cls='rf-vid', label='Full film')}<p class="small" style="color:rgba(255,255,255,.7);margin-top:14px">The film highlights scenarios that are often left out of mainstream, heteronormative portrayals of consent, and shows how easily harmful dynamics can be missed in real life.</p></div>
  </div>
</section>

<section class="rf-band rf-band--lift">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Before you press play</p><h2>Red flag or a violation of consent?</h2>
    <p class="lede" style="color:rgba(255,255,255,.85)">This guide helps students tell the difference between early warning signs and behavior that rises to coercion, harassment or assault.</p></div></div>
    <div class="grid g2">
      <div class="side__card"><h3>Unintentional harm is still harm</h3><p>Violations of consent aren’t always intentional, and harm can happen without malicious intent. Intention does not erase the harm, which is why clear, thoughtful discussion of consent matters.</p></div>
      <div class="side__card"><h3>Impact matters more than intent</h3><p>Sexual harassment and assault are judged by how the survivor experiences the behavior, not by what the other person meant to do. Assault can happen through emotional manipulation or coercion, not only physical force.</p><p class="small" style="margin-top:10px"><b>Ask the group:</b> Why is it important to focus on the impact of someone’s actions rather than their intent when talking about consent and harm?</p></div>
    </div>
  </div>
</section>

<section class="rf-band" id="movers">
  <div class="wrap">
    <p class="eyebrow">The pillars of consent</p>
    <h2>Watch the film with MOVERS in mind.</h2>
    <p class="lede" style="color:rgba(255,255,255,.85)">Establish the six pillars before you show the film, then keep coming back to them. Ask students to notice where consent is missing or can’t be present.</p>
    <div class="movers" role="group" aria-label="Pillars of consent">{movers}</div>
    {pill_panels}
    <a class="rf-ch" href="choking-hazard.html"><b>Choking Hazard</b><span>Choking can’t meet these pillars: there’s no safe way to choke someone. SafeBAE’s campaign on sexual strangulation, which young people call “choking”, has the evidence and free warning posters.</span><i>Read the campaign &rarr;</i></a>
  </div>
</section>

<section class="rf-band rf-band--lift" id="scenes">
  <div class="wrap feedwrap">
    <div>
      <p class="eyebrow">Recap the scenes</p>
      <h2>The submissions</h2>
      <p class="lede" style="color:rgba(255,255,255,.85)">After the film, recap each scene and work through the prompts. Brief answers are included for facilitators.</p>
      <div class="feed">{''.join(posts)}</div>
    </div>
    <aside class="side">
      <div class="side__card"><h3>How to run it</h3><ol><li>Introduce the six pillars of consent.</li><li>Watch the full film.</li><li>Recap each scene and discuss.</li><li>Practice grounding together.</li><li>Finish with Red to Green.</li></ol></div>
      <div class="side__card"><h3>Before you begin</h3><p>Tell your counselors first, make it okay to step out, and be clear about mandated reporting.</p><a class="arrow-link" href="#begin" style="color:var(--neon2)">Read the checklist</a></div>
    </aside>
  </div>
</section>

<section class="rf-band" id="ground">
  <div class="wrap ground">
    <div>
      <p class="eyebrow" style="color:var(--neon2)">Bonus scene: grounding</p>
      <h2>Do what Nessa does.</h2>
      <p class="lede" style="color:rgba(255,255,255,.85)">After a high-stress moment, Nessa uses the 5-4-3-2-1 technique to bring herself back to the present. Remind students it is always okay to take a break when they feel activated, in class or in real life.</p>
      <p style="color:rgba(255,255,255,.8)">Try it together: tap each number as you notice those things around you. You can also guide a body scan, five slow breaths (in through the nose, out through the mouth), or a supportive phrase repeated five times, such as “I deserve to be loved and happy.”</p>
    </div>
    <div><div class="g54321" role="group" aria-label="5-4-3-2-1 grounding">{gbtns}</div><p class="small" id="gdone" style="color:var(--neon2);margin-top:12px" aria-live="polite"></p></div>
  </div>
</section>

<section class="rf-band rf-band--lift" id="red-to-green">
  <div class="wrap">
    <p class="eyebrow">Activity</p>
    <h2>Consent: Red to Green</h2>
    <p class="lede" style="color:rgba(255,255,255,.85)">In class, students write their own anonymous red-flag and green-flag examples and place them on the spectrum. You can also use printed examples. Here are six to sort together.</p>
    <div class="spec-legend"><span style="color:var(--neon)">100% not consent</span><span>Unsure</span><span style="color:var(--neon2)">100% consent</span></div>
    <div class="spec-bar" aria-hidden="true">{pins}</div><p class="spec-count" id="speccount" aria-live="polite">0 of 6 sorted</p>
    <div class="scen">{scen}</div>
  </div>
</section>

{vibe_band("Nessa begins to recognize red flags in her own relationship once she looks at it honestly. Vibe Check gives young people a private place to do the same: a free, anonymous reflection tool for anyone worried they crossed a line or caused harm.")}

<section class="rf-band">
  <div class="wrap split">
    <div><p class="eyebrow">Shareable graphics</p><h2>Put it on the wall.</h2><p class="lede" style="color:rgba(255,255,255,.85)">Posters that go with the film. Download the full set for free.</p>{btn('Download all posters (.zip)', POSTERS_ZIP, 'mint')}</div>
    <div class="posters2" data-gallery><button data-src="{imgsrc('no-means-no-pdf')}" data-cap="No means no, but so does…">{img('no-means-no-pdf', 'Poster: No means no, but so does silence, maybe later, I’m not sure, being drunk')}</button><button data-src="{imgsrc('screen-shot-2023-01-23-at-5-56-30-pm-1')}" data-cap="No doesn’t mean convince me">{img('screen-shot-2023-01-23-at-5-56-30-pm-1', 'Graphic: No doesn’t mean convince me')}</button></div>
  </div>
</section>

{begin('rf-band rf-band--lift', 'These conversations can surface strong emotions and may lead to disclosures of abuse.', help_extra='<span>LGBTQ+ youth: The Trevor Project, text START to 678-678</span>')}
{tail('red-flags', ['knowb4unude', 'male-survivors', 'baecode'], 'rf-band')}
'''
    js = r'''<script>
(function(){
  var bs = document.querySelectorAll('.movers button'), ps = document.querySelectorAll('.pillar');
  bs.forEach(function(b){ b.addEventListener('click', function(){ bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x===b)); }); ps.forEach(function(p){ p.hidden = p.dataset.panel !== b.dataset.p; }); }); });
  document.querySelectorAll('.sc').forEach(function(c){ c.querySelectorAll('.opts button').forEach(function(b){ b.addEventListener('click', function(){ c.querySelectorAll('.opts button').forEach(function(x){ x.setAttribute('aria-pressed', String(x===b)); }); c.classList.add('done'); var i = c.querySelector('.mini i'); i.style.left = ({0:6,1:50,2:94})[c.dataset.ans] + '%'; var pin = document.querySelector('[data-pin="' + c.dataset.i + '"]'); if(pin) pin.classList.add('on'); var sc = document.getElementById('speccount'); if(sc){ var n = document.querySelectorAll('.sc.done').length; sc.textContent = n + ' of 6 sorted' + (n===6 ? '. Only one belongs at the green end.' : ''); } }); }); });
  var g = document.querySelectorAll('.g54321 button'), gd = document.getElementById('gdone');
  g.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed', b.getAttribute('aria-pressed')==='true'?'false':'true'); var n = document.querySelectorAll('.g54321 [aria-pressed="true"]').length; gd.textContent = n===5 ? 'Take one more slow breath. You’re here.' : ''; }); });
})();
</script>'''
    film_page('film-its-giving-red-flags.html', 'It’s Giving Red Flags', 'A SafeBAE short film and teaching guide about red flags, the pillars of consent, and unhealthy relationships.',
              body, 'red', 'family=Tilt+Neon', CSS, js)
