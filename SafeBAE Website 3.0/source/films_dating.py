from films_common import *

CSS = '''
/* Intimacy & Dating After Sexual Assault: round, soft and unhurried. Nunito in lowercase, aqua and white, circles in place of corners. */
.film--date{--soft:#e8fbfc; --round:'Nunito',var(--body); --f-card:#fff; --f-line:var(--line); --f-ink:var(--slate); --f-ink2:var(--ink-soft); --f-acc:var(--teal); --f-acc-ink:#fff; --f-lab:var(--logo-teal); --f-r:28px; --f-disp:var(--round); --f-dw:800; --f-ds:100%}
.film--date main{background:var(--soft); color:var(--slate)}
.film--date h1,.film--date h2,.film--date h3{font-family:var(--round); font-weight:800; font-stretch:100%; letter-spacing:-.01em}

/* hero: the title runs the full width, the film sits level with the text under it */
.dt-hero{position:relative; overflow:hidden; background:var(--aqua); --wm-o:.24}
.dt-orb{position:absolute; z-index:0; border-radius:50%; pointer-events:none}
.dt-orb--1{width:clamp(300px,42vw,600px); aspect-ratio:1; right:-7%; top:-36%; background:#fff; opacity:.6}
.dt-hero .wm-daisy{right:-9%; top:-30%; bottom:auto; width:min(50vw,640px)}
.dt-hero__g{display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); grid-template-areas:"head head" "txt vid"; gap:clamp(24px,2.8vw,40px) clamp(28px,4vw,56px); padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,84px)}
.dt-hero__head{grid-area:head; min-width:0}
.dt-hero__txt{grid-area:txt; min-width:0; display:flex; flex-direction:column; align-items:flex-start}
.dt-hero__vid{grid-area:vid; min-width:0; display:flex}
.dt-hero .crumbs{color:var(--ink-soft)} .dt-hero .crumbs a{color:var(--logo-teal)}
.dt-hero .eyebrow{margin-bottom:.9rem}
.dt-title{font-size:clamp(2.8rem,6.6vw,6rem); line-height:1; text-transform:lowercase; color:var(--logo-teal); margin:0; text-wrap:balance}
.dt-title .mk{padding:0 .04em}
.dt-hero .lede{margin:0 0 1.3em; font-size:clamp(1.08rem,1.34vw,1.22rem); line-height:1.6}
.dt-hero__note{margin:auto 0 0; padding-top:18px; font-size:.95rem; line-height:1.55; color:var(--ink-soft)}
.dt-hero__txt .btns{gap:10px}
.dt-hero__txt .btn{padding-inline:.95em; font-size:.95rem; white-space:nowrap}
/* the film still keeps 16:9 at least and grows to the height of the text beside it */
.dt-vid{aspect-ratio:auto; display:grid; width:100%; border-radius:32px; box-shadow:0 40px 80px -44px rgba(29,65,78,.65)}
.dt-vid::before{content:""; grid-area:1/1; padding-top:56.25%}
.dt-vid img{position:absolute; inset:0; object-position:50% 22%}
/* a close-up: the play button sits beside her face, not on it */
.dt-vid .vid__play{place-items:center end; padding:0 clamp(22px,7%,54px) 44px 0}
.dt-vid .vid__label > span{text-wrap:balance}
@media (min-width:701px){ .dt-title > span{display:block} }

/* bands */
.dt-band{padding-block:var(--band)}
.dt-band--white{background:#fff}
.dt-band h2{font-size:clamp(2rem,4vw,3.4rem); line-height:1.04; color:var(--logo-teal); margin:0}
.dt-band .eyebrow{color:var(--logo-teal)}

/* healing is not a straight line: the line that wanders, and three slow breaths */
.dt-heal{display:grid; grid-template-columns:minmax(0,7fr) minmax(0,5fr); gap:clamp(28px,4vw,56px); align-items:center}
.dt-heal .lede{margin:.9em 0 0}
.dt-wander{position:relative; display:inline-block; white-space:nowrap; isolation:isolate}
.dt-wander svg{position:absolute; left:-.06em; right:-.04em; bottom:-.26em; width:calc(100% + .1em); height:.62em; z-index:-1; overflow:visible; clip-path:inset(-70% -2% -30% -2%); transition:clip-path 1.7s var(--ease)}
.dt-wander path{fill:none; stroke:var(--mint); stroke-width:.16em; stroke-linecap:round; stroke-linejoin:round}
.dt-wander.pre svg{clip-path:inset(-70% 102% -30% -2%)}
.dt-breath{display:flex; flex-direction:column; align-items:center; gap:18px; min-width:0}
.dt-breath__orb{position:relative; width:min(300px,72vw); aspect-ratio:1; border-radius:50%; border:0; padding:0; background:none; cursor:pointer; display:grid; place-items:center; font:inherit; color:var(--logo-teal); -webkit-tap-highlight-color:transparent}
.dt-breath__orb::before{content:""; position:absolute; inset:0; border-radius:50%; border:2px dashed rgba(19,132,143,.45); transition:border-color .3s}
.dt-breath__orb:hover::before{border-color:var(--teal)}
.dt-breath__orb:focus-visible{outline:3px solid var(--teal); outline-offset:6px; border-radius:50%}
.dt-breath__disc{position:absolute; inset:0; border-radius:50%; background:var(--aqua); box-shadow:inset 0 0 0 10px #fff, inset 0 0 0 12px rgba(19,132,143,.22); transform:scale(.66); transition:transform .7s var(--ease)}
.dt-breath[data-state="in"] .dt-breath__disc{transform:scale(1); transition:transform 4.5s cubic-bezier(.45,0,.55,1)}
.dt-breath[data-state="hold"] .dt-breath__disc{transform:scale(1)}
.dt-breath[data-state="out"] .dt-breath__disc{transform:scale(.66); transition:transform 4.5s cubic-bezier(.45,0,.55,1)}
.dt-breath__in{position:relative; display:flex; flex-direction:column; align-items:center; gap:10px}
.dt-breath__word{font-family:var(--round); font-weight:800; font-size:1.4rem; line-height:1.1; text-transform:lowercase}
.dt-breath__dots{display:flex; gap:7px}
.dt-breath__dots i{width:9px; height:9px; border-radius:50%; background:rgba(29,90,102,.22); transition:background .4s}
.dt-breath__dots i.on{background:var(--teal)}
.dt-breath__hint{margin:0; font-size:.95rem; line-height:1.5; font-weight:600; color:var(--ink-soft); text-align:center}
@media (prefers-reduced-motion:reduce){ .dt-breath__disc{transform:scale(.82)!important} }

/* guidance: one switch, two sets of cards */
.dt-ghead{display:flex; align-items:end; justify-content:space-between; gap:18px 40px; flex-wrap:wrap; margin-bottom:var(--head-gap)}
.dt-ghead h2{flex:1 1 520px; min-width:0}
.persp{display:inline-flex; flex:none; background:#fff; border:1px solid var(--line); border-radius:999px; padding:6px; box-shadow:var(--shadow-soft)}
.persp button{font:inherit; font-family:var(--round); font-weight:800; font-size:1.05rem; line-height:1.1; min-height:48px; border:0; background:transparent; color:var(--logo-teal); padding:12px 24px; border-radius:999px; cursor:pointer; transition:background .25s, color .25s}
.persp button:hover:not([aria-selected="true"]){background:var(--aqua)}
.persp button[aria-selected="true"]{background:var(--teal); color:#fff}
.gcards{display:grid; grid-template-columns:repeat(24,minmax(0,1fr)); gap:var(--gap); align-items:stretch}
.gcard{grid-column:span 12; display:flex; flex-direction:column; min-width:0; background:#fff; border:1px solid var(--line); border-radius:28px; padding:var(--pad-card)}
/* survivors: the longer card takes the wider cell so each row ends level; the second row mirrors the first */
.gcards--s .gcard:nth-child(1), .gcards--s .gcard:nth-child(4){grid-column:span 14}
.gcards--s .gcard:nth-child(2), .gcards--s .gcard:nth-child(3){grid-column:span 10}
.gcard h3{font-size:1.4rem; line-height:1.2; color:var(--logo-teal); margin:0 0 .7em}
.gcard ul{list-style:none; margin:0; padding:0; display:grid; gap:.7em}
.gcard li{position:relative; margin:0; padding-left:1.55em; font-size:1rem; line-height:1.6}
.gcard li::before{content:""; position:absolute; left:.1em; top:.56em; width:.5em; height:.5em; border-radius:50%; background:var(--mint); box-shadow:0 0 0 2px var(--teal)}
.gcard p{margin:0; font-size:1rem; line-height:1.6}
.gcard--soft{background:var(--aqua); border-color:transparent}
.practices{display:flex; flex-wrap:wrap; gap:10px; margin:18px 0 20px}
.practices span{background:#fff; border-radius:999px; padding:9px 16px; font-family:var(--round); font-weight:800; font-size:.98rem; line-height:1.2; color:var(--logo-teal)}
.dt-tat{margin-top:auto!important; padding-top:16px; border-top:1px solid rgba(29,65,78,.2); font-size:.95rem!important}
.dt-tat a{white-space:nowrap}

/* reflect together: heading beside the film still, six prompts in an even grid under them */
.dt-reflect__top{display:grid; grid-template-columns:minmax(0,8fr) minmax(0,4fr); gap:clamp(28px,4vw,56px); align-items:center; margin-bottom:var(--head-gap)}
.dt-reflect__top h2{margin-bottom:.4em}
.dt-reflect__top .lede{margin:0}
.dt-still{margin:0; border-radius:24px; overflow:hidden; aspect-ratio:600/338; background:#33486b; box-shadow:var(--shadow-soft)}
.dt-still img{width:100%; height:100%; object-fit:cover}
.film--date .prompts{--p-bg:var(--soft); --p-line:transparent}
.dt-reflect .prompts{grid-template-columns:repeat(2,minmax(0,1fr)); grid-auto-rows:1fr; gap:12px var(--gap)}
.dt-reflect .prompts li{display:grid; grid-template-columns:38px minmax(0,1fr); gap:16px; align-items:center; padding:16px 22px 16px 16px; border-radius:22px; font-size:1.02rem; line-height:1.45}
.dt-reflect .prompts li::before{content:"?"; width:38px; height:38px; border-radius:50%; display:grid; place-items:center; background:#fff; color:var(--teal); font-family:var(--round); font-weight:800; font-size:1.2rem; line-height:1}

/* show up for survivors: five lines, set large */
.dt-show{position:relative; overflow:hidden; background:var(--teal); color:#fff}
.dt-show > .wrap{position:relative; z-index:1}
.dt-show h2{color:#fff; margin-bottom:var(--head-gap)}
.dt-show .daisy-art{position:absolute; z-index:0; right:-7%; top:50%; width:min(52vw,700px); color:var(--aqua); opacity:.2; transform:translateY(-46%)}
.dt-show__list{list-style:none; margin:0; padding:0; border-bottom:1px solid rgba(255,255,255,.34)}
.dt-show__list li{margin:0; display:grid; grid-template-columns:34px minmax(0,1fr); gap:18px; align-items:center; padding:17px 0; border-top:1px solid rgba(255,255,255,.34); font-family:var(--round); font-weight:800; font-size:clamp(1.12rem,1.75vw,1.45rem); line-height:1.3}
.dt-show__list .daisy{width:34px; height:34px; color:var(--mint)}

/* posters, hung as posters */
.dt-posters{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--gap)}
.dt-posters button{border:0; padding:0; background:var(--soft); border-radius:var(--r-xl); overflow:hidden; cursor:zoom-in; aspect-ratio:3/4; box-shadow:var(--shadow-soft); transition:transform .3s var(--ease), box-shadow .3s}
.dt-posters button:hover{transform:translateY(-5px); box-shadow:0 30px 54px -30px rgba(22,53,64,.6)}
.dt-posters button:focus-visible{outline:3px solid var(--teal); outline-offset:4px}
.dt-posters img{width:100%; height:100%; object-fit:cover}
.film--date .fbegin .lede{color:var(--ink-soft)}
.dt-hero :focus-visible, .dt-band:not(.dt-show) :focus-visible{outline-color:var(--teal)}

@media (max-width:1279px){
  .gcards--s .gcard:nth-child(1), .gcards--s .gcard:nth-child(4){grid-column:span 13}
  .gcards--s .gcard:nth-child(2), .gcards--s .gcard:nth-child(3){grid-column:span 11}
}
@media (max-width:1180px){
  .dt-hero__g{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
}
@media (max-width:900px){
  .dt-hero__g{grid-template-columns:minmax(0,1fr); grid-template-areas:"head" "vid" "txt"}
  .dt-hero__note{margin-top:0}
  .dt-heal{grid-template-columns:minmax(0,1fr)}
  .dt-reflect__top{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
  .dt-show .daisy-art{right:-30%; width:92vw; opacity:.14}
}
@media (max-width:760px){
  .gcards{grid-template-columns:minmax(0,1fr)} .gcards .gcard:nth-child(n){grid-column:auto}
  .dt-reflect .prompts{grid-template-columns:minmax(0,1fr); grid-auto-rows:auto}
  .dt-posters{grid-template-columns:repeat(2,minmax(0,1fr))}
  .dt-ghead{align-items:flex-start}
  .persp{width:100%} .persp button{flex:1; padding-inline:10px}
  .dt-vid{border-radius:24px}
  .dt-vid .vid__label small{display:none}
  .dt-vid .vid__label{font-size:.95rem; padding:10px 16px 11px}
  .dt-vid .vid__play{padding-bottom:56px} .dt-vid .vid__play span{width:64px; height:64px}
  .dt-show__list li{grid-template-columns:28px minmax(0,1fr); gap:14px; align-items:start} .dt-show__list .daisy{width:28px; height:28px; margin-top:.05em}
}
@media (max-width:560px){
  .dt-reflect__top{grid-template-columns:minmax(0,1fr)}
}
'''

SURV = [
 ('Be aware of self-care and self-harm', ['Some survivors may feel drawn to new partners who are also unhealthy or abusive. Try to notice if patterns of unsafe or harmful relationships are developing.', 'Sometimes survivors mirror harmful behaviors as a way of coping. If you notice this in yourself, reach out to a trusted friend, counselor or therapist.', 'Avoiding trauma is common, but it can lead to risky behaviors such as alcohol or drug use, withdrawing from supportive relationships, or unsafe sexual encounters. Be gentle with yourself and reach out for professional help if you notice these patterns.', 'If you are still in contact with the person who harmed you, know that you deserve safety. Lean on trusted people who can help you stay safe.', 'Ask close friends or family to tell you honestly if they notice signs of risk-taking or unhealthy relationship patterns.']),
 ('Acknowledge how you’re feeling', ['Feelings of shame are common after assault, but it is never the survivor’s fault. Unlearning self-blame can take time; committing to self-care and healing helps.', 'Communicate openly with new partners and ask for patience and understanding as you heal.', 'If and when you feel ready, you may choose to share some of your story with your partner. You never have to go into detail or disclose anything you aren’t comfortable sharing.', 'Take as much time as you need to feel physically and emotionally safe with someone again. If anyone pressures you into intimacy, that is not a healthy partner.']),
 ('Setting and protecting boundaries', ['Pay close attention to how people, places and situations affect you. If something feels uncomfortable, frightening or uneasy, honor that response.', 'Once you know the boundaries you need, share them clearly. You never need to justify a boundary.', 'If someone doesn’t respect your boundaries, they are not respecting you.', 'It is often easier to start with stricter boundaries and relax them over time if you feel safe.']),
]
PART = [
 ('Be patient and understanding', ['Your partner’s emotions may sometimes feel overwhelming or hard to understand. Many of these reactions are linked to trauma or PTSD. Be patient, and encourage professional support if they want help managing triggers.']),
 ('Communicate openly', ['Talk with your partner about what helps them feel safe and supported.', 'Ask how you can show up for them in daily life and in your relationship.']),
 ('Practice active consent', ['Always make sure your partner feels completely comfortable before any sexual activity.', 'Don’t rely only on a verbal “yes.” Pay attention to body language, facial expressions and tone of voice.', 'If there’s any doubt, stop and check in. Consent must be ongoing, enthusiastic and free from pressure.']),
 ('If they seem far away', ['If your partner seems distant, distracted or “checked out” during intimacy, they may be dissociating, a common trauma response. Stop immediately.', 'Gently check in and offer comfort through conversation, grounding, or simply being present.', 'Only continue physical intimacy on another day, when they feel ready, able and fully present.']),
 ('Notice patterns, and take care of you too', ['Be aware if your partner is struggling with unhealthy coping that may harm themselves or others, and encourage them to seek help.', 'You deserve kindness and patience too. Supporting your partner does not mean accepting harmful treatment.']),
 ('Affirm their worth', ['Remind your partner they are not defined by their assault. Affirm their strengths, their healing, and who they are beyond trauma.', 'Encourage their healing and, if they want, join supportive activities with them. Never pressure them; if they aren’t comfortable with something you suggest, let it go.']),
]

# a pen line that starts out straight, loops back on itself, dips and carries on
WANDER = ('<svg viewBox="0 0 300 40" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path vector-effect="non-scaling-stroke" '
          'd="M4 26C36 24 66 25 96 23C124 21 147 -11 129 -14C108 -17 103 33 141 29C172 26 190 15 212 21C236 27 262 24 296 20"/></svg>')

def cards(lst, kind, extra=''):
    out = [f'<div class="gcard"><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in items)}</ul></div>' for t, items in lst]
    return f'<div class="gcards gcards--{kind} reveal">' + ''.join(out) + extra + '</div>'

def build():
    posters = [('healing-from-trauma-3', 'Healing from trauma'), ('everyone-can-do-something-1', 'No one can do everything but everyone can do something'), ('relationships-4', 'What goes into a healthy relationship'), ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships')]
    ph = ''.join(f'<button type="button" data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, "Poster: " + c)}</button>' for n, c in posters)
    helps = ['Remind survivors that the assault was not their fault.', 'Encourage their healing and, if they’re comfortable, help them find supportive resources.', 'Respect their privacy. Don’t press them to share before they’re ready.', 'Never suggest doubt, blame or judgment about their experience.', 'Show solidarity: if you hear victim-blaming, slut-shaming or rape jokes, speak up.']
    reconnect = f'''<div class="gcard gcard--soft"><h3>Reconnecting with yourself</h3><p>Try practices that help you feel grounded and present in your body. Some therapists specialize in trauma and may recommend approaches such as EMDR (Eye Movement Desensitization and Reprocessing). Learn more at {a('emdria.org', 'https://www.emdria.org', 'link')}.</p><div class="practices"><span>Mindfulness</span><span>Journaling</span><span>Going for walks</span><span>Yoga, Tai Chi or Qigong</span><span>Making art</span><span>A therapist or peer support group</span></div><p class="dt-tat">Tattoos are one path some survivors take to reclaim their bodies. SafeBAE co-founder Daisy Coleman was a tattoo artist. {a('Tattoos &amp; Healing', 'fordaisy-tattoos.html', 'link')}</p></div>'''
    hh = ''.join(f'<li><span class="daisy" aria-hidden="true"></span><span>{esc(h)}</span></li>' for h in helps)
    body = f'''
<section class="dt-hero fhero fhero--light">
  <span class="dt-orb dt-orb--1" aria-hidden="true"></span><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap dt-hero__g">
    <div class="dt-hero__head rise">
      {film_crumbs('Intimacy & Dating After Sexual Assault')}
      <p class="eyebrow">Made with Teen Vogue &middot; film + teaching guide</p>
      <h1 class="dt-title"><span>intimacy &amp; dating</span> <span><span class="mk">after</span> sexual assault</span></h1>
    </div>
    <div class="dt-hero__txt">
      <p class="lede">Relationships and intimacy after assault can bring new challenges. Survivors may face triggers that complicate dating, and partners may feel unsure how to help. This film and guide affirm that healing looks different for everyone, and offer concrete tools for navigating intimacy with care and consent.</p>
      <div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=rIxB8vlmAjY', 'teal')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
      <p class="dt-hero__note">SafeBAE co-founder Ella Fairon and Henry O’Neal talk about intimacy after sexual assault.</p>
    </div>
    <div class="dt-hero__vid" id="film">{yt('rIxB8vlmAjY', 'Ella Fairon & Henry O’Neal on intimacy after sexual assault', thumb='dating-still-ella', cls='dt-vid', label='With Teen Vogue')}</div>
  </div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap dt-heal">
    <div>
      <h2>Healing is not <span class="dt-wander">a straight line.{WANDER}</span></h2>
      <p class="lede">Many survivors live with post-traumatic stress, and intimacy may sometimes be triggering. Every survivor’s experience is unique. Some days will feel easier than others. What matters is staying committed to healing, surrounding yourself with supportive people, and continuing to communicate needs and boundaries.</p>
    </div>
    <div class="dt-breath" data-breath data-state="idle">
      <button class="dt-breath__orb" type="button" aria-pressed="false" aria-describedby="dt-breath-hint"><span class="dt-breath__disc" aria-hidden="true"></span><span class="dt-breath__in"><span class="dt-breath__word" aria-live="polite">take a breath</span><span class="dt-breath__dots" aria-hidden="true"><i></i><i></i><i></i></span></span></button>
      <p class="dt-breath__hint" id="dt-breath-hint">Press the circle for three slow breaths.</p>
    </div>
  </div>
</section>

<section class="dt-band" id="guidance">
  <div class="wrap">
    <div data-tabs="dating">
      <div class="dt-ghead"><h2>Guidance for survivors, and for partners.</h2>
        <div class="persp" role="tablist" aria-label="Choose a perspective"><button role="tab" id="pt-s" aria-controls="pp-s" aria-selected="true">For survivors</button><button role="tab" id="pt-p" aria-controls="pp-p" aria-selected="false" tabindex="-1">For partners</button></div></div>
      <div role="tabpanel" id="pp-s" aria-labelledby="pt-s">{cards(SURV, 's', extra=reconnect)}</div>
      <div role="tabpanel" id="pp-p" aria-labelledby="pt-p" hidden>{cards(PART, 'p')}</div>
    </div>
  </div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap dt-reflect">
    <div class="dt-reflect__top">
      <div><p class="eyebrow">After the film</p><h2>Reflect together.</h2><p class="lede">Each person is responsible for their own healing. Partners can play a supportive role, but they aren’t substitutes for trained professionals.</p></div>
      <figure class="dt-still">{img('dating-after-sexual-assault-2', 'Ella Fairon and Henry O’Neal sit facing each other across a small table in the film Dating After Sexual Assault, by SafeBAE and Teen Vogue')}</figure>
    </div>
    {prompts(['What are some of the ways Henry supports Ella in feeling more comfortable and working through her triggers?', 'How might these approaches inform how you support a partner or friend who has experienced trauma?', 'What are some specific ways, big or small, you could show support for a partner or any survivor?', 'What are some verbal and physical signs that your partner is comfortable in a situation? What are signs they might not be?', 'How can you balance supporting a survivor while also taking care of your own emotional health?', 'What might be some healthy ways to check in with yourself?'])}
  </div>
</section>

<section class="dt-band dt-show">
  <span class="daisy-art" aria-hidden="true"></span>
  <div class="wrap"><h2>Show up for survivors.</h2><ul class="dt-show__list reveal">{hh}</ul></div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap"><div class="section-head"><div><p class="eyebrow">Shareable graphics</p><h2>Posters for healing.</h2></div><div class="section-head__act">{btn('Download all posters (.zip)', POSTERS_ZIP, 'teal')}</div></div><div class="dt-posters reveal" data-gallery>{ph}</div></div>
</section>
{begin('dt-band', 'These conversations can surface strong emotions and may lead to disclosures of abuse.')}
{tail('dating', ['knowb4unude', 'rape-culture', 'male-survivors'], 'dt-band dt-band--white')}
'''
    js = r'''<script>
(function(){
  var d = document, reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* the line under "a straight line" draws itself once, when the heading comes into view */
  var w = d.querySelector('.dt-wander');
  if(w && 'IntersectionObserver' in window && !reduce && w.getBoundingClientRect().top > window.innerHeight){
    w.classList.add('pre');
    var io = new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ w.classList.remove('pre'); io.disconnect(); } }); }, {rootMargin:'0px 0px -12% 0px'});
    io.observe(w);
  }
  /* three slow breaths: in for 4.5 seconds, hold for 1, out for 4.5, then rest */
  var box = d.querySelector('[data-breath]'); if(!box) return;
  var orb = box.querySelector('.dt-breath__orb'), word = box.querySelector('.dt-breath__word'), hint = box.querySelector('.dt-breath__hint'),
      dots = [].slice.call(box.querySelectorAll('.dt-breath__dots i')), timers = [], running = false, IN = 4500, HOLD = 1000, OUT = 4500;
  function clear(){ timers.forEach(clearTimeout); timers = []; }
  function at(ms, fn){ timers.push(setTimeout(fn, ms)); }
  function set(state, text){ box.setAttribute('data-state', state); word.textContent = text; }
  function rest(done){ clear(); running = false; orb.setAttribute('aria-pressed', 'false'); set('idle', 'take a breath'); if(!done) dots.forEach(function(i){ i.classList.remove('on'); }); hint.textContent = done ? 'Three slow breaths. Press the circle to go again.' : 'Press the circle for three slow breaths.'; }
  function breath(n){
    if(n >= dots.length){ rest(true); return; }
    hint.textContent = 'Breath ' + (n + 1) + ' of ' + dots.length + '. Press the circle to stop.';
    set('in', 'breathe in');
    at(IN, function(){ set('hold', 'hold'); });
    at(IN + HOLD, function(){ set('out', 'breathe out'); });
    at(IN + HOLD + OUT, function(){ dots[n].classList.add('on'); timers = []; breath(n + 1); });
  }
  orb.addEventListener('click', function(){ if(running){ rest(false); return; } running = true; orb.setAttribute('aria-pressed', 'true'); dots.forEach(function(i){ i.classList.remove('on'); }); breath(0); });
})();
</script>'''
    film_page('film-dating-after-sexual-assault.html', 'Intimacy & Dating After Sexual Assault', 'A SafeBAE film made with Teen Vogue and a teaching guide on intimacy, dating and healing after sexual assault, for survivors and partners.', body, 'date', 'family=Nunito:wght@600;800', CSS, js)
