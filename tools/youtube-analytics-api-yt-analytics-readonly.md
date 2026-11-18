# YouTube Analytics API (yt-analytics.readonly)

- **Type:** API
- **Category:** video analysis
- **Official URL:** https://developers.google.com/youtube/analytics
- **GitHub repo:** unknown
- **Price:** No fee found; each request counts against a Google Cloud quota (`developers.google.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Google (official YouTube API; not code-reviewed): safe. No security findings are recorded. a project's plan (tool scout, 2026-10-30) asks for the read-only scope `yt-analytics.readonly`, with one Google sign-in from the user; Google's API reference says `reports.query` also needs the read-only `youtube.readonly` scope (`developers.google.com`, checked 2026-10-31).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): in your own Google Cloud project, create the OAuth client and sign in once with only the read-only scopes yt-analytics.readonly and youtube.readonly (reports.query needs both, Google API reference). Keep the client secret and token files outside any repo folder and give them to tools as environment variables or file paths, never in chat. Do not grant write scopes such as youtube or youtube.upload; this use only reads reports.
Android: not needed (use the YouTube Studio app).

## YOLO install

Not written yet.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://developers.google.com/youtube/analytics](https://developers.google.com/youtube/analytics)
Claude Code: needs one Google sign-in (OAuth) from the user, with the read-only scopes `yt-analytics.readonly` and `youtube.readonly` (Google's reference requires the second for `reports.query`); never paste tokens into chat, add them as secrets/env vars.
