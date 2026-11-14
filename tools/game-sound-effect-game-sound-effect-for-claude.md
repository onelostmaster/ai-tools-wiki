# Game-Sound-Effect (Game-Sound-Effect-for-Claude)

- **Type:** plugin
- **Category:** voice and audio, 3D and games
- **Official URL:** https://github.com/GhazaGG/Game-Sound-Effect-for-Claude
- **GitHub repo:** https://github.com/GhazaGG/Game-Sound-Effect-for-Claude @ 0f287ed (2026-10-29, still HEAD on 2026-11-02; plugin game-sfx 0.1.0; MIT; the scout gave only the name "Game-Sound-Effect"; matched by a GitHub search on 2026-10-31, the only Claude skill by that name)
- **Price:** Free (MIT, github.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @0f287ed, game-sfx 0.1.0, 2026-11-02, no-intake review): Looks safe. Pure stdlib Python, no hooks, MCP or install scripts, no eval or shell. Only network use: scripts/freesound.py:19-59 calls freesound.org with your FREESOUND_API_KEY (also read from the Windows user registry, line 26) and downloads CC0 previews. doctor.py:24-28 runs ffprobe/ffmpeg with argument lists. No telemetry.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add GhazaGG/Game-Sound-Effect-for-Claude` then `/plugin install game-sfx@game-sfx` (README).
Windows: needs Python 3.8+; the synth uses only the standard library and works offline. The sample pipeline (`freesound.py`) also needs `ffmpeg` and a free Freesound key in the `FREESOUND_API_KEY` environment variable; set it yourself, never paste it into chat.
