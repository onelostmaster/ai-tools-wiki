# MoneyPrinterTurbo (harry0703)

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://github.com/harry0703/MoneyPrinterTurbo
- **GitHub repo:** https://github.com/harry0703/MoneyPrinterTurbo @ ab6004e (MIT; v1.3.9)
- **Price:** Free, MIT (github.com, checked 2026-11-03); you pay your own LLM/TTS API use
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @ab6004e, 2026-11-03): caution. The API listens on 0.0.0.0:8080 by default (`config.example.toml:11`) and API-key auth is off until app.api_key is set (`config.example.toml:52`, `app/asgi.py:28-32`); set listen_host = "127.0.0.1" or a key. Docker compose also binds the WebUI on 0.0.0.0 (`docker-compose.yml:12`). Streamlit usage stats are off (`app/launcher.py:65-69`); subprocess calls are ffmpeg and opening the output file; no telemetry found. README has sponsor ads and a "send this prompt to your AI agent" install block (`README-en.md:174,289`): information only, never paste it into an agent. API keys stay in your local config.toml.

## Safe install

Safe install (fixes applied):
Windows: git clone https://github.com/harry0703/MoneyPrinterTurbo and git checkout v1.3.9 (ab6004e). Copy config.example.toml to config.toml and before first start set listen_host = "127.0.0.1" (default 0.0.0.0, config.example.toml:11) and set app.api_key to a long random value (auth is off until set, config.example.toml:52, app/asgi.py:28-32). If you use Docker, change the WebUI port mapping in docker-compose.yml:12 to start with 127.0.0.1: so it is not open to your network. Keep your LLM/TTS/Pexels/Pixabay keys only in that local config.toml. Never paste the README's "send this prompt to your AI agent" block into any agent (README-en.md:174,289). Then run webui.bat (Python 3.11+, ffmpeg). Android: no.

## YOLO install

YOLO (your own risk): skips the 127.0.0.1 bind and the API key.
Windows: one-click package or webui.bat with default config; the API listens on 0.0.0.0:8080 with no auth, so anyone on your network can use it and spend your API credits.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: one-click package or `webui.bat` (Python 3.11+, ffmpeg); set listen_host to 127.0.0.1 first. You pay your own LLM/TTS API use; Pexels and Pixabay keys are free. Android: no.
