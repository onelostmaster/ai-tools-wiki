# AgenticSeek

- **Type:** app
- **Category:** automation, research
- **Official URL:** http://agenticseek.tech
- **GitHub repo:** https://github.com/Fosowl/agenticSeek @ 4f5f924 (GPL-3.0)
- **Price:** Free, open source (GPL-3.0) (github.com, checked 2026-11-01); needs a 12-24 GB VRAM GPU
- **Decision:** Avoid
- **Safety verdict:** avoid
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

Claude : avoid. Rests on code lines already logged by a review bot (@4f5f924, 2026-11-01): model-written shell runs with shell=True (`BashInterpreter.py:61-68`); privilege drop only as root on Linux/Docker (`sandbox.py:55-56`); its own blocklist says it is not a security boundary (`safety.py:4-7`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Do not install: flagged avoid (see Safety reason).
