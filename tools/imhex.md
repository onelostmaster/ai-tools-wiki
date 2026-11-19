# ImHex

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://imhex.werwolv.net
- **GitHub repo:** https://github.com/WerWolv/ImHex @ 34483cb (GPL-2.0)
- **Price:** Free, GPL-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @34483cb, a review, 2026-11-02): caution. If you allow server contact it sends anonymous stats (uuid, version, OS, GPU) (init_tasks.cpp:53-75); it asks at first start (settings_entries.cpp:46-48), so say no. Crash-log upload is on by default (settings_entries.cpp:755). DO_NOT_TRACK=1 turns it off (imhex_api.cpp:1136-1146). Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (DO_NOT_TRACK=1 set before first start, No to server contact at first start, crash-log upload confirmed off); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: official installer from imhex.werwolv.net or the GitHub release matching 34483cb. Set the user env var DO_NOT_TRACK=1 before first start, which turns off stats and crash upload (imhex_api.cpp:1136-1146); also answer No to server contact at first start (settings_entries.cpp:46-48) and confirm crash-log upload is off in Settings (on by default, settings_entries.cpp:755). Android: no.

## YOLO install

YOLO (your own risk): skips the DO_NOT_TRACK switch and the crash-upload check.
Windows: latest installer with defaults; crash-log upload stays on (settings_entries.cpp:755).

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: official installer from imhex.werwolv.net or GitHub; say no to server contact and turn off crash upload. Android: no.
