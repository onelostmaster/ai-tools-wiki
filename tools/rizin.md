# rizin

- **Type:** CLI
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://rizin.re
- **GitHub repo:** https://github.com/rizinorg/rizin @ f74c1d7 (LGPL-3.0)
- **Price:** Free, LGPL-3.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @f74c1d7, a review, 2026-11-02): safe. No phone-home found.

## Safe install

Safe install (fixes applied):
Windows: download rizin-windows-static-v0.9.1.zip from the official GitHub release v0.9.1 (2026-06-29), unzip to its own folder and add its bin folder to PATH for your user only. No phone-home found in the reviewed f74c1d7. Unverified: the release binaries -> contain: open only files you are allowed to analyse, and analyse unknown malware samples only inside a VM. Claude Code: can drive the rizin CLI once it is on PATH. Android: official android-aarch64 tarball exists, but use it only under Termux on a test device. claude.ai, Hermes: no.

## YOLO install

YOLO (your own risk): skips the per-user PATH and the VM for unknown samples.
Unzip the latest Windows release and run rizin.exe.

## Install notes

Safe, but ask the user before installing.
Windows: official installer from rizin.re or GitHub releases. Android: no.
