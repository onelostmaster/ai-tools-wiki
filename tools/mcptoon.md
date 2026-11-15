# mcptoon

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://github.com/activeing123/mcptoon
- **GitHub repo:** https://github.com/activeing123/mcptoon @ 3af4967 (Apache-2.0; HEAD on 2026-11-14, latest commit on 2026-11-12 ET; version 0.8.40)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @3af4967, 2026-11-14, no-intake review): Caution. About 40,000 lines of pure-Python CLI, zero runtime dependencies (pyproject.toml line 32); no telemetry or analytics code, no obfuscated or encoded payloads, no eval of downloaded code. Network: PyPI version check (upgrade.py line 60), which a footer spawns in the background at most once a day as a check only (upgrade.py lines 239-266, cli.py line 4367); the upgrade itself asks before installing (lines 345-359); registry searches (installer.py lines 36-37, skills.py line 1379); your own MCP servers. serve binds 127.0.0.1 for a bare :port (serve.py lines 1986-1991); opt-in --install-autostart creates a Windows logon task (lines 1720-1745). OAuth tokens saved owner-only (oauth.py lines 115-131). Why caution: quickstart/sync takes over every detected agent's MCP config and writes into ~/.claude/CLAUDE.md (sync.py lines 207-213), with backups and mcptoon restore; exec is documented as 'not a security sandbox' (exec_sandbox.py line 31); its bundled SKILL.md tells agents to pip install mcptoon themselves when the CLI is missing and then tell the user (SKILL.md lines 18-31). Earlier note corrected: install --search only searches and installs nothing (installer.py line 12). Replaces the earlier not-reviewed status.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @3af4967 (caution; see Safety reason). Claude Code on Windows: install in a venv or with pipx (pipx install mcptoon==0.8.40 pins the reviewed version), not a bare pip install into system Python. Prefer the narrow path: run mcptoon commands yourself rather than quickstart or sync --takeover, which rewrite every detected agent's MCP config, add a pointer to ~/.claude/CLAUDE.md and copy its /mcptoon skill into each agent. If you do run quickstart, preview first with mcptoon uninstall --dry and keep mcptoon restore in mind to put your servers back. Do not let an agent run mcptoon exec on untrusted code: its 'sandbox' has your full file, network and credential access. Installing servers from the public registries (Smithery, MCP registry) brings in unvetted code; vet each one first. mcptoon serve binds 127.0.0.1 by default; --install-autostart adds a Windows logon Scheduled Task (remove with serve --uninstall-autostart). claude.ai and Android: not a fit (needs a local computer).
