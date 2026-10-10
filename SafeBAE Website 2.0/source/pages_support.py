"""SUPPORT & RIGHTS group: survivor-support, title-ix, myths-facts, faq, posters, blog."""
from lib import *
from data import FAQ, LIB
from films_common import help_inline, HELPLINE_CSS, POSTERS_ZIP, related
import datetime, json, re

WPU = 'https://www.safebae.org/wp-content/uploads/'
JOTFORM = 'https://form.jotform.com/243014598961160'
SUBSTACK = 'https://substack.com/@safebae'
BOOKSHOP = 'https://bookshop.org/shop/SafeBAE'


def crumbs(*items):
    out = []
    for t, h in items:
        out.append(a(esc(t), h) if h else f'<span>{esc(t)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(out) + '</nav>'


def esc_note():
    return ('<p class="sp-esc"><span>Need to leave quickly?</span> <span>Press <span class="kbd">Esc</span> twice</span> '
            '<span>or</span> <button type="button" data-quick-exit>Quick exit</button></p>')


def month(d):
    return datetime.date.fromisoformat(d).strftime('%b %Y')


def post_card(title, date, link, thumb):
    return (f'<a class="sp-post" href="{esc(link)}" target="_blank" rel="noopener">'
            f'<span class="sp-post__img">{img(thumb, "")}</span>'
            f'<time datetime="{date}">{month(date)}</time><b>{esc(title)}</b>'
            f'<span class="sp-post__go">Read on safebae.org &#8599;</span></a>')


def next_cards(items):
    out = []
    for kicker, title, desc, href in items:
        ext = href.startswith('http')
        t = ' target="_blank" rel="noopener"' if ext else ''
        out.append(f'<a href="{esc(href)}"{t}><small>{esc(kicker)}</small><b>{esc(title)}</b><span>{esc(desc)}</span>'
                   f'<i class="go" aria-hidden="true">{"&#8599;" if ext else "&rarr;"}</i></a>')
    return '<div class="sp-next">' + ''.join(out) + '</div>'


def player(slides, label, cls='', pid='', interval=5200):
    """slides: list of (image, caption, alt)."""
    sl = ''.join(f'<div class="player__slide{" on" if i == 0 else ""}" data-cap="{esc(c)}">{img(n, alt, loading="eager" if i == 0 else "lazy")}</div>'
                 for i, (n, c, alt) in enumerate(slides))
    i = f' id="{pid}"' if pid else ''
    return (f'<div class="player {cls}"{i} data-player data-zoom data-interval="{interval}" aria-roledescription="carousel" aria-label="{esc(label)}">'
            f'<div class="player__bar"><i></i></div>{sl}<div class="player__ctl"><button type="button" data-prev aria-label="Previous slide">&#8249;</button>'
            f'<span class="player__cap"></span><button type="button" data-next aria-label="Next slide">&#8250;</button></div></div>')


def vibe_band(title='Worried you, or a friend, crossed a line?'):
    return f'''<section class="band band--teal sp-vibe" id="vibe-check">
  <div class="wrap sp-vibe__grid">
    <div>
      <p class="sp-vibe__mark"><span class="daisy" aria-hidden="true"></span>Vibe Check by SafeBAE</p>
      <h2>{esc(title)}</h2>
      <p class="lede" style="color:#fff">CheckYourVibe.org is a free, anonymous reflection tool for young people who are questioning whether they, or a friend, may have crossed a boundary or caused harm.</p>
      <p style="color:#fff">Young people are increasingly turning to anonymous forums and AI chatbots to ask difficult questions about relationships and consent. Vibe Check guides users through confusing situations and connects them with real, evidence-based resources on consent, communication and accountability. No names, no accounts, and nothing is stored.</p>
      <div class="btns">{btn('Open Vibe Check', 'https://checkyourvibe.org/', 'mint')}{btn('How it works', 'vibe-check.html', 'white', arrow=True)}</div>
    </div>
    <div class="sp-vibe__phone"><div class="sp-phone">{img('vc-screen', 'The Vibe Check home screen on a phone')}</div><span class="sticker">Anonymous</span><span class="sticker sticker--white sticker--r">Nothing is stored</span></div>
  </div>
</section>'''


SP_CSS = '''
.sp-esc{display:flex; flex-wrap:wrap; align-items:center; gap:6px 8px; margin:20px 0 0; font-size:.88rem; font-weight:600}
.sp-esc .kbd{font-size:.76rem; padding:1px 6px}
.sp-esc button{font:inherit; font-size:.82rem; font-weight:800; background:var(--coral); color:var(--slate); border:0; border-radius:5px; padding:4px 10px; cursor:pointer}
.sp-post{display:flex; flex-direction:column; text-decoration:none; color:inherit; height:100%; min-width:0}
.sp-post__img{display:block; aspect-ratio:40/21; border-radius:12px; overflow:hidden; background:var(--slate)}
.sp-post__img img{width:100%; height:100%; object-fit:cover; transition:transform .5s}
.sp-post:hover .sp-post__img img{transform:scale(1.04)}
.sp-post time{font-family:var(--mono); font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); margin-top:14px; font-weight:600}
.sp-post b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.12rem; line-height:1.2; margin-top:4px; text-wrap:pretty}
.sp-post:hover b{text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:3px}
.sp-post__go{margin-top:auto; padding-top:10px; font-size:.8rem; font-weight:700; color:var(--ink-soft)}
.band--slate .sp-post time,.band--deep .sp-post time{color:var(--mint)} .band--slate .sp-post b,.band--deep .sp-post b{color:#fff} .band--slate .sp-post__go,.band--deep .sp-post__go{color:rgba(255,255,255,.65)}
.sp-posts{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:22px}
.sp-posts--3{grid-template-columns:repeat(3,minmax(0,1fr))}
@media (max-width:1000px){.sp-posts{grid-template-columns:repeat(2,minmax(0,1fr))} .sp-posts--3{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:760px){.sp-posts--3{grid-template-columns:1fr}}
@media (max-width:560px){.sp-posts{grid-template-columns:1fr}}
.sp-next{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.sp-next a{position:relative; display:flex; flex-direction:column; gap:6px; padding:20px 20px 52px; border-radius:14px; background:#fff; border:1px solid var(--line); text-decoration:none; color:var(--slate); transition:transform .2s, box-shadow .2s; min-width:0}
.sp-next a:hover{transform:translateY(-3px); box-shadow:var(--shadow-soft)}
.sp-next small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.sp-next b{font-family:var(--display); font-stretch:108%; font-size:1.25rem; line-height:1.12; color:var(--logo-teal)}
.sp-next span{font-size:.92rem; color:var(--ink-soft); line-height:1.45}
.sp-next .go{position:absolute; left:20px; bottom:16px; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal); font-style:normal; font-weight:800; transition:background .2s, transform .2s}
.sp-next a:hover .go{background:var(--mint); transform:translateX(3px)}
@media (max-width:960px){.sp-next{grid-template-columns:1fr 1fr}} @media (max-width:520px){.sp-next{grid-template-columns:1fr}}
.player.sp-portrait{aspect-ratio:4/5}
.player.sp-portrait .player__slide img{background:#fff}
.player[data-zoom]{cursor:zoom-in}
.sp-chips{display:flex; flex-wrap:wrap; gap:8px}
.sp-chips button,.sp-chips a{font:inherit; font-size:.86rem; font-weight:700; line-height:1.2; padding:8px 14px; border-radius:999px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; text-decoration:none}
.sp-chips button:hover,.sp-chips a:hover{border-color:var(--teal)}
.sp-chips button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.sp-chips small{font-family:var(--mono); font-size:.7rem; opacity:.7; margin-left:4px}
.band--slate .sp-chips button,.band--deep .sp-chips button{background:transparent; color:#fff; border-color:var(--line-dark)}
.band--slate .sp-chips button[aria-pressed="true"],.band--deep .sp-chips button[aria-pressed="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.sp-vibe__grid{display:grid; grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr); gap:clamp(28px,5vw,72px); align-items:center}
.sp-vibe__mark{display:flex; align-items:center; gap:12px; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:1.2rem; color:var(--mint); margin:0 0 18px}
.sp-vibe__mark .daisy{width:38px; height:38px}
.sp-vibe h2{color:#fff}
.sp-vibe__phone{position:relative}
.sp-phone{width:min(280px,70vw); margin-inline:auto; aspect-ratio:390/800; border-radius:42px; border:10px solid #0b1f25; background:#0b1f25; overflow:hidden; transform:rotate(-4deg); box-shadow:0 50px 90px -30px rgba(0,0,0,.6)}
.sp-phone img{width:100%; height:100%; object-fit:cover; object-position:top}
.sp-vibe__phone .sticker{position:absolute; left:4%; top:16%}
.sp-vibe__phone .sticker--white{left:auto; top:auto; right:4%; bottom:18%}
@media (max-width:860px){.sp-vibe__grid{grid-template-columns:1fr} .sp-phone{width:min(230px,62vw)}}
.sp-lead{color:var(--ink-soft)}
.section-head > .btns{flex:0 1 auto; min-width:0; margin-left:auto; justify-content:flex-end}
@media (max-width:700px){.section-head > .btns{margin-left:0; justify-content:flex-start}}
.helpline.sp-help{background:var(--slate); color:#fff} .helpline.sp-help span{color:rgba(255,255,255,.88)}
.mf-hero .eyebrow,.po-hero .eyebrow,.bl-hero .eyebrow{color:var(--mint)}
/* 2.0: eyebrow colours (Logo Teal on light, mint on dark, white on SafeBAE Teal) */
main .eyebrow{color:var(--logo-teal)}
main :is(.band--slate,.band--deep,.band--logo,.mf-hero,.po-hero,.bl-hero,.tx-hero,.tx-who,.fq-ask__b,.po-zip,.ss-shop) .eyebrow{color:var(--mint)}
main .band--teal .eyebrow{color:#fff}
/* 2.0: marker word on custom dark heroes = mint ink */
:is(.mf-hero,.po-hero,.bl-hero,.tx-hero) .mk{background:none; color:var(--mint)}
.sp-hero{position:relative; overflow:hidden}
.sp-hero > .wrap{position:relative; z-index:1}
.ss-hero .wm-daisy,.fq-hero .wm-daisy{color:var(--logo-teal); opacity:.07}
'''

# =====================================================================
# 1. SURVIVOR SUPPORT
# =====================================================================
HOTLINES_SRC = [
  dict(name='love is respect', sub='National Teen Dating Abuse Hotline', desc='Free, confidential 24/7 peer support for teens experiencing dating abuse.',
       acts=[('Text', 'LOVEIS to 22522', 'sms:22522', '22522'), ('Call', '1-866-331-9474', 'tel:18663319474', '1-866-331-9474')],
       site=('loveisrespect.org', 'https://www.loveisrespect.org'), tags='text call dating', h24=True),
  dict(name='RAINN', sub='National Sexual Assault Hotline', desc='Free, confidential 24/7 support for survivors of sexual assault and their loved ones.',
       acts=[('Call', '800-656-HOPE (4673)', 'tel:18006564673', '800-656-4673'), ('Text', 'HOPE to 64673', 'sms:64673', '64673')],
       site=('rainn.org', 'https://rainn.org/help-and-healing/hotline/'), tags='call text assault', h24=True),
  dict(name='Trevor Lifeline', sub='Crisis support for LGBTQ+ youth', desc='24/7 crisis counseling for LGBTQ+ youth from The Trevor Project.',
       acts=[('Text', 'START to 678-678', 'sms:678678', '678-678'), ('Call', '1-866-488-7386', 'tel:18664887386', '1-866-488-7386')],
       site=('thetrevorproject.org', 'https://www.thetrevorproject.org/get-help/'), tags='text call lgbtq crisis', h24=True),
  dict(name='988 Suicide & Crisis Lifeline', sub='24/7 suicide & crisis support', desc='Free, confidential 24/7 support for anyone in suicidal crisis or emotional distress.',
       acts=[('Call or text', '988', 'tel:988', '988'), ('Chat', 'Online at 988lifeline.org', 'https://988lifeline.org', None)],
       site=('988lifeline.org', 'https://988lifeline.org'), tags='call text crisis', h24=True),
  dict(name='Crisis Text Line', sub='Free 24/7 crisis counseling', desc='Text with a live crisis counselor about anything. Free, 24/7, confidential.',
       acts=[('Text', 'HOME to 741741', 'sms:741741', '741741'), ('Español', 'HOLA to 741741', 'sms:741741', '741741')],
       site=('crisistextline.org', 'https://www.crisistextline.org/'), tags='text crisis', h24=True),
  dict(name='Take Back The Night', sub='Free legal hotline', desc='A global movement to end sexual violence and support survivors, including free legal assistance.',
       acts=[('Call', '567-742-8837 (567-SHATTER)', 'tel:15677428837', '567-742-8837'), ('Online', 'Or complete the online form', 'https://takebackthenight.org/legal-assistance/', None)],
       site=('takebackthenight.org', 'https://takebackthenight.org/legal-assistance/'), tags='call legal assault', h24=False),
  dict(name='SAMHSA National Helpline', sub='Mental health & substance use', desc='Free, confidential 24/7 treatment referrals for mental health and substance use (English & Spanish).',
       acts=[('Call', '1-800-662-HELP (4357)', 'tel:18006624357', '1-800-662-4357')],
       site=('samhsa.gov', 'https://www.samhsa.gov/find-help/helplines/national-helpline'), tags='call crisis', h24=True),
  dict(name='Raliance', sub='Local rape crisis center directory', desc='A national directory to find the rape crisis center nearest you.',
       acts=[('Online', 'Browse the directory online', 'https://www.raliance.org/rape-crisis-centers/', None)],
       site=('raliance.org', 'https://www.raliance.org/rape-crisis-centers/'), tags='local assault', h24=False),
]
HL_FILTERS = [('all', 'All lines'), ('text', 'Text'), ('call', 'Call'), ('dating', 'Dating abuse'), ('assault', 'Sexual assault'),
              ('lgbtq', 'LGBTQ+ youth'), ('crisis', 'Crisis & mental health'), ('legal', 'Legal help'), ('local', 'Local help')]

CHOKE_SIGNS = ['Passed out, even briefly, or can’t remember part of what happened', 'Breathing changes, or pain or difficulty swallowing',
               'A hoarse, raspy or deeper voice, or trouble speaking', 'Neck pain or tenderness, or a mark or bruise on your neck',
               'Vision changes, ringing ears, or hearing changes', 'A headache, dizziness or lightheadedness',
               'Small red spots in your eyes or on your face', 'Lost bladder or bowel control']

PRACTICES = ['Re-affirm your self-worth', 'Practice mindfulness', 'Practice self care', 'Take the time you need to process',
             'Journal your thoughts', 'Express your feelings', 'Honor your needs', 'Forgive yourself', 'Reassure yourself',
             'Talk about your experiences', 'Focus on the present moment', 'Practice positive self talk']

WAYS = [('Start by believing.', 'The single best way to support a survivor is to believe them. Questioning their account, even out of shock, can be devastating and may keep them from ever opening up again.'),
        ('Listen more than you speak.', 'Show you’re engaged: make eye contact, don’t interrupt, and let them share as much or as little as they want. You don’t need details to be helpful. Never press for them.'),
        ('Validate their feelings.', 'If they minimize what happened (“other people have it worse”), gently remind them they’re allowed to be as upset as they need to be. No assault is “not bad enough” to matter.'),
        ('Meet immediate needs first.', 'Before processing emotions, make sure they feel physically safe and cared for. Something as simple as a glass of water, a snack, a cozy blanket, or asking if they want a hug can signal to their brain that they’re safe now.'),
        ('Let them lead.', 'Follow their choices about whether to report, who to tell, and how to cope. Reporting can be re-traumatizing, so never pressure them to. You can help them understand their options while respecting whatever they decide.')]
SAY = ['“I’m so sorry this happened to you.”', '“You are not alone. I know there are people that can help.”', '“How can I support you?”',
       '“It’s not your fault.”', '“I’m glad you felt safe to tell me so I can be here for you.”', '“You didn’t deserve that to happen to you.”']
DONT = ['“Why didn’t you just leave?”', '“Why were you there?”', '“If you kissed, you should have known something was going to happen.”',
        '“Were you drinking?”', '“What were you wearing?”', '“It’s going to be fine; just move on.”', '“If it was really a big deal, why didn’t you tell me sooner?”']

BS = 'https://bookshop.org/a/safebae/'
MEDIA = [
 ('books', 'Consent-themed picture books (children)', [
   ('Body Boundaries Make Me Stronger', 'Elizabeth Cole', 'https://www.goodreads.com/book/show/69706233'),
   ('C Is For Consent', 'Eleanor Morrison, illustrated by Faye Orlove', BS + '9780999890806'),
   ('Can I Give You A Squish?', 'Emily Neilson', BS + '9781984814777'),
   ('Consent Ninja', 'Mary Nhin', 'https://www.ninjalifehacks.tv/products/consent-ninja-paperback-book'),
   ('Don’t Hug Doug: (He Doesn’t Like It)', 'Carrie Finison, Daniel Wiseman', BS + '9781984813022'),
   ('Don’t Hug The Quokka!', 'Daniel Errico, Mia Powell', BS + '9781433837067'),
   ('Don’t Touch My Hair', 'Sharee Miller', BS + '9780316562584'),
   ('Hands Off, Harry!', 'Rosemary Wells', BS + '9780061921124'),
   ('Harrison P. Spader, Personal Space Invader', 'Christianne Jones, Cale Atkinson', BS + '9781515827238'),
   ('I Choose To Say No', 'Elizabeth Estrada', 'https://www.goodreads.com/en/book/show/59612653-i-choose-to-say-no'),
   ('Miles Is The Boss Of His Body', 'Samantha Kurtzman-Counter, Abbie Schiller, illustrated by Valentina Ventimiglia', BS + '9780989407137'),
   ('My Body Belongs To Me', 'Jill Starishevsky, illustrated by Angela Padrón', BS + '9798330921874'),
   ('We Ask Permission', 'Lydia Bowers, Isabel Muñoz', BS + '9781631986758'),
   ('Where Hands Go', 'Krystaelynne Sanders Diggs and Ananta Mohanta', 'https://ksdiggs.com/products/where-hands-go-an-introduction-to-safe-and-unsafe-touch'),
   ('Will Ladybug Hug?', 'Hilary Leung', BS + '9781338215601'),
   ('Yes! No!: A First Conversation About Consent', 'Megan Madison, Jessica Ralli, Isabel Roxas', BS + '9780593383322')]),
 ('docs', 'Documentaries', [
   ('A Thousand Girls Like Me', '', 'https://www.imdb.com/title/tt8804304/'), ('Allen v. Farrow', '', 'https://www.imdb.com/title/tt13990468/'),
   ('Aly Raisman: Darkness to Light', '', 'https://www.imdb.com/title/tt10098366/'), ('Athlete A', '', 'https://www.imdb.com/title/tt11905462/'),
   ('Audrie & Daisy', '', 'https://www.imdb.com/title/tt5278460/'), ('Dive', '', 'https://www.imdb.com/title/tt22656762/'),
   ('I Am Evidence', '', 'https://www.imdb.com/title/tt6794374/'), ('Jeffrey Epstein: Filthy Rich', '', 'https://www.imdb.com/title/tt12312250/'),
   ('On the Record', '', 'https://www.imdb.com/title/tt11394650/'), ('Phoenix Rising', '', 'https://www.imdb.com/title/tt17036612/'),
   ('Roll Red Roll', '', 'https://www.imdb.com/title/tt8092888/'), ('Surviving R. Kelly', '', 'https://www.imdb.com/title/tt8385496/'),
   ('The Hunting Ground', '', 'https://www.imdb.com/title/tt4185572/'), ('Untouchable', '', 'https://www.imdb.com/title/tt9358228/'),
   ('Victim/Suspect', '', 'https://www.imdb.com/title/tt24079788/'), ('What Haunts Us', '', 'https://www.imdb.com/title/tt6073760/')]),
 ('films', 'Films & TV (scripted)', [
   ('8th Grade', '', 'https://www.imdb.com/title/tt7014006/'), ('I May Destroy You', '', 'https://www.imdb.com/title/tt11204260/'),
   ('Moxie', '', 'https://www.imdb.com/title/tt6432466/'), ('Pink', '', 'https://www.imdb.com/title/tt5571734/'),
   ('Promising Young Woman', '', 'https://www.imdb.com/title/tt9620292/'), ('The Assistant', '', 'https://www.imdb.com/title/tt9000224/'),
   ('Unbelievable', '', 'https://www.imdb.com/title/tt7909970/')]),
 ('nonfiction', 'Nonfiction books & memoirs', [
   ('Talk To Your Boys', 'Joanna Schroeder and Christopher Pepper', BS + '9781523527311'),
   ('Abolition. Feminism. Now.', 'Angela Davis, Gina Dent, Erica Meiners, Beth Richie', BS + '9781642592580'),
   ('All About Love', 'Bell Hooks', BS + '9780060959470'),
   ('All Boys Aren’t Blue: A Memoir Manifesto', 'George M. Johnson', BS + '9781250895561'),
   ('Boys & Sex', 'Peggy Orenstein', BS + '9780062666987'),
   ('Catch and Kill', 'Ronan Farrow', BS + '9780316486644'),
   ('Consent on Campus: A Manifesto', 'Donna Freitas', BS + '9780190671150'),
   ('Credible', 'Deborah Tuerkheimer', BS + '9780063585195'),
   ('Even if You’re Broken', 'Katie Rose Guest Pryal', 'https://bluecrowpublishing.com/team/even-if-youre-broken-essays-on-sexual-assault-and-metoo/'),
   ('For the Love of Men: From Toxic to a More Mindful Masculinity', 'Liz Plank', BS + '9781250757203'),
   ('Girls & Sex', 'Peggy Orenstein', BS + '9780062209740'),
   ('I’m Glad My Mom Died', 'Jennette McCurdy', BS + '9781982185831'),
   ('In the Dreamhouse', 'Carmen Maria Machado', BS + '9781644450383'),
   ('Is Rape a Crime?: A Memoir, an Investigation, and a Manifesto', 'Michelle Bowdler', BS + '9781250255761'),
   ('Know My Name: A Memoir', 'Chanel Miller', BS + '9780735223721'),
   ('Man Enough', 'Justin Baldoni', BS + '9780063055605'),
   ('Missoula: Rape and the Justice System in a College Town', 'Jon Krakauer', BS + '9780804170567'),
   ('Not That Bad', 'Roxane Gay', BS + '9780062413512'),
   ('Notes on a Silencing: A Memoir', 'Lacy Crawford', BS + '9780316491532'),
   ('Roll Red Roll: Rape, Power, and Football in the American Heartland', 'Nancy Schwartzman', BS + '9780306924361'),
   ('Sexual Citizens', 'Jennifer Hirsch, Shamus Khan', BS + '9781324001706'),
   ('Sexual Justice', 'Alexandra Brodsky', BS + '9781250839367'),
   ('She Said', 'Jodi Kantor, Megan Twohey', BS + '9780525560364'),
   ('South of Forgiveness', 'Thordis Elva, Tom Stranger', BS + '9781510730014'),
   ('The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma', 'Bessel Van Der Kolk, MD', BS + '9780143127741'),
   ('The Macho Paradox: Why Some Men Hurt Women and How All Men Can Help', 'Jackson Katz', BS + '9781402204012'),
   ('The Moment: Standing Up to Bill Cosby, Speaking Up for Women', 'Andrea Constand', 'https://www.penguinrandomhouse.com/books/646293/the-moment-by-andrea-constand/'),
   ('The Purity Myth', 'Jessica Valenti', BS + '9781580053143'),
   ('The Revolution Starts at Home', 'Ching-in Chen, Jai Dulani, Leah Lakshmi Piepzna-Samarasinha', BS + '9781849352628'),
   ('The Truth Will Set You Free But First It’ll Piss You Off!', 'Gloria Steinem', BS + '9780593132685'),
   ('Unbound: My Story of Liberation and the Birth of the Me Too Movement', 'Tarana Burke', BS + '9781250621740'),
   ('Unslut: A Diary and a Memoir', 'Emily Lindin', BS + '9781942186007'),
   ('Women Don’t Owe You Pretty', 'Florence Given', BS + '9781524857561')]),
 ('ya', 'Young adult fiction', [
   ('All Girls', 'Emily Layden', BS + '9781250751126'),
   ('All the Rage', 'Courtney Summers', 'https://us.macmillan.com/books/9781250069153/alltherage/'),
   ('Asking For It', 'Louise O’Neill', 'https://uk.bookshop.org/p/books/asking-for-it-louise-o-neill/199196a1adfc0bbf?ean=9781784293208'),
   ('Beartown', 'Fredrik Backman', BS + '9781501160776'),
   ('Bitter End', 'Jennifer Brown', BS + '9780316086967'),
   ('Breaking Beautiful', 'Jennifer Shaw Wolf', 'https://www.goodreads.com/book/show/10914560-breaking-beautiful'),
   ('Dreamland', 'Sarah Dessen', BS + '9780142401750'),
   ('Exit, Pursued by a Bear', 'E.K. Johnston', 'https://www.penguinrandomhouse.com/books/529826/exit-pursued-by-a-bear-by-ek-johnston/'),
   ('Fault Line', 'Christa Desir', BS + '9781442460720'),
   ('Finnikin of the Rock', 'Melina Marchetta', 'https://www.goodreads.com/book/show/4932435-finnikin-of-the-rock'),
   ('If You Could Be Mine', 'Sara Farizan', BS + '9781616204556'),
   ('Inexcusable', 'Chris Lynch', BS + '9781481432023'),
   ('I’ll Meet You There', 'Heather Demetrios', BS + '9781250080073'),
   ('Lily and Taylor', 'Elise Moser', 'https://houseofanansi.com/products/lily-and-taylor'),
   ('My Life Next Door', 'Huntley Fitzpatrick', BS + '9780142426043'),
   ('My Sister, The Serial Killer', 'Oyinkan Braithwaite', BS + '9780525564201'),
   ('Pointe', 'Brandy Colbert', BS + '9780147514417'),
   ('Queenie', 'Candice Carty Williams', BS + '9781501196027'),
   ('Speak', 'Laurie Halse Anderson', BS + '9780312674397'),
   ('The Dangerous Art of Blending In', 'Angelo Surmelis', BS + '9780062659019'),
   ('The Miseducation of Cameron Post', 'Emily M. Danforth', BS + '9780062020574'),
   ('The Young Elites', 'Marie Lu', BS + '9780147511683'),
   ('Where the Stars Still Shine', 'Trish Doller', 'https://www.goodreads.com/book/show/15826648-where-the-stars-still-shine')]),
 ('pods', 'Podcasts & alternative media', [
   ('Dear Katie Podcast', 'Katie Koestner', 'https://katiekoestner.com/podcast/'),
   ('Man Enough', 'Justin Baldoni, Liz Plank, Jamey Heath', 'https://manenough.com/podcast/'),
   ('Your Friend is Accused of SA, Now What?', 'Teenager Therapy', 'https://open.spotify.com/episode/4G1sLBqWPcyOfv5m8tFczP'),
   ('Unscrewed', 'Jaclyn Friedman', 'https://podcasts.apple.com/us/podcast/unscrewed/id580230127'),
   ('Self-Compassion: The Proven Power of Being Kind to Yourself', 'Kristin Neff', BS + '9780061733529'),
   ('You Throw Like a Girl', 'Don McPherson', 'https://www.akashicbooks.com/catalog/you-throw-like-a-girl/')]),
]


def src_label(u):
    if 'bookshop.org' in u: return 'Bookshop'
    if 'imdb.com' in u: return 'IMDb'
    if 'goodreads.com' in u: return 'Goodreads'
    if 'spotify.com' in u: return 'Spotify'
    if 'apple.com' in u: return 'Apple'
    if 'penguinrandomhouse' in u or 'macmillan' in u or 'akashic' in u or 'bluecrow' in u or 'houseofanansi' in u: return 'Publisher'
    return 'Website'


OC1 = [('offcampusp11', 'Let’s talk about Off Campus', 'Let’s talk about Off Campus: models of consent and healthy sexual relationships. Trigger warning: mention of sexual assault.'),
       ('offcampusp12', 'Based on Elle Kennedy’s bestselling series', 'Based on Elle Kennedy’s bestselling series, Off Campus will premiere on Prime Video on May 13th. The first season will be based on the first book in the series, The Deal.'),
       ('offcampusp13', 'Hannah Wells is a survivor of sexual assault', 'Hannah Wells, the main character, is a survivor of sexual assault. Hannah (played by Ella Bright) is a resilient character, but she carries a lot of baggage, especially when it comes to sex. Quote from Ella Bright in a Teen Vogue interview.'),
       ('offcampusp14', '“Sex is all about trust.”', '“Sex is all about trust. Even if you don’t love the other person, even if it’s just a hookup, it still takes a serious amount of trust to open yourself up and let yourself go to that vulnerable place, you know?” Garrett Graham, The Deal by Elle Kennedy.'),
       ('offcampusp15', 'What consent looks like', 'Throughout the book, Hannah and Garrett show us what consent looks like and the importance of being in-tune with your partner. He takes things slow, asks for verbal consent and continuously checks in.'),
       ('offcampusp16', 'How partners can help', '“Partners can help by practicing clear, proactive communication that affirms the survivor’s experience, articulates the boundaries of the relationship, and offers a willingness to be patient.” CAASE.'),
       ('offcampusp17', 'Tips for a healthy sexual relationship', 'Some tips for building a healthy sexual relationship: figure out what your boundaries are and talk about them with your partner; check in throughout; express your needs and wants; look and listen for non-verbal cues.')]
OC2 = [('offcampusp21', 'Green flags from Off Campus, season 1', 'Green flags from Off Campus, season 1. Warning: spoilers.'),
       ('offcampusp22', 'Green flag 1: “Consent is key.”', 'Green flag 1. “Trust. That’s it. She’s just got to feel completely safe. Like, completely relaxed. But consent is key. And she can’t consent if she doesn’t feel safe.” Dean, episode 4.'),
       ('offcampusp23', 'Green flag 2: “Not until you want me to.”', 'Green flag 2. Hannah: “Uh, you don’t need to turn around. You’re about to see me naked.” Garrett: “Yeah, but not until you want me to.”'),
       ('offcampusp24', 'Green flag 3: He notices she’s nervous', 'Green flag 3. Garrett notices Hannah is nervous. He gives her something more comfortable to wear. He dances with her to get the nerves out.'),
       ('offcampusp25', 'Green flag 4: He reads her cues and stops', 'Green flag 4. When they’re about to have sex, Garrett reads Hannah’s non-verbal cues and can tell that she’s not fully comfortable. So, he stops. He reminds her she doesn’t have to do this, showing respect for her decisions.'),
       ('offcampusp26', 'Green flag 5: A safe place to open up', 'Green flag 5. Hannah being a safe place for Garrett to show emotion and open up about his dad.'),
       ('offcampusp27', '“A healthy sex life is so important.”', '“I think being able to tell a story of someone who has dealt with sexual assault and can still have a romance and a healthy sex life is so important.” Louisa Levy, Off Campus showrunner.')]

SS_CSS = '''
.ss-hero{background:var(--aqua); color:var(--slate); position:relative; overflow:hidden}
.ss-hero__grid{display:grid; grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(44px,6vw,84px)}
.ss-hero .crumbs{color:var(--ink-soft)} .ss-hero .crumbs a{color:var(--logo-teal)}
.ss-hero .eyebrow{color:var(--logo-teal)}
.ss-hero h1{font-size:clamp(2.7rem,6.2vw,5.4rem); font-stretch:116%; font-weight:850; line-height:.95; letter-spacing:-.02em; color:var(--logo-teal); margin:0 0 .3em}
.ss-hero .lede{color:var(--slate); max-width:none}
.ss-hero__photo{position:relative}
.ss-hero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.ss-hero__photo .sticker{position:absolute; left:-12px; bottom:24px}
.ss-bubble{position:absolute; margin:0; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(.98rem,1.4vw,1.18rem); line-height:1.2; padding:12px 16px; border-radius:18px; box-shadow:var(--shadow-soft); animation:sb-rise .9s .5s var(--ease) both}
.ss-bubble--a{right:-14px; top:-20px; background:#fff; color:var(--logo-teal); border-bottom-right-radius:4px}
.ss-bubble--b{right:8%; bottom:-22px; background:var(--slate); color:#fff; border-bottom-left-radius:4px; animation-delay:.8s}
.ss-bubble::after{content:""; position:absolute; width:14px; height:14px; background:inherit; bottom:-6px; transform:rotate(45deg)}
.ss-bubble--a::after{right:22px} .ss-bubble--b::after{left:22px}
@media (max-width:860px){.ss-hero__grid{grid-template-columns:1fr} .ss-hero__photo{max-width:520px; margin:18px 0 22px} .ss-hero__photo .sticker{left:10px} .ss-bubble--a{right:6px} .ss-bubble--b{right:auto; left:14px}}
@media (max-width:560px){.ss-hero__photo .sticker{display:none}}
@media (max-width:520px){.ss-tattoo{grid-template-columns:64px minmax(0,1fr) auto; gap:12px} .ss-tattoo img{width:64px; height:64px}}
.ss-hl-head{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:20px 48px; align-items:end; margin-bottom:26px}
.ss-hl-head p.lede{color:rgba(255,255,255,.85); margin:0}
.ss-911{display:flex; gap:12px; align-items:center; background:var(--coral); color:var(--slate); border-radius:12px; padding:14px 18px; font-weight:700; line-height:1.35}
.ss-911 b{font-family:var(--display); font-stretch:115%; font-weight:900; font-size:1.7rem; line-height:1}
@media (max-width:860px){.ss-hl-head{grid-template-columns:1fr}}
.ss-filter{margin:0 0 20px}
.ss-filter__count{font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--aqua); margin:0 0 12px}
.ss-lines{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.ss-line{display:flex; flex-direction:column; gap:8px; padding:20px; border-radius:14px; background:rgba(255,255,255,.05); border:1px solid var(--line-dark); min-width:0}
.ss-line[hidden]{display:none}
.ss-line__top{display:flex; justify-content:space-between; gap:10px; align-items:flex-start}
.ss-line h3{font-size:1.3rem; margin:0; color:#fff}
.ss-line__top .chip{background:var(--mint); flex:none}
.ss-line__sub{font-family:var(--mono); font-size:.68rem; letter-spacing:.08em; text-transform:uppercase; color:var(--mint); margin:0; font-weight:600}
.ss-line__desc{font-size:.9rem; color:rgba(255,255,255,.8); margin:0; line-height:1.45}
.ss-acts{display:grid; gap:10px; margin-top:4px}
.ss-act small{display:block; font-family:var(--mono); font-size:.64rem; letter-spacing:.1em; text-transform:uppercase; color:rgba(255,255,255,.62); margin-bottom:4px}
.ss-act .copy{display:flex; width:100%; justify-content:space-between; gap:8px; font-size:.94rem; background:#fff; border:0; padding:7px 7px 7px 12px}
.ss-act .copy a{text-decoration:none; color:var(--slate); min-width:0; overflow-wrap:anywhere}
.ss-act .copy button{flex:none}
.ss-act__link{color:var(--aqua)!important; font-weight:700; text-decoration:underline; text-decoration-color:var(--mint); text-underline-offset:3px}
.ss-line__site{margin-top:auto; padding-top:8px; font-weight:700; font-size:.86rem; color:var(--aqua)!important; text-decoration:none}
.ss-line__site:hover{color:var(--mint)!important}
@media (max-width:1100px){.ss-lines{grid-template-columns:repeat(2,minmax(0,1fr))}} @media (max-width:560px){.ss-lines{grid-template-columns:1fr}}
.ss-choke{display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:18px clamp(24px,4vw,48px); margin-top:18px; padding:clamp(20px,3vw,32px); border-radius:var(--r-xl); background:#fff; color:var(--slate); border-top:6px solid var(--coral)}
.ss-choke__tag{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--logo-teal); margin:0 0 8px}
.ss-choke h3{font-size:clamp(1.5rem,2.4vw,2rem); margin:0 0 .35em; color:var(--slate)}
.ss-choke__head > p{margin:0 0 12px}
.ss-choke__say{display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 8px; padding:12px 14px; border-radius:12px; background:var(--aqua); font-size:.92rem}
.ss-choke__say b{font-family:var(--display); font-stretch:110%; font-weight:900; font-size:1.3rem}
.ss-choke__signs{list-style:none; padding:0; margin:0; display:grid; grid-template-columns:1fr 1fr; gap:8px; align-content:start}
.ss-choke__signs li{margin:0; padding:10px 12px 10px 30px; border-radius:12px; background:var(--mist); font-size:.9rem; font-weight:600; line-height:1.35; position:relative}
.ss-choke__signs li::before{content:""; position:absolute; left:12px; top:16px; width:8px; height:8px; border-radius:50%; background:var(--coral)}
.ss-choke__911{grid-column:1/-1; margin:0; padding-top:14px; border-top:1px solid var(--line); font-size:.92rem}
@media (max-width:900px){.ss-choke{grid-template-columns:1fr}} @media (max-width:520px){.ss-choke__signs{grid-template-columns:1fr}}
.ss-heal{display:grid; grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr); gap:clamp(28px,5vw,64px); align-items:stretch}
.ss-tattoo{display:grid; grid-template-columns:92px minmax(0,1fr) auto; gap:16px; align-items:center; margin-top:24px; padding:12px 18px 12px 12px; border-radius:var(--r-xl); border:1px solid var(--line); background:var(--mist); text-decoration:none; color:var(--slate); transition:box-shadow .25s var(--ease), transform .25s var(--ease)}
.ss-tattoo:hover{box-shadow:var(--shadow-soft); transform:translateY(-2px)}
.ss-tattoo img{width:92px; height:92px; object-fit:cover; border-radius:14px}
.ss-tattoo small{display:block; font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600}
.ss-tattoo b{display:block; font-family:var(--display); font-stretch:108%; font-size:1.15rem; line-height:1.15}
.ss-tattoo span span{display:block; font-size:.9rem; color:var(--ink-soft); line-height:1.4; margin-top:2px}
.ss-tattoo i{font-style:normal; font-weight:800; width:32px; height:32px; border-radius:50%; display:grid; place-items:center; background:var(--aqua); color:var(--logo-teal)}
.ss-practice{background:var(--slate); color:#fff; border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); display:flex; flex-direction:column}
.ss-practice h3{color:#fff; margin-bottom:.3em}
.ss-practice > p{color:rgba(255,255,255,.8); margin:0}
.ss-tiles{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-auto-rows:1fr; gap:8px; margin:18px 0; flex:1}
.ss-tiles button{font:inherit; text-align:left; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:.98rem; line-height:1.15; padding:14px; border-radius:10px; border:1.5px solid var(--line-dark); background:rgba(255,255,255,.04); color:#fff; cursor:pointer; min-height:74px; transition:background .25s, color .25s, border-color .25s, transform .25s}
.ss-tiles button:hover{border-color:var(--mint)}
.ss-tiles button[aria-pressed="true"]{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.ss-tiles button.pick{transform:scale(1.04); box-shadow:0 0 0 4px rgba(21,255,200,.35)}
.ss-pick{display:flex; flex-wrap:wrap; gap:12px 16px; align-items:center}
.ss-pick output{font-weight:700; color:var(--mint)}
@media (max-width:860px){.ss-heal{grid-template-columns:1fr}} @media (max-width:520px){.ss-tiles{grid-template-columns:1fr 1fr}}
.ss-now{display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center; justify-content:space-between; margin-top:22px; padding:16px 18px; border-radius:12px; background:var(--slate); color:#fff}
.ss-now b{font-family:var(--display); font-stretch:106%}
.ss-now strong{color:var(--mint)}
.ss-tell{display:grid; grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr); gap:clamp(28px,5vw,72px); align-items:start}
.ss-tell__head{position:sticky; top:104px}
.ss-tell__head .lede{font-weight:600; color:rgba(255,255,255,.9)}
.ss-ways{border-top:1px solid var(--line-dark)}
.ss-way{display:grid; grid-template-columns:minmax(0,210px) minmax(0,1fr); gap:20px; padding:20px 0; border-bottom:1px solid var(--line-dark)}
.ss-way b{font-family:var(--display); font-stretch:110%; font-weight:800; font-size:1.35rem; line-height:1.1; color:var(--mint)}
.ss-way p{margin:0; color:rgba(255,255,255,.86)}
@media (max-width:860px){.ss-tell{grid-template-columns:1fr} .ss-tell__head{position:static}} @media (max-width:560px){.ss-way{grid-template-columns:1fr; gap:6px}}
.ss-say{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; align-items:stretch}
.ss-say__col{border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); min-width:0}
.ss-say__col--do{background:var(--mint); color:var(--slate)}
.ss-say__col--dont{background:#fff; border:1px solid var(--line); color:var(--slate)}
.ss-say h3{margin:0}
.ss-say__col > small{display:block; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; margin-bottom:6px; color:var(--logo-teal)}
.ss-say ul{list-style:none; padding:0; margin:16px 0 0; display:grid; gap:8px}
.ss-say li{position:relative; margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:1.1rem; line-height:1.3; padding:12px 14px 12px 44px; border-radius:10px}
.ss-say__col--do li{background:rgba(255,255,255,.6)}
.ss-say__col--do li::before{content:""; position:absolute; left:17px; top:15px; width:8px; height:14px; border-right:3px solid var(--slate); border-bottom:3px solid var(--slate); transform:rotate(45deg)}
.ss-say__col--dont li{background:var(--mist); color:var(--ink-soft)}
.ss-say__col--dont li::before,.ss-say__col--dont li::after{content:""; position:absolute; left:14px; top:22px; width:16px; height:3px; border-radius:2px; background:var(--ink-soft); transform:rotate(45deg)}
.ss-say__col--dont li::after{transform:rotate(-45deg)}
@media (max-width:760px){.ss-say{grid-template-columns:1fr}}
.ss-print{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:18px; align-items:center; margin-top:16px; padding:14px 18px 14px 14px; border-radius:14px; background:#fff; border:1px solid var(--line)}
.ss-print button{border:0; padding:0; background:none; cursor:zoom-in}
.ss-print img{width:110px; border-radius:6px; box-shadow:0 10px 24px -14px rgba(29,65,78,.6)}
.ss-print b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.1rem}
.ss-print span{color:var(--ink-soft); font-size:.92rem}
@media (max-width:640px){.ss-print{grid-template-columns:auto minmax(0,1fr)} .ss-print .btns{grid-column:1/-1}}
.ss-gal{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.ss-gal button{position:relative; border:0; padding:0; background:#fff; border-radius:14px; cursor:zoom-in; aspect-ratio:3/4; display:block; overflow:hidden; box-shadow:0 14px 30px -20px rgba(29,65,78,.6)}
.ss-gal img{position:absolute; left:10px; top:10px; width:calc(100% - 20px); height:calc(100% - 20px); object-fit:contain; transition:transform .35s}
.ss-gal button:hover img{transform:scale(1.03)}
@media (max-width:860px){.ss-gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ss-media{display:grid; grid-template-columns:minmax(0,.72fr) minmax(0,1.28fr); gap:clamp(28px,5vw,64px); align-items:start}
.ss-media__side{position:sticky; top:104px}
.ss-shop{margin-top:22px; padding:20px; border-radius:14px; background:var(--slate); color:#fff}
.ss-shop p{color:rgba(255,255,255,.86); margin:0 0 14px}
.ss-count{display:inline-block; vertical-align:3px; margin-left:8px; font-family:var(--mono); font-size:.68rem; letter-spacing:.06em; font-weight:600; background:var(--aqua); color:var(--slate); padding:3px 8px; border-radius:4px; font-stretch:100%}
.ss-books{list-style:none; padding:0; margin:0; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:0 24px}
.ss-books li{margin:0; border-top:1px solid var(--line)}
.ss-books a{display:grid; grid-template-columns:minmax(0,1fr) auto; gap:2px 12px; padding:10px 2px; text-decoration:none; color:var(--slate); align-items:center}
.ss-books b{font-weight:700; font-size:.95rem; line-height:1.3}
.ss-books small{grid-column:1; color:var(--ink-soft); font-size:.82rem; line-height:1.3}
.ss-books em{grid-row:1 / span 2; grid-column:2; font-style:normal; font-family:var(--mono); font-size:.6rem; letter-spacing:.08em; text-transform:uppercase; color:var(--logo-teal); border:1px solid currentColor; border-radius:4px; padding:2px 5px; white-space:nowrap}
.ss-books a:hover b{color:var(--teal); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px}
@media (max-width:860px){.ss-media{grid-template-columns:1fr} .ss-media__side{position:static}} @media (max-width:560px){.ss-books{grid-template-columns:1fr}}
.ss-oc{display:grid; grid-template-columns:minmax(0,.86fr) minmax(0,1fr) minmax(0,1fr); gap:clamp(18px,3vw,34px); align-items:start}
.ss-oc__set > p{display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; align-items:baseline; margin:0 0 10px}
.ss-oc__set b{font-family:var(--display); font-stretch:106%; font-size:1.08rem; line-height:1.2}
.ss-oc__set .chip{background:var(--mint)}
.ss-oc__intro p{color:rgba(255,255,255,.9)} .ss-oc__set b{color:#fff}
@media (max-width:1000px){.ss-oc{grid-template-columns:1fr 1fr} .ss-oc__intro{grid-column:1/-1}} @media (max-width:640px){.ss-oc{grid-template-columns:1fr}}
'''


def survivor_support():
    filt = ''.join(f'<button type="button" data-f="{k}" aria-pressed="{str(k == "all").lower()}">{esc(l)}</button>' for k, l in HL_FILTERS)
    cards = []
    for h in HOTLINES_SRC:
        acts = []
        for label, disp, href, cp in h['acts']:
            if cp:
                acts.append(f'<div class="ss-act"><small>{esc(label)}</small><span class="copy"><a href="{esc(href)}">{esc(disp)}</a><button type="button" data-copy="{esc(cp)}" aria-label="Copy {esc(cp)}">Copy</button></span></div>')
            else:
                acts.append(f'<div class="ss-act"><small>{esc(label)}</small>{a(esc(disp), href, "ss-act__link")}</div>')
        chip = '<span class="chip">24/7</span>' if h['h24'] else ''
        cards.append(f'''<article class="ss-line" data-tags="{h['tags']}"><div class="ss-line__top"><h3>{esc(h['name'])}</h3>{chip}</div>
<p class="ss-line__sub">{esc(h['sub'])}</p><p class="ss-line__desc">{esc(h['desc'])}</p><div class="ss-acts">{''.join(acts)}</div>
{a(esc(h['site'][0]) + ' &#8599;', h['site'][1], 'ss-line__site')}</article>''')

    tiles = ''.join(f'<button type="button" aria-pressed="false">{esc(p)}</button>' for p in PRACTICES)
    ways = ''.join(f'<div class="ss-way"><b>{esc(t)}</b><p>{esc(d)}</p></div>' for t, d in WAYS)
    say = ''.join(f'<li>{esc(s)}</li>' for s in SAY)
    dont = ''.join(f'<li>{esc(s)}</li>' for s in DONT)

    gal_items = [('healing-from-trauma-3', 'Healing from a traumatic relationship', 'Poster: Healing from a traumatic relationship. Re-affirm your self-worth, practice mindfulness, practice self care, take the time you need to process, journal your thoughts, express your feelings, honor your needs, forgive yourself, reassure yourself, talk about your experiences, focus on the present moment, practice positive self talk.'),
                 ('everyone-can-do-something-1', 'No one can do everything, but everyone can do something', 'Poster: No one can do everything but everyone can do something. End rape culture.'),
                 ('relationships-4', 'What goes into a healthy relationship?', 'Poster: What goes into a healthy relationship? Equality at the center, surrounded by nonviolence, respect, trust, good communication, honesty, healthy boundaries and more.'),
                 ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships', 'Poster comparing healthy and unhealthy relationship behaviors.')]
    gal = ''.join(f'<button type="button" data-src="{imgsrc(n)}" data-cap="{esc(c)}">{img(n, alt)}</button>' for n, c, alt in gal_items)

    accs = []
    for i, (k, title, items) in enumerate(MEDIA):
        lis = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener"><b>{esc(t)}</b>{f"<small>{esc(by)}</small>" if by else ""}<em>{src_label(u)}</em></a></li>' for t, by, u in items)
        accs.append(f'<details{" open" if i == 0 else ""}><summary>{esc(title)} <span class="ss-count">{len(items)}</span></summary><div class="acc__body"><ul class="ss-books">{lis}</ul></div></details>')

    body = f'''
<section class="ss-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap ss-hero__grid">
    <div class="rise">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Survivor Support', None))}
      <h1>Survivor support &amp; <span class="mk">healing</span></h1>
      <p class="lede">Healing after sexual violence is deeply personal, with no single path forward. Many survivors find strength in connection, whether with peers, supportive communities, or professionals.</p>
      <div class="btns">{btn('Talk to someone now', '#hotlines', 'coral', arrow=True)}{btn('When someone tells you', '#when-someone-tells-you', 'slate')}</div>
      {esc_note()}
    </div>
    <div class="ss-hero__photo">{img('safebae-5', 'Two young women leaning their heads together and smiling', loading='eager')}<span class="sticker">Free &amp; confidential</span>
      <p class="ss-bubble ss-bubble--a" aria-hidden="true">“It’s not your fault.”</p>
      <p class="ss-bubble ss-bubble--b" aria-hidden="true">“How can I support you?”</p></div>
  </div>
</section>

<section class="band band--slate" id="hotlines">
  <div class="wrap">
    <div class="ss-hl-head">
      <div><p class="eyebrow">8 free, confidential lines</p><h2>Talk to someone now</h2>
        <p class="lede">There are many resources to help find your local services. We recommend contacting your local rape crisis services to get recommendations for services close to you.</p></div>
      <p class="ss-911"><b>911</b><span>If you are in immediate danger, call 911.</span></p>
    </div>
    <div class="sp-chips ss-filter" role="group" aria-label="Filter hotlines">{filt}</div>
    <p class="ss-filter__count" id="ss-count" aria-live="polite">8 lines</p>
    <div class="ss-lines">{''.join(cards)}</div>
    <article class="ss-choke" id="strangled" aria-labelledby="ss-choke-h">
      <div class="ss-choke__head">
        <p class="ss-choke__tag">From Choking Hazard, SafeBAE’s campaign on sexual strangulation</p>
        <h3 id="ss-choke-h">If you were choked or strangled</h3>
        <p>Go to an ER today, even with no marks and even if you agreed to it, if you:</p>
        <p class="ss-choke__say"><span>At the front desk, say</span> <b>“I was strangled.”</b> <span>Not just “my throat hurts.”</span></p>
        <div class="btns">{btn('What to know about choking', 'choking-hazard.html', 'slate', 'sm', arrow=True)}</div>
      </div>
      <ul class="ss-choke__signs">{''.join(f'<li>{esc(x)}</li>' for x in CHOKE_SIGNS)}</ul>
      <p class="ss-choke__911"><b>Call 911</b> if someone is unconscious, has trouble breathing, has a swelling neck, seems confused, has one-sided weakness or numbness, has a seizure, or shows stroke signs. Symptoms can show up later: throat swelling can develop hours later, and a torn-artery stroke can occur days or weeks later.</p>
    </article>
  </div>
</section>

<section class="band band--paper" id="healing">
  <div class="wrap ss-heal">
    <div>
      <h2>Healing takes time, and support.</h2>
      <p class="lede">Connection with peers, supportive communities, or professionals can ease feelings of isolation, reduce guilt or shame, and provide tools for coping. Even when survivors understand they are not to blame, it often takes time and support to fully believe it.</p>
      <p>For some, reconnecting with their body and emotions may feel overwhelming. Some survivors experience disconnection or turn to risky behaviors to manage pain. While facing these feelings can be difficult, avoiding them can cause further harm. With compassionate support and mental health resources, survivors can begin to process trauma, reclaim safety, and move toward healing.</p>
      <div class="btns" style="margin-top:20px">{btn('Find a local rape crisis center', 'https://www.raliance.org/rape-crisis-centers/', 'slate')}<button class="btn btn--ghost" data-open-help type="button">All hotlines</button></div>
      <a class="ss-tattoo" href="fordaisy-tattoos.html">{img('fordaisy28', 'Daisy Coleman tattooing a client')}<span><small>#ForDaisy</small><b>Tattoos &amp; healing</b><span>SafeBAE co-founder Daisy Coleman was a tattoo artist. Some survivors describe tattoos as one path to reclaiming their bodies.</span></span><i aria-hidden="true">&rarr;</i></a>
    </div>
    <div class="ss-practice">
      <h3>Healing from a traumatic relationship</h3>
      <p>Small practices that can help. Tap the ones you want to try, or let us pick one for today.</p>
      <div class="ss-tiles" role="group" aria-label="Healing practices">{tiles}</div>
      <div class="ss-pick"><button class="btn btn--mint btn--sm" type="button" id="ss-pick">Pick one for me</button><output id="ss-today" aria-live="polite"></output></div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="dating">
  <div class="wrap split">
    <div>{yt('rIxB8vlmAjY', 'Intimacy & Dating After Sexual Assault', label='With Teen Vogue')}</div>
    <div>
      <p class="eyebrow">Film + teaching guide &middot; with <i>Teen Vogue</i></p>
      <h2>Dating after sexual assault</h2>
      <p>Relationships and intimacy after assault can bring new challenges. Survivors may face triggers that complicate dating, while partners may feel uncertain about how to provide support. To open space for these conversations, SafeBAE partnered with <i>Teen Vogue</i> to produce <a class="link" href="film-dating-after-sexual-assault.html">Dating After Sexual Assault</a>.</p>
      <p>The short video and teaching guide affirm that healing looks different for everyone and offer practical tools for navigating trust, communication, and boundaries, creating space for survivors and partners to explore healthy intimacy after trauma.</p>
      <div class="btns">{btn('Film + teaching guide', 'film-dating-after-sexual-assault.html', 'slate', arrow=True)}</div>
      <div class="ss-now"><span><b>If you’d like immediate support from a trained professional,</b> you can text <strong>LOVEIS</strong> to <strong>22522</strong>.</span><span class="copy"><span>22522</span><button type="button" data-copy="22522">Copy</button></span></div>
    </div>
  </div>
</section>

<section class="band band--slate" id="when-someone-tells-you">
  <div class="wrap ss-tell">
    <div class="ss-tell__head">
      <h2>When someone tells you they’ve been assaulted</h2>
      <p class="lede">Opening up about sexual violence takes tremendous courage. If someone chooses to share their experience with you, here’s how to show up for them.</p>
      <div class="btns">{btn('How to support a friend (FAQ)', 'faq.html#faq-healing', 'ghost')}</div>
    </div>
    <div class="ss-ways">{ways}</div>
  </div>
</section>

<section class="band band--mist band--tight" id="what-to-say">
  <div class="wrap">
    <div class="section-head"><div><h2>Words that help, and words that hurt</h2></div></div>
    <div class="ss-say">
      <div class="ss-say__col ss-say__col--do"><small>Try saying</small><h3>Words that help</h3><ul>{say}</ul></div>
      <div class="ss-say__col ss-say__col--dont"><small>Don’t say</small><h3>Words to avoid</h3><ul>{dont}</ul></div>
    </div>
    <div class="ss-print" data-gallery>
      <button type="button" data-src="{imgsrc('8x8-what-not-to-say-poster-pdf')}" data-cap="What to say vs. what not to say">{img('8x8-what-not-to-say-poster-pdf', 'Poster: What to say to a friend who shares they have been assaulted, versus what not to say')}</button>
      <div><b>Print it as a poster</b><span>These phrases as a free “What to say vs. what not to say” poster for classrooms, counseling offices, hallways and student spaces.</span></div>
      <div class="btns">{btn('Download (PDF)', WPU + '2025/08/8x8-what-not-to-say-poster.pdf', 'slate', 'sm')}</div>
    </div>
  </div>
</section>

<section class="band band--mint" id="shareable-graphics">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">4 graphics &middot; free to print</p><h2>Shareable graphics</h2></div><div class="btns">{btn('Download all posters (.zip)', POSTERS_ZIP, 'slate')}{btn('See every poster', 'posters.html', 'ghost', arrow=True)}</div></div>
    <div class="ss-gal" data-gallery>{gal}</div>
  </div>
</section>

<section class="band band--paper" id="media">
  <div class="wrap ss-media">
    <div class="ss-media__side">
      <p class="eyebrow">101 books, films &amp; podcasts</p>
      <h2>Survivor-centered media</h2>
      <div class="ss-shop"><p>You can support SafeBAE’s work by purchasing books from our digital bookshop.</p>{btn('SafeBAE on Bookshop.org', BOOKSHOP, 'mint', 'sm')}</div>
    </div>
    <div class="acc">{''.join(accs)}</div>
  </div>
</section>

<section class="band band--deep" id="off-campus">
  <div class="wrap ss-oc">
    <div class="ss-oc__intro">
      <p class="eyebrow">A recent favorite</p>
      <h2>Off Campus</h2>
      <p>Based on Elle Kennedy’s bestselling series, <i>Off Campus</i> follows Hannah Wells, a survivor of sexual assault, and Garrett Graham. The story models consent and healthy sexual relationships, from a partner who checks in to one who stops when she isn’t fully comfortable.</p>
      <p class="small" style="color:rgba(255,255,255,.75)">Tap a slide to enlarge it. The first set mentions sexual assault; the second contains spoilers for season one.</p>
    </div>
    <div class="ss-oc__set"><p><b>Let’s talk about Off Campus</b><span class="chip">Mentions SA</span></p>{player(OC1, 'Let’s talk about Off Campus: seven slides', 'sp-portrait')}</div>
    <div class="ss-oc__set"><p><b>Green flags from season 1</b><span class="chip">Spoilers</span></p>{player(OC2, 'Green flags from Off Campus season 1: seven slides', 'sp-portrait', interval=5600)}</div>
  </div>
</section>

<section class="band band--paper band--tight">
  <div class="wrap">
    <div class="section-head"><div><h2>More support and answers</h2></div></div>
    {next_cards([('Your rights', 'Title IX', 'What your school owes you, supportive measures, and who to talk to.', 'title-ix.html'),
                 ('Research', 'Myths & facts', 'Why survivors don’t report, and what the research actually says.', 'myths-facts.html'),
                 ('Answers', 'FAQ', 'Straight answers about consent, reporting, healing and more.', 'faq.html'),
                 ('Anonymous tool', 'Vibe Check', 'For a young person worried they, or a friend, crossed a line.', 'https://checkyourvibe.org/')])}
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  var f = document.querySelector('.ss-filter'), out = document.getElementById('ss-count');
  if(f){ var bs = f.querySelectorAll('button'), cards = document.querySelectorAll('.ss-line');
    bs.forEach(function(b){ b.addEventListener('click', function(){ var t = b.getAttribute('data-f'), n = 0;
      bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); });
      cards.forEach(function(c){ var on = t === 'all' || (' ' + c.getAttribute('data-tags') + ' ').indexOf(' ' + t + ' ') >= 0; c.hidden = !on; if(on) n++; });
      if(out) out.textContent = n + (n === 1 ? ' line' : ' lines'); }); }); }
  var tiles = document.querySelectorAll('.ss-tiles button'), today = document.getElementById('ss-today'), pk = document.getElementById('ss-pick');
  tiles.forEach(function(t){ t.addEventListener('click', function(){ t.setAttribute('aria-pressed', t.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); t.classList.remove('pick'); }); });
  if(pk) pk.addEventListener('click', function(){ var i = Math.floor(Math.random() * tiles.length); tiles.forEach(function(x){ x.classList.remove('pick'); }); var t = tiles[i]; t.classList.add('pick'); t.setAttribute('aria-pressed', 'true'); today.textContent = 'For today: ' + t.textContent + '.'; });
})();
</script>'''
    page('survivor-support.html', 'Survivor Support & Healing · SafeBAE',
         'Support resources for survivors and those helping them, including hotlines, healing tools, and guidance for when someone discloses assault.',
         body, active='resources', body_class='ss', head_extra=f'<style>{SP_CSS}{SS_CSS}</style>', scripts=js)


# =====================================================================
# 2. TITLE IX
# =====================================================================
TIMELINE = [
  ('1972', '1972', 'Title IX Enacted', 'Title IX of the Education Amendments of 1972 is signed into law, prohibiting sex-based discrimination in any education program or activity receiving federal financial assistance.'),
  ('1977', '1977', 'Alexander v. Yale', 'A group of students filed a lawsuit against Yale University, arguing that the university’s failure to address sexual harassment constituted a violation of Title IX. This was the first case to use Title IX to argue that sexual harassment is a form of sex discrimination.'),
  ('1992', '1992', 'Franklin v. Gwinnett County Public Schools', 'This landmark decision marked the first successful interpretation of Title IX to cover sexual harassment, significantly strengthening the law’s enforcement and protections against gender-based discrimination in educational settings.'),
  ('2011', '2011', 'The “Dear Colleague” Letter', 'The Obama administration’s Office for Civil Rights issues the “Dear Colleague” Letter, clarifying that sexual violence is a form of sexual harassment prohibited by Title IX and outlining schools’ responsibility to respond promptly and equitably to reports of sexual violence.'),
  ('2017', '2017', 'Rescission of 2011 Guidance', 'The 2011 guidance is rescinded by the Trump/DeVos administration, and interim guidance is provided, allowing schools more flexibility in handling sexual violence cases and decreasing protections for survivors.'),
  ('2020', '2020', 'The Trump/DeVos Title IX Rules', 'In May 2020, new Title IX regulations are published. These regulations require schools to follow specific procedures for investigating and adjudicating sexual harassment and assault cases, including live hearings and cross-examinations. These rules make it harder for survivors to get the support they need.'),
  ('2022', '2022', 'Proposed Title IX Rule', 'After over a year of pressure from organizers, the Biden administration proposes new changes to the Title IX regulations on June 23, 2022 (the 50th anniversary of Title IX) to better protect students and ensure fair processes. These changes aimed to address some of the criticisms of the 2020 rules.'),
  ('2024', '2024', 'Final Rule Update', 'New Title IX rules are finalized and released on April 19, 2024, and take effect August 1, 2024. These rules provided enhanced protections for students and survivors, including LGBTQ+ students and pregnant and postpartum students.'),
  ('Jan 2025', 'January 9, 2025', 'Vacatur and Post-Decision Status', 'A federal district court issues a decisive ruling that vacates the 2024 Final Rule in its entirety. The Department of Education has confirmed that the 2024 Title IX regulations and related resources are not effective in any jurisdiction, meaning the 2020 regulations are the rules schools must follow today.'),
  ('Jun 2026', 'June 16, 2026', 'Civil Rights Enforcement Moves to the DOJ', 'The U.S. Department of Education moves civil rights enforcement from OCR to the Department of Justice, shifting how harassment and discrimination complaints in K-12 schools and colleges are investigated and resolved, and making it even more confusing for students and families to understand where and how to seek justice.'),
  ('Today', 'Today', 'What Comes Next?', 'The future of Title IX and its enforcement at the federal level remains uncertain, and yet students still have the legal right to be protected in their schools.'),
]
RIGHTS = ['Your school is required by law to ensure your safety on campus.',
          'Your school is required to have established procedures for handling complaints of sexual discrimination, harassment, or violence.',
          'You have the right to report sexual harassment or assault to your school, and your school MUST take steps to ensure victims do not have to share space, such as classes, with their abuser.',
          'Your school should inform you of your right to counseling services and your right to make a report to law enforcement.',
          'Your school may NOT retaliate against someone filing a complaint and must keep the complainant safe from retaliatory harassment.',
          'Schools can NOT discourage you from continuing your education, and must provide reasonable accommodations for your safety.']
VIOLATION = ['the survivor experiences harassment during the reporting process',
             'the investigation isn’t prompt and impartial',
             'the survivor faces retaliation',
             'the school fails to provide reasonable accommodations or a no-contact order']
MEASURES = [
  ('Care & support', ['Referral to health services', 'Provision of resources for medical and/or psychological support or disability', 'Access to community resources', 'Referral to survivor advocate services']),
  ('Safety at school', ['School grounds-based no-contact orders', 'Imposition of interim suspension for the perpetrator', 'Limiting a perpetrator’s access to activities', 'Arranging cafeteria and study hall schedules']),
  ('Classes & schoolwork', ['Change in academic schedule', 'Change in course load, including reduced course load or alternative assignments', 'Academic support and tutoring', 'Option for independent study',
                            'Excused class absence for treatment, hospitalization, and medical or mental health conditions', 'Assurance that survivors will suffer no academic penalties for court or conduct proceedings',
                            'Retrospective withdrawal from classes', 'Immediate withdrawal from a class', 'Leave of absence from the institution']),
  ('Anything else', ['Any other reasonable safe forms of assistance and support as requested by the survivor to help them feel safe and supported']),
]
TELL_ME_LIES = [('1', 'Tell Me Lies… but not about Title IX', 'Tell Me Lies… but not about Title IX. A new season of Tell Me Lies is out, and sexual assault is a central plotline. We’re not doing a recap; we’re doing a reality check on what the show portrays.'),
                ('2', 'What happens in the show', 'Tell Me Lies is a Hulu drama set around a college friend group. This season includes a scene where Lucy is brought into an admin-style meeting with another student who was assaulted by the same person, and the conversation is framed like they need Lucy to “come forward” so the stories can corroborate each other.'),
                ('3', 'What the show portrays', 'What the show portrays: a surprise group meeting, an implied requirement that survivors corroborate each other, and admin-driven urgency over survivor choice.'),
                ('4', 'What Title IX is actually supposed to do', 'What Title IX is actually supposed to do: the school’s job starts with the Title IX Coordinator; supportive measures are offered immediately, even if no formal complaint is filed; privacy and confidentiality are built in; the complainant chooses whether to file a formal complaint; parties are handled separately and get written notice.'),
                ('5', 'What this storyline teaches viewers', 'What this storyline teaches viewers, and why it is harmful: four lies, including “you need another survivor to back you up” and “if you don’t do the formal process, nothing happens.”'),
                ('6', 'Real prevention starts here', 'When a show makes sexual assault a major storyline, it has a responsibility not to normalize a process that pressures survivors or makes reporting look like a trap. Real prevention starts with these conversations.')]
TIX_POSTS = [('Why Students Walk Out: The Westlake High Protest and the Power of Youth Activism', '2025-05-06', 'https://www.safebae.org/why-students-walk-out-the-westlake-high-protest-and-the-power-of-youth-activism/', 'blog-why-students-walk-out-the-westlake-high-prot'),
             ('A Future Without the Department of Education: What We Must Do Now', '2025-04-21', 'https://www.safebae.org/a-future-without-the-department-of-education-what-we-must-do-now/', 'blog-a-future-without-the-department-of-education'),
             ('In a Time of Federal Cutbacks, Students Are Demanding Consent Education—We Need to Keep Showing Up', '2025-01-31', 'https://www.safebae.org/in-a-time-of-federal-cutbacks-students-are-demanding-consent-education-we-need-to-keep-showing-up/', 'blog-in-a-time-of-federal-cutbacks-students-are-d')]
TIX_FAQ = 'https://www.safebae.org/what-is-title-ix-student-rights/'
_P = '<svg viewBox="0 0 24 40"><circle cx="12" cy="7" r="6"/><path d="M3 40V22a9 9 0 0 1 18 0v18z"/></svg>'
PEOPLE = ''.join(f'<i class="{"on" if k < 7 else ""}" style="--d:{k * 70}ms">{_P}</i>' for k in range(10))

TX_CSS = '''
.tx-hero{background:var(--logo-teal) var(--grain); color:#fff}
.tx-hero__grid{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,72px); align-items:center; padding-block:clamp(48px,6vw,92px)}
.tx-hero h1{font-size:clamp(4.2rem,12vw,10rem); font-stretch:125%; font-weight:900; line-height:.8; letter-spacing:-.03em; margin:0; text-transform:uppercase}
.tx-hero h1 > span{display:block; font-size:clamp(1.6rem,3.2vw,2.6rem); font-stretch:112%; letter-spacing:-.01em; line-height:1.05; margin-top:.35em; color:#fff}
.tx-hero .lede{color:rgba(255,255,255,.9); margin-top:24px; max-width:none}
.tx-hero__media{position:relative}
.tx-hero__photo{position:relative; margin-left:12%}
.tx-hero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.tx-hero__photo .sticker{position:absolute; right:-10px; top:18px}
.tx-law{position:relative; z-index:1; width:min(84%,500px); margin:-80px 0 0; background:var(--slate-deep); border-radius:var(--r-xl); padding:clamp(20px,2.6vw,32px); box-shadow:var(--shadow-soft); border-top:6px solid var(--mint)}
.tx-law small{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.tx-law blockquote{margin:10px 0 0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.02rem,1.5vw,1.25rem); line-height:1.35; text-wrap:pretty}
.tx-law blockquote::before{content:"\\201C"; display:block; font-size:3.4em; line-height:.55; color:var(--mint); font-stretch:125%; margin-bottom:.05em}
@media (max-width:900px){.tx-hero__grid{grid-template-columns:1fr}}
@media (max-width:560px){.tx-hero__photo{margin-left:0} .tx-law{width:auto; margin:-40px 10px 0}}
.tx-does{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px}
.tx-does > div{border-radius:var(--r-xl); padding:24px; background:var(--mist); border-top:6px solid var(--teal); min-width:0}
.tx-does > div:nth-child(2){border-color:var(--mint)} .tx-does > div:nth-child(3){border-color:var(--logo-teal)}
.tx-does b{display:block; font-family:var(--display); font-stretch:110%; font-size:1.45rem; line-height:1.1; color:var(--logo-teal); margin-bottom:8px}
.tx-does p{margin:0; color:var(--ink-soft)}
@media (max-width:860px){.tx-does{grid-template-columns:1fr}}
.tx-stat{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:clamp(18px,4vw,48px); align-items:center}
.tx-pict{display:flex; flex-direction:column; gap:10px}
.tx-stat b{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(4.4rem,10vw,8rem); line-height:.8; letter-spacing:-.03em}
.tx-people{display:flex; gap:5px}
.tx-people i{display:block; width:clamp(16px,2vw,24px)}
.tx-people svg{display:block; width:100%; fill:transparent; stroke:var(--slate); stroke-width:2.2}
.tx-people i.on svg{fill:var(--slate)}
.js .tx-people i.on svg{fill:transparent; transition:fill .4s var(--ease) var(--d)}
.js .tx-pict.seen .tx-people i.on svg{fill:var(--slate)}
.tx-stat p{font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.12rem,2vw,1.55rem); line-height:1.3; margin:0}
@media (max-width:860px){.tx-stat{grid-template-columns:1fr; gap:12px} .tx-stat .btn{justify-self:start}}
.tx-vq{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(20px,3vw,40px); align-items:stretch}
.tx-vq__vid{display:flex; flex-direction:column; justify-content:center}
@media (max-width:900px){.tx-vq{grid-template-columns:1fr}}
.tx-quiz{background:var(--mint); color:var(--slate); border-radius:var(--r-xl); padding:clamp(22px,3vw,36px); display:flex; flex-direction:column}
.tx-quiz h2{font-size:clamp(1.8rem,3vw,2.5rem); margin:0 0 .2em}
main .tx-quiz .eyebrow{color:var(--slate)}
.tx-prog{display:flex; gap:6px; margin:10px 0 22px}
.tx-prog span{flex:1; height:6px; border-radius:3px; background:rgba(29,65,78,.18); transition:background .3s}
.tx-prog span.done{background:var(--slate)}
.tx-step + .tx-step{margin-top:20px; padding-top:20px; border-top:1px solid rgba(29,65,78,.2)}
.js .tx-step{display:none; margin:0; padding:0; border:0} .js .tx-step.on{display:block; animation:txin .35s ease}
@keyframes txin{from{opacity:0; transform:translateY(8px)} to{opacity:1; transform:none}}
.tx-q{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:clamp(1.3rem,2.2vw,1.7rem); line-height:1.15; margin:0 0 16px}
.tx-choices{display:grid; grid-template-columns:1fr 1fr; gap:10px}
.tx-choices button{font:inherit; font-family:var(--display); font-weight:800; font-stretch:108%; font-size:1.15rem; padding:16px; border-radius:10px; border:2px solid var(--slate); background:#fff; color:var(--slate); cursor:pointer; transition:background .2s, color .2s}
.tx-choices button:hover{background:var(--slate); color:#fff}
.tx-unsure{margin-top:12px; font:inherit; font-weight:700; background:none; border:0; color:var(--slate); text-decoration:underline; text-underline-offset:3px; cursor:pointer; padding:4px 0}
.tx-help{margin-top:10px; background:rgba(255,255,255,.6); border-radius:10px; padding:14px 16px; font-size:.93rem; line-height:1.5}
.tx-res{background:#fff; border-radius:12px; padding:18px 20px}
.tx-res h3{font-size:clamp(1.4rem,2.4vw,1.9rem); margin:0 0 .35em}
.tx-res p{margin:0 0 14px}
.tx-res .btns{gap:8px}
.tx-tl__track{position:relative; display:grid; grid-template-columns:repeat(11,minmax(0,1fr)); gap:4px; margin-bottom:24px}
.tx-tl__line{position:absolute; left:4.5%; right:4.5%; top:19px; height:3px; background:var(--line-dark); border-radius:2px}
.tx-tl__line i{display:block; height:100%; width:0; background:var(--mint); transition:width .45s ease; border-radius:2px}
.tx-tl__track button{position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; gap:10px; background:none; border:0; color:rgba(255,255,255,.7); font:inherit; cursor:pointer; padding:4px 0 6px}
.tx-tl__track .dot{width:18px; height:18px; margin-top:8px; border-radius:50%; background:var(--slate); border:3px solid rgba(209,254,255,.45); transition:all .25s}
.tx-tl__track button:hover .dot{border-color:var(--mint)}
.tx-tl__track button.past .dot{border-color:var(--mint); background:var(--mint)}
.tx-tl__track button[aria-selected="true"] .dot{background:var(--mint); border-color:#fff; transform:scale(1.4)}
.tx-tl__track .lbl{font-family:var(--mono); font-size:.74rem; font-weight:600; letter-spacing:.03em; white-space:nowrap}
.tx-tl__track button[aria-selected="true"] .lbl{color:var(--mint)}
.tx-tl__panel{display:grid; grid-template-columns:minmax(0,.75fr) minmax(0,1.25fr); gap:clamp(20px,4vw,56px); align-items:center; padding:clamp(22px,3vw,40px); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark); min-height:250px}
.tx-tl__panel + .tx-tl__panel{margin-top:12px}
.js .tx-tl__panel{display:none; margin:0} .js .tx-tl__panel.on{display:grid; animation:txin .35s ease}
.tx-tl__panel .tx-tl__date{font-family:var(--display); font-weight:900; font-stretch:125%; font-size:clamp(3rem,7vw,6rem); line-height:.88; letter-spacing:-.02em; color:var(--mint); margin:0}
.tx-tl__panel .tx-tl__date--long{font-size:clamp(2rem,4vw,3.3rem); line-height:.95}
.tx-tl__panel h3{font-size:clamp(1.4rem,2.4vw,2rem); color:#fff}
.tx-tl__panel p{color:rgba(255,255,255,.86); margin:0}
.tx-tl__nav{display:flex; justify-content:space-between; align-items:center; gap:12px; margin-top:16px}
.tx-tl__nav button{font:inherit; font-weight:700; background:transparent; color:#fff; border:1.5px solid var(--line-dark); border-radius:999px; padding:8px 16px; cursor:pointer}
.tx-tl__nav button:hover{border-color:var(--mint); color:var(--mint)}
.tx-tl__n{font-family:var(--mono); font-size:.76rem; letter-spacing:.08em; color:var(--aqua)}
.tx-tl:not(.ready) .tx-tl__nav,.tx-tl:not(.ready) .tx-tl__track{display:none}
@media (max-width:860px){.tx-tl__track{display:flex; overflow-x:auto; gap:22px; padding:0 4px 8px; scrollbar-width:thin; scroll-snap-type:x proximity} .tx-tl__track button{flex:none; scroll-snap-align:center} .tx-tl__line{display:none} .tx-tl__panel{grid-template-columns:1fr; min-height:0}}
.tx-rights{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(24px,4vw,56px); align-items:stretch}
.tx-list{list-style:none; padding:0; margin:20px 0 0; display:grid; grid-template-columns:1fr 1fr; gap:10px}
.tx-list li{position:relative; margin:0; padding:16px 16px 16px 48px; border-radius:12px; background:var(--mist); font-weight:600; line-height:1.45; font-size:.96rem}
.tx-list li::before{content:""; position:absolute; left:16px; top:17px; width:22px; height:22px; border-radius:50%; background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%231d414e' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat}
.tx-who{background:var(--slate); color:#fff; border-radius:var(--r-xl); padding:clamp(22px,3vw,36px); display:flex; flex-direction:column}
.tx-who h3{color:#fff; font-size:clamp(1.5rem,2.4vw,2rem)}
.tx-who p{color:rgba(255,255,255,.88)}
.tx-who ul{margin:0 0 16px; padding-left:1.1em; color:rgba(255,255,255,.88)}
.tx-who li::marker{color:var(--mint)}
.tx-who .btns{margin-top:auto}
@media (max-width:960px){.tx-rights{grid-template-columns:1fr}} @media (max-width:620px){.tx-list{grid-template-columns:1fr}}
.tx-sm{display:grid; gap:14px; background:#fff; border-radius:var(--r-xl); padding:clamp(18px,3vw,30px); box-shadow:var(--shadow-soft)}
.tx-sm__grp{display:grid; grid-template-columns:170px minmax(0,1fr); gap:10px 20px; align-items:start; padding-bottom:14px; border-bottom:1px solid var(--line)}
.tx-sm__grp > b{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); padding-top:11px; font-weight:600}
.tx-sm__pills{display:flex; flex-wrap:wrap; gap:8px}
.tx-sm__pills button{font:inherit; font-size:.9rem; font-weight:600; text-align:left; line-height:1.3; padding:9px 14px 9px 38px; border-radius:22px; border:1.5px solid var(--line); background:var(--mist); color:var(--slate); cursor:pointer; position:relative; max-width:100%}
.tx-sm__pills button::before{content:""; position:absolute; left:13px; top:11px; width:15px; height:15px; border-radius:4px; border:2px solid var(--teal); background:#fff}
.tx-sm__pills button:hover{border-color:var(--teal)}
.tx-sm__pills button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.tx-sm__pills button[aria-pressed="true"]::before{background:var(--mint) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='%231d414e' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/11px no-repeat; border-color:var(--mint)}
.tx-sm__bar{display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; justify-content:space-between}
.tx-sm__bar output{font-family:var(--mono); font-size:.78rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-soft)}
.tx-sm textarea{width:100%; min-height:150px; font:inherit; font-size:.9rem; padding:12px; border-radius:10px; border:2px solid var(--teal)}
.tx-sm__note{margin:0; font-weight:700; padding:14px 16px; border-radius:12px; background:var(--aqua); line-height:1.45}
@media (max-width:700px){.tx-sm__grp{grid-template-columns:1fr; gap:8px} .tx-sm__grp > b{padding-top:0}}
.tx-more{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; margin-top:18px; align-items:stretch}
.tx-more > div{display:grid; grid-template-columns:auto minmax(0,1fr); gap:18px; align-items:center; background:#fff; border-radius:var(--r-xl); padding:16px 18px 16px 16px; border:1px solid var(--line)}
.tx-more img{width:150px; border-radius:10px}
.tx-more button.tx-zoom{border:0; padding:0; background:none; cursor:zoom-in}
.tx-more b{display:block; font-family:var(--display); font-stretch:106%; font-size:1.15rem; line-height:1.15; margin-bottom:4px}
.tx-more p{margin:0 0 10px; font-size:.92rem; color:var(--ink-soft)}
@media (max-width:860px){.tx-more{grid-template-columns:1fr}} @media (max-width:480px){.tx-more > div{grid-template-columns:1fr} .tx-more img{width:100%; max-width:240px}}
.tx-media{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,56px); align-items:center}
.tx-media .player{max-width:440px; margin-inline:auto; width:100%}
.tx-media__q{margin:18px 0; padding:16px 18px; border-left:4px solid var(--mint); background:rgba(255,255,255,.05); border-radius:0 12px 12px 0; color:rgba(255,255,255,.88); font-size:.98rem}
@media (max-width:860px){.tx-media{grid-template-columns:1fr}}
.tx-posts{margin-top:clamp(32px,4vw,48px); padding-top:clamp(24px,3vw,36px); border-top:1px solid var(--line-dark)}
.tx-posts .section-head h3{margin:0; color:#fff}
.tx-more2 .split{align-items:center}
.tx-better{color:var(--slate); font-weight:800; text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:3px; text-underline-offset:4px}
.tx-photo{position:relative}
.tx-photo img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.tx-photo .sticker{position:absolute; right:-8px; top:20px}
'''


def title_ix():
    tl_btns, tl_panels = [], []
    for i, (short, full, h, txt) in enumerate(TIMELINE):
        tl_btns.append(f'<button type="button" role="tab" id="tl-t{i}" aria-controls="tl-p{i}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}"><span class="dot"></span><span class="lbl">{esc(short)}</span></button>')
        long = ' tx-tl__date--long' if len(full) > 6 else ''
        tl_panels.append(f'<article class="tx-tl__panel{" on" if i == 0 else ""}" role="tabpanel" id="tl-p{i}" aria-labelledby="tl-t{i}"><p class="tx-tl__date{long}">{esc(full)}</p><div><h3>{esc(h)}</h3><p>{esc(txt)}</p></div></article>')
    rights = ''.join(f'<li>{esc(r)}</li>' for r in RIGHTS)
    viol = ''.join(f'<li>{esc(v)}</li>' for v in VIOLATION)
    sm = ''.join(f'<div class="tx-sm__grp"><b>{esc(g)}</b><div class="tx-sm__pills">' + ''.join(f'<button type="button" aria-pressed="false">{esc(x)}</button>' for x in items) + '</div></div>' for g, items in MEASURES)
    tml = [(n, c, alt) for n, c, alt in TELL_ME_LIES]
    posts = ''.join(post_card(*p) for p in TIX_POSTS)

    body = f'''
<section class="tx-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap tx-hero__grid">
    <div class="rise">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Title IX', None))}
      <h1>Title IX <span>Your <span class="mk">rights</span> at school</span></h1>
      <p class="lede">Title IX is a federal civil rights law that protects students from sex discrimination in schools and guarantees the right to an education free from harassment, assault, and inequity. Every student deserves to know these protections exist.</p>
      <div class="btns">{btn('Is my school covered?', '#covered', 'mint', arrow=True)}{btn('Supportive measures', '#supportive-measures', 'ghost')}</div>
    </div>
    <div class="tx-hero__media">
      <div class="tx-hero__photo">{img('img-2395', 'Two SafeBAE educators leading a session in a classroom', loading='eager')}<span class="sticker sticker--r">Know your rights</span></div>
      <figure class="tx-law"><small>Title IX of the Education Amendments of 1972</small>
        <blockquote>No person in the United States shall, on the basis of sex, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any education program or activity receiving Federal financial assistance.</blockquote></figure>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>So, what does it do?</h2></div></div>
    <div class="tx-does">
      <div><b>Prohibits discrimination</b><p>Title IX prohibits sex-based discrimination in any school or educational program that receives federal funding.</p></div>
      <div><b>Protects all students</b><p>Title IX protections apply to all students, regardless of gender identity or expression.</p></div>
      <div><b>Covers various issues</b><p>Title IX covers a wide range of issues, including sexual harassment, assault, and other forms of gender-based violence.</p></div>
    </div>
  </div>
</section>

<section class="band band--mint band--tight">
  <div class="wrap tx-stat"><div class="tx-pict" role="img" aria-label="7 out of 10 students"><b>70%</b><span class="tx-people" aria-hidden="true">{PEOPLE}</span></div><p>of students in SafeBAE’s national school climate survey said their school didn’t adequately teach their Title IX rights. It is important to know your rights in order to protect yourself or a friend.</p>{btn('Read the full answer', TIX_FAQ, 'slate', 'sm')}</div>
</section>

<section class="band band--slate" id="covered">
  <div class="wrap tx-vq">
    <div class="tx-vq__vid"><p class="eyebrow">Animated explainer</p><h2>Title IX explained</h2>{yt('cdtPRr_5wXE', 'Title IX Explained', label='Animated explainer')}</div>
    <div class="tx-quiz" id="txQuiz">
      <p class="eyebrow">Take the 2-question quiz</p>
      <h2>Is my school covered by Title IX?</h2>
      <div class="tx-prog" aria-hidden="true"><span data-p="1"></span><span data-p="2"></span></div>
      <section class="tx-step on" data-step="s1" aria-live="polite">
        <p class="tx-q">Do you attend a public or private school?</p>
        <div class="tx-choices"><button type="button" data-a1="public">Public</button><button type="button" data-a1="private">Private</button></div>
        <button type="button" class="tx-unsure" aria-expanded="false" aria-controls="txh1">Unsure?</button>
        <div class="tx-help" id="txh1" hidden><b>Here’s how to find out:</b> Your school’s website likely lists this information under its “About Us” page or pages discussing its history, mission, or governance. You can also check your student handbook, enrollment forms, or ask a teacher or administrator.</div>
      </section>
      <section class="tx-step" data-step="s2" aria-live="polite">
        <p class="tx-q">Does your school receive <em>any</em> federal funding?</p>
        <div class="tx-choices"><button type="button" data-a2="yes">Yes</button><button type="button" data-a2="no">No</button></div>
        <button type="button" class="tx-unsure" aria-expanded="false" aria-controls="txh2">Unsure?</button>
        <div class="tx-help" id="txh2" hidden><b>Here’s how to find out:</b> Information about your school’s funding sources can likely be found in its annual reports, budgets, or financial statements. You can also check <a class="link" href="https://www.usaspending.gov/" target="_blank" rel="noopener">usaspending.gov</a> or see if your school’s tax statements are available online. If you’re not able to find this information online, you can ask a school administrator, guidance counselor, or teacher.</div>
      </section>
      <section class="tx-step" data-step="yes" aria-live="polite"><div class="tx-res">
        <h3>Your school IS covered by Title IX</h3>
        <p>That means your school is legally required to prevent and respond to sex-based discrimination, including sexual harassment and assault, so every student has equal access to education.</p>
        <div class="btns">{btn('Supportive measures', '#supportive-measures', 'slate', 'sm')}{btn('Who do I talk to?', '#coordinator', 'ghost', 'sm')}<button type="button" class="btn btn--ghost btn--sm" data-restart>Start over</button></div></div>
      </section>
      <section class="tx-step" data-step="no" aria-live="polite"><div class="tx-res">
        <h3>Your school is NOT covered by Title IX</h3>
        <p>Private schools that receive no federal funding aren’t bound by Title IX. But your school may still have its own anti-discrimination and safety policies. Check your student handbook or ask an administrator about your rights and protections.</p>
        <div class="btns">{btn('Push for a stronger policy', 'reform-policy.html', 'slate', 'sm')}<button type="button" class="btn btn--ghost btn--sm" data-restart>Start over</button></div></div>
      </section>
    </div>
  </div>
</section>

<section class="band band--paper" id="rights">
  <div class="wrap tx-rights">
    <div>
      <h2>What Title IX laws really mean</h2>
      <p class="sp-lead">Title IX addresses sexual violence and requires schools to proactively address, remedy, and eliminate sexual violence on their campuses. You are protected under Title IX regardless of your gender and how you identify.</p>
      <ul class="tx-list">{rights}</ul>
    </div>
    <div class="tx-who" id="coordinator">
      <p class="eyebrow">Who do I talk to?</p>
      <h3>Go to your Title IX Coordinator</h3>
      <p>When in doubt, go directly to the school Title IX Director (sometimes called the Title IX Coordinator). Your school website should have that information, or you can ask the school secretary.</p>
      <p style="margin-bottom:8px"><b>A school is in violation of Title IX if:</b></p>
      <ul>{viol}</ul>
      <p>Title IX laws are always changing, which is why knowing what is available to protect you is so crucial.</p>
      <div class="btns">{btn('Read the full FAQ answer', TIX_FAQ, 'mint', 'sm')}<button class="btn btn--ghost btn--sm" type="button" data-open-help>Talk to someone now</button></div>
    </div>
  </div>
</section>

<section class="band band--deep" id="timeline">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">11 moments &middot; 1972 to today</p><h2>Timeline of Title IX</h2><p class="lede" style="color:rgba(255,255,255,.88)">Select a year to read what changed.</p></div></div>
    <div class="tx-tl" id="txTl">
      <div class="tx-tl__track" role="tablist" aria-label="Title IX timeline"><div class="tx-tl__line" aria-hidden="true"><i></i></div>{''.join(tl_btns)}</div>
      <div class="tx-tl__panels">{''.join(tl_panels)}</div>
      <div class="tx-tl__nav"><button type="button" data-tl="-1">&#8249; Earlier</button><span class="tx-tl__n" aria-live="polite">1 of {len(TIMELINE)}</span><button type="button" data-tl="1">Later &#8250;</button></div>
    </div>
  </div>
</section>

<section class="band band--aqua" id="supportive-measures">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">18 supportive measures</p><h2>Support you can ask for, with or without an investigation</h2>
      <p class="lede lede--full">Schools are required to offer supportive measures to students impacted by any form of sex discrimination, including sexual harassment and sexual assault. Students and families can request supportive measures even if they choose not to have an investigation.</p></div></div>
    <div class="tx-sm" id="txSm">
      <p style="margin:0; font-weight:600">Tap the measures you want to ask your school about, then copy your list to bring to your Title IX Coordinator, a counselor or a trusted adult.</p>
      {sm}
      <div class="tx-sm__bar"><output id="txSmN">0 selected</output><div class="btns"><button class="btn btn--slate btn--sm" type="button" id="txSmCopy">Copy my list</button><button class="btn btn--ghost btn--sm" type="button" id="txSmClear">Clear</button></div></div>
      <textarea id="txSmOut" hidden aria-label="Your list of supportive measures" readonly></textarea>
      <p class="tx-sm__note">Your school cannot require or pressure you to pursue any of these options. They can be offered and the reporting student can take advantage of them. However, they should never be made to feel they have to leave school or change schools.</p>
    </div>
    <div class="tx-more">
      <div>{img('nwlc-logo-1200x630-1', 'National Women’s Law Center')}<div><b>FAQs brought to you by our friends</b><p>The National Women’s Law Center’s guide to supportive measures in K-12 schools.</p>{btn('Supportive Measures FAQ (K-12)', 'https://nwlc.org/wp-content/uploads/2021/11/Supportive-Measures-FAQ-K12-vF.pdf', 'teal', 'sm')}</div></div>
      <div data-gallery><button type="button" class="tx-zoom" data-src="{imgsrc('13-title-ix-1')}" data-cap="Supportive measures">{img('13-title-ix-1', 'Infographic: supportive measures your school can offer a survivor, with or without an investigation')}</button><div><b>Save it as one graphic</b><p>Every supportive measure on one shareable slide.</p><button type="button" class="btn btn--slate btn--sm" onclick="this.closest('[data-gallery]').querySelector('button[data-src]').click()">View the graphic</button></div></div>
    </div>
  </div>
</section>

<section class="band band--slate" id="media-analysis">
  <div class="wrap">
    <div class="tx-media">
      <div>
        <p class="eyebrow">Resources, updates &amp; media analysis</p>
        <h2>Tell Me Lies… but not about Title IX</h2>
        <p class="lede" style="color:rgba(255,255,255,.88)">SafeBAE’s blog posts and social media explainers on Title IX, school accountability, and student rights.</p>
        <p class="tx-media__q">“A new season of Tell Me Lies is out, and sexual assault is a central plotline. We’re not doing a recap… we’re doing a reality check on what the show portrays.” <span class="mono small" style="display:block;margin-top:6px;color:var(--mint)">@safe_bae</span></p>
        <div class="btns">{btn('Follow @safe_bae', 'https://www.instagram.com/safe_bae/', 'mint', 'sm')}{btn('All Title IX posts', 'https://www.safebae.org/category/title-ix/', 'ghost', 'sm')}</div>
      </div>
      {player(tml, 'Tell Me Lies… but not about Title IX: six slides', 'sp-portrait', interval=6000)}
    </div>
    <div class="tx-posts"><div class="section-head"><div><h3>From the SafeBAE blog</h3></div></div><div class="sp-posts sp-posts--3">{posts}</div></div>
  </div>
</section>

<section class="band band--paper tx-more2">
  <div class="wrap split">
    <div>
      <h2>Schools can do more</h2>
      <p>Since 2020, schools have been pulled back and forth between restrictive rules, attempts at expanded protections, and ongoing court challenges. This leaves survivors with fewer options, and schools without clear or consistent guidance. That’s why knowing about Title IX is important, but not enough on its own. <b class="tx-better">Your school has the power to do better.</b></p>
      <p>We created the School Policy Reform Guide to help students, educators, and administrators strengthen policies beyond the bare federal minimum. By adopting trauma-informed, survivor-centered practices, schools can ensure real safety, transparency, and accountability.</p>
      <div class="btns">{btn('For students', 'reform-policy.html', 'slate', arrow=True)}{btn('For administrators', 'policy-reform-guide.html', 'ghost', arrow=True)}</div>
    </div>
    <div class="tx-photo">{img('img-3947', 'Students in a classroom during a SafeBAE session')}<span class="sticker sticker--r">Policy reform guide</span></div>
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  /* quiz */
  var q = document.getElementById('txQuiz');
  if(q){ var steps = q.querySelectorAll('.tx-step'), p1 = q.querySelector('[data-p="1"]'), p2 = q.querySelector('[data-p="2"]');
    function show(n){ steps.forEach(function(s){ s.classList.toggle('on', s.getAttribute('data-step') === n); }); var f = q.querySelector('.tx-step.on button'); if(f && n !== 's1') f.focus({preventScroll:true}); }
    q.addEventListener('click', function(e){ var t = e.target.closest('button'); if(!t) return;
      if(t.hasAttribute('data-a1')){ p1.classList.add('done'); if(t.getAttribute('data-a1') === 'public'){ p2.classList.add('done'); show('yes'); } else show('s2'); }
      else if(t.hasAttribute('data-a2')){ p2.classList.add('done'); show(t.getAttribute('data-a2') === 'yes' ? 'yes' : 'no'); }
      else if(t.classList.contains('tx-unsure')){ var b = document.getElementById(t.getAttribute('aria-controls')); var o = b.hidden; b.hidden = !o; t.setAttribute('aria-expanded', String(o)); }
      else if(t.hasAttribute('data-restart')){ p1.classList.remove('done'); p2.classList.remove('done'); q.querySelectorAll('.tx-help').forEach(function(h){ h.hidden = true; }); q.querySelectorAll('.tx-unsure').forEach(function(b){ b.setAttribute('aria-expanded','false'); }); show('s1'); q.querySelector('[data-a1]').focus({preventScroll:true}); }
    }); }
  /* pictograph */
  var pc = document.querySelector('.tx-pict'); if(pc){ if('IntersectionObserver' in window){ var po = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ pc.classList.add('seen'); po.disconnect(); } }); }, {threshold:.5}); po.observe(pc); } else pc.classList.add('seen'); }
  /* timeline */
  var tl = document.getElementById('txTl');
  if(tl){ tl.classList.add('ready'); var tabs = tl.querySelectorAll('[role="tab"]'), panels = tl.querySelectorAll('.tx-tl__panel'), fill = tl.querySelector('.tx-tl__line i'), n = tl.querySelector('.tx-tl__n'), cur = 0;
    function sel(i, focus){ cur = (i + tabs.length) % tabs.length; tabs.forEach(function(t, k){ var on = k === cur; t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1; t.classList.toggle('past', k < cur); panels[k].classList.toggle('on', on); });
      if(fill) fill.style.width = (cur / (tabs.length - 1) * 100) + '%'; n.textContent = (cur + 1) + ' of ' + tabs.length;
      if(focus) tabs[cur].focus(); var tr = tabs[cur].parentNode; if(tr.scrollWidth > tr.clientWidth) tr.scrollTo({left: tabs[cur].offsetLeft - tr.clientWidth/2 + tabs[cur].offsetWidth/2, behavior:'smooth'}); }
    tabs.forEach(function(t, i){ t.addEventListener('click', function(){ sel(i); }); t.addEventListener('keydown', function(e){ var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if(d){ e.preventDefault(); sel(cur + d, true); } }); });
    tl.querySelectorAll('[data-tl]').forEach(function(b){ b.addEventListener('click', function(){ sel(cur + (+b.getAttribute('data-tl'))); }); });
    sel(0); }
  /* supportive measures list */
  var sm = document.getElementById('txSm');
  if(sm){ var pills = sm.querySelectorAll('.tx-sm__pills button'), out = document.getElementById('txSmN'), ta = document.getElementById('txSmOut'), cp = document.getElementById('txSmCopy');
    function chosen(){ return Array.prototype.filter.call(pills, function(p){ return p.getAttribute('aria-pressed') === 'true'; }).map(function(p){ return p.textContent; }); }
    function upd(){ var c = chosen(); out.textContent = c.length + ' selected'; if(!ta.hidden) ta.value = text(c); }
    function text(c){ return 'Supportive measures I would like to ask about:\n' + c.map(function(x){ return '- ' + x; }).join('\n'); }
    pills.forEach(function(p){ p.addEventListener('click', function(){ p.setAttribute('aria-pressed', p.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); upd(); }); });
    cp.addEventListener('click', function(){ var c = chosen(); if(!c.length){ out.textContent = 'Pick at least one first'; return; } var t = text(c);
      function fallback(){ ta.hidden = false; ta.value = t; ta.focus(); ta.select(); cp.textContent = 'Select and copy below'; }
      if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(t).then(function(){ cp.textContent = 'Copied'; setTimeout(function(){ cp.textContent = 'Copy my list'; }, 1600); }, fallback); } else fallback(); });
    document.getElementById('txSmClear').addEventListener('click', function(){ pills.forEach(function(p){ p.setAttribute('aria-pressed','false'); }); ta.hidden = true; cp.textContent = 'Copy my list'; upd(); }); }
})();
</script>'''
    page('title-ix.html', 'Title IX · SafeBAE',
         'Understand Title IX: student rights, reporting options, how schools must respond to sexual harassment, and a timeline of the law’s key changes.',
         body, active='resources', body_class='tx', head_extra=f'<style>{SP_CSS}{TX_CSS}</style>', scripts=js)


# =====================================================================
# 3. MYTHS & FACTS
# =====================================================================
MYTH_GROUPS = [
  ('Masculinity & male survivors', [
    ('Men are too strong to be assaulted.', 'Strength does not prevent sexual violence. At least <b>1 in 6 men</b> will experience sexual abuse or assault in their lifetime.'),
    ('Men always want sex and welcome all sexual advances.', 'Sexual assault is never wanted. It is a traumatic experience for any survivor, regardless of gender.'),
    ('Only gay men commit sexual violence against other men.', 'Sexual violence is about <b>power and control</b>, not sexual orientation. Survivors and perpetrators can be of any gender or identity.'),
    ('Men abused by women “got lucky.”', 'Sexual violence is never a privilege. Women can, and do, sexually abuse or assault boys and men. Survivors are not “lucky”; they are harmed and exploited.')]),
  ('Who it affects & who commits it', [
    ('“Real rape” is committed by strangers.', 'Anyone can be a perpetrator: date rape and stranger rape are both rape. Most rapes are committed by someone the victim knows: <b>92% of female victims</b> and <b>74% of male victims</b> report perpetrators who were acquaintances or intimate partners, and as many as <b>93% of child sexual abuse survivors</b> knew their abuser.'),
    ('Only women can be raped.', 'Sexual assault is experienced by people of all genders. <b>1 out of 10</b> rape victims is male, and <b>1 in 2</b> transgender people are sexually assaulted in their lifetime.'),
    ('Sexual assault can’t happen within a marriage or relationship.', 'Consent is required every time, in every relationship. A relationship, or a past “yes,” is never standing consent. Intimate partner sexual violence is real, harmful, and a crime in all 50 states.'),
    ('Sexual violence doesn’t happen to people with disabilities.', 'People with disabilities experience sexual violence at far higher rates. People with intellectual disabilities are sexually assaulted at <b>7 times the rate</b> of people without disabilities, and their abusers are often people they know and rely on.')]),
  ('Blame & believing survivors', [
    ('False claims of rape are common. Most are made for revenge, regret, or attention.', 'False reporting rates for sexual assault are in the <b>2–10% range</b>, the same as other crimes. The far bigger problem is under-reporting: the majority of sexual assaults are never reported to authorities at all.'),
    ('Clothing choices, location, and drinking can prevent rape and harassment.', 'Sexual assault is about <b>power, not clothing</b>. This logic holds survivors responsible for their own assaults instead of placing responsibility where it belongs: on perpetrators.'),
    ('If they didn’t fight back, it wasn’t really assault.', 'Freezing is one of the most common trauma responses. Many survivors experience <b>tonic immobility</b>, an involuntary reaction that makes it impossible to move or speak. Not fighting back is never consent.'),
    ('If it really happened, they would have reported it right away.', 'Delayed reporting is the norm, not the exception. Fear, shame, self-blame, and trauma keep many survivors silent for months, years, or forever. A delay says nothing about the truth of what happened.')]),
]
REASONS = ['It’s emotionally painful, and trauma can make details hard to remember.',
           'Shame and stigma: fear of being judged, blamed, or “slut-shamed.”',
           'Fear of not being believed, or that people will defend the perpetrator.',
           'Fear that nothing will be done: fewer than 2% of reports lead to a conviction.',
           'Fear of punishment or retaliation, especially for teens.',
           'Not realizing what happened was abuse in the first place.']
RISK = [('stats-marginalized2', 'Foster youth', 'Foster youth: compared to children living with both biological parents, children in foster care are 10 times more likely to be sexually abused. 81% of girls in foster care were sexually abused and 68% suffered abuse at the hands of multiple people.'),
        ('stats-marginalized3', 'Race and ethnicity', 'Race and ethnicity: non-white people often face numerous barriers to accessing resources and reporting. For every Black woman who reports rape, at least 15 Black women do not report.'),
        ('stats-marginalized4', 'Indigenous people', 'Indigenous people are at greatest risk of experiencing sexual violence in the United States. 41% of sexual assaults against Indigenous people in the U.S. are committed by a stranger.'),
        ('stats-marginalized5', 'Black youth', 'Black youth are also at increased risk of experiencing sexual violence. One in four Black girls will be sexually assaulted before they turn 18 (National Center on Violence Against Women in the Black Community).'),
        ('stats-marginalized6', 'People with disabilities', 'People with disabilities: youth with physical or developmental disabilities are 5 times more likely to be sexually assaulted than their nondisabled peers. Over 90% of people with developmental disabilities will experience sexual assault (University of Michigan).'),
        ('stats-marginalized7', 'LGBTQ+ people', 'LGBTQ+ people face increased barriers to reporting, including fears of being outed, risk of violence and of not being believed. Myth: being sexually assaulted by someone of the same gender can make a person gay or lesbian. Fact: the assault is typically not based on the sexual preferences of the victim or rapist, and therefore does not necessarily change the victim’s sexual orientation.'),
        ('stats-marginalized8', 'Lesbian and bisexual women', 'Lesbian and bisexual women are much more likely to experience sexual violence compared to heterosexual women, with 63% of bisexual, 49% of lesbian, and 35% of heterosexual women reporting being raped in their lifetime by anyone (NIH).'),
        ('stats-marginalized9', 'Transgender and gender diverse people', 'Transgender and gender diverse people: almost half of all transgender people have been sexually assaulted at some point in their lives, and these rates are even higher for non-white trans people and those who have done sex work, been homeless, or have a disability (National Center for Transgender Equality).'),
        ('stats-marginalized10', 'Transgender people face the greatest risks', 'Transgender people face the greatest risks for all types of violence, especially those who have more than one marginalized identity. Transgender people are significantly more likely to be murdered during their assault. #ProtectTransYouth'),
        ('stats-marginalized11', 'Statistics on male survivors', 'Statistics on male survivors: over half of male victims of completed or attempted rape reported experiencing their first victimization prior to age 18. Men are more likely to be sexually assaulted than be falsely accused of rape.')]
CAUSES = [('Being under the influence', 'var(--coral)'), ('The clothes someone is wearing', 'var(--mint)'), ('Walking alone', 'var(--teal)'),
          ('Flirty behavior', 'var(--aqua)'), ('Hooking up with a lot of people', 'var(--gray)')]
ELEMENTS = ['Victim blaming', 'Racial stereotypes', 'Rape myths', 'Media + algorithms', 'Peer influence', 'Gender + sexuality beliefs']

MF_CSS = '''
.mf-hero{background:var(--slate) var(--grain); color:#fff}
.mf-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(40px,5vw,64px)}
.mf-hero__grid{display:grid; grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr); gap:clamp(28px,5vw,64px); align-items:center}
.mf-hero__media{position:relative; padding:0 0 70px 0}
.mf-hero__photo img{width:100%; aspect-ratio:4/3; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft); filter:saturate(.9)}
.mf-hero__card{position:absolute; left:-36px; bottom:0; width:min(74%,320px); height:170px; perspective:1000px; animation:sb-rise .9s .4s var(--ease) both}
.mf-hero__in{position:relative; width:100%; height:100%; transform-style:preserve-3d; animation:mfcard 9s 1.6s var(--ease) infinite}
.mf-hero__face{position:absolute; inset:0; backface-visibility:hidden; -webkit-backface-visibility:hidden; border-radius:var(--r-xl); padding:18px 20px; display:flex; flex-direction:column; gap:8px; background:var(--slate-deep); border:1.5px solid var(--line-dark); box-shadow:var(--shadow-soft)}
.mf-hero__face small{font-family:var(--mono); font-size:.68rem; letter-spacing:.12em; text-transform:uppercase; font-weight:600; color:var(--coral)}
.mf-hero__face b{font-family:var(--display); font-stretch:106%; font-size:1.12rem; line-height:1.25}
.mf-hero__face--back{background:var(--mint); color:var(--slate); border-color:var(--mint); transform:rotateY(180deg)}
.mf-hero__face--back small{color:var(--slate)}
@keyframes mfcard{0%,38%{transform:rotateY(0)} 50%,88%{transform:rotateY(180deg)} 100%{transform:rotateY(360deg)}}
@media (max-width:900px){.mf-hero__grid{grid-template-columns:1fr} .mf-hero__media{max-width:520px} .mf-hero__card{left:12px}}
.mf-hero h1{font-size:clamp(2.4rem,4.8vw,4.6rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; margin:0 0 .35em}
.mf-strike{position:relative; display:inline-block; color:var(--mint)}
.mf-strike::after{content:""; position:absolute; left:-4%; right:-4%; top:52%; height:.11em; background:var(--coral); border-radius:.06em; transform:rotate(-4deg) scaleX(0); transform-origin:left; animation:mfstrike .7s .5s cubic-bezier(.2,.8,.2,1) forwards}
@keyframes mfstrike{to{transform:rotate(-4deg) scaleX(1)}}
.mf-hero .lede{color:rgba(255,255,255,.88); max-width:none}
.mf-qs{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-top:34px}
.mf-qs a{display:flex; flex-direction:column; justify-content:space-between; gap:18px; min-height:150px; padding:18px; border-radius:14px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); color:#fff; text-decoration:none; transition:background .2s, transform .2s, color .2s}
.mf-qs a:hover{background:var(--mint); color:var(--slate); transform:translateY(-3px)}
.mf-qs small{font-family:var(--mono); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.mf-qs a:hover small{color:var(--slate)}
.mf-qs b{font-family:var(--display); font-stretch:110%; font-size:clamp(1.15rem,1.7vw,1.4rem); line-height:1.1}
.mf-qs i{font-style:normal; font-weight:800}
@media (max-width:960px){.mf-qs{grid-template-columns:1fr 1fr}} @media (max-width:520px){.mf-qs a{min-height:118px; padding:14px}}
.mf-causes{display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(28px,5vw,72px); align-items:center}
.mf-els{display:flex; flex-wrap:wrap; gap:8px; margin-top:12px}
.mf-els span{font-family:var(--display); font-stretch:108%; font-weight:800; font-size:1rem; padding:10px 16px; border-radius:999px; background:var(--aqua); color:var(--slate)}
.mf-els span:nth-child(3n+2){background:var(--teal); color:#fff} .mf-els span:nth-child(3n){background:var(--mint)}
.mf-els-label{font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin:22px 0 0}
.mf-pie{background:var(--mist); border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:22px; align-items:center}
.mf-pie__title{grid-column:1/-1; margin:0; font-family:var(--display); font-weight:900; font-stretch:125%; text-transform:uppercase; font-size:clamp(1.6rem,3vw,2.4rem); line-height:1; letter-spacing:-.01em}
.mf-pie__chart{position:relative; aspect-ratio:1}
.mf-pie__chart svg{width:100%; height:100%; transform:rotate(-90deg)}
.mf-pie__chart .bg{fill:#fff; stroke:var(--gray); stroke-width:2}
.mf-pie__chart .fill{fill:none; stroke:var(--slate); stroke-width:100; stroke-dasharray:0 100; transition:stroke-dasharray 1s cubic-bezier(.2,.8,.2,1)}
.mf-pie__pct{position:absolute; inset:0; display:grid; place-items:center; font-family:var(--display); font-weight:900; font-stretch:112%; font-size:clamp(1.8rem,3vw,2.6rem); color:var(--slate); transition:color .4s}
.mf-pie.full .mf-pie__pct{color:var(--mint)}
.mf-pie__legend{list-style:none; padding:0; margin:0; display:grid; gap:6px}
.mf-pie__legend li{margin:0}
.mf-pie__legend button{display:flex; align-items:center; gap:10px; width:100%; text-align:left; font:inherit; font-weight:700; font-size:.92rem; line-height:1.25; padding:8px 10px; border-radius:8px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer}
.mf-pie__legend button::before{content:""; flex:none; width:18px; height:18px; border-radius:4px; background:var(--sw)}
.mf-pie__legend button:hover{border-color:var(--teal)}
.mf-pie__legend button[aria-pressed="true"] .t{text-decoration:line-through; text-decoration-thickness:2px; color:var(--ink-soft)}
.mf-pie__legend button[aria-pressed="true"]::after{content:"0%"; margin-left:auto; font-family:var(--mono); font-size:.74rem; text-decoration:none; color:var(--slate); font-weight:600}
.mf-pie__legend .is-cause[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)} .mf-pie__legend .is-cause[aria-pressed="true"] .t{text-decoration:none; color:#fff}
.mf-pie__legend .is-cause[aria-pressed="true"]::after{content:"100%"; color:var(--mint)}
.mf-pie__msg{grid-column:1/-1; margin:0; min-height:3em; font-weight:600}
.mf-pie__msg b{font-family:var(--display); font-stretch:110%}
@media (max-width:960px){.mf-causes{grid-template-columns:1fr}} @media (max-width:520px){.mf-pie{grid-template-columns:1fr} .mf-pie__chart{max-width:220px; margin-inline:auto; width:100%}}
.mf-report{display:grid; grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr); gap:clamp(24px,4vw,56px); align-items:center}
.mf-reasons{list-style:none; padding:0; margin:18px 0 0; display:grid; grid-template-columns:1fr 1fr; gap:10px}
.mf-reasons li{margin:0; background:#fff; border-radius:12px; padding:16px; font-weight:600; line-height:1.45; border-left:5px solid var(--teal)}
.mf-report__img img{width:100%; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
@media (max-width:860px){.mf-report{grid-template-columns:1fr} .mf-report__img{max-width:360px}} @media (max-width:560px){.mf-reasons{grid-template-columns:1fr}}
.mf-meg{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:clamp(24px,4vw,56px); align-items:start}
.mf-meg__q{margin:22px 0 0; padding:20px 22px; border-radius:var(--r-xl); background:var(--slate); color:#fff}
.mf-meg__q blockquote{margin:0; font-family:var(--display); font-stretch:104%; font-weight:700; font-size:clamp(1.05rem,1.6vw,1.25rem); line-height:1.4}
.mf-meg__q .cite{color:var(--mint)}
.mf-tweet{margin-top:16px; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; background:#fff}
.mf-tweet img{width:100%}
.mf-tweet figcaption{font-size:.8rem; color:var(--ink-soft); padding:8px 14px 10px; border-top:1px solid var(--line)}
@media (max-width:860px){.mf-meg{grid-template-columns:1fr}}
.mf-mvf-head{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(24px,4vw,56px); align-items:center; margin-bottom:clamp(26px,3vw,40px)}
.mf-mvf-head .lede{color:rgba(255,255,255,.88)}
@media (max-width:860px){.mf-mvf-head{grid-template-columns:1fr}}
.mf-grp + .mf-grp{margin-top:clamp(26px,3vw,40px)}
.mf-choke{display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:20px clamp(20px,3vw,40px); align-items:center; margin-top:clamp(28px,3.5vw,44px); padding:clamp(18px,2.6vw,28px); border-radius:var(--r-xl); background:rgba(255,255,255,.05); border:1px solid var(--line-dark)}
.mf-choke__label{width:220px; padding:6px}
.mf-choke__tag{margin:0 0 8px; font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; color:var(--mint)}
.mf-choke__pair{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 10px}
.mf-choke__pair span{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.1rem; padding:8px 12px; border-radius:12px; background:var(--slate-deep); border:1px solid var(--line-dark)}
.mf-choke__pair span:last-child{background:var(--mint); color:var(--slate); border-color:var(--mint)}
.mf-choke__pair small{display:block; font-family:var(--mono); font-size:.62rem; letter-spacing:.1em; text-transform:uppercase; font-weight:600; opacity:.8}
.mf-choke__txt{margin:0; font-size:.94rem; color:rgba(255,255,255,.86)}
@media (max-width:900px){.mf-choke{grid-template-columns:1fr} .mf-choke__label{width:100%; max-width:260px} .mf-choke .btn{justify-self:start}}
.mf-grp h3{display:flex; align-items:baseline; gap:12px; color:#fff; font-size:clamp(1.3rem,2vw,1.6rem)}
.mf-grp h3 small{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.mf-flips{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px}
.mf-flips{align-items:stretch} .mf-flips .flip{min-height:270px; height:100%} .mf-flips .flip__in{height:100%} .mf-flips .flip__face{min-height:100%}
.mf-flips .flip__face--front{background:var(--slate-deep); border:1.5px solid var(--line-dark)}
.mf-flips .flip__face--front .flip__tag{color:var(--coral)}
.mf-flips .flip__face--front .flip__txt{font-size:clamp(1.15rem,1.5vw,1.35rem)}
.mf-flips .flip__face--back .flip__txt{font-family:var(--body); font-weight:600; font-size:.95rem; line-height:1.45}
.mf-flips .flip__face--back .flip__txt b{font-family:var(--display); font-weight:900; font-stretch:110%}
.mf-flips .flip:focus-visible{outline-offset:4px}
@media (max-width:1060px){.mf-flips{grid-template-columns:1fr 1fr}} @media (max-width:560px){.mf-flips{grid-template-columns:1fr} .mf-flips .flip{min-height:220px}}
.mf-risk{display:grid; grid-template-columns:minmax(0,1.45fr) minmax(0,.55fr); gap:clamp(18px,3vw,32px); align-items:stretch}
.mf-risk > .player{align-self:start}
.mf-after{margin-top:clamp(36px,4.5vw,56px); padding-top:clamp(28px,3.5vw,40px); border-top:1px solid var(--line)}
.mf-risk__side{display:flex; flex-direction:column; gap:12px; min-width:0}
.mf-risk__hint{margin:12px 0 0; font-weight:700; line-height:1.45}
.mf-risk__list{display:grid; gap:6px; flex:1; align-content:space-between; counter-reset:rk}
.mf-risk__list button{font:inherit; font-size:.9rem; font-weight:700; text-align:left; line-height:1.25; padding:8px 12px 8px 42px; border-radius:10px; border:1.5px solid var(--line); background:#fff; color:var(--slate); cursor:pointer; position:relative; counter-increment:rk}
.mf-risk__list button::before{content:counter(rk); position:absolute; left:10px; top:50%; transform:translateY(-50%); width:22px; height:22px; border-radius:50%; display:grid; place-items:center; font-family:var(--mono); font-size:.68rem; background:var(--aqua); color:var(--slate)}
.mf-risk__list button:hover{border-color:var(--teal)}
.mf-risk__list button[aria-pressed="true"]{background:var(--slate); color:#fff; border-color:var(--slate)}
.mf-risk__list button[aria-pressed="true"]::before{background:var(--mint)}
@media (max-width:960px){.mf-risk{grid-template-columns:1fr} .mf-risk__list{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.mf-risk__list{grid-template-columns:1fr}}
'''


def myths_facts():
    flips_html = []
    for g, items in MYTH_GROUPS:
        cards = ''.join(f'<button type="button" class="flip" data-flip aria-pressed="false"><span class="flip__in"><span class="flip__face flip__face--front"><span class="flip__tag">Myth</span><span class="flip__txt">{esc(m)}</span><span class="hint">Tap for the fact</span></span>'
                        f'<span class="flip__face flip__face--back"><span class="flip__tag">Fact</span><span class="flip__txt">{f}</span><span class="hint">Tap to flip back</span></span></span></button>' for m, f in items)
        flips_html.append(f'<div class="mf-grp"><h3>{esc(g)} <small>{len(items)} myths</small></h3><div class="mf-flips">{cards}</div></div>')
    legend = ''.join(f'<li><button type="button" aria-pressed="false" style="--sw:{c}" data-v="0"><span class="t">{esc(t)}</span></button></li>' for t, c in CAUSES)
    legend += '<li><button type="button" aria-pressed="false" style="--sw:var(--slate)" data-v="100" class="is-cause"><span class="t">Rapist</span></button></li>'
    els = ''.join(f'<span>{esc(e)}</span>' for e in ELEMENTS)
    reasons = ''.join(f'<li>{esc(r)}</li>' for r in REASONS)
    risk_chips = ''.join(f'<button type="button" data-go="{i}" aria-pressed="{str(i == 0).lower()}">{esc(c)}</button>' for i, (n, c, alt) in enumerate(RISK))

    body = f'''
<section class="mf-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <div class="mf-hero__grid">
      <div class="rise">
        {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Myths & Facts', None))}
        <p class="eyebrow">Myths, facts &amp; statistics</p>
        <h1>Let’s debunk the <span class="mk mf-strike">myths</span> about sexual assault.</h1>
        <p class="lede">What the research actually says about sexual violence, who is most affected, and why so much of it goes unreported.</p>
      </div>
      <div class="mf-hero__media">
        <div class="mf-hero__photo">{img('img-2400', 'Students sitting in a circle during a SafeBAE discussion', loading='eager')}</div>
        <div class="mf-hero__card" aria-hidden="true"><div class="mf-hero__in">
          <div class="mf-hero__face"><small>Myth</small><b>If they didn’t fight back, it wasn’t really assault.</b></div>
          <div class="mf-hero__face mf-hero__face--back"><small>Fact</small><b>Freezing is one of the most common trauma responses. Not fighting back is never consent.</b></div>
        </div></div>
      </div>
    </div>
    <nav class="mf-qs" aria-label="Questions on this page">
      <a href="#causes"><small>Causes</small><b>What causes sexual violence?</b><i aria-hidden="true">&darr;</i></a>
      <a href="#survivors-report"><small>Reporting</small><b>Why don’t survivors report?</b><i aria-hidden="true">&darr;</i></a>
      <a href="#myths-vs-facts"><small>12 myths</small><b>Understanding myths vs. facts</b><i aria-hidden="true">&darr;</i></a>
      <a href="#who-is-most-at-risk"><small>Risk</small><b>Who is most at risk?</b><i aria-hidden="true">&darr;</i></a>
    </nav>
  </div>
</section>

<section class="band band--paper" id="causes">
  <div class="wrap mf-causes">
    <div>
      <h2>What causes sexual violence?</h2>
      <p class="lede">People blame a lot of things: being under the influence, the clothes someone is wearing, walking alone, flirty behavior, or hooking up with a lot of people. None of these cause sexual violence. It happens when someone chooses to ignore or violate another person’s boundaries and consent.</p>
      <p>That choice is often reinforced by rape culture: victim-blaming, harmful stereotypes, peer pressure, media, algorithms, and beliefs about gender, sexuality, power, and entitlement. Prevention means holding people accountable and challenging the culture that excuses harm.</p>
      <p class="mf-els-label">Elements of rape culture</p>
      <div class="mf-els">{els}</div>
    </div>
    <div class="mf-pie" id="mfPie">
      <p class="mf-pie__title">Causes of rape</p>
      <div class="mf-pie__chart"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="99"/><circle class="fill" cx="100" cy="100" r="50" pathLength="100"/></svg><span class="mf-pie__pct" aria-hidden="true">?</span></div>
      <ul class="mf-pie__legend">{legend}</ul>
      <p class="mf-pie__msg" aria-live="polite">Tap each one to see how much of the chart it takes up.</p>
    </div>
  </div>
</section>

<section class="band band--aqua" id="survivors-report">
  <div class="wrap mf-report">
    <div>
      <h2>Why don’t survivors report?</h2>
      <p class="lede lede--full">If a survivor doesn’t report to the police, it does NOT mean the violence didn’t happen. There are many reasons someone might not come forward:</p>
      <ul class="mf-reasons">{reasons}</ul>
    </div>
    <div class="mf-report__img">{img('square', 'Reporting for survivors can feel like hitting a brick wall.')}</div>
  </div>
</section>

<section class="band band--paper" id="megan">
  <div class="wrap mf-meg">
    <div>
      <p class="eyebrow">Real example</p>
      <h2>Megan Thee Stallion</h2>
      <p>In 2020, Megan Thee Stallion was harmed by someone she knew. When police arrived, she said she had stepped on glass because she feared the situation could escalate into police violence. After she later spoke out, she was mocked, doubted, and blamed publicly.</p>
      <p>Her story shows why reporting is never simple, and why we should never assume silence means nothing happened. Survivors deserve to be believed, supported, and given choices.</p>
      <figure class="mf-meg__q" style="margin-inline:0"><blockquote>“I didn’t want them to kill any of us, or shoot any of us. So I just said I stepped on glass… Even though this person just did this to me, my first reaction still was to try to save us. I didn’t want to see anybody die.”</blockquote><span class="cite">Megan Thee Stallion</span></figure>
    </div>
    <div>
      {yt('EY7aAlieiko', 'Gayle King on Megan Thee Stallion’s Hurt and Pain From 2020 Shooting', label='Entertainment Tonight')}
      <figure class="mf-tweet" style="margin-inline:0;margin-bottom:0">{img('63abc69e2b109-image', 'Tweet from Megan Thee Stallion, @theestallion, January 21, 2021: “Y’all so believe black women and protect black women online BUT WHEN I LITERALLY SAY I GOT SHOT ITS CONFUSING”')}<figcaption>Megan Thee Stallion on Twitter, January 21, 2021</figcaption></figure>
    </div>
  </div>
</section>

<section class="band band--slate" id="myths-vs-facts">
  <div class="wrap">
    <div class="mf-mvf-head">
      <div><p class="eyebrow">12 myths &middot; 3 themes</p><h2>Myths vs. facts: sexual violence</h2>
        <p class="lede">Tap a card to flip it and see what the research says.</p>
        <div class="btns"><button class="btn btn--mint" type="button" id="mfAll">Reveal all facts</button></div></div>
      {yt('elCyCZb9BU8', 'Sexual Assault: Myths vs. Facts', label='SafeBAE')}
    </div>
    {''.join(flips_html)}
    <aside class="mf-choke" aria-label="From the Choking Hazard campaign">
      <div class="mf-choke__label">{hz_label("hz--tilt")}</div>
      <div class="mf-choke__body">
        <p class="mf-choke__tag">One more myth, from Choking Hazard</p>
        <p class="mf-choke__pair"><span><small>Myth</small>“It’s safe if you do it right.”</span><span><small>Fact</small>There’s no safe way.</span></p>
        <p class="mf-choke__txt">SafeBAE’s campaign on sexual strangulation, which young people call “choking”, gives young people, parents and educators the evidence, myth-vs-fact, and the signs that need medical care.</p>
      </div>
      {btn('Choking Hazard', 'choking-hazard.html', 'mint', arrow=True)}
    </aside>
  </div>
</section>

<section class="band band--paper" id="who-is-most-at-risk">
  <div class="wrap">
    <div class="section-head"><div><p class="eyebrow">Who is most at risk?</p><h2>Identity shapes risk, and access to help</h2>
      <p class="lede lede--full">Different identities, and the intersections between them, play a big role in the risk of experiencing violence and in access to reporting and healing resources. As you read these statistics, remember that there’s a lack of research on many marginalized groups, so these numbers are subject to change, and this is in no way a comprehensive list.</p>
      <p class="mf-risk__hint">Explore the slide deck to learn more about how different marginalized groups experience heightened risk, barriers to reporting, and unequal access to support.</p></div></div>
    <div class="mf-risk">
      {player(RISK, 'Stats: marginalized groups, ten slides', '', 'mfPlayer', interval=7000)}
      <div class="mf-risk__side"><div class="mf-risk__list" role="group" aria-label="Jump to a slide">{risk_chips}</div></div>
    </div>
    <div class="mf-after"><div style="margin-bottom:18px">{help_inline(title='Free, confidential support, 24/7').replace('class="helpline"', 'class="helpline sp-help"', 1)}</div>
    {next_cards([('Support', 'Survivor support', 'Hotlines, healing resources and what to say when someone tells you.', 'survivor-support.html'),
                 ('Film + guide', 'Supporting male survivors', 'Theo Hutt’s story, and the myths that keep male survivors silent.', 'film-sexual-assault-of-men.html'),
                 ('Rights', 'Title IX', 'What your school owes you and how to ask for supportive measures.', 'title-ix.html'),
                 ('Answers', 'FAQ', 'Why survivors don’t report, rape culture, coercion and more.', 'faq.html')])}
</div>
  </div>
</section>


{give_band()}
'''
    js = r'''<script>
(function(){
  var pie = document.getElementById('mfPie');
  if(pie){ var fill = pie.querySelector('.fill'), pct = pie.querySelector('.mf-pie__pct'), msg = pie.querySelector('.mf-pie__msg'), bs = pie.querySelectorAll('.mf-pie__legend button');
    bs.forEach(function(b){ b.addEventListener('click', function(){ b.setAttribute('aria-pressed','true'); var v = +b.getAttribute('data-v');
      if(v){ fill.style.strokeDasharray = '100 100'; pie.classList.add('full'); pct.textContent = '100%'; msg.innerHTML = '<b>Rapist: 100%.</b> It happens when someone chooses to ignore or violate another person’s boundaries and consent.'; }
      else { if(!pie.classList.contains('full')) pct.textContent = '0%'; msg.innerHTML = '<b>' + b.textContent + ': 0%.</b> None of these cause sexual violence.'; } }); }); }
  var all = document.getElementById('mfAll');
  if(all) all.addEventListener('click', function(){ var fl = document.querySelectorAll('.mf-flips .flip'), on = all.getAttribute('data-on') !== '1'; fl.forEach(function(f){ f.setAttribute('aria-pressed', String(on)); }); all.setAttribute('data-on', on ? '1' : '0'); all.textContent = on ? 'Show the myths again' : 'Reveal all facts'; });
  var pl = document.getElementById('mfPlayer'), chips = document.querySelectorAll('[data-go]');
  if(pl && chips.length){ var cap = pl.querySelector('.player__cap'), nx = pl.querySelector('[data-next]'), N = pl.querySelectorAll('.player__slide').length;
    function cur(){ return (parseInt(cap.textContent, 10) || 1) - 1; }
    chips.forEach(function(c){ c.addEventListener('click', function(){ var steps = (+c.getAttribute('data-go') - cur() + N) % N; for(var i = 0; i < steps; i++) nx.click(); }); });
    new MutationObserver(function(){ var k = cur(); chips.forEach(function(c){ c.setAttribute('aria-pressed', String(+c.getAttribute('data-go') === k)); }); }).observe(cap, {childList:true, characterData:true, subtree:true}); }
})();
</script>'''
    page('myths-facts.html', 'Myths & Facts · SafeBAE',
         'SafeBAE debunks common myths about sexual assault with research and statistics, covering causes, underreporting, male survivors, and who is most at risk.',
         body, active='resources', body_class='mf', head_extra=f'<style>{SP_CSS}{HELPLINE_CSS}{MF_CSS}</style>', scripts=js)


# =====================================================================
# 4. FAQ
# =====================================================================
FAQ_CATS = [('faq-consent', 'Consent'), ('faq-violence', 'Understanding sexual violence'), ('faq-relationships', 'Healthy relationships'),
            ('faq-online', 'Online safety & nudes'), ('faq-action', 'Taking action & your rights'), ('faq-healing', 'Support & healing')]
FAQ_LONG = {  # canonical long-form posts on safebae.org (from the live WordPress site)
  'Why don’t survivors report sexual assault?': 'https://www.safebae.org/why-dont-survivors-report-sexual-assault/',
  'What is Title IX and what are my rights at school?': 'https://www.safebae.org/what-is-title-ix-student-rights/',
}
FAQ_REL = {
  'What is consent?': [('Practice in the BAE Skills Lab', 'https://skills-lab.safebae.org/'), ('Choking Hazard: why choking can’t meet the pillars of consent', 'choking-hazard.html')],
  'Can someone give consent if they’re drunk or high?': ('Myths & facts about blame', 'myths-facts.html#myths-vs-facts'),
  'What is rape culture?': ('Film: Rape Culture & a Culture of Respect', 'film-rape-culture.html'),
  'Why don’t survivors report sexual assault?': ('Why survivors don’t report', 'myths-facts.html#survivors-report'),
  'Can boys and men be victims of sexual violence?': ('Film: Supporting Male Survivors', 'film-sexual-assault-of-men.html'),
  'What are the signs of a healthy relationship?': ('Film: It’s Giving Red Flags', 'film-its-giving-red-flags.html'),
  'What are the signs of an unhealthy or abusive relationship?': ('Talk to love is respect', 'survivor-support.html#hotlines'),
  'What are the risks of sending nudes?': [('Film: #knowB4Unude', 'film-knowb4unude.html'), ('AI Literacy Training: fake images and sextortion', 'ai-literacy.html')],
  'What is bystander intervention?': ('Film: BAEcode: Game On!', 'film-baecode-game-on.html'),
  'What is Title IX and what are my rights at school?': ('Your rights under Title IX', 'title-ix.html'),
  'How do I report sexual assault? What are my options?': ('Hotlines and local help', 'survivor-support.html#hotlines'),
  'How do I support a friend who has been sexually assaulted?': ('What to say, and what not to say', 'survivor-support.html#when-someone-tells-you'),
  'How do survivors heal after sexual assault?': ('Healing resources', 'survivor-support.html#healing'),
}

FQ_CSS = '''
.fq-hero{background:var(--aqua); color:var(--slate)}
.fq-hero .wrap{padding-block:clamp(44px,5.5vw,80px) clamp(40px,5vw,64px)}
.fq-hero__grid{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,64px); align-items:center}
.fq-hero__media{position:relative; padding:24px 0 30px}
.fq-hero__media img{width:100%; aspect-ratio:5/4; object-fit:cover; border-radius:var(--r-xl); box-shadow:var(--shadow-soft)}
.fq-ask-b{position:absolute; display:inline-flex; align-items:center; gap:8px; font-family:var(--display); font-stretch:106%; font-weight:800; font-size:clamp(.92rem,1.3vw,1.05rem); line-height:1.2; padding:11px 15px; border-radius:18px; text-decoration:none; box-shadow:var(--shadow-soft); transition:transform .25s var(--ease); animation:sb-rise .9s var(--ease) both}
.fq-ask-b i{font-style:normal; transition:transform .2s var(--ease)}
.fq-ask-b:hover{transform:translateY(-3px)} .fq-ask-b:hover i{transform:translateX(3px)}
.fq-ask-b--a{left:-12px; top:0; background:#fff; color:var(--logo-teal); border-bottom-left-radius:4px; animation-delay:.45s}
.fq-ask-b--b{right:-14px; top:42%; background:var(--slate); color:#fff; border-bottom-right-radius:4px; animation-delay:.7s}
.fq-ask-b--c{left:10%; bottom:0; background:var(--mint); color:var(--slate); border-bottom-left-radius:4px; animation-delay:.95s}
@media (max-width:900px){.fq-hero__grid{grid-template-columns:1fr} .fq-hero__media{max-width:520px} .fq-ask-b--a{left:8px} .fq-ask-b--b{right:8px}}
.fq-hero .crumbs{color:var(--ink-soft)} .fq-hero .crumbs a{color:var(--logo-teal)}
.fq-hero .eyebrow{color:var(--logo-teal)}
.fq-hero h1{font-size:clamp(2.5rem,5vw,4.8rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; color:var(--logo-teal); margin:0 0 .3em}
.fq-hero .lede{max-width:none}
.fq-search{display:flex; gap:10px; align-items:center; background:#fff; border-radius:14px; padding:8px 8px 8px 18px; box-shadow:0 20px 40px -24px rgba(29,65,78,.5); border:2px solid transparent; max-width:760px}
.fq-search:focus-within{border-color:var(--teal)}
.fq-search svg{width:22px; height:22px; color:var(--teal); flex:none}
.fq-search input{flex:1; min-width:0; border:0; outline:0; font:inherit; font-size:1.1rem; color:var(--slate); background:transparent; padding:10px 0}
.fq-search button{flex:none}
.fq-count{font-family:var(--mono); font-size:.74rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft); margin:14px 0 0}
.fq-jump{position:sticky; top:76px; z-index:30; background:rgba(255,255,255,.96); backdrop-filter:blur(6px); border-bottom:1px solid var(--line)}
.fq-jump .wrap{display:flex; gap:8px; overflow-x:auto; padding-block:12px; scrollbar-width:none}
.fq-jump .wrap::-webkit-scrollbar{display:none}
.fq-jump a{flex:none; font-size:.86rem; font-weight:700; padding:8px 14px; border-radius:999px; border:1.5px solid var(--line); text-decoration:none; color:var(--slate); white-space:nowrap; background:#fff}
.fq-jump a small{font-family:var(--mono); font-size:.7rem; color:var(--logo-teal); margin-left:4px}
.fq-jump a:hover{border-color:var(--teal)}
.fq-jump a.on{background:var(--slate); color:#fff; border-color:var(--slate)} .fq-jump a.on small{color:var(--mint)}
.fq-jump a.off{opacity:.35; pointer-events:none}
.fq-cat{display:grid; grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr); gap:clamp(20px,4vw,56px); padding-block:clamp(28px,3.5vw,44px); border-top:1px solid var(--line); scroll-margin-top:140px}
.fq-cat:first-child{border-top:0; padding-top:0}
.fq-cat[hidden]{display:none}
.fq-cat__head{position:sticky; top:150px; align-self:start}
.fq-cat__head small{display:block; font-family:var(--mono); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--logo-teal); font-weight:600; margin-bottom:8px}
.fq-cat__head h2{font-size:clamp(1.6rem,2.8vw,2.4rem)}
.fq-acc details[hidden]{display:none}
.fq-acc details{scroll-margin-top:150px}
.fq-acc .acc__body p{margin:0 0 14px; font-size:1.02rem; line-height:1.65}
.fq-links{display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center}
.fq-acc mark{background:rgba(21,255,200,.45); color:inherit; border-radius:3px; padding:0 1px}
.fq-empty{padding:28px; border-radius:var(--r-xl); background:var(--mist); text-align:left}
.fq-empty h2{font-size:clamp(1.4rem,2.4vw,1.9rem)}
@media (max-width:860px){.fq-cat{grid-template-columns:1fr; gap:6px} .fq-cat__head{position:static}}
.fq-ask{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:16px; align-items:stretch}
.fq-ask > div{border-radius:var(--r-xl); padding:clamp(20px,3vw,32px); display:flex; flex-direction:column; gap:6px}
.fq-ask > div .btns{margin-top:auto; padding-top:10px}
.fq-ask__a{background:var(--mist); border:1px solid var(--line)}
.fq-ask__b{background:var(--slate); color:#fff}
.fq-ask__b p{color:rgba(255,255,255,.85)}
.fq-ask h3{margin:0}
@media (max-width:760px){.fq-ask{grid-template-columns:1fr}}
'''


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('’', '')).strip('-')[:60]


def faq():
    total = sum(len(q) for _, q in FAQ)
    jump = ''.join(f'<a href="#{cid}" data-cat="{cid}">{esc(lbl)}<small>{len(FAQ[i][1])}</small></a>' for i, (cid, lbl) in enumerate(FAQ_CATS))
    cats = []
    for i, (cat, qs) in enumerate(FAQ):
        cid, short = FAQ_CATS[i]
        dets = []
        for q, ans, link in qs:
            long = FAQ_LONG.get(q, link if link.startswith('http') else None)
            rel = FAQ_REL.get(q)
            links = ''
            if long: links += btn('Read the full answer', long, 'slate', 'sm')
            for r_ in ([rel] if isinstance(rel, tuple) else (rel or [])):
                links += a(esc(r_[0]), r_[1], 'arrow-link' if not r_[1].startswith('http') else 'link')
            dets.append(f'<details id="q-{slugify(q)}"><summary>{esc(q)}</summary><div class="acc__body"><p>{esc(ans)}</p><div class="fq-links">{links}</div></div></details>')
        cats.append(f'<section class="fq-cat" id="{cid}" data-cat="{cid}"><div class="fq-cat__head"><small>{len(qs)} question{"s" if len(qs) != 1 else ""}</small><h2>{esc(cat)}</h2></div><div class="acc fq-acc">{"".join(dets)}</div></section>')

    body = f'''
<section class="fq-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap fq-hero__grid">
    <div class="rise">
    {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('FAQ', None))}
    <h1>Frequently asked <span class="mk">questions</span></h1>
    <p class="lede">SafeBAE answers your questions about teen dating violence, sexual assault, consent, and healthy relationships.</p>
    <form class="fq-search" role="search" onsubmit="return false"><label class="sr-only" for="fq-q">Filter the questions</label>{ICON_SEARCH}<input id="fq-q" type="search" placeholder="Type to filter: consent, Title IX, nudes, report…" autocomplete="off"><button class="btn btn--slate btn--sm" type="button" id="fq-clear" hidden>Clear</button></form>
    <p class="fq-count" id="fq-count" aria-live="polite">{total} questions in {len(FAQ)} topics</p>
    </div>
    <div class="fq-hero__media">
      {img('sumact5', 'Three students talking during a SafeBAE Summer Activist Institute session', loading='eager')}
      <a class="fq-ask-b fq-ask-b--a" href="#q-what-is-consent">What is consent?<i aria-hidden="true">&rarr;</i></a>
      <a class="fq-ask-b fq-ask-b--b" href="#q-how-do-i-support-a-friend-who-has-been-sexually-assaulted">How do I support a friend?<i aria-hidden="true">&rarr;</i></a>
      <a class="fq-ask-b fq-ask-b--c" href="#q-what-is-title-ix-and-what-are-my-rights-at-school">What are my rights at school?<i aria-hidden="true">&rarr;</i></a>
    </div>
  </div>
</section>
<nav class="fq-jump" aria-label="FAQ topics"><div class="wrap">{jump}</div></nav>
<section class="band band--paper">
  <div class="wrap">
    <div id="fq-list">{''.join(cats)}</div>
    <div class="fq-empty" id="fq-empty" hidden><h2>No questions match “<span id="fq-term"></span>”.</h2><p>Try a shorter word, or search every page, film and podcast on the site.</p><div class="btns"><button class="btn btn--slate" type="button" id="fq-site">Search the whole site</button>{btn('Ask the SafeBAE team', 'contact.html', 'ghost')}</div></div>
  </div>
</section>
{vibe_band('Not sure if you crossed a line?')}
<section class="band band--paper band--tight">
  <div class="wrap fq-ask">
    <div class="fq-ask__a"><p class="eyebrow" style="margin:0">Still have a question?</p><h3>Ask the SafeBAE team</h3><p class="muted" style="margin:0">Reach the SafeBAE team with questions about our programs, trainings and resources.</p><div class="btns">{btn('Contact us', 'contact.html', 'slate', arrow=True)}{btn('Myths & facts', 'myths-facts.html', 'ghost')}</div></div>
    <div class="fq-ask__b"><p class="eyebrow" style="margin:0">Need to talk to someone?</p><h3>Free, confidential support</h3><p style="margin:0">Text LOVEIS to 22522, call 800-656-HOPE (4673), or call or text 988. Most lines are open 24/7.</p><div class="btns"><button class="btn btn--coral" type="button" data-open-help>All hotlines</button>{btn('Survivor support', 'survivor-support.html', 'ghost', arrow=True)}</div></div>
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  var inp = document.getElementById('fq-q'); if(!inp) return;
  var items = [].slice.call(document.querySelectorAll('.fq-acc details')), cats = [].slice.call(document.querySelectorAll('.fq-cat')), jl = [].slice.call(document.querySelectorAll('.fq-jump a'));
  var cnt = document.getElementById('fq-count'), empty = document.getElementById('fq-empty'), term = document.getElementById('fq-term'), clr = document.getElementById('fq-clear'), total = items.length;
  function norm(s){ return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’']/g, ''); }
  items.forEach(function(d){ d._t = norm(d.textContent); d._s = d.querySelector('summary'); d._s0 = d._s.textContent; d._p = d.querySelector('.acc__body p'); d._p0 = d._p.textContent; });
  function escH(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function mark(txt, terms){ var h = escH(txt); if(!terms.length) return h; terms.forEach(function(t){ if(t.length < 2) return; var re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'); h = h.replace(re, '<mark>$1</mark>'); }); return h; }
  function run(){ var raw = inp.value.trim(), terms = norm(raw).split(/\s+/).filter(Boolean), n = 0;
    items.forEach(function(d){ var ok = terms.every(function(t){ return d._t.indexOf(t) >= 0; }); d.hidden = !ok; if(ok) n++;
      d._s.innerHTML = mark(d._s0, terms.length ? raw.split(/\s+/) : []); d._p.innerHTML = mark(d._p0, terms.length ? raw.split(/\s+/) : []); });
    cats.forEach(function(c){ var any = !!c.querySelector('details:not([hidden])'); c.hidden = !any; });
    jl.forEach(function(l){ var c = document.getElementById(l.getAttribute('data-cat')); l.classList.toggle('off', !!(c && c.hidden)); });
    if(terms.length && n && n <= 4) items.forEach(function(d){ if(!d.hidden) d.open = true; });
    cnt.textContent = terms.length ? (n + ' of ' + total + ' questions match') : (total + ' questions in ' + cats.length + ' topics');
    empty.hidden = n > 0; term.textContent = raw; clr.hidden = !raw; }
  inp.addEventListener('input', run);
  clr.addEventListener('click', function(){ inp.value = ''; run(); inp.focus(); });
  document.getElementById('fq-site').addEventListener('click', function(){ if(window.SB && SB.openSearch) SB.openSearch(inp.value); });
  try{ var m = location.search.match(/[?&]q=([^&]+)/); if(m){ inp.value = decodeURIComponent(m[1].replace(/\+/g,' ')); run(); } }catch(e){}
  /* open a question from the hash */
  function openHash(){ var h = location.hash.slice(1); if(!h) return; var el = document.getElementById(h); if(el && el.tagName === 'DETAILS'){ el.open = true; } }
  openHash(); window.addEventListener('hashchange', openHash);
  /* active topic in the jump bar */
  if('IntersectionObserver' in window){ var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ var id = e.target.id; jl.forEach(function(l){ l.classList.toggle('on', l.getAttribute('data-cat') === id); }); } }); }, {rootMargin:'-45% 0px -50% 0px'}); cats.forEach(function(c){ io.observe(c); }); }
})();
</script>'''
    page('faq.html', 'FAQ · SafeBAE', 'Get answers to your most pressing questions on topics like consent, boundaries, and relationships from SafeBAE.',
         body, active='resources', body_class='fq', head_extra=f'<style>{SP_CSS}{FQ_CSS}</style>', scripts=js)


# =====================================================================
# 5. POSTERS
# =====================================================================
POSTERS = [  # (image, title, topic, individual download or None, format, alt)
  ('8x8-what-not-to-say-poster-pdf', 'What to say vs. what not to say', 'support', WPU + '2025/08/8x8-what-not-to-say-poster.pdf', 'PDF', 'Poster: what to say to a friend who shares they have been assaulted, and what not to say'),
  ('healing-from-trauma-3', 'Healing from a traumatic relationship', 'support', WPU + '2025/09/Healing-From-Trauma_page-0001-3.jpg', 'JPG', 'Poster: Healing from a traumatic relationship, with twelve self-care practices'),
  ('everyone-can-do-something-1', 'No one can do everything, but everyone can do something', 'support', WPU + '2025/09/Everyone-Can-Do-Something_page-0001-1-scaled.jpg', 'JPG', 'Poster: No one can do everything but everyone can do something. End rape culture.'),
  ('poster-ending-online-harassment', 'Ending online harassment is everyone’s responsibility', 'online', None, 'PNG', 'Poster: Ending online harassment is everyone’s responsibility'),
  ('no-means-no-pdf', 'No means no, but so does…', 'consent', WPU + '2024/11/no-means-no.pdf', 'PDF', 'Poster: No means no, but so does silence, “maybe later,” “I’m not sure,” being drunk, changing their mind, a power imbalance, seeming hesitant, and pressuring them. Always get enthusiastic consent.'),
  ('poster-consent-is-bae', 'Consent is BAE', 'consent', WPU + '2025/08/8x8-consent-is-bae.png', 'PNG', 'Poster: Consent is BAE, before anything else. Mutual, ongoing, sober, enthusiastic, voluntary, revocable.'),
  ('baby-consent-print-materials-1', 'Early ways to teach consent', 'consent', WPU + '2025/08/baby-consent-print-materials-1_page-0001-scaled.jpg', 'JPG', 'Poster: early ways to teach consent. Smile, high five, fist bump, handshake, hug.'),
  ('poster-sober', 'If you’ve had too much to drink…', 'consent', None, 'PDF', 'Poster: If you’ve had too much to drink, you know not to drive, but did you know the same is true for hooking up?'),
  ('poster-arousal-not-consent', 'Arousal ≠ consent', 'consent', None, 'PDF', 'Poster: Arousal does not equal consent'),
  ('poster-erection-not-consent', 'Erection ≠ consent', 'consent', None, 'PDF', 'Poster: Erection does not equal consent'),
  ('relationships-4', 'What goes into a healthy relationship?', 'relationships', WPU + '2025/09/relationships-4_page-0001-scaled.jpg', 'JPG', 'Poster: What goes into a healthy relationship? Equality at the center, surrounded by trust, respect, honesty, healthy boundaries, good communication and more.'),
  ('relationships-vs-poster-1', 'Healthy vs. unhealthy relationships', 'relationships', WPU + '2025/09/relationships-vs-Poster-1_page-0001-scaled.jpg', 'JPG', 'Poster comparing healthy and unhealthy relationship behaviors'),
  ('knowb4unude-1', 'Have you ever gotten a nude you didn’t want?', 'online', WPU + '2025/09/KnowB4Unude-1.jpg', 'JPG', 'Poster: Have you ever gotten a nude you didn’t want? #knowB4Unude'),
  ('nudes-poster-2', 'Do you trust the person you send nudes to?', 'online', WPU + '2025/08/nudes-poster-2_page-0001.jpg', 'JPG', 'Poster: Do you trust the person you send nudes to? #knowB4Unude'),
  ('nudes-poster-3', 'If a teacher catches you sharing nudes…', 'online', WPU + '2025/08/Nudes-poster-3_page-0001.jpg', 'JPG', 'Poster: Did you know that if a teacher catches you sharing nudes, they’re required to tell the police? #knowB4Unude'),
  ('poster-do-you-knowb4unude', 'Do you #knowB4Unude?', 'online', WPU + '2023/11/do-you-knowB4Unude-4.jpg', 'JPG', 'Poster: Do you #knowB4Unude? A peach emoji in a photo frame.'),
  ('all-statistics', 'Causes of rape', 'facts', WPU + '2026/07/ALL-statistics.png', 'PNG', 'Pie chart poster: causes of rape. Being under the influence, clothes, walking alone, flirty behavior and hooking up all take up none of the chart. The rapist takes up all of it.'),
  ('poster-3-false-reports', 'How often do false reports for rape occur?', 'facts', None, 'PDF', 'Poster: How often do false reports for rape occur? 3% of the time. Support survivors.'),
  ('poster-never-report', 'Half of high school victims never report', 'facts', None, 'PDF', 'Poster: 1/2 of high school victims never report. Journal of Adolescent Health.'),
  ('poster-60-percent', '60% of high school boys…', 'facts', None, 'PDF', 'Poster: 60% of high school boys find it acceptable to force sex on a girl in some circumstances. Journal of Adolescent Health.'),
  ('poster-81-percent', '81% have experienced sexual harassment', 'facts', None, 'PDF', 'Poster: By the time students are done with secondary school, 81% have experienced some sort of sexual harassment (Gruber & Fineran). Help us change that.'),
  ('poster-male-survivors', 'Guys are more likely to be assaulted than falsely accused', 'facts', None, 'PDF', 'Poster: Statistically, guys are more likely to be sexually assaulted than they are to be falsely accused of rape.'),
]
PO_TOPICS = [('all', 'All posters'), ('consent', 'Consent'), ('relationships', 'Relationships'), ('online', 'Nudes & online'), ('support', 'Support & action'), ('facts', 'Facts & figures')]

PO_CSS = '''
.related{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px}
@media (max-width:860px){.related{grid-template-columns:1fr}}
.po-hero{background:var(--slate) var(--grain); color:#fff}
.po-hero__grid{display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(48px,6vw,88px)}
.po-hero h1{font-size:clamp(2.3rem,4.8vw,4.4rem); font-stretch:122%; font-weight:900; text-transform:uppercase; line-height:.9; letter-spacing:-.02em; margin:0 0 .3em}
.po-hero .lede{color:rgba(255,255,255,.88); max-width:none}
.po-fan{position:relative; height:clamp(300px,36vw,470px)}
.po-fan figure{position:absolute; margin:0; width:44%; aspect-ratio:3/4; background:#fff; padding:8px; border-radius:6px; box-shadow:0 26px 50px -22px rgba(0,0,0,.7); transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.po-fan figure img{width:100%; height:100%; object-fit:cover; border-radius:3px}
.po-fan figure::before{content:""; position:absolute; top:-10px; left:50%; width:70px; height:22px; margin-left:-35px; background:rgba(21,255,200,.75); transform:rotate(-3deg); z-index:2}
.po-fan figure:nth-child(1){left:0; top:14%; transform:rotate(-10deg)}
.po-fan figure:nth-child(2){left:28%; top:2%; transform:rotate(-1deg); z-index:2}
.po-fan figure:nth-child(3){left:56%; top:12%; transform:rotate(8deg); z-index:1}
.po-fan:hover figure:nth-child(1){transform:rotate(-14deg) translateX(-10px)} .po-fan:hover figure:nth-child(3){transform:rotate(12deg) translateX(10px)}
.po-fan .sticker{position:absolute; right:2%; bottom:6%; z-index:3}
@media (max-width:860px){.po-hero__grid{grid-template-columns:1fr} .po-fan{height:clamp(240px,64vw,380px); max-width:520px}}
.po-ch{overflow:hidden; padding-top:14px}
.po-tape{display:flex; gap:0; white-space:nowrap; margin-bottom:var(--band); background:repeating-linear-gradient(-45deg, var(--slate) 0 16px, var(--mint) 16px 32px); padding:7px 0; transform:rotate(-1.2deg) scale(1.03); transform-origin:center}
.po-tape span{flex:none; font-family:var(--display); font-weight:900; font-stretch:118%; text-transform:uppercase; font-size:.95rem; letter-spacing:.04em; color:var(--slate); background:#fff; padding:5px 18px; margin-right:40px}
.po-ch__grid{display:grid; grid-template-columns:auto minmax(0,1fr); gap:clamp(28px,5vw,72px); align-items:center}
.po-ch__label{width:clamp(250px,28vw,380px); padding:8px}
@media (max-width:760px){.po-ch__grid{grid-template-columns:1fr} .po-ch__label{width:min(300px,100%)}}
.po-tools{display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:14px 24px; margin-bottom:24px}
.po-grid{display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:18px}
.po-card{display:flex; flex-direction:column; background:#fff; border:1px solid var(--line); border-radius:var(--r-xl); overflow:hidden; min-width:0; transition:box-shadow .2s, transform .2s}
.po-card:hover{box-shadow:var(--shadow-soft); transform:translateY(-3px)}
.po-card[hidden]{display:none}
.po-card__img{position:relative; display:block; aspect-ratio:1; background:var(--mist); border:0; padding:0; cursor:zoom-in; width:100%; overflow:hidden}
.po-card__img img{position:absolute; left:16px; top:16px; width:calc(100% - 32px); height:calc(100% - 32px); object-fit:contain; filter:drop-shadow(0 10px 12px rgba(29,65,78,.28)); transition:transform .35s}
.po-card__img:hover img{transform:scale(1.04) rotate(-1deg)}
.po-card__body{padding:14px 16px 16px; display:flex; flex-direction:column; gap:10px; flex:1}
.po-card__body b{font-family:var(--display); font-stretch:106%; font-weight:800; font-size:1.02rem; line-height:1.2}
.po-card__foot{margin-top:auto; display:flex; justify-content:space-between; align-items:center; gap:8px; flex-wrap:wrap}
.po-dl{font-weight:700; font-size:.88rem; color:var(--logo-teal); text-decoration:underline; text-decoration-color:var(--mint); text-decoration-thickness:2px; text-underline-offset:3px}
.po-dl--zip{color:var(--ink-soft); text-decoration-color:var(--gray)}
@media (max-width:1060px){.po-grid{grid-template-columns:repeat(3,minmax(0,1fr))}} @media (max-width:720px){.po-grid{grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px} .po-card__img img{left:10px; top:10px; width:calc(100% - 20px); height:calc(100% - 20px)} .po-card__body{padding:12px}}
.po-card.po-zip{grid-column:span 2; background:var(--slate); color:#fff; border-color:var(--slate); padding:clamp(20px,3vw,32px); justify-content:space-between; gap:18px}
.po-zip .eyebrow{color:var(--mint)}
.po-zip b{display:block; font-family:var(--display); font-weight:900; font-stretch:115%; font-size:clamp(1.6rem,3vw,2.4rem); line-height:1}
.po-zip p{margin:10px 0 0; color:#fff}
.po-zip .btn{align-self:flex-start}
'''


def posters():
    counts = {k: (len(POSTERS) if k == 'all' else sum(1 for p in POSTERS if p[2] == k)) for k, _ in PO_TOPICS}
    chips_ = ''.join(f'<button type="button" data-t="{k}" aria-pressed="{str(k == "all").lower()}">{esc(l)}<small>{counts[k]}</small></button>' for k, l in PO_TOPICS)
    cards = []
    for n, t, topic, dl, fmt, alt in POSTERS:
        foot = (a(f'Download ({fmt})', dl, 'po-dl') if dl else a('In the full set (.zip)', POSTERS_ZIP, 'po-dl po-dl--zip'))
        cards.append(f'<article class="po-card" data-t="{topic}"><button type="button" class="po-card__img" data-src="{imgsrc(n)}" data-cap="{esc(t)}" aria-label="Enlarge poster: {esc(t)}">{img(n, alt)}</button>'
                     f'<div class="po-card__body"><b>{esc(t)}</b><div class="po-card__foot">{foot}</div></div></article>')
    fan = ''.join(f'<figure>{img(n, "", loading="eager")}</figure>' for n in ['relationships-vs-poster-1', 'baby-consent-print-materials-1', 'everyone-can-do-something-1'])
    body = f'''
<section class="po-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap po-hero__grid">
    <div class="rise">
      {crumbs(('Home', 'index.html'), ('Library', 'library.html'), ('Posters', None))}
      <p class="eyebrow">Free to print &amp; share</p>
      <h1>Shareable prevention <span class="mk">posters</span></h1>
      <p class="lede">Our posters are easy-to-share educational materials that can help reinforce key messages around consent, healthy relationships, boundaries, and student support. They work well in classrooms, counseling offices, hallways, wellness centers, and student spaces.</p>
      <div class="btns">{btn('Download all posters (.zip)', POSTERS_ZIP, 'mint')}{btn('Teaching guides', 'library.html#guides', 'ghost', arrow=True)}</div>
    </div>
    <div class="po-fan" aria-hidden="true">{fan}<span class="sticker sticker--r">Free</span></div>
  </div>
</section>
<section class="band band--paper" id="gallery">
  <div class="wrap">
    <div class="po-tools"><div class="sp-chips" role="group" aria-label="Filter posters by topic" id="po-filter">{chips_}</div><p class="small muted" style="margin:0">Tap a poster to see it full size.</p></div>
    <div class="po-grid" id="po-grid">{''.join(cards)}<article class="po-card po-zip" data-t="all"><div><p class="eyebrow">The full set</p><b>21 posters in one free download</b><p>Every poster above as PDFs and images in one .zip. No Means No is a separate PDF, linked on its card.</p></div>{btn('Download the .zip', POSTERS_ZIP, 'mint')}</article></div>
  </div>
</section>
<section class="band band--deep po-ch" id="choking-hazard-posters">
  <div class="po-tape" aria-hidden="true"><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span><span>There’s no safe way to choke someone</span></div>
  <div class="wrap po-ch__grid">
    <div class="po-ch__label">{hz_label("hz--tilt")}</div>
    <div>
      <p class="eyebrow">Free from Choking Hazard</p>
      <h2>Warning posters on sexual strangulation</h2>
      <p class="lede" style="color:rgba(255,255,255,.9)">Choking Hazard is SafeBAE’s campaign on sexual strangulation, which young people call “choking”. Its free warning posters and warning sticker are available to download from the campaign site.</p>
      <div class="btns">{btn('Download the warning posters', 'https://chokinghazard.org/resources/#downloads', 'mint')}{btn('About the campaign', 'choking-hazard.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>
<section class="band band--paper">
  <div class="wrap">
    <div class="section-head"><div><h2>Pair a poster with a film and guide</h2></div>{btn('The full library', 'library.html', 'slate', arrow=True)}</div>
    {related(['red-flags', 'knowb4unude', 'male-survivors'])}
    <div style="margin-top:26px">{help_inline(title='Free, confidential support, 24/7').replace('class="helpline"', 'class="helpline sp-help"', 1)}</div>
  </div>
</section>
{give_band()}
'''
    js = r'''<script>
(function(){
  var f = document.getElementById('po-filter'), grid = document.getElementById('po-grid'); if(!f || !grid) return;
  var bs = f.querySelectorAll('button'), cards = [].slice.call(grid.querySelectorAll('.po-card:not(.po-zip)'));
  bs.forEach(function(b){ b.addEventListener('click', function(){ var t = b.getAttribute('data-t'); bs.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); }); cards.forEach(function(c){ c.hidden = !(t === 'all' || c.getAttribute('data-t') === t); }); var z = grid.querySelector('.po-zip'); if(z) z.hidden = t !== 'all'; }); });
  grid.addEventListener('click', function(e){ var b = e.target.closest('.po-card__img'); if(!b || !window.SB || !SB.openLightbox) return; var vis = cards.filter(function(c){ return !c.hidden; }).map(function(c){ return c.querySelector('.po-card__img'); });
    SB.openLightbox(vis.map(function(x){ return {src:x.getAttribute('data-src'), cap:x.getAttribute('data-cap')}; }), vis.indexOf(b)); });
})();
</script>'''
    page('posters.html', 'Posters · SafeBAE', 'Download posters on consent, boundaries, and prevention. Free visuals for classrooms, schools, and student spaces.',
         body, active='library', body_class='po', head_extra=f'<style>{SP_CSS}{HELPLINE_CSS}{PO_CSS}</style>', scripts=js)


# =====================================================================
# 6. BLOG
# =====================================================================
BLOG_LEAD = ('Vibe Check: A tool for perpetrators, from survivors', '2026-05-29', 'https://www.safebae.org/vibe-check-a-tool-for-perpetrators-from-survivors/', 'blog-vibe-check-a-tool-for-perpetrators-from-surv')
BLOG_SECTIONS = [
  ('explainers', 'Media analysis & explainers', [('All explainers', 'https://www.safebae.org/category/cultural-analysis-explainers/')], [
    ('The Real Crisis Behind the Manosphere', '2026-03-17', 'https://www.safebae.org/what-is-the-manosphere-online-misogyny/', 'blog-what-is-the-manosphere-online-misogyny'),
    ('ANTM on Netflix: Consent & Rape Culture', '2026-02-26', 'https://www.safebae.org/antm-on-netflix-sexual-violence-edited-as-entertainment/', 'blog-antm-on-netflix-sexual-violence-edited-as-en'),
    ('How Are Young People Learning About Sex and Consent Online And Why Is It Important?', '2026-01-26', 'https://www.safebae.org/how-are-young-people-learning-about-sex-and-consent-online-and-why-is-it-important/', 'blog-how-are-young-people-learning-about-sex-and'),
    ('Rape Culture, Then And Now: What Have We Learned?', '2025-11-18', 'https://www.safebae.org/rape-culture-then-and-now-what-have-we-learned/', 'blog-rape-culture-then-and-now-what-have-we-learn')]),
  ('policy', 'Policy & legal news', [('All policy & legal news', 'https://www.safebae.org/category/policy-legal-news/')], [
    ('New York Just Passed a Bill to Protect Minors from Unsafe AI Chatbots.', '2026-07-02', 'https://www.safebae.org/new-york-just-passed-a-bill-to-protect-minors-from-unsafe-ai-chatbots/', 'blog-new-york-just-passed-a-bill-to-protect-minor'),
    ('Why Students Walk Out: The Westlake High Protest and the Power of Youth Activism', '2025-05-06', 'https://www.safebae.org/why-students-walk-out-the-westlake-high-protest-and-the-power-of-youth-activism/', 'blog-why-students-walk-out-the-westlake-high-prot'),
    ('Tennessee Bill to Guarantee Teen Rape Kits Fails in Committee', '2025-05-01', 'https://www.safebae.org/tennessee-bill-to-guarantee-teen-rape-kits-fails-in-committee/', 'blog-tennessee-bill-to-guarantee-teen-rape-kits-f'),
    ('Consent Education Wins in Indiana After Students Speak Out', '2025-04-25', 'https://www.safebae.org/consent-education-wins-in-indiana-after-students-speak-out/', 'blog-consent-education-wins-in-indiana-after-stud')]),
  ('culture', 'Culture news & commentary', [('All culture news', 'https://www.safebae.org/category/culture-news-commentary/')], [
    ('Sedona Prince Goes Undrafted in 2025 WNBA Draft After Year of Assault Allegations', '2025-04-15', 'https://www.safebae.org/sedona-prince-goes-undrafted-in-2025-wnba-draft-after-year-of-assault-allegations/', 'blog-sedona-prince-goes-undrafted-in-2025-wnba-dr'),
    ('A Rape Game Was Live on Steam. That Should Tell Us Everything.', '2025-04-11', 'https://www.safebae.org/a-rape-game-was-live-on-steam-that-should-tell-us-everything/', 'blog-a-rape-game-was-live-on-steam-that-should-te'),
    ('What Drake & Josh’s Reunion Teaches Us About Supporting Survivors', '2025-03-26', 'https://www.safebae.org/what-drake-joshs-reunion-teaches-us-about-supporting-survivors/', 'blog-what-drake-joshs-reunion-teaches-us-about-su'),
    ('Jack Wright, Sienna Mae, and the Urgent Need for Consent Education', '2025-01-21', 'https://www.safebae.org/jack-wright-sienna-mae-and-the-urgent-need-for-consent-education/', 'blog-jack-wright-sienna-mae-and-the-urgent-need-f')]),
  ('programs', 'Programs, partnerships & school visits', [('Programs', 'https://www.safebae.org/category/programs/'), ('School visits & trainings', 'https://www.safebae.org/category/school-visits-trainings/')], [
    ('Launching Leaders: How SafeBAE Alumni Took the Healthy Youth Conference Stage', '2025-04-30', 'https://www.safebae.org/launching-leaders-how-safebae-alumni-took-the-healthy-youth-conference-stage/', 'blog-launching-leaders-how-safebae-alumni-took-th'),
    ('SafeBAE Joins HopSkipDrive’s Safety Advisory Board', '2025-04-26', 'https://www.safebae.org/safebae-joins-hopskipdrives-safety-advisory-board/', 'blog-safebae-joins-hopskipdrives-safety-advisory'),
    ('Kicking Off Our Whole-School Approach with Alliance Public Schools in Los Angeles', '2025-04-14', 'https://www.safebae.org/kicking-off-our-whole-school-approach-with-alliance-public-schools-in-los-angeles/', 'blog-kicking-off-our-whole-school-approach-with-a'),
    ('SafeBAE Brings Consent Education to Middle Schoolers at Belmont Day School', '2025-03-10', 'https://www.safebae.org/safebae-brings-consent-education-to-middle-schoolers-at-belmont-day-school/', 'blog-safebae-brings-consent-education-to-middle-s')]),
]
BLOG_TOPICS = [('Title IX', 'https://www.safebae.org/category/title-ix/'), ('Vibe Check', 'https://www.safebae.org/category/vibe-check/'),
               ('Stories', 'https://www.safebae.org/category/blog/stories/'), ('News', 'https://www.safebae.org/category/blog/news/'),
               ('FAQ answers', 'https://www.safebae.org/category/faq/'), ('Every post', 'https://www.safebae.org/category/blog/')]
SUBSTACK_POSTS = [('Vibe Check by SafeBAE', 'A tool for perpetrators, from survivors.', 'https://safebae.substack.com/p/vibe-check'),
                  ('When you Ask AI for Advice, and It Just Agrees with You…', 'A new study shows why that is a problem.', 'https://safebae.substack.com/p/when-you-ask-ai-for-advice-and-it'),
                  ('New York Just Passed a Bill to Protect Minors from Unsafe AI Chatbots.', 'Here is why that matters for consent and accountability.', 'https://safebae.substack.com/p/new-york-just-passed-a-bill-to-protect')]

BL_CSS = '''
.bl-hero{background:var(--slate) var(--grain); color:#fff}
.bl-hero__grid{display:grid; grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr); gap:clamp(28px,5vw,64px); align-items:center; padding-block:clamp(44px,6vw,84px)}
.bl-mast{font-family:var(--display); font-weight:900; font-stretch:118%; text-transform:uppercase; font-size:clamp(3rem,6vw,5.6rem); line-height:.82; letter-spacing:-.03em; margin:0 0 .25em}
.bl-hero .lede{color:rgba(255,255,255,.9); max-width:none}
.bl-warn{display:flex; gap:10px; align-items:flex-start; margin:0 0 16px; padding:12px 14px; border-radius:10px; background:rgba(255,255,255,.06); border:1px solid var(--line-dark); font-size:.9rem; color:var(--aqua)}
.bl-warn b{color:#fff}
.bl-warn button{margin-left:auto; flex:none; font:inherit; font-size:.8rem; font-weight:800; background:var(--coral); color:var(--slate); border:0; border-radius:5px; padding:4px 10px; cursor:pointer}
.bl-lead{display:grid; text-decoration:none; color:#fff; background:var(--slate-deep); border-radius:var(--r-xl); overflow:hidden; box-shadow:var(--shadow-soft); transition:transform .25s}
.bl-lead:hover{transform:translateY(-4px)}
.bl-lead__img{aspect-ratio:16/9; overflow:hidden}
.bl-lead__img img{width:100%; height:100%; object-fit:cover; transition:transform .6s}
.bl-lead:hover .bl-lead__img img{transform:scale(1.03)}
.bl-lead__body{padding:20px 22px 22px; display:grid; gap:8px}
.bl-lead__body small{font-family:var(--mono); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mint); font-weight:600}
.bl-lead__body b{font-family:var(--display); font-stretch:110%; font-size:clamp(1.4rem,2.4vw,2rem); line-height:1.08}
.bl-lead__body span{color:rgba(255,255,255,.82); font-size:.95rem}
@media (max-width:900px){.bl-hero__grid{grid-template-columns:1fr}}
.bl-sec .section-head{border-top:4px solid var(--slate); padding-top:16px}
.band--deep.bl-sec .section-head{border-color:var(--mint)}
.bl-sec h2{font-size:clamp(1.8rem,3.4vw,2.9rem)}
.bl-sec .btns{gap:8px}
.bl-topics{display:flex; flex-wrap:wrap; align-items:center; gap:10px 14px}
.bl-topics b{font-family:var(--display); font-stretch:108%; font-size:1.2rem; margin-right:6px}
.bl-topbar{display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px 28px}
.bl-new{display:inline-flex; align-items:center; gap:10px; max-width:460px; text-decoration:none; color:var(--slate); font-weight:700; font-size:.9rem; line-height:1.35; padding:10px 14px; border-radius:14px; background:#fff; border:1px solid var(--line)}
.bl-new b{flex:none; font-family:var(--mono); font-size:.64rem; letter-spacing:.12em; text-transform:uppercase; background:var(--slate); color:var(--mint); padding:3px 7px; border-radius:4px}
.bl-new i{font-style:normal; transition:transform .2s var(--ease)} .bl-new:hover i{transform:translateX(3px)} .bl-new:hover span{text-decoration:underline; text-underline-offset:3px}
.bl-two{display:grid; grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr); gap:16px; align-items:stretch}
.bl-sub,.bl-write{border-radius:var(--r-xl); padding:clamp(22px,3vw,36px); display:flex; flex-direction:column; min-width:0}
.bl-sub{background:var(--teal); color:#fff}
.bl-sub h2,.bl-write h2{font-size:clamp(1.7rem,3vw,2.5rem)}
.bl-sub .eyebrow{color:var(--aqua)}
.bl-sub .rows{margin:6px 0 20px; border-color:rgba(255,255,255,.25)}
.bl-sub .row{border-color:rgba(255,255,255,.25)}
.bl-sub .row:hover{background:rgba(255,255,255,.08)}
.bl-sub .row b{color:#fff} .bl-sub .row small{color:#fff}
.bl-sub .btns,.bl-write .btns{margin-top:auto}
.bl-write{background:var(--aqua); color:var(--slate)}
.bl-write p{margin:0 0 18px}
@media (max-width:900px){.bl-two{grid-template-columns:1fr}}
@media (max-width:560px){.bl-sec .sp-posts{grid-template-columns:none; grid-auto-flow:column; grid-auto-columns:80%; overflow-x:auto; scroll-snap-type:x mandatory; padding-bottom:10px; scrollbar-width:thin} .bl-sec .sp-post{scroll-snap-align:start}}
'''


def blog():
    secs = []
    for i, (k, title, links, posts) in enumerate(BLOG_SECTIONS):
        band = 'band--paper' if i % 2 == 0 else 'band--deep'
        lb = ''.join(btn(t, u, 'ghost', 'sm') for t, u in links)
        secs.append(f'''<section class="band {band} band--tight bl-sec" id="{k}"><div class="wrap">
<div class="section-head"><div><h2>{esc(title)}</h2></div><div class="btns">{lb}</div></div>
<div class="sp-posts">{''.join(post_card(*p) for p in posts)}</div></div></section>''')
    topics = ''.join(f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)} &#8599;</a>' for t, u in BLOG_TOPICS)
    subs = ''.join(row(t, d, u) for t, d, u in SUBSTACK_POSTS)
    t, d, u, th = BLOG_LEAD
    body = f'''
<section class="bl-hero sp-hero">
  <span class="wm-daisy" aria-hidden="true"></span>
  <div class="wrap bl-hero__grid">
    <div class="rise">
      {crumbs(('Home', 'index.html'), ('Resources', 'resources.html'), ('Blog', None))}
      <p class="eyebrow">The SafeBAE blog</p>
      <h1 class="bl-mast">News &amp;<br><span class="mk">stories</span></h1>
      <p class="lede">Read stories from survivors, stay updated with SafeBAE, and share what you learn with your friends.</p>
      <p class="bl-warn"><span><b>Content note:</b> material posted may contain sensitive language. Reader discretion is advised.</span><button type="button" data-open-help>Get help</button></p>
      <div class="btns">{btn('Submit an article', JOTFORM, 'mint')}{btn('Get the newsletter', SUBSTACK, 'ghost')}</div>
    </div>
    <a class="bl-lead" href="{esc(u)}" target="_blank" rel="noopener">
      <span class="bl-lead__img">{img(th, '', loading='eager')}</span>
      <span class="bl-lead__body"><small>Featured &middot; Vibe Check &middot; {month(d)}</small><b>{esc(t)}</b><span>A free and anonymous tool for young people who are worried they may have crossed a boundary or caused harm.</span><span style="color:var(--mint);font-weight:700">Read on safebae.org &#8599;</span></span>
    </a>
  </div>
</section>
{''.join(secs)}
<section class="band band--aqua band--tight">
  <div class="wrap bl-topbar"><div class="bl-topics sp-chips"><b>Browse by topic</b>{topics}</div><a class="bl-new" href="ai-literacy.html"><b>New</b><span>The SafeBAE AI Literacy Training launches during U.S. Media Literacy Week, October 26–30</span><i aria-hidden="true">&rarr;</i></a></div>
</section>
<section class="band band--paper">
  <div class="wrap bl-two">
    <div class="bl-sub">
      <p class="eyebrow">SafeBAE on Substack</p>
      <h2>Get the newsletter</h2>
      <div class="rows">{subs}</div>
      <div class="btns">{btn('Subscribe on Substack', SUBSTACK, 'mint')}{btn('Explore Vibe Check', 'vibe-check.html', 'white', arrow=True)}</div>
    </div>
    <div class="bl-write">
      <h2>Submit an article</h2>
      <p>If you would like to submit an article of your own to SafeBAE, send it through our submission form.</p>
      <div class="btns">{btn('Submit an article', JOTFORM, 'slate')}{btn('Contact us', 'contact.html', 'ghost', arrow=True)}</div>
    </div>
  </div>
</section>
{give_band()}
'''
    page('blog.html', 'Blog · SafeBAE', 'SafeBAE’s blog: media analysis, policy and legal news, culture commentary, and stories from schools on consent and sexual violence prevention.',
         body, active='resources', body_class='bl', head_extra=f'<style>{SP_CSS}{BL_CSS}</style>')


def build():
    survivor_support()
    title_ix()
    myths_facts()
    faq()
    posters()
    blog()


if __name__ == '__main__':
    build()
