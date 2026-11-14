# oh-my-claudecode (OMC)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://oh-my-claudecode.dev
- **GitHub repo:** https://github.com/Yeachan-Heo/oh-my-claudecode @ 98e2c16 (MIT; latest commit on 2026-10-31)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); needs a Claude Pro/Max plan or API key.
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-01

## Safety reason

Not code-reviewed; the post only names it. README: large plugin plus an npm CLI published under another name (`oh-my-claude-sisyphus`, installed `@latest`); runs autonomous loops; can call Gemini CLI, Codex CLI and the Jev API (needs their keys or plans, about $60/month for all three per README); needs tmux (psmux on Windows).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` then `/plugin install oh-my-claudecode` (README).
Windows: `winget install psmux` for team mode (README).
