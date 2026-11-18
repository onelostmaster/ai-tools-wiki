# Camofox browser plugin (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, research
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/camofox
- **GitHub repo:** [https://github.com/NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins)
- **Price:** Free plugin; needs your own Camofox server
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 2026-10-28): Looks safe. Official Nous plugin; talks only to your own `CAMOFOX_URL` server and blocks URLs that carry secrets (`camofox/camofox_policy.py:91-110`). Stealth browsing and cookie import are the point, so mind site ToS.

## Safe install

Safe install (fixes applied):
Hermes: hermes plugins install camofox. Point CAMOFOX_URL only at your own Camofox server, started locked down: CAMOFOX_BIND_HOST=127.0.0.1, CAMOFOX_ACCESS_KEY set, CAMOFOX_CRASH_REPORT_ENABLED=false (see the camofox-browser row). The plugin blocks URLs that carry secrets (camofox/camofox_policy.py:91-110). Stealth browsing and cookie import are its purpose; follow each site's terms.

## YOLO install

Not written yet.

## Install notes

Hermes: hermes plugins install camofox (needs your own Camofox server)
Server: see the "Camofox browser server (camofox-browser)" row (caution 5/10) and start it locked down: CAMOFOX_BIND_HOST=127.0.0.1, CAMOFOX_ACCESS_KEY set, CAMOFOX_CRASH_REPORT_ENABLED=false.
