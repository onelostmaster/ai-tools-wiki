# Bang Motion

- **Type:** plugin
- **Category:** generating videos
- **Official URL:** https://github.com/bangtutorial/bang-motion
- **GitHub repo:** [https://github.com/bangtutorial/bang-motion](https://github.com/bangtutorial/bang-motion)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, c1aa65e): Looks safe. Instructions plus HTML starters; no telemetry, beacons, eval, hooks, postinstall, `curl|bash` or self-update; scripts are local only. Caveats: starters load GSAP/Three.js/Google Fonts from CDNs (pinned, no SRI); `scripts/ae/bridge` has unpinned puppeteer ^25 and no lockfile; the optional After Effects route relays renders through Higgsfield's MCP and CloudFront.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add bangtutorial/bang-motion` then `/plugin install bang-motion@bang-motion` (README), or clone it into `~/.claude/skills/bang-motion` (one copy only)
Hermes: unconfirmed: copy the whole repo to `~/.hermes/skills/creative/bang-motion/` and start a new session
Optional MP4 export: `npm i puppeteer` plus ffmpeg
