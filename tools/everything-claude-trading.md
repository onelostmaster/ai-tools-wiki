# everything-claude-trading

- **Type:** plugin
- **Category:** finance, research
- **Official URL:** https://github.com/brainbytes-dev/everything-claude-trading
- **GitHub repo:** https://github.com/brainbytes-dev/everything-claude-trading @ 9a8fcfc (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @9a8fcfc) and Claude (@9a8fcfc), 2026-11-01: Looks safe. Markdown plus 4 small local Node hooks (`hooks/hooks.json`; `scripts/hooks/*.js` only read stdin and print warnings; no network, exec or file writes). Skip `mcp-configs/mcp-servers.json`: unpinned `npx -y`, two package names not on npm (squattable), one unofficial server.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: copy the skill folders you want (each `skills/<category>/<skill>` has a `SKILL.md`; `<category>` and `<skill>` are folder names in the repo) into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) and start a new session. The README's `claude install-skill` command and the plugin install are unconfirmed; skip the MCP config.
Hermes: unconfirmed: copy the same skill folders into `~/.hermes/skills/` and start a new session.
