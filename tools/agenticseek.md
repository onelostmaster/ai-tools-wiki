# AgenticSeek

- **Type:** app
- **Category:** automation, research
- **Official URL:** http://agenticseek.tech
- **GitHub repo:** https://github.com/Fosowl/agenticSeek @ 4f5f924 (GPL-3.0)
- **Price:** Free, open source (GPL-3.0) (github.com, checked 2026-11-01); needs a 12-24 GB VRAM GPU
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @4f5f924 (2026-11-14): safe with fixes, Skip (Hermes covers it). Model-written shell runs with shell=True (sources/tools/BashInterpreter.py:63), so run only the Docker backend: agent code runs as uid 1000 with write access only to WORK_DIR and /tmp, the API is on 127.0.0.1 only and loopback is blocked for agent code (docker-compose.yml:76-90). Outside Docker (not root) there is no privilege drop (sources/tools/sandbox.py:53-55).

## Safe install

Safe install (fixes applied):
Docker only: docker compose --profile full up with WORK_DIR set to a new empty folder; keep the 127.0.0.1 port line; never run it outside Docker; keep API keys out of WORK_DIR.

## YOLO install

YOLO (your own risk): skips Docker, so model-written shell runs as you.
python3 cli.py on the host with WORK_DIR set to your files.

## Install notes

Ask the user before installing. Docker only: docker compose --profile full up with WORK_DIR set to a new empty folder; keep the 127.0.0.1 port line; never run it outside Docker; keep API keys out of WORK_DIR.
