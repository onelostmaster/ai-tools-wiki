# UX/UI Agent Skills (XIAS, plugin87)

- **Type:** plugin
- **Category:** design, building a site
- **Official URL:** https://github.com/plugin87/ux-ui-agent-skills
- **GitHub repo:** https://github.com/plugin87/ux-ui-agent-skills @ def84a7 (v3.0.0, 2026-10-27; MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @def84a7, a review, 2026-11-02): safe. Plugin adds 3 hooks that run local Node checks at session start, after every Write/Edit and at Stop (`hooks/hooks.json:3-35`, `hooks/posttooluse-fast-gates.mjs:76`); no network calls found in the hooks. Large repo (53 MB).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code (Windows): install as a plugin (README); needs Node for the hooks, which run on every edit. claude.ai and Android: no.
