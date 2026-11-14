# agent-video-editor

- **Type:** skill
- **Category:** editing
- **Official URL:** https://github.com/kmilo93sd/agent-video-editor
- **GitHub repo:** https://github.com/kmilo93sd/agent-video-editor @ 8e32c0a (MIT; committed 2026-10-04 14:10 ET per git log, still HEAD on 2026-11-03; plugin 2.0.0)
- **Price:** Free (MIT code; CC0 sounds and graphics, per LICENSE and LICENSES.md)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @8e32c0a, plugin 2.0.0, 2026-11-03, no-intake review): Looks safe. .claude-plugin/plugin.json and marketplace.json declare only the skill: no hooks, MCP servers or install scripts. Most of the repo is Markdown advice plus CC0 audio and HTML graphics. The Node helpers only call local ffmpeg/ffprobe/node with argument lists via execFileSync/spawnSync (library/verify.mjs:63-77, graphics/check.mjs:40, templates/edit-engine.mjs:30,97, record.example.mjs:91), no shell or eval. Network only in the opt-in tutorial templates: ElevenLabs text-to-speech (templates/gen-voice.mjs:64) and Google Gemini images (templates/gen-illustrations.mjs:49), with keys read from your .env (gen-voice.mjs:31-33; voice.md:69-79). Graphics preview loads pinned gsap 3.14.2 from jsDelivr (graphics/preview.html:7). No telemetry. SKILL.md:77 says nothing is rendered or published without your approval.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (works on Windows): `/plugin marketplace add kmilo93sd/agent-video-editor` then `/plugin install agent-video-editor@agent-video-editor` (README). Or by hand: copy `skills/editing-videos/` into `~/.claude/skills/` (on Windows `%USERPROFILE%\.claude\skills\`). The editing advice itself needs nothing. The search tools for the sound, graphics and meme kits need Node; the narrated screen tutorial templates need Node 20+, ffmpeg on the PATH, Playwright for recording, an ElevenLabs key for the voice, an optional Gemini key for illustrations, and HyperFrames for rendering. Put keys only in the project's `.env` file with Notepad, never in chat. The bundled sounds and graphics are CC0 (check each file's line in `library/LICENSES.md` before copying). Useful for the faceless AI video channel idea: pacing, hooks, captions, audio levels and a Shorts recipe.
