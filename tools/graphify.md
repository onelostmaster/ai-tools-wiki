# graphify

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://github.com/Graphify-Labs/graphify
- **GitHub repo:** [https://github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a0946f9): Looks safe. Local code knowledge graph; no telemetry, query log off by default; LLM extraction only with your own key; the Claude install adds PreToolUse search/read hooks to `.claude/settings.json`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): uv tool install graphifyy (two y's), then graphify install. That step adds PreToolUse search/read hooks to .claude/settings.json every time (that is how it works); open the file afterwards and check only graphify's hook lines were added. LLM extraction runs only with your own key, kept in an env var. Hermes: uv tool install graphifyy, then graphify install --platform hermes (README:241). No telemetry; query log off by default.

## YOLO install

Not written yet.

## Install notes

Claude Code: `uv tool install graphifyy` (PyPI name has two y's), then `graphify install` (adds PreToolUse hooks to `.claude/settings.json`).
Hermes: `uv tool install graphifyy`, then `graphify install --platform hermes` (README:241).
