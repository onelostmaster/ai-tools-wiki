# agent-sprite-forge (0x0funky)

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://github.com/0x0funky/agent-sprite-forge
- **GitHub repo:** https://github.com/0x0funky/agent-sprite-forge @ 5324342 (MIT; last commit 2026-10-06)
- **Price:** Free, MIT (github.com, checked 2026-11-03); image/video API calls are paid per use by the provider
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @5324342, 2026-11-03): caution for money, not malware. Generation goes to any paid API whose key is configured (OpenAI, Gemini, xAI, BytePlus, fal.ai) and the skill treats the configured key as consent with no per-call question (`skills/generate2dmedia/SKILL.md:23`); no spend cap by default, only a ledger and optional --budget-usd (`SKILL.md:51`). Local Codex CLI route runs read-only, ephemeral (`skills/generate2dmedia/scripts/cli_media.py:761`). No telemetry found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code on Windows: add the skills folder; set --budget-usd and keep keys in env or %APPDATA%\\agent-sprite-forge\\config.json (`SKILL.md:47`), never in chat. Needs Python (numpy, Pillow, scipy) and ffmpeg for video. Android: no.
