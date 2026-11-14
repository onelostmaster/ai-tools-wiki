# mcptoon

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://github.com/activeing123/mcptoon
- **GitHub repo:** https://github.com/activeing123/mcptoon @ c94aee8 (Apache-2.0; created 2026-07-27; latest commit on 2026-10-31)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-01

## Safety reason

Not code-reviewed; the reel only names it. README: unpinned `pip install mcptoon`; `quickstart` writes the config of every agent it detects, moves your existing MCP servers behind its gateway and installs its own `/mcptoon` skill in each agent (undo: `mcptoon restore`); `install --search` installs servers from public registries (17,000+, not vetted). Claims no telemetry.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `pip install mcptoon && mcptoon quickstart` (README; prefer `pipx` or a venv). It changes every detected agent's MCP config; `mcptoon uninstall --dry` previews removal and `mcptoon restore` puts your servers back.
