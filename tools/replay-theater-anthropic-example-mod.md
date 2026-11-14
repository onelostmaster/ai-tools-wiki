# Replay Theater (Anthropic example mod)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub repo:** [https://github.com/anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground) (claude-code/mods/replay-theater, read at 569c528)
- **Price:** Free (Apache-2.0 open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 569c528, 2026-10-31) and Claude (re-read, a project, 2026-10-31): Looks safe. Apache-2.0 Anthropic example mod. Like all mods, it runs with your permissions. It only records Edit/Write calls and reads the old file, keeps everything in memory and never blocks edits.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only), Windows: `git clone https://github.com/anthropics/claude-code-playground.git`, `cd claude-code-playground\claude-code\mods`, `claude plugin marketplace add ./`, then `claude plugin install replay-theater@claude-code-playground-mods --scope user` (`mods/README.md`, per a review bot a review).
