# AE-MCP (ishu86 after-effects-mcp)

- **Type:** MCP
- **Category:** editing, generating videos
- **Official URL:** https://github.com/ishu86/after-effects-mcp
- **GitHub repo:** https://github.com/ishu86/after-effects-mcp @ 5223c17 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26); needs a paid Adobe After Effects plan (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: needs After Effects 2024+ (paid Adobe app) on Windows or macOS; npm install, npm run build, then scripts\\install-cep.bat. Verified in scripts/install-cep.bat: it sets HKCU\\SOFTWARE\\Adobe\\CSXS.10/11/12 PlayerDebugMode=1, which lets After Effects load any unsigned CEP extension, and symlinks (or copies) the panel into %APPDATA%\\Adobe\\CEP\\extensions\\com.aemcp.panel. Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: clone at the pinned commit 5223c17, build in a sandbox, only install the CEP panel on a machine where you accept unsigned After Effects extensions (install-cep.bat turns that on; undo with the reg delete lines in Install notes), no API keys (it needs none). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows: npm install, npm run build, scripts\\install-cep.bat, then add the server to %APPDATA%\\Claude\\claude_desktop_config.json (README). Fix for the debug flag: after removing the panel, reg delete HKCU\\SOFTWARE\\Adobe\\CSXS.12 /v PlayerDebugMode /f (and CSXS.11, CSXS.10).
