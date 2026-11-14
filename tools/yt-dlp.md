# yt-dlp

- **Type:** CLI
- **Category:** research, video analysis
- **Official URL:** https://github.com/yt-dlp/yt-dlp
- **GitHub repo:** [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) (confirmed on PyPI, 2026-10-31)
- **Price:** Free (Unlicense, per PyPI, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-09

## Safety reason

Claude (code read, b77c930 = 2026.10.26, 2026-11-01): caution, 6/10. No telemetry; releases GPG-signed. Risks for agents: config files auto-load from the current folder, ~/.config and /etc (a config can set --exec, --proxy, plugin dirs) unless --ignore-config; Python plugins auto-import from site-packages/sys.path unless YTDLP_NO_PLUGINS=1; --cookies-from-browser decrypts every cookie in the browser, and yt-dlp's bot-check error tells agents to use it; 5 high-severity injection advisories in 2026 plus a certifi MITM warning for old executables, so stay current. Platform risk: YouTube ToS forbids downloading/automated access; account cookies risk bans; re-uploading others' clips brings strikes. Live test from a Claude cloud machine (2026-11-01): Instagram reels download without login; TikTok works with the curl_cffi extra; YouTube gives metadata and captions but the video download gets HTTP 403 (cloud-IP block). Earlier: a review bot inferred caution (Instagram/TikTok terms); Grok uses it in a project reel breakdowns (2026-10-30/31).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: use the a download skill skill (user's account skill): pinned venv with pip install --only-binary=\:all\: "yt-dlp[default,pin,pin-deno,pin-curl-cffi]==2026.10.26". Cloud projects must allow instagram.com, *.instagram.com, *.cdninstagram.com, *.fbcdn.net (TikTok: tiktok.com, *.tiktok.com, *.tiktokcdn.com, *.tiktokcdn-us.com, *.tiktokv.com; YouTube: youtube.com, *.youtube.com, *.googlevideo.com, *.ytimg.com) under Network access.
10.26" (wheel sha256 a05c5b5d8562f7e8a62f5334348b406af4930d56d3a65f8021d14af0e22339ae). One Unix user per bot.
Every run: YTDLP_NO_PLUGINS=1 yt-dlp --ignore-config --no-config-locations --no-plugin-dirs --no-remote-components --no-cookies --no-cookies-from-browser --no-exec --no-exec-before-download --no-playlist -t sleep -P <own folder> -o "%(id)s.%(ext)s" -- URL
Standalone binary check: sha256sum must equal 767ba9dce7052aa196f8b12652f433d76de128ba168966fa84b6394d5e6c6795 (yt-dlp_linux 2026.10.26) or e51e69e89489f199530f13d32a4342da3ddb2cf34842f364603a066db05afbf3 (zipimport yt-dlp), from the GPG-verified SHA2-256SUMS.
Rules: no -U from agents (a human updates within ~1 week of each stable, at once for Security releases); never a project's or any posting account's cookies; on a bot check, 403 or 429 stop and ask for the file; never re-upload third-party clips; only deno as JS runtime; no apt package. Hermes: not needed (its youtube-content skill uses youtube-transcript-api).
Tip (2026-11-01, from the wiki and a review bot): for captions use `--sub-langs en,en-orig`, not `en.*` (that hits HTTP 429). Private posts, Stories, Saved and DMs need sign-in, which the no-cookies rule rules out, so ask the user for the file.
Tip (2026-11-02, from the wiki): from a cloud container, Instagram and TikTok downloads work (TikTok needs the curl_cffi extra), but YouTube gives only info and captions; the video file itself returns HTTP 403, so ask the user for the file.
