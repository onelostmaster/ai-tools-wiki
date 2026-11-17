# everything-claude-trading

- **Type:** plugin
- **Category:** finance, research
- **Official URL:** https://github.com/brainbytes-dev/everything-claude-trading
- **GitHub repo:** https://github.com/brainbytes-dev/everything-claude-trading @ 9a8fcfc (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @9a8fcfc) and Claude (@9a8fcfc), 2026-11-01: Looks safe. Markdown plus 4 small local Node hooks (`hooks/hooks.json`; `scripts/hooks/*.js` only read stdin and print warnings; no network, exec or file writes). Skip `mcp-configs/mcp-servers.json`: unpinned `npx -y`, two package names not on npm (squattable), one unofficial server.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy only the skill folders you want (skills/<category>/<skill>, each with a SKILL.md) from reviewed commit 9a8fcfc into %USERPROFILE%\.claude\\skills\\ and start a new session. Copying skills only also leaves out the 4 warn-only Node hooks (they read stdin and print warnings, hooks/hooks.json). Knowledge only: it places no trades.
Hermes: copy the same folders into ~/.hermes/skills/<category>/.

## YOLO install

YOLO (your own risk): skips the commit pin and the skills-only copy.
Install the whole repo at HEAD with the README's claude install-skill or plugin route (not confirmed to work), hooks included. Even here, do not add mcp-configs/mcp-servers.json: the two unregistered npm names are a takeover risk, not a setting.

## Install notes

Claude Code: copy the skill folders you want (each `skills/<category>/<skill>` has a `SKILL.md`; `<category>` and `<skill>` are folder names in the repo) into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) and start a new session. The README's `claude install-skill` command and the plugin install are unconfirmed; skip the MCP config.
Hermes: unconfirmed: copy the same skill folders into `~/.hermes/skills/` and start a new session.
