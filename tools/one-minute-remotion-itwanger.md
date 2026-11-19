# one-minute-remotion (itwanger)

- **Type:** skill
- **Category:** generating videos, education
- **Official URL:** https://github.com/itwanger/one-minute-remotion
- **GitHub repo:** https://github.com/itwanger/one-minute-remotion @ 02dbfc4 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot code read @02dbfc4: safe with the fixes in Safe install. No hooks, no MCP config, no telemetry; helpers call only ffmpeg/ffprobe/node locally (align_words.py:8, gen_cues.py:41,69, import_audio.py:30, verify_export.py:5); init_project.py:1,74 never installs, synthesizes or overwrites. Verified risks and fixes: (1) README:56-60 install is `npx skills add ... -g` (-y skips prompts): it installs for every project through the unpinned Vercel skills CLI; fix: copy the folder at commit 02dbfc4 yourself. (2) Project npm deps are pinned (remotion/templates/package.json: @remotion/cli 4.0.521, react 19.2.3) with a package-lock.json; fix: npm ci, not npm install. (3) README:122: the first render downloads Chromium; remotion.mjs:16-17 uses REMOTION_BROWSER_EXECUTABLE if set; fix: point it at your installed Chrome. (4) Optional Volcengine TTS: key read only from env VOLC_TTS_API_KEY (project_paths.py:27-29) and sent as X-Api-Key to the apiBase in video.config.json (gen_audio.py:8-13; apiBase empty by default); fix: key in env only, apiBase set to Volcengine's own endpoint, or import your own audio (import_audio.py) and skip TTS. (5) start_studio.py:38-42 starts Remotion Studio detached in the background (start_new_session) and leaves it running; fix: stop it yourself (PID in preview/studio/studio.json). Unverified: which network interface Remotion Studio listens on (remotion.mjs:21 passes only --port); contained by allowing Node on private networks only when Windows Firewall asks. Bundled huashu drawing library is MIT and SHA-256 checked before copying (install_huashu.py:15-17); fonts OFL; SKILL.md:10 says no author voice, clone model or credentials are bundled.

## Safe install

Safe install (fixes applied): Claude Code on Windows: git clone https://github.com/itwanger/one-minute-remotion, git checkout 02dbfc4, copy the whole folder (not only SKILL.md) to %USERPROFILE%\.claude\\skills\\one-minute-remotion (or <project>\.claude\\skills\\ for one project); do not use `npx skills add -g -y`. Needs Node.js 22.20+, Python 3.10+, FFmpeg/ffprobe (README:122). In each video project run `npm ci` (uses the bundled lock), set REMOTION_BROWSER_EXECUTABLE to your installed Chrome so no Chromium is downloaded, and allow Node on private networks only. Voice: import your own WAV/MP3, or put VOLC_TTS_API_KEY in an environment variable (never in chat or config) and set apiBase only to Volcengine's own endpoint. Stop the background Studio when done (PID in preview/studio/studio.json). claude.ai: upload the release zip one-minute-remotion.zip as a skill for script and storyboard only; rendering needs local commands. Hermes: not supported (no Hermes loader). Android: no.

## YOLO install

YOLO (your own risk): skips the pinned commit, the lockfile install, the Chrome path and the firewall limit. npx skills add itwanger/one-minute-remotion -g -a claude-code -y (README:59), then npm install in each project; the first render downloads Chromium.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied. Output is Chinese-language science explainers by default (SKILL.md:3); stages stop for your approval each step and export only when you say so (SKILL.md:12-20).
