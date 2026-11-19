# motlab (staryone)

- **Type:** CLI
- **Category:** generating videos, editing
- **Official URL:** https://github.com/staryone/motlab
- **GitHub repo:** https://github.com/staryone/motlab @ 9a44f75 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-18)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-18

## Safety reason

Not code-reviewed for safety. README: needs Node 24+, Chrome or Chromium and ffmpeg/ffprobe on PATH; the npm route installs globally (npm install -g @motlab/cli) and setup copies the skills into the agent skill folder; the clone route (node install.js) runs npm ci and puts a motlab command in ~/.local/bin. Both routes add a motlab command to your user PATH; this always happens. Repo, license and latest commit confirmed from github.com metadata, 2026-11-18.

## Safe install

Unreviewed: contain it: clone at the pinned commit 9a44f75 inside a devcontainer or sandbox (not your main Windows profile), run node install.js --skill none there so nothing is copied into your real skills folder, no API keys (it needs none), and keep network on only for the npm ci step. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code on Windows: npm install -g @motlab/cli then npx @motlab/cli setup (README; installs globally and copies the skills to %USERPROFILE%\.claude\\skills). Codex: npx @motlab/cli setup --skill agents. Needs Node 24+, Chrome and ffmpeg.
