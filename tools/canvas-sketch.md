# canvas-sketch

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/mattdesl/canvas-sketch
- **GitHub repo:** https://github.com/mattdesl/canvas-sketch
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; mattdesl/canvas-sketch @798a24f. Generative artwork and loops. Source scan found no telemetry/install hooks; lib/save.js:10-11 references a commented data-URL save helper, not a remote upload. README Quick Start uses separate canvas-sketch-cli, which was not reviewed here.

## Safe install

Safe install (fixes applied):
Windows Claude Code: inside a project folder run `npx canvas-sketch-cli@1.15.0 sketch.js --new --open` (README.md:35; pinned to the current npm release) instead of a global install. The library itself (canvas-sketch 0.7.8) has no install scripts or uploads (lib/save.js:10-11 is a local data-URL save helper). unverified: canvas-sketch-cli was not code-reviewed; run it only in a dedicated project folder with no secrets in it. The output is a web page that runs in any browser, Android included. Not a claude.ai or Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin and project-folder containment.
npm install -g canvas-sketch-cli

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; the sketches it makes are web pages that run in any browser, Android included. No native Claude skill/MCP in this repo.
