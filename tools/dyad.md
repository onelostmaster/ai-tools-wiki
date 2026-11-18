# Dyad

- **Type:** app
- **Category:** building a site
- **Official URL:** https://github.com/dyad-sh/dyad
- **GitHub repo:** [https://github.com/dyad-sh/dyad](https://github.com/dyad-sh/dyad)
- **Price:** Free (Apache-2.0 + pro)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code scan, 0ec8cc2, a review): Looks safe. Local AI app builder with your own keys; telemetry is opt-in (banner); it auto-updates; a macOS native keychain reader builds on install. The big app was scanned for telemetry, installers, updaters and keys, not fully read. Re-used in a review (2026-11-01, same scan @0ec8cc2): telemetry opt-in, auto-update (`main.ts:22`); Pro upsell.

## Safe install

Safe install (fixes applied):
Windows: install the desktop app from the official site dyad.sh. Leave the telemetry banner declined (telemetry is opt-in). Enter your model keys only in Dyad's settings, never in chat. It auto-updates (main.ts:22, a review); unverified: whether a setting turns that off. The macOS keychain reader does not apply on Windows.

## YOLO install

Not written yet.

## Install notes

Windows: install the desktop app from `dyad.sh` (the source's route).
