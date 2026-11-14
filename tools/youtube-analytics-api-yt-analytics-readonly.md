# YouTube Analytics API (yt-analytics.readonly)

- **Type:** API
- **Category:** video analysis
- **Official URL:** https://developers.google.com/youtube/analytics
- **GitHub repo:** unknown
- **Price:** No fee found; each request counts against a Google Cloud quota (`developers.google.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-10-31

## Safety reason

Google (official YouTube API; not code-reviewed): safe. No security findings are recorded. a project's plan (tool scout, 2026-10-30) asks for the read-only scope `yt-analytics.readonly`, with one Google sign-in from the user; Google's API reference says `reports.query` also needs the read-only `youtube.readonly` scope (`developers.google.com`, checked 2026-10-31).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://developers.google.com/youtube/analytics](https://developers.google.com/youtube/analytics)
Claude Code: needs one Google sign-in (OAuth) from the user, with the read-only scopes `yt-analytics.readonly` and `youtube.readonly` (Google's reference requires the second for `reports.query`); never paste tokens into chat, add them as secrets/env vars.
