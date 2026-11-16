# coolray-video-qc (ShakeJ)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/ShakeJ/coolray-video-qc
- **GitHub repo:** https://github.com/ShakeJ/coolray-video-qc @ 4ecab08 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-15)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-15

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-15) read it as read-only FFmpeg QC. README: no account, API key or upload, source files are not modified, scripts never install dependencies; Windows has not been validated by the author (macOS tested, Linux CI). Repo, license and latest commit confirmed from github.com metadata, 2026-11-15.

## Safe install

Unreviewed: contain it: download the v0.1.0 release ZIP (pinned version, not the moving main branch), run it first from a test folder on copies of your videos, no API keys needed and no network needed (it works on local files only), and keep the output folder separate from your source files. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: copy the folder (SKILL.md at its root) to %USERPROFILE%\.claude\\skills\\coolray-video-qc (README). Needs Python 3.10+ and ffmpeg/ffprobe on PATH. Windows is not validated by the author.
