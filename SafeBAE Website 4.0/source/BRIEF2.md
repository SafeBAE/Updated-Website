# SafeBAE site 2.0 — brief for page builders

Drew (SafeBAE's Director of Strategic Initiatives) reviewed version 1 of the rebuilt site and asked for a **2.0 version**: "slightly more visually refined and more cohesive and brilliant and creative", plus new pages (AI Literacy Training, the Choking Hazard campaign, a Tattoos & Healing subpage under a new #ForDaisy tab) and mentions of the new pages across the site.

## Where to work (critical)
- **Version 1 is frozen.** Never edit, rebuild or write anything under `/home/claude/build/`, `/home/claude/site/`, `/home/claude/tools/` or `/home/claude/shots/`. Those are the delivered v1.
- 2.0 lives in **`/home/claude/v2/`**: generator `v2/build/`, output `v2/site/`, tools `v2/tools/`, screenshots `v2/shots/`. `v2/build/lib.py` already writes to `v2/site/`.
- Build only your own module: `cd /home/claude/v2/build && python3 -c "import <module>; <module>.build()"`. Don't run `build.py` (other builders are mid-edit).
- Screenshots: `cd /home/claude/v2 && python3 tools/snap.py <page>.html 1440 full` (writes `v2/shots/<page>_1440.png`), `python3 tools/slice.py shots/<page>_1440.png 2200 0.4`, element shots `python3 tools/el.py <page>.html "<selector>" 1280 shots/<name>.png`. Link/overflow check: `python3 tools/check.py all <page>.html …` (it reports links to pages other builders haven't built yet — `ai-literacy.html`, `choking-hazard.html`, `fordaisy-tattoos.html` — ignore those three).
- Don't edit `lib.py`, `site.css`, `site.js`, `data.py`, or another builder's module. If you need a shared change, say so in your report.
- The original brief `/home/claude/build/BRIEF.md` (read-only) still applies: brand colours, copy rules, no invented facts, carry content over, 400px must work. Re-read its Design rules and Copy rules sections.

## What's already new in the shared system (look at any v2 page to see it)
- **Header:** a 7th tab, `#ForDaisy` (with a daisy icon). New mega-menu links to `ai-literacy.html`, `choking-hazard.html`, `fordaisy-tattoos.html`.
- **Announcement ribbon** under the header (mint) rotating the two new programs. Don't add another sitewide banner.
- **Footer** opens with a huge "SAFE BEFORE ANYONE ELSE" wordmark.
- **Grain** texture on every dark surface (`.band--slate/--deep/--logo`, `.phero` dark variants).
- **Hero grammar:** `lib.phero()` now adds a slowly rotating daisy watermark and a staggered rising entrance. For a custom hero, add `<span class="wm-daisy" aria-hidden="true"></span>` as the first child of a `position:relative; overflow:hidden` hero section (put your content above it with `position:relative; z-index:1`) and `class="rise"` on the text column.
- **Marker word** `<span class="mk">…</span>`: on light backgrounds a mint highlighter swash, on dark backgrounds mint ink. This is the site's signature emphasis.
- Tokens added: `--r-xl:22px`, `--shadow-soft`, `--ease`. `.card` now uses `--r-xl`.

## The 2.0 pass on each of your pages
Make each page feel like one site, more finished, a little more surprising. Keep all content and every working interaction. Don't restructure pages that work; refine them.
1. **Hero:** every hero has imagery (photo, collage, cover, or a purposeful graphic). No text-only heroes. Use the shared hero grammar (watermark + rise) — for `phero()` heroes it's automatic; add it to custom heroes. Size the hero to its content (no empty band under it).
2. **Marker word:** in every page's H1, wrap the one word or short phrase that carries the meaning in `<span class="mk">`. Replace any older ad-hoc mint-coloured H1 spans with `.mk`. Optionally one H2 per page. Never more.
3. **Eyebrows:** keep only ones that add information (a category, a source, a count, a date). Remove purely decorative kickers so not every heading has one. Eyebrows: mint on dark, Logo Teal on light — never SafeBAE Teal text on Deep Slate (2.5:1).
4. **Rhythm:** alternate light and dark sections; no two adjacent sections with the same background unless deliberately joined; vertical padding from `var(--band)`; no gap over ~120px; side-by-side boxes end at equal height.
5. **Surfaces:** large cards `border-radius: var(--r-xl)`, small chips/tiles 12–14px; 1px `var(--line)` borders on light; `var(--shadow-soft)` for raised elements; feature photos 22px radius, often with a `.sticker` label. Remove one-off shadows/radii that fight this.
6. **Colour:** Coral only for urgency/support and at most one coral button per page. Midnight Indigo never. Small text on SafeBAE Teal must be white.
7. **One creative upgrade per page** where it genuinely helps: a better interactive, a richer visual for a key fact, a stronger image composition, a pull-quote treatment — something a visitor will remember. Don't add clutter: Drew dislikes pages that stack pickers, carousels, stat rows and checklists ("too messy and overwhelming"), and also dislikes bare pages.
8. **Copy:** re-read every heading and lede you touch against the copy rules (no meta copy, no triads, no "not X but Y", no "Whether you're…"). Plain, declarative.

## Mentioning the new pages (only where it genuinely fits the audience)
Use these facts only. Link internally.
- **AI Literacy Training** → `ai-literacy.html` (the training itself: https://ai-literacy.safebae.org). The free SafeBAE AI Literacy Training: six self-paced modules for high school and college students; anyone 13 or older can take it. It covers how AI works, how feeds and AI shape what we see and believe, AI and healthy relationships, using AI well, fake images, and sextortion. It launches during U.S. Media Literacy Week, October 26–30, 2026. Learners create a free account so progress saves; educators can register for group access. Name it exactly "SafeBAE AI Literacy Training" (or "AI Literacy Training").
- **Choking Hazard** → `choking-hazard.html` (campaign site: https://chokinghazard.org). SafeBAE's campaign on sexual strangulation, which young people call "choking". Core line: "There's no safe way to choke someone." It gives young people, parents and educators the evidence, myth-vs-fact, signs that need medical care, and free warning posters. For schools: SafeBAE's **Sexual Strangulation Prevention** program launches November 2026 (mention this only on school/educator-facing pages).
- **Tattoos & Healing** → `fordaisy-tattoos.html`: Daisy Coleman was a tattoo artist; the page covers her art and tattoos as one path some survivors take to reclaim their bodies.

## Final report (your last message)
Short: pages changed and the main 2.0 changes per page; where you added mentions of the new pages; anything you couldn't do; any shared-file change you need. No code.
