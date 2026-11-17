# Code Simplifier (Anthropic plugin)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/anthropics/claude-plugins-official
- **GitHub repo:** https://github.com/anthropics/claude-plugins-official (folder plugins/code-simplifier) @ a7ba5b9 (Apache-2.0; pushed 2026-10-30)
- **Price:** Free plugin (Apache-2.0); uses your Claude plan or API tokens
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read @a7ba5b9, a review, 2026-11-02): safe. One agent prompt only (`agents/code-simplifier.md`, model opus at `:4`); no scripts or hooks. It edits your code, so check the diff.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): /plugin install code-simplifier@claude-plugins-official (Anthropic official directory). It only edits code through one agent prompt (agents/code-simplifier.md); fix: run it on a git branch and read the diff before you commit. Uses Opus (agents/code-simplifier.md:4), so it spends your plan or API tokens. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the branch and diff check.
/plugin install code-simplifier@claude-plugins-official, run it on your working tree.

## Install notes

Safe, but ask the user before installing.
Claude Code: install from Anthropic's official plugin directory (claude-plugins-official); review its diffs before committing.
Windows: works in Claude Code on Windows. Android: no.
