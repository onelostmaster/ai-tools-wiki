# final-phase-lite (Jadouminou)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/Jadouminou/final-phase-lite
- **GitHub repo:** https://github.com/Jadouminou/final-phase-lite @ bf3114a (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-18)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-18

## Safety reason

Not code-reviewed for safety. README: install is done by asking Claude to "install this for me" (it checks Node 20+, Claude Code or OpenCode and FFmpeg and adds the final-phase-lite skill); removal runs node install.mjs --remove; it reads your Claude Code session to follow it. Tested by the author on a Mac; Windows not stated. Repo, license and latest commit confirmed from github.com metadata, 2026-11-18.

## Safe install

Unreviewed: contain it: clone at the pinned commit bf3114a, read install.mjs yourself before letting Claude run it, run it in a test project inside a devcontainer or sandbox, no API keys (it needs none with your Claude Code plan). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: open the cloned folder in Claude Code and say "install this for me" (README); needs Node 20+ and FFmpeg.
