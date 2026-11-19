# Browser Use

- **Type:** library
- **Category:** automation, scraping
- **Official URL:** https://browser-use.com
- **GitHub repo:** https://github.com/browser-use/browser-use @ b49a68e (MIT)
- **Price:** Library free (MIT); Browser Use Cloud $0.02 per browser-hour + $5/GB proxy, pay as you go (browser-use.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @b49a68e, a review / Hermes a review, 2026-11-02): caution. PostHog telemetry on by default, off with ANONYMIZED_TELEMETRY=false; cloud sync follows that setting (browser_use/config.py:58-63; telemetry/service.py:21). An agent in your logged-in browser can act on any site. Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (ANONYMIZED_TELEMETRY=false set before first run, separate browser profile with no logins, LLM keys in env vars); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: in a project venv, uv add browser-use==<release matching b49a68e>. Set ANONYMIZED_TELEMETRY=false before first run; otherwise PostHog telemetry is on and cloud sync follows it (browser_use/config.py:58-63; telemetry/service.py:21). Point it only at a separate browser profile with no logins, because the agent can act on any site that profile is signed in to; keep LLM keys in env vars. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the telemetry switch and the separate profile.
Windows: uv add browser-use with defaults in your normal browser; telemetry stays on and the agent can act on every site you are signed in to.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: uv add browser-use (README); set ANONYMIZED_TELEMETRY=false and use a separate browser profile with no logins. Android: no.
