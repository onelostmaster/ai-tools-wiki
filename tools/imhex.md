# ImHex

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://imhex.werwolv.net
- **GitHub repo:** https://github.com/WerWolv/ImHex @ 34483cb (GPL-2.0)
- **Price:** Free, GPL-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @34483cb, a review, 2026-11-02): caution. If you allow server contact it sends anonymous stats (uuid, version, OS, GPU) (`init_tasks.cpp:53-75`); it asks at first start (`settings_entries.cpp:46-48`), so say no. Crash-log upload is on by default (`settings_entries.cpp:755`). DO_NOT_TRACK=1 turns it off (`imhex_api.cpp:1136-1146`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: official installer from imhex.werwolv.net or GitHub; say no to server contact and turn off crash upload. Android: no.
