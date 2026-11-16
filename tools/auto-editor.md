# Auto-Editor

- **Type:** CLI
- **Category:** editing
- **Official URL:** https://auto-editor.com
- **GitHub repo:** https://github.com/WyattBlue/auto-editor @ 5ad05f9 (Unlicense, public domain)
- **Price:** Free CLI, Unlicense (github.com, checked 2026-11-02); hosted online/desktop app price unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @5ad05f9, a review, 2026-11-02): safe. Nim program; no network calls, update check or telemetry found. The separate online app and desktop app at app.auto-editor.com use proprietary assets (`README.md:115`), not reviewed.

## Safe install

Safe install (fixes applied):
Windows: download auto-editor-windows-x86_64.exe (or -aarch64.exe on ARM) from the official GitHub release 31.8.0 (2026-10-30, github.com/WyattBlue/auto-editor/releases); no installer, no admin. The review is of 5ad05f9 (2026-11-02), 29 commits after 31.8.0 and before 31.9.0 (2026-11-13). Unverified: the prebuilt 31.8.0 binary. Contain it: run it on copies of your videos and block its internet with a Windows Firewall outbound rule (admin): `netsh advfirewall firewall add rule name="auto-editor" dir=out action=block program="<full path>\auto-editor-windows-x86_64.exe"`; it needs no internet to cut video. The whisper command uses a model file you download yourself from Hugging Face (src/cmds/whisper.nim:75-76). Skip the online app and desktop app at app.auto-editor.com (proprietary, README.md:115, not reviewed). Skip `npx skills add WyattBlue/auto-editor` (README.md:24) until its skills folder is reviewed. Claude Code (local only): Claude can call the exe for rough cuts. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the firewall block and the review gap; gets the newest release and its skills.
Latest auto-editor-windows-x86_64.exe from the releases page, then npx skills add WyattBlue/auto-editor

## Install notes

Safe, but ask the user before installing.
Windows: official release exe; see Safe install. Claude Code (local only): can script rough cuts. Android: no.
