# claude-code-mods (hamzafer)

- **Type:** plugin
- **Category:** developer tools, 3D and games
- **Official URL:** https://github.com/hamzafer/claude-code-mods
- **GitHub repo:** https://github.com/hamzafer/claude-code-mods @ 5cef0d3 (2026-11-01; npm claude-code-mods 0.4.1 with provenance; MIT; not a fork)
- **Price:** Free, MIT (`LICENSE`, checked 2026-11-02). Optional mods need paid keys: openai-balance (OpenAI admin key), openrouter-balance, switchboard (TypeSafe Jev / Vercel AI Gateway / OpenAI).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @5cef0d3, a review, 2026-11-02): mixed.tsx:228-232`). Caution: `npx claude-code-mods@latest` is unpinned and pulls the mod list from main (`cli/src/catalog.js:6,16`); community mods are others' code; switchboard, openai-balance, openrouter-balance, now-playing send data to outside APIs. No telemetry, eval or curl|bash.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: only the three safe mods, by hand (docs/install.md): `claude plugin marketplace add hamzafer/claude-code-mods`, then `claude plugin install context-bar@claude-code-mods` (likewise `blast-radius@claude-code-mods`, `agent-radar@claude-code-mods`), restart Claude Code. Needs Claude Code 2.1.287+. Skip the npx checklist and the network mods.
Windows: blast-radius and agent-radar call bash, find, du, lsof and sh; run Claude Code in WSL or Git Bash (untested).
