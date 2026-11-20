# MelonLoader (LavaGang)

- **Type:** app
- **Category:** 3D and games
- **Official URL:** https://github.com/LavaGang/MelonLoader
- **GitHub repo:** https://github.com/LavaGang/MelonLoader @ 5aff4d9 (Apache-2.0; v0.7.4; installer LavaGang/MelonLoader.Installer)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @5aff4d9 (2026-11-19): caution. Correction: the game-name call to api.melonloader.com has a switch, force_offline_generation = true in UserData/Loader.cfg [unityengine] or --melonloader.agfoffline (README.md:163-169). No fix: every mod runs with your full Windows user rights and MelonLoader has no mod sandbox; only a separate Windows account or VM contains it. Anti-cheat bans modded clients in online games.

## Safe install

Safe install (fixes applied):
Windows: get MelonLoader.Installer from the official LavaGang/MelonLoader.Installer releases and install MelonLoader v0.7.4 (the reviewed 5aff4d9), not the newest. Use it only on single-player or offline games (anti-cheat bans modded clients) and only add mods from their own official pages; every mod runs with your full user rights (no sandbox exists for this). After the first run creates UserData/Loader.cfg, set force_offline_generation = true under [unityengine] (or launch with --melonloader.agfoffline, README.md:163-169) so it stops sending the game name to api.melonloader.com (RemoteAPI.cs:72-76,139-141); it still downloads Cpp2IL and Unity dependencies from GitHub releases and runs them on Il2Cpp games (Packages/Cpp2IL.cs:47, ExecutablePackage.cs:54-60). Install the .NET 6 runtime yourself from Microsoft first so you choose that install instead of the loader fetching it from aka.ms (DotnetInstaller.cs:10,60). Android: no (upstream WIP, README.md:43-44).

## YOLO install

YOLO (your own risk): skips the version pin, the self-installed .NET 6 and the mod-source rule.
Windows: latest MelonLoader.Installer .exe, pick the game folder, add any mods; the loader downloads and silently runs the .NET 6 installer itself if needed.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: MelonLoader.Installer .exe, pick the game folder. Only use mods from known sources, and only on single-player or offline games (unverified: whether a given online game's anti-cheat bans modded clients; containment: never use it on online or multiplayer games). Android: WIP upstream (README.md:43-44), not usable yet.
