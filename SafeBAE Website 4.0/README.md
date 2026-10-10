# SafeBAE website 4.0

The fourth version of the rebuilt safebae.org: 49 pages. Versions 1, 2 and 3 sit untouched next to this folder.

## Open it

- **Quick look:** open `site/index.html` in Chrome or Safari. Pages, menus, search, tabs, players and interactives all work from your computer.
- **Embeds:** YouTube, Spotify, Zeffy, Google Forms and Calendly load only when the site is served from a real web address. Opened from your computer, those spots show a button that opens the same video, episode or form in a new tab.
- **Online preview:** the same build is published as a private Claude artifact, "SafeBAE Site 4.0". Links between pages swap the page in place there, so the browser Back button doesn't step between pages.

## What changed from 3.0

**The footer.** One compact block instead of five layers:

- logo, the mission sentence, Donate and newsletter buttons, and social icons on the left;
- four link columns (Students, Adults & schools, Resources, About) with five links each, down from six columns and 42 links;
- one "Need to talk to someone now?" line with three numbers and All hotlines;
- SAFE BEFORE ANYONE ELSE as the sign-off, two lines across the full width, with SAFE and the B, A, E in glowing neon and every other letter solid aqua (no see-through letters);
- the legal line with the Candid seal, Contact, Photo credits and Back to top.

The big daisy behind the footer is gone. `footer-signoff-options.png` (next to this README) shows the sign-off before and after, plus two other treatments if you want to swap.

**Page endings.** Before 3.0's footer, most pages stacked an aqua "Keep prevention free" donate band and a coral "Need support right now?" strip. Both are gone; the footer's Donate button and help line do those jobs on every page. Donate, Chip In and Fundraise keep their own giving sections. Each page now ends with one closing section, then the footer.

**Navigation.** Every tab in the menu bar is now a link to its landing page (About, For Students, For Adults, Request a Program, the Resources Hub, #ForDaisy). Hovering a tab still opens its menu; on a touch screen the first tap opens the menu and the second opens the page. The phone menu and the footer both link the Resources Hub.

**The header.** Two bars instead of three. The mint announcement ribbon used to rotate between two messages forever; "New: AI Literacy Training, Oct 26–30 · Choking Hazard" now sits still in the top bar, and in the phone menu. The Resources menu's feature card is now a teal Vibe Check card with the phone screen.

**Choking Hazard.** The page used to rebuild most of chokinghazard.org. It now gives context and sends people there, in six sections:

1. the hero, with the warning labels and tape;
2. three facts and the 2022 survey numbers;
3. four doors into chokinghazard.org: the evidence, media ratings, posters and the sticker, and the short film;
4. the signs that need an emergency room, when to call 911 and what to say at the desk;
5. Vibe Check;
6. the Sexual Strangulation Prevention program for schools.

The page went from 14,900px tall to 5,800px.

**Every page was planned again.** Each page got one job, and sections that served another page's job were cut or merged, with a link to where that content lives. Promos that repeated across pages are mostly gone: "New from SafeBAE", "Two new programs", "More from SafeBAE" link grids and repeated hotline strips. Vibe Check stays as a full teal band wherever it fits the audience. The whole site is 17% shorter.

| Page | Sections | Height (px) | Main change |
|---|---|---|---|
| Choking Hazard | 15 → 6 | 14,866 → 5,812 | Context and launch to chokinghazard.org |
| AI Literacy Training | 10 → 6 | 10,133 → 5,962 | Launch page; module detail lives in the training |
| 360° Schools | 13 → 6 | 12,255 → 7,418 | REES moved into its component; evidence merged |
| Parents & Caregivers | 11 → 8 | 12,029 → 9,830 | Merged support sections; restorative justice diagram and the full Vibe Check guide kept |
| Vibe Check | 11 → 8 | 11,478 → 10,024 | Demo beside the walkthrough; Dominick Shattuck's full note kept |
| Home | 13 → 9 | 11,359 → 8,708 | REES, stats and podcast bands cut |
| Survivor Support | 12 → 6 | 11,579 → 8,934 | "When someone tells you" and "Words that help" merged |
| About | 10 → 7 | 10,069 → 7,483 | Founders merged; seven promo cards became one row |
| Students | 10 → 7 | 10,029 → 7,582 | Fellows and link grid cut; films joined Skills Lab |
| Resources Hub | 6 → 5 | 9,259 → 8,729 | The 3.0 hub, back as it was; its Vibe Check questions now play once |
| Clubs | 9 → 5 | 7,387 → 5,239 | Contacts joined registration |
| Peer Educator Training | 9 → 5 | 8,908 → 6,782 | Why it matters merged into what it is |
| Film pages (8) | 3 endings → 2 | about −8% each | "Before you begin" + guide merged into "Teach it" |

The rest of the pages had a lighter pass: one ending, level rows, fewer labels and chips.

**Small fixes.**

- The film cards for It's Giving Red Flags and Intimacy & Dating now use clean stills. The old images had the film title and subtitles burned in under the card label.
- Several rows that ended at different heights now end level.
- A few chips that were under 14px are now 14px.
- The Resources page's Vibe Check questions no longer loop forever.

## Please check these before launch

**New in 4.0: content that moved or was cut**

- **Parents page.** The "what to say" poster is no longer on this page; it's on Survivor Support, and the page links there. The restorative justice diagram is back beside "Accountability outside a formal investigation", credited to iirp.edu. "Sharing Vibe Check with your child" is back in full (five steps, what to say, what to avoid, conversation starters) and links to the adults' guide on the Vibe Check page.
- **AI Literacy Training page.** The module-by-module detail is gone. The training itself carries it. The Vibe Check band and the hotline section are cut; one help line remains.
- **Home.** The REES band is cut; REES is component 5 of the 360° section and on 360-schools.html#rees. The 86,000+ figure moved into the hero.
- **360° Schools.** The "Two new programs", the podcast row and the separate Vibe Check band are cut. Vibe Check is part of component 6.
- **Peer Educator Training.** The paid-mentorship line for college students now appears only on the College Students page.
- **#ForDaisy.** The tribute wall shows 16 messages first, with "Show more" (all 495 are still there). The gallery shows its first rows, with "Show all 31 photos".
- **Photo credits.** The page lists only stock photos still in use. One Unsplash parent photo dropped out.

**Carried over from 3.0 (still open)**

- **Assemblies:** the page has no topics, length, grade levels or prices, because SafeBAE hasn't published them.
- **Forms:** they still don't submit anywhere. The tribute message, contact and program request forms open an email draft on a live site. Connect them to a form service before launch, the tribute wall first.
- **Zeffy:** the frames on Donate, Chip In and Fundraise need one look on a live address.
- **Skills Lab:** "Take a Hint" and "Who's Right?" are not listed. They weren't in the Skills Lab files I had.
- **Choking Hazard:** the "about 20 pounds to open a can" figure is credited to Armstrong & Strack (2016), as on chokinghazard.org; the exact figure wasn't confirmed in the paper.
- Everything else on the 3.0 and earlier lists that you haven't already cleared: Peer Educator count, 15 lessons vs. 16 modules, Summer Institute name spellings, fundraiser dates, tattoo-law and cover-up program sources, and low-resolution team photos.

## Source

`source/` holds the Python generator for 4.0 (one module per page group). It also holds:

- the four briefs (`BRIEF4.md` is this round's);
- `HANDOFF.md`, on how to rebuild and what the rules are;
- each builder's page plan in `work/group*_plan.md`;
- the layout audit and screenshot tools.

The generator's file paths point to the build workspace (`/home/claude/v4`). Update them before running it elsewhere, or edit the HTML in `site/` directly.
