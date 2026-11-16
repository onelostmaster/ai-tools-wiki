# claude-instagram-autopilot (Ootto)

- **Type:** app
- **Category:** social posting, automation, generating videos
- **Official URL:** https://github.com/Ootto-AI/claude-instagram-autopilot
- **GitHub repo:** https://github.com/Ootto-AI/claude-instagram-autopilot @ 39cd0eb (MIT; read by a review bot and Claude, a review)
- **Price:** Free (MIT, github.com, checked 2026-10-31); needs your own Anthropic API key and a Composio account.
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @39cd0eb (2026-11-15): safe with fixes, Skip. The daily Action installs Claude Code unpinned (autopilot.yml:30), runs claude -p with --dangerously-skip-permissions next to your API and Composio secrets (lines 35-41) and pushes git add -A (line 47). Fix: pin the CLI, replace the skip flag with --allowedTools "Read,Write,Edit" (no Bash or web: no exfil route), commit only out/, keep the repo private.

## Safe install

Safe install (fixes applied):
Private fork at 39cd0eb; autopilot.yml line 30 npm i -g @anthropic-ai/claude-code@2.1.325; line 41 --allowedTools "Read,Write,Edit" instead of --dangerously-skip-permissions; line 47 git add out/; keep the publish step (line 52) commented.

## YOLO install

YOLO (your own risk): skips the pin, tool limit and narrow commit, so a skip-permissions agent runs with your keys in CI.
Fork and add the secrets as the README says.

## Install notes

Ask the user before installing. Private fork at 39cd0eb; autopilot.yml line 30 npm i -g @anthropic-ai/claude-code@2.1.325; line 41 --allowedTools "Read,Write,Edit" instead of --dangerously-skip-permissions; line 47 git add out/; keep the publish step (line 52) commented.
