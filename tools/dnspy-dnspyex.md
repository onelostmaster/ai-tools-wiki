# dnSpy / dnSpyEx

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/dnSpy/dnSpy
- **GitHub repo:** https://github.com/dnSpyEx/dnSpy @ 6e8a26a (GPL-3.0)
- **Price:** Free, GPL-3.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @6e8a26a, a review, 2026-11-02): caution. The original dnSpy (Official URL) was archived on 2020-12-20; dnSpyEx is an unofficial GitHub fork. Startup update check on by default (`UpdateService.cs:93,146`).

## Safe install

Safe install (fixes applied):
Windows: download the dnSpyEx release zip for commit 6e8a26a's release from github.com/dnSpyEx/dnSpy/releases (unofficial fork; the original dnSpy was archived 2020-12-20), unzip to a user folder. On first start turn off the startup update check in Settings; otherwise it contacts GitHub at every start (UpdateService.cs:93,146). Open only files you trust in it. Android: no.

## YOLO install

YOLO (your own risk): skips the pinned release and the update-check switch.
Windows: latest dnSpyEx release zip; startup update check stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: dnSpyEx release from GitHub; turn off the update check. Android: no.
