# UX/UI Agent Skills (XIAS, plugin87)

- **Type:** plugin
- **Category:** design, building a site
- **Official URL:** https://github.com/plugin87/ux-ui-agent-skills
- **GitHub repo:** https://github.com/plugin87/ux-ui-agent-skills @ def84a7 (v3.0.0, 2026-10-27; MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @def84a7, a review, 2026-11-02): safe. Plugin adds 3 hooks that run local Node checks at session start, after every Write/Edit and at Stop (`hooks/hooks.json:3-35`, `hooks/posttooluse-fast-gates.mjs:76`); no network calls found in the hooks. Large repo (53 MB).

## Safe install

Safe install (fixes applied):
Windows Claude Code: `git clone https://github.com/plugin87/ux-ui-agent-skills` and `git checkout def84a7` (the reviewed v3.0.0; v3.1.0 from 2026-11-10 is not reviewed), then in Claude Code `/plugin marketplace add <path to that folder>` and `/plugin install ux-ui-agent-skills@ux-ui-agent-skills` (README.md:224-225 gives the same two commands with the GitHub name). It adds 3 hooks that run local Node checks at session start, after every Write/Edit and at Stop (hooks/hooks.json:3-35), with no network calls; install Node.js first. The repo is 53 MB. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the commit pin (gets v3.1.0, unreviewed).
/plugin marketplace add plugin87/ux-ui-agent-skills then /plugin install ux-ui-agent-skills@ux-ui-agent-skills

## Install notes

Safe, but ask the user before installing.
Claude Code (Windows): install as a plugin (README); needs Node for the hooks, which run on every edit. claude.ai and Android: no.
