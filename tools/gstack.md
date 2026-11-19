# gstack

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/garrytan/gstack
- **GitHub repo:** [https://github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @3ecd716 v1.100.0.0 (2026-11-18): safe with fixes. Telemetry is off until you opt in; the update check and outside Codex/Claude reviews (send code) are on by default and turn off with gstack-config (README.md:290). Install tells you to bar Claude in Chrome in CLAUDE.md (README.md:38,313). /browse can use your real cookies (BROWSER.md:8,17). Fix: both switches off, skip that CLAUDE.md line, no cookie import.

## Safe install

Safe install (fixes applied):
Clone at 3ecd716 into ~/.claude/skills/gstack; ./setup --no-plan-tune-hooks --no-timeline-stop-hook; gstack-config set update_check false; gstack-config set codex_reviews disabled; decline telemetry; do not add the CLAUDE.md browser line; no cookie import.

## YOLO install

YOLO (your own risk): skips both switches and the CLAUDE.md rule.
Run the README one-liner as written.

## Install notes

Ask the user before installing. Clone at 3ecd716 into ~/.claude/skills/gstack; ./setup --no-plan-tune-hooks --no-timeline-stop-hook; gstack-config set update_check false; gstack-config set codex_reviews disabled; decline telemetry; do not add the CLAUDE.md browser line; no cookie import.
