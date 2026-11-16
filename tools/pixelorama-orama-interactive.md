# Pixelorama (Orama-Interactive)

- **Type:** app
- **Category:** 3D and games, design
- **Official URL:** https://www.pixelorama.org
- **GitHub repo:** https://github.com/Orama-Interactive/Pixelorama @ f3cb9ab (MIT; v1.2.4)
- **Price:** Free, MIT (github.com, checked 2026-11-03); optional paid Steam build supports the devs
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @f3cb9ab, 2026-11-03): safe. No telemetry or auto-updater found. Network only when you import a Lospec palette (`src/Autoload/Palettes.gd:758-764`), confirm an image download from a URL (`src/Main.gd:754-755`) or browse the extension store, which reads the official PixeloramaExtensionRepository list (`src/UI/ExtensionExplorer/ExtensionExplorer.gd:9`) and downloads .pck files (`Entry/ExtensionEntry.gd:20,89`). Extensions load as full-access Godot packs (`src/HandleExtensions.gd:119`), so install only known ones. Slider math uses Godot Expression on your own input (`src/UI/Nodes/Sliders/ValueSlider.gd:295-300`), local only.

## Safe install

Safe install (fixes applied):
Windows: download Pixelorama_v1.2.4_setup.exe or Pixelorama-Windows-64bit.zip from the official GitHub release v1.2.4 (github.com/Orama-Interactive/Pixelorama/releases), or `winget install pixelorama`. Android: install Pixelorama.apk from the same official v1.2.4 release (sideload; allow unknown sources for your browser only while installing). There is no auto-updater or telemetry. Network use happens only when you import a Lospec palette, download an image from a URL, or open the extension store; extensions run as full-access Godot packs (src/HandleExtensions.gd:119), so install none, or only ones you trust. Not a Claude or Hermes tool.

## YOLO install

YOLO (your own risk): skips the extension restriction.
winget install pixelorama

## Install notes

Safe, but ask the user before installing.
Windows: GitHub releases, itch.io, Steam or winget install pixelorama; also runs in the browser. Video export uses your own ffmpeg. Install only known extensions. Android: official Pixelorama.apk in the GitHub release v1.2.4 (release assets checked 2026-11-15); sideload it.
