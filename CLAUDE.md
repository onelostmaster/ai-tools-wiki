# Rules for Claude working on the website

This repo is public. Everything you commit, every commit message, every branch name and every pull request text is public forever.

## What lives where

- The data files belong to the nightly export, which rewrites them every night: `README.md`, `AGENTS.md`, `DECISIONS.md`, `YOLO.md`, `tools/` and `data/`. Never edit them. A wrong fact in them is reported upstream as a request, never fixed here.
- Website code lives only in `site/`, `.claude/`, `CLAUDE.md`, `docs/` and `.gitignore`.
- The site reads only `data/tools.json`. Never copy tool data by hand into a page, a fixture or a second data file.
- `docs/PLAN.md` is the build order. `docs/HANDOFF.md` holds dated entries for the setup side (`setup-N` in, `proj-N` out).

## Code rules

- Build: `site/build.py`, Python standard library only. Front end: plain HTML, CSS and JavaScript. No npm, no CDN, no framework, no web fonts from other hosts, no analytics, no cookies, no third-party scripts.
- A new library, font or tool needs its code or licence read, its risks with their fixes, and the owner's OK before it lands. The default answer is to write it with the standard library instead.
- Keep `Content-Security-Policy: default-src 'self'` in `_headers`. That means no inline scripts or styles.
- Never write keys, tokens or passwords anywhere.
- `robots.txt` uses `User-agent: *` only and never names a crawler.
- Never merge and never push to `main`. Work on a `claude/` branch and open a pull request; the owner merges.
- Never change a Cloudflare setting or a repo setting.

## Private terms

A private list of names and link patterns (kept outside this repo, never committed) must not appear anywhere in this repo. Before each push, check every file of the branch except `.git`, every commit message on the branch, the branch name and the pull request text against that list: case-insensitive, whole words, the same way the nightly export's leak scan does. That means common phrases from the list count too, so reword your own text. Links to the private workspace tool are never written literally: in code, use escaped regex text or build the string from parts; in prose, call them "Notion links". A single hit in any file blocks the nightly public export for everyone.

Third-party copies (for example a pinned skill folder) get the same check before they are proposed. A file that hits is left out and named on the OK request. Never edit a pinned copy.

## QA gate

Run all of it before the owner sees a pull request, and fix what it finds first.

1. `python3 -I site/build.py` passes on today's data, and `python3 -I site/test_gate.py` passes (the gate fails on broken copies). Add a test for every new gate rule.
2. The private-terms check above finds nothing.
3. Playwright screenshots of the built pages at 360, 768 and 1280 px wide, with zero console errors, plus a keyboard focus walk (every link and control reachable with Tab, with a visible focus ring). Use the preinstalled Playwright; never run `playwright install`. Never commit screenshots.
4. Page-weight budget: the home page under 100 KB before the search index, all JavaScript under 20 KB.
5. One independent reviewer agent reads the diff against these rules and the work rules; fix its findings.

Put the screenshot result, the budget line and, once Cloudflare is connected, the preview link in the pull request description. Log each gate run as one appended line in the project's QA log (`qa-log.csv` in the project's shared files, outside this repo; never rewrite it).

## Build gate (in `site/build.py`)

The build stops, and nothing is published, on any of these:

- a top-level key other than `count` and `tools`, an empty tool list, or a `count` that is missing, not a whole number or does not match the number of tools;
- a tool field outside the 14 public fields, or a field that is not text;
- a Safety verdict other than `safe`, `caution`, `unreviewed` or `avoid`;
- a YOLO install on an avoid or unreviewed tool other than empty or exactly `Not offered.`;
- a link to the private workspace tool (including its public-page domain) anywhere in the data, keys included, after Unicode normalization and with lookalike dots read as dots.

An empty Decision is allowed and renders as "Not decided".
