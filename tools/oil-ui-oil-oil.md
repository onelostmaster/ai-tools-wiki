# oil-ui (oil-oil)

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/oil-oil/oil-ui
- **GitHub repo:** https://github.com/oil-oil/oil-ui @ 4e8d25f (MIT; committed 2026-11-02)
- **Price:** Free, MIT; Pro $9.99 one-time (ui.oiloil.org/en/pro, checked 2026-11-02); image credits are a separate top-up with no listed price
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @4e8d25f, a review, 2026-11-02): caution. Auto-runs a version check against ui.oiloil.org when the skill loads, pre-approved in its own SKILL.md (`SKILL.md:4-8,35`); off with OIL_NO_UPDATE_CHECK=1, updates only when asked (`scripts/check_update.py:173`). Optional paid image credits (`scripts/oiloil-image.mjs:48`); suggests buying Pro.

## Safe install

Safe install (fixes applied):
Claude Code on Windows: copy the skill from https://github.com/oil-oil/oil-ui at commit 4e8d25f into %USERPROFILE%\.claude\\skills and set the user env var OIL_NO_UPDATE_CHECK=1 before starting Claude Code; otherwise it contacts ui.oiloil.org for a version check every time the skill loads, pre-approved in its own SKILL.md (SKILL.md:4-8,35; off switch scripts/check_update.py:173). Don't buy image credits or Pro unless you want them (scripts/oiloil-image.mjs:48). Needs Python, Node and Chrome or Edge. claude.ai and Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and OIL_NO_UPDATE_CHECK=1.
Claude Code on Windows: add the skill; it checks ui.oiloil.org for updates each time it loads.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code (Windows): add the skill, set OIL_NO_UPDATE_CHECK=1; needs Python, Node and Chrome or Edge. claude.ai and Android: no.
