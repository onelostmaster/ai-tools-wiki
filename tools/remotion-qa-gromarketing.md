# remotion-qa (GroMarketing)

- **Type:** CLI
- **Category:** generating videos, editing, video analysis
- **Official URL:** https://github.com/GroMarketing/remotion-qa
- **GitHub repo:** https://github.com/GroMarketing/remotion-qa @ dd246e9 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-17)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed for safety. README at dd246e9: install is npm install --save-dev remotion-qa or npx (README.md:49-53); if no ffmpeg binary is found it downloads the bundled ffmpeg-static copy once on first run (README.md:55-58); the render command runs npx remotion render (README.md:169). A project Tool Scout (Claude, 2026-11-17) read it: 3/5, idea only (reading-time rule per caption: longest line / 15 cps + 0.4 s per extra line + 1 s). Repo, commit, license confirmed from github.com metadata, 2026-11-17; 0 stars, last push 2026-10-05.

## Safe install

Unreviewed: contain it: install it as a dev dependency inside one Remotion project only (npm install --save-dev remotion-qa@<version matching dd246e9>, never global), set REMOTION_QA_FFMPEG to your own ffmpeg (winget install Gyan.FFmpeg) so it downloads nothing on first run (README.md:55-58), no keys in that project, run it on copies of rendered videos. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README.md\:49-53\: npm install --save-dev remotion-qa (or npx remotion-qa). Set REMOTION_QA_FFMPEG to your own ffmpeg to skip the first-run download (README.md:58).
