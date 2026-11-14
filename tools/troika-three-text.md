# Troika (three-text)

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/protectwise/troika
- **GitHub repo:** https://github.com/protectwise/troika
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; protectwise/troika @9c89d51. 3D typography. Font resolver makes XMLHttpRequests (packages/troika-three-text/src/FontResolver.js:57) and resolves fallback fonts; workerBootstrap.js:84-91 creates script blobs/importScripts. Root postinstall runs bootstrap (package.json:40), examples reference Google fonts. Pin and self-host fonts/assets; dependency/font resolver not fully audited.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; browser output may run on Android subject to GPU support. No native Claude skill/MCP in this repo.
