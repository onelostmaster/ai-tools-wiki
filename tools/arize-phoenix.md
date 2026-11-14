# Arize Phoenix

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/Arize-ai/phoenix
- **GitHub repo:** https://github.com/Arize-ai/phoenix @ e3ba11f (Elastic License 2.0, source-available)
- **Price:** Free to self-host; hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @e3ba11f, a review, 2026-11-02): caution. Source-available (Elastic License 2.0), not open source. FullStory web tracking only if PHOENIX_FULLSTORY_ORG is set (`src/phoenix/config.py:154-156`); helm chart has PHOENIX_TELEMETRY_ENABLED (`values.yaml:175`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: pip or Docker (not tested). Android: dashboard in a phone browser once hosted.
