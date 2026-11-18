# Cap

- **Type:** app
- **Category:** editing
- **Official URL:** https://github.com/CapSoftware/Cap
- **GitHub repo:** [https://github.com/CapSoftware/Cap](https://github.com/CapSoftware/Cap)
- **Price:** Free (AGPL); paid tiers not verified
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (scanned for telemetry, installers, updaters and keys, not fully read; a review, 6d78eb2): Looks safe. The CLI installs via `curl|sh` (preview with `--dry-run` first); `cap agents install` writes skills into `~/.claude/skills`.

## Safe install

Safe install (fixes applied):
Windows: install the desktop app from the official page https://cap.so/download. CLI (only if needed): download the installer script, run it with --dry-run first and read what it does, then run it (it is curl|sh; a review, 6d78eb2). cap agents install writes skills into ~/.claude/skills every time it runs, so run it only if you want those skills. Paid tiers: unknown.

## YOLO install

YOLO (your own risk): skips the --dry-run preview.
The CLI curl|sh one-liner from https://cap.so/docs/installation.

## Install notes

Windows: no confirmed command yet; follow the official docs at [https://cap.so/download](https://cap.so/download) (desktop app)
Claude Code (local only): no confirmed command yet; the CLI installer is `curl|sh`, so preview with `--dry-run` first and follow the official docs at [https://cap.so/docs/installation](https://cap.so/docs/installation)
