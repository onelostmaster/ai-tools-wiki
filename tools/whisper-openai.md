# Whisper (OpenAI)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://openai.com/index/whisper/
- **GitHub repo:** [https://github.com/openai/whisper](https://github.com/openai/whisper) (listed on PyPI as openai-whisper's homepage, checked 2026-10-31)
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Whisper (official vendor, OpenAI; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Open-source speech-recognition model and Python package (`openai-whisper`, MIT per PyPI) that runs locally and needs the ffmpeg command-line tool. No risks recorded.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): python -m venv whisper-env, activate it, then pip install openai-whisper==<the version PyPI shows today> (pinned, inside the venv) and winget install Gyan.FFmpeg for the ffmpeg command-line tool it needs. Runs locally; no key.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install -U openai-whisper (PyPI) into your main Python, plus ffmpeg.

## Install notes

Claude Code: `pip install -U openai-whisper` (PyPI); it also needs the ffmpeg command-line tool (see the ffmpeg row).
