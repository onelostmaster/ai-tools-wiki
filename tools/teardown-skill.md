# teardown skill

- **Type:** skill
- **Category:** generating videos, 3D and games
- **Official URL:** https://github.com/elvarofficial/teardown
- **GitHub repo:** [https://github.com/elvarofficial/teardown](https://github.com/elvarofficial/teardown)
- **Price:** Free
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a91262a, a project a review, 2026-10-31): Looks safe. No network or telemetry; local ffmpeg, Python and Chromium calls only. Brand-new GitHub account, and the suggested `npx skills add` installer is unpinned.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills add elvarofficial/teardown -g -a claude-code` (unpinned installer), or clone into `~/.claude/skills/teardown` (unconfirmed); then `npm install && npx playwright install chromium` in the folder. Needs Node 20+, ffmpeg and Python 3.
Hermes: unconfirmed: copy the whole repo to `~/.hermes/skills/creative/teardown/`, run the same npm command, then start a new session (copy rather than `hermes skills install`, which may skip `sims/` and `sfx/`).
