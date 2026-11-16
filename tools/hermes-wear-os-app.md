# Hermes Wear OS app

- **Type:** app
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/borealBytes/hermes-wearos
- **GitHub repo:** [https://github.com/borealBytes/hermes-wearos](https://github.com/borealBytes/hermes-wearos)
- **Price:** unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @50b65cd = v0.10.12 (2026-11-15): safe with fixes. Redesigned: API_SERVER_KEY now travels only over a tailnet-bound private lane after a one-time pairing secret, with anonymous calls refused (app/.../net/PrivateLane.kt:18-23). The watchkit daemon binds 127.0.0.1 by default (server/watchkit/watchkit.mjs:103). Fix: set its host to your tailnet IP, never a LAN or 0.0.0.0; keep Tailscale on.

## Safe install

Safe install (fixes applied):
Clone at 50b65cd; Tailscale on phone, watch host and PC; in server/watchkit config.json set host to the PC's 100.x tailnet IP; build and sideload with scripts/build.sh and install-watch.sh; never expose watchkit with Funnel.

## YOLO install

YOLO (your own risk): skips the tailnet-only bind.
Set watchkit host to 0.0.0.0 on your home LAN.

## Install notes

Ask the user before installing. Clone at 50b65cd; Tailscale on phone, watch host and PC; in server/watchkit config.json set host to the PC's 100.x tailnet IP; build and sideload with scripts/build.sh and install-watch.sh; never expose watchkit with Funnel.
