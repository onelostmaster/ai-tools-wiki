# ElevenLabs agent skills

- **Type:** skill
- **Category:** voice and audio
- **Official URL:** https://elevenlabs.io/blog/elevenlabs-agent-skills
- **GitHub repo:** [https://github.com/elevenlabs/skills](https://github.com/elevenlabs/skills) (not in the source; ElevenLabs' blog installs it as `elevenlabs/skills`, checked 2026-10-31)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @1d84076 (2026-11-15): safe with fixes. Plain skill docs. Each SKILL.md runs npx -y @elevenlabs/cli@latest onboard init only when ELEVENLABS_API_KEY is unset (for example voice-isolator/SKILL.md:13). Fix: set a restricted key first so that line never runs. Each call spends your ElevenLabs credits. The claude.ai ElevenLabs connector covers most of this already.

## Safe install

Safe install (fixes applied):
Copy the skill folders you need from 1d84076 into ~/.claude/skills; create an ElevenLabs API key limited to those endpoints with a credit quota; set ELEVENLABS_API_KEY as an env secret before first use; no global CLI install.

## YOLO install

YOLO (your own risk): skips the key and pin, so the skill runs the latest CLI sign-in.
Install with npx skills add elevenlabs/skills and let it onboard.

## Install notes

Ask the user before installing. Copy the skill folders you need from 1d84076 into ~/.claude/skills; create an ElevenLabs API key limited to those endpoints with a credit quota; set ELEVENLABS_API_KEY as an env secret before first use; no global CLI install.
