# SafeBAE site 4.0 — brief for page builders

You are one of several builders working in parallel on version 4 of the rebuilt safebae.org (SafeBAE: the survivor-founded, youth-led nonprofit working to end sexual violence among middle and high school students). The client is Drew Davis, SafeBAE's Director of Strategic Initiatives. Version 3 is frozen; v4 is a copy of it.

## What Drew asked for (his words)
> 1. The footer is insane. It's way too much, it's completely unwieldy. Fix it. Make it more cohesive and simple.
> 2. Overall, I need visual refinement and more strategic planning in terms of the layout and content on each page, as well as the overall navigation experience.
> 3. Some pages feel overwhelming — like the choking hazard one... it doesn't need to replicate everything from the actual chokinghazard.org site... just launch people there and provide some context.
> 4. Make it better overall.

Items 1 and 3 are done (see "Already done"). **Your job is item 2 and 4 on your pages: decide what each page is for, cut or merge what doesn't serve that, and make what stays look finished.** The v3 pages are long and dense: the same promos (Vibe Check, AI Literacy, Choking Hazard, "two new programs", hotlines, "more from SafeBAE" link grids) repeat across pages, and many pages end with two or three closing bands. v4 pages are shorter, calmer and more deliberate, with a few substantial elements each.

## Where to work
- v4 lives in `/home/claude/v4/`: generator `build/`, output `site/`, tools `tools/`, screenshots `shots/`, scratch `work/`.
- Build only your own module(s): `cd /home/claude/v4/build && python3 -c "import <module>; <module>.build()"`. Never run `build.py`.
- **Do not edit** `lib.py`, `site/assets/css/site.css`, `site/assets/js/site.js`, `data.py`, `build.py`, `search_index.py`, `tools/`, `films_common.py` (unless you own it), or any module you were not assigned. Page CSS goes in your module's CSS strings (keep your page's class prefix); page JS in `scripts=`. If you need a shared change, say so in your report.
- Helpers other modules import (`pages_home.cpet_player`, `film_strip`, `ring_svg`, `FILM_STRIP_CSS`, `COMP_TEXT`, `pages_ai.brush`, everything in `films_common`) keep their names, signatures and class names.
- Prefix every file you write in `shots/` and `work/` with your page or group name (other builders share those folders).
- Read first: BRIEF3.md (layout standard, craft standard, colour and copy rules — all still apply), this brief, `build/lib.py` (header/footer/NAV), the "4.0 system layer" at the end of `site.css`, and your module(s).

## Already done in the shared system (don't redo)
- **Footer (lib.footer):** one compact block — logo, mission, Donate + newsletter, socials, four link columns, one "Need to talk to someone now?" help line, the one-line SAFE BEFORE ANYONE ELSE sign-off, legal line. It carries the donate ask and the hotlines on every page.
- **`give_band()` now returns nothing.** The aqua "Keep prevention free for every student" band is gone from every page; don't rebuild it by hand. (Donate, Chip In and Fundraise keep their own giving content.)
- **The coral "Need support right now?" strip above the footer is gone.** Hotlines are in the utility bar, the header "Get help" button (`data-open-help`), and the footer help line. Support pages keep their own hotline content.
- **Header:** two bars. The mint announcement ribbon is gone; "New: AI Literacy Training, Oct 26–30 · Choking Hazard" sits in the utility bar. Mega menus unchanged except the Resources feature card.
- **choking-hazard.html is rebuilt as a context-and-launch page** (`pages_choking.py`, 16 sections → 6, 14,900px → 5,900px): hero with the campaign label, three facts, four doors to chokinghazard.org, the medical-care essentials, Vibe Check, the schools program. Look at it before you start: `python3 tools/snap.py choking-hazard.html 1440 full`. It is the pattern for every page that introduces an external tool or campaign site.

## The v4 standard: strategic pages
1. **One job per page.** Write it down for each of your pages before you edit (it's in the plan below; refine it if you disagree). Every section must serve that job. A section that serves another page's job goes, and becomes a link.
2. **Launch pages** (a page about something that lives on its own site — Vibe Check, AI Literacy Training, Skills Lab, Peer Educator Training, Club Hub, chokinghazard.org): give context and send people there. Who it's for, what it does, the one or two things that make it distinctive, how to start, the launch button. Don't reproduce the tool's own content screen by screen.
3. **Hub pages** (Home, Students, Adults, Resources, Request a Program): route people. Short descriptions and clear links; don't re-explain each program in depth when it has its own page.
4. **Content pages** (Survivor Support, Title IX, Myths & Facts, Parents, the program pages, film pages): keep the substantive content, cut the cross-promotion around it.
5. **No repeated promos.** At most one cross-promo per page besides the page's own subject. Vibe Check, where it's relevant to the audience, is a full teal band (Drew's flagship — never a small card), and only one per page. Drop "New from SafeBAE" / "Two new programs" blocks except where the plan keeps them. Drop "More from SafeBAE" / "Meet the people and the work" / "More support and answers" link grids: the nav, breadcrumbs and footer do that job.
6. **One ending.** Each page ends with at most one closing section (a CTA or a "next step"), then the footer. Program pages that ended with "Programs schools can request" + a CTA band end with one section that does both.
7. **Section budget.** Hero included: hubs ≤ 7 sections, launch pages ≤ 6–7, content pages ≤ 8, film pages ≤ 9. Rough height targets at 1440: hubs ≤ 6,500px, launch pages ≤ 5,500px, content pages ≤ 7,500px. Shorter is fine if the page is complete. Measure with `snap.py` (it writes the PNG; check its height).
8. **When you cut, don't lose facts that matter.** Move a fact into a section that stays, or make sure the page it belongs to has it (link there). Never invent facts, names, numbers, quotes, links or dates. Keep SafeBAE's own wording.
9. **Merging is better than stacking.** Two thin sections about one thing become one section with a 7/5 or 8/4 split. A 20-word band becomes a line inside its neighbour.
10. **Visual refinement on everything that stays** (BRIEF3 layout standard): 12-column grid, rows end level, one card anatomy per group, no orphans, no dead zones, ledes full width, body text ≥15px in cards, nothing readable under 14px, alternate light and dark sections with no two neighbours on the same background, `var(--band)` padding, consistent radii. Fewer eyebrows, chips and stickers than v3: keep one only where it adds information.
11. Keep each page's **one signature moment** (its best interactive or visual) and make sure it works and looks finished.

Drew's standing rules (all in BRIEF3; the ones most often broken): brand colours only; coral #fe7171 never darkened, used for urgency/support, at most one coral button per page; Midnight Indigo never; no decorative 01/02/03; subtitles and ledes run the full content width (never a narrow max-width); no meta copy ("This page…", "Below you'll find…", "Explore…"); no triads, no "not X but Y", no "Whether you're…", no hype words or exclamation marks; stills from SafeBAE's own videos never tinted; side-by-side boxes end level; campaign pages keep their own look (KnowB4UNude lavender + emoji, Red Flags neon, BAEcode arcade, Choking Hazard label/tape, Vibe Check lockup, #ForDaisy line daisy).

## The plan, page by page
Sections are named by their current h2. "Cut" means remove from this page (the content lives elsewhere or isn't needed). "Merge" means combine into one section. Use judgment on the details; if you depart from the plan, say why in your report.

### Group A — front door & hubs (`pages_home`, `pages_resources`, `pages_programs`)
**index.html** — Job: say who SafeBAE is and route each audience to its door. Now 13 sections / 10,100px → target ≤ 9 / ~7,500px.
- Keep: hero; "What brings you to SafeBAE?" (the audience router — the signature); New from SafeBAE (AI Literacy + Choking Hazard, the one place on the site both get a feature); Vibe Check band; Certified Peer Educator Training; Films (library strip); SafeBAE 360° Schools; testimonial + partner logos; #ForDaisy.
- Cut: the REES "Document your experience" band (it's a 360° component; the 360 section and 360-schools.html cover it); the mint stats band (it repeats the hero's 3,000+ and 70+; move "86,000+ students reached" and "founded 2015" into the hero stats only if they fit cleanly); "SafeBAE in conversation" podcasts (Library and Partners & Press have them).
- Check the order alternates light/dark after the cuts.

**resources.html** — Job: the index of every resource. Now 8,000px. Keep the hero search, "Start with one of these", "Browse by who you are", and the shelves (signature). Make sure the shelves include choking-hazard as a campaign link (no deep content). Trim "Start with one of these" if it duplicates the shelves item for item (8 featured cards + 3 audience panels + 5 shelves is three ways to say the same thing): keep featured to the ~6 flagship items, and make "Browse by who you are" compact. Target ≤ 6,500px.

**request-a-program.html** — Job: show schools every program and get the request. Now 5,300px, fine. Light pass: the programs grid must be one anatomy, level, no orphan; the 360° band reads as the approach behind the programs; pricing + request don't repeat each other.

**assemblies.html** — Job: what an assembly is and how to book one. Now 6,000px. Merge "An assembly is a first step" with "Where schools go after an assembly" if they say the same thing from two ends. Keep films, testimonial, request. Target ≤ 5,000px.

### Group B — students (`pages_students`, `pages_students2`, `pages_skills`)
**students.html** — Job: route students to what they can do. 10 sections / 8,800px → ≤ 7 / ~6,500px. Keep: hero; "Pick a starting point" (router); Peer Educator + AI Literacy; clubs; Vibe Check band; Skills Lab + Title IX; films (short strip); "If something happened, you don't have to handle it alone" (support). Cut: "Meet the fellows" band (Summer Institute has its own page; give it a link in the starting-point row or the clubs section), the "More from SafeBAE" link grid.

**peer-educator.html** — Job: explain the Certified Peer Educator Training and get students registered (launch page; the course lives on Podia). 9 sections / 7,700px → ≤ 7 / ~6,000px. Keep: hero; what it is; preview player + 16 modules (signature); six steps; register (form). Merge "Why peer education matters" into "What is the Peer Educator Certification?" (its numbers as a stat row). Cut the mint strip if it only repeats hero facts; cut "Put the training to work" (AI Literacy promo) or reduce it to one line under the register form.

**clubs.html** — Job: get a school to register a club (launch page for the Club Hub). 9 sections / 6,200px → ≤ 6 / ~5,000px. Keep: hero; "Which one fits your school?"; "Registering unlocks the Club Hub"; "You decide what your chapter does" (merge the untitled deep band into it); register (merge "Questions, challenges or event ideas?" contacts into the register section). Cut "From learning to changing policy" (one link to reform-policy.html from the register or chapter section).

**reform-policy.html** — Job: help a student start policy reform and get the guide. 7 sections / 5,000px → ≤ 5. Merge the step-by-step guide with "Register to get the guide" (registering is step one). Shorten "Know your rights under Title IX" to a compact band that links to title-ix.html (title-ix.html holds the full content). Cut or fold "Where policy change fits".

**summer-institute.html**, **espanol.html** — light pass (endings, layout, an empty first section on espanol if there is one).

**skills-lab.html** — Job: launch page for skills-lab.safebae.org. 7 sections / 5,600px → ≤ 6 / ~4,800px. Keep: hero; "Pick a tool by the time you have" (signature); "Running one with a group"; Vibe Check band; the final "Open the Skills Lab" band. Cut "Go deeper" (Peer Educator + FAQ cards) or reduce it to a line.

### Group C — flagship tools & #ForDaisy (`pages_vibe`, `pages_ai`, `pages_daisy`)
**vibe-check.html** — Job: Drew's flagship. Explain Vibe Check, show it, build trust, and launch checkyourvibe.org; give adults a clear path. 11 sections / 10,300px → ≤ 8 / ~7,500px. It stays rich and prominent — trim repetition, not ambition. Keep: hero (lockup); the AI-chatbot context; "One step at a time" (signature walkthrough) with the demo video merged in or directly beside it; "Nothing is stored" + what it is / isn't; the four parts of accountability (compact, or merged with what it is); in the news (press logos + 2 features); the adults' guide (make it compact: the guide download, plus the five referral steps; the tabs can stay if they're tight — this is now the one full adults' guide on the site; parents.html will link here); the final launch band. Cut or reduce to a single quote the untitled mist section (Shattuck / Substack, 341 words).

**ai-literacy.html** — Job: launch page for ai-literacy.safebae.org (launches Oct 26–30, 2026). 10 sections / 8,900px → ≤ 6 / ~5,500px. Keep: hero; who it's for + what you'll be able to do; the six modules as a compact list (one line each, the chapter map can stay as the signature; the 1,220-word module detail goes); the Four-Step Check (compact); how it works (account, own pace, resume code, certificate) merged with "For educators and parents" (group access, privacy); the final "Start the training" band. Cut: "Where it connects to SafeBAE's other tools", the Vibe Check band (not this audience's need here), "Support is available" (footer and help drawer carry it; keep one help line if the sextortion module needs it).

**fordaisy.html** — Job: remember Daisy and let people add to her tribute wall (a memorial; stakeholders care about it — handle with care). 10 sections / 8,500px → ≤ 7. Keep: hero; the intro; "Daisy was more than her advocacy"; the tribute wall (signature — show a first set and a "Show more" button rather than every tribute at once); "If Daisy touched your life" (add a message); merge "The words and images from those days" with the photo gallery; merge "Daisy's voice, and her legacy" (podcasts) with the Peer Educator Training dedication into one closing section.

**fordaisy-tattoos.html** — 9 sections / 6,900px → ≤ 7 / ~5,500px. Merge "Before you decide" with "What trauma-informed tattooing looks like". Cut the "Back to #ForDaisy" band (breadcrumb, nav and a link in the closing section cover it). Keep sources (compact).

### Group D — adults (`pages_adults`, `pages_adults2`)
**adults.html** — Job: route parents, educators and college students. 6,100px → ≤ 5 sections / ~5,000px. Keep: hero; "Find what fits your role" (router); Vibe Check adults' guide band; films. Merge "Bring SafeBAE to your school, campus or community" with "New from SafeBAE" into one schools band (the two new programs become two links in it).

**parents.html** — Job: help parents talk with their kids and respond if something happens. 11 sections / 10,800px → ≤ 8 / ~7,500px. Keep: hero; "Start early, and keep talking" (fold the "How to Not (Accidentally) Raise a Rapist" podcast in as a feature inside it, or keep it as a tight band — not both); "Topics to talk through with your teen" (signature tabs); choking (compact band: what parents should know + link to choking-hazard.html and chokinghazard.org — no deep content); "If your child tells you something happened" merged with "Listen to your child's wishes first" (believe, support, options, accountability outside an investigation); one Vibe Check band that merges "CheckYourVibe.org" with "Sharing Vibe Check with your child" (the three most important steps + "Read the full adults' guide" → vibe-check.html#adults; the 633-word step list lives there now); "Connect your student with SafeBAE" (compact).

**educators.html** — 4,800px, light pass. Merge "Two new programs for schools" into "Ready to request a program?" (two links) so the page ends once.

**college.html** — light pass; the AI Literacy band becomes compact or a line inside "Get certified".

**donate.html, chip-in.html, fundraise.html** — light pass. These are the only pages with a giving band; make sure each ends once and the Zeffy embeds sit level with their neighbours.

### Group E — schools (`pages_schools`, `pages_schools2`)
**360-schools.html** — Job: explain the whole-school approach and how a school adopts it. 13 sections / 11,000px → ≤ 8 / ~7,000px. Keep: hero; "Six components that work together" (signature ring); "How schools adopt SafeBAE 360°" (merge "Young people lead every implementation" into it — youth leadership is how adoption works); "Where each role starts"; "What the 360° pilot found" (merge the untitled impact strip and the partner-school logos into it as evidence); the REES reporting tool only as part of its component (cut the separate band if the component panel covers it); the closing CTA. Cut: "Two new programs schools can add" (Request a Program lists them), the separate Vibe Check band if Vibe Check is one of the six components (check: "Educational Resources to Reduce Recidivism") — otherwise keep one teal band, "Listen: SafeBAE on prevention in schools".

**consent-curriculum.html, professional-development.html, policy-reform-guide.html, accountability-training.html** — each ends with "Programs schools can request" + a CTA band: merge into one closing section (the request CTA with a compact row of the sibling programs). Cut "Two new programs for your school" on professional-development and trim "More for your classroom" on consent-curriculum to what a teacher needs (films + guides; one line for the rest). Accountability Training keeps its Vibe Check band (it's the audience). Each ≤ 6 sections / ~5,000px.

### Group F — support & answers (`pages_support`, `pages_support2`)
**survivor-support.html** — Job: get help now, then healing, then how to support someone. 12 sections / 10,400px → ≤ 8 / ~7,500px. Keep: hero; "Talk to someone now" (hotline grid with filters — signature); "Healing takes time, and support."; merge "When someone tells you they've been assaulted" with "Words that help, and words that hurt" (and the shareable poster download inside it); "Dating after sexual assault" (compact, links to the film page); "Survivor-centered media" (keep, compact — tabs or a tight list); Vibe Check band (tight). Cut: "Shareable graphics" as its own band (fold into the words section or posters.html link), "Off Campus" as its own band (fold into media if it's a book/series entry), "More support and answers".

**title-ix.html** — Job: explain students' rights under Title IX and what to do. 12 blocks / 8,100px → ≤ 8 / ~6,500px. Keep: hero; what it does (+ the stat strip merged in); "Is my school covered?" (stepper — signature); "What Title IX laws really mean" + coordinator; timeline (compact: collapsible or tighter cards); supportive measures. Cut "Tell Me Lies… but not about Title IX" (blog link at most). Fold "Schools can do more" into one closing line/CTA to reform-policy.html and policy-reform-guide.html.

**myths-facts.html** — 8,100px → ~7,000px. Light restructure: keep the myths-vs-facts set (signature) and the causes / reporting / identity sections; check that the Megan Thee Stallion section earns its place (keep if it's SafeBAE's own content, tighten).

**faq.html, posters.html, blog.html** — light pass. Posters: the Choking Hazard posters band is compact and links out. FAQ: ends once.

### Group G — about (`pages_about`, `pages_about2`)
**about.html** — Job: who SafeBAE is and how it began. 10 sections / 8,800px → ≤ 8 / ~6,500px. Keep: hero; the BAE strip; story; how we began; co-founders; Shael Norris; milestones (signature timeline). Reduce "Prevention led by young people, in their own schools" (7 promo cards) to a compact set of 3–4 links or one row. Cut "Meet the people and the work" (nav/footer).

**team.html, impact.html, partners-press.html, contact.html, credits.html** — light pass: endings ("Ways to join this work" stays only if it's short), level rows, consistent people cards. Impact: "Does prevention work?" video band can merge with the evidence section.

### Group H — library & films (`pages_library`, `films_common`, `films_*.py`)
**library.html** — light pass.
**8 film pages** — Each ends with "Before you begin" + "Get the teaching guide" + "Teach these next" (three closing sections). Merge "Before you begin" into the guide section (one "Teach it" section: guide download + facilitator notes) in `films_common`, then make each film module use it. Fold the tiny poster sections ("Put it on the wall", "Posters for healing", "Share the campaign", "From the campaign", 10–24 words) into the guide section or the hero. Keep each film's own look. Keep the Vibe Check band where a film has one. Target ≤ 9 sections each; trim long discussion content only where it repeats.

## How to work (required)
1. For each page, write its job and your section plan (keep / merge / cut) in `work/<group>_plan.md` before editing.
2. Build, then look. `cd /home/claude/v4 && python3 tools/snap.py <page>.html 1440 full`, then `python3 tools/slice.py shots/<page>_1440.png 1500 0.55` and read the slices. For a quick whole-page view: `python3 tools/ov.py shots/<page>_1440.png shots/<page>_ov.jpg 4 0 0.27`. Element shots: `python3 tools/el.py <page>.html "<selector>" 1440 shots/<name>.png "<click selector>"`. Layout leads: `python3 tools/audit.py <page>.html 1440`.
3. Check 400px: `python3 tools/snap.py <page>.html 400 full` then `python3 tools/mobile_sheet.py shots/<page>_400.png 2800 0.5 4`.
4. Finish with `python3 tools/check.py all <your pages>` (no broken links or anchors, no overflow at 360/400/1440, no console errors). Fix any link that pointed at an anchor you removed (search all modules you own; if another group's page links to an anchor you removed, keep the anchor id on the section that now holds that content).
5. Be economical: the machine has 2 cores and 3 browser slots shared by every builder. Shoot what you will look at; view slices at 0.5–0.6 scale; don't re-shoot unchanged pages.

## Final report (your last message, short)
Per page: job (one line), sections before → after and height before → after, what you cut or merged (one line each), where any cut content now lives, the signature moment, anything you could not do, any shared-file change you need. No code.
