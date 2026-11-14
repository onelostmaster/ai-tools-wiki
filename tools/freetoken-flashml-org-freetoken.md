# FreeToken (FlashML-org/FreeToken)

- **Type:** app
- **Category:** developer tools, Hermes add-ons, 3D and games
- **Official URL:** https://github.com/FlashML-org/FreeToken
- **GitHub repo:** https://github.com/FlashML-org/FreeToken @ 3d23551 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); desktop app price unknown
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @3d23551, a review / Hermes a review, 2026-11-02): caution. Its launcher can run vendor curl | bash installers for agents, only when you ask in an interactive terminal (`python/freetoken/launch.py:93-115,974-1023`). Control plane is loopback-only (`server/accounting.py:117-145`). The Windows desktop app (flashml.ai) is not in the repo and was not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: desktop app from flashml.ai (not reviewed) or the CLI per its README; needs an NVIDIA RTX 30/40/50 GPU. Never let it run vendor installers unasked.
Hermes: point Hermes at its local endpoint.
Android: no.
