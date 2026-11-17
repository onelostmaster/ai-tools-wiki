# halfsize (YKLovePython)

- **Type:** CLI
- **Category:** editing, video
- **Official URL:** https://YKLovePython.github.io/halfsize/
- **GitHub repo:** https://github.com/YKLovePython/halfsize @ d8764ac (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-16) listed it but did not read or rate it (skipped by description). Repo and commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: install it in a project folder with `npm install halfsize@<pinned version>` (not -g, not @latest), point HALFSIZE_FFMPEG/HALFSIZE_FFPROBE at a winget Gyan.FFmpeg build so no prebuilt binary is downloaded (README:332), run it on copies of your videos, no keys needed, skip the npx skills route. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README\:100-124\: `npx halfsize video.mp4 --to 25mb` or `npm install -g halfsize` (global). README:310: ffmpeg-static downloads a prebuilt FFmpeg during npm install. README:193: skill route `npx skills add YKLovePython/halfsize`. README:148 says files stay on your machine. Windows: `winget install Gyan.FFmpeg` and HALFSIZE_FFMPEG/HALFSIZE_FFPROBE env vars point it at that build (README:332,343).
