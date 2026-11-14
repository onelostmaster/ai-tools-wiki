# Cap

- **Type:** app
- **Category:** editing
- **Official URL:** https://github.com/CapSoftware/Cap
- **GitHub repo:** [https://github.com/CapSoftware/Cap](https://github.com/CapSoftware/Cap)
- **Price:** Free (AGPL); paid tiers not verified
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (scanned for telemetry, installers, updaters and keys, not fully read; a review, 6d78eb2): Looks safe. The CLI installs via `curl|sh` (preview with `--dry-run` first); `cap agents install` writes skills into `~/.claude/skills`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: no confirmed command yet; follow the official docs at [https://cap.so/download](https://cap.so/download) (desktop app)
Claude Code (local only): no confirmed command yet; the CLI installer is `curl|sh`, so preview with `--dry-run` first and follow the official docs at [https://cap.so/docs/installation](https://cap.so/docs/installation)
