# AE-MCP (ishu86 after-effects-mcp)

- **Type:** MCP
- **Category:** editing, generating videos
- **Official URL:** https://github.com/ishu86/after-effects-mcp
- **GitHub repo:** https://github.com/ishu86/after-effects-mcp @ 5223c17 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26); needs a paid Adobe After Effects plan (price not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-27

## Safety reason

a review bot read @5223c17: safe with these fixes. A local stdio MCP server that turns 70+ tool calls into ExtendScript and passes it to an After Effects panel through JSON files in Documents\\ae-mcp-commands (file-communicator.ts:44-45, host.jsx:24); it makes no web calls and needs no API keys. Tool inputs are validated before a script is generated (stdio-server.ts:2013-2019). Verified 1: the panel runs whatever script is inside each command file in that folder (host.jsx:108 and :128, eval), polling while the panel is open (main.js:102-103), so any program running as you that writes a file there runs ExtendScript in After Effects. Fix: open Window > Extensions > AE-MCP only while you use it and close it afterwards. Verified 2: the Windows installer sets PlayerDebugMode=1 for CSXS 10, 11 and 12 (install-cep.bat, the three reg add lines), which lets every unsigned CEP extension load in Adobe apps, not just this one. Fix: when you stop using AE-MCP, set it back with reg add HKCU\\SOFTWARE\\Adobe\\CSXS.12 /v PlayerDebugMode /t REG_SZ /d 0 /f (same for CSXS.11 and .10). Verified 3: the tools can delete compositions and layers, save, collect files and reduce the open project (stdio-server.ts:209, :1810, :1824). Fix: work on a copy of the project file. Verified 4: README installs with npm install, which can move the ^ dependency ranges in package.json, while the repo ships package-lock.json. Fix: npm ci at the pinned commit. Note: the panel runs with --enable-nodejs (manifest.xml:25) but main.js makes no Node calls. MIT (LICENSE).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, After Effects 2024+ and Node 18+): git clone https://github.com/ishu86/after-effects-mcp ; cd after-effects-mcp ; git checkout 5223c17a8e8c1273b25c6a9d306839259ad35143 ; npm ci ; npm run build ; scripts\\install-cep.bat . Then: claude mcp add ae-mcp -- node <your clone path>\\dist\\index.js . Work on a copy of your project, open the AE-MCP panel only while using it, and when you stop using AE-MCP set PlayerDebugMode back to 0 for CSXS.10, .11 and .12 (reg add HKCU\\SOFTWARE\\Adobe\\CSXS.12 /v PlayerDebugMode /t REG_SZ /d 0 /f).
claude.ai, Hermes, Android: not supported (local server that drives After Effects on the same Windows computer).

## YOLO install

YOLO (your own risk): skips the pinned commit and lockfile install, the project copy, closing the panel and resetting PlayerDebugMode. README: git clone https://github.com/ishu86/after-effects-mcp.git ; cd after-effects-mcp ; npm install ; npm run build ; scripts\\install-cep.bat , then add node dist/index.js as an MCP server.

## Install notes

Safe with fixes: install at pinned commit 5223c17 with npm ci; open the AE-MCP panel only while using it (it runs any script file dropped in Documents\\ae-mcp-commands); its installer turns on PlayerDebugMode for all unsigned Adobe extensions, so set it back to 0 when done; work on a copy of the project. No API keys, no web calls. Needs a paid After Effects licence. Fits the faceless video channel: titles, lower thirds, transitions and keyframes from Claude Code.
