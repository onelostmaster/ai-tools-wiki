# Handy

- **Type:** app
- **Category:** voice and audio, Notion and productivity
- **Official URL:** https://handy.computer
- **GitHub repo:** https://github.com/cjpais/Handy @ 0ed36e1 (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @0ed36e1, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. Signed updater (`tauri.conf.json:86`); update checks on (`settings.rs:596`); models SHA-256 checked.

## Safe install

Safe install (fixes applied):
Windows: download Handy_0.9.8_x64-setup.exe (or the .msi) from github.com/cjpais/Handy/releases/tag/v0.9.8 and run it. The reviewed commit 0ed36e1 is 32 commits after v0.9.8 and 27 before v0.10.0, so no release matches it exactly; v0.9.8 is the newest release before it (v0.10.0 of 2026-11-02 and v0.10.1 of 2026-11-14 are not reviewed). Update checks are on by default (src-tauri/src/settings.rs:596) and will offer the newer versions; to stay on v0.9.8, turn update checks off in its settings or set the environment variable HANDY_DISABLE_UPDATER=1 (settings.rs:1378-1388). Updates it does install are signature-checked (tauri.conf.json:86). Speech models download on first use with SHA-256 checks.

## YOLO install

YOLO (your own risk): skips the v0.9.8 pin and turning update checks off.
winget install cjpais.Handy (README), which gets the latest release, and let it update itself.

## Install notes

Windows: `winget install cjpais.Handy` or the release installer (README).
