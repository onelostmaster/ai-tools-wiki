# Synfig Studio

- **Type:** app
- **Category:** generating videos, design
- **Official URL:** https://github.com/synfig/synfig
- **GitHub repo:** https://github.com/synfig/synfig
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; synfig/synfig @751779e. 2D character animation. No telemetry indicator found in targeted scan. Plugin execution is real code execution (synfig-studio/src/gui/pluginmanager.cpp:633 Glib::spawn_sync); bundled Lottie viewer evaluates animation expressions (plugins/lottie-exporter/bodymovin.js:12069-12074). Use trusted projects/plugins only; not a Claude plugin.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
