# Whisper (OpenAI)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://openai.com/index/whisper/
- **GitHub repo:** [https://github.com/openai/whisper](https://github.com/openai/whisper) (listed on PyPI as openai-whisper's homepage, checked 2026-10-31)
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

Whisper (official vendor, OpenAI; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Open-source speech-recognition model and Python package (`openai-whisper`, MIT per PyPI) that runs locally and needs the ffmpeg command-line tool. No risks recorded.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install -U openai-whisper` (PyPI); it also needs the ffmpeg command-line tool (see the ffmpeg row).
