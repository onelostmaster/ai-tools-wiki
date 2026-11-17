# Vane

- **Type:** app
- **Category:** research
- **Official URL:** https://github.com/ItzCrazyKns/Vane
- **GitHub repo:** https://github.com/ItzCrazyKns/Vane @ 348feca (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model APIs you connect may cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @348feca, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. No login; Docker publishes port 3000 to your network; weather widget sends your IP to freeipapi (`actions.ts:24-27`).

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop): docker run -d -p 127.0.0.1:3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest, then open http://localhost:3000. The latest image was built 2026-09-01 from the reviewed commit 348feca (repo HEAD on 2026-11-16). Fix: the 127.0.0.1 bind, because Vane has no login and the README command opens port 3000 to your network. The weather widget sends your IP address to freeipapi whenever it loads (actions.ts:24-27); this will happen with the widget on screen and no setting to stop it was confirmed.

## YOLO install

YOLO (your own risk): skips the localhost bind.
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest (README); anyone on your network can use it.

## Install notes

Windows (Docker): `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` (README). It has no login and port 3000 is open to your network.
