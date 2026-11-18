# what-if-animation

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/kelano86/what-if-animation
- **GitHub repo:** https://github.com/kelano86/what-if-animation @ 8092fb5 (MIT; commit read by a project Claude; still the latest commit on 2026-10-31)
- **Price:** Free (MIT, github.com, checked 2026-10-31); voice and SFX use your ElevenLabs credits.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a project Claude (code read, 8092fb5, 2026-10-31): no safety problems reported; it borrowed three ideas into PR #6 and tested them on ep1 with no credits. Findings: needs your `ELEVENLABS_API_KEY` in the environment or a `.env` file, and each episode spends ElevenLabs credits; the studio folder runs `npm install`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/kelano86/what-if-animation ~/.claude/skills/what-if-animation, then git -C ~/.claude/skills/what-if-animation checkout 8092fb5 (the reviewed commit). Copy studio to ./what-if-studio and run npm install there (README; expected). Set ELEVENLABS_API_KEY in your environment or a .env in that folder yourself, never in chat; each episode spends your ElevenLabs credits.

## YOLO install

YOLO (your own risk): skips the commit pin.
Clone at HEAD as in the README.

## Install notes

Claude Code: `git clone https://github.com/kelano86/what-if-animation ~/.claude/skills/what-if-animation`, then `cp -r ~/.claude/skills/what-if-animation/studio ./what-if-studio` and `cd what-if-studio && npm install` (README). Add `ELEVENLABS_API_KEY` as an env var or in `.env` yourself; never paste it into chat.
