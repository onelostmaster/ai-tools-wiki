# MoviePy

- **Type:** library
- **Category:** editing
- **Official URL:** https://github.com/Zulko/moviepy
- **GitHub repo:** https://github.com/Zulko/moviepy @ 211e4b1 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @211e4b1, a review, 2026-11-02): safe. Only calls ffmpeg/ffplay as subprocesses (`moviepy/tools.py:27`; `video/io/ffmpeg_tools.py:251`); no network or telemetry found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install moviepy` (README). Claude Code (local only): can assemble clips in scripts. Android: no.
