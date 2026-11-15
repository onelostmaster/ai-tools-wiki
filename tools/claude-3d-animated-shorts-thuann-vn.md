# claude-3d-animated-shorts (thuann-vn)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/thuann-vn/claude-3d-animated-shorts
- **GitHub repo:** https://github.com/thuann-vn/claude-3d-animated-shorts @ f5b4c4a (MIT; HEAD on 2026-11-13; fork-style rework of mromidev/claude-animated-shorts, MIT)
- **Price:** Free (MIT LICENSE, checked at commit f5b4c4a on 2026-11-13); bundled furniture CC0 (Kenney, KayKit); ElevenLabs voice, if used, is billed by ElevenLabs.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @f5b4c4a, 2026-11-13, no-intake review): Safe. One skill (SKILL.md, 80 lines of instructions, no hooks, MCP server or commands) plus a local three.js engine (engine/*.js, about 1,550 lines) and small Python/Node helpers. render.cjs serves the engine folder on a random localhost port with a path check, drives headless Chrome through puppeteer-core and pipes frames to ffmpeg (lines 8-21). Network use: fetch-assets.sh downloads fixed asset files from three.js r170, Google Fonts (unpinned main branch), rsms/inter v3.19 and the Poly Haven API (lines 8-27); tools/tts.mjs sends your script text to ElevenLabs with your key (lines 6-12). main.js line 683 posts viewer OK/fix notes to a same-origin /api/feedback path that the bundled servers do not have, so nothing leaves your machine. No telemetry, no shell-outs beyond ffmpeg. Caveats: the look copies a named YouTube channel's style (style only, no frames included), so keep your own characters and stories; importmap names ez-tree and three.quarks that package.json does not install.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Git Bash): `git clone https://github.com/thuann-vn/claude-3d-animated-shorts "$USERPROFILE/.claude/skills/claude-3d-animated-shorts"`, then `git -C "$USERPROFILE/.claude/skills/claude-3d-animated-shorts" checkout f5b4c4a` (the reviewed commit), then `scripts/fetch-assets.sh` and `npm ci` (or `npm install`) in engine/. This folder installs it for your user in every project; clone into the project's `.claude/skills/` instead to keep it to one project. Set CHROME to your chrome.exe path (render.cjs:6 only checks Mac and Linux paths). Voice is optional: ELEVENLABS_API_KEY in an environment variable, and set LANG_CODE and VOICE, because tools/tts.mjs defaults to Vietnamese and the author's voice id.

## YOLO install

YOLO (your own risk): skips the commit pin.
git clone https://github.com/thuann-vn/claude-3d-animated-shorts %USERPROFILE%\.claude\\skills\\claude-3d-animated-shorts, then scripts/fetch-assets.sh and npm install in engine/

## Install notes

Code-reviewed by a review bot @f5b4c4a (safe). Claude Code on Windows: git clone https://github.com/thuann-vn/claude-3d-animated-shorts into %USERPROFILE%\.claude\\skills\\claude-3d-animated-shorts (README Install). Then, in Git Bash, run scripts/fetch-assets.sh (downloads the Xbot rig and horse from three.js r170, two fonts and 28 Poly Haven CC0 props; nothing is executed) and npm install in engine/ (three, postprocessing, n8ao, puppeteer-core; no install scripts). Needs Node 18+, Python 3 with Pillow, ffmpeg and Chrome. On Windows set CHROME to your chrome.exe path, because render.cjs only looks in Mac and Linux paths (render.cjs line 6). Voice is optional: tools/tts.mjs uses your own paid ElevenLabs key from ELEVENLABS_API_KEY (or ~/.config/elevenlabs/key) and defaults to Vietnamese and the author's voice id, so set LANG_CODE and VOICE; keep the key in an environment variable, never in chat. Not on claude.ai (needs local Node, ffmpeg and Chrome). Install is unpinned, so later commits arrive without a review.
