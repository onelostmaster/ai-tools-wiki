# claude-video-kit (runesleo)

- **Type:** plugin
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/runesleo/claude-video-kit
- **GitHub repo:** https://github.com/runesleo/claude-video-kit @ 3a908d8 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-23); CosyVoice/DashScope and Fish Audio are separate paid services (price not checked)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-23

## Safety reason

Not code-reviewed for safety. README: installs as a Claude Code or Codex plugin from the runesleo/x-reader marketplace or this repo; local rendering needs Node 20+, Python 3.10+, ffmpeg, npm install in remotion/ and pip install -r scripts/requirements.txt; the keyless demo uses the macOS say voice only; production narration sends text to CosyVoice (DASHSCOPE_API_KEY) by default or Fish Audio. Latest tag is a release candidate (v0.3.0-rc). Repo, license and latest commit confirmed from github.com metadata, 2026-11-23.

## Safe install

Unreviewed: contain it: clone at the pinned commit 3a908d8 inside a devcontainer or sandbox, install Python packages in a venv there, use a separate low-quota DashScope or Fish Audio key only when you need narration, and keep network on only for npm ci / pip and the TTS call. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code on Windows: /plugin marketplace add runesleo/claude-video-kit then /plugin install video-explainer-kit@video-explainer (README). Rendering: git clone, npm ci --prefix remotion, pip install -r scripts/requirements.txt; needs Node 20+, Python 3.10+, ffmpeg. The no-key demo is macOS-only.
