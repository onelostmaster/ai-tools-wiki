# GameForge plugin

- **Type:** plugin
- **Category:** Hermes add-ons, 3D and games
- **Official URL:** https://github.com/DECRUX9812/hermes-plugin-gameforge
- **GitHub repo:** [https://github.com/DECRUX9812/hermes-plugin-gameforge](https://github.com/DECRUX9812/hermes-plugin-gameforge)
- **Price:** Free code; optional paid ElevenLabs/Tripo/fal/Meshy APIs (not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a project a review): Looks safe. Subprocess only for ffmpeg/blender/godot/unity/butler; asks before Blender scripts and itch publish; keys via scoped secrets; network only to optional ElevenLabs/Tripo/fal/Meshy APIs and Godot templates with a SHA512 check.

## Safe install

Safe install (fixes applied):
Hermes: hermes plugins install DECRUX9812/hermes-plugin-gameforge --enable (README:14). Optional ElevenLabs/Tripo/fal/Meshy keys go in its scoped secrets, never in chat. Keep its confirm prompts on: it asks before running Blender scripts and before itch.io publish . Godot templates are SHA512-checked.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install DECRUX9812/hermes-plugin-gameforge --enable` (README:14). Optional ElevenLabs/Tripo/fal/Meshy keys go in its scoped secrets; never paste keys into chat.
