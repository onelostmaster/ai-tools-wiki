# viral-hook-reels-skill (dovudhusan)

- **Type:** skill
- **Category:** generating videos, editing, voice and audio
- **Official URL:** https://github.com/dovudhusan/viral-hook-reels-skill
- **GitHub repo:** https://github.com/dovudhusan/viral-hook-reels-skill @ 023e3f4 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-18); ElevenLabs is a separate paid service (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-18

## Safety reason

Not code-reviewed for safety. README: Instagram links are downloaded by yt-dlp with your own logged-in Chrome session (TikTok and Shorts links need no login); the first run installs the engine's packages and creates engine/.env for an ElevenLabs API key; built and tested on macOS, Windows untested. Reusing other creators' footage raises rights questions. Repo, license and latest commit confirmed from github.com metadata, 2026-11-18.

## Safe install

Unreviewed: contain it: clone at the pinned commit 023e3f4 into a sandbox, use only TikTok or Shorts links so yt-dlp never reads your Chrome Instagram session, and use a separate ElevenLabs key with a low quota. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: git clone into %USERPROFILE%\.claude\\skills\\hook-reel (README); needs node, ffmpeg, yt-dlp and an ElevenLabs API key. Windows is untested by the author.
