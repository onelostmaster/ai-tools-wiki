# promptfoo

- **Type:** CLI
- **Category:** security, developer tools
- **Official URL:** https://www.promptfoo.dev
- **GitHub repo:** https://github.com/promptfoo/promptfoo @ 081b652 (MIT; latest commit on 2026-10-31; promptfoo is now part of OpenAI)
- **Price:** Community edition free (`promptfoo.dev/pricing`, checked 2026-10-31); Enterprise is quoted.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-03

## Safety reason

a review bot (vendor docs, 2026-10-31): safe. Official product of Promptfoo (now part of OpenAI), MIT. Collects basic usage telemetry by default (commands, assertion types; plus your email if logged in to promptfoo cloud); turn off with `PROMPTFOO_DISABLE_TELEMETRY=1`. Red-team runs send attack prompts to the models you point it at.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `npm install -g promptfoo` (or `brew install promptfoo` / `pip install promptfoo`); set `PROMPTFOO_DISABLE_TELEMETRY=1` first (`promptfoo.dev` docs).
