# html-to-mp4 (Universaljojo)

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://github.com/Universaljojo/html-to-mp4
- **GitHub repo:** https://github.com/Universaljojo/html-to-mp4 @ ce5aea0 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: needs Node 18+, ffmpeg, Python 3 only for overlay_slogan.py; npm install then npx playwright install chromium downloads Chromium; run node record.mjs. Install steps in the README are macOS/Linux (brew/apt); Windows ffmpeg comes from winget. Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: clone at the pinned commit ce5aea0 inside a devcontainer or sandbox, npm ci there, no API keys (it needs none), network on only for npm and the Chromium download. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows: winget install ffmpeg; in an example folder: npm install, npx playwright install chromium, node record.mjs (README).
