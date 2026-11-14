# radare2

- **Type:** CLI
- **Category:** security, developer tools, 3D and games
- **Official URL:** https://github.com/radareorg/radare2
- **GitHub repo:** https://github.com/radareorg/radare2 @ 79f6d2a (release 6.2.4, 2026-10-05; LGPLv3)
- **Price:** Free, LGPLv3 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read @79f6d2a, a review, 2026-11-02): safe. The source install runs `sys/install.sh`, which asks for sudo to symlink system-wide (`sys/install.sh:7-29,87`); prefer the release build. r2pm plugins are third-party and unreviewed. No telemetry or curl|bash found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: download the Windows release zip (6.2.4) from https://github.com/radareorg/radare2/releases and add its bin folder to PATH (README).
Android: runs in Termux . Only reverse-engineer software you own or are allowed to.
