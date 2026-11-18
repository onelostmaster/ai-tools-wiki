# Arize Phoenix

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/Arize-ai/phoenix
- **GitHub repo:** https://github.com/Arize-ai/phoenix @ e3ba11f (Elastic License 2.0, source-available)
- **Price:** Free to self-host; hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @8b409d4 v21.1.0 (2026-11-17): safe with fixes. Source-available (Elastic License 2.0). The web UI loads a Scarf.sh pixel with a built-in ID (src/phoenix/config.py:3842; server/templates/index.html:156); PHOENIX_TELEMETRY_ENABLED=false turns off Scarf and FullStory (config.py:164-168). Non-loopback hosts turn on auth unless PHOENIX_ENABLE_AUTH says otherwise (config.py:58). Fix: telemetry off.

## Safe install

Safe install (fixes applied):
Own venv; pip install arize-phoenix==21.1.0; env PHOENIX_TELEMETRY_ENABLED=false; keep the default loopback host or leave auth on.

## YOLO install

YOLO (your own risk): skips telemetry off and the pin.
pip install -U arize-phoenix with the pixel on.

## Install notes

Ask the user before installing.
Windows: pip or Docker (not tested). Android: dashboard in a phone browser once hosted.
