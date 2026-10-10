# SafeBAE website rebuild

A complete static rebuild of safebae.org: 44 pages, built from the content of the live site (everything except individual blog posts).

## Open it

- **Quick look:** open `site/index.html` in Chrome or Safari. Every page, image, menu, search, tab, slide player and lightbox works from your computer.
- **Embeds:** YouTube, Spotify, Zeffy, Google Forms and Calendly only load when the site is served from a real web address (any static host: GitHub Pages, Netlify, your WordPress server). Opened from your computer, those spots show a button that opens the same video, episode or form in a new tab.
- **Online preview:** the same build is published as a private Claude artifact ("SafeBAE Site Rebuild"). In that preview, links between pages swap the page in place, so the browser Back button doesn't step between pages there.

## What's in `site/`

| Area | Pages |
|---|---|
| Home | `index.html` |
| Library | `library.html` (one searchable library of films, podcasts and teaching guides) and eight film / guide landing pages (`film-*.html`) |
| Resources | `resources.html`, `vibe-check.html`, `survivor-support.html`, `title-ix.html`, `myths-facts.html`, `faq.html`, `posters.html`, `blog.html` |
| Students | `students.html`, `peer-educator.html`, `clubs.html`, `reform-policy.html`, `summer-institute.html`, `espanol.html` |
| Adults | `adults.html`, `parents.html`, `educators.html`, `college.html`, `request-a-program.html` |
| 360° Schools | `360-schools.html`, `consent-curriculum.html`, `professional-development.html`, `policy-reform-guide.html`, `accountability-training.html` |
| About | `about.html`, `team.html`, `impact.html`, `partners-press.html`, `fordaisy.html`, `contact.html`, `credits.html` |
| Giving | `donate.html`, `chip-in.html`, `fundraise.html` |

Shared code lives in `site/assets/` (one stylesheet, `site.js` for menus, search, help drawer, quick exit, tabs and players, and the Library's data). Press **Cmd/Ctrl + K** or **/** anywhere to search the whole site. **Esc Esc** is the quick exit.

## Not wired up yet

- **Forms are front-end only.** Contact, program request, the #ForDaisy tribute message and similar forms validate and show a thank-you. On a live site they open an email draft to info@safebae.org. To collect submissions, connect them to a form service or keep your existing Forminator / Google Forms.
- **Teaching guides download directly.** The old site gated each PDF behind a Forminator form (name, email, school, state, intended use). The new pages link the PDF and invite people to the existing guide feedback survey instead. Put a gate back if you need that data.
- **Blog posts stay on safebae.org.** `blog.html` links out to the real posts. Its post list is a snapshot from October 8, 2026 and won't update on its own.
- **Search index is static.** It covers every page, section, library item, FAQ answer and hotline as of this build.

## Please check these before launch

- **Peer Educator count:** the site uses 3,000+ (your current figure). The data report page in the old site said "more than 2,000 students across 45 states"; that sentence is kept in its original context on `impact.html`.
- **Consent curriculum:** the curriculum page lists 15 lessons; the old 360° page said 16 modules. The new site uses 15 everywhere.
- **360° components:** the old Request a Program page said five; the 360° page said six (adding REES). The new site uses six everywhere.
- **Summer Institute name spellings** follow the old page, which differs from the photo filenames: Dolly Barrat / Barratt, Anna Diegnan / Deignan, Mica / Micaela Ormeno, Claudia Cham / Kulee Cham.
- **Team:** Apollo Knapp's old LinkedIn link pointed to a profile under a different name, so the name is unlinked.
- **Partner logos:** the old site's logo links were scrambled (several went to the same site), so logos are shown without links.
- **Fundraisers:** the Justin, Tina and Vanessa pages include dated lines ("This month…", "tonight's livestream"). Confirm which fundraisers are still running.
- **Positive News** (Vibe Check press): no article link was available, so the card links to positive.news.
- **Added beyond the old site:** NCMEC's Take It Down service on the #knowB4Unude page (removing shared nude images of minors); the Vibe Check how-it-works steps and the BAE Skills Lab activity details come from the live tools; the Title IX rights list and the 70% climate-survey figure come from SafeBAE's own Title IX post.
- **Photos:** a few Unsplash photos fill pages that had none; all are credited on `credits.html`.

## Source

`source/` holds the Python generator that produced every page (one module per section). It was written for the build workspace, so its file paths need updating before it will run elsewhere. Edit the HTML in `site/` directly if that's easier.
