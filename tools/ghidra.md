# Ghidra

- **Type:** app
- **Category:** security, developer tools, 3D and games
- **Official URL:** https://github.com/NationalSecurityAgency/ghidra
- **GitHub repo:** https://github.com/NationalSecurityAgency/ghidra @ 251f360 (release 12.2, 2026-10-22; Apache-2.0)
- **Price:** Free, Apache-2.0 (`LICENSE`, github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read of launch scripts @251f360, a review, 2026-11-02): safe. No telemetry or auto-update found in `Ghidra/RuntimeScripts`. Its README warns some old versions have known vulnerabilities (`README.md:23-26`), so use the current 12.2 release (needs JDK 25). A binary you analyse is untrusted input.

## Safe install

Safe install (fixes applied):
Windows: install a 64-bit JDK 25, download ghidra_12.2_PUBLIC_20261016.zip (release Ghidra_12.2_build, reviewed commit 251f360) from github.com/NationalSecurityAgency/ghidra/releases, check its SHA-256 against the one on the release page, unzip to a user folder and run ghidraRun.bat. Fix: use 12.2, not an old version (README.md:23-26 warns old versions have known vulnerabilities). Open untrusted binaries only in a VM. Only analyse software you own or may analyse.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: install JDK 25 64-bit, download the official release zip from https://github.com/NationalSecurityAgency/ghidra/releases, unzip and run `ghidraRun.bat` (README). Only reverse-engineer software you own or are allowed to.
