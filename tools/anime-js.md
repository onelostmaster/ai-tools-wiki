# Anime.js

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/juliangarnier/anime
- **GitHub repo:** https://github.com/juliangarnier/anime
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; juliangarnier/anime @01b81be. Animation timelines and easing. Source scan found no telemetry or install hooks; src/index.js:1-2 exports animation/timer modules. Examples load Google Fonts (examples/text/split-effects/index.html:16-18), not required by the library.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; browser output may run on Android subject to GPU support. No native Claude skill/MCP in this repo.
