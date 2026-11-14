# graphify

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://github.com/Graphify-Labs/graphify
- **GitHub repo:** [https://github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a0946f9): Looks safe. Local code knowledge graph; no telemetry, query log off by default; LLM extraction only with your own key; the Claude install adds PreToolUse search/read hooks to `.claude/settings.json`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `uv tool install graphifyy` (PyPI name has two y's), then `graphify install` (adds PreToolUse hooks to `.claude/settings.json`).
Hermes: `uv tool install graphifyy`, then `graphify install --platform hermes` (README:241).
