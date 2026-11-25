# agent-screenplay (gmpetrov)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/gmpetrov/agent-screenplay
- **GitHub repo:** https://github.com/gmpetrov/agent-screenplay @ b1a5da3 (v0.1.7, MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-04)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

a review bot read @b1a5da3: safe with these fixes. It is a CLI plus stdio MCP server (not just a skill) that films websites or desktop apps with Playwright and ffmpeg and edits them into an MP4. No package install scripts of its own (package.json scripts); no shell:true, eval or new Function in src. Verified 1: 'npx agent-screenplay init' registers the MCP server as unpinned 'npx -y agent-screenplay mcp' (init.ts:39) at Claude Code user scope (init.ts:90), and also edits ~/.codex/config.toml and ~/.cursor/mcp.json if those exist (init.ts:97-134) and copies SKILL.md into ~/.claude/skills and ~/.codex/skills (init.ts:146-156); it downloads Chromium through Playwright (init.ts:60-68). Run from a git checkout it registers the local build instead (init.ts:34-36). Fix: clone at b1a5da3, build it, run init from the checkout with --no-mcp, and add the MCP server yourself pointing at that build. Verified 2: the npm package is a separate artifact from the repo; unverified: that the npm 0.1.7 tarball matches this commit. Fix: build from the pinned clone instead of npx. Verified 3: 'login <url>' saves the site session (cookies) to .screenplay/auth.json in the project (README.md:101, cli.ts:125). Fix: add .screenplay/ to the project's .gitignore and delete auth.json when done. Verified 4: voice-over keys (CARTESIA_API_KEY, ELEVENLABS_API_KEY) are sent only to api.cartesia.ai and api.elevenlabs.io (cartesia.ts:6, elevenlabs.ts:4). Fix: none needed; or skip keys and use your own audio files (README.md:117). Verified 5: desktop-app recording drives the computer through agent-desktop, which is not a dependency and must be installed globally (desktop.ts:102-112), not reviewed here. Fix: use web recordings only until agent-desktop has its own review. Other: the style editor listens only on 127.0.0.1 with a token in the URL (editor/server.ts:105-108); the Windows 'recording' pill runs the bundled assets/indicator/windows.ps1 with -ExecutionPolicy Bypass for that one process (indicator.ts:22), SCREENPLAY_INDICATOR=0 turns it off (indicator.ts:28); the browser hides the automation flag and HeadlessChrome user agent so bot checks pass (browser.ts:16, 53). MIT.

## Safe install

Safe install (fixes applied):
Windows + Claude Code: install Node 20+ and Git yourself. Then: git clone https://github.com/gmpetrov/agent-screenplay ; cd agent-screenplay ; git checkout b1a5da340898bb9ba56dbf0b1fc496f6557549d8 ; npm ci ; npm run build ; node dist/cli.js init --no-mcp (downloads Chromium once and copies the guide skill to %USERPROFILE%\.claude\\skills\\screenplay; leaves Codex and Cursor configs alone). Add the MCP server yourself, pinned to this build: claude mcp add --scope user screenplay -- node <full path>\\agent-screenplay\\dist\\cli.js mcp. Web recordings only (do not install agent-desktop). In each project add .screenplay/ to .gitignore and delete .screenplay\\auth.json after a login recording. Voice-over: your own audio files, or a Cartesia/ElevenLabs key in the environment.
claude.ai, Hermes, Android: not supported (needs local Node, Chromium and an MCP client or shell).

## YOLO install

YOLO (your own risk): skips the pinned build and the manual MCP entry. Run npx agent-screenplay init (registers unpinned npx -y agent-screenplay mcp at user scope and edits Codex and Cursor configs if present), and npm install -g agent-desktop for desktop-app recordings.

## Install notes

Safe with fixes: CLI + MCP server that films a website (or desktop app) from a JSON scenario and edits it into a Screen Studio-style MP4 (smooth cursor, auto-zoom, callouts, voice-over). Build from the clone pinned at b1a5da3, run init --no-mcp, add the MCP server yourself pointing at the local build, web recordings only, keep .screenplay/auth.json out of git. Possible use: screen-demo segments for the faceless video channel.
