# Synfig Studio

- **Type:** app
- **Category:** generating videos, design
- **Official URL:** https://github.com/synfig/synfig
- **GitHub repo:** https://github.com/synfig/synfig
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; synfig/synfig @751779e. 2D character animation. No telemetry indicator found in targeted scan. Plugin execution is real code execution (synfig-studio/src/gui/pluginmanager.cpp:633 Glib::spawn_sync); bundled Lottie viewer evaluates animation expressions (plugins/lottie-exporter/bodymovin.js:12069-12074). Use trusted projects/plugins only; not a Claude plugin.

## Safe install

Safe install (fixes applied):
Windows: download SynfigStudio-1.5.5-2026.03.15-win64-79bf7.exe from https://github.com/synfig/synfig/releases (release v1.5.5), check it against checksum-sha256.txt from the same release, and install it. Never install plugins from anywhere but your own files: plugins run as real programs (synfig-studio/src/gui/pluginmanager.cpp:633). Open only your own projects; the bundled Lottie preview evaluates animation expressions (plugins/lottie-exporter/bodymovin.js:12069-12074), so preview only Lottie files you made. Not a claude.ai, Hermes or Android tool.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
