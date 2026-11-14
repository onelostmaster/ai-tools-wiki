# Pake

- **Type:** CLI
- **Category:** developer tools, building a site
- **Official URL:** https://pake.run
- **GitHub repo:** https://github.com/tw93/Pake @ ed24c60 (GPL-3.0 with an output exception; latest commit on 2026-10-31)
- **Price:** Free (GPL-3.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-01

## Safety reason

Not code-reviewed; the post only names it. README: global npm CLI; the first build sets up a Rust/Tauri toolchain; the agent prompt tells Claude to read `llms.txt` from unpkg `@latest` (unpinned remote instructions). Apps you build are yours (GPL output exception).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `/plugin marketplace add tw93/Pake` then `/plugin install pake@pake` (README).
Claude Code (local only): `pnpm install -g pake-cli`, then `pake https://example.com --name Example` (README).
