# WhisperX

- **Type:** library
- **Category:** voice and audio, editing, video analysis
- **Official URL:** https://github.com/m-bain/whisperX
- **GitHub repo:** https://github.com/m-bain/whisperX @ 5d3678b (BSD-2-Clause) · diarization via pyannote/pyannote-audio @ cc679dc
- **Price:** Free, BSD-2-Clause (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @5d3678b + pyannote-audio @cc679dc, a review, 2026-11-02): caution. Speaker labels use pyannote-audio 4 (pyproject.toml:18), which sends usage events (model name, version, session ID) to otel.pyannote.ai by default (telemetry/config.yaml; metrics.py:49,57-75,150-151); off with PYANNOTE_METRICS_ENABLED=0. Diarization needs a Hugging Face token (transcribe.py:212-214). Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (PYANNOTE_METRICS_ENABLED=0 set before first run, read-only HF token in HF_TOKEN env var); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install whisperx==<release matching 5d3678b> (CUDA toolkit 12.8 for GPU). Before the first run set the user env var PYANNOTE_METRICS_ENABLED=0; otherwise every diarization run sends model name, version and a session ID to otel.pyannote.ai (pyannote-audio telemetry/config.yaml; metrics.py:49,57-75,150-151). Speaker labels need a Hugging Face token (transcribe.py:212-214): create a read-only token and keep it in the HF_TOKEN env var, never in a script or chat. Claude Code (local only): can script it for subtitles. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and PYANNOTE_METRICS_ENABLED=0.
Windows: pip install whisperx; diarization runs send usage events to otel.pyannote.ai.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: pip install whisperx (README; CUDA toolkit 12.8 for GPU); set PYANNOTE_METRICS_ENABLED=0; keep the HF token in an env variable. Claude Code (local only): can script it for subtitles. Android: no.
