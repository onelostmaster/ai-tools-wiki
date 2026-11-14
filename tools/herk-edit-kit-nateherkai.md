# herk-edit-kit (nateherkai)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/nateherkai/herk-edit-kit
- **GitHub repo:** https://github.com/nateherkai/herk-edit-kit @ 10511e5 (2.0.0; MIT LICENSE file; committed 2026-10-14 08:51 ET, still HEAD on 2026-11-09)
- **Price:** Free, MIT (LICENSE file on github.com, checked 2026-11-06; API reported NOASSERTION)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-09

## Safety reason

a review bot (code read @10511e5, 2026-11-09, no-intake review): Safe. A Claude Code and Codex workspace of video-editing skills (.claude/skills, mirrored to .agents/skills) plus Node helper scripts; no hooks, no MCP config, no settings.json; .claude/launch.json only starts a local npx hyperframes preview on port 3010. Scripts run only ffmpeg/ffprobe and node locally (cut-silences.mjs line 290, apply-cuts.mjs 167, mix.mjs 32); setup.mjs only checks node/ffmpeg/ffprobe and copies .env.example to .env (lines 8-15); nothing installs software. Network: transcribe-elevenlabs.mjs uploads audio to api.elevenlabs.io speech-to-text (line 26, fetch at 132); motion-showreel sfx.mjs calls ElevenLabs sound generation (line 31); kie.mjs makes paid Kie.ai calls and uploads files to kieai.redpandaai.co (lines 36-73), with a 'Confirm with the user first' note (line 4). Keys come from env or .env. npm dependencies are pinned in package-lock.json (hyperframes 0.7.109, gsap 3.14.2, playwright); HyperFrames skills come from heygen-com/hyperframes per skills-lock.json. CLAUDE.md leaves model and permission choices to the user. Note: video-projects/clickup-demo scripts are the author's demo; populate.mjs creates a list and about 18 tasks in ClickUp with CLICKUP_API_KEY and a hardcoded team id. Not reviewed: media assets, style-library HTML and the npm packages themselves.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @10511e5 (safe). Claude Code on Windows: clone the repo at commit 10511e5 into its own folder and open Claude Code there; the skills live in the repo's .claude/skills and only load inside that folder, so nothing is copied into %USERPROFILE%\.claude. Needs Node 22+ and ffmpeg/ffprobe on PATH (install them yourself, e.g. winget install Gyan.FFmpeg); then npm ci and npm run setup, which only checks those tools and copies .env.example to .env. Put keys in .env yourself, never in chat. Default transcription uploads your audio to ElevenLabs (ELEVENLABS_API_KEY); the motion-showreel Kie.ai and ElevenLabs sound-effect scripts are paid calls on your own credits. Do not run the video-projects/clickup-demo scripts: they are the author's demo and create tasks in a ClickUp workspace with your CLICKUP_API_KEY.
