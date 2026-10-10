from films_common import *

CSS = '''
.film--date{--soft:#f3feff; --round:'Nunito',var(--body)}
.film--date main{background:var(--soft); color:var(--slate)}
.film--date h1,.film--date h2,.film--date h3{font-family:var(--round); font-weight:800; font-stretch:100%; letter-spacing:-.01em}
.dt-hero{position:relative; overflow:hidden; background:var(--aqua)}
.dt-hero .wrap{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px); position:relative; z-index:2}
.dt-hero .crumbs{color:var(--ink-soft)} .dt-hero .crumbs a{color:var(--logo-teal)}
.dt-title{font-size:clamp(2.8rem,6.4vw,6rem); line-height:.98; text-transform:lowercase; color:var(--logo-teal); margin:0 0 .35em}
.dt-title em{font-style:normal; color:var(--teal)}
.blob{position:absolute; border-radius:50%; filter:blur(2px); opacity:.55; z-index:1}
.blob--1{width:520px; height:520px; right:-160px; top:-160px; background:radial-gradient(circle, #fff 0%, rgba(255,255,255,0) 70%)}
.blob--2{width:380px; height:380px; left:-120px; bottom:-180px; background:radial-gradient(circle, rgba(21,255,200,.45) 0%, rgba(21,255,200,0) 70%)}
.dt-vid{border-radius:32px; box-shadow:0 40px 80px -40px rgba(29,65,78,.6)}
.dt-band{padding-block:var(--band)}
.dt-band--white{background:#fff}
.dt-band h2{font-size:clamp(2rem,4vw,3.4rem); color:var(--logo-teal)}
.dt-band .eyebrow{color:var(--teal)}
.breathe{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(24px,5vw,72px); align-items:center}
.circle{position:relative; width:min(340px,80vw); aspect-ratio:1; margin-inline:auto; display:grid; place-items:center}
.circle::before{content:""; position:absolute; inset:0; border-radius:50%; background:radial-gradient(circle at 40% 35%, #fff, var(--aqua) 55%, #9ef3f0); box-shadow:0 30px 60px -30px rgba(19,132,143,.6); animation:breathe 10s ease-in-out infinite}
.circle span{position:relative; font-family:var(--round); font-weight:800; font-size:1.3rem; color:var(--logo-teal)}
@keyframes breathe{0%,100%{transform:scale(.78)} 45%,55%{transform:scale(1)}}
@media (prefers-reduced-motion:reduce){.circle::before{animation:none}}
.persp{display:inline-flex; background:#fff; border-radius:999px; padding:6px; box-shadow:0 10px 30px -15px rgba(29,65,78,.4); margin:20px 0 28px}
.persp button{font:inherit; font-family:var(--round); font-weight:800; font-size:1.05rem; border:0; background:transparent; color:var(--logo-teal); padding:12px 22px; border-radius:999px; cursor:pointer}
.persp button[aria-selected="true"]{background:var(--teal); color:#fff}
.gcards{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; align-items:stretch}
.gcards .gcard{margin:0; display:block; width:100%; min-width:0}
.gcard{background:#fff; border-radius:28px; padding:clamp(20px,3vw,30px); box-shadow:0 20px 40px -30px rgba(29,65,78,.5)}
.gcard h3{font-size:1.4rem; color:var(--teal)}
.gcard ul{margin:0; padding-left:1.1em} .gcard li{margin:.45em 0}
.gcard--wide{grid-column:1/-1; background:var(--teal); color:#fff} .gcard--wide h3{color:var(--mint)}
@media (max-width:860px){.dt-hero .wrap,.breathe{grid-template-columns:1fr} .gcards{grid-template-columns:minmax(0,1fr)}}
.practices{display:flex; flex-wrap:wrap; gap:10px; margin-top:18px}
.practices span{background:#fff; border-radius:999px; padding:10px 16px; font-weight:700; color:var(--logo-teal); box-shadow:0 8px 20px -14px rgba(29,65,78,.6)}
.helps{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.helps div{background:var(--aqua); border-radius:24px; padding:20px; font-weight:700; color:var(--logo-teal); line-height:1.4}
.helps .daisy{display:block; width:30px; height:30px; color:var(--teal); margin-bottom:10px}
@media (max-width:960px){.helps{grid-template-columns:1fr 1fr} .helps > :last-child:nth-child(odd){grid-column:1/-1}}
.dposters{display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px}
.dposters button{border:0; padding:10px; background:#fff; border-radius:22px; cursor:zoom-in; aspect-ratio:3/4; display:grid; place-items:center; box-shadow:0 14px 30px -20px rgba(29,65,78,.6)}
.dposters img{max-height:100%; width:auto; object-fit:contain; border-radius:12px}
@media (max-width:860px){.dposters{grid-template-columns:repeat(2,minmax(0,1fr))}}
.film--date .gpanel{--g-bg:var(--logo-teal)}
.film--date .card{border-radius:24px}
.film--date .prompts{--p-bg:#fff; --p-line:var(--line)}
.film--date .before{--b-bg:#fff}
.film--date .gform{background:rgba(255,255,255,.1)}
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

def cards(lst, wide_last=False):
    out = []
    for i, (t, items) in enumerate(lst):
        out.append(f'<div class="gcard{" gcard--wide" if wide_last and i == len(lst)-1 else ""}"><h3>{esc(t)}</h3><ul>{"".join(f"<li>{esc(x)}</li>" for x in items)}</ul></div>')
    return '<div class="gcards">' + ''.join(out) + '</div>'

def build():
    posters = [('dating-after-sexual-assault-2', 'Dating after sexual assault'), ('healing-from-trauma-3', 'Healing from trauma'), ('everyone-can-do-something-1', 'No one can do everything but everyone can do something'), ('relationships-4', 'What goes into a healthy relationship'), ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships')]
    ph = ''.join(f'<button data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, c)}</button>' for n, c in posters)
    helps = ['Remind survivors that the assault was not their fault.', 'Encourage their healing and, if they’re comfortable, help them find supportive resources.', 'Respect their privacy. Don’t press them to share before they’re ready.', 'Never suggest doubt, blame or judgment about their experience.', 'Show solidarity: if you hear victim-blaming, slut-shaming or rape jokes, speak up.']
    hh = ''.join(f'<div><span class="daisy" aria-hidden="true"></span>{esc(h)}</div>' for i, h in enumerate(helps))
    body = f'''
<section class="dt-hero">
  <span class="blob blob--1"></span><span class="blob blob--2"></span>
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>Intimacy &amp; Dating After Sexual Assault</span></nav>
      <p class="eyebrow">Made with Teen Vogue &middot; film + teaching guide</p>
      <h1 class="dt-title">intimacy &amp; dating <em>after</em> sexual assault</h1>
      <p class="lede">Relationships and intimacy after assault can bring new challenges. Survivors may face triggers that complicate dating, and partners may feel unsure how to help. This film and guide affirm that healing looks different for everyone, and offer concrete tools for navigating intimacy with care and consent.</p>
      <div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=rIxB8vlmAjY', 'teal')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div>{yt('rIxB8vlmAjY', 'Ella Fairon & Henry O’Neal on intimacy after sexual assault', cls='dt-vid', label='With Teen Vogue')}<p class="small muted" style="margin-top:14px">SafeBAE co-founder Ella Fairon and Henry O’Neal talk about intimacy after sexual assault.</p></div>
  </div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap breathe">
    <div class="circle" aria-hidden="true"><span>breathe</span></div>
    <div>
      <p class="eyebrow">Before you begin</p>
      <h2>Healing is not a straight line.</h2>
      <p class="lede">Many survivors live with post-traumatic stress, and intimacy may sometimes be triggering. Every survivor’s experience is unique. Some days will feel easier than others. What matters is staying committed to healing, surrounding yourself with supportive people, and continuing to communicate needs and boundaries.</p>
    </div>
  </div>
  <div class="wrap" style="margin-top:32px">{before_you_begin()}</div>
</section>

<section class="dt-band" id="guidance">
  <div class="wrap">
    <p class="eyebrow">Two perspectives</p>
    <h2>Guidance for survivors, and for partners.</h2>
    <div data-tabs="dating">
      <div class="persp" role="tablist" aria-label="Choose a perspective"><button role="tab" id="pt-s" aria-controls="pp-s" aria-selected="true">For survivors</button><button role="tab" id="pt-p" aria-controls="pp-p" aria-selected="false" tabindex="-1">For partners</button></div>
      <div role="tabpanel" id="pp-s" aria-labelledby="pt-s">{cards(SURV)}
        <div class="gcard"><h3>Reconnecting with yourself</h3><p>Try practices that help you feel grounded and present in your body. Some therapists specialize in trauma and may recommend approaches such as EMDR (Eye Movement Desensitization and Reprocessing). Learn more at {a('emdria.org', 'https://www.emdria.org', 'link')}.</p><div class="practices"><span>Mindfulness</span><span>Journaling</span><span>Going for walks</span><span>Yoga, Tai Chi or Qigong</span><span>Making art</span><span>A therapist or peer support group</span></div></div>
      </div>
      <div role="tabpanel" id="pp-p" aria-labelledby="pt-p" hidden>{cards(PART)}</div>
    </div>
  </div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap">
    <div class="split split--top">
      <div><p class="eyebrow">After the film</p><h2>Reflect together.</h2><p class="lede">Each person is responsible for their own healing. Partners can play a supportive role, but they aren’t substitutes for trained professionals.</p></div>
      <div>{prompts(['What are some of the ways Henry supports Ella in feeling more comfortable and working through her triggers?', 'How might these approaches inform how you support a partner or friend who has experienced trauma?', 'What are some specific ways, big or small, you could show support for a partner or any survivor?', 'What are some verbal and physical signs that your partner is comfortable in a situation? What are signs they might not be?', 'How can you balance supporting a survivor while also taking care of your own emotional health?', 'What might be some healthy ways to check in with yourself?'])}</div>
    </div>
  </div>
</section>

<section class="dt-band">
  <div class="wrap"><p class="eyebrow">More ways to help</p><h2>Show up for survivors.</h2><div class="helps">{hh}</div></div>
</section>

<section class="dt-band dt-band--white">
  <div class="wrap"><div class="section-head"><div><p class="eyebrow">Shareable graphics</p><h2>Posters for healing.</h2></div>{btn('Download all posters (.zip)', POSTERS_ZIP, 'teal')}</div><div class="dposters" data-gallery>{ph}</div><div style="margin-top:26px">{help_inline()}</div></div>
</section>
{guide_panel('dating')}
<section class="dt-band"><div class="wrap"><p class="eyebrow">Go deeper</p><h2>Teach these next</h2>{related(['knowb4unude', 'rape-culture', 'male-survivors'])}</div></section>
'''
    film_page('film-dating-after-sexual-assault.html', 'Intimacy & Dating After Sexual Assault', 'A SafeBAE film made with Teen Vogue and a teaching guide on intimacy, dating and healing after sexual assault, for survivors and partners.', body, 'date', 'family=Nunito:wght@600;800', CSS)
