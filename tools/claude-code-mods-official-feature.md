# Claude Code Mods (official feature)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub repo:** none (built into Claude Code)
- **Price:** Included with Claude Code
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-04

## Safety reason

a review bot (docs review, no code to read, a review, 2026-10-31): Use with caution. Per Anthropic's docs, mods are not sandboxed: they run with your permissions, can read env vars and settings (API keys), see every prompt and tool call, rewrite prompts, message other sessions, auto-approve tool calls and make network requests. Review any mod Claude writes before keeping it.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code (local only): built in (v2.1.287 or later); nothing to install. Check `claude --version` and see loaded mods with `/plugin`.
Claude Code (local only): kill switch `"disableAllHooks": true` or start with `--safe-mode`; review a mod with `claude plugin validate` on its folder (Claude-written mods live in `~/.claude/dev-mods/`).
Hermes: no equivalent (Claude Code only).
