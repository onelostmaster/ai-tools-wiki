# MelonLoader (LavaGang)

- **Type:** app
- **Category:** 3D and games
- **Official URL:** https://github.com/LavaGang/MelonLoader
- **GitHub repo:** https://github.com/LavaGang/MelonLoader @ 5aff4d9 (Apache-2.0; v0.7.4; installer LavaGang/MelonLoader.Installer)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @5aff4d9, 2026-11-03): caution. On first run for Il2Cpp games it sends the game name to api.melonloader.com for Unity version info (`Dependencies/Il2CppAssemblyGenerator/RemoteAPI.cs:72-76,139-141`), downloads Cpp2IL and Unity dependencies from GitHub releases (`Packages/Cpp2IL.cs:47`, `Packages/UnityDependencies.cs:11`) and runs them as child processes (`Packages/Models/ExecutablePackage.cs:54-60`). On Windows it can download and silently run the .NET 6 runtime installer from aka.ms (`MelonLoader.Bootstrap/RuntimeHandlers/Dotnet/DotnetInstaller.cs:10,60`). Every mod runs with full user permissions. No other telemetry found.

## Safe install

Safe install (fixes applied):
Windows: get MelonLoader.Installer from the official LavaGang/MelonLoader.Installer releases and install MelonLoader v0.7.4 (the reviewed 5aff4d9), not the newest. Use it only on single-player or offline games (anti-cheat bans modded clients) and only add mods from their own official pages; every mod runs with your full user rights (no sandbox exists for this). This will happen on the first launch of an Il2Cpp game and cannot be turned off because the loader needs it: it sends the game name to api.melonloader.com (RemoteAPI.cs:72-76,139-141), downloads Cpp2IL and Unity dependencies from GitHub releases and runs them (Packages/Cpp2IL.cs:47, ExecutablePackage.cs:54-60). Install the .NET 6 runtime yourself from Microsoft first so you choose that install instead of the loader fetching it from aka.ms (DotnetInstaller.cs:10,60). Android: no (upstream WIP, README.md:43-44).

## YOLO install

YOLO (your own risk): skips the version pin, the self-installed .NET 6 and the mod-source rule.
Windows: latest MelonLoader.Installer .exe, pick the game folder, add any mods; the loader downloads and silently runs the .NET 6 installer itself if needed.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: MelonLoader.Installer .exe, pick the game folder. Only use mods from known sources, and only on single-player or offline games (anti-cheat may ban modded clients). Android: WIP upstream (`README.md:43-44`), not usable yet.
