# Astryx

- **Type:** library
- **Category:** design, frontend, developer tools, building a site
- **Official URL:** https://astryx.atmeta.com
- **GitHub repo:** https://github.com/meta/astryx @ 31bc5dc (0.7.17; MIT; official Meta repo; commit 2026-11-14 08:25 ET confirmed via GitHub API; earlier a review bot read @82036d5)
- **Price:** Free, MIT (LICENSE, official site and GitHub, checked 2026-11-14). Currently in beta.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @31bc5dc (0.7.17), 2026-11-14: safe with the Install notes fixes. No telemetry SDK; postinstall only prints a nudge. Verified risks, each fixed: the plugin skill tells agents to `npm i -g` (SKILL.md:19; fix: no plugin skill, project-local CLI); hosted MCP sends queries off-machine (fix: don't add it); daily registry check on a global install (fix: `NO_UPDATE_NOTIFIER=1`); public gap reports need `--confirm-public` (never pass it). a review bot spot-checked SKILL.md:19, update-notice-env.mjs:38 and agent-doc-state.mjs:186-193 at 31bc5dc.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder, `npm install -D -E --ignore-scripts @astryxdesign/core@0.7.17 @astryxdesign/cli@0.7.17`, then `npx @astryxdesign/cli init`. Set `NO_UPDATE_NOTIFIER=1` and `DO_NOT_TRACK=1`. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json (it denies global npm installs and curl|sh). Do not install the Astryx plugin skill or run `astryx init --user`. Do not add the hosted MCP at astryx.atmeta.com/mcp; use the local CLI. Never pass `--confirm-public`. Never run the unscoped `npx astryx` (that name is a different package). Re-review before bumping the pin.

## YOLO install

YOLO (your own risk): skips the pinned version, --ignore-scripts, NO_UPDATE_NOTIFIER=1, the deny rule against global npm, and staying off the hosted MCP and `astryx init --user`.
`npm i -g @astryxdesign/cli` (README), or install the Astryx skill, which tells an agent to run that command when `astryx` is not found (SKILL.md:19).

## Install notes

Safe with these fixes, all of them. In the project folder: `npm install -D -E --ignore-scripts @astryxdesign/core@0.7.17 @astryxdesign/cli@0.7.17`, then `npx @astryxdesign/cli init`. Never `npx astryx`: the unscoped name is a different package (packages/cli/foundation/agent-docs/agent-doc-state.mjs:190-193). Set env var `NO_UPDATE_NOTIFIER=1` (foundation/release/update-notice-env.mjs:38). Don't install the Astryx plugin skill or run `astryx init --user`. Don't add the hosted MCP at `astryx.atmeta.com/mcp`; the local CLI has the same docs. Never pass `--confirm-public` to gap reports. Claude Code: add to settings.json `"permissions": {"deny": ["Bash(npm i -g:*)", "Bash(npm install -g:*)"]}`. Re-review before bumping the pin. Ask the user before installing.
