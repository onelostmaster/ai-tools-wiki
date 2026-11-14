# genjutsu (AThevon)

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/AThevon/genjutsu
- **GitHub repo:** https://github.com/AThevon/genjutsu @ ac9ca74 (release v4.1.3, 2026-11-01; MIT, `LICENSE:1`)
- **Price:** Free, MIT (github.com, checked 2026-11-02); claude.ai needs Pro, Max, Team or Enterprise for code execution (genjutsu.athevon.dev/docs/install, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @ac9ca74, a review, 2026-11-02): safe. No hooks, no auto-run commands and no network calls in skill scripts. Bundles a copy of ui-ux-pro-max (credited in `skills/_jutsu/ui-ux-pro-max/UPSTREAM.md`). bunshin spawns many subagents (heavy on usage) and states its cost first.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
claude.ai: upload genjutsu.zip as a skill on the web (needs a plan with code execution); then it also works in the Android Claude app. Claude Code (Windows): install as a plugin (README). Watch usage with bunshin.
