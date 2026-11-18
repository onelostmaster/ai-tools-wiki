# Claude Skins

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/hellosverre/claude-skins
- **GitHub repo:** [https://github.com/hellosverre/claude-skins](https://github.com/hellosverre/claude-skins) (read at 985ad63)
- **Price:** Free (MIT open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 985ad63, 2026-10-31): Looks safe. MIT. Like all mods, it runs with your permissions. Re-themes tool rows. Once a day it fetches `plugin.json` from GitHub main and only shows a toast (no auto-install); a GitHub-star nag after 3 days; on Windows it reads the dark-mode setting with `reg query`; it wraps every tool call, for display only. Skip the README's mod-store (about 2,700 unvetted mods).

## Safe install

Safe install (fixes applied):
Claude Code (local only), Windows: git clone https://github.com/hellosverre/claude-skins.git, git checkout 985ad63 (reviewed), /plugin marketplace add <path to that folder>, then /plugin install skins@hellosverre-mods with auto-update off. Once a day it fetches plugin.json from GitHub main and only shows an update toast; ignore the toast and stay on the pinned commit. Do not use the README's mod-store (about 2,700 unvetted mods).
claude.ai: not available.

## YOLO install

YOLO (your own risk): skips the commit pin and following the update toast.
/plugin marketplace add hellosverre/claude-skins then /plugin install skins@hellosverre-mods (README) at HEAD. Still skip the mod-store.

## Install notes

Claude Code (local only): `/plugin marketplace add hellosverre/claude-skins`, then `/plugin install skins@hellosverre-mods` (README, per a review bot a review; hand-tested on Windows per its README). Don't use the README's mod-store.
