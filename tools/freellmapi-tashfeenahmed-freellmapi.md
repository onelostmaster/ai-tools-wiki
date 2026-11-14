# FreeLLMAPI (tashfeenahmed/freellmapi)

- **Type:** app
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://github.com/tashfeenahmed/freellmapi
- **GitHub repo:** https://github.com/tashfeenahmed/freellmapi @ 741d030 (MIT)
- **Price:** Free, MIT; Premium live catalog $19/year (freellmapi.co, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @741d030, a review / Hermes a review, 2026-11-02): caution. Stores your provider keys AES-256-GCM encrypted locally (`README.md:156`) but pulls a remote signed model catalog (`README.md:31`); curl | bash installer (`README.md:169`); pooling free tiers may break provider terms (`README.md:510-512`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: the official .exe from its GitHub releases, not the curl | bash installer; keep keys local.
Hermes: point Hermes at its local endpoint.
Android: a Play Store app is listed but not reviewed.
