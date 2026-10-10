from films_common import *

# Ending Online Harassment of Survivors: SafeBAE's #QuitThisShit campaign.
# The look comes from the campaign's own materials: the black title card set in rough typewriter capitals
# with lower-case i's, the black letter tiles on the wall behind the cast, black shirts, white studio.
# So: near-black page, white type, Special Elite for display, the hash tile as the page's mark,
# photos framed as white-bordered prints. Mint stays the action colour.

CSS = '''
.film--oh{--oh:#0f1a1e; --oh2:#16252b; --oh-line:rgba(255,255,255,.14); --ty:'Special Elite','Courier New',monospace;
  --f-card:var(--oh2); --f-line:rgba(255,255,255,.14); --f-ink:#fff; --f-ink2:rgba(255,255,255,.84); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint);
  --f-disp:var(--ty); --f-dw:400; --f-dt:uppercase; --f-dl:.01em; --f-ds:100%}
.film--oh main{background:var(--oh) var(--grain); color:#fff}
.film--oh .fx-h{line-height:1.1}

/* the campaign's letter tiles */
.oh-tiles{display:inline-flex; gap:5px; flex:none}
.oh-tiles span{display:block; min-width:2.2em; height:2.2em; padding:.66em .5em 0; text-align:center; white-space:nowrap; background:#000; color:#fff; border:2px solid #fff; font-family:var(--ty); font-size:1.02rem; line-height:1; letter-spacing:.02em; text-transform:uppercase}
.oh-tiles i, .oh-title i{font-style:normal; text-transform:none}
.oh-hash{display:grid; place-items:center; width:40px; height:40px; padding-top:5px; background:#000; color:#fff; border:2px solid #fff; font-family:var(--ty); font-size:1.5rem; line-height:1; flex:none}

/* hero: the title and the cast photo hang level; actions and summary under them */
.oh-hero{--wm-o:.1}
.oh-hero .wm-daisy{right:-14%; bottom:-62%}
.oh-hero__g{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-areas:"head pic" "act txt"; gap:clamp(26px,3vw,40px) clamp(28px,4vw,56px); align-items:start; padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,84px)}
.oh-hero__head{grid-area:head; align-self:end; min-width:0; container-type:inline-size}
.oh-hero__pic{grid-area:pic; align-self:end; min-width:0; margin:0; position:relative}
.oh-hero__act{grid-area:act; min-width:0}
.oh-hero__txt{grid-area:txt; min-width:0}
.oh-hero .crumbs{color:rgba(255,255,255,.62)}
.oh-kicker{display:flex; align-items:center; gap:14px 18px; flex-wrap:wrap; margin:0 0 clamp(16px,1.8vw,24px)}
.oh-kicker .eyebrow{margin:0; color:var(--mint)}
.oh-title{font-family:var(--ty); font-weight:400; font-size:min(5.6rem, 13.4cqi); line-height:.98; letter-spacing:.005em; text-transform:uppercase; color:#fff; margin:0 0 -.12em}
.oh-title > span{display:block; white-space:nowrap}
.oh-title .mk{padding:0; background:none; color:var(--mint)}
.oh-print{display:block; width:100%; padding:0; border:10px solid #fff; border-radius:6px; background:#fff; overflow:hidden; cursor:zoom-in; transform:rotate(1.2deg); box-shadow:0 40px 80px -30px rgba(0,0,0,.85); transition:transform .4s var(--ease)}
.oh-print:hover{transform:rotate(0deg) translateY(-4px)}
.oh-print img{display:block; width:100%; aspect-ratio:16/9; object-fit:cover; object-position:50% 30%}
.oh-hero__pic .sticker{position:absolute; left:-14px; bottom:26px; z-index:1}
.oh-hero .lede{color:rgba(255,255,255,.94); margin:0; font-size:clamp(1.06rem,1.34vw,1.22rem)}
.oh-hero__act .btns{gap:10px}
.oh-hero__act .btn{padding-inline:.95em; font-size:.95rem}
.oh-hero__note{margin:18px 0 0; font-size:.98rem; line-height:1.55; color:rgba(255,255,255,.78)}

/* bands and heads */
.oh-band{padding-block:var(--band); position:relative}
.oh-band--alt{background:var(--oh2) var(--grain); --f-card:var(--oh)}
.oh-band h2{font-family:var(--ty); font-weight:400; font-size:clamp(1.9rem,3.9vw,3.1rem); text-transform:uppercase; line-height:1.1; letter-spacing:.01em; margin:0}
.oh-band .eyebrow{color:var(--mint)}
.oh-head{margin-bottom:var(--head-gap)}
.oh-head .lede{margin:.7em 0 0; color:rgba(255,255,255,.9)}
.oh-head--act{display:flex; align-items:end; justify-content:space-between; gap:20px 40px; flex-wrap:wrap}
.oh-head--act > div{flex:1 1 520px; min-width:0}
.oh-g{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:var(--gap) clamp(24px,4vw,56px); align-items:stretch}
.oh-label{display:block; font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--mint); margin:0 0 12px}
.oh-qs{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:10px}
.oh-qs li{flex:1 1 auto; display:flex; align-items:center; margin:0; padding:14px 18px; border-radius:14px; background:rgba(255,255,255,.05); border:1px solid var(--oh-line); font-weight:600; font-size:1.02rem; line-height:1.45}

/* rewrite the thread */
.oh-thread :focus-visible{outline-color:var(--teal)}
.oh-thread{display:flex; flex-direction:column; background:#fff; color:#14272d; border-radius:var(--r-xl); overflow:hidden; box-shadow:0 40px 80px -40px rgba(0,0,0,.8); min-width:0}
.oh-post{display:grid; grid-template-columns:48px minmax(0,1fr); gap:14px; align-items:center; padding:20px 22px; border-bottom:1px solid #d6e5e8; background:#eef7f8}
.oh-post > span{width:48px; height:48px; border-radius:50%; background:var(--slate); color:var(--mint); display:grid; place-items:center}
.oh-post > span .daisy{width:28px; height:28px}
.oh-post b{display:block; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.12rem; line-height:1.25}
.oh-post p{margin:4px 0 0; color:#3f5a62; font-size:.98rem; line-height:1.45}
.oh-cmt{flex:1 1 auto; display:grid; grid-template-columns:42px minmax(0,1fr) auto; gap:14px; align-items:center; min-height:104px; padding:12px 22px; border-bottom:1px solid #e6f0f1; transition:background .4s}
.oh-cmt > i{width:42px; height:42px; border-radius:50%; background:#cfdde0; display:grid; place-items:center; font-style:normal; font-weight:800; font-size:.875rem; color:#46646e; transition:background .3s}
.oh-cmt__t{min-width:0}
.oh-cmt__t small{display:block; font-weight:700; color:#46646e; font-size:.875rem; line-height:1.3}
.oh-cmt .old{margin:2px 0 0; font-size:1.06rem; line-height:1.4; text-decoration:line-through; text-decoration-color:transparent; text-decoration-thickness:2px; transition:color .3s, text-decoration-color .3s}
.oh-cmt .new{display:none; width:fit-content; max-width:100%; margin:7px 0 0; padding:7px 13px; border-radius:16px 16px 16px 4px; background:var(--mint); color:var(--slate); font-weight:800; font-size:1rem; line-height:1.3}
.oh-cmt button{font:inherit; font-size:.875rem; font-weight:800; min-height:44px; padding:8px 12px; border-radius:10px; border:2px solid var(--slate); background:var(--slate); color:#fff; cursor:pointer; white-space:nowrap; transition:background .2s, color .2s, border-color .2s}
.oh-cmt button:hover{background:#fff; color:var(--slate)}
.oh-cmt.fixed{background:#f3fffc}
.oh-cmt.fixed > i{background:var(--mint); color:var(--slate)}
.oh-cmt.fixed .old{font-size:.9rem; color:#6f8990; text-decoration-color:var(--coral)}
.oh-cmt.fixed .new{display:block; animation:oh-type .55s steps(14) both}
.oh-cmt.fixed button{border-color:transparent; background:transparent; color:var(--logo-teal); cursor:default; padding-inline:4px}
@keyframes oh-type{from{clip-path:inset(0 100% 0 0)} to{clip-path:inset(0 0 0 0)}}
.oh-thread__foot{padding:15px 22px; font-family:var(--mono); font-size:.875rem; font-weight:600; color:#3f5a62; display:flex; align-items:center; justify-content:space-between; gap:12px 16px; flex-wrap:wrap}
.oh-meter{height:8px; background:#dfecee; border-radius:99px; overflow:hidden; flex:1 1 72px}
.oh-meter i{display:block; height:100%; width:0; background:var(--teal); border-radius:99px; transition:width .5s var(--ease)}
.oh-side{display:flex; flex-direction:column; justify-content:space-between; gap:20px; min-width:0}
.oh-side > p{margin:0; font-size:1.04rem; line-height:1.6; color:rgba(255,255,255,.92)}
.oh-ask{padding:18px 20px; border-radius:var(--r-xl); border:1.5px solid rgba(21,255,200,.5); background:rgba(21,255,200,.06)}
.oh-ask p{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.08rem; line-height:1.45}
.oh-say__c{display:flex; flex-wrap:wrap; gap:10px}
.oh-say__c span{background:var(--mint); color:var(--slate); padding:10px 15px; border-radius:18px 18px 18px 4px; font-weight:800; font-size:1rem; line-height:1.25}
.oh-say__c span:nth-child(even){background:#fff; border-radius:18px 18px 4px 18px}

/* the films: three tiles, one open */
.oh-tabs{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--gap); margin:0 0 clamp(14px,1.5vw,20px)}
.oh-tab{position:relative; display:flex; flex-direction:column; gap:6px; min-height:92px; padding:16px 20px 18px; text-align:left; font:inherit; color:#fff; cursor:pointer; border-radius:14px; border:2px solid rgba(255,255,255,.2); background:var(--oh2); transition:border-color .25s, background .25s, box-shadow .25s, transform .25s var(--ease)}
.oh-tab small{font-family:var(--mono); font-size:.72rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; color:var(--mint)}
.oh-tab small.w{align-self:flex-start; color:var(--slate); background:var(--coral); padding:2px 7px; border-radius:4px}
.oh-tab b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.2rem; line-height:1.2}
.oh-tab:hover{border-color:rgba(21,255,200,.6); transform:translateY(-2px)}
.oh-tab[aria-selected="true"]{border-color:var(--mint); background:#123035; box-shadow:0 0 0 4px rgba(21,255,200,.12)}
.oh-tab[aria-selected="true"]::after{content:""; position:absolute; left:50%; bottom:-11px; width:16px; height:16px; margin-left:-8px; background:#123035; border-right:2px solid var(--mint); border-bottom:2px solid var(--mint); transform:rotate(45deg); border-radius:0 0 4px 0}
.oh-vp{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(20px,3.4vw,44px); align-items:stretch; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--oh2); border:1px solid var(--oh-line)}
.oh-vp__m{min-width:0}
.oh-vp__m > p{margin:16px 0 0; font-size:1rem; line-height:1.6; color:rgba(255,255,255,.88)}
.oh-vp__q{display:flex; flex-direction:column; min-width:0}
.oh-vp__q .oh-qs{flex:1}
.oh-cw{aspect-ratio:16/9; border-radius:var(--r-lg); background:var(--oh); display:grid; place-items:center; text-align:center; padding:clamp(16px,3vw,28px); border:2px dashed var(--coral)}
.oh-cw .eyebrow{color:var(--coral); margin-bottom:.6rem}
.oh-cw p:not(.eyebrow){margin:0 auto 16px; font-size:1.02rem; line-height:1.5}

/* ways to step in */
.oh-col{display:flex; flex-direction:column; gap:var(--gap); min-width:0}
.oh-tips{flex:1; list-style:none; margin:0; padding:6px var(--pad-card); display:flex; flex-direction:column; border-radius:var(--r-xl); background:var(--oh); border:1px solid var(--oh-line)}
.oh-tips li{flex:1 1 auto; display:grid; grid-template-columns:40px minmax(0,1fr); gap:18px; align-items:center; margin:0; padding:14px 0; font-size:1.1rem; line-height:1.4; color:rgba(255,255,255,.9)}
.oh-tips li + li{border-top:1px solid var(--oh-line)}
.oh-tips b{font-weight:800; color:#fff}
.oh-you{flex:1 1 auto; padding:var(--pad-card); border-radius:var(--r-xl); background:var(--oh); border:1px solid var(--oh-line); border-top:5px solid var(--coral)}
.oh-you h3{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.3rem; line-height:1.15; margin:0 0 .5em}
.oh-you p{margin:0; font-size:1rem; line-height:1.6; color:rgba(255,255,255,.88)}
.oh-you .btns{margin-top:16px}

/* from the campaign: prints hung at their own proportions */
.oh-wall{display:flex; gap:var(--gap); align-items:stretch}
.oh-wall button{flex:var(--ar) 1 0; aspect-ratio:var(--ar); min-width:0; padding:0; border:8px solid #fff; border-radius:6px; background:#fff; overflow:hidden; cursor:zoom-in; box-shadow:0 30px 60px -34px rgba(0,0,0,.85); transition:transform .3s var(--ease)}
.oh-wall button:hover{transform:translateY(-4px) rotate(-.6deg)}
.oh-wall button:nth-child(even):hover{transform:translateY(-4px) rotate(.6deg)}
.oh-wall img{display:block; width:100%; height:100%; object-fit:cover}
.oh-wall .oh-still img{transform:scale(1.05)}

@media (max-width:1000px){
  .oh-g, .oh-vp{grid-template-columns:minmax(0,1fr)}
  .oh-tab b{font-size:1.08rem}
}
@media (max-width:900px){
  /* two rows of two: one column line for both rows, each row as tall as its first print */
  .oh-wall{display:grid; grid-template-columns:37.3fr 62.7fr}
  .oh-wall button{flex:none; width:100%; height:100%; aspect-ratio:auto}
  .oh-wall button:nth-child(1){aspect-ratio:1; height:auto}
  .oh-wall button:nth-child(3){aspect-ratio:.75; height:auto}
  .oh-wall .oh-still img{transform:scale(1.14)}
}
@media (max-width:960px){
  .oh-hero__g{grid-template-columns:minmax(0,1fr); grid-template-areas:"head" "pic" "txt" "act"}
  .oh-hero__pic .sticker{left:10px}
  .oh-print{transform:none}
}
@media (max-width:760px){
  .oh-tabs{grid-template-columns:minmax(0,1fr); gap:10px}
  .oh-tab{min-height:0; flex-direction:row; align-items:center; justify-content:space-between; gap:12px; padding:14px 18px}
  .oh-tab small{order:2; flex:none}
  .oh-tab[aria-selected="true"]::after{display:none}
}
@media (max-width:560px){
  .oh-wall{grid-template-columns:minmax(0,1fr)} .oh-wall button, .oh-wall button:nth-child(1), .oh-wall button:nth-child(3){aspect-ratio:var(--ar); height:auto}
  .oh-wall .oh-still img{transform:scale(1.05)}
  .oh-cmt{grid-template-columns:36px minmax(0,1fr); gap:10px 12px; padding:14px 16px; min-height:0}
  .oh-cmt > i{width:36px; height:36px; grid-row:span 2; align-self:start}
  .oh-cmt button{grid-column:2; justify-self:start}
  .oh-post{padding:16px}
  .oh-tips li{grid-template-columns:34px minmax(0,1fr); gap:14px; font-size:1.04rem}
  .oh-hash{width:34px; height:34px; font-size:1.25rem}
  .oh-cw{aspect-ratio:auto}
  .film--oh .oh-vp .vid__label{font-size:.92rem; padding:9px 12px 10px} .film--oh .oh-vp .vid__label small{display:none}
  .oh-vp{padding:14px}
}
'''

CMTS = [('Why were you there?', 'It’s not your fault.'), ('Were you drinking?', 'You didn’t deserve that.'), ('What were you wearing?', 'I’m here for you.'),
        ('If it was really a big deal, why didn’t you tell anyone sooner?', 'Thank you for telling me.'), ('It’s going to be fine, just move on.', 'Let me know how I can support you.')]

TIPS = ['<b>Report</b> the harmful post, account or comment to the platform.', '<b>Don’t like, share or repost</b> hurtful messages or images.', '<b>Show support</b> to the survivor, online and in person.',
        '<b>Report harassment</b> to a trusted adult.', 'If you hear gossip, <b>speak up</b> and say it’s not okay.']

HASH = '<span class="oh-hash" aria-hidden="true">#</span>'

def build():
    cm = ''.join(f'<div class="oh-cmt"><i aria-hidden="true">{chr(65+i)}{chr(75+i)}</i><div class="oh-cmt__t"><small>user_{4821+i*137}</small><p class="old">{esc(o)}</p><p class="new">{esc(n)}</p></div><button type="button">Report &amp; reply</button></div>' for i, (o, n) in enumerate(CMTS))
    films = [
      ('cy', 'What It’s Like to Be Cyberbullied', False, yt('TTPzlIWqxqE', 'What It’s Like to Be Cyberbullied as a Sexual Assault Survivor', label='SafeBAE x Teen Vogue'), 'The non-explicit short film from SafeBAE’s campaign to break the cycle of online revictimization. Appropriate for all school settings.',
       ['What are your initial thoughts and feelings after watching?', 'Survivors of sexual assault often experience guilt and self-blame. How does victim blaming or online harassment amplify those emotions?', 'The film highlights common victim-blaming phrases. Do you notice this kind of language in your community? How can you push back when you hear it, in person or online?']),
      ('end', 'Help Put an End to It', False, yt('-I4Jmz7Yxys', 'Help put an end to online harassment of teen survivors', label='Non-explicit'), 'A second non-explicit option from the same campaign.',
       ['Before watching, had you thought about the effect a single post, comment or message could have on someone?', 'How might this change the way you act online?', 'Do you know how to report online harassment if it happened to you or a friend?']),
      ('qts', '#QuitThisSh*t', True, None, 'Created by SafeBAE youth leaders in 2016. The script was written entirely from real messages survivors have received, so it is explicit. Many educators find that this authenticity makes it especially powerful, but use your discretion and consider the non-explicit options.',
       ['What are your first thoughts or feelings after watching?', 'Do you know someone who has been harassed online? What was the impact on them? (Don’t share names or identifying details.)', 'Have you heard of something similar happening in your community? Did people gossip about the survivor? Were there consequences for the people responsible?', 'Are you aware of help services or how to report online harassment?']),
    ]
    vt = ''.join(f'<button class="oh-tab" type="button" role="tab" id="vt-{k}" aria-controls="vp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small{" class=w" if w else ""}>{"Explicit" if w else "Non-explicit"}</small><b>{esc(t)}</b></button>' for i, (k, t, w, *_r) in enumerate(films))
    vp = []
    for i, (k, t, w, media, d, qs) in enumerate(films):
        if w:
            media = f'<div class="oh-cw" data-cw><div><p class="eyebrow">Content warning</p><p>This video contains explicit language and real messages survivors received. It may not be appropriate for all school settings.</p><button class="btn btn--coral btn--sm" type="button" data-reveal>Show the video</button></div><template>{yt("UbeoN5zlPGo", "#QuitThisShit", label="Explicit language")}</template></div>'
        vp.append(f'<div class="oh-vp" role="tabpanel" id="vp-{k}" aria-labelledby="vt-{k}"{"" if i==0 else " hidden"}><div class="oh-vp__m">{media}<p>{esc(d)}</p></div><div class="oh-vp__q"><h3 class="oh-label">Discuss</h3><ul class="oh-qs">{"".join(f"<li>{esc(q)}</li>" for q in qs)}</ul></div></div>')
    wall = [('poster-ending-online-harassment', 'Poster: Ending online harassment is everyone’s responsibility', 1.0),
            ('screen-shot-2017-04-18-at-4-07-42-pm', '#QuitThisShit still', 16 / 9),
            ('online-harassment-poster-5', 'Poster: No one can do everything, but everyone can do something. End rape culture.', 1000 / 1333),
            ('8x8-what-not-to-say-poster-pdf', 'Poster: what to say and what not to say to a friend who shares they have been assaulted', 1000 / 838)]
    gh = ''.join(f'<button type="button"{" class=oh-still" if n.startswith("screen-shot") else ""} style="--ar:{ar:.4f}" data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c, ar in wall)
    tips = ''.join(f'<li>{HASH}<span>{t}</span></li>' for t in TIPS)
    ask = ['What are some other ways you might be able to step in? Why does it matter?', 'How could you show support to the survivor? If you were in their place, what would you want others to do?', 'Now that you’ve seen and talked about how online harassment impacts survivors, would you be more likely to intervene if you saw it happening?']
    body = f'''
<section class="oh-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap oh-hero__g">
    <div class="oh-hero__head rise">
      {film_crumbs('Online Harassment of Survivors')}
      <p class="oh-kicker"><span class="oh-tiles" role="img" aria-label="#QuitThisSh*t"><span>#</span><span>Qu<i>i</i>t</span><span>Th<i>i</i>s</span><span>Sh*t</span></span><span class="eyebrow">Two films + a teaching guide</span></p>
      <h1 class="oh-title" aria-label="End online harassment of survivors"><span aria-hidden="true"><span class="mk">End</span> onl<i>i</i>ne</span><span aria-hidden="true">harassment</span><span aria-hidden="true">of surv<i>i</i>vors</span></h1>
    </div>
    <figure class="oh-hero__pic" data-gallery><button class="oh-print" type="button" data-src="{imgsrc('qts-full-cast-copy-2')}" data-cap="#QuitThisShit cast">{img('qts-full-cast-copy-2', 'The cast of #QuitThisSh*t, made by SafeBAE youth leaders', loading='eager')}</button><span class="sticker">Made by SafeBAE youth leaders</span></figure>
    <div class="oh-hero__act"><div class="btns">{btn('Watch the films', '#films', 'mint', arrow=True)}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
      <p class="oh-hero__note">This guide helps peers understand that impact, recognize how harmful language re-victimizes survivors, and practice responses that affirm and protect them.</p></div>
    <div class="oh-hero__txt"><p class="lede">Many survivors describe online harassment and disbelief as being as harmful as the assault itself, or more. Rumors, victim-blaming and shaming at school and on social media are hard to escape and can cause long-lasting trauma, including suicidal ideation.</p></div>
  </div>
</section>

<section class="oh-band oh-band--alt" id="thread">
  <div class="wrap">
    <div class="oh-head"><p class="eyebrow">Rewrite the thread</p><h2>Report it, then reach out.</h2></div>
    <div class="oh-g">
      <div class="oh-thread" aria-label="Example comment thread">
        <div class="oh-post"><span aria-hidden="true">{daisy()}</span><div><b>A survivor posted about what happened to them.</b><p>These are the replies that came next. Report each one and post what a friend would say instead.</p></div></div>
        {cm}
        <div class="oh-thread__foot"><span id="ohcount" aria-live="polite">0 of 5 replies rewritten</span><span class="oh-meter" aria-hidden="true"><i id="ohmeter"></i></span></div>
      </div>
      <div class="oh-side">
        <p>After reporting a harmful post, reach out to the survivor directly, in person or with a supportive message. Let them know you believe them, that they don’t deserve what’s happening, and that you have their back.</p>
        <p>It may be tempting to argue with the person doing the harassing, but that can escalate things or bring unwanted attention back to the survivor. Talk to the survivor first and follow their lead.</p>
        <div class="oh-ask"><b class="oh-label">Ask the group</b><p>Hateful posts can spread quickly, yet people are often hesitant to reach out or show support. Why do you think that is? How can we change this?</p></div>
        <div class="oh-say"><b class="oh-label">What a friend would say</b><div class="oh-say__c"><span>Thank you for telling me.</span><span>You didn’t deserve that.</span><span>I’m here for you.</span><span>It’s not your fault.</span><span>Let me know how I can support.</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="oh-band" id="films">
  <div class="wrap">
    <div class="oh-head"><p class="eyebrow">Two non-explicit, one explicit</p><h2>Choose the right version for your room.</h2></div>
    <div data-tabs="oh"><div class="oh-tabs" role="tablist" aria-label="Films">{vt}</div>{''.join(vp)}</div>
  </div>
</section>

<section class="oh-band oh-band--alt">
  <div class="wrap">
    <div class="oh-head"><p class="eyebrow">Tips to share with students</p><h2>Ways you can step in</h2></div>
    <div class="oh-g">
      <div class="oh-col">
        <ul class="oh-tips">{tips}</ul>
        <div><b class="oh-label">Ask the group</b><ul class="oh-qs">{''.join(f'<li>{esc(q)}</li>' for q in ask)}</ul></div>
      </div>
      <div class="oh-col">
        <div class="oh-you"><h3>If it’s happening to you</h3><p>Report the harmful posts, comments or accounts to the platform. Take screenshots in case you want to share them with school officials or law enforcement later. Avoid replying, since it can escalate things; block the people involved instead. It may help to take a break from social media. Remind yourself: what’s being spread is not true, and it reflects on the harasser, not you.</p></div>
        <div class="oh-you"><h3>Don’t face it alone</h3><p>Reach out to a close friend, a school counselor, a therapist, a trusted family member or an advocate in your community. School officials are mandated reporters, so depending on what you share they may need to inform parents or administrators. If you’re unsure what that looks like at your school, ask about the reporting process.</p><div class="btns"><button class="btn btn--white btn--sm" type="button" data-open-help>All hotlines</button></div></div>
      </div>
    </div>
  </div>
</section>

{teach_tail('online-harassment', 'oh-band', ['knowb4unude', 'dating', 'red-flags'], 'oh-band oh-band--alt',
  lede='Set group agreements first. These conversations can surface strong emotions and may lead to disclosures of abuse.',
  items=[('Explain why it matters', 'Introduce the purpose of the discussion, then set group agreements around trust, respect and privacy.'), ('No names', 'When sharing experiences about others, students should leave out names and identifying details.'), ('Name the options', 'The videos may bring up strong emotions. Let students know they can take a break, talk with a counselor, or contact anonymous resources like loveisrespect.org, and share your mandated reporting protocols.')],
  posters=('From the campaign', f'<div class="oh-wall" data-gallery>{gh}</div>'))}
'''
    js = r'''<script>
(function(){
  var cs = document.querySelectorAll('.oh-cmt'), n = 0, cnt = document.getElementById('ohcount'), m = document.getElementById('ohmeter');
  cs.forEach(function(c){ var b = c.querySelector('button'); b.addEventListener('click', function(){ if(c.classList.contains('fixed')) return; c.classList.add('fixed'); b.textContent = 'Reported'; b.disabled = true; n++; cnt.textContent = n + ' of ' + cs.length + ' replies rewritten' + (n === cs.length ? '. That’s what support looks like.' : ''); m.style.width = (n / cs.length * 100) + '%'; }); });
  document.querySelectorAll('[data-cw]').forEach(function(w){ w.querySelector('[data-reveal]').addEventListener('click', function(){ var t = w.querySelector('template'); var frag = t.content.cloneNode(true); w.replaceWith(frag); }); });
})();
</script>'''
    film_page('film-online-harassment-of-survivors.html', 'Ending Online Harassment of Survivors', 'SafeBAE’s films and teaching guide on the online harassment and re-victimization of teen sexual assault survivors.', body, 'oh', 'family=Special+Elite', CSS, js)
