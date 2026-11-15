# i-have-adhd plugin

- **Type:** plugin
- **Category:** Notion and productivity
- **GitHub repo:** unknown
- **Price:** Free (MIT)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (a project tool scout, read before install, v0.4.1, 2026-10-30): safe. Markdown plus a local-only opt-in hook; MIT.

## Safe install

Safe install (fixes applied):
Claude Code (a project only): already listed in .claude/settings.json (PR #1); it loads in new threads only after tool-scout/setup-script-plugins.sh runs from the environment setup script (a project tool scout). Keep the reviewed v0.4.1 and leave its opt-in hook off unless you want it (local-only, Claude review 2026-10-30). Other projects and platforms: no install path, because no official repo or marketplace name is recorded; do not install a copy found by search. unverified: the source repo; contain it by using only a project marketplace entry Claude reviewed.

## YOLO install

Not written yet.

## Install notes

Claude Code (a project): listed in the project's `.claude/settings.json` (PR #1), but per a project tool scout it does not load in new threads until its marketplace is registered via `tool-scout/setup-script-plugins.sh` in the environment's setup script.
Claude Code (other projects): no confirmed command yet; no marketplace name or repo URL is recorded.
