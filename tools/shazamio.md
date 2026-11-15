# shazamio

- **Type:** library
- **Category:** voice and audio, video analysis
- **Official URL:** https://pypi.org/project/shazamio/
- **GitHub repo:** https://github.com/shazamio/ShazamIO @ a0789af (2026-11-01, v0.9.0, MIT); native core https://github.com/shazamio/shazamio-core @ f6076da
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @a0789af, v0.9. The Python layer only calls Shazam and Apple endpoints (shazamio/misc.py:10-59) through aiohttp; a song lookup sends the audio fingerprint, not the audio, with random UUIDs, the timezone and an empty geolocation (shazamio/converter.py:6-12, shazamio/api.py:498-514). No subprocess, eval/exec, pickle, telemetry or hooks. The Rust core (shazamio-core, pinned ==2.0.0 in pyproject.toml) decodes and fingerprints audio locally with no network or process code. Note: it uses an unofficial, reverse-engineered Shazam API, so it can break or be rate limited (HTTP 429) at any time.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install shazamio==0.9.0` (the reviewed v0.9.0, a0789af; it pins shazamio-core==2.0.0). It sends only the audio fingerprint to Shazam (shazamio/api.py:498-514). It uses an unofficial Shazam API, so lookups will fail when Shazam changes it or rate-limits (HTTP 429); No fix: that is outside the library. Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install shazamio`

## Install notes

Claude Code: `pip install shazamio` (PyPI)
