from films_common import *
import math

CSS = '''
.film--rc{--slab:'Zilla Slab',Georgia,serif; --f-card:#fff; --f-line:var(--line); --f-ink:var(--slate); --f-ink2:var(--ink-soft); --f-acc:var(--teal); --f-acc-ink:#fff; --f-lab:var(--logo-teal); --f-disp:var(--slab); --f-dw:700; --f-ds:100%}
.film--rc main{background:#fff; color:var(--slate)}
.film--rc h1,.film--rc h2,.film--rc h3{font-family:var(--slab); font-weight:700; font-stretch:100%; letter-spacing:-.01em}
.rc-hero{background:var(--teal); color:#fff}
.rc-hero .wrap{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(24px,5vw,64px); align-items:center; padding-block:clamp(48px,7vw,96px)}
.rc-hero{background:var(--logo-teal)} .rc-hero .crumbs{color:rgba(255,255,255,.85)} .rc-hero .eyebrow{color:var(--mint)}
.rc-title{font-size:clamp(3rem,7.4vw,7rem); line-height:.92; margin:0 0 .3em}
.rc-title .x{position:relative; color:var(--aqua); text-decoration:line-through; text-decoration-color:var(--coral); text-decoration-thickness:.12em; text-decoration-skip-ink:none}

@keyframes strike{from{transform:scaleX(0)} to{transform:scaleX(1)}}
.rc-title .to{display:block; font-size:.52em; line-height:1.05; margin-top:.25em; color:#fff}
.rc-title .mk{padding:0}
.rc-hero .lede{color:rgba(255,255,255,.92)}
.rc-band{padding-block:var(--band)}
.rc-band--aqua{background:var(--aqua)}
.rc-band--slate{background:var(--slate); color:#fff}
.rc-band h2{font-size:clamp(2.1rem,4.6vw,3.8rem); line-height:1}
.rc-band .eyebrow{color:var(--logo-teal)} .rc-band--slate .eyebrow{color:var(--mint)}
.define{font-family:var(--slab); font-weight:700; font-size:clamp(1.6rem,3.4vw,2.9rem); line-height:1.18; margin:0}
.define mark{background:none; color:inherit; text-decoration:underline; text-decoration-color:var(--teal); text-decoration-thickness:.1em; text-underline-offset:.14em; text-decoration-skip-ink:none}
.elem{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,60px); align-items:center}
.orbit{position:relative; width:min(520px,100%); aspect-ratio:1; margin-inline:auto}
.orbit__c{position:absolute; inset:32%; border-radius:50%; background:var(--slate); color:#fff; display:grid; place-items:center; text-align:center; font-family:var(--slab); font-weight:700; font-size:clamp(1rem,2vw,1.4rem); line-height:1.1; padding:10px}
.orbit button{position:absolute; width:27%; aspect-ratio:1; margin:-13.5% 0 0 -13.5%; border-radius:50%; border:3px solid var(--teal); background:#fff; color:var(--slate); font:inherit; font-family:var(--slab); font-weight:700; font-size:clamp(.82rem,1.5vw,1.05rem); line-height:1.1; cursor:pointer; padding:8px; transition:transform .25s, background .25s}
.orbit button:hover{transform:scale(1.06)}
.orbit button[aria-pressed="true"]{background:var(--logo-teal); border-color:var(--logo-teal); color:#fff; transform:scale(1.1); box-shadow:0 14px 30px -14px rgba(29,65,78,.7)}
.orbit line{transition:stroke-width .3s, stroke-dasharray .3s}
.orbit line.on{stroke:#1d5a66; stroke-width:1.1; stroke-dasharray:none}
.orbit-wrap{min-width:0}
.rc-ch{margin:16px 0 0; padding:14px 16px; border-radius:14px; background:var(--mist); border:1px solid var(--line); font-size:.95rem}
.rc-ch b{display:block; font-family:var(--slab); font-size:1.1rem}
.orbit svg{position:absolute; inset:0; width:100%; height:100%}
.epanel{background:#fff; border:1px solid var(--line); box-shadow:var(--shadow-soft); border-radius:var(--r-xl); padding:clamp(20px,3vw,34px); min-height:340px}
.epanel h3{font-size:clamp(1.6rem,2.6vw,2.2rem)}
.epanel ul{padding-left:1.1em; margin:0 0 1em}
.epanel .q{font-weight:700; border-left:4px solid var(--teal); padding-left:12px; margin-top:16px}
@media (max-width:900px){.elem,.rc-hero .wrap{grid-template-columns:1fr}}
.mf{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px}
.mf .flip{min-height:200px}
.film--rc .flip__face--front{background:var(--slate)}
.film--rc .flip__face--back{background:var(--mint)}
.film--rc .flip__txt{font-family:var(--slab); font-weight:700; font-size:1.25rem}
@media (max-width:760px){.mf{grid-template-columns:1fr}}
.wall{display:flex; flex-wrap:wrap; gap:10px}
.wall button{font:inherit; font-family:var(--slab); font-weight:700; font-size:clamp(1.05rem,1.8vw,1.5rem); padding:10px 16px; border-radius:6px; border:2px solid rgba(255,255,255,.3); background:transparent; color:#fff; cursor:pointer; position:relative}
.wall button:hover{border-color:var(--coral)}
.wall button[aria-pressed="true"]{color:rgba(255,255,255,.45); text-decoration:line-through; text-decoration-color:var(--coral); text-decoration-thickness:4px; border-color:var(--coral)}
.pledge{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px}
.pl{display:grid; grid-template-columns:34px 1fr; gap:12px; align-items:start; padding:16px; border-radius:14px; border:2px solid var(--line); cursor:pointer; background:#fff}
.pl input{appearance:none; -webkit-appearance:none; width:30px; height:30px; border-radius:8px; border:2px solid var(--teal); margin:0; cursor:pointer; display:grid; place-items:center}
.pl input:checked{background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' stroke='%231d414e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/18px no-repeat; border-color:var(--mint)}
.pl b{display:block; font-family:var(--slab); font-size:1.15rem}
.pl span{font-size:.93rem; color:var(--ink-soft)}
.pl:has(input:checked){border-color:var(--mint); background:#effffa}
@media (max-width:760px){.pledge{grid-template-columns:1fr}}
.film--rc .prompts{--p-bg:#fff; --p-line:var(--line)}
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

CH = '<p class="rc-ch"><b>Choking Hazard</b>SafeBAE’s campaign on sexual strangulation, which young people call “choking”. There’s no safe way to choke someone. The campaign has the evidence, myth vs. fact, and free warning posters. ' + a('See the campaign', 'choking-hazard.html', 'link') + '</p>'

def build():
    n = len(ELEMS)
    pos = []
    for i in range(n):
        ang = math.radians(-90 + i * 360 / n)
        pos.append((50 + 36 * math.cos(ang), 50 + 36 * math.sin(ang)))
    lines = ''.join(f'<line{" class=on" if i == 0 else ""} data-l="{i}" x1="50" y1="50" x2="{x:.1f}" y2="{y:.1f}" stroke="#13848f" stroke-width=".5" stroke-dasharray="1.5 1.5"/>' for i, (x, y) in enumerate(pos))
    nodes = ''.join(f'<button style="left:{x:.1f}%;top:{y:.1f}%" aria-pressed="{str(i==0).lower()}" data-e="{i}">{esc(t)}</button>' for i, ((t, *_r), (x, y)) in enumerate(zip(ELEMS, pos)))
    panels = ''.join(f'<div class="epanel" data-ep="{i}"{"" if i==0 else " hidden"}><p class="eyebrow">Element {i+1} of {n}</p><h3>{esc(t)}</h3><p>{esc(d)}</p><ul>{"".join(f"<li>{esc(x)}</li>" for x in pts)}</ul>{"<p>" + a("Explore Race, Rape Culture, and Resistance", "film-race-rape-culture-resistance.html", "link") + "</p>" if i==5 else ""}{("<p class=\"q\">" + esc(q) + "</p>") if q else ""}{CH if i==1 else ""}</div>' for i, (t, d, pts, q) in enumerate(ELEMS))
    myths = ''.join(f'<button class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag" style="color:var(--aqua)">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span><span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{esc(f)}</span><span class="hint">Tap to flip back</span></span></span></button>' for m, f in MYTHS)
    wall = ''.join(f'<button aria-pressed="false">{esc(w)}</button>' for w in STARTS)
    pledge = ''.join(f'<label class="pl"><input type="checkbox" id="pl-{i}" data-pl="{i}"><span><b>{esc(t)}</b><span>{esc(d)}</span></span></label>' for i, (t, d) in enumerate(PLEDGE))
    body = f'''
<section class="rc-hero fhero fhero--dark"><span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="library.html">Library</a><span>/</span><span>Rape Culture</span></nav>
      <p class="eyebrow" style="color:var(--mint)">With Charlie Coleman &amp; Teen Vogue &middot; film + teaching guide</p>
      <h1 class="rc-title"><span class="x">Rape culture</span><span class="to">&amp; how to shift to a <span class="mk">culture of respect</span></span></h1>
      <p class="lede">SafeBAE co-founder Charlie Coleman talks about rape culture and his sister Daisy’s sexual assault, and invites men to examine their role in identifying and interrupting toxic masculinity. The guide gives students concrete steps for challenging harmful norms and building a culture rooted in equity, consent and accountability.</p>
      <div class="btns">{btn('Watch the film', 'https://www.youtube.com/watch?v=FsmycfJPWs4', 'mint')}{btn('Get the teaching guide', '#guide', 'ghost', arrow=True)}</div>
    </div>
    <div>{yt('FsmycfJPWs4', 'Charlie Coleman on Rape Culture & His Sister Daisy’s Assault', label='SafeBAE x Teen Vogue')}</div>
  </div>
</section>

<section class="rc-band">
  <div class="wrap">
    <p class="eyebrow">What is rape culture?</p>
    <p class="define">Rape culture is the values, attitudes, beliefs and everyday behaviors that <mark>make sexual violence seem normal, excusable, or less serious than it is.</mark> When we excuse or ignore harmful behavior, sexual violence becomes more likely to happen and less likely to be challenged.</p>
  </div>
</section>

<section class="rc-band rc-band--aqua">
  <div class="wrap">
    <p class="eyebrow">Where is this behavior learned?</p>
    <h2>Six elements of rape culture</h2>
    <p class="lede">Choose an element to see how it shows up and the question to ask your students.</p>
    <div class="elem">
      <div class="orbit-wrap"><div class="orbit"><svg viewBox="0 0 100 100" aria-hidden="true">{lines}</svg><div class="orbit__c">Elements of rape culture</div>{nodes}</div><p class="small muted" style="text-align:center;margin-top:10px">Diagram credit: RUSSW-VAWC</p></div>
      <div>{panels}</div>
    </div>
  </div>
</section>

<section class="rc-band">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Rape myths &amp; victim blaming</p><h2>Myths vs. facts</h2></div>{btn('More myths & facts', 'myths-facts.html', 'slate', arrow=True)}</div>
    <div class="mf">{myths}</div>
  </div>
</section>

<section class="rc-band rc-band--slate">
  <div class="wrap">
    <h2>Interrupt it.</h2>
    <p class="lede" style="color:rgba(255,255,255,.88)">Rape culture starts with everyday behavior that goes unchallenged. Tap each one you’re ready to call out.</p>
    <div class="wall">{wall}</div>
    <p class="small" id="wallc" style="margin-top:16px;color:var(--mint)" aria-live="polite"></p>
  </div>
</section>

<section class="rc-band">
  <div class="wrap split split--top">
    <div><p class="eyebrow">After the film</p><h2>Discuss</h2><p class="lede">Charlie points out that “no” isn’t the only way to show someone doesn’t consent.</p></div>
    <div>{prompts(['First reactions: what stood out to you in this video? How did it make you feel?', 'Language in your community: have you heard jokes, comments or phrases like the ones Charlie mentioned? How did people respond?', 'Recognizing non-consent: what other signs, verbal or nonverbal, might show someone is uncomfortable or not giving consent?', 'Gender expectations: Charlie talks about standards and pressures for men. How do these expectations affect not only men, but everyone? How might you challenge this kind of talk?'])}</div>
  </div>
</section>

<section class="rc-band rc-band--aqua">
  <div class="wrap">
    <h2>What is one small action you could take this week?</h2>
    <p class="lede">Changing culture starts with everyday choices. Check the ones you’ll commit to. Your choices stay on this device.</p>
    <div class="pledge">{pledge}</div>
  </div>
</section>

{vibe_band('Charlie asks men to look at their own role. Vibe Check is a free, anonymous reflection tool for young people questioning whether they crossed a boundary or caused harm, with guided modules on rape culture and on men and masculinity.', 'Looking at your own behavior?')}
{begin('rc-band', 'These conversations can surface strong emotions and may lead to disclosures of abuse.')}
{tail('rape-culture', ['knowb4unude', 'male-survivors', 'rrcr'], 'rc-band rc-band--aqua')}
'''
    js = r'''<script>
(function(){
  var bs = document.querySelectorAll('.orbit button'), ps = document.querySelectorAll('[data-ep]'), ls = document.querySelectorAll('.orbit line');
  bs.forEach(function(b){ b.addEventListener('click', function(){ bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x===b)); }); ps.forEach(function(p){ p.hidden = p.dataset.ep !== b.dataset.e; }); ls.forEach(function(l){ l.classList.toggle('on', l.dataset.l === b.dataset.e); }); }); });
  var w = document.querySelectorAll('.wall button'), wc = document.getElementById('wallc');
  w.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed', b.getAttribute('aria-pressed')==='true'?'false':'true'); var n = document.querySelectorAll('.wall [aria-pressed="true"]').length; wc.textContent = n ? n + ' of ' + w.length + ' called out' + (n===w.length ? '. That’s a culture of respect.' : '') : ''; }); });
  document.querySelectorAll('[data-pl]').forEach(function(c){ var k = 'sb-pledge-' + c.dataset.pl; try{ c.checked = localStorage.getItem(k)==='1'; }catch(e){} c.addEventListener('change', function(){ try{ localStorage.setItem(k, c.checked?'1':'0'); }catch(e){} }); });
})();
</script>'''
    film_page('film-rape-culture.html', 'Rape Culture & a Culture of Respect', 'SafeBAE’s film with Charlie Coleman and Teen Vogue and a teaching guide on recognizing rape culture and building a culture of respect.', body, 'rc', 'family=Zilla+Slab:wght@600;700', CSS, js)
