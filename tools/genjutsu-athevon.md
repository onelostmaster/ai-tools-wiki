# genjutsu (AThevon)

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/AThevon/genjutsu
- **GitHub repo:** https://github.com/AThevon/genjutsu @ ac9ca74 (release v4.1.3, 2026-11-01; MIT, `LICENSE:1`)
- **Price:** Free, MIT (github.com, checked 2026-11-02); claude.ai needs Pro, Max, Team or Enterprise for code execution (genjutsu.athevon.dev/docs/install, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @ac9ca74, a review, 2026-11-02): safe. No hooks, no auto-run commands and no network calls in skill scripts. Bundles a copy of ui-ux-pro-max (credited in `skills/_jutsu/ui-ux-pro-max/UPSTREAM.md`). bunshin spawns many subagents (heavy on usage) and states its cost first.

## Safe install

Safe install (fixes applied):
Windows Claude Code: `git clone https://github.com/AThevon/genjutsu` and `git checkout ac9ca74` (the reviewed v4.1.3; v4.2.0 from 2026-11-13 is 4 commits newer and not reviewed), then in Claude Code `/plugin marketplace add <path to that folder>` and `/plugin install genjutsu@genjutsu` (README.md:47-50 gives the same two commands with the GitHub name; marketplace name from .claude-plugin/marketplace.json). Skip the README's first route `npx skills add https://genjutsu.athevon.dev -g` (README.md:40): it installs globally from the website, not from the reviewed commit. bunshin spawns many subagents and states its cost first; read that cost before you say yes. claude.ai (then also the Android Claude app): upload genjutsu.zip from the official GitHub release v4.1.3 as a skill; needs a plan with code execution; unverified: that the zip matches commit ac9ca74, contained by claude.ai's code sandbox. Not a Hermes tool.

## YOLO install

YOLO (your own risk): skips the commit pin (gets v4.2.0, unreviewed) and the global install from the website.
npx skills add https://genjutsu.athevon.dev -g

## Install notes

Safe, but ask the user before installing.
claude.ai: upload genjutsu.zip as a skill on the web (needs a plan with code execution); then it also works in the Android Claude app. Claude Code (Windows): install as a plugin (README). Watch usage with bunshin.
