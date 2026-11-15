# claude-code-video-studio (lewislf)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/lewislf/claude-code-video-studio
- **GitHub repo:** https://github.com/lewislf/claude-code-video-studio @ 07ec7f7 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-14)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-14

## Safety reason

Not code-reviewed for safety. The a project Tool Scout (Claude, 2026-11-14) listed it but did not read or rate it. Repo and commit confirmed from github.com metadata, 2026-11-14.

## Safe install

Unreviewed: contain it: WSL2 Ubuntu only, in a separate folder or devcontainer, with the venv the README names (~/.venvs/studio), pin commit 07ec7f7, no keys, and network only for the model downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README:144 requires an NVIDIA GPU, Linux with systemd-run (memory caps), ffmpeg and Node 22+; the skills run studio/ scripts with python3, ffmpeg and systemd-run (README:173). Not a native Windows tool. unverified: whether it works under WSL2.
