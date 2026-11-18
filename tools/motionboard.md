# motionboard

- **Type:** skill
- **Category:** generating videos, design
- **Official URL:** https://motionboard.app
- **GitHub repo:** https://github.com/krisyangdev/motionboard @ 4e1b437 (MIT; committed 2026-10-31 13:19 ET, still HEAD on 2026-11-03; plugin 1.0.0; listed as krisyangdev/motionboard in awesome-claude-video-skills)
- **Price:** Free (MIT, github.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @4e1b437, 2026-11-03, no-intake review): Looks safe. The plugin (.claude-plugin/plugin.json, marketplace.json) is one skill with no hooks, MCP servers or install scripts. skills/motionboard is markdown (SKILL.md, 38 recipes) plus 38 HTML/GSAP shot projects; their package.json files only wrap `npx --yes hyperframes@0.8.209` preview/check/render/publish (e.g. source/match-cut/package.json), no pre/postinstall. Shot HTML loads pinned GSAP 3.14.2 and three.js 0.181.2 from jsDelivr; no fetch, beacon, cookie or eval calls. SKILL.md:56-58 lists all network use (npm, fonts, CDN, one preview MP4 from media.motionboard.app) and says no telemetry. No prompt-injection text. Not reviewed: the HyperFrames CLI itself and the motionboard.app site code in src/.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/krisyangdev/motionboard.git, git checkout 4e1b437 (reviewed, plugin 1.0.0), then /plugin marketplace add <path to that folder> and /plugin install motionboard@motionboard with auto-update off. Install Node 22+ and ffmpeg yourself. Shots fetch HyperFrames with npx --yes hyperframes@0.8.209 (pinned in each shot package.json; HeyGen's CLI, unverified: its own code was not read), so run renders in a project folder with no keys in its environment. Never run the shot folders' publish script (npx hyperframes publish uploads the shot); the skill does not call it.
claude.ai: not available.

## YOLO install

YOLO (your own risk): skips the commit pin and the no-keys render folder.
/plugin marketplace add krisyangdev/motionboard then /plugin install motionboard@motionboard, or npx skills add krisyangdev/motionboard (README), at HEAD.

## Install notes

Claude Code (works on Windows): `/plugin marketplace add krisyangdev/motionboard` then `/plugin install motionboard@motionboard`, or `npx skills add krisyangdev/motionboard` (README). Needs Node 22+, ffmpeg and the HyperFrames CLI, which each shot fetches with `npx --yes hyperframes@0.8.209` (HeyGen's npm package, not reviewed here). Rendering needs internet for Google Fonts and GSAP/three.js from jsDelivr. Each shot folder's package.json also has a `publish` script (`npx hyperframes publish`); the skill never calls it, so don't run it unless you mean to upload a shot to HyperFrames. Fits the faceless AI video channel idea for motion-graphics B-roll and intros.
