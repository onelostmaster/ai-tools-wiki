# zero-dollar-studio

- **Type:** plugin
- **Category:** generating videos, voice and audio, editing
- **Official URL:** https://github.com/TheNoumanDev/zero-dollar-studio
- **GitHub repo:** https://github.com/TheNoumanDev/zero-dollar-studio @ d265696 (committed 2026-11-01 11:38 ET, HEAD on 2026-11-03; make-video 0.1.3, snipshorts 0.1.2, cartoonsmith 0.1.2; MIT; listed as TheNoumanDev/zero-dollar-studio in awesome-claude-video-skills)
- **Price:** Free (MIT, github.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @d265696, 2026-11-03, no-intake review): Looks safe. Plugin manifests (.claude-plugin/*.json) have no hooks, MCP servers or install scripts. Setup scripts download only pinned files from official sources: a soundfont from GitHub (make-video tools/setup.sh:23-24), Hugging Face models (setup.sh:26-31), the YuNet face model from opencv_zoo (snipshorts podcast/setup.sh:17-18) and Rhubarb and Real-ESRGAN GitHub releases (cartoonsmith setup_cartoon.sh:28-44). Python and Node tools call ffmpeg, yt-dlp, fluidsynth and Remotion with argument lists, no shell=True or eval. snipshorts podcast/llm.py:33-37 pipes prompts to your logged-in claude CLI (uses your plan). Nothing is posted or uploaded (podcast/post.py:7; make-video SKILL.md:136). No telemetry or curl|bash.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add TheNoumanDev/zero-dollar-studio` then `/plugin install make-video@zero-dollar-studio` (snipshorts and cartoonsmith are add-ons in the same marketplace).
Windows: not supported as shipped. The skill checks for macOS on Apple Silicon first (make-video SKILL.md:16) and its setup uses Homebrew and the Apple GPU (tools/setup. Setup downloads about 6 GB of models from Hugging Face (Chatterbox, Whisper small.en). snipshorts needs a logged-in Claude Code CLI and yt-dlp.
