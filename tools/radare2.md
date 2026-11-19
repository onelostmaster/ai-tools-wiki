# radare2

- **Type:** CLI
- **Category:** security, developer tools, 3D and games
- **Official URL:** https://github.com/radareorg/radare2
- **GitHub repo:** https://github.com/radareorg/radare2 @ 79f6d2a (release 6.2.4, 2026-10-05; LGPLv3)
- **Price:** Free, LGPLv3 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @79f6d2a, a review, 2026-11-02): safe. The source install runs `sys/install.sh`, which asks for sudo to symlink system-wide (`sys/install.sh:7-29,87`); prefer the release build. r2pm plugins are third-party and unreviewed. No telemetry or curl|bash found.

## Safe install

Safe install (fixes applied):
Windows: download radare2-6.2.4-w64.zip (the reviewed release, commit 79f6d2a) from github.com/radareorg/radare2/releases, unzip to a user folder and add its bin folder to your user PATH. Fix: do not build from source with sys/install.sh, which asks for sudo and symlinks system-wide (sys/install.sh:7-29,87); do not add r2pm plugins (third-party, unreviewed). 6.2.6 (2026-11-05) is out but not reviewed.
Android: pkg install radare2 in Termux. Only analyse software you own or are allowed to analyse.

## YOLO install

YOLO (your own risk): skips the 6.2.4 pin and the no-r2pm rule.
Download the latest radare2-<version>-w64.zip (6.2.6 on 2026-11-16) and install r2pm plugins as you like.

## Install notes

Safe, but ask the user before installing.
Windows: download the Windows release zip (6.2.4) from https://github.com/radareorg/radare2/releases and add its bin folder to PATH (README).
Android: runs in Termux . Only reverse-engineer software you own or are allowed to.
