# SafeBAE website 2.0

The second version of the rebuilt safebae.org: 47 pages. Version 1 sits untouched next to this folder (`../site`).

## Open it

- **Quick look:** open `site/index.html` in Chrome or Safari. Pages, images, menus, search, tabs, players and the new interactives all work from your computer.
- **Embeds:** YouTube, Spotify, Zeffy, Google Forms and Calendly load only when the site is served from a real web address. Opened from your computer, those spots show a button that opens the same video, episode or form in a new tab.
- **Online preview:** the same build is published as a private Claude artifact, "SafeBAE Site 2.0". Links between pages swap the page in place there, so the browser Back button doesn't step between pages.

## What's new in 2.0

**New pages**

| Page | File | What it is |
|---|---|---|
| AI Literacy Training | `ai-literacy.html` | The six modules (with times and screen counts from the live training), the Four-Step Check, how accounts and certificates work, educator group access, privacy, support lines. Styled after the training's own hand-drawn look. |
| Choking Hazard | `choking-hazard.html` | The campaign on sexual strangulation: the evidence with its sources, force and timing charts, peel-to-reveal myth vs. fact, consent, media ratings, the short film, when to go to the ER, hotlines, posters, and the Sexual Strangulation Prevention program for schools. |
| Tattoos & Healing | `fordaisy-tattoos.html` | Daisy's tattoo art through tribute-wall quotes, what survivors and researchers describe, a consultation checklist, cover-up programs in the news, and support for anyone a tattoo isn't right for. |

**Across the site**

- **#ForDaisy is a main tab** in the header, with Remembering Daisy, Tattoos & Healing, the tribute wall and Add your message.
- **A mint announcement ribbon** under the header rotates the AI Literacy Training launch and Choking Hazard. Visitors can close it.
- **Mentions of the new programs** where they fit each audience: home, students, peer educator, clubs, adults, parents, educators, college, request a program, 360° Schools and its subpages, resources, survivor support, myths & facts, FAQ, posters, blog, library, Vibe Check and four film pages. The Sexual Strangulation Prevention program (November 2026) appears only on school and educator pages and on the Choking Hazard page.
- **One visual system:** every hero has imagery, a slowly turning daisy watermark and a rising entrance; one mint "marker" word per headline; light and dark sections alternate; consistent corner radii and shadows; grain on dark bands; decorative eyebrow labels removed; coral kept to support and urgency.
- **One Choking Hazard label** everywhere it appears: the campaign's own yellow warning label (its yellow is used only on that label).
- **Footer** opens with a large "Safe Before Anyone Else" wordmark.
- **Per-page upgrades**, for example: a scroll-filled milestone line on About, a clickable team mosaic, count-up impact numbers, a 7-in-10 Title IX pictograph, an animated teacher-pilot chart, a live Red-to-Green sort on It's Giving Red Flags, and a daisy that blooms when someone posts to the tribute wall.
- **Phones:** every page fits screens from 320px wide with no sideways scrolling.

## Please check these before launch

- **Forms still don't submit anywhere.** The tribute message, contact and program request forms open an email draft on a live site. Connect them to a form service before launch, especially the tribute wall.
- **AI Literacy Training pictures:** the screenshots on `ai-literacy.html` were taken from the live training at ai-literacy.safebae.org. The training's content sits behind its sign-up screen; no account was created, the sign-up box was hidden in a private browser window to capture what was already on the page. Replace them if the training's screens change before launch.
- **Take It Down wording:** the training describes Take It Down as "free removal of intimate images of anyone under 18." Take It Down's own site says it helps remove images taken before age 18 from participating platforms. The new page uses Take It Down's wording; the training may want the same change.
- **Choking Hazard facts** were checked against chokinghazard.org and the studies it cites. Two things to know:
  - chokinghazard.org/learn-more/ currently shows placeholder text, so the new page links to the campaign homepage and its resources page instead.
  - The "about 20 pounds to open a can" figure is credited to Armstrong & Strack (2016), as on chokinghazard.org. It is widely used in strangulation training, but it wasn't possible to confirm the exact figure in that paper.
- **Tattoo laws for minors** on `fordaisy-tattoos.html` come from a 2013 state-law review (17 states banned tattooing under 18; 28 required a parent's consent). The page tells readers to check their own state.
- **Cover-up programs** (Phoenix Ink & Beauty's Art of Healing, Flavia Carvalho, Sacred Transformations) are presented as examples from news reporting, not SafeBAE partners. Confirm they are still running before promoting them further.
- **New photo:** `accountability-training.html` uses an Unsplash photo of hands at a laptop (MJ Duford), credited on `credits.html`.
- **Everything on version 1's list still applies** (Peer Educator count, 15 lessons vs. 16 modules, six 360° components, Summer Institute name spellings, fundraiser dates, partner logo links). See `../README.md`.

## Source

`source/` holds the Python generator for 2.0 (one module per section) and `research_new_pages.md`, the research notes and citations behind the three new pages. The generator's file paths point to the build workspace, so update them before running it elsewhere, or edit the HTML in `site/` directly.
