# Savvy Progress

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/JohnnyVizz/claude-kit
- **GitHub repo:** [https://github.com/JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) (plugins/savvy-progress, read at c871c15)
- **Price:** Free (MIT open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, c871c15, 2026-10-31): Looks safe. MIT. Like all mods, it runs with your permissions. A progress band and subagent panel with cost; no network or process calls (it only reads settings and the locale, adds two progress tools and passes Agent calls through). Don't add the sibling session-band mod: it has a macOS-only Swift notifier and runs processes.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `/plugin marketplace add johnnyvizz/claude-kit`, then `/plugin install savvy-progress@claude-kit` (README, per a review bot a review). Needs the mods API (Claude Code 2.1.287 or later).
