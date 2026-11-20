# Eva Icons (Akveo)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://akveo.github.io/eva-icons
- **GitHub repo:** https://github.com/akveo/eva-icons @70d2471f, 8,814 stars; latest default-branch commit 2020-09-08 15:02 ET; original nonfork; archived=False
- **Price:** Free, MIT (LICENSE.txt; official README online). Preserve license notices; third-party marks separately. No subscription stated.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @70d2471 + npm eva-icons 1.1.3 (2026-11-19): safe with fixes. The static SVG/PNG files carry no script; the unescaped attributes are only in the JS replace()/toSvg() API (package/src/icon.js:26-37), which the static files never call. npm 1.1.3 has no scripts or dependencies. Last commit 2020 is not a risk for static artwork. Fix: static files only, pinned.

## Safe install

Safe install (fixes applied):
Windows or Claude Code: use only the static SVG/PNG files (from the repo at commit 70d2471 or the official download), self-hosted, or npm install --save-exact --ignore-scripts eva-icons@1.1.3 (npm latest on 2026-11-15; no scripts, no dependencies) and import the SVG files. Don't use the JS replace()/toSvg() API with any text you didn't write yourself (icon.js lines 26-37 and replace.js lines 35-50 put attributes into the DOM unescaped). Don't load it from unpkg and don't run the old website dev server (binds 0.0.0.0:3333). Android and claude.ai: use the SVG files. Hermes: static files only.

## YOLO install

YOLO (your own risk): skips the version pin and the static-files-only rule.
npm i eva-icons

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented only: npm i eva-icons, or download individual SVG/PNG from official website. Self-host approved static SVG; avoid unpinned unpkg script and old developer server. Windows authoring/Android rendered assets; no official MCP found. Hermes compatibility untested.
