# MoviePy

- **Type:** library
- **Category:** editing
- **Official URL:** https://github.com/Zulko/moviepy
- **GitHub repo:** https://github.com/Zulko/moviepy @ 211e4b1 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @211e4b1, a review, 2026-11-02): safe. Only calls ffmpeg/ffplay as subprocesses (`moviepy/tools.py:27`; `video/io/ffmpeg_tools.py:251`); no network or telemetry found.

## Safe install

Safe install (fixes applied):
Windows (Python, git): make a venv, then `pip install "moviepy @ git+https://github.com/Zulko/moviepy@211e4b1"` (the reviewed commit; the newest PyPI release 2.2.1 from 2025-05-21 is 97 commits older and not what was reviewed). It uses the FFmpeg that imageio_ffmpeg provides unless FFMPEG_BINARY is set (moviepy/config.py:18,38-41). On import it loads the nearest .env file it finds from the working folder upward (moviepy/config.py:11-14), and a FFMPEG_BINARY or FFPLAY_BINARY line there picks the program it runs; fix: run it from your own project folder and set FFMPEG_BINARY yourself, or check any .env above that folder first. Claude Code (local only): Claude can write and run MoviePy scripts in that venv. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin (gets PyPI 2.2.1, older than the review) and the venv.
pip install moviepy

## Install notes

Safe, but ask the user before installing.
Windows: `pip install moviepy` (README). Claude Code (local only): can assemble clips in scripts. Android: no.
