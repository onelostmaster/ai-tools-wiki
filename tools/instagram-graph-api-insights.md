# Instagram Graph API (insights)

- **Type:** API
- **Category:** video analysis
- **Official URL:** https://developers.facebook.com/docs/instagram-platform/insights/
- **GitHub repo:** unknown
- **Price:** No fee found in Meta's docs; needs an Instagram professional account (`developers.facebook.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Meta (official Instagram Platform API; not code-reviewed): safe. No security findings are recorded.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): follow https://developers.facebook.com/docs/instagram-platform/insights/ with an Instagram professional account; with Instagram Login grant only instagram_business_manage_insights (plus the basic profile permission the login requires) and no publishing or messaging permissions. Keep the access token in an environment variable outside any repo, never in chat. Data lags up to 48 hours (Meta docs).

## YOLO install

Not written yet.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://developers.facebook.com/docs/instagram-platform/insights/](https://developers.facebook.com/docs/instagram-platform/insights/)
Never paste access tokens into chat, add them as secrets/env vars.
