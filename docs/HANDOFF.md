# Handoff log

Dated entries between the setup side and the website side. `setup-N` entries are what the website side took from setup. `proj-N` entries are notes back to setup. Newest last. No links and no private names here.

## setup-1 (2026-11-14)

Taken from the setup plan:

- Static site built from `data/tools.json` by one Python standard-library script in `site/`, hosted on Cloudflare Pages (free plan, commercial use allowed, response headers through `_headers`, a preview per branch, no tokens). Other hosts were checked against their terms and limits on 2026-11-14 and set aside.
- Cloudflare settings to use when connecting: production branch `main`; previews only for `claude/` branches; root directory the repo root; build command `python3 -I site/build.py`; output `site/dist`; `PYTHON_VERSION=3.13`; the Cloudflare GitHub app installed on this repo only. Connect only after pull request 1 is merged.
- The nightly export rewrites only `README.md`, `AGENTS.md`, `DECISIONS.md`, `YOLO.md`, `tools/` and `data/tools.json`, and leak-scans every file in this repo except `.git`. Website files survive the export and are scanned too.
- Data on 2026-11-14 (counted from the file): 576 tools; 285 safe, 175 caution, 107 unreviewed, 9 avoid; 0 Safe install lines and 0 YOLO lines written; 116 avoid or unreviewed rows carry the YOLO value `Not offered.`; 18 rows have an empty Decision.
- Build gate rules (see `CLAUDE.md`) and the corrections from the setup review: the progress line counts against 576; `Not offered.` is allowed for avoid and unreviewed rows; an empty Decision renders as "Not decided"; top-level keys allowed are `count` and `tools`.
- Design and review tools: a front-end design skill and a motion skill as account skills (nothing in the repo), a web-quality review skill set copied in later at a pinned commit after the owner's OK, and the preinstalled Playwright for screenshots. Not picked: hosted site builders, UI frameworks, CDN fonts, search libraries and audit tools that would need npm.
- Binary files (fonts, images) may be committed: the export's leak scan reads them since 2026-11-14. They still go through the private-terms check and the tools register.
- Deploy check: read the Cloudflare check or commit status on `main`'s latest commit through GitHub, because the cloud network may block the site's own host.
