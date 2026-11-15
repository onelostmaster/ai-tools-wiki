# pocketworld (Tu-Zhenzhao)

- **Type:** skill
- **Category:** generating videos, building a site
- **Official URL:** https://github.com/Tu-Zhenzhao/pocketworld
- **GitHub repo:** https://github.com/Tu-Zhenzhao/pocketworld @ 2059674 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-14)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-14

## Safety reason

Not code-reviewed for safety. The a project Tool Scout (Claude, 2026-11-14) listed it but did not read or rate it. Repo and commit confirmed from github.com metadata, 2026-11-14.

## Safe install

Unreviewed: contain it: use the v0.6.0 release zip after checking it against SHA256SUMS (INSTALL.md:37), install to a test skills folder in a devcontainer, no browser download, no keys. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
INSTALL.md\:26-35\: `node scripts/install.mjs --dest <host skills dir>/pocketworld` copies the skill and installs its locked Node dependencies; browser download only with --install-browser. Needs Node 20+, ffmpeg for video/GIF (INSTALL.md:47). v0.6.0 release zip ships SHA256SUMS (INSTALL.md:37).
