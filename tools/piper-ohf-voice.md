# Piper (OHF-Voice)

- **Type:** CLI
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/OHF-Voice/piper1-gpl
- **GitHub repo:** https://github.com/OHF-Voice/piper1-gpl
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @304d5da (2026-11-19): safe with fixes. Local TTS; voices download from the official Hugging Face repo (src/piper/download_voices.py:14-16). The only exposure is the optional web server's default host 0.0.0.0 (src/piper/http_server.py:24), fixed by --host 127.0.0.1. The maintainer call (README.md:22-24) is not a risk; commits continue (46c3c71, 2026-11-17). Fix: venv, pin 1.8.0, 127.0.0.1.

## Safe install

Safe install (fixes applied):
Windows: in a fresh venv pip install piper-tts==1.8.0 (README.md:8), then python -m piper.download_voices en_US-lessac-medium (docs/CLI.md:24; downloads from the official Hugging Face voices repo, download_voices.py:14-16) and python -m piper -m en_US-lessac-medium -f test.wav -- "This is a test." (docs/CLI.md:34). Use the CLI. If you need the web server, always start it as python -m piper.http_server --host 127.0.0.1 -m en_US-lessac-medium: the default host is 0.0.0.0, which exposes it to your network (http_server.py:24). Check each voice's license on its model card before publishing audio. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the venv, version pin and 127.0.0.1 binding.
pip install piper-tts && python -m piper.http_server -m en_US-lessac-medium

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
