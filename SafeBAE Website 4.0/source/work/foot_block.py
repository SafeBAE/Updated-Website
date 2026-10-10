FOOT_COLS = [
  ('Students', [('For Students','students.html'),('SafeBAE Clubs','clubs.html'),('Club Hub','https://clubs.safebae.org'),('Peer Educator Training','peer-educator.html'),('AI Literacy Training','ai-literacy.html'),('Summer Activist Institute','summer-institute.html'),('Reform Your Policy','reform-policy.html'),('En Español','espanol.html')]),
  ('Adults', [('For Adults','adults.html'),('Parents & Caregivers','parents.html'),('Educators','educators.html'),('College Students','college.html'),
              ('!Give', ''), ('Donate','donate.html'),('Chip In','chip-in.html'),('Fundraise','fundraise.html')]),
  ('Request a Program', [('All programs','request-a-program.html'),('Assemblies','assemblies.html'),('360° Schools','360-schools.html'),('Consent Curriculum','consent-curriculum.html'),('Faculty & Staff Training','professional-development.html'),('Policy Reform Guide','policy-reform-guide.html'),('Accountability Training','accountability-training.html'),('Strangulation Prevention','choking-hazard.html#schools')]),
  ('Resources', [('Resources Hub','resources.html'),('The Library','library.html'),('Posters','posters.html'),('Vibe Check','vibe-check.html'),('BAE Skills Lab','skills-lab.html'),('Choking Hazard','choking-hazard.html'),('#KnowB4UNude','film-knowb4unude.html'),('Blog','blog.html')]),
  ('Support & answers', [('Survivor Support','survivor-support.html'),('Hotlines','survivor-support.html#hotlines'),('Title IX','title-ix.html'),('Myths & Facts','myths-facts.html'),('FAQ','faq.html'),
              ('!#ForDaisy', ''), ('Remembering Daisy','fordaisy.html'),('Tattoos & Healing','fordaisy-tattoos.html')]),
  ('About', [('About SafeBAE','about.html'),('Our Team','team.html'),('Data & Impact','impact.html'),('Partners & Press','partners-press.html'),('Contact','contact.html'),
              ('!Shop', ''), ('Educational products','https://safebae.podia.com/'),('Digital Bookshop','https://bookshop.org/shop/SafeBAE')]),
]

SOCIAL = [
  ('Instagram', 'https://www.instagram.com/safe_bae/', '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3.2" y="3.2" width="17.6" height="17.6" rx="5"/><circle cx="12" cy="12" r="4.1"/><circle cx="17.2" cy="6.8" r="1.15" fill="currentColor" stroke="none"/></svg>'),
  ('TikTok', 'https://www.tiktok.com/@safe_bae', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'),
  ('YouTube', 'https://www.youtube.com/@SafeBAE', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.28 5 12 5 12 5s-6.28 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.76 1.77C5.72 19 12 19 12 19s6.28 0 7.84-.43a2.5 2.5 0 0 0 1.76-1.77A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8ZM10 15V9l5.2 3Z"/></svg>'),
  ('LinkedIn', 'https://www.linkedin.com/company/safebae/', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.94 8.5H3.56V20h3.38zM5.25 3.5a1.96 1.96 0 1 0 0 3.92 1.96 1.96 0 0 0 0-3.92ZM20.44 20v-6.3c0-3.1-1.65-4.54-3.86-4.54a3.33 3.33 0 0 0-3.02 1.66V8.5h-3.37V20h3.37v-6c0-1.2.6-2.05 1.76-2.05 1.1 0 1.74.78 1.74 2.05v6z"/></svg>'),
  ('Substack', 'https://substack.com/@safebae', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3.6h16v2.5H4zm0 4.7h16v2.5H4zM4 13h16v8.4l-8-4.5-8 4.5z"/></svg>'),
  ('Facebook', 'https://www.facebook.com/www.safebae.org', '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.6 21.5v-8h2.7l.4-3.2h-3.1V8.3c0-.92.26-1.55 1.58-1.55h1.7V3.9a22 22 0 0 0-2.46-.13c-2.44 0-4.1 1.49-4.1 4.22v2.31H7.6v3.2h2.72v8z"/></svg>'),
]

def footer():
    def col(t, links):
        out = f'<div class="fcol"><h4>{esc(t)}</h4><ul>'
        for l, h in links:
            if l.startswith('!'):
                out += f'</ul><h4 class="fcol__sub">{esc(l[1:])}</h4><ul>'
            else:
                out += f'<li>{a(esc(l), h, "ext" if h.startswith("http") else "")}</li>'
        return out + '</ul></div>'
    cols = ''.join(col(t, links) for t, links in FOOT_COLS)
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="SafeBAE on {n}" title="{n}">{svg}</a>' for n, u, svg in SOCIAL)
    return f'''
<section class="support-strip" aria-label="Support resources">
  <div class="wrap">
    <b>Need support right now?</b>
    <div class="nums"><span>Text <strong>LOVEIS</strong> to 22522</span><span>Call <strong>800-656-HOPE</strong></span><span>Call or text <strong>988</strong></span><span>LGBTQ+ youth: text <strong>START</strong> to 678-678</span></div>
    <button data-open-help>All hotlines</button>
  </div>
</section>
<footer class="site-footer">
  <span class="footer-daisy" aria-hidden="true"></span>
  <div class="wrap">
    <a class="footer-mark" href="index.html" aria-label="SafeBAE: Safe Before Anyone Else"><span class="fm-l fm-l1"><b>Safe</b> <b>B</b><i>efore</i></span><span class="fm-l fm-l2"><b>A</b><i>nyone</i> <b>E</b><i>lse.</i></span></a>
    <div class="footer-lead">
      <div class="footer-brand">{LOGO_SVG}<p>The only survivor-founded, youth-led organization working to end sexual violence among middle and high school students nationwide.</p></div>
      <div class="footer-act">
        <div class="btns">{btn('Donate', 'donate.html', 'mint')}{btn('Get the newsletter', 'https://substack.com/@safebae', 'ghost')}</div>
        <div class="socials">{soc}</div>
      </div>
    </div>
    <nav class="footer-cols" aria-label="Footer">{cols}</nav>
    <div class="footer-bottom">
      <div class="candid">{img('candid-platinum-seal-of-transparency-1-0', 'Candid Platinum Seal of Transparency 2025')}<span>SafeBAE is a registered 501(c)(3) nonprofit.<br>EIN 81-5451147 &middot; 7 Evelyn Drive, Bristol, RI 02809</span></div>
      <div class="footer-legal"><span>&copy; 2026 SafeBAE</span>{a('Photo credits','credits.html')}<a class="footer-up" href="#top"><span class="daisy" aria-hidden="true"></span>Back to top</a></div>
    </div>
  </div>
</footer>'''

