# claude-instagram-autopilot (Ootto)

- **Type:** app
- **Category:** social posting, automation, generating videos
- **Official URL:** https://github.com/Ootto-AI/claude-instagram-autopilot
- **GitHub repo:** https://github.com/Ootto-AI/claude-instagram-autopilot @ 39cd0eb (MIT; read by a review bot and Claude, a review)
- **Price:** Free (MIT, github.com, checked 2026-10-31); needs your own Anthropic API key and a Composio account.
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 39cd0eb, a review, 2026-10-31): Use with caution; Claude (read 39cd0eb) confirmed. The CI job runs `claude -p ... --dangerously-skip-permissions` with your `ANTHROPIC_API_KEY` and Composio secrets, installs Claude Code unpinned (`npm i -g @anthropic-ai/claude-code`), and does `git add -A` + push. Its README says to install Agent Reach (flagged before).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: no steps given (a review bot withholds steps for caution items).
