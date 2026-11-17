# career-ops

- **Type:** plugin
- **Category:** automation, research
- **Official URL:** https://career-ops.org
- **GitHub repo:** https://github.com/career-ops-hq/career-ops @ 6210e44 (MIT; latest commit on 2026-10-31)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); you pay your AI provider.
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed; the post only names it. README: says no telemetry, never submits or sends anything (drafts only), and your CV goes only to the AI provider you pick; Playwright drives a browser for PDFs and the apply helper; opt-in Gmail, Notion and Apify plugins; installs through unpinned `npx`.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: run it in a devcontainer or WSL2 folder with a copy of your CV only (no other personal files), git clone at the row's commit 6210e44 instead of npx @santifer/career-ops init (if you use npx, pin it: 1.40.0 is the latest on npm 2026-11-16), install Chromium only for that folder, skip the Gmail, Notion and Apify add-ons, give it no keys beyond the one AI provider you pick, and treat every draft as a draft: you send applications yourself. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `/plugin marketplace add career-ops-hq/career-ops` then `/plugin install career-ops@career-ops` (README).
Claude Code (local only): `npx @santifer/career-ops init`, then `npm install` and `npx playwright install chromium` for PDFs (README).
