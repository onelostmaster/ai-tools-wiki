# rudywizz-motion (Rudywizz)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://rudywizz.github.io/rudywizz-motion/
- **GitHub repo:** https://github.com/Rudywizz/rudywizz-motion @ 05028e6 (MIT)
- **Price:** Free on GitHub and npm, MIT (github.com, checked 2026-11-24)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-24

## Safety reason

Not code-reviewed for safety. README: needs Node 18+ and ffmpeg; the npm route (npm install -g rudywizz-motion) installs the CLI globally; rendering uses your installed Chrome/Edge or a Playwright Chromium download; also installs as a Claude Code plugin (/plugin marketplace add Rudywizz/rudywizz-motion) or with npx skills add. Repo, license and latest commit confirmed from github.com metadata, 2026-11-24.

## Safe install

Unreviewed: contain it: skip npm install -g (it installs globally); clone at the pinned commit 05028e6 inside a devcontainer or sandbox, run npm ci there and use npx rudywizz-motion, no API keys (it needs none), network on only for npm and the Chromium download. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: /plugin marketplace add Rudywizz/rudywizz-motion then /plugin install rudywizz-motion@rudywizz (README). Windows: winget install ffmpeg; put options in a JSON file instead of quoting JSON on the command line (README).
