# Camofox browser server (camofox-browser)

- **Type:** app
- **Category:** scraping, research
- **Official URL:** https://github.com/jo-inc/camofox-browser
- **GitHub repo:** [https://github.com/jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) @ 39c8209 (v1.18.1, 2026-10-04; MIT)
- **Price:** Free (MIT). Residential proxies, if used, are paid.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

Claude (code read, v1.18.1 39c8209, 2026-11-01): caution, 5/10. With default settings the REST API on port 9377 listens on every network interface (server.js:7196) and needs no key except for cookie import and traces, so /tabs/:id/evaluate (runs JavaScript in pages) is open to anyone who can reach the port. Crash/hang telemetry is on by default and becomes issues on the public GitHub repo via [camofox-telemetry.askjo.workers.dev](http://camofox-telemetry.askjo.workers.dev) (opt out: CAMOFOX_CRASH_REPORT_ENABLED=false). Cookies and localStorage are saved to ~/.camofox/profiles/. The first run downloads about 300 MB of Camoufox. Built to evade bot detection, which can break site terms.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Own machine only: git clone [https://github.com/jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) && cd camofox-browser && git checkout v1.18.1 && npm ci (Node 22+), then CAMOFOX_BIND_HOST=127.0.0.1 CAMOFOX_ACCESS_KEY=<random 32+ chars> CAMOFOX_CRASH_REPORT_ENABLED=false npm start
Never expose port 9377 to the internet; no cookie import of real accounts; a residential proxy only with user approval.
Hermes: pair with the official camofox plugin (hermes plugins install camofox) and point CAMOFOX_URL at this server.
Not a fix for YouTube's cloud-IP bot check: use a home IP or attach the file instead.
