# agent-sprite-forge (0x0funky)

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://github.com/0x0funky/agent-sprite-forge
- **GitHub repo:** https://github.com/0x0funky/agent-sprite-forge @ 5324342 (MIT; last commit 2026-10-06)
- **Price:** Free, MIT (github.com, checked 2026-11-03); image/video API calls are paid per use by the provider
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @5324342, 2026-11-03): caution for money, not malware. Generation goes to any paid API whose key is configured (OpenAI, Gemini, xAI, BytePlus, fal.ai) and the skill treats the configured key as consent with no per-call question (skills/generate2dmedia/SKILL.md:23); no spend cap by default, only a ledger and optional --budget-usd (SKILL.md:51). Local Codex CLI route runs read-only, ephemeral (skills/generate2dmedia/scripts/cli_media.py:761). No telemetry found. Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (only one provider key configured outside chat and --budget-usd passed on every run); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Claude Code on Windows: copy the skills folder from https://github.com/0x0funky/agent-sprite-forge at commit 5324342 into %USERPROFILE%\.claude\\skills. Configure only the one provider key you want charged, in an env var or %APPDATA%\\agent-sprite-forge\\config.json (SKILL.md:47), never in chat, and always pass --budget-usd (SKILL.md:51); without it the skill spends on any configured key with no per-call question (skills/generate2dmedia/SKILL.md:23). Needs Python (numpy, Pillow, scipy) and ffmpeg for video. Android: no.

## YOLO install

YOLO (your own risk): skips the single key and the budget cap.
Claude Code on Windows: add the skills folder with all your provider keys set; it spends on any of them with no cap and no question.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Claude Code on Windows: add the skills folder; set --budget-usd and keep keys in env or %APPDATA%\\agent-sprite-forge\\config.json (SKILL.md:47), never in chat. Needs Python (numpy, Pillow, scipy) and ffmpeg for video. Android: no.
