# Claude Code Mods (official feature)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub repo:** none (built into Claude Code)
- **Price:** Included with Claude Code
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-18

## Safety reason

Claude docs read (code.claude.com mods overview, 2026-11-18): safe with fixes. Mods run unsandboxed with your permissions, see every prompt and can approve tool calls; the built-in guard cc-plugin-sec-default stops a user mod from overriding deny/ask rules. claude plugin validate lists a mod's hooks and calls before install; --safe-mode or "disableAllHooks": true turn installed mods off. Fix: validate first, trusted marketplaces only.

## Safe install

Safe install (fixes applied):
Built in (v2.1.287+). Before installing any mod: clone it and run claude plugin validate ./<mod>; read its hooks: and calls: lines; install only from marketplaces you trust, pinned to a commit; check cc-plugin-sec-default shows under /plugin → Installed; kill switch "disableAllHooks": true.

## YOLO install

YOLO (your own risk): skips validate and the pin.
Install any mod Claude writes or a marketplace offers.

## Install notes

Ask the user before installing.
Claude Code (local only): built in (v2.1.287 or later); nothing to install. Check `claude --version` and see loaded mods with `/plugin`.
Claude Code (local only): kill switch `"disableAllHooks": true` or start with `--safe-mode`; review a mod with `claude plugin validate` on its folder (Claude-written mods live in `~/.claude/dev-mods/`).
Hermes: no equivalent (Claude Code only).
