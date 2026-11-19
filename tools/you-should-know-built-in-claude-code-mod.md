# You Should Know (built-in Claude Code mod)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub repo:** none (built into Claude Code)
- **Price:** Included with Claude Code; each check spends usage (several thousand tokens, per `code.claude.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-18

## Safety reason

Anthropic (built-in mod `cc-plugin-you-should-know`, off by default; source not public, not audited by a review bot, a review, 2026-10-31): safe. A side agent periodically reads the conversation, including tool results, with your model, which spends extra usage. Claude Code docs: the side agent has no tools, each check bills several thousand tokens, notes are stored locally, and it runs only in first-party sessions with telemetry on.

## Safe install

Safe install (fixes applied):
Claude Code (local only, v2.1.287 or later): nothing to install; it is built in and off by default. Enable it only for long runs with /plugin enable cc-plugin-you-should-know@builtin and turn it off afterwards with /plugin disable cc-plugin-you-should-know@builtin. While it is on, every check reads the conversation with your model and bills several thousand tokens (Claude Code docs); that cost will happen and the only way to avoid it is to keep it off.
claude.ai: not available.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): built in (v2.1.287 or later); nothing to install. Enable with `/plugin enable cc-plugin-you-should-know@builtin`; turn it off with `/plugin disable cc-plugin-you-should-know@builtin` (Claude Code docs).
