# Threejs-Awesome-Graphics-Agent-Skills (scottstts)

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills
- **GitHub repo:** https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills @ 53eb5a2 (0.13.0; MIT AND GPL-3.0-only per package.json; committed 2026-10-22 09:37 ET, still HEAD on 2026-11-09)
- **Price:** Free, MIT (github.com, checked 2026-11-04)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-09

## Safety reason

a review bot (code read @53eb5a2, 2026-11-09, no-intake review): Safe. 24 skills under skills/ are Markdown guides plus three.js example code that runs only in a browser page you open. Installer bin/threejs-awesome-graphics-agent-skills.mjs (407 lines) imports only Node built-ins (lines 3-16), makes no network calls, writes to the chosen skills folder under your home or project (lines 176-192), and deletes only skill folders named in its own manifest, validated against ^[a-z0-9-]\{1,63\}$ (lines 195-212, rm at 302-354); --force is needed to replace untracked folders. No postinstall script, hooks, telemetry or MCP config (package.json scripts are dev tests only). Dev-only extras: example-gallery/server.mjs listens on 127.0.0.1:4173 by default (line 418) with a ../ path check (line 134) and opens your browser (lines 400-411); scripts/check-three-freshness.mjs:25 reads the npm registry. Not reviewed: the prebuilt solver-kernels.wasm in threejs-spectral-ocean assets (browser sandboxed). .claude/CLAUDE.md is maintainer notes, no agent injection found; it claims no licensing concerns for its source projects, but GPL-3.0 notices ship with three examples, so keep those out of MIT code.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code on Windows: the simplest route is to copy only the skill folders you want from skills/ into %USERPROFILE%\.claude\\skills\\ (a project uses 7 Markdown guide skills pinned at 53eb5a2). The repo's Node installer (npx threejs-awesome-graphics-agent-skills install) also works: it uses only Node built-ins, makes no network calls, and only replaces skill folders it recorded in its own manifest unless you pass --force. Do not copy code from the GPL-3.0 example folders (they ship their own GPL-3.0.txt and THIRD_PARTY_LICENSES.md) into MIT projects. The .claude/CLAUDE.md file is the author's maintainer notes and only applies if you open the repo itself in Claude Code.
