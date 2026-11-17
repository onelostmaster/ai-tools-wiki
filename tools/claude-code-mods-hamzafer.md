# claude-code-mods (hamzafer)

- **Type:** plugin
- **Category:** developer tools, 3D and games
- **Official URL:** https://github.com/hamzafer/claude-code-mods
- **GitHub repo:** https://github.com/hamzafer/claude-code-mods @ 5cef0d3 (2026-11-01; npm claude-code-mods 0.4.1 with provenance; MIT; not a fork)
- **Price:** Free, MIT (`LICENSE`, checked 2026-11-02). Optional mods need paid keys: openai-balance (OpenAI admin key), openrouter-balance, switchboard (TypeSafe Jev / Vercel AI Gateway / OpenAI).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @f6f08c6 (2026-11-16): safe with fixes. context-bar, blast-radius and agent-radar have no network code. The npx claude-code-mods checklist pulls the mod list from main (cli/src/catalog.js:6, 16), and switchboard, openai-balance, openrouter-balance and now-playing send data to outside APIs. Fix: pinned marketplace, the three local mods only.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add hamzafer/claude-code-mods#f6f08c6, then claude plugin install context-bar@claude-code-mods (likewise blast-radius, agent-radar); skip the npx checklist and network mods. Needs Claude Code 2.1.287+.

## YOLO install

YOLO (your own risk): skips the pin and the mod filter.
npx claude-code-mods@latest and pick any mods.

## Install notes

Ask the user before installing.
Claude Code: only the three safe mods, by hand (docs/install.md): `claude plugin marketplace add hamzafer/claude-code-mods`, then `claude plugin install context-bar@claude-code-mods` (likewise `blast-radius@claude-code-mods`, `agent-radar@claude-code-mods`), restart Claude Code. Needs Claude Code 2.1.287+. Skip the npx checklist and the network mods.
Windows: blast-radius and agent-radar call bash, find, du, lsof and sh; run Claude Code in WSL or Git Bash (untested).
