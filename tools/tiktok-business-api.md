# TikTok Business API

- **Type:** API
- **Category:** video analysis
- **Official URL:** https://business-api.tiktok.com/portal
- **GitHub repo:** unknown
- **Price:** No fee found; developer registration needs a verified company-domain email (`business-api.tiktok.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

TikTok (official API for Business; not code-reviewed): safe. No security findings are recorded. TikTok's docs: the Organic API's Accounts API covers profile and post insights for authorized accounts; developer registration needs a verified company-domain email, and TikTok says it can't onboard personal accounts or individual developers yet.

## Safe install

Safe install (fixes applied):
TikTok does not onboard personal accounts or individual developers yet, so this will not work with a personal setup). If registered, authorize only the Accounts API insights scopes for your own account, keep the access token in an environment variable outside any repo, never in chat.

## YOLO install

Not written yet.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://business-api.tiktok.com/portal](https://business-api.tiktok.com/portal)
Claude Code: needs a TikTok developer registration and the account holder's authorization; never paste access tokens into chat, add them as secrets/env vars.
