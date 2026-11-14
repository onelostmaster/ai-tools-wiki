# WhisperX

- **Type:** library
- **Category:** voice and audio, editing, video analysis
- **Official URL:** https://github.com/m-bain/whisperX
- **GitHub repo:** https://github.com/m-bain/whisperX @ 5d3678b (BSD-2-Clause) · diarization via pyannote/pyannote-audio @ cc679dc
- **Price:** Free, BSD-2-Clause (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @5d3678b + pyannote-audio @cc679dc, a review, 2026-11-02): caution. Speaker labels use pyannote-audio 4 (`pyproject.toml:18`), which sends usage events (model name, version, session ID) to `otel.pyannote.ai` by default (`telemetry/config.yaml`; `metrics.py:49,57-75,150-151`); off with PYANNOTE_METRICS_ENABLED=0. Diarization needs a Hugging Face token (`transcribe.py:212-214`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install whisperx` (README; CUDA toolkit 12.8 for GPU); set PYANNOTE_METRICS_ENABLED=0; keep the HF token in an env variable. Claude Code (local only): can script it for subtitles. Android: no.
