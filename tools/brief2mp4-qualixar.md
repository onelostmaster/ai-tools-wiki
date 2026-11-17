# brief2mp4 (qualixar)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://qualixar.com/learn/guides/brief2mp4-guide
- **GitHub repo:** https://github.com/qualixar/brief2mp4 @ c262562 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-16) read it: 2/5, delivery spec check, mostly covered. Repo and commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: use the Claude Code plugin route only (README:69) pinned to commit c262562, install Node 22, ffmpeg and Git via winget yourself instead of running install.ps1 with -ExecutionPolicy Bypass, skip the 3D and edit packs, no keys needed. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README:69: Claude Code plugin `/plugin marketplace add qualixar/brief2mp4` then `/plugin install brief2mp4@brief2mp4`. README:72: Windows `install.ps1 -InstallTools` runs with `-ExecutionPolicy Bypass` and installs Node, ffmpeg and Git Bash via winget (README:63,92-94); 3D and edit packs are extra downloads (README:174-206).
