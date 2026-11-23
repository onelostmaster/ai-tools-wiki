# oh-my-claudecode (OMC)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://oh-my-claudecode.dev
- **GitHub repo:** https://github.com/Yeachan-Heo/oh-my-claudecode @ dec7e41 (MIT; v5.8.6; commit 2026-11-11)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); needs a Claude Pro/Max plan or API key.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

a review bot read @dec7e41: safe with these fixes. Verified 1: the plugin registers about 30 local node hooks on every prompt, tool call, stop and session start/end (hooks/hooks.json); they run only local scripts and fail open on errors (scripts/permission-handler.mjs:15-17). Fix: none needed; install only into a test project first so you see what they inject. Verified 2: omc-setup --global overwrites ~/.claude/CLAUDE.md by default, keeping a backup (skills/omc-setup/SKILL.md:58-65). Fix: run /oh-my-claudecode:omc-setup --local inside the project, or pick preserve mode, which writes CLAUDE-omc.md instead. Verified 3: README installs the CLI globally with npm i -g oh-my-claude-sisyphus@latest (README.md:73), and that package runs a postinstall build script (package.json:92). Fix: skip the CLI (the plugin works without it); if you need omc team, pin the version: npm i -g oh-my-claude-sisyphus@5.8.6 --ignore-scripts. Verified 4: the Jev compaction module sends excerpts of your conversation and tool results (user text up to 4000 characters) to api.typesafe.ai (hooks/jev-compaction.mjs:105,123,1182), but only when TYPESAFE_API_KEY is set and points are opted in (src/hooks/jev/config.ts:4-7,146,225). Fix: never set TYPESAFE_API_KEY or OMC_JEV_* variables. Verified 5: the PermissionRequest hook auto-approves only git status, gh issue/pr view/list/status, ls and plain ripgrep searches without shell metacharacters, and respects your own ask rules (src/hooks/permission-handler/index.ts:33-44,561-572). Fix: none needed; add Bash(ls:*) etc. to permissions.ask if you want to approve those too. Verified 6: the persistent-mode Stop hook blocks Claude from stopping while an autopilot/ralph mode is active, up to a hard iteration cap (scripts/persistent-mode.mjs:95,314,337). Fix: use /autopilot and other loop modes only in a session you are watching, never with skip-permissions. Verified 7: on session start it asks registry.npmjs.org for the latest oh-my-claude-sisyphus and Claude Code versions (version number only, 2 s timeout, scripts/session-start.mjs:1318-1344); in plugin mode it never updates itself (scripts/session-start.mjs:1648-1654). Fix: none needed. Verified 8: the marketplace URL follows the moving main branch. Fix: clone and add the pinned commit as a local marketplace. Unverified: how the marketplace copy gets the built dist/ folder the hooks import (dist/ is git-ignored, .gitignore:33). Containment: first install into a throwaway test project and check that /oh-my-claudecode commands work before using it on real repos. No telemetry found besides the opt-in Jev calls. Gemini, Codex and Grok team panes need their own CLIs and plans (README.md:221).

## Safe install

Safe install (fixes applied):
Claude Code on Windows (PowerShell, Git for Windows installed for the setup bash script): git clone https://github.com/Yeachan-Heo/oh-my-claudecode C:\\tools\\omc ; cd C:\\tools\\omc ; git checkout dec7e41 . Then in Claude Code, one line at a time: /plugin marketplace add C:\\tools\\omc then /plugin install oh-my-claudecode . In your project run /oh-my-claudecode:omc-setup --local (never --global overwrite). Skip the npm CLI; if you need omc team: npm i -g oh-my-claude-sisyphus@5.8.6 --ignore-scripts and winget install psmux. Never set TYPESAFE_API_KEY; run /autopilot only in a session you watch; try it in a test project first.
claude.ai, Hermes, Android: not supported (Claude Code plugin only).

## YOLO install

YOLO (your own risk): skips the pin, the local setup and the CLI pin. /plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode , /plugin install oh-my-claudecode , /omc-setup (default global overwrites ~/.claude/CLAUDE.md), npm i -g oh-my-claude-sisyphus@latest (README.md:61-90).

## Install notes

Safe with fixes: multi-agent orchestration plugin for Claude Code (teams, autopilot, ~30 local hooks), no telemetry. Pin commit dec7e41 as a local marketplace, set it up with omc-setup --local so your global CLAUDE.md stays, skip the global @latest CLI (or pin 5.8.6 with --ignore-scripts), never set TYPESAFE_API_KEY (that turns on sending conversation excerpts to api.typesafe.ai), and run autopilot loops only in a session you watch. Try it in a test project first.
