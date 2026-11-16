# Anime.js

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/juliangarnier/anime
- **GitHub repo:** https://github.com/juliangarnier/anime
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; juliangarnier/anime @01b81be. Animation timelines and easing. Source scan found no telemetry or install hooks; src/index.js:1-2 exports animation/timer modules. Examples load Google Fonts (examples/text/split-effects/index.html:16-18), not required by the library.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any web project: `npm install animejs@4.5.0` (current npm release; no install scripts, no runtime dependencies) and bundle it locally. The library makes no network calls (src/index.js:1-2 exports animation/timer modules only); the Google Fonts load is only in the repo examples (examples/text/split-effects/index.html:16-18), so don't copy those example pages as-is. Not a claude.ai or Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin.
npm install animejs

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; the result is a web page that runs in any modern browser, Android included (plain SVG/DOM animation, no GPU requirement). No native Claude skill/MCP in this repo.
