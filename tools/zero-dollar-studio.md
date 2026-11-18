# zero-dollar-studio

- **Type:** plugin
- **Category:** generating videos, voice and audio, editing
- **Official URL:** https://github.com/TheNoumanDev/zero-dollar-studio
- **GitHub repo:** https://github.com/TheNoumanDev/zero-dollar-studio @ d265696 (committed 2026-11-01 11:38 ET, HEAD on 2026-11-03; make-video 0.1.3, snipshorts 0.1.2, cartoonsmith 0.1.2; MIT; listed as TheNoumanDev/zero-dollar-studio in awesome-claude-video-skills)
- **Price:** Free (MIT, github.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @d265696, 2026-11-03, no-intake review): Looks safe. Plugin manifests (.claude-plugin/*.json) have no hooks, MCP servers or install scripts. Setup scripts download only pinned files from official sources: a soundfont from GitHub (make-video tools/setup.sh:23-24), Hugging Face models (setup.sh:26-31), the YuNet face model from opencv_zoo (snipshorts podcast/setup.sh:17-18) and Rhubarb and Real-ESRGAN GitHub releases (cartoonsmith setup_cartoon.sh:28-44). Python and Node tools call ffmpeg, yt-dlp, fluidsynth and Remotion with argument lists, no shell=True or eval. snipshorts podcast/llm.py:33-37 pipes prompts to your logged-in claude CLI (uses your plan). Nothing is posted or uploaded (podcast/post.py:7; make-video SKILL.md:136). No telemetry or curl|bash.

## Safe install

Safe install (fixes applied):
Windows: no working install as shipped: make-video SKILL.md line 16 requires macOS on Apple Silicon and tools/setup.sh lines 2-15 use Homebrew and the Apple GPU, so it needs porting (for example under WSL2) first. If you port it: git clone https://github.com/TheNoumanDev/zero-dollar-studio.git, git checkout d265696 (reviewed), /plugin marketplace add <path to that folder>, /plugin install make-video@zero-dollar-studio with auto-update off; setup downloads about 6 GB of pinned models from Hugging Face. snipshorts sends prompts to your logged-in claude CLI and uses your plan (podcast/llm.py lines 33-37). Nothing is posted or uploaded.

## YOLO install

YOLO (your own risk): skips the commit pin.
/plugin marketplace add TheNoumanDev/zero-dollar-studio then /plugin install make-video@zero-dollar-studio (README) at HEAD; still Mac-only.

## Install notes

Claude Code: `/plugin marketplace add TheNoumanDev/zero-dollar-studio` then `/plugin install make-video@zero-dollar-studio` (snipshorts and cartoonsmith are add-ons in the same marketplace).
Windows: not supported as shipped. Setup downloads about 6 GB of models from Hugging Face (Chatterbox, Whisper small.en). snipshorts needs a logged-in Claude Code CLI and yt-dlp.
