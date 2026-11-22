# stickman-video-director (kaomei)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/kaomei/stickman-video-director
- **GitHub repo:** https://github.com/kaomei/stickman-video-director @ 7fa6a9a (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-20); image, voice and video services it connects bill separately (README FAQ)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-21

## Safety reason

a review bot code read @7fa6a9a: safe with the fixes in Safe install. The only network call in the scripts is the Gemini image/audio request in scripts/gemini-media.mjs:33 (generativelanguage.googleapis.com), which reads GEMINI_API_KEY from the environment and refuses to run without it, telling you not to paste it in chat (gemini-media.mjs:16). Child processes are started as argument lists (ffmpeg, ffprobe, python3), never shell strings (e.g. a6_finish.py:166-252, b-delivery-completeness.mjs:23). B6 runs agent-written scene files with exec but blocks them from starting processes with an audit hook (b6_production.py:100,171-174). Two npm dependencies, @napi-rs/canvas 0.1.100 and sharp 0.35.5, pinned with a lockfile and no install scripts (package.json; package-lock.json). Whisper caption alignment is optional and downloads a model only with --allow-model-download (align_captions.py:29-31). The skill forbids starring, following or publishing for you (thumbnail-publishing-kit.md:10,17). Verified behaviour and fixes: (1) the README's default install is a prompt telling your agent to install it and set up anything missing (README.en.md:190-198), and the terminal route is the third-party npx skills add installer at the moving main branch (installation-troubleshooting.md:10); fix: pinned sparse clone at 7fa6a9a copied into one agent by hand. (2) B mode needs npm ci in the skill folder (autopilot.md:35; autopilot-runtime.md:6), which downloads the two pinned native packages from npm; fix: run npm ci yourself, nothing global. (3) A mode defaults to driving Google Flow in the agent's built-in browser with your sign-in and spends your Flow credits once you authorize a test or production (mode-execution-boundaries.md:49-53,59); fix: authorize only prompts, or give an explicit total credit cap when you authorize generation. (4) B6 starts python3 by default (autopilot.mjs:28; b6-production.mjs:60), which on Windows is often the Store alias; fix: set B6_PYTHON to a venv python with the pinned assets/b6/hong-kong-v90/requirements.txt (numpy 2.0.2, Pillow 11.3.0, opencv-python-headless 4.13.0.92). Unverified: the npx skills installer CLI and the Flow/Gemini/ElevenLabs services were not code-read; containment: don't use npx skills add, keep only the key you choose in the session environment, set a credit cap.

## Safe install

Safe install (fixes applied): Claude Code on Windows (Git 2.25+, Node.js 20+, FFmpeg and FFprobe on PATH; normal terminal): git clone --filter=blob:none --sparse https://github.com/kaomei/stickman-video-director.git %USERPROFILE%\\src\\stickman-video-director && cd %USERPROFILE%\\src\\stickman-video-director && git checkout 7fa6a9a && git sparse-checkout set skills/directing-stickman-videos && xcopy /E /I skills\\directing-stickman-videos %USERPROFILE%\.claude\\skills\\directing-stickman-videos. For B mode (code-rendered videos): cd %USERPROFILE%\.claude\\skills\\directing-stickman-videos && npm ci && node scripts/autopilot.mjs doctor. For B6 only: py -m venv %USERPROFILE%\.venvs\\stickman && %USERPROFILE%\.venvs\\stickman\\Scripts\\pip install -r assets\\b6\\hong-kong-v90\\requirements.txt and set B6_PYTHON=%USERPROFILE%\.venvs\\stickman\\Scripts\\python.exe. Don't paste the README's \"Help me install this skill\" prompt and don't use npx skills add. Keys: only set GEMINI_API_KEY in that terminal if you want Gemini images or voice; for A mode authorize prompts only, or give a total credit cap before any Flow generation. Hermes: same pinned sparse clone, copy skills/directing-stickman-videos to ~/.hermes/skills/creative/directing-stickman-videos. claude.ai: no (B mode needs local Node and FFmpeg). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the hand copy and the credit cap. npx skills add kaomei/stickman-video-director --skill directing-stickman-videos (installation-troubleshooting.md:10; third-party installer, moving main branch, asks which agent and scope), or paste the README's "Help me install this skill" prompt and let the agent set up what is missing.

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied (pinned sparse clone at 7fa6a9a copied into one agent by hand, npm ci only inside the skill folder, B6 Python in a venv via B6_PYTHON, keys only in the environment, prompts-only or a total credit cap for A mode). Turns a script into stickman videos: B mode renders locally with Node and FFmpeg, A mode writes prompts and can generate on Google Flow with your credits. Strong fit for the faceless video channel.
