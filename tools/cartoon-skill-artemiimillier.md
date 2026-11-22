# cartoon-skill (artemiimillier)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/artemiimillier/cartoon-skill
- **GitHub repo:** https://github.com/artemiimillier/cartoon-skill @ e92360c (MIT)
- **Price:** Skill free on GitHub, MIT (LICENSE file, checked 2026-11-21); Viralex AI price unknown
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-21

## Safety reason

Not code-reviewed for safety. README (e92360c) lines 41-43: setup requires connecting the third-party Viralex AI MCP (https://mcp.viralex.ai/mcp) before anything else; line 98: optional OPENAI/GEMINI/ELEVENLABS keys and a TELEGRAM_BOT_TOKEN go in cartoon/.env; kit/scripts/send_telegram.py exists. Unverified: the Python/Node scripts and what Viralex receives -> Contain: separate project, pinned commit, no keys, no Telegram, demo render only. Checked 2026-11-21.

## Safe install

Unreviewed: contain it: clone into a separate project folder on Windows, git checkout e92360c, read .claude/skills/cartoon/SKILL.md and kit/package.json first, copy the skill into that project's .claude\\skills\\ only (not %USERPROFILE%\.claude\\skills\), skip the Viralex MCP and send_telegram.py, add no API keys or bot tokens, keep Claude Code's normal permission prompts on. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: clone into a separate project folder on Windows, git checkout e92360c, read .claude/skills/cartoon/SKILL.md and kit/package.json first, copy the skill into that project's .claude\\skills\\ only (not %USERPROFILE%\.claude\\skills\), skip the Viralex MCP and send_telegram.py, add no API keys or bot tokens, keep Claude Code's normal permission prompts on.
