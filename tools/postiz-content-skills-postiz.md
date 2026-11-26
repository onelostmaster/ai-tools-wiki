# postiz-content-skills (Postiz)

- **Type:** skill
- **Category:** generating videos, social posting, research
- **Official URL:** https://github.com/gitroomhq/postiz-content-skills
- **GitHub repo:** https://github.com/gitroomhq/postiz-content-skills @ 70fcc01 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25); README list prices per Short about $16 of Seedance clips plus HeyGen and ElevenLabs credits (provider prices not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: macOS or Linux (Windows only through WSL); ./install.sh installs ffmpeg, jq, the Postiz, agent-browser, DataForSEO and ElevenLabs CLIs, a Python environment, third-party skills, the claude-seo plugin and a Remotion template (via content-setup/scripts/install-deps.sh, not read); API keys stored in ~/.content-skills/.env; publishes posts through Postiz. unverified: whether the CLIs install globally. Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: run ./install.sh --skills-only from the pinned commit 70fcc01 inside a WSL devcontainer or sandbox, no real Postiz/HeyGen/ElevenLabs keys, no connected social accounts, network on only for install downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows: WSL only (README). Claude Code: ./install.sh (or --skills-only to copy the skills without the software).
