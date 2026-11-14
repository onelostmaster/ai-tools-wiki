# MeshLine (pmndrs)

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/pmndrs/meshline
- **GitHub repo:** https://github.com/pmndrs/meshline
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; pmndrs/meshline @4df8778. Stylized 3D lines/trails. No telemetry/network/install hooks found; src/index.ts:1-2 exports geometry/material. Latest repo commit June 2024: stale, check compatibility with your three.js version before use.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; browser output may run on Android subject to GPU support. No native Claude skill/MCP in this repo.
