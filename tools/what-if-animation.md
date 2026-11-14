# what-if-animation

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/kelano86/what-if-animation
- **GitHub repo:** https://github.com/kelano86/what-if-animation @ 8092fb5 (MIT; commit read by a project Claude; still the latest commit on 2026-10-31)
- **Price:** Free (MIT, github.com, checked 2026-10-31); voice and SFX use your ElevenLabs credits.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a project Claude (code read, 8092fb5, 2026-10-31): no safety problems reported; it borrowed three ideas into PR #6 and tested them on ep1 with no credits. Findings: needs your `ELEVENLABS_API_KEY` in the environment or a `.env` file, and each episode spends ElevenLabs credits; the studio folder runs `npm install`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `git clone https://github.com/kelano86/what-if-animation ~/.claude/skills/what-if-animation`, then `cp -r ~/.claude/skills/what-if-animation/studio ./what-if-studio` and `cd what-if-studio && npm install` (README). Add `ELEVENLABS_API_KEY` as an env var or in `.env` yourself; never paste it into chat.
