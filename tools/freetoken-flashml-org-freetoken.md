# FreeToken (FlashML-org/FreeToken)

- **Type:** app
- **Category:** developer tools, Hermes add-ons, 3D and games
- **Official URL:** https://github.com/FlashML-org/FreeToken
- **GitHub repo:** https://github.com/FlashML-org/FreeToken @ 3d23551 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); desktop app price unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @548f97f v0.2.2 (2026-11-17): safe with fixes. The launcher offers vendor curl|bash installers for agents (python/freetoken/launch.py:93-115) but shows the command and asks y/n, and refuses without a terminal (:967-984). Control plane binds 127.0.0.1 (daemon/server.py:48); admin stop is loopback-only (server/accounting.py:138-146). No telemetry. The flashml.ai desktop app is not in the repo.

## Safe install

Safe install (fixes applied):
Own venv; uv pip install "freetoken[accel]==0.2.2"; answer n to every agent-install prompt and install agents from their own docs; skip the flashml.ai desktop app; Hermes: point at its local endpoint.

## YOLO install

YOLO (your own risk): skips the pin and the n answers.
Let the launcher run the vendor installers and use the desktop app.

## Install notes

Ask the user before installing.
Windows: desktop app from flashml.ai (not reviewed) or the CLI per its README; needs an NVIDIA RTX 30/40/50 GPU. Never let it run vendor installers unasked.
Hermes: point Hermes at its local endpoint.
Android: no.
