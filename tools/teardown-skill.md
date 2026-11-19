# teardown skill

- **Type:** skill
- **Category:** generating videos, 3D and games
- **Official URL:** https://github.com/elvarofficial/teardown
- **GitHub repo:** [https://github.com/elvarofficial/teardown](https://github.com/elvarofficial/teardown)
- **Price:** Free
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read, a91262a, a project a review, 2026-10-31): Looks safe. No network or telemetry; local ffmpeg, Python and Chromium calls only. Brand-new GitHub account, and the suggested `npx skills add` installer is unpinned.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `git clone https://github.com/elvarofficial/teardown %USERPROFILE%\.claude\skills\teardown`, then `git checkout a91262a` (the reviewed commit, still HEAD on 2026-11-14), then in that folder `npm ci` (uses package-lock.json, all five dependencies pinned exactly in package.json, Playwright 1.58.2) and `npx playwright install chromium`. This replaces the unpinned `npx skills add ... -g` installer, which installs globally for every project. Install scripts that run during npm ci: esbuild and fsevents (package-lock.json:457,498; fsevents only on macOS). Needs Node 20+, ffmpeg and Python 3. Hermes (unconfirmed route): copy the whole folder to ~/.hermes/skills/creative/teardown/, run the same two commands, start a new session. claude.ai and Android: no install route.

## YOLO install

YOLO (your own risk): skips the commit pin and the lockfile install, and installs globally.
npx skills add elvarofficial/teardown -g -a claude-code, then npm install && npx playwright install chromium in the folder (package.json setup script).

## Install notes

Claude Code: npx skills add elvarofficial/teardown -g -a claude-code (unpinned installer), or clone into ~/.claude/skills/teardown (unconfirmed); then npm install && npx playwright install chromium in the folder. Needs Node 20+, ffmpeg and Python 3.
Hermes: unconfirmed: copy the whole repo to ~/.hermes/skills/creative/teardown/, run the same npm command, then start a new session (copy rather than hermes skills install, unverified: whether it copies sims/ and sfx/; copying the whole folder avoids the question).
