# Terrain3D (TokisanGames)

- **Type:** plugin
- **Category:** 3D and games
- **Official URL:** https://github.com/TokisanGames/Terrain3D
- **GitHub repo:** https://github.com/TokisanGames/Terrain3D @ 852b6c9 (MIT, LICENSE.txt; C++ GDExtension + GDScript editor addon)
- **Price:** Free, MIT (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @852b6c9, 2026-11-03): safe. No network, HTTPRequest or OS.execute calls found in src/ or project/addons/terrain_3d; godot-cpp is a submodule (.gitmodules). Prebuilt release binaries were not reviewed.

## Safe install

Safe install (fixes applied):
Windows: in Godot 4, download Terrain3D_v1.1.0-stable.zip from the official GitHub release (github.com/TokisanGames/Terrain3D/releases) or the Godot Asset Library and copy addons/terrain_3d into your project. The source has no network or OS.execute calls (review @852b6c9). Unverified: the prebuilt GDExtension DLLs in the release zip, and v1.1.0-stable is on a release branch that diverged from the reviewed commit (GitHub compare: 10 ahead, 21 behind). Contain it: commit your project to git first and try it in a copy of the project. Android: only as a Godot export target. Not a Claude or Hermes tool.

## YOLO install

YOLO (your own risk): skips the project backup.
Install Terrain3D from the Godot Asset Library into your main project.

## Install notes

Safe, but ask the user before installing.
Windows: Godot 4 editor plugin from the official GitHub releases or Godot Asset Library. Android: only as a Godot export target, not reviewed. Not a Claude or Hermes tool.
