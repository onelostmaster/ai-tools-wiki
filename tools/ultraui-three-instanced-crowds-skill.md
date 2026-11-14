# UltraUI three-instanced-crowds skill

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://github.com/AvnehSBhatia/UltraUI
- **GitHub repo:** https://github.com/AvnehSBhatia/UltraUI @ 592ae7f (skills/three/three-instanced-crowds; MIT; HEAD on 2026-11-13, last commit 2026-08-30)
- **Price:** Free (MIT LICENSE, checked at commit 592ae7f on 2026-11-13)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-13

## Safety reason

a review bot (code read @592ae7f, 2026-11-13, no-intake review): Safe. Markdown only: SKILL.md (690 lines; frontmatter lines 1-5 has name, description, category, pairs_with, no allowed-tools), reference.md (103), EVAL.md (127) and SOURCES.md (25). Code samples are Three.js InstancedMesh code for pages you build (import three at SKILL.md lines 74 and 465; pins three 0.169.0, line 31); no fetch, network calls, keys, hooks, MCP or scripts. The whole repo has no scripts or package files (only Markdown, LICENSE and .txt docs dumps under prompts/). Only install route that runs code is the README/CLAUDE.md npx skills add command (CLAUDE.md line 15), not reviewed. Replaces the earlier unreviewed status.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @592ae7f (safe). Claude Code on Windows: copy the folder skills/three/three-instanced-crowds from https://github.com/AvnehSBhatia/UltraUI into %USERPROFILE%\.claude\\skills\\three-instanced-crowds (flat, one level), then start a new session. The README's npx skills add command is a third-party installer that downloads and runs code; it was not reviewed, so the folder copy is the dependable route. Do not install all 147 skills (the README itself warns each one adds to every prompt). claude.ai: zip the three-instanced-crowds folder (SKILL.md, reference.md, EVAL.md) and upload it under Settings, Capabilities, Skills. Nothing to run; no keys. Unpinned copy: later commits arrive without a review.
