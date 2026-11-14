# Ponytail

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://ponytail.dev
- **GitHub repo:** [https://github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- **Price:** Free (MIT, open-source); no paid plan listed on ponytail.dev or the README (checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read, v5.3.3 on main, pushed 2026-10-29): safe. Hooks on SessionStart, SubagentStart and UserPromptSubmit run local node scripts (git ls-files repo map, mode flag, cost band). No telemetry or install scripts.config/ponytail`. Network only if you set its optional webhook URL. Install only from DietrichGebert/ponytail (copycats exist).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add DietrichGebert/ponytail`, then `/plugin install ponytail@ponytail` (official README and `INSTALL.md`; the hooks also work on Windows, config in `%APPDATA%\ponytail`).
Hermes: `hermes plugins install DietrichGebert/ponytail --enable`; if it fails the schema check, `git clone https://github.com/DietrichGebert/ponytail.git ~/.hermes/plugins/ponytail`, then `hermes plugins enable ponytail` and restart (official `INSTALL.md`).
