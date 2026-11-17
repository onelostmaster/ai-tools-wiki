# Code Review (Anthropic plugin)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/anthropics/claude-plugins-official
- **GitHub repo:** https://github.com/anthropics/claude-plugins-official (folder plugins/code-review) @ a7ba5b9 (Apache-2.0; pushed 2026-10-30)
- **Price:** Free plugin (Apache-2.0); uses your Claude plan or API tokens
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read @a7ba5b9, a review, 2026-11-02): safe. Allowed tools are only gh read commands plus gh pr comment and an inline-comment tool (`commands/code-review.md:2`); it posts to the PR only when you pass --comment (`code-review.md:66`). Launches Opus and Sonnet subagents (`code-review.md:56`), so it uses your Claude plan or API tokens. Needs gh signed in.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): /plugin install code-review@claude-plugins-official (Anthropic official directory); needs the GitHub CLI signed in (gh auth login). Run /code-review without --comment: it then posts nothing to the PR (commands/code-review.md:66) and only shows results in your terminal. Launches Opus and Sonnet subagents (code-review.md:56), so it spends your plan or API tokens. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips leaving --comment off.
/code-review --comment (posts its review on the PR).

## Install notes

Safe, but ask the user before installing.
Claude Code: install from Anthropic's official plugin directory (claude-plugins-official). Needs the GitHub CLI signed in.
Windows: works in Claude Code on Windows. Android: no.
