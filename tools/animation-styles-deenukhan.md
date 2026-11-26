# animation-styles (deenukhan)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/deenukhan/animation-styles
- **GitHub repo:** https://github.com/deenukhan/animation-styles @ 7f7afbd (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-12)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot read @7f7afbd (commit 2026-11-10, still the latest on 2026-11-25; read: package.json, package-lock.json (count only), remotion.config.ts, scripts/new-project.mjs, scripts/render.mjs, SKILL.md, SETUP.md and a grep of src/ and scripts/ for child_process, fetch, URLs, env and eval; nothing run): safe with these fixes. A Claude Code skill that is a Remotion project: 39 styles as React/TypeScript code, rendered locally to MP4. No hooks, MCP server, keys, network calls in its own code, or eval; all dependencies are exact versions (Remotion 4.0.534, React 19.1.0; package.json) with a lockfile. Verified 1: Claude runs npm install itself when node_modules is missing (SKILL.md:15, 21), and the first render downloads a browser engine (~100 MB) and fonts (SETUP.md:34). Fix: run npm install yourself once in the pinned clone (npm ci uses the lockfile), with network on for that first render only. Verified 2: SETUP.md:18-23 tells Claude to clone --depth 1 from main and to git pull to update, so the skill follows main. Fix: clone and check out commit 7f7afbd, and don't pull. Verified 3: on Windows, render.mjs runs remotion through the shell (render.mjs:52) and passes the --still value straight into the command line (render.mjs:66-69). Fix: give --still a plain frame number only. Other: films are built in a separate animation-films folder, not in the skill (SKILL.md:21, 83; new-project.mjs:18-19). Remotion's own licence terms apply: see the Remotion (framework, v4) row. MIT.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, PowerShell): git clone https://github.com/deenukhan/animation-styles "$env:USERPROFILE\.claude\\skills\\animation-styles" ; cd "$env:USERPROFILE\.claude\\skills\\animation-styles" ; git checkout 7f7afbd4c5a216135e51be354cb245dcfabedb3a ; npm ci (Node 18+; exact versions from the lockfile) ; npm run list (39 styles). Do the first render yourself with network on (it downloads a ~100 MB browser engine and fonts). Don't git pull. Use --still with a plain frame number only.
claude.ai, Hermes, Android: not supported (needs local Node and Remotion).

## YOLO install

YOLO (your own risk): skips the pinned commit and npm ci. SETUP.md\:7-16\: ask Claude to 'Install this skill for me: https://github.com/deenukhan/animation-styles' and let it clone main, npm install and git pull later.

## Install notes

Safe with fixes: Claude Code skill with 39 animation styles drawn in code with Remotion (whiteboard, ukiyo-e, pixel art, claymation, silent film...), each retelling the same 5-second story; Claude retells your idea in any style and renders an MP4 locally, no image or video AI. Pin 7f7afbd, npm ci yourself, no git pull, plain numbers for --still. Reference for the faceless video channel idea; Decision Skip kept.
