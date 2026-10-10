from films_common import *

CSS = '''
.film--men{--st:'Saira Stencil One',sans-serif; --m-bg:#13303a; --f-card:#0e252d; --f-line:rgba(255,255,255,.1); --f-ink:#fff; --f-ink2:rgba(255,255,255,.8); --f-acc:var(--mint); --f-acc-ink:var(--slate); --f-lab:var(--mint); --f-disp:var(--st); --f-dw:400; --f-dt:uppercase; --f-dl:.04em; --f-ds:100%}
.film--men main{background:var(--m-bg); color:#fff}
.mn-hero{position:relative; overflow:hidden; min-height:min(720px, 86vh); display:flex; align-items:flex-end}
.mn-hero__img{position:absolute; inset:0}
.mn-hero__img img{width:100%; height:100%; object-fit:cover; object-position:70% 30%; filter:grayscale(.35) contrast(1.05)}
.mn-hero__img::after{content:""; position:absolute; inset:0; background:linear-gradient(90deg, var(--m-bg) 8%, rgba(19,48,58,.82) 42%, rgba(19,48,58,.1) 80%), linear-gradient(0deg, var(--m-bg), transparent 40%)}
.mn-hero .wrap{position:relative; z-index:2; padding-block:clamp(56px,8vw,110px); width:100%}
.mn-hero .wm-daisy{z-index:1}
.mn-hero .crumbs{color:rgba(255,255,255,.7)}
.mn-title{font-family:var(--st); font-weight:400; font-size:clamp(3rem,8.6vw,8rem); line-height:.9; letter-spacing:.06em; text-transform:uppercase; margin:0 0 .3em; max-width:9ch}
.mn-title .mk{padding:0}
.mn-hero .lede{color:rgba(255,255,255,.92); max-width:min(780px,64%)}
@media (max-width:760px){.mn-hero__img::after{background:linear-gradient(0deg, var(--m-bg) 35%, rgba(19,48,58,.78))} .mn-hero .lede{max-width:none}}
.mn-band{padding-block:var(--band)}
.mn-band--alt{background:#0e252d}
.mn-band--mint{background:var(--mint); color:var(--slate)}
.mn-band h2{font-family:var(--st); font-weight:400; font-size:clamp(2rem,4.6vw,3.8rem); letter-spacing:.04em; text-transform:uppercase; line-height:1}
.mn-band .eyebrow{color:var(--mint)} .mn-band--mint .eyebrow{color:var(--slate)}
.big16{display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(20px,4vw,56px); align-items:center}
.big16 b{font-family:var(--st); font-weight:400; font-size:clamp(6rem,18vw,15rem); line-height:.8; letter-spacing:.02em}
.big16 p{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(1.4rem,2.8vw,2.4rem); line-height:1.15; margin:0}
@media (max-width:700px){.big16{grid-template-columns:1fr}}
.mmyth{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.mmyth .flip{min-height:220px}
.film--men .flip__face--front{background:#0e252d; border:2px solid rgba(21,255,200,.35)}
.film--men .flip__face--back{background:var(--mint)}
@media (max-width:960px){.mmyth{grid-template-columns:1fr 1fr}} @media (max-width:560px){.mmyth{grid-template-columns:1fr}}
.rules{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px}
.rules > div{background:#0e252d; border-radius:var(--r-xl); padding:22px; border:1px solid rgba(255,255,255,.1); display:flex; flex-direction:column}
.rules h3{font-family:var(--st); font-weight:400; letter-spacing:.04em; text-transform:uppercase; font-size:1.3rem; color:var(--mint)}
.rules ul{list-style:none; padding:0; margin:0; display:grid; gap:8px; flex:1; grid-auto-rows:1fr}
.rules li{position:relative; display:flex; align-items:center; font-family:var(--display); font-stretch:108%; font-weight:800; font-size:clamp(1.1rem,2vw,1.5rem); line-height:1.15; padding:10px 12px; border-radius:8px; background:rgba(255,255,255,.04); transition:color .4s; margin:0}
.rules li em{font-style:normal; background:linear-gradient(var(--coral),var(--coral)) no-repeat 0 60%/0 4px; -webkit-box-decoration-break:clone; box-decoration-break:clone; transition:background-size .45s var(--ease)}
.rules.challenged li{color:rgba(255,255,255,.45)}
.rules.challenged li em{background-size:100% 4px}
.rules.challenged > div:nth-child(1) li:nth-child(2) em{transition-delay:.12s} .rules.challenged > div:nth-child(1) li:nth-child(3) em{transition-delay:.24s} .rules.challenged > div:nth-child(1) li:nth-child(4) em{transition-delay:.36s} .rules.challenged > div:nth-child(1) li:nth-child(5) em{transition-delay:.48s}
.rules.challenged > div:nth-child(2) li:nth-child(1) em{transition-delay:.6s} .rules.challenged > div:nth-child(2) li:nth-child(2) em{transition-delay:.72s} .rules.challenged > div:nth-child(2) li:nth-child(3) em{transition-delay:.84s}
.mn-disc{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:start}
.mn-disc > div:first-child{position:sticky; top:110px}
@media (max-width:860px){.mn-disc{grid-template-columns:minmax(0,1fr)} .mn-disc > div:first-child{position:static}}
.rules-after{display:none; margin-top:16px; padding:18px 20px; border-radius:14px; background:var(--mint); color:var(--slate); font-weight:700}
.challenged-wrap .rules-after{display:block}
@media (max-width:760px){.rules{grid-template-columns:1fr}}
.defs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.defs div{border-top:4px solid var(--mint); padding-top:14px}
.defs h3{font-family:var(--st); font-weight:400; letter-spacing:.04em; text-transform:uppercase; font-size:1.25rem}
.defs p{margin:0; color:rgba(255,255,255,.85); font-size:.95rem}
@media (max-width:960px){.defs{grid-template-columns:1fr 1fr}} @media (max-width:560px){.defs{grid-template-columns:1fr}}
.respond{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px}
.respond > :last-child{grid-column:span 2}
.respond div{background:#fff; color:var(--slate); border-radius:14px; padding:16px}
.respond b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.05rem; margin-bottom:6px}
.respond p{margin:0; font-size:.88rem; color:var(--ink-soft)}
@media (max-width:1100px){.respond{grid-template-columns:repeat(4,minmax(0,1fr))}} @media (max-width:700px){.respond{grid-template-columns:1fr 1fr}}
.idstats{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.idstats div{background:#0e252d; border-radius:16px; padding:20px; border:1px solid rgba(255,255,255,.1)}
.idstats b{display:block; font-family:var(--st); font-weight:400; font-size:clamp(2.2rem,4vw,3.4rem); color:var(--mint); line-height:1; letter-spacing:.02em}
.idstats p{margin:10px 0 0; font-size:.93rem; color:rgba(255,255,255,.85)}
@media (max-width:960px){.idstats{grid-template-columns:1fr 1fr}}
.film--men .before{--b-bg:#0e252d; --b-line:rgba(255,255,255,.1)}
.film--men .prompts{--p-bg:#0e252d}
'''

MYTHS = [('Men are too strong to be assaulted.', 'Strength does not prevent sexual violence. At least one in six men will experience sexual abuse or assault.'),
         ('Only gay men commit sexual violence.', 'Sexual violence is about power and control, not sexual orientation. Survivors and perpetrators can be of any gender or identity.'),
         ('Men always want sex and welcome all sexual advances.', 'Sexual assault is never wanted. It is a traumatic experience for any survivor, regardless of gender.'),
         ('Men abused by women “got lucky.”', 'Sexual violence is never a privilege. Women can and do sexually abuse or assault boys and men. Survivors are not “lucky”; they are harmed and exploited.')]

def build():
    myths = ''.join(f'<button class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag" style="color:var(--aqua)">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span><span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{esc(f)}</span><span class="hint">Tap to flip back</span></span></span></button>' for m, f in MYTHS)
    resp = [('Believe them', 'Take their words seriously. Doubt can cause deep harm.'), ('Listen', 'Let them share at their own pace. Don’t push for details.'), ('Don’t dismiss it', 'Avoid minimizing or questioning their feelings, especially because of gender.'), ('Allow their emotions', 'Give space for anger, fear, sadness or relief.'), ('Don’t pressure them to report', 'Whether to report is their choice.'), ('Review options together', 'Share resources, and let them decide what feels right.'), ('Keep showing up', 'Check in, stay present, and keep connecting them with help when they’re ready.')]
    rh = ''.join(f'<div><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in resp)
    body = f'''
<section class="mn-hero fhero fhero--dark">
  <div class="mn-hero__img">{img('safebae-14', '', loading='eager')}</div><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap"><div class="rise">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>Supporting Male Survivors</span></nav>
    <p class="eyebrow" style="color:var(--mint)">Theo’s story &middot; testimony + teaching guide</p>
    <h1 class="mn-title">Sexual assault <span class="mk">of men</span></h1>
    <p class="lede">Survivor and SafeBAE Board Member Theo Hutt shares his story, challenging the stigma and myths that keep male survivors silent. The guide helps educators unpack masculinity norms, explore barriers to healing, and build classroom dialogue that validates survivors of all genders.</p>
    <div class="btns">{btn('Watch Theo’s story', 'https://www.youtube.com/watch?v=J50PuImLUV4', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
  </div></div>
</section>

<section class="mn-band mn-band--mint">
  <div class="wrap big16"><b>1 in 6</b><p>At least one in six men will experience sexual abuse or assault. Ending sexual violence requires the active engagement of all genders.</p></div>
</section>

<section class="mn-band">
  <div class="wrap mn-disc">
    <div><p class="eyebrow">After the film</p><h2>Discuss</h2>{yt('J50PuImLUV4', 'Male Survivors of Sexual Assault: Theo’s Story', label='Watch')}</div>
    <div>{prompts(['What are your initial thoughts or feelings after watching the video?', 'Can you think of examples in the media where victims were not believed because of their gender?', 'Which cultural norms or stereotypes fuel the belief that men cannot be victims of sexual violence? For example, the idea that men are always open to sex, or that they can always defend themselves.', 'How can we work together to reduce stigma and increase support for male survivors?', 'How might race, sexuality, gender identity or disability shape men’s experiences of sexual violence and disclosure?'])}</div>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <h2>Myth or fact?</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">People of all genders can be vulnerable to sexual violence. People of all genders can perpetrate it. And not all men commit assault.</p>
    <div class="mmyth">{myths}</div>
  </div>
</section>

<section class="mn-band" id="rules">
  <div class="wrap">
    <p class="eyebrow">Toxic masculinity</p><h2>The rules boys are taught</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">Toxic masculinity is the set of rigid expectations about how men are “supposed” to behave. These norms discourage vulnerability and empathy and promote control, dominance and aggression. Some of them, like entitlement to sex, directly contribute to sexual violence.</p>
    <div class="rwrap">
      <div class="rules">
        <div><h3>Young men are often taught not to</h3><ul><li><span><em>Be vulnerable or ask for help</em></span></li><li><span><em>Show emotions or “weakness”</em></span></li><li><span><em>Be too kind or gentle</em></span></li><li><span><em>Lose, give up control, or take “no” for an answer</em></span></li><li><span><em>Speak out against friends or teammates</em></span></li></ul></div>
        <div><h3>Instead, they’re pressured to</h3><ul><li><span><em>Always be dominating</em></span></li><li><span><em>Always appear powerful</em></span></li><li><span><em>Always act aggressively</em></span></li></ul></div>
      </div>
      <div class="btns" style="margin-top:18px"><button class="btn btn--mint" type="button" id="challenge" aria-pressed="false">Challenge these rules</button></div>
      <p class="rules-after">These expectations are harmful for everyone. Challenging them means making space for all genders to express vulnerability, ask for help, and build healthy, respectful relationships. Ask students: how do these messages show up in your school, media or sports culture?</p>
    </div>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <p class="eyebrow">What is sexual violence?</p><h2>Know the terms</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">At its core, sexual violence is the use of power and control to harm, exploit and oppress.</p>
    <div class="defs"><div><h3>Sexual harassment</h3><p>Unwelcome sexual advances, requests for sexual favors, or verbal or physical harassment of a sexual nature, often in schools or workplaces.</p></div><div><h3>Sexual assault</h3><p>Any sexual contact or behavior that happens without the clear, voluntary consent of everyone involved.</p></div><div><h3>Rape</h3><p>Legally defined with variations across states, often as sexual penetration without consent.</p></div><div><h3>Sexual abuse</h3><p>Sexual contact a person experiences or is made to perform through force, threats, fear or deception, or when legal consent can’t be given. Often used for adult-to-child victimization.</p></div></div>
  </div>
</section>

<section class="mn-band">
  <div class="wrap">
    <p class="eyebrow">If a friend tells you they’ve been assaulted</p><h2>Your role: listen, believe, offer care.</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">The first person a survivor talks to can shape their healing. Your role isn’t to investigate or judge.</p>
    <div class="respond">{rh}</div>
  </div>
</section>

<section class="mn-band mn-band--alt">
  <div class="wrap">
    <p class="eyebrow">Different identities &amp; sexual violence</p><h2>Not every man’s experience is the same</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">Men of color, transgender men and queer men experience higher rates of victimization and often face added stigma when seeking support.</p>
    <div class="idstats"><div><b>4&times;</b><p>Transgender people experience sexual victimization more than four times as often as cisgender people (86.2 vs. 21.7 per 1,000 in 2017–2018).</p></div><div><b>12%</b><p>of Black men reported being survivors of sexual violence in a 2010 study, compared to 7.5% of white men.</p></div><div><b>~4&times;</b><p>LGBT people are nearly four times more likely to experience violent victimization than non-LGBT people.</p></div><div><b>Higher</b><p>Individuals with disabilities are at significantly higher risk of sexual victimization than people without disabilities.</p></div></div>
    <p class="small" style="margin-top:14px;color:rgba(255,255,255,.7)">Ask: how might identity affect whether someone feels safe to come forward? We encourage extending these conversations beyond health class, into advisory, literature, history and other spaces.</p>
  </div>
</section>

{begin('mn-band', 'These conversations can surface strong emotions and may lead to disclosures of abuse.')}
{tail('male-survivors', ['dating', 'rape-culture', 'rrcr'], 'mn-band mn-band--alt')}
'''
    js = r'''<script>
(function(){ var b = document.getElementById('challenge'), w = document.querySelector('.rwrap'), r = document.querySelector('.rules'); if(!b) return; b.addEventListener('click', function(){ var on = !r.classList.contains('challenged'); r.classList.toggle('challenged', on); w.classList.toggle('challenged-wrap', on); b.textContent = on ? 'Show the rules again' : 'Challenge these rules'; b.setAttribute('aria-pressed', String(on)); }); })();
</script>'''
    film_page('film-sexual-assault-of-men.html', 'Supporting Male Survivors', 'Theo Hutt’s story and SafeBAE’s teaching guide on the sexual assault of men, masculinity norms, and supporting survivors of all genders.', body, 'men', 'family=Saira+Stencil+One', CSS, js)
