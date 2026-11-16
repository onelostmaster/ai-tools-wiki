# BepInEx

- **Type:** app
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/BepInEx/BepInEx
- **GitHub repo:** https://github.com/BepInEx/BepInEx @ b782da4 (LGPL-2.1; last commit 2026-10-23)
- **Price:** Free, LGPL-2.1 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @b782da4, a review, 2026-11-02): safe. No telemetry or analytics found. For IL2CPP games it downloads Unity base libraries from the official BepInEx host, configurable or skippable (`Runtimes/Unity/BepInEx.Unity.IL2CPP/Il2CppInteropManager.cs:57-64`, download `:295-310`). Only Process.Start is a Linux notify-send call (`Runtimes/Unity/BepInEx.Unity.IL2CPP/Utils/NotifySend.cs:46`). Every plugin DLL you add runs with full rights: trusted plugins only, single-player or offline games only (online anti-cheat can ban).

## Safe install

Safe install (fixes applied):
Windows: download BepInEx_win_x64_5.4.23.6.zip (or win_x86 for 32-bit games) from the official GitHub release v5.4.23.6 (2026-10-23), make a backup copy of the game folder, then unzip into the game folder next to the game .exe and start the game once to create the config. Unverified: the 5.x release binaries (the reviewed b782da4 is the 6.x master branch) -> contain: backup copy of the game folder, single-player or offline games only (online anti-cheat bans modded clients), and add only plugin DLLs you trust or wrote yourself, since every plugin runs with full rights. For IL2CPP games (6.x only) it downloads Unity base libraries from the official BepInEx host (Runtimes/Unity/BepInEx.Unity.IL2CPP/Il2CppInteropManager.cs:57-64). Claude Code can write the C# plugins. Android: no.

## YOLO install

YOLO (your own risk): skips the game-folder backup and uses the 6.x bleeding-edge build (6.0.0-pre.2 or nightly), unreviewed.
Unzip the 6.x build for your game type into the game folder.

## Install notes

Safe, but ask the user before installing.
Windows: official release zip from GitHub (5.x stable; 6 is bleeding edge) unpacked into the game folder, per its docs (not tested). Claude Code can write plugins.
Android: no.
