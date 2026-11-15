# yt-dlp

- **Type:** CLI
- **Category:** research, video analysis
- **Official URL:** https://github.com/yt-dlp/yt-dlp
- **GitHub repo:** [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) (confirmed on PyPI, 2026-10-31)
- **Price:** Free (Unlicense, per PyPI, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (code read b77c930 = 2026.10.26; fix-mode 2026-11-14): caution, 6/10. Every code risk has a fix in Install notes (--ignore-config, YTDLP_NO_PLUGINS=1, --no-cookies, --no-exec, pinned wheel hash, no -U from agents). No fix: YouTube's Terms forbid downloading and automated access, and no flag changes that; account cookies risk bans, so they stay off. Instagram and TikTok public reels work without cookies.

## Safe install

Safe install (fixes applied):
A download skill skill's pinned venv and the full 'Every run' command in Install notes. Never -U from agents, never cookies.

## YOLO install

YOLO (your own risk): skips the pin, config and plugin blocks and the no-cookies rule.
pip install -U yt-dlp then yt-dlp --cookies-from-browser chrome URL.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: use a download skill skill (user's account skill): pinned venv with pip install --only-binary=\:all\: "yt-dlp[default,pin,pin-deno,pin-curl-cffi]==2026.10.26". Cloud projects must allow instagram.com, *.instagram.com, *.cdninstagram.com, *.fbcdn.net (TikTok: tiktok.com, *.tiktok.com, *.tiktokcdn.com, *.tiktokcdn-us.com, *.tiktokv.com; YouTube: youtube.com, *.youtube.com, *.googlevideo.com, *.ytimg.com) under Network access.
One Unix user per bot.
Every run: YTDLP_NO_PLUGINS=1 yt-dlp --ignore-config --no-config-locations --no-plugin-dirs --no-remote-components --no-cookies --no-cookies-from-browser --no-exec --no-exec-before-download --no-playlist -t sleep -P <own folder> -o "%(id)s.%(ext)s" -- URL
Standalone binary check: sha256sum must equal 767ba9dce7052aa196f8b12652f433d76de128ba168966fa84b6394d5e6c6795 (yt-dlp_linux 2026.10.26) or e51e69e89489f199530f13d32a4342da3ddb2cf34842f364603a066db05afbf3 (zipimport yt-dlp), from the GPG-verified SHA2-256SUMS.
Rules: no -U from agents (a human updates within ~1 week of each stable, at once for Security releases); never a project's or any posting account's cookies; on a bot check, 403 or 429 stop and ask for the file; never re-upload third-party clips; only deno as JS runtime; no apt package. Hermes: not needed (its youtube-content skill uses youtube-transcript-api).
Tip (2026-11-01, from the wiki and a review bot): for captions use `--sub-langs en,en-orig`, not `en.*` (that hits HTTP 429). Private posts, Stories, Saved and DMs need sign-in, which the no-cookies rule rules out, so ask the user for the file.
Tip (2026-11-02, from the wiki): from a cloud container, Instagram and TikTok downloads work (TikTok needs the curl_cffi extra), but YouTube gives only info and captions; the video file itself returns HTTP 403, so ask the user for the file.
