# hermes inbox (labs plugin)

- **Type:** plugin
- **Category:** Hermes add-ons, Notion and productivity
- **Official URL:** https://github.com/NousResearch/hermes-labs-plugins/tree/main/inbox
- **GitHub repo:** [https://github.com/NousResearch/hermes-labs-plugins](https://github.com/NousResearch/hermes-labs-plugins)
- **Price:** Free
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, pin 62dbc16, a project a review): Looks safe. About 620 lines; no network calls, no shell/eval, no model tools or hooks; only reads local Hermes stores (SQLite opened read-only) and `HERMES_KANBAN_*` env vars. Nous Research labs plugin, unsupported community tier.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install inbox` (README:35)
