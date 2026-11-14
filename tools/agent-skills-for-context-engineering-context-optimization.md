# Agent Skills for Context Engineering (context-optimization)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
- **GitHub repo:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering @ 9ff0c99 (MIT; plugin 2.6.0; HEAD on 2026-11-12, last commit 2026-10-11)
- **Price:** Free (MIT LICENSE, checked at commit 9ff0c99 on 2026-11-12).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @9ff0c99, 2026-11-12, no-intake review): Safe. The plugin lists 18 skill folders and nothing else: no hooks, no MCP server, no commands or agents (.claude-plugin/marketplace.json, .plugin/plugin.json line 8). The skills are markdown with references; their example scripts use only the Python standard library plus numpy, make no network calls and read no keys. The two that delete files only remove their own demo folder (filesystem_context.py lines 410-415). sandbox_manager.py is a stub whose execute_command does nothing (lines 91-101); its clone and npm build lines (lines 183-195) and the os.system lines in hosted-agents/references/infrastructure-patterns.md (lines 43-52) are teaching examples, not run by the plugin. Caveat: the marketplace source is the repo root (strict false), so the researcher/ folder and its macOS launchd install script are copied too, but nothing calls them (README line 317). No telemetry. Not reviewed in depth: researcher/ and examples/.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @9ff0c99 (plugin context-engineering 2.6.0, safe). Claude Code on Windows: /plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering then /plugin install context-engineering@context-engineering-marketplace (README lines 103-117). It installs 18 text skills that load by topic; nothing runs at install. The example Python scripts in the skills only run if you ask (some need numpy). Do not run the researcher folder's launchd install.sh or research loop: it is a macOS scheduler for the author's own research system and is not part of the skills. Installs are unpinned, so later versions arrive without a review.
