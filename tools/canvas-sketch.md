# canvas-sketch

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/mattdesl/canvas-sketch
- **GitHub repo:** https://github.com/mattdesl/canvas-sketch
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; mattdesl/canvas-sketch @798a24f. Generative artwork and loops. Source scan found no telemetry/install hooks; lib/save.js:10-11 references a commented data-URL save helper, not a remote upload. README Quick Start uses separate canvas-sketch-cli, which was not reviewed here.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; browser output may run on Android subject to GPU support. No native Claude skill/MCP in this repo.
