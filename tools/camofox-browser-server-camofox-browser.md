# Camofox browser server (camofox-browser)

- **Type:** app
- **Category:** scraping, research
- **Official URL:** https://github.com/jo-inc/camofox-browser
- **GitHub repo:** [https://github.com/jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) @ 39c8209 (v1.18.1, 2026-10-04; MIT)
- **Price:** Free (MIT). Residential proxies, if used, are paid.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @31376c2 = v1.19.0 (2026-11-16): safe with fixes. With no CAMOFOX_BIND_HOST it listens on every interface (server.js:8823, lib/config.js:150) and without CAMOFOX_ACCESS_KEY routes are open (lib/auth.js:104), including page JavaScript. Crash reports go public unless CAMOFOX_CRASH_REPORT_ENABLED=false (config.js:256). Fix: all three set. It evades bot detection: use it only on sites that allow automation.

## Safe install

Safe install (fixes applied):
git clone https://github.com/jo-inc/camofox-browser && git checkout v1.19.0 && npm ci; start with CAMOFOX_BIND_HOST=127.0.0.1 CAMOFOX_ACCESS_KEY=<random 32+ chars> CAMOFOX_CRASH_REPORT_ENABLED=false; no real-account cookie import.

## YOLO install

YOLO (your own risk): skips the bind, key and crash-report switch, so port 9377 is open on your network.
npm start with defaults.

## Install notes

Ask the user before installing.
Own machine only: git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser && git checkout v1.18.1 && npm ci (Node 22+), then CAMOFOX_BIND_HOST=127.0.0.1 CAMOFOX_ACCESS_KEY=<random 32+ chars> CAMOFOX_CRASH_REPORT_ENABLED=false npm start
Never expose port 9377 to the internet; no cookie import of real accounts; a residential proxy only with user approval.
Hermes: pair with the official camofox plugin (hermes plugins install camofox) and point CAMOFOX_URL at this server.
Not a fix for YouTube's cloud-IP bot check: use a home IP or attach the file instead.
