# Build plan

The goal: a fast, static, tracking-free website for the public AI tools wiki in this repo. Every tool gets its own page with its safety verdict and its Safe install, with search and filters on the home page, a separate page for YOLO installs, and plain outputs for AI readers.

## Choices

- **Data:** `data/tools.json` only (14 public fields per tool). The nightly export rewrites it; the site never edits it.
- **Build:** one Python standard-library script, `site/build.py`, writes everything into `site/dist/`.
- **Host:** Cloudflare Pages on its free plan, building from this repo on every push to `main`, with a preview for each `claude/` branch. Build command `python3 -I site/build.py`, output folder `site/dist`, `PYTHON_VERSION=3.13`.
- **Front end:** hand-written HTML and CSS, one small JavaScript file for search, filters and copy buttons, system fonts. No framework, no CDN, no analytics, no cookies.
- **Safety:** an allow-list gate in the build (see `CLAUDE.md`), `Content-Security-Policy: default-src 'self'`, and a private-terms check before every push.

## Build order

1. **Pull request 1 (this one):** rules (`CLAUDE.md`), this plan, the handoff log, safe-default Claude settings, `.gitignore`, and `site/build.py` with the gate, one tool page, `build.json` and `_headers`, plus gate tests.
2. **Owner connects Cloudflare Pages** after pull request 1 is merged. Before that, a build on `main` would fail because the build script would not exist yet.
3. **Pull request 2:** design and accessibility review skills, pinned at a reviewed commit, if the owner says yes.
4. **Pull request 3:** every tool page, the home page with search (an index of name, type, category, verdicts and a short reason, filtered in the browser; filter state in the URL; `/` focuses search) and filters.
5. **Pull request 4:** the YOLO page behind its own door (red frame, first line says what it skips, never for avoid or unreviewed tools), an About page that reviews the site the way the wiki reviews a tool, `/tools.json`, `/llms.txt`, `index.json`, `sitemap.xml` and `robots.txt`, and a "Copy for your AI" button.
6. **Then, daily:** check each deploy against the data it was built from (`build.json` carries the data file's git blob id and the build commit), and make one improvement a day.

## While Safe installs are still being written

Today 0 of 576 Safe install lines are filled. Each page says "Safe install: not written yet", the home page shows how many are written, install notes copy only under a "not fix-reviewed yet" header, each page shows the date its verdict holds for, and a re-check badge appears after 60 days.

## Feedback without tracking

A "Report a wrong verdict" link opens a prefilled issue on this repo. No counters, no cookies.

## Not decided yet

- A custom domain (a yearly cost, the owner's call).
- The site is 9 out of 10 on paper; it earns the 10 after one month of nightly deploys without a miss.
