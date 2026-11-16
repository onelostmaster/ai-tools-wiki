# Video2X

- **Type:** app
- **Category:** editing
- **Official URL:** https://github.com/k4yt3x/video2x
- **GitHub repo:** https://github.com/k4yt3x/video2x @ 7db9c18 (AGPL-3.0)
- **Price:** Free, AGPL-3.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @7db9c18, a review, 2026-11-02): safe. C++ core and CLI, no network code found; one helper script downloads Anime4K shaders (`scripts/download_merge_anime4k_glsl.py`).

## Safe install

Safe install (fixes applied):
Windows: video2x-windows-amd64.zip (CLI) from the official GitHub release 6.4.0 (github.com/k4yt3x/video2x/releases), unzip to a folder, no admin. The core has no network code (review @7db9c18); skip scripts/download_merge_anime4k_glsl.py, the one helper that downloads shaders. Unverified: the prebuilt 6.4.0 binaries (released 2025-01-24, older than the reviewed 7db9c18 from 2026-03-07). Contain it: run it on copies of your videos and keep originals elsewhere. Android: no. Not a Claude or Hermes tool.

## YOLO install

YOLO (your own risk): skips the CLI-only route; the Qt6 GUI's source is not in the reviewed repo (no GUI folder or submodule at 7db9c18), so the GUI is unreviewed.
video2x-qt6-windows-amd64-installer.exe from the 6.4.0 release (README.md:56).

## Install notes

Safe, but ask the user before installing.
Windows: installer and GUI: CLI zip from the official 6.4.0 release (README.md:54-58); see Safe install. Android: no.
