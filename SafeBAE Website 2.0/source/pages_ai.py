"""ai-literacy.html: the SafeBAE AI Literacy Training product page.
Sources: the live training at https://ai-literacy.safebae.org (checked 9 Oct 2026: program home,
Preface, module overviews, contents, settings, support, educators page) and research_new_pages.md (B).
Imagery: the training's own illustrations and screenshots of the live training (captured with Playwright)."""
from lib import *
from urllib.parse import quote

TRAIN = 'https://ai-literacy.safebae.org/'
EDU = 'https://ai-literacy.safebae.org/educators.html'
PRIV = 'https://ai-literacy.safebae.org/privacy-policy.html'


def svg_uri(svg):
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/'-.,()") + '")'


def brush(fill, op):
    # the training's double brushstroke (two offset strokes)
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 400' preserveAspectRatio='none'><g fill='{fill}' fill-opacity='{op}'>"
                   "<path d='M90 84Q960 -44 1812 84Q1834 88 1848 118Q1880 190 1891 288Q1893 312 1872 310Q960 230 152 310Q134 311 124 290Q92 205 78 112Q74 87 90 84Z'/>"
                   "<path d='M38 158Q900 32 1766 158Q1788 162 1802 192Q1832 262 1842 360Q1845 384 1822 382Q960 306 103 383Q84 384 74 362Q43 280 28 186Q24 161 38 158Z'/></g></svg>")


def loop(stroke, w=3):
    # a pen loop that overshoots where it starts, like the training's callout loops
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 120' preserveAspectRatio='none'><path d='M34 30C120 6 300 2 368 22C396 30 402 66 384 88C346 116 124 122 42 106C8 98 2 66 16 44C28 24 84 12 156 8' fill='none' stroke='{stroke}' stroke-width='{w}' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")


def wave(stroke):
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 14' preserveAspectRatio='none'><path d='M2 8C20 2 34 2 52 8S84 14 102 8S134 2 152 8S184 14 198 7' fill='none' stroke='{stroke}' stroke-width='2.4' stroke-linecap='round' vector-effect='non-scaling-stroke'/></svg>")


def ring(stroke):
    return svg_uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><path d='M52 6C78 6 95 24 94 50C93 76 74 94 48 93C22 92 6 74 7 49C8 26 26 9 50 8C62 8 70 11 76 15' fill='none' stroke='{stroke}' stroke-width='3.2' stroke-linecap='round'/></svg>")


MODS = [
  dict(k='welcome', n='', label='start here', title='Welcome', time='2 min', screens=1,
       lead='What this program covers, who it is for, and what you will be able to do by the end.',
       desc='The Preface introduces the program, who it is for, and the four things learners will be able to do by the end.',
       explore=[], sections=[],
       img=('ai-shot-welcome', 'shot', 'Screenshot of the training’s Preface screen, “Welcome to the SafeBAE AI Literacy Training”', 'Preface')),
  dict(k='m1', n=1, label='how AI works', title='What Is AI, Really?', time='45 min', screens=11,
       lead='Before we can talk about how AI affects our relationships, our thinking, or our safety, we need to understand what AI actually is and what it isn’t.',
       desc='Traditional AI, machine learning, generative AI, hallucinations, and why privacy matters.',
       explore=['What hallucinations are, and how to check a source yourself.', 'Why AI sounds correct even when it’s wrong.', 'Who can read your AI chats, and what to change.',
                'What an AI agent is, and what changes when AI takes actions.', 'The Four-Step Check, a framework for using AI.'],
       sections=['Different Types of AI', 'How Generative AI Works', 'Training Data and Testing Data', 'Hallucinations', 'When AI Sounds Certain', 'Your Chats Are Records', 'What’s Really Going On?', 'AI Agents', 'The Four-Step Check'],
       img=('ai-illo-gravity', 'illo', 'A crowd looks up in confusion at a big screen that reads “Why gravity isn’t real, by AI,” while a small screen-faced AI figure waves from the crowd.', '1D · Hallucinations')),
  dict(k='m2', n=2, label='feeds and thinking', title='How AI Shapes the Way We Think', time='60 min', screens=9,
       lead='AI doesn’t just regurgitate information, it also shapes how we think.',
       desc='Sycophancy, filter bubbles, emotional attachment, and the Four-Step Check skillset.',
       explore=['How recommendation algorithms work and shape what you see online.', 'What information a feed collects about you, and what it has no way of knowing.', 'Social sycophancy and validation, or why AI tends to agree with you.',
                'Confirmation bias and filter bubbles.', 'Emotional attachment and persuasion.', 'How to recognize online misinformation and manipulation.'],
       sections=['How the Feed Decides What You See', 'Taking Some of It Back', 'Confirmation Bias and Filter Bubbles', 'Social Sycophancy and Validation', 'What Would You Say?', 'Emotional Attachment and Persuasion', 'How AI Changes What You Believe'],
       img=('ai-illo-phone', 'illo', 'A teenager looks down at their phone, shoulders slumped, while a screen-headed AI figure puts an arm around them.', '2F · Emotional Attachment and Persuasion')),
  dict(k='m3', n=3, label='relationships', title='AI and Healthy Relationships', time='45 min', screens=8,
       lead='A chatbot can respond immediately, remember what you have told it and agree with how you feel. It is not in a relationship with you.',
       desc='Simulated vs. genuine connection, AI companions, dependency, and boundaries.',
       explore=['The difference between AI-simulated connection and genuine connection.', 'Emotional attachment to AI companions, and when reliance can become a problem.', 'Why companion apps are designed the way they are, and what laws and safety rules apply to them.',
                'How AI can show up inside real relationships, and why that’s risky.', 'How AI can make you less receptive to boundaries, feedback and differing opinions.', 'What changes when an AI agent reads or sends messages that involve other people.'],
       sections=['AI vs. Genuine Connection', 'AI Companions and Dependency', 'A Pattern Check', 'AI, Boundaries, and Consent in Relationships', 'AI Agents and Other People', 'Your Own Boundaries, in Practice'],
       img=('ai-shot-pattern', 'shot', 'Screenshot of the training: “A Pattern Check,” twelve questions about how you use AI, each answered from Never to Most days', '3C · A Pattern Check')),
  dict(k='m4', n=4, label='using AI well', title='Using AI Responsibly', time='30 min', screens=8,
       lead='AI is a tool, and like any tool, it can be used well or poorly.',
       desc='How to fact-check what AI tells you, set your own boundaries with it, notice overreliance, and know when a question should go to a person.',
       explore=['Critical thinking and fact-checking skills.', 'Healthy boundaries with AI.', 'How to recognize overreliance on AI.', 'Practical strategies for using AI safely and thoughtfully.'],
       sections=['Check It', 'Three Checks, For Real', 'Your Boundaries', 'Write Yours', 'AI or a Person?', 'Where Does This Question Go?'],
       img=('ai-shot-write', 'shot', 'Screenshot of the training: the “My AI Boundaries” personal plan, with prompts for daily and weekly time limits', '4D · Write Yours')),
  dict(k='m5', n=5, label='fake images', title='Nudify Apps and AI-Generated Image Abuse', time='45 min', screens=12,
       lead='This module focuses on one of the ways AI is being used to cause harm: creating sexual images of real people without their consent.',
       desc='What nudification apps are, the harm and the law, real deepfake cases, and how to support someone who has been targeted.',
       explore=['What nudification apps are and how they use AI to create sexualized images.', 'The harms of nonconsensual AI-generated sexual images.', 'The legal consequences of creating or sharing these images.',
                'How to support someone whose image has been used without consent.', 'Practical steps for reporting and removing nonconsensual images.'],
       sections=['Before Any of This', 'One Photo Is Enough', 'Harm and the Law', 'Know Your Rights', 'Real Cases', 'What Usually Happens Instead', 'Getting an Image Removed', 'If It Happens', 'Where to Go'],
       img=('ai-shot-removed', 'shot', 'Screenshot of the training: “Getting an Image Removed,” on free removal tools that work without uploading the image', '5G · Getting an Image Removed')),
  dict(k='m6', n=6, label='sextortion', title='Sextortion and Digital Manipulation', time='45 min', screens=7,
       lead='Sextortion is when someone threatens to share intimate images or information unless a person gives them something they want.',
       desc='What sextortion is, how AI is making it more common and more dangerous, and how to protect yourself and support a friend.',
       explore=['What sextortion is, and who does it.', 'The five stages it usually runs in, and what each one looks like.', 'How AI is making sextortion easier and more dangerous.',
                'The warning signs of sextortion and manipulation.', 'Practical strategies for protecting yourself online.', 'How to support a friend who is going through sextortion.'],
       sections=['What Sextortion Is', 'The Script', 'What AI Changed', 'The Ten-Minute Lockdown', 'If It Is Happening to You or a Friend'],
       img=('ai-shot-script', 'shot', 'Screenshot of the training: “The Script,” the five stages sextortion often follows, from building trust to creating urgency', '6B · The Script')),
  dict(k='end', n='', label='wrap-up', title='Conclusion', time='3 min', screens=1,
       lead='Everything you learned, and where to go next.',
       desc='The certificate is a one-page file you can print or download. It unlocks once you have finished every screen and every activity in the program.',
       explore=['The Four-Step Check: Pause. Question. Check. Ask.', 'Why confident language is not evidence that an answer is right.', 'Why an AI can produce caring language without experiencing care.',
                'When a question depends on another person’s feelings, boundaries or consent, and has to go to that person.', 'What rights you have if an image of you is made or shared, and how to get it removed.', 'The six steps if it happens to you, and what to do if it happens to a friend.'],
       sections=[],
       img=('ai-illo-cards', 'illo', 'A screen-faced AI figure sits at a card table under hanging lamps, holding playing cards, with word cards reading the, on, sat, cat, the laid out in front of it.', '1B · How Generative AI Works')),
]

STEPS4 = [
  ('Pause', 'Don’t accept the answer automatically.', 'Pause means creating a little space between getting an answer and believing or using it. AI can produce an answer instantly. That does not mean you need to accept it instantly.'),
  ('Question', 'What is it claiming? How could you know if it is true?', 'Question means identifying what the AI is actually claiming, and what evidence would support it. Is it giving you a fact? A statistic? An interpretation? A guess about another person? Different claims need different evidence.'),
  ('Check', 'Verify important claims somewhere outside the AI.', 'Check means verifying important information somewhere outside the chatbot. If the AI gives you a citation, check that the source exists and says what the AI claims it says. The more important the answer is, the stronger your checking should be.'),
  ('Ask', 'For anything about your life, ask a person.', 'Ask means recognizing when information alone is not enough. Questions about your health, safety, relationships, school situation, legal rights, or another person’s intentions often depend on context an AI does not have.'),
]

GOALS = [
  'Think critically about AI-generated content, especially on sensitive topics like relationships, consent, and sexual health.',
  'Set healthy boundaries with AI tools and recognize signs of over-reliance.',
  'Understand AI’s limits, including what it can do, what it can’t do, and why it’s not a substitute for real-world connection.',
  'Know when to seek real-world support from trusted adults, friends, and resources.',
]

SUPPORT = [
  ('988 Suicide & Crisis Lifeline', 'Call or text 988', 'Any crisis, any hour. Trained counselors, by phone, text or chat.', 'https://988lifeline.org/'),
  ('Crisis Text Line', 'Text HOME to 741741', 'A trained counselor texts back. No phone call.', 'https://www.crisistextline.org/'),
  ('The Trevor Project', 'Call 1-866-488-7386 or text START to 678-678', 'Counselors trained to work with LGBTQ+ young people.', 'https://www.thetrevorproject.org/get-help/'),
  ('National Sexual Assault Hotline', 'Call 800.656.4673 or text HOPE to 64673', 'Free and confidential. Staff go through your options with you.', 'https://rainn.org/hotline'),
  ('love is respect', 'Call 1-866-331-9474 or text LOVEIS to 22522', 'For a dating relationship that feels controlling or unsafe.', 'https://www.loveisrespect.org/'),
  ('Childhelp National Child Abuse Hotline', 'Call or text 800.422.4453', 'For when the person hurting you is an adult in your life.', 'https://www.childhelphotline.org/'),
  ('Take It Down', 'takeitdown.ncmec.org', 'Free help removing nude or sexual images taken of you before you turned 18, from participating platforms. The image never leaves your phone.', 'https://takeitdown.ncmec.org/'),
]

CONNECT = [
  ('Certified Peer Educator Training', 'A 16-module course on consent, boundaries, bystander intervention, online safety and your Title IX rights. Module 3 points to it for the relationship skills it covers more fully.', 'peer-educator.html', 'preview1', 'Free · 16 modules'),
  ('#knowB4Unude', 'SafeBAE’s PSA on the pressures, risks and consequences of sharing intimate images, with a teaching guide. A natural companion to Modules 5 and 6.', 'film-knowb4unude.html', 'knowb4unude', 'Film + guide'),
  ('Vibe Check', 'An anonymous self-check for anyone worried they crossed a line with somebody. Made by survivors.', 'vibe-check.html', 'vc-step-start', 'Anonymous'),
  ('BAE Skills Lab', 'Six interactive lessons on consent, boundaries and healthy relationships.', 'https://skills-lab.safebae.org/', 'sl-home', '6 activities'),
]


def frame(name, alt, cap='', cls=''):
    capt = f'<figcaption>{esc(cap)}</figcaption>' if cap else ''
    return (f'<figure class="ai-frame {cls}"><div class="ai-frame__bar" aria-hidden="true"><i></i><i></i><i></i><span>ai-literacy.safebae.org</span></div>'
            f'{img(name, alt)}{capt}</figure>')


def mod_panel(m, i):
    num = f'Module {m["n"]}' if m['n'] else ('Start here' if m['k'] == 'welcome' else 'Wrap-up')
    name, kind, alt, cap = m['img']
    media = frame(name, alt, cap) if kind == 'shot' else f'<figure class="ai-illo">{img(name, alt)}<figcaption>{esc(cap)}</figcaption></figure>'
    letter = str(m['n']) if m['n'] else ''
    secs = ''.join(f'<li><b>{letter}{chr(65+j)}</b>{esc(s)}</li>' for j, s in enumerate(m['sections']))
    secs_html = f'<div class="ai-secs"><p class="ai-hand-lbl">Inside this module</p><ol>{secs}</ol></div>' if secs else ''
    exp_lbl = 'In this module, you will explore' if m['n'] else ('What you’ll have learned, among other things' if m['k'] == 'end' else '')
    exp = ''.join(f'<li>{esc(x)}</li>' for x in m['explore'])
    exp_html = f'<p class="ai-hand-lbl">{exp_lbl}</p><ul class="ai-ticks">{exp}</ul>' if exp else f'<p class="ai-mpanel__desc">{esc(m["desc"])}</p>'
    desc_html = f'<p class="ai-mpanel__desc">{esc(m["desc"])}</p>' if exp else ''
    return f'''<div class="ai-mpanel" role="tabpanel" id="mp-{m['k']}" aria-labelledby="tab-mod-{m['k']}"{'' if m['k'] == 'm1' else ' hidden'}>
  <div class="ai-mpanel__txt">
    <p class="ai-mpanel__k"><span>{esc(num)}</span><span>{esc(m['time'])}</span><span>{m['screens']} screen{'s' if m['screens'] > 1 else ''}</span></p>
    <h3>{esc(m['title'])}</h3>
    <p class="ai-mpanel__lead">{esc(m['lead'])}</p>
    {desc_html}
    {exp_html}
  </div>
  <div class="ai-mpanel__side">{media}{secs_html}</div>
</div>'''


def map_html():
    btns = []
    for m in MODS:
        sel = m['k'] == 'm1'
        dot = str(m['n']) if m['n'] else ('&#9733;' if m['k'] == 'welcome' else '&#10003;')
        btns.append(f'<button class="ai-stop{" ai-stop--end" if not m["n"] else ""}" role="tab" id="tab-mod-{m["k"]}" aria-controls="mp-{m["k"]}" aria-selected="{str(sel).lower()}" tabindex="{0 if sel else -1}">'
                    f'<span class="ai-stop__dot" aria-hidden="true">{dot}</span><span class="ai-stop__lbl">{esc(m["label"])}</span><span class="ai-stop__t">{esc(m["time"])}</span>'
                    f'<span class="sr-only">{esc(m["title"])}</span></button>')
    return '<div class="ai-map" role="tablist" aria-label="Training map">' + ''.join(btns) + '</div>'


def four_step():
    nodes = ''.join(f'<button type="button" class="ai-node ai-node--{i}" data-step="{i}" aria-pressed="{str(i == 0).lower()}"><span class="ai-node__n">{i+1}</span><b>{esc(t)}</b><small>{esc(s)}</small></button>' for i, (t, s, l) in enumerate(STEPS4))
    details = ''.join(f'<div class="ai-4d" data-d="{i}"{"" if i == 0 else " hidden"}><b>{esc(t)}</b><p>{esc(l)}</p></div>' for i, (t, s, l) in enumerate(STEPS4))
    return f'''<div class="ai-4">
  <div class="ai-wheel">
    <svg class="ai-wheel__c" viewBox="0 0 400 400" aria-hidden="true"><path d="M206 38C300 40 364 108 362 202C360 296 292 364 198 362C104 360 38 292 40 198C42 110 108 44 190 40C214 39 232 42 250 48" fill="none" stroke="#13848f" stroke-width="4" stroke-linecap="round"/><path d="M244 36l12 13-17 6" fill="none" stroke="#13848f" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div class="ai-wheel__mid"><b>Keep going around</b><span>every answer, every time</span></div>
    {nodes}
  </div>
  <div class="ai-4details" aria-live="polite">{details}</div>
</div>'''


def build():
    BRUSH_TEAL = brush('#13848f', '0.85')
    BRUSH_MINT = brush('#15ffc8', '0.9')
    LOOP_MINT = loop('#15ffc8')
    LOOP_TEAL = loop('#13848f')
    LOOP_CORAL = loop('#fe7171')
    WAVE_TEAL = wave('#13848f')
    WAVE_MINT = wave('#15ffc8')
    RING_TEAL = ring('#13848f')
    RING_MINT = ring('#15ffc8')
    DOTS = 'radial-gradient(rgba(19,132,143,.2) 1.1px, transparent 1.5px) 0 0/18px 18px'
    DOTS_DARK = 'radial-gradient(rgba(209,254,255,.11) 1.1px, transparent 1.5px) 0 0/18px 18px'

    CSS = f'''
body.ai{{--hand:"Balsamiq Sans","Comic Neue",var(--body)}}
.ai h1,.ai .ai-hand{{font-family:var(--hand)}}
/* marker word on this page = the training's double brushstroke */
.ai .mk{{background:{BRUSH_MINT} center/100% 100% no-repeat; padding:.02em .22em .08em; margin:0 -.1em; color:var(--slate); border-radius:0}}
.ai .ai-hero .mk{{background-image:{BRUSH_TEAL}; color:#fff}}
.ai-loop{{position:relative; display:inline-block}}
.ai-loop::after{{content:""; position:absolute; inset:-.32em -.5em -.36em -.55em; background:{LOOP_MINT} center/100% 100% no-repeat; pointer-events:none}}
.ai-loop--teal::after{{background-image:{LOOP_TEAL}}}
.ai-hand-lbl{{font-family:var(--hand); font-weight:700; font-size:1.05rem; margin:0 0 10px; color:var(--logo-teal)}}
.ai-wave{{height:14px; background:{WAVE_TEAL} center/100% 100% no-repeat; border:0; margin:22px 0}}

/* ---------- hero ---------- */
.ai-hero{{position:relative; overflow:hidden; background:var(--slate); background-image:var(--grain), {DOTS_DARK}; color:#fff}}
.ai-hero > .wrap{{position:relative; z-index:1; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.02fr); gap:clamp(28px,4vw,60px); align-items:center; padding-block:clamp(40px,5vw,72px) clamp(44px,5.5vw,80px)}}
.ai-hero .wrap > *{{min-width:0}}
.ai-hero .crumbs{{color:rgba(255,255,255,.8)}}
.ai-hero .eyebrow{{color:var(--mint)}}
.ai-hero h1{{font-weight:700; font-stretch:100%; font-size:clamp(2.4rem,4.3vw,3.9rem); line-height:1.08; letter-spacing:-.01em; margin:0 0 .4em; text-transform:none}}
.ai-hero .lede{{color:#fff; max-width:none}}
.ai-launch{{font-family:var(--hand); font-size:clamp(1.1rem,1.6vw,1.32rem); margin:6px 0 26px; color:var(--aqua)}}
.ai-launch .ai-loop{{color:#fff; font-weight:700; margin:0 .35em}}
.ai-facts{{display:flex; flex-wrap:wrap; gap:8px; margin-top:24px}}
.ai-facts span{{font-family:var(--hand); font-weight:700; font-size:.98rem; padding:6px 12px; border-radius:10px; border:2px solid rgba(209,254,255,.35); color:#fff}}
.ai-facts span:first-child{{background:var(--mint); color:var(--slate); border-color:var(--mint)}}
.ai-stage{{position:relative; padding:10px 9% 64px 0}}
.ai-frame{{margin:0; position:relative; background:#fff; border:2px solid var(--slate); border-radius:16px; overflow:hidden; box-shadow:8px 8px 0 var(--mint)}}
.ai-frame__bar{{display:flex; align-items:center; gap:6px; height:30px; padding:0 12px; background:var(--slate-deep); border-bottom:2px solid var(--slate)}}
.ai-frame__bar i{{width:9px; height:9px; border-radius:50%; background:rgba(209,254,255,.35)}}
.ai-frame__bar i:first-child{{background:var(--coral)}}
.ai-frame__bar span{{margin-left:10px; font-family:var(--mono); font-size:.66rem; letter-spacing:.06em; color:var(--aqua); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}}
.ai-frame img{{width:100%; height:auto}}
.ai-frame figcaption{{font-family:var(--hand); font-weight:700; font-size:.92rem; padding:8px 14px; background:var(--aqua); color:var(--slate); border-top:2px solid var(--slate)}}
.ai-stage .ai-frame{{transform:rotate(1.4deg)}}
.ai-phone{{position:absolute; right:0; bottom:0; width:27%; aspect-ratio:390/800; border-radius:30px; border:8px solid #0b1f25; background:#0b1f25; overflow:hidden; box-shadow:0 30px 60px -24px rgba(0,0,0,.7), 6px 6px 0 var(--mint); transform:rotate(5deg); z-index:2}}
.ai-phone img{{width:100%; height:100%; object-fit:cover; object-position:top}}
.ai-note{{position:absolute; left:4%; bottom:4px; z-index:3; font-family:var(--hand); font-weight:700; font-size:clamp(1rem,1.4vw,1.2rem); color:var(--slate); background:var(--mint); padding:8px 14px 9px; border-radius:6px; transform:rotate(-3deg); box-shadow:3px 3px 0 var(--slate)}}
.ai-note svg{{position:absolute; right:-50px; top:-34px; width:56px; height:50px; color:var(--mint); transform:scaleX(-1)}}
@media (max-width:960px){{ .ai-hero > .wrap{{grid-template-columns:minmax(0,1fr)}} .ai-stage{{max-width:640px}} }}
@media (max-width:520px){{ .ai-stage{{padding:6px 14% 70px 0}} .ai-phone{{width:34%; border-width:6px; border-radius:22px}} .ai-note{{left:0}} .ai-note svg{{display:none}} }}

/* ---------- who + goals ---------- */
.ai-dots{{background:#fff; background-image:{DOTS}}}
.ai-who{{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(28px,4.5vw,64px); align-items:stretch}}
.ai-who > *{{min-width:0}}
.ai-who h2{{font-size:clamp(1.9rem,3.4vw,3rem)}}
.ai-who .ai-illo{{margin-top:26px}}
.ai-illo{{margin:0; position:relative}}
.ai-illo img{{width:100%; border-radius:var(--r-xl); border:2px solid var(--slate); box-shadow:8px 8px 0 var(--mint)}}
.ai-illo figcaption{{font-family:var(--hand); font-size:.92rem; color:var(--ink-soft); margin-top:12px}}
.ai-goals{{background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3vw,34px); box-shadow:8px 8px 0 var(--teal)}}
.ai-goals h3{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(1.4rem,2.2vw,1.8rem); margin-bottom:.6em}}
.ai-goals ol{{list-style:none; padding:0; margin:0; display:grid; gap:16px; counter-reset:g}}
.ai-goals li{{counter-increment:g; display:grid; grid-template-columns:44px minmax(0,1fr); gap:14px; align-items:start; margin:0; font-size:1.02rem; line-height:1.5}}
.ai-goals li::before{{content:counter(g); width:44px; height:44px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; font-size:1.25rem; color:var(--logo-teal); background:{RING_TEAL} center/100% 100% no-repeat}}
.ai-goals b{{font-family:var(--hand)}}
.ai-noteq{{margin:22px 0 0; position:relative; padding:26px 28px 24px; border-radius:18px; background:var(--aqua)}}
.ai-noteq::after{{content:""; position:absolute; inset:-10px -12px; background:{LOOP_TEAL} center/100% 100% no-repeat; pointer-events:none}}
.ai-noteq figcaption{{font-family:var(--hand); font-weight:700; color:var(--logo-teal); margin-bottom:6px}}
.ai-noteq blockquote{{margin:0; font-family:var(--hand); font-size:1.12rem; line-height:1.5; color:var(--slate)}}
@media (max-width:900px){{ .ai-who{{grid-template-columns:1fr}} }}

/* ---------- module map ---------- */
.ai-mods{{background-image:var(--grain), {DOTS_DARK}}}
.ai-mods .section-head h2{{font-family:var(--hand); font-stretch:100%; font-weight:700}}
.ai-map{{position:relative; display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); gap:4px; margin-bottom:28px; padding-top:4px}}
.ai-map::before{{content:""; position:absolute; left:6%; right:6%; top:30px; height:14px; background:{WAVE_MINT} center/100% 100% no-repeat; opacity:.55}}
.ai-stop{{position:relative; font:inherit; background:none; border:0; color:#fff; cursor:pointer; display:flex; flex-direction:column; align-items:center; gap:6px; padding:0 2px 10px; text-align:center; border-radius:12px}}
.ai-stop__dot{{width:56px; height:56px; display:grid; place-items:center; border-radius:50%; background:var(--slate-deep); border:2.5px solid rgba(209,254,255,.45); font-family:var(--hand); font-weight:700; font-size:1.5rem; color:var(--aqua); transition:transform .3s var(--ease), background .3s, border-color .3s, color .3s; position:relative; z-index:1}}
.ai-stop--end .ai-stop__dot{{font-size:1.2rem}}
.ai-stop__lbl{{font-family:var(--hand); font-weight:700; font-size:1rem; line-height:1.15; color:#fff}}
.ai-stop__t{{font-family:var(--mono); font-size:.68rem; letter-spacing:.06em; color:var(--aqua)}}
.ai-stop:hover .ai-stop__dot{{border-color:var(--mint); transform:translateY(-3px)}}
.ai-stop[aria-selected="true"] .ai-stop__dot{{background:var(--mint); border-color:var(--mint); color:var(--slate); transform:scale(1.08)}}
.ai-stop[aria-selected="true"] .ai-stop__dot::after{{content:""; position:absolute; inset:-12px; background:{RING_MINT} center/100% 100% no-repeat}}
.ai-stop[aria-selected="true"] .ai-stop__lbl{{color:var(--mint)}}
.ai-mpanel{{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:start; background:#fff; color:var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3.2vw,40px); box-shadow:8px 8px 0 var(--mint)}}
.ai-mpanel > *{{min-width:0}}
.ai-mpanel__k{{display:flex; flex-wrap:wrap; gap:6px; margin:0 0 12px}}
.ai-mpanel__k span{{font-family:var(--mono); font-size:.72rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; padding:4px 9px; border-radius:6px; background:var(--aqua); color:var(--slate)}}
.ai-mpanel__k span:first-child{{background:var(--slate); color:var(--mint)}}
.ai-mpanel h3{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(1.7rem,2.8vw,2.5rem); line-height:1.1; margin:0 0 .45em}}
.ai-mpanel__lead{{font-family:var(--hand); font-size:1.18rem; line-height:1.5; margin:0 0 14px}}
.ai-mpanel__desc{{color:var(--ink-soft); margin:0 0 18px}}
.ai-ticks{{list-style:none; padding:0; margin:0; display:grid; gap:9px}}
.ai-ticks li{{display:grid; grid-template-columns:22px minmax(0,1fr); gap:10px; margin:0; line-height:1.45; font-size:.97rem}}
.ai-ticks li::before{{content:""; width:20px; height:20px; margin-top:2px; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 13c3 2 5 5 6 7c3-7 7-12 12-16' fill='none' stroke='%2313848f' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}}
.ai-secs{{margin-top:22px}}
.ai-secs ol{{list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:6px}}
.ai-secs li{{margin:0; display:inline-flex; align-items:center; gap:6px; font-size:.84rem; font-weight:600; padding:5px 10px 5px 6px; border-radius:8px; background:var(--mist); border:1px solid var(--line)}}
.ai-secs li b{{font-family:var(--mono); font-size:.68rem; background:var(--slate); color:var(--mint); border-radius:4px; padding:2px 5px}}
.ai-mpanel .ai-illo img{{box-shadow:6px 6px 0 var(--teal)}}
.ai-mpanel .ai-frame{{box-shadow:6px 6px 0 var(--teal)}}
.ai-mgo{{margin-top:24px}}
@media (max-width:1000px){{ .ai-map{{display:flex; overflow-x:auto; scrollbar-width:none; gap:2px; margin-inline:calc(var(--gutter) * -1); padding-inline:var(--gutter); scroll-snap-type:x proximity}} .ai-map::-webkit-scrollbar{{display:none}} .ai-map::before{{display:none}} .ai-stop{{flex:0 0 96px; scroll-snap-align:start}} .ai-mpanel{{grid-template-columns:1fr}} .ai-mpanel__side{{display:contents}} .ai-mpanel figure{{order:-1}} .ai-secs{{order:2; margin-top:0}} }}

/* ---------- four-step check ---------- */
.ai-4wrap{{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(28px,5vw,72px); align-items:center}}
.ai-4wrap > *{{min-width:0}}
.ai-4wrap h2{{font-family:var(--hand); font-stretch:100%; font-weight:700; font-size:clamp(2rem,4vw,3.4rem); line-height:1.08}}
.ai-4{{display:grid; gap:18px}}
.ai-wheel{{position:relative; width:min(460px,100%); aspect-ratio:1; margin-inline:auto}}
.ai-wheel__c{{position:absolute; inset:9%; width:82%; height:82%}}
.ai-wheel__mid{{position:absolute; inset:0 31%; display:grid; place-content:center; text-align:center; pointer-events:none; line-height:1.2; gap:2px}}
.ai-wheel__mid b{{font-family:var(--hand); font-size:1.05rem; color:var(--logo-teal)}}
.ai-wheel__mid span{{font-family:var(--hand); font-size:.86rem; color:var(--ink-soft)}}
.ai-node{{position:absolute; width:34%; font:inherit; text-align:center; background:#fff; color:var(--slate); border:2px solid var(--slate); border-radius:16px; padding:10px 12px 12px; cursor:pointer; box-shadow:4px 4px 0 var(--teal); transition:transform .25s var(--ease), background .25s, box-shadow .25s; display:flex; flex-direction:column; align-items:center; gap:2px}}
.ai-node__n{{width:30px; height:30px; display:grid; place-items:center; font-family:var(--hand); font-weight:700; background:{RING_TEAL} center/100% 100% no-repeat}}
.ai-node b{{font-family:var(--hand); font-size:1.25rem; text-transform:uppercase; letter-spacing:.04em}}
.ai-node small{{font-size:.8rem; line-height:1.3; color:var(--ink-soft)}}
.ai-node:hover{{transform:translateY(-3px)}}
.ai-node[aria-pressed="true"]{{background:var(--mint); box-shadow:4px 4px 0 var(--slate)}}
.ai-node[aria-pressed="true"] small{{color:var(--slate)}}
.ai-node--0{{left:33%; top:-1%}} .ai-node--1{{right:-3%; top:34%}} .ai-node--2{{left:33%; bottom:-1%}} .ai-node--3{{left:-3%; top:34%}}
.ai-4d{{position:relative; background:#fff; border:2px solid var(--slate); border-radius:18px; padding:18px 22px; box-shadow:6px 6px 0 var(--mint)}}
.ai-4d b{{display:block; font-family:var(--hand); font-size:1.25rem; color:var(--logo-teal); margin-bottom:4px}}
.ai-4d p{{margin:0; line-height:1.55}}
@media (max-width:900px){{ .ai-4wrap{{grid-template-columns:1fr}} }}
@media (max-width:560px){{ .ai-wheel{{aspect-ratio:auto; display:grid; grid-template-columns:1fr 1fr; gap:12px}} .ai-wheel__c,.ai-wheel__mid{{display:none}} .ai-node{{position:static; width:auto}} .ai-node--1{{order:1}} .ai-node--2{{order:3}} .ai-node--3{{order:2}} }}

/* ---------- how it works ---------- */
.ai-steps{{list-style:none; margin:0; padding:0; display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:clamp(16px,2vw,26px); counter-reset:h}}
.ai-steps li{{position:relative; margin:0; counter-increment:h; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); padding:22px 22px 24px; box-shadow:6px 6px 0 var(--aqua); min-width:0}}
.ai-steps li::before{{content:counter(h); display:grid; place-items:center; width:58px; height:58px; margin-bottom:10px; font-family:var(--hand); font-weight:700; font-size:1.9rem; color:var(--logo-teal); background:{RING_TEAL} center/100% 100% no-repeat}}
.ai-steps li:not(:last-child)::after{{content:""; position:absolute; right:-24px; top:40px; width:30px; height:22px; z-index:2; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 24'%3E%3Cpath d='M2 14C12 6 22 6 34 12M26 4l9 8-10 6' fill='none' stroke='%2313848f' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}}
.ai-steps h3{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:1.3rem; margin-bottom:.4em}}
.ai-steps p{{margin:0; color:var(--ink-soft); font-size:.95rem; line-height:1.5}}
.ai-feat{{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,4.5vw,64px); align-items:center; margin-top:clamp(40px,5vw,64px)}}
.ai-feat > *{{min-width:0}}
.ai-feat h3{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(1.5rem,2.4vw,2.1rem)}}
.ai-flist{{list-style:none; padding:0; margin:0; display:grid; gap:12px}}
.ai-flist li{{margin:0; display:grid; grid-template-columns:132px minmax(0,1fr); gap:14px; align-items:baseline; padding-bottom:12px; border-bottom:1px solid var(--line)}}
.ai-flist li:last-child{{border-bottom:0; padding-bottom:0}}
.ai-flist b{{font-family:var(--hand); font-size:1.06rem; color:var(--logo-teal)}}
.ai-flist span{{font-size:.95rem; line-height:1.5}}
.ai-flist .x b{{justify-self:start; display:inline-block; background:var(--coral); color:var(--slate); padding:1px 8px; border-radius:6px}}
.ai-shotwrap{{position:relative}}
.ai-shotwrap .ai-mark{{position:absolute; pointer-events:none; background:{loop('#15ffc8', 4)} center/100% 100% no-repeat}}
@media (max-width:1000px){{ .ai-steps{{grid-template-columns:1fr 1fr}} .ai-steps li:nth-child(2)::after{{display:none}} .ai-feat{{grid-template-columns:1fr}} }}
@media (max-width:560px){{ .ai-steps{{grid-template-columns:1fr}} .ai-steps li::after{{display:none}} .ai-flist li{{grid-template-columns:1fr; gap:2px}} }}

/* ---------- educators / parents / privacy ---------- */
.ai-trio{{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(16px,2vw,24px); align-items:stretch}}
.ai-card{{display:flex; flex-direction:column; gap:12px; border-radius:var(--r-xl); padding:clamp(22px,2.6vw,32px); background:rgba(255,255,255,.05); border:1.5px solid var(--line-dark); min-width:0}}
.ai-card h3{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:1.6rem; margin:0; color:#fff}}
.ai-card p{{margin:0; color:#fff; line-height:1.55}}
.ai-card .btns{{margin-top:auto; padding-top:8px}}
.ai-card--edu{{background:var(--mint); color:var(--slate); border-color:var(--mint)}}
.ai-card--edu h3,.ai-card--edu p{{color:var(--slate)}}
.ai-card blockquote{{margin:0; font-family:var(--hand); font-size:1.08rem; line-height:1.5; color:#fff; padding:14px 16px; border-radius:14px; background:rgba(255,255,255,.06); border-left:4px solid var(--mint)}}
.ai-card small{{color:var(--aqua); font-size:.88rem; line-height:1.45}}
@media (max-width:960px){{ .ai-trio{{grid-template-columns:1fr}} }}

/* ---------- connects ---------- */
.ai-conn{{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:clamp(14px,1.8vw,22px)}}
.ai-cc{{display:flex; flex-direction:column; background:#fff; border:2px solid var(--slate); border-radius:var(--r-xl); overflow:hidden; text-decoration:none; color:var(--slate); box-shadow:6px 6px 0 var(--teal); transition:transform .2s var(--ease), box-shadow .2s; min-width:0}}
.ai-cc:hover{{transform:translate(-2px,-3px); box-shadow:9px 9px 0 var(--mint)}}
.ai-cc__img{{aspect-ratio:16/10; overflow:hidden; background:var(--slate); border-bottom:2px solid var(--slate)}}
.ai-cc__img img{{width:100%; height:100%; object-fit:cover; object-position:top}}
.ai-cc__b{{padding:16px 18px 18px; display:flex; flex-direction:column; gap:6px; flex:1}}
.ai-cc__b small{{font-family:var(--mono); font-size:.66rem; letter-spacing:.08em; text-transform:uppercase; font-weight:600; color:var(--logo-teal)}}
.ai-cc__b b{{font-family:var(--hand); font-size:1.3rem; line-height:1.15}}
.ai-cc__b span{{font-size:.9rem; color:var(--ink-soft); line-height:1.45}}
.ai-cc__go{{margin-top:auto; padding-top:8px; font-weight:800; font-family:var(--display); color:var(--logo-teal)}}
@media (max-width:1000px){{ .ai-conn{{grid-template-columns:1fr 1fr}} }}
@media (max-width:560px){{ .ai-conn{{grid-template-columns:1fr}} }}

/* ---------- support ---------- */
.ai-sup{{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-top:8px}}
.ai-sl{{display:flex; flex-direction:column; gap:4px; padding:16px 18px; border-radius:14px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); text-decoration:none; color:#fff; min-width:0}}
.ai-sl:hover{{border-color:var(--mint)}}
.ai-sl b{{font-family:var(--display); font-stretch:106%; font-size:1.02rem; line-height:1.2}}
.ai-sl strong{{font-family:var(--mono); font-weight:600; font-size:.86rem; color:var(--mint); overflow-wrap:anywhere}}
.ai-sl span{{font-size:.86rem; color:#fff; opacity:.86; line-height:1.4}}
.ai-sl--wide{{grid-column:span 2}}
.ai-suphead{{display:flex; justify-content:space-between; align-items:end; gap:16px 30px; flex-wrap:wrap; margin-bottom:22px}}
.ai-suphead h2{{font-family:var(--hand); font-stretch:100%; font-weight:700; margin:0}}
.ai-suphead p{{margin:.4em 0 0; color:#fff}}
@media (max-width:960px){{ .ai-sup{{grid-template-columns:1fr 1fr}} .ai-sl--wide{{grid-column:1/-1}} }}
@media (max-width:520px){{ .ai-sup{{grid-template-columns:1fr}} }}

/* ---------- final CTA ---------- */
.ai-cta{{text-align:center}}
.ai-cta h2{{font-family:var(--hand); font-weight:700; font-stretch:100%; font-size:clamp(2.4rem,6.4vw,5.6rem); line-height:1.02; margin:0 0 .25em}}
.ai-cta .mk{{background-image:{brush('#ffffff', '0.85')}}}
.ai-cta p{{font-family:var(--hand); font-size:clamp(1.1rem,1.6vw,1.35rem); max-width:none; margin:0}}
.ai-cta .btns{{justify-content:center; margin-top:26px}}
.ai-cta__url{{display:block; margin-top:18px; font-family:var(--mono); font-size:.86rem; letter-spacing:.06em; color:var(--slate)}}
'''

    JS = r'''
(function(){
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* four-step check */
  var nodes = d.querySelectorAll('.ai-node'), dets = d.querySelectorAll('.ai-4d'), cur = 0, auto = !reduce, seen = false;
  function pick(i, user){ cur = i; nodes.forEach(function(n){ n.setAttribute('aria-pressed', String(+n.dataset.step === i)); }); dets.forEach(function(x){ x.hidden = +x.dataset.d !== i; }); if(user) auto = false; }
  nodes.forEach(function(n){ n.addEventListener('click', function(){ pick(+n.dataset.step, true); }); });
  var wheel = d.querySelector('.ai-4');
  if(wheel){
    if('IntersectionObserver' in window){ new IntersectionObserver(function(es){ es.forEach(function(e){ seen = e.isIntersecting; }); }, {threshold:.4}).observe(wheel); } else seen = true;
    wheel.addEventListener('mouseenter', function(){ auto = false; });
    setInterval(function(){ if(auto && seen) pick((cur + 1) % nodes.length); }, 3600);
  }
  /* keep the selected stop visible when the map scrolls (narrow screens) */
  var map = d.querySelector('.ai-map');
  if(map){ map.addEventListener('click', function(e){ var b = e.target.closest('[role="tab"]'); if(!b || map.scrollWidth <= map.clientWidth + 4) return; map.scrollTo({left: b.offsetLeft - map.clientWidth/2 + b.offsetWidth/2, behavior: reduce ? 'auto' : 'smooth'}); }); }
})();
'''

    panels = ''.join(mod_panel(m, i) for i, m in enumerate(MODS))
    sup = ''.join(f'<a class="ai-sl{" ai-sl--wide" if n == "Take It Down" else ""}" href="{u}" target="_blank" rel="noopener"><b>{esc(n)}</b><strong>{esc(num)}</strong><span>{esc(dsc)}</span></a>' for n, num, dsc, u in SUPPORT)
    conn = ''.join(f'<a class="ai-cc" href="{h}"{ " target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><span class="ai-cc__img">{img(im, "")}</span><span class="ai-cc__b"><small>{esc(tag)}</small><b>{esc(t)}</b><span>{esc(dsc)}</span><span class="ai-cc__go">{"Open" if h.startswith("http") else "Go"} {"&#8599;" if h.startswith("http") else "&rarr;"}</span></span></a>' for t, dsc, h, im, tag in CONNECT)
    goals = ''.join(f'<li><span>{esc(g)}</span></li>' for g in GOALS)
    arrow = '<svg viewBox="0 0 60 54" aria-hidden="true"><path d="M52 50C36 44 18 30 10 8M4 18l6-12 11 7" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

    body = f'''
<section class="ai-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="rise">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="students.html">Students</a><span>/</span><span>AI Literacy Training</span></nav>
      <p class="eyebrow">New &middot; Free &middot; Ages 13+</p>
      <h1>SafeBAE AI Literacy <span class="mk">Training</span></h1>
      <p class="lede">Six modules for high school and college students on AI, how it works, where it can go wrong, and what it means for navigating relationships, consent, privacy, and a world increasingly shaped by algorithms.</p>
      <p class="ai-launch">Launches during U.S. Media Literacy Week, <span class="ai-loop">October 26–30, 2026</span></p>
      <div class="btns">{btn('Start the training', TRAIN, 'mint')}{btn('Group access for educators', EDU, 'ghost')}</div>
      <div class="ai-facts"><span>Free</span><span>6 modules</span><span>Self-paced</span><span>Progress saves</span><span>Certificate</span></div>
    </div>
    <div class="ai-stage">
      {frame('ai-shot-home', 'Screenshot of the training’s home screen: “SafeBAE AI Literacy Training” beside a drawing of a billboard with a binary smiley face and a name tag that reads “Hello, my name is AI”')}
      <div class="ai-phone">{img('ai-m-four', 'The training on a phone, open to the Four-Step Check')}</div>
      <span class="ai-note">{arrow}Media Literacy Week, Oct 26–30</span>
    </div>
  </div>
</section>

<section class="band ai-dots">
  <div class="wrap ai-who">
    <div>
      <p class="eyebrow">Who it’s for</p>
      <h2>Made for high school and college students</h2>
      <p class="lede">The training is designed for high school and college students, though anyone 13 or older may find it useful. It builds the skills to understand AI and how it affects your relationships, your safety and the decisions you make.</p>
      <figure class="ai-illo">{img('ai-illo-hello', 'A billboard showing a smiling face drawn in binary code, with a name tag that reads “Hello, my name is AI.”')}<figcaption>Illustrations from the training</figcaption></figure>
    </div>
    <div>
      <div class="ai-goals">
        <h3>By the end, you will be able to:</h3>
        <ol>{goals}</ol>
      </div>
      <figure class="ai-noteq">
        <figcaption>A note before you begin</figcaption>
        <blockquote>“This program is not about shaming anyone for using AI. AI can be a helpful tool for creativity, learning, and fun. However, like any tool, it’s important to know how to use it thoughtfully.”</blockquote>
      </figure>
    </div>
  </div>
</section>

<section class="band band--deep ai-mods" id="modules">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Chapter map &middot; 57 screens</p><h2>Six modules, in order</h2></div></div>
    <div data-tabs="ai-mod">
      {map_html()}
      {panels}
    </div>
    <div class="btns ai-mgo">{btn('Start Module 1', TRAIN, 'mint')}</div>
  </div>
</section>

<section class="band band--aqua">
  <div class="wrap ai-4wrap">
    <div>
      <p class="eyebrow">A skill from Module 1</p>
      <h2>Pause. Question. Check. Ask.</h2>
      <p class="lede">The Four-Step Check gives you a simple way to decide what to trust, what to verify, and when an AI answer is not enough.</p>
      <p>These four steps are for answers. An AI agent takes actions, so the check has to come before it acts. Module 2 builds on it.</p>
    </div>
    {four_step()}
  </div>
</section>

<section class="band band--paper" id="how">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">How it works</p><h2>Create an account and go at your own pace</h2></div></div>
    <ol class="ai-steps">
      <li><h3>Create a free account</h3><p>Your name, your school or organization, a class code if someone gave you one, your email and a password. You confirm you are 13 or older.</p></li>
      <li><h3>Go at your own pace</h3><p>Your progress is saved to your account, so you can stop any time and pick up where you left off on any phone or computer.</p></li>
      <li><h3>Switch devices with a resume code</h3><p>Pick up on a phone, tablet or school computer. Your progress travels; anything you wrote stays on the device where you wrote it.</p></li>
      <li><h3>Get your certificate</h3><p>A one-page certificate you can print or download. It unlocks once you have finished every screen and every activity.</p></li>
    </ol>
    <div class="ai-feat">
      <div class="ai-shotwrap">
        {frame('ai-shot-settings', 'Screenshot of the training’s Settings and privacy panel, with text size and font options')}
        <span class="ai-mark" style="left:25%;top:36%;width:33%;height:28%" aria-hidden="true"></span>
      </div>
      <div>
        <h3>Built into every screen</h3>
        <ul class="ai-flist">
          <li class="x"><b>Quick Exit</b><span>A Quick Exit button sits in the header of every screen.</span></li>
          <li><b>Support</b><span>The Support button lists free crisis lines and SafeBAE resources.</span></li>
          <li><b>Text size</b><span>Small, Default, Large or Extra large.</span></li>
          <li><b>Font</b><span>Handwritten or Standard. Standard is a plainer font, for anyone who finds the handwritten one harder to read.</span></li>
          <li><b>Activities</b><span>Quick checks, sorting activities, simulated feeds, scenarios and a personal AI boundaries plan.</span></li>
          <li><b>Completion record</b><span>A printable record of which screens and activities were completed, and how much time was spent.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--slate">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">For adults</p><h2>For educators and parents</h2></div></div>
    <div class="ai-trio">
      <div class="ai-card ai-card--edu">
        <h3>Group access for educators</h3>
        <p>Assign the training to your students and follow their progress. Tell SafeBAE about your group; SafeBAE reviews each registration and emails you a class code to give your students.</p>
        <p>Registering creates an ordinary account for the training, so you can go through it yourself straight away.</p>
        <div class="btns">{btn('Register for group access', EDU, 'slate')}</div>
      </div>
      <div class="ai-card">
        <h3>For parents and caregivers</h3>
        <p>The training is free and self-paced, for high school and college students and anyone 13 or older. When a learner joins with a class code, the teacher or group leader who gave it can see their name, school, email and how far they have got.</p>
        <p>Learners can print or download a completion record to hand in when a teacher, parent, advisor or club leader asks for one.</p>
        <div class="btns">{btn('Resources for parents', 'parents.html', 'ghost', arrow=True)}</div>
      </div>
      <div class="ai-card">
        <h3>Privacy</h3>
        <blockquote>“Your name, school, email, progress and quiz answers are saved to your account, where SafeBAE staff can see them. What you type, and the personal plans and self-checks you fill in, stay on the device you used.”</blockquote>
        <small>From the training’s sign-up screen.</small>
        <div class="btns">{btn('Read the Privacy Policy', PRIV, 'ghost')}</div>
      </div>
    </div>
  </div>
</section>

<section class="band band--mist">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">More from SafeBAE</p><h2>Where it connects to SafeBAE’s other tools</h2></div></div>
    <div class="ai-conn">{conn}</div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap">
    <div class="ai-suphead"><div><p class="eyebrow">Listed inside the training</p><h2>Support is available</h2><p>Free resources, most open any hour. If you are in immediate danger, call 911.</p></div><button class="btn btn--coral" data-open-help>All hotlines</button></div>
    <div class="ai-sup">{sup}</div>
  </div>
</section>

<section class="band band--mint">
  <div class="wrap ai-cta">
    <p class="eyebrow">Launches October 26–30, 2026</p>
    <h2>Start the <span class="mk">training</span></h2>
    <p>Create a free account and your progress saves as you go.</p>
    <div class="btns">{btn('Open the AI Literacy Training', TRAIN, 'slate')}{btn('Group access for educators', EDU, 'ghost')}</div>
    <span class="ai-cta__url">ai-literacy.safebae.org</span>
  </div>
</section>
'''
    page('ai-literacy.html', 'AI Literacy Training · SafeBAE',
         'The free SafeBAE AI Literacy Training: six self-paced modules for high school and college students on how AI works, feeds, relationships, using AI well, fake images and sextortion. Launches October 26–30, 2026.',
         body, active='students', body_class='ai', fonts='family=Balsamiq+Sans:ital,wght@0,400;0,700;1,400',
         head_extra=f'<style>{CSS}</style>', scripts=f'<script>{JS}</script>')


if __name__ == '__main__':
    build()
