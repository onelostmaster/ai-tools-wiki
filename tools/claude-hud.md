# Claude HUD

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/jarrodwatts/claude-hud
- **GitHub repo:** [https://github.com/jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, 83e98cf, a review): Looks safe. Local status line; setup backs up `settings.json` and replaces your statusLine; its `--extra-cmd` shell exec only runs if you set `CLAUDE_HUD_ALLOW_EXTRA_CMD`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, local terminal): /plugin marketplace add jarrodwatts/claude-hud, /plugin install claude-hud, /reload-plugins, then /claude-hud:setup. Setup will replace your statusLine in settings.json and keeps a backup (that is how it works). Leave CLAUDE_HUD_ALLOW_EXTRA_CMD unset so its --extra-cmd shell exec stays off .

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `/plugin marketplace add jarrodwatts/claude-hud`, then `/plugin install claude-hud`, `/reload-plugins` and `/claude-hud:setup` (setup backs up `settings.json` and replaces your statusLine).
