# file-search skill (Netresearch)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/netresearch/file-search-skill
- **GitHub repo:** https://github.com/netresearch/file-search-skill @ bc99455 (MIT and CC-BY-SA-4.0; plugin 1.8.4; HEAD on 2026-11-12)
- **Price:** Free (LICENSE-MIT and LICENSE-CC-BY-SA-4.0 files, checked at commit bc99455 on 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @bc99455, 2026-11-12, no-intake review): Safe. The plugin is a markdown skill (skills/file-search/SKILL.md plus references) and one PreToolUse hook on Bash (hooks/hooks.json lines 4-15) that runs scripts/pre_bash_search_nudge.py with uv run --offline, a 3-second timeout and || true. The script uses only the Python standard library with no dependencies (lines 5-8, 26-32), opens no network connection and runs no command: it reads the hook payload, regex-matches find and grep, and prints a warn-only system message once per rule per session (lines 235-258); it always exits 0 (lines 262-266). Its only write is a small JSON file of seen-rule hashes in a 0700 folder under the temp directory, with symlink and owner checks (lines 126-159, 170-195). No keys, telemetry or MCP server. Maintainer-only files (.envrc sets git hooksPath; package.json prepare runs pre-commit install; scripts/verify-harness.sh) do not run for a plugin user. Not reviewed: the netresearch claude-code-marketplace repo and the GitHub workflows.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @bc99455 (plugin 1.8.4, safe). Claude Code on Windows: /plugin marketplace add netresearch/claude-code-marketplace then /plugin install file-search@netresearch-claude-code-marketplace (README lines 47-48). The search tools (ripgrep, ast-grep, fd, ripgrep-all, semgrep, tokei, scc) are not bundled; install the ones you want separately. The warn-only hook runs through uv (hooks/hooks.json line 10); without uv on PATH it does nothing and the skill still works. The npx skills route installs only SKILL.md, without the hook (README line 71). The marketplace repo itself was not reviewed, and installs are unpinned, so later versions arrive without a review.
