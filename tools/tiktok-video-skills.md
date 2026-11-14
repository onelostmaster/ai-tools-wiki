# tiktok-video-skills

- **Type:** skill
- **Category:** generating videos, social posting
- **Official URL:** https://github.com/iart-ai/tiktok-video-skills
- **GitHub repo:** https://github.com/iart-ai/tiktok-video-skills @ 2a77533 (plugin 0.1.0; MIT; committed 2026-06-22 09:24 ET, HEAD on 2026-11-11)
- **Price:** Free (MIT LICENSE file); iart.ai hosted agent is separate, price unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-11

## Safety reason

a review bot (code read @2a77533, 2026-11-11, no-intake review): Safe. Four markdown skills (skills/*/SKILL.md plus references/*.md, Remotion code examples) and three short bash helpers; .claude-plugin/plugin.json and marketplace.json only name the plugin (no hooks, no MCP servers, no settings, no allowed-tools, nothing asks for keys). scripts/contact-sheet.sh (17 lines) and probe-mp4.sh (24 lines) only call ffmpeg/ffprobe on files you pass; scripts/seek-shot.sh line 17 runs npx -y playwright screenshot on a local HTML file, which fetches Playwright unpinned. showcase.html (demo page, not part of the skill) loads GSAP from cdnjs and Google Fonts. Skill footers link to iart.ai with tracking parameters (promotional only). Not reviewed: showcase.gif.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @2a77533 (plugin 0.1.0) (safe). Claude Code on Windows, pinned: download the repo at commit 2a77533 (or git clone, then git checkout 2a77533) and copy the four folders under skills\\ (short-form-video, caption-animation, countdown-video, lower-thirds) into %USERPROFILE%\.claude\\skills\\ or a project's .claude\\skills folder. Unpinned alternative (README): /plugin marketplace add iart-ai/tiktok-video-skills, then /plugin install tiktok-video-skills. The skills write Remotion (React) code, so a render needs Node.js and a Remotion project (npx remotion render ...); ffmpeg/ffprobe (e.g. winget install Gyan.FFmpeg) for the checks. The three helper scripts in scripts\\ are bash only (use Git Bash or WSL, or skip them); seek-shot.sh runs npx -y playwright, which downloads Playwright and Chromium unpinned on first use. Links to iart.ai in the skills are ads for a paid hosted service; nothing needs an account or key.
