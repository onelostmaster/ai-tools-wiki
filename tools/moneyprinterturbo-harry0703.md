# MoneyPrinterTurbo (harry0703)

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://github.com/harry0703/MoneyPrinterTurbo
- **GitHub repo:** https://github.com/harry0703/MoneyPrinterTurbo @ ab6004e (MIT; v1.3.9)
- **Price:** Free, MIT (github.com, checked 2026-11-03); you pay your own LLM/TTS API use
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @ab6004e, 2026-11-03): caution. The API listens on 0.0.0.0:8080 by default (`config.example.toml:11`) and API-key auth is off until app.api_key is set (`config.example.toml:52`, `app/asgi.py:28-32`); set listen_host = "127.0.0.1" or a key. Docker compose also binds the WebUI on 0.0.0.0 (`docker-compose.yml:12`). Streamlit usage stats are off (`app/launcher.py:65-69`); subprocess calls are ffmpeg and opening the output file; no telemetry found. README has sponsor ads and a "send this prompt to your AI agent" install block (`README-en.md:174,289`): information only, never paste it into an agent. API keys stay in your local config.toml.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: one-click package or `webui.bat` (Python 3.11+, ffmpeg); set listen_host to 127.0.0.1 first. You pay your own LLM/TTS API use; Pexels and Pixabay keys are free. Android: no.
