from films_common import *

CSS = '''
.film--know{--kb:#0a1519; --kb2:#10232a; --mono-d:'Rubik Mono One',sans-serif}
.film--know main{background:var(--kb); color:#fff}
.kb-hero .wrap{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px)}
.kb-hero .crumbs{color:rgba(255,255,255,.6)}
.kb-title{font-family:var(--mono-d); font-weight:400; font-size:clamp(3rem,8vw,7.4rem); line-height:.9; color:var(--mint); margin:0 0 .3em; letter-spacing:-.02em; display:grid; grid-template-columns:auto 1fr; column-gap:.12em; align-items:center}
.kb-title .hash{grid-row:span 3; font-size:2.6em; line-height:.8; color:var(--mint)}
.kb-title span:not(.hash){display:block}
.kb-hero .lede{color:rgba(255,255,255,.88)}
.kphone{width:min(340px,86vw); margin-inline:auto; border-radius:44px; border:10px solid #000; background:#0e1c21; box-shadow:0 0 0 2px rgba(21,255,200,.25), 0 40px 80px -30px rgba(0,0,0,.9); padding:20px 14px 26px; display:flex; flex-direction:column; gap:10px; min-height:520px}
.kphone__top{display:flex; align-items:center; gap:10px; padding:4px 6px 12px; border-bottom:1px solid rgba(255,255,255,.08)}
.kphone__top i{width:36px; height:36px; border-radius:50%; background:var(--teal); display:grid; place-items:center; font-style:normal; font-weight:800}
.kphone__top b{font-size:.95rem} .kphone__top small{display:block; color:rgba(255,255,255,.55); font-size:.75rem}
.msg{max-width:84%; padding:10px 14px; border-radius:18px; font-size:.95rem; line-height:1.35; opacity:0; transform:translateY(8px); animation:pop .5s forwards}
.msg.in{background:#22363d; border-bottom-left-radius:4px}
.msg.out{background:var(--mint); color:var(--slate); margin-left:auto; border-bottom-right-radius:4px; font-weight:600}
.msg:nth-of-type(1){animation-delay:.3s}.msg:nth-of-type(2){animation-delay:1.1s}.msg:nth-of-type(3){animation-delay:1.9s}.msg:nth-of-type(4){animation-delay:2.7s}.msg:nth-of-type(5){animation-delay:3.5s}
@keyframes pop{to{opacity:1; transform:none}}
@media (prefers-reduced-motion:reduce){.msg{opacity:1; transform:none}}
.typing{display:flex; gap:4px; padding:12px 14px; background:#22363d; border-radius:18px; width:64px}
.typing i{width:7px; height:7px; border-radius:50%; background:rgba(255,255,255,.6); animation:dot 1.2s infinite} .typing i:nth-child(2){animation-delay:.2s} .typing i:nth-child(3){animation-delay:.4s}
@keyframes dot{50%{opacity:.2; transform:translateY(-2px)}}
.kb-band{padding-block:var(--band)}
.kb-band--alt{background:var(--kb2)}
.kb-band h2{font-family:var(--mono-d); font-weight:400; font-size:clamp(1.6rem,3.4vw,2.8rem); line-height:1.08; letter-spacing:-.01em}
.kb-band .eyebrow{color:var(--mint)}
.kb-quote{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.3rem,2.6vw,2.2rem); line-height:1.3; margin:0; color:#fff}
.kb-quote mark{background:none; color:var(--mint)}
.nums{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; margin-top:26px}
.num{background:var(--kb2); border:1px solid rgba(21,255,200,.25); border-radius:18px; padding:22px}
.num b{display:block; font-family:var(--mono-d); font-weight:400; font-size:clamp(2.6rem,6vw,5rem); color:var(--mint); line-height:1}
.num span{display:block; margin-top:8px; font-weight:700; font-size:1.05rem}
.notifs{display:grid; gap:12px; margin-top:22px}
.notif{display:grid; grid-template-columns:44px 1fr; gap:14px; align-items:start; background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.1); border-radius:18px; padding:16px; backdrop-filter:blur(4px)}
.notif i{width:44px; height:44px; border-radius:12px; background:var(--coral); display:grid; place-items:center; font-style:normal; font-weight:900; color:var(--slate)}
.notif small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:rgba(255,255,255,.6)}
.notif p{margin:4px 0 0; font-size:1.02rem}
.notif p b{color:var(--mint)}
@media (max-width:860px){.kb-hero .wrap{grid-template-columns:1fr} .nums{grid-template-columns:1fr}}
.wyd{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(20px,4vw,48px)}
.wyd__tabs{display:grid; gap:10px; align-content:start}
.wyd__tabs button{font:inherit; text-align:left; cursor:pointer; padding:16px 18px; border-radius:16px; border:2px solid rgba(255,255,255,.14); background:transparent; color:#fff; font-weight:700; line-height:1.35}
.wyd__tabs button small{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint); margin-bottom:4px}
.wyd__tabs button[aria-selected="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.wyd__tabs button[aria-selected="true"] small{color:var(--slate)}
.wyd__panel{background:var(--kb2); border-radius:20px; padding:clamp(20px,3vw,32px); border:1px solid rgba(255,255,255,.1)}
.checks{list-style:none; padding:0; margin:0; display:grid; gap:10px}
.checks li{display:grid; grid-template-columns:30px 1fr; gap:10px; align-items:start; font-size:1.05rem; margin:0}
.checks li::before{content:""; width:26px; height:26px; border-radius:8px; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' stroke='%231d414e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
@media (max-width:860px){.wyd{grid-template-columns:1fr}}
.warn{background:var(--coral); color:var(--slate); border-radius:22px; padding:clamp(22px,4vw,44px); display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(20px,4vw,48px)}
.warn .rows{align-content:start} .warn .eyebrow{color:var(--slate)}
.warn h2{font-family:var(--mono-d); font-weight:400; font-size:clamp(1.5rem,3vw,2.4rem)}
.warn .rows{border-color:rgba(29,65,78,.25)} .warn .row{border-color:rgba(29,65,78,.25)} .warn .row:hover{background:rgba(255,255,255,.25)} .warn .row b{color:var(--slate)} .warn .row small{color:var(--slate)} .warn .row .go{background:#fff}
@media (max-width:860px){.warn{grid-template-columns:1fr}}
.ptiles{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.ptiles button{border:0; padding:0; background:#000; cursor:zoom-in; border-radius:14px; overflow:hidden; aspect-ratio:4/5}
.ptiles img{width:100%; height:100%; object-fit:cover; transition:transform .4s}
.ptiles button:hover img{transform:scale(1.04)}
.ptiles button:last-child img{object-fit:contain; padding:10px}
@media (max-width:860px){.ptiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
.film--know .gpanel{--g-bg:var(--kb2)}
.film--know .before{--b-bg:var(--kb2); --b-line:rgba(255,255,255,.1)}
.film--know .card{background:var(--kb2); color:#fff; border-color:rgba(255,255,255,.1)} .film--know .card__body p{color:rgba(255,255,255,.75)}
.film--know .prompts{--p-bg:var(--kb2)}
'''

SCEN = [
 ('Someone you know', 'sends you an unsolicited nude of themselves', ['Let them know this is not okay and ask them not to do it again.', 'Report it to a trusted adult or school official if it continues.', 'Report it on the social media platform, if it was sent online.', 'Block them if necessary.']),
 ('Someone you don’t know', 'sends you a nude by random number, AirDrop, social media or a dating app', ['Report the account to the app or platform if possible.', 'Block them immediately.']),
 ('Someone sends or shows you', 'a nude of another person', ['Tell them clearly that sharing without consent is not okay.', 'If you know the person in the image, let them know what happened.', 'Report it to a trusted adult or school official.', 'Report it on the social media platform, if it was shared online.']),
]

def build():
    tabs = ''.join(f'<button role="tab" id="wy-{i}" aria-controls="wyp-{i}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}"><small>{esc(a_)}</small>{esc(b)}</button>' for i, (a_, b, _s) in enumerate(SCEN))
    panels = ''.join(f'<div class="wyd__panel" role="tabpanel" id="wyp-{i}" aria-labelledby="wy-{i}"{"" if i==0 else " hidden"}><p class="eyebrow">If {esc(a_.lower())} {esc(b)}</p><ul class="checks">{"".join(f"<li>{esc(x)}</li>" for x in st)}</ul><p style="margin-top:18px;color:rgba(255,255,255,.75)">Protect both yourself and the person in the image.</p></div>' for i, (a_, b, st) in enumerate(SCEN))
    posters = [('nudes-poster-2', 'Do you trust the person you send nudes to?'), ('nudes-poster-3', 'Did you know that if a teacher catches you sharing nudes, they’re required to tell the police?'), ('knowb4unude-1', 'Have you ever gotten a nude you didn’t want?'), ('knowb4unude', '#knowB4Unude'), ('untitled-design-2020-02-12t110716-010-3', '#knowB4Unude campaign graphic')]
    ph = ''.join(f'<button data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c in posters)
    qs = ['Did any of the scenes feel familiar or similar to situations you’ve heard about?', 'Have you ever known someone who felt pressured to send a nude? What impact did that have on them?', 'Have you heard of a nude being shared at school without the person’s permission? What happened afterward? Did people gossip or shame the person in the photo?', 'Were there any consequences for the person who shared it without consent?', 'Before watching, did you know that sharing nudes of anyone under 18 is against the law? Does that change how you think about your own choices?', 'If someone were being harassed with nudes at your school, who would be a safe adult you could turn to?']
    body = f'''
<section class="kb-hero">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>#knowB4Unude</span></nav>
      <p class="eyebrow" style="color:var(--aqua)">A public service announcement + teaching guide</p>
      <h1 class="kb-title" aria-label="#knowB4Unude"><span class="hash">#</span><span>Know</span><span>B4U</span><span>Nude</span></h1>
      <p class="lede">Youth explore the pressures, risks and consequences of sending nudes, and push back on the oversimplified “just don’t do it” message adults usually give. Sexting has become a cultural norm, so this PSA and its guide start a non-judgmental conversation about consent, digital safety, image-based harm, and how peers can support each other without shame.</p>
      <div class="btns">{btn('Watch the PSA', 'https://www.youtube.com/watch?v=iNAVcRO22S0', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div class="kphone" aria-label="Example messages">
      <div class="kphone__top"><i>?</i><span><b>Unknown</b><small>now</small></span></div>
      <p class="msg in">hey</p>
      <p class="msg in">Do you trust the person you send nudes to?</p>
      <p class="msg in">Have you ever gotten a nude you didn’t want?</p>
      <p class="msg out">Know the risks before you send.</p>
      <p class="msg in">…</p>
      <span class="typing" aria-hidden="true"><i></i><i></i><i></i></span>
    </div>
  </div>
</section>

<section class="kb-band kb-band--alt">
  <div class="wrap split">
    <div>{yt('iNAVcRO22S0', '#knowB4Unude', thumb='knowb4unude', label='PSA')}</div>
    <div>
      <blockquote class="kb-quote">“Most of the information we get about online communication is ‘just don’t send nudes.’ But this approach is <mark>unrealistic, victim blaming, and doesn’t address the real problem.</mark> We are not here to shame kids for sending nudes. We want to offer them the opportunity to learn about the risks and talk about the pressures that surround sending and forwarding explicit pictures.”</blockquote>
      <span class="cite" style="color:var(--mint)">Molly Gallenberg, SafeBAE Youth Ambassador and #KnowB4Unude Associate Producer</span>
    </div>
  </div>
</section>

<section class="kb-band">
  <div class="wrap">
    <p class="eyebrow">The numbers</p>
    <h2>It’s more common than adults think.</h2>
    <div class="nums"><div class="num"><b data-count="15">15%</b><span>of teens under 18 report that they send nudes</span></div><div class="num"><b data-count="27">27%</b><span>receive them</span></div><div class="num"><b data-count="12">12%</b><span>forward them</span></div></div>
    <p class="small" style="color:rgba(255,255,255,.6);margin-top:10px">JAMA Pediatrics, March 2018</p>
    <div class="notifs">
      <div class="notif"><i>2/3</i><div><small>Sarah Thomas, Northwestern University, February 2019</small><p>An analysis of <b>500 accounts from girls ages 12 to 18</b> about negative experiences sexting found that two-thirds had been asked to provide explicit images, and the requests often progressed from promises of affection to “anger displays, harassment and threats.”</p></div></div>
      <div class="notif"><i>8%</i><div><small>Sarah Thomas, Northwestern University, February 2019</small><p><b>Less than 8% of girls</b> shared explicit pictures because they wanted to. The rest did so out of a desire to please, acquiesce to, or avoid conflict with a boy.</p></div></div>
      <div class="notif"><i>4&times;</i><div><small>Sarah Thomas, Northwestern University, February 2019</small><p>Girls and boys both send nude photos, but <b>boys are nearly four times as likely to pressure girls</b> to do so than the reverse. In relationships it was often normalized with claims like “everyone else has a picture of their girlfriend.”</p></div></div>
    </div>
  </div>
</section>

<section class="kb-band kb-band--alt">
  <div class="wrap split split--top">
    <div><p class="eyebrow">After the PSA</p><h2>Start the conversation.</h2><p class="lede" style="color:rgba(255,255,255,.85)">This guide is not meant to shame or judge people for sending nudes; it’s an opportunity to talk openly about the risks, pressures, and potential outcomes so that everyone can make informed decisions.</p><p style="color:rgba(255,255,255,.8)">Some of the most vulnerable ages for harm related to nudes are in middle school, so encourage older students to share what they learn with younger siblings and through peer mentoring.</p></div>
    <div>{prompts(qs)}</div>
  </div>
</section>

<section class="kb-band">
  <div class="wrap">
    <p class="eyebrow">Possible scenarios</p><h2>What would you do?</h2>
    <div class="wyd" data-tabs="kb"><div class="wyd__tabs" role="tablist" aria-label="Scenarios">{tabs}</div><div>{panels}</div></div>
  </div>
</section>

<section class="kb-band kb-band--alt">
  <div class="wrap">
    <div class="warn">
      <div>
        <p class="eyebrow">Sextortion &amp; online predators</p>
        <h2>If someone you don’t know starts pressuring you online, block them and tell a trusted adult.</h2>
        <p>There has been a sharp increase in adults pretending to be young people on apps, social media and gaming platforms. Their goal is often to pressure teens into sending nudes, then threaten to make the image public unless they send money or more images. This is called sextortion. The stress of these threats has tragically led some young people to take their own lives.</p>
        <p><b>If your nudes are shared without permission, it is never your fault.</b> No one deserves to have their images used against them. School officials are mandated reporters, so they may need to inform parents depending on the situation.</p>
      </div>
      <div class="rows">{row('Talk to someone you trust', 'A close friend, a trusted adult or a school counselor.', 'survivor-support.html')}{row('DM @safe_bae', 'We’ll help you find local services.', 'https://www.instagram.com/safe_bae/')}{row('Take It Down (NCMEC)', 'A free service that helps remove nude images of people under 18 from participating platforms.', 'https://takeitdown.ncmec.org/')}{row('love is respect', 'Text LOVEIS to 22522 or call 1-866-331-9474, 24/7.', 'https://www.loveisrespect.org')}</div>
    </div>
    <div class="grid g2" style="margin-top:22px">
      <div class="side__card" style="background:var(--kb);border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:22px"><h3>State laws</h3><p style="color:rgba(255,255,255,.8)">Intimate-image laws differ from state to state. With your students, look up what the law says in your state and discuss the possible consequences for people who share images without consent, at any age.</p></div>
      <div class="side__card" style="background:var(--kb);border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:22px"><h3>School policies</h3><p style="color:rgba(255,255,255,.8)">Review your district’s student handbook or ask a counselor what the rules are. Every school handles this differently. If yours doesn’t have clear rules, consider advocating with your school board to create them. {a('Reform your school’s policy', 'reform-policy.html', 'link', attrs=' style="color:var(--mint)"')}</p></div>
    </div>
  </div>
</section>

<section class="kb-band"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Campaign posters</p><h2>Share the campaign.</h2></div>{btn('Download all posters (.zip)', POSTERS_ZIP, 'mint')}</div><div class="ptiles" data-gallery>{ph}</div></div></section>
<section class="kb-band kb-band--alt"><div class="wrap"><p class="eyebrow">Before you begin</p><h2>Set up the room.</h2>{before_you_begin()}<div style="margin-top:18px">{help_inline()}</div></div></section>
{guide_panel('knowb4unude')}
<section class="kb-band"><div class="wrap"><p class="eyebrow">Go deeper</p><h2>Teach these next</h2>{related(['rape-culture', 'male-survivors', 'online-harassment'])}</div></section>
'''
    film_page('film-knowb4unude.html', '#knowB4Unude', '#knowB4Unude is SafeBAE’s PSA and teaching guide on the pressures, risks and consequences of sending nudes.', body, 'know', 'family=Rubik+Mono+One', CSS)
