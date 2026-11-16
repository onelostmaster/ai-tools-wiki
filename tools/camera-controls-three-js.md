# Camera Controls (three.js)

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/yomotsu/camera-controls
- **GitHub repo:** https://github.com/yomotsu/camera-controls
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; yomotsu/camera-controls @c516011. Smooth camera motion for three.js. No telemetry/network/install hooks found in source scan; src/index.ts:1-2 exports CameraControls and EventDispatcher. Browser library, not a Claude skill.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any three.js web project: `npm install camera-controls@3.1.2` (current npm release, no install scripts) alongside three >=0.126.1 (its peer dependency), then `CameraControls.install({ THREE })` in your code as the README shows. It runs in the browser sandbox; no network or telemetry in the reviewed source (src/index.ts:1-2). Not a claude.ai or Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin.
npm install camera-controls

## Install notes

Not installed. Ask the user before any installation, including Try. Browser library for your own three.js pages; runs on Windows and Android browsers with WebGL; unverified: your phone's GPU support (test the page on it). No native Claude skill/MCP in this repo.
