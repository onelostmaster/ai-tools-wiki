# shazamio

- **Type:** library
- **Category:** voice and audio, video analysis
- **Official URL:** https://pypi.org/project/shazamio/
- **GitHub repo:** https://github.com/shazamio/ShazamIO @ a0789af (2026-11-01, v0.9.0, MIT); native core https://github.com/shazamio/shazamio-core @ f6076da
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @a0789af, v0.9. The Python layer only calls Shazam and Apple endpoints (shazamio/misc.py:10-59) through aiohttp; a song lookup sends the audio fingerprint, not the audio, with random UUIDs, the timezone and an empty geolocation (shazamio/converter.py:6-12, shazamio/api.py:498-514). No subprocess, eval/exec, pickle, telemetry or hooks. The Rust core (shazamio-core, pinned ==2.0.0 in pyproject.toml) decodes and fingerprints audio locally with no network or process code. Note: it uses an unofficial, reverse-engineered Shazam API, so it can break or be rate limited (HTTP 429) at any time.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install shazamio` (PyPI)
