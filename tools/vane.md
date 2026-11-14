# Vane

- **Type:** app
- **Category:** research
- **Official URL:** https://github.com/ItzCrazyKns/Vane
- **GitHub repo:** https://github.com/ItzCrazyKns/Vane @ 348feca (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model APIs you connect may cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (pattern scan plus targeted reads @348feca, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. No login; Docker publishes port 3000 to your network; weather widget sends your IP to freeipapi (`actions.ts:24-27`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows (Docker): `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` (README). It has no login and port 3000 is open to your network.
