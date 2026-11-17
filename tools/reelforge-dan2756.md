# ReelForge (dan2756)

- **Type:** app
- **Category:** generating videos, social posting
- **Official URL:** https://github.com/dan2756/ReelForge
- **GitHub repo:** https://github.com/dan2756/ReelForge @ 10ea0f4 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-16) read it: 1.5/5, competitor app, skip. Repo and commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: do not pipe the script to iex: download install.ps1 from a pinned release, read it, and run it in a Windows Sandbox or spare VM with REELFORGE_DIR set to a test folder; log in no social accounts and run `reelforge stats off` (README:488). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README:49: Windows install is `irm .../releases/latest/download/install.ps1 | iex` (runs the latest release script); it downloads Blender, ffmpeg and sound effects into C:\\Users\\<you>\\ReelForge (README:61,76). README:189: Instagram and X need a log-in in its own browser window. README:231,488: an hourly background stats job, switchable with `reelforge stats off`.
