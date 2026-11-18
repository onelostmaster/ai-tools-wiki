# FreeLLMAPI (tashfeenahmed/freellmapi)

- **Type:** app
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://github.com/tashfeenahmed/freellmapi
- **GitHub repo:** https://github.com/tashfeenahmed/freellmapi @ 741d030 (MIT)
- **Price:** Free, MIT; Premium live catalog $19/year (freellmapi.co, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @ca0a274 v0.16.32 (2026-11-17): safe with fixes. The catalog feed is Ed25519-checked against a pinned key (server/src/services/catalog-sync.ts:112,1088); CATALOG_SYNC_DISABLED=1 stops it (:1268). Compose binds 127.0.0.1 (docker-compose.yml:25); the watchtower updater is opt-in (:58). The quick start is curl|bash on :latest (README.md:169). Fix: pinned image, one key per provider account.

## Safe install

Safe install (fixes applied):
Clone at ca0a274; set image to ghcr.io/tashfeenahmed/freellmapi:v0.16.32 in docker-compose.yml; docker compose up -d (no autoupdate profile); keys only in the dashboard, one account per provider; Windows: the release .exe, not curl|bash.

## YOLO install

YOLO (your own risk): skips the pin and the one-account rule.
curl -fsSL https://freellmapi.co/install.sh | bash on :latest and pool as many keys as you like.

## Install notes

Ask the user before installing.
Windows: the official .exe from its GitHub releases, not the curl | bash installer; keep keys local.
Hermes: point Hermes at its local endpoint.
Android: a Play Store app is listed but not reviewed.
