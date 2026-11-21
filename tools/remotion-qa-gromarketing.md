# remotion-qa (GroMarketing)

- **Type:** CLI
- **Category:** generating videos, editing, video analysis
- **Official URL:** https://github.com/GroMarketing/remotion-qa
- **GitHub repo:** https://github.com/GroMarketing/remotion-qa @ dd246e9 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-17)
- **Decision:** Later
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

a review bot code read @dd246e9: safe with the fixes in Safe install. One dependency, ffmpeg-static (lockfile pins 5.3.0 with an integrity hash, package-lock.json:107-111). No telemetry, no API keys, and no network calls in its own code (no fetch or http in src/ or bin/). Video inputs are passed to ffmpeg as local files only with every other protocol refused (src/ffmpeg.mjs:14-18). The Claude Code plugin is the skill text only, no hooks or scripts (.claude-plugin/plugin.json, marketplace.json). Verified behaviour and fixes: (1) ffmpeg-static has an install script that downloads an ffmpeg binary (package-lock.json:111), and if that binary is missing and no ffmpeg is on PATH, remotion-qa runs that download itself on first use (src/ffmpeg.mjs:37-43); fix: install with --ignore-scripts and set REMOTION_QA_FFMPEG to your own ffmpeg, which it uses before anything else (src/ffmpeg.mjs:31). (2) The skill and README call npx remotion-qa (SKILL.md:16,44,59,73), which fetches the latest version from npm when it is not installed in the project; fix: install it in the project at the pinned commit so npx uses that copy. (3) The render command runs npx remotion render (bin/remotion-qa.mjs:100) and, when the pace check fails, deletes any existing <out>.failed-pace.mp4 and moves the new render there (bin/remotion-qa.mjs:104-106); on Windows Node will not start npx.cmd without a shell, so render fails there (Node child_process docs); fix: render with npx remotion render yourself, then run remotion-qa check. (4) --frames writes PNGs and overwrites files with the same name in that folder (src/safezone.mjs:106-108); fix: give it a new empty folder.

## Safe install

Safe install (fixes applied): Claude Code on Windows, inside one Remotion project (needs Node 18+): winget install Gyan.FFmpeg, then setx REMOTION_QA_FFMPEG "<full path to ffmpeg.exe>" and open a new terminal; in the project folder npm install --save-dev --ignore-scripts github:GroMarketing/remotion-qa#dd246e9 (never global; --ignore-scripts stops the ffmpeg download). Render with npx remotion render yourself, then npx remotion-qa check out\\video.mp4 --beats captions.srt --frames qa-frames-<new folder>; don't use remotion-qa render. Skill: copy node_modules\\remotion-qa\\skills\\remotion-qa to %USERPROFILE%\.claude\\skills\\remotion-qa (text only). Hermes: same project install, copy the same skill folder into your Hermes skills folder. claude.ai: no (needs local Node and ffmpeg). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, --ignore-scripts and your own ffmpeg. npm install --save-dev remotion-qa (README.md:52; ffmpeg-static downloads its ffmpeg binary) or plain npx remotion-qa (latest from npm each time); Claude Code plugin: /plugin install remotion-qa@remotion-qa (README.md:198).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Checks rendered Reels/Shorts videos for dead air, captions too fast to read, text under the platform UI and mobile font floors; local only, no keys, no telemetry.
