# Code Simplifier (Anthropic plugin)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/anthropics/claude-plugins-official
- **GitHub repo:** https://github.com/anthropics/claude-plugins-official (folder plugins/code-simplifier) @ a7ba5b9 (Apache-2.0; pushed 2026-10-30)
- **Price:** Free plugin (Apache-2.0); uses your Claude plan or API tokens
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read @a7ba5b9, a review, 2026-11-02): safe. One agent prompt only (`agents/code-simplifier.md`, model opus at `:4`); no scripts or hooks. It edits your code, so check the diff.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: install from Anthropic's official plugin directory (claude-plugins-official); review its diffs before committing.
Windows: works in Claude Code on Windows. Android: no.
