# jp-web-design-guardrails

- **Type:** skill
- **Category:** a project, building a site
- **Official URL:** https://github.com/mrslbt/jp-web-design-guardrails
- **GitHub repo:** https://github.com/mrslbt/jp-web-design-guardrails @ 1ac0c1a (MIT; HEAD on 2026-11-13, last commit 2026-04-01)
- **Price:** Free (MIT LICENSE, checked at commit 1ac0c1a on 2026-11-13)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @1ac0c1a, 2026-11-13, no-intake review): Safe. Markdown only: one skill (skills/jp-design/SKILL.md, 280 lines) and three reference files (typography, ui-patterns, code-snippets; about 1,620 lines), plus a 22-line plugin.json with name and keywords only. No hooks, MCP server, commands, scripts or allowed-tools. The only network references are Google Fonts link tags it suggests for pages you build (SKILL.md lines 131-138) and an optional pyftsubset example for self-hosted fonts (typography.md lines 456-461). JavaScript in the references is small formatting and regex helpers for dates, numbers and yen, run only in pages you build. No instructions to agents beyond design rules. Replaces a review bot's earlier caution, which was only because no repo was known.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy skills/jp-design from https://github.com/mrslbt/jp-web-design-guardrails at reviewed commit 1ac0c1a into %USERPROFILE%\.claude\\skills\\jp-design, then start a new session (/jp-design). claude.ai: zip that jp-design folder (SKILL.md plus references/) and upload it under Settings, Capabilities, Skills. Markdown only; no keys, nothing runs.

## YOLO install

YOLO (your own risk): skips the commit pin.
The README one-line plugin command (latest commit, and the repo has no marketplace file).

## Install notes

Code-reviewed by a review bot @1ac0c1a (safe). Claude Code on Windows: copy the folder skills/jp-design from https://github.com/mrslbt/jp-web-design-guardrails into %USERPROFILE%\.claude\\skills\\jp-design, then start a new session (it loads as /jp-design). The README's one-line plugin command (README Install) is the author's; the repo has a .claude-plugin/plugin.json but no marketplace file, so the folder copy is the dependable route. claude.ai: zip the jp-design folder (SKILL.md plus references/) and upload it under Settings, Capabilities, Skills. Nothing to run; no keys. Install is unpinned, so later commits arrive without a review.
