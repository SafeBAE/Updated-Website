from films_common import *

CSS = '''
.film--oh{--oh:#0f1a1e; --oh2:#16252b; --dot:'DotGothic16',monospace; --f-card:var(--oh2); --f-line:rgba(255,255,255,.12); --f-ink:#fff; --f-ink2:rgba(255,255,255,.8); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint); --f-disp:var(--dot); --f-dw:400; --f-dt:uppercase; --f-dl:.01em; --f-ds:100%}
.film--oh main{background:var(--oh); color:#fff}
.oh-hero .wrap{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px)}
.oh-win{position:relative; border:3px solid var(--mint); border-radius:6px; background:#0b1417; box-shadow:10px 10px 0 rgba(21,255,200,.18), 0 40px 80px -30px rgba(0,0,0,.8); transform:rotate(1.5deg)}
.oh-win__bar{display:flex; align-items:center; gap:10px; padding:8px 12px; border-bottom:3px solid var(--mint); font-family:var(--dot); font-size:.95rem; color:var(--mint)}
.oh-win__bar i{width:12px; height:12px; border:2px solid var(--mint); border-radius:2px} .oh-win__bar span{flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.oh-win img{display:block; width:100%; aspect-ratio:16/10; object-fit:cover}
.oh-win .sticker{position:absolute; left:-14px; bottom:22px}
@media (max-width:900px){.oh-hero .wrap{grid-template-columns:minmax(0,1fr)} .oh-win{max-width:560px; transform:none} .oh-win .sticker{left:10px}}
.oh-hero .crumbs{color:rgba(255,255,255,.6)}
.oh-title{font-family:var(--dot); font-weight:400; font-size:clamp(2.6rem,5.4vw,5.6rem); line-height:.98; text-transform:uppercase; color:#fff; margin:0 0 .3em; letter-spacing:.01em; text-shadow:0 0 18px rgba(21,255,200,.35)}
.oh-title > span{display:block}
.oh-title .mk{padding:0}
.oh-hero .lede{color:rgba(255,255,255,.88); max-width:none}
.oh-band{padding-block:var(--band)}
.oh-band--alt{background:var(--oh2)}
.oh-band h2{font-family:var(--dot); font-weight:400; font-size:clamp(1.8rem,4vw,3.2rem); text-transform:uppercase; line-height:1.05}
.oh-band .eyebrow{color:var(--mint)}
.thread-wrap{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(24px,4vw,56px); align-items:start}
.thread{background:#fff; color:#14272d; border-radius:var(--r-xl); overflow:hidden; box-shadow:0 40px 80px -40px rgba(0,0,0,.8)}
.thread__post{padding:18px 20px; border-bottom:1px solid #e3eef0}
.thread__post b{display:block}
.thread__post p{margin:6px 0 0; color:#3f5a62}
.cmt{display:grid; grid-template-columns:40px 1fr auto; gap:12px; align-items:start; padding:14px 20px; border-bottom:1px solid #eef5f6; transition:background .4s}
.cmt i{width:40px; height:40px; border-radius:50%; background:#cfdde0; display:grid; place-items:center; font-style:normal; font-weight:800; font-size:.8rem; color:#46646e}
.cmt small{font-weight:700; color:#46646e; font-size:.8rem}
.cmt p{margin:2px 0 0; font-size:1rem}
.cmt .old{display:block}
.cmt .new{display:none; color:#0b6b74; font-weight:700}
.cmt button{font:inherit; font-size:.78rem; font-weight:800; padding:7px 10px; border-radius:8px; border:2px solid var(--slate); background:var(--slate); color:#fff; cursor:pointer; white-space:nowrap}
.cmt button:hover{background:#fff; color:var(--slate)}
.cmt.fixed{background:#eafffa}
.cmt.fixed i{background:var(--mint); color:var(--slate)}
.cmt.fixed .old{text-decoration:line-through; color:#9bb0b5; font-size:.85rem}
.cmt.fixed .new{display:block}
.cmt.fixed button{border-color:var(--mint); color:var(--slate); background:var(--mint); cursor:default}
.cmt.fixed .new{animation:oh-type .5s steps(12) both}
@keyframes oh-type{from{clip-path:inset(0 100% 0 0)} to{clip-path:inset(0 0 0 0)}}
.thread__foot{padding:14px 20px; font-family:var(--mono); font-size:.8rem; color:#46646e; display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap}
.meter{height:8px; background:#e3eef0; border-radius:99px; overflow:hidden; flex:1 1 140px; align-self:center}
.meter i{display:block; height:100%; width:0; background:var(--mint); transition:width .5s}
@media (max-width:900px){.thread-wrap{grid-template-columns:1fr}}
.vtabs{display:flex; flex-wrap:wrap; gap:8px; margin:18px 0}
.vtabs button{font:inherit; font-weight:800; padding:10px 16px; border-radius:10px; border:2px solid rgba(255,255,255,.18); background:transparent; color:#fff; cursor:pointer}
.vtabs button[aria-selected="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.vtabs button .w{font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; text-transform:uppercase; background:var(--coral); color:var(--slate); padding:2px 6px; border-radius:4px; margin-left:6px}
.vpanel{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(20px,4vw,48px); align-items:start}
.cw{position:relative; aspect-ratio:16/9; border-radius:16px; background:#1d2c31; display:grid; place-items:center; text-align:center; padding:24px; border:2px dashed var(--coral)}
.cw p{max-width:46ch; margin:0 auto 14px}
@media (max-width:900px){.vpanel{grid-template-columns:1fr}}
.steps5{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.steps5 div{background:var(--oh2); border:1px solid rgba(255,255,255,.12); border-top:4px solid var(--mint); border-radius:16px; padding:18px; font-weight:600}
.steps5 b{display:block; font-family:var(--dot); font-size:2rem; color:var(--mint); line-height:1; margin-bottom:10px}
@media (max-width:960px){.steps5{grid-template-columns:1fr 1fr} .steps5 > :last-child:nth-child(odd){grid-column:1/-1}}
.say{display:flex; flex-wrap:wrap; gap:10px; margin-top:16px}
.say span{background:var(--mint); color:var(--slate); padding:10px 14px; border-radius:18px 18px 18px 4px; font-weight:800}
.ogallery{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px}
.ogallery button{border:0; padding:0; border-radius:14px; overflow:hidden; cursor:zoom-in; background:#000; aspect-ratio:4/3}
.ogallery img{width:100%; height:100%; object-fit:cover}
.ogallery button:nth-child(2) img{object-fit:contain; background:#0d2a2f}
@media (max-width:760px){.ogallery{grid-template-columns:1fr}}
.film--oh .before{--b-bg:var(--oh2); --b-line:rgba(255,255,255,.12)}
.film--oh .prompts{--p-bg:var(--oh2)}
'''

CMTS = [('Why were you there?', 'It’s not your fault.'), ('Were you drinking?', 'You didn’t deserve that.'), ('What were you wearing?', 'I’m here for you.'),
        ('If it was really a big deal, why didn’t you tell anyone sooner?', 'Thank you for telling me.'), ('It’s going to be fine, just move on.', 'Let me know how I can support you.')]

def build():
    cm = ''.join(f'<div class="cmt"><i>{chr(65+i)}{chr(75+i)}</i><div><small>user_{4821+i*137}</small><p><span class="old">{esc(o)}</span><span class="new">{esc(n)}</span></p></div><button type="button">Report &amp; reply</button></div>' for i, (o, n) in enumerate(CMTS))
    films = [
      ('cy', 'What It’s Like to Be Cyberbullied', False, yt('TTPzlIWqxqE', 'What It’s Like to Be Cyberbullied as a Sexual Assault Survivor', label='SafeBAE x Teen Vogue'), 'The non-explicit short film from SafeBAE’s campaign to break the cycle of online revictimization. Appropriate for all school settings.',
       ['What are your initial thoughts and feelings after watching?', 'Survivors of sexual assault often experience guilt and self-blame. How does victim blaming or online harassment amplify those emotions?', 'The film highlights common victim-blaming phrases. Do you notice this kind of language in your community? How can you push back when you hear it, in person or online?']),
      ('end', 'Help Put an End to It', False, yt('-I4Jmz7Yxys', 'Help put an end to online harassment of teen survivors', label='Non-explicit'), 'A second non-explicit option from the same campaign.',
       ['Before watching, had you thought about the effect a single post, comment or message could have on someone?', 'How might this change the way you act online?', 'Do you know how to report online harassment if it happened to you or a friend?']),
      ('qts', '#QuitThisSh*t', True, None, 'Created by SafeBAE youth leaders in 2016. The script was written entirely from real messages survivors have received, so it is explicit. Many educators find that this authenticity makes it especially powerful, but use your discretion and consider the non-explicit options.',
       ['What are your first thoughts or feelings after watching?', 'Do you know someone who has been harassed online? What was the impact on them? (Don’t share names or identifying details.)', 'Have you heard of something similar happening in your community? Did people gossip about the survivor? Were there consequences for the people responsible?', 'Are you aware of help services or how to report online harassment?']),
    ]
    vt = ''.join(f'<button role="tab" id="vt-{k}" aria-controls="vp-{k}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{esc(t)}{"<span class=w>Explicit</span>" if w else ""}</button>' for i, (k, t, w, *_r) in enumerate(films))
    vp = []
    for i, (k, t, w, media, d, qs) in enumerate(films):
        if w:
            media = f'<div class="cw" data-cw><div><p class="eyebrow" style="color:var(--coral)">Content warning</p><p>This video contains explicit language and real messages survivors received. It may not be appropriate for all school settings.</p><button class="btn btn--coral btn--sm" type="button" data-reveal>Show the video</button></div><template>{yt("UbeoN5zlPGo", "#QuitThisShit", label="Explicit language")}</template></div>'
        vp.append(f'<div class="vpanel" role="tabpanel" id="vp-{k}" aria-labelledby="vt-{k}"{"" if i==0 else " hidden"}><div>{media}</div><div><p style="color:rgba(255,255,255,.85)">{esc(d)}</p><h3 style="font-size:1.15rem;margin-top:18px">Discuss</h3>{prompts(qs)}</div></div>')
    gal = [('qts-full-cast-copy-2', '#QuitThisShit cast'), ('online-harassment-poster-5', 'Poster: No one can do everything, but everyone can do something. End rape culture.'), ('screen-shot-2017-04-18-at-4-07-42-pm', '#QuitThisShit still')]
    gh = ''.join(f'<button data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c in gal)
    body = f'''
<section class="oh-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
   <div class="rise">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>Online Harassment of Survivors</span></nav>
    <p class="eyebrow">Two films + a teaching guide</p>
    <h1 class="oh-title"><span><span class="mk">End</span> online</span><span>harassment</span><span>of survivors</span></h1>
    <p class="lede">Many survivors describe online harassment and disbelief as being as harmful as the assault itself, or more. Rumors, victim-blaming and shaming at school and on social media are hard to escape and can cause long-lasting trauma, including suicidal ideation. This guide helps peers understand that impact, recognize how harmful language re-victimizes survivors, and practice responses that affirm and protect them.</p>
    <div class="btns">{btn('Watch the films', '#films', 'mint', arrow=True)}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
   </div>
   <figure class="oh-win" style="margin:0"><div class="oh-win__bar" aria-hidden="true"><i></i><span>quit_this_sh*t.jpg</span><i></i></div>{img('qts-full-cast-copy-2', 'The cast of #QuitThisSh*t, made by SafeBAE youth leaders', loading='eager')}<span class="sticker">Made by SafeBAE youth leaders</span></figure>
  </div>
</section>

<section class="oh-band oh-band--alt">
  <div class="wrap thread-wrap">
    <div class="thread" aria-label="Example comment thread">
      <div class="thread__post"><b>A survivor posted about what happened to them.</b><p>These are the replies that came next. Report each one and post what a friend would say instead.</p></div>
      {cm}
      <div class="thread__foot"><span id="ohcount">0 of 5 replies rewritten</span><span class="meter"><i id="ohmeter"></i></span></div>
    </div>
    <div>
      <p class="eyebrow">Rewrite the thread</p>
      <h2>Report it, then reach out.</h2>
      <p style="color:rgba(255,255,255,.88)">After reporting a harmful post, reach out to the survivor directly, in person or with a supportive message. Let them know you believe them, that they don’t deserve what’s happening, and that you have their back.</p>
      <p style="color:rgba(255,255,255,.88)">It may be tempting to argue with the person doing the harassing, but that can escalate things or bring unwanted attention back to the survivor. Talk to the survivor first and follow their lead.</p>
      <p class="small" style="color:#fff"><b>Ask the group:</b> Hateful posts can spread quickly, yet people are often hesitant to reach out or show support. Why do you think that is? How can we change this?</p>
      <div class="say"><span>Thank you for telling me.</span><span>You didn’t deserve that.</span><span>I’m here for you.</span><span>It’s not your fault.</span><span>Let me know how I can support.</span></div>
    </div>
  </div>
</section>

<section class="oh-band" id="films">
  <div class="wrap">
    <p class="eyebrow">Two non-explicit, one explicit</p><h2>Choose the right version for your room.</h2>
    <div data-tabs="oh"><div class="vtabs" role="tablist" aria-label="Films">{vt}</div>{''.join(vp)}</div>
  </div>
</section>

<section class="oh-band oh-band--alt">
  <div class="wrap">
    <p class="eyebrow">Tips to share with students</p><h2>Ways you can step in</h2>
    <div class="steps5"><div>Report the harmful post, account or comment to the platform.</div><div>Don’t like, share or repost hurtful messages or images.</div><div>Show support to the survivor, online and in person.</div><div>Report harassment to a trusted adult.</div><div>If you hear gossip, speak up and say it’s not okay.</div></div>
    <div class="grid g2" style="margin-top:22px">
      <div class="before" style="grid-template-columns:1fr"><div><b>If it’s happening to you</b><p>Report the harmful posts, comments or accounts to the platform. Take screenshots in case you want to share them with school officials or law enforcement later. Avoid replying, since it can escalate things; block the people involved instead. It may help to take a break from social media. Remind yourself: what’s being spread is not true, and it reflects on the harasser, not you.</p></div></div>
      <div class="before" style="grid-template-columns:1fr"><div><b>Don’t face it alone</b><p>Reach out to a close friend, a school counselor, a therapist, a trusted family member or an advocate in your community. School officials are mandated reporters, so depending on what you share they may need to inform parents or administrators. If you’re unsure what that looks like at your school, ask about the reporting process.</p></div></div>
    </div>
    <div style="margin-top:22px">{prompts(['What are some other ways you might be able to step in? Why does it matter?', 'How could you show support to the survivor? If you were in their place, what would you want others to do?', 'Now that you’ve seen and talked about how online harassment impacts survivors, would you be more likely to intervene if you saw it happening?'])}</div>
  </div>
</section>

{begin('oh-band', 'Set group agreements first. These conversations can surface strong emotions and may lead to disclosures of abuse.', items=[('Explain why it matters', 'Introduce the purpose of the discussion, then set group agreements around trust, respect and privacy.'), ('No names', 'When sharing experiences about others, students should leave out names and identifying details.'), ('Name the options', 'The videos may bring up strong emotions. Let students know they can take a break, talk with a counselor, or contact anonymous resources like loveisrespect.org, and share your mandated reporting protocols.')])}

<section class="oh-band oh-band--alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Shareable graphics</p><h2>From the campaign</h2></div>{btn('Download all posters (.zip)', POSTERS_ZIP, 'mint')}</div><div class="ogallery" data-gallery>{gh}</div></div></section>
{tail('online-harassment', ['knowb4unude', 'dating', 'red-flags'], 'oh-band')}
'''
    js = r'''<script>
(function(){
  var cs = document.querySelectorAll('.cmt'), n = 0, cnt = document.getElementById('ohcount'), m = document.getElementById('ohmeter');
  cs.forEach(function(c){ var b = c.querySelector('button'); b.addEventListener('click', function(){ if(c.classList.contains('fixed')) return; c.classList.add('fixed'); b.textContent = 'Replied'; n++; cnt.textContent = n + ' of ' + cs.length + ' replies rewritten' + (n===cs.length ? '. That’s what support looks like.' : ''); m.style.width = (n/cs.length*100) + '%'; }); });
  document.querySelectorAll('[data-cw]').forEach(function(w){ w.querySelector('[data-reveal]').addEventListener('click', function(){ var t = w.querySelector('template'); var frag = t.content.cloneNode(true); w.replaceWith(frag); }); });
})();
</script>'''
    film_page('film-online-harassment-of-survivors.html', 'Ending Online Harassment of Survivors', 'SafeBAE’s films and teaching guide on the online harassment and re-victimization of teen sexual assault survivors.', body, 'oh', 'family=DotGothic16', CSS, js)
