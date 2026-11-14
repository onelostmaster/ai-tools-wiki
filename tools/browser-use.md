# Browser Use

- **Type:** library
- **Category:** automation, scraping
- **Official URL:** https://browser-use.com
- **GitHub repo:** https://github.com/browser-use/browser-use @ b49a68e (MIT)
- **Price:** Library free (MIT); Browser Use Cloud $0.02 per browser-hour + $5/GB proxy, pay as you go (browser-use.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @b49a68e, a review / Hermes a review, 2026-11-02): caution. PostHog telemetry on by default, off with ANONYMIZED_TELEMETRY=false; cloud sync follows that setting (`browser_use/config.py:58-63`; `telemetry/service.py:21`). An agent in your logged-in browser can act on any site.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `uv add browser-use` (README); set ANONYMIZED_TELEMETRY=false and use a separate browser profile with no logins. Android: no.
