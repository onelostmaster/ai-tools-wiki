# BepInEx

- **Type:** app
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/BepInEx/BepInEx
- **GitHub repo:** https://github.com/BepInEx/BepInEx @ b782da4 (LGPL-2.1; last commit 2026-10-23)
- **Price:** Free, LGPL-2.1 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-04

## Safety reason

a review bot (light code read @b782da4, a review, 2026-11-02): safe. No telemetry or analytics found. For IL2CPP games it downloads Unity base libraries from the official BepInEx host, configurable or skippable (`Runtimes/Unity/BepInEx.Unity.IL2CPP/Il2CppInteropManager.cs:57-64`, download `:295-310`). Only Process.Start is a Linux notify-send call (`Runtimes/Unity/BepInEx.Unity.IL2CPP/Utils/NotifySend.cs:46`). Every plugin DLL you add runs with full rights: trusted plugins only, single-player or offline games only (online anti-cheat can ban).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: official release zip from GitHub (5.x stable; 6 is bleeding edge) unpacked into the game folder, per its docs (not tested). Claude Code can write plugins.
Android: no.
