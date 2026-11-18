# story-animator

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/deenukhan/story-animator
- **GitHub repo:** https://github.com/deenukhan/story-animator @ 6bff528 (committed 2026-10-28 ET, still HEAD on 2026-11-03; plugin 1.0.0; MIT; listed as deenukhan/story-animator in awesome-claude-video-skills)
- **Price:** Free (MIT, github.com, checked 2026-10-31); ElevenLabs usage is billed by ElevenLabs.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @6bff528, plugin 1.0.0, 2026-11-03, no-intake review): Looks safe. Plugin manifests (.claude-plugin/*.json) have no hooks, MCP servers or install scripts. scripts/mix.py:39-46 and contact_sheet.sh:10-13 run only ffmpeg/npx remotion with argument lists; transcribe.py runs faster-whisper locally. Network only to ElevenLabs (references/voice-and-sound.md:26-36, your key or connector; uses your credits), npm install of a pinned Remotion template (SKILL.md:72) and Google Fonts at render. No telemetry, eval or curl|bash.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/deenukhan/story-animator.git, git checkout 6bff528 (reviewed, plugin 1.0.0), then /plugin marketplace add <path to that folder> and /plugin install story-animator@story-animator with auto-update off. Install Node.js, Python 3 and ffmpeg (winget install ffmpeg) yourself; put faster-whisper in a venv. Voice: use the ElevenLabs connector or set ELEVENLABS_API_KEY in your own environment, never in chat; every narration spends your ElevenLabs credits (references/voice-and-sound.md lines 26-36). The skill runs npm install on a pinned Remotion 4.0.534 template (SKILL.md line 72); that is expected.
claude.ai: not available (Claude Code plugin).

## YOLO install

YOLO (your own risk): skips the commit pin.
/plugin marketplace add deenukhan/story-animator then /plugin install story-animator@story-animator (README) at HEAD.

## Install notes

Claude Code (Windows): `/plugin marketplace add deenukhan/story-animator` then `/plugin install story-animator@story-animator`, or copy `skills/story-animator` into your Claude skills folder (README).
Needs Node.js (the skill runs `npm install` on a pinned Remotion 4.0.534 template), ffmpeg (`winget install ffmpeg`) and Python 3; word timing needs faster-whisper in a venv. Voice: the ElevenLabs connector, or an `ELEVENLABS_API_KEY` you set in your own environment (never paste it into chat). Remotion's own license terms apply to rendered videos.
