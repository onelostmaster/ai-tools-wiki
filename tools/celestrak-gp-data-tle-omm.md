# CelesTrak GP data (TLE/OMM)

- **Type:** dataset
- **Category:** research
- **Official URL:** https://celestrak.org/NORAD/documentation/gp-data-formats.php
- **GitHub repo:** unknown
- **Price:** Free, donations welcome; at most one download per 2 hours per query (celestrak.org GP docs, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-15

## Safety reason

Read-only public data from the CelesTrak non-profit, no account or key. Strict rate rules on the official GP docs page (checked 2026-11-12): data updates every 2 hours, one download per update per query, more than 50 HTTP 301/403/404 errors in 2 hours sends the IP to the firewall.

## Safe install

Safe install (fixes applied):
Nothing to install: plain HTTPS GET to https://celestrak.org/NORAD/elements/gp.php with GROUP, CATNR or NAME and FORMAT=JSON or CSV (answered 200 on 2026-11-15), no key or account, from any platform (claude.ai, Claude Code, Hermes, Android, Windows). Fixes for the official rate rules (GP docs page): cache each query and re-download only when the cached file is over 2 hours old; stop on the first 301/403/404 and tell the user, because more than 50 such errors in 2 hours puts the IP behind CelesTrak's firewall; use the .org domain only.

## YOLO install

Not written yet.

## Install notes

Any platform: query https://celestrak.org/NORAD/elements/gp.php with GROUP, CATNR or NAME and FORMAT=JSON or CSV (CSV is the default; TLE cannot hold catalog numbers above 69999). Cache the file and re-download only when it is over 2 hours old; stop on any 301/403/404 and tell the user. Use the .org domain, never .com.
