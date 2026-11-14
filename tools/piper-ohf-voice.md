# Piper (OHF-Voice)

- **Type:** CLI
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/OHF-Voice/piper1-gpl
- **GitHub repo:** https://github.com/OHF-Voice/piper1-gpl
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; OHF-Voice/piper1-gpl @304d5da. Local TTS after voice download (src/piper/download_voices.py:14-16,195 fetch Hugging Face). Optional HTTP server binds 0.0.0.0 by default (src/piper/http_server.py:24,398); use CLI or explicitly bind 127.0.0.1. Audio playback spawns ffplay (audio_playback.py:18). No telemetry found; voice model licenses vary. README:23 seeks maintainers.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
