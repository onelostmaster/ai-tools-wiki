# dnSpy / dnSpyEx

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/dnSpy/dnSpy
- **GitHub repo:** https://github.com/dnSpyEx/dnSpy @ 6e8a26a (GPL-3.0)
- **Price:** Free, GPL-3.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @6e8a26a (2026-11-20): safe with fixes. dnSpyEx is the active fork (last commit 2026-11-18); release zips are built by its own GitHub Actions workflow (.github/workflows/build.yml:9-11,57-61), so provenance is traceable. The startup GitHub update check defaults on (dnSpy/dnSpy/MainApp/UpdateService.cs:93,146) and has a setting. Debugging runs the target. Fix: v6.6.0 zip, update check off, decompile only for untrusted files.

## Safe install

Safe install (fixes applied):
Windows: download the dnSpyEx v6.6.0 release zip (2026-06-20; the review read 6e8a26a, 15 commits later) from https://github.com/dnSpyEx/dnSpy/releases/tag/v6.6.0 and unzip it to a user folder. On first start untick Check for updates on startup in Settings (on by default, UpdateService.cs:93; it calls api.github.com, :146). Decompiling only reads a file; the debugger runs it, so debug untrusted assemblies only inside a VM. Android: no.

## YOLO install

YOLO (your own risk): skips the pinned release and the update-check switch.
Windows: latest dnSpyEx release zip; startup update check stays on.

## Install notes

Ask the user before installing.
Windows: dnSpyEx release from GitHub; turn off the update check. Android: no.
