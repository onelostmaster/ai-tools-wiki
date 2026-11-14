# Claude HUD

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/jarrodwatts/claude-hud
- **GitHub repo:** [https://github.com/jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 83e98cf, a review): Looks safe. Local status line; setup backs up `settings.json` and replaces your statusLine; its `--extra-cmd` shell exec only runs if you set `CLAUDE_HUD_ALLOW_EXTRA_CMD`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `/plugin marketplace add jarrodwatts/claude-hud`, then `/plugin install claude-hud`, `/reload-plugins` and `/claude-hud:setup` (setup backs up `settings.json` and replaces your statusLine).
