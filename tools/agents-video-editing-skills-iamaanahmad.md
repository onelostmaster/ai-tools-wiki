# agents-video-editing-skills (iamaanahmad)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/iamaanahmad/agents-video-editing-skills
- **GitHub repo:** https://github.com/iamaanahmad/agents-video-editing-skills @ 981466b (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-27

## Safety reason

a review bot read @981466b: safe with these fixes. 14 Markdown skills (FFmpeg, Remotion, moviepy, captions, voiceover, export, QA) plus two small Python helpers that call ffmpeg/ffprobe with fixed argument lists (export_platforms.py:59 and :102, probe.py:24); the installers only copy files and make no web calls. Verified 1: both installers delete an existing folder with the same name in the target skills folder before copying (install.py:111-114, cli.mjs:118), so a skill of yours called ffmpeg-essentials, captions-subtitles and so on is replaced. Fix: run with --dry-run first and rename any clashing skill of yours. Verified 2: --rules writes a marked block into CLAUDE.md (install.py:31-32 and :96, cli.mjs:241); it replaces only its own block. Fix: leave out --rules if you don't want CLAUDE.md changed. Verified 3: the README's npx agents-video-editing-skills runs the newest npm release, not the reviewed commit. Fix: install from a clone at commit 981466b with python scripts/install.py (standard library only). Verified 4: the skills tell the agent to install unpinned packages when a task needs them (remotion-programmatic-video/SKILL.md:15 npx create-video@latest, screen-recording-demos/SKILL.md:22 pip install playwright, moviepy-python-video/SKILL.md:20), and the ElevenLabs example reads ELEVENLABS_API_KEY from the environment (voiceover-tts/SKILL.md:37). Fix: keep Claude Code's command permission prompts on, approve installs one by one with a pinned version, and set the key only in the session where you use TTS. Verified 5: export_platforms.py passes -y, so it overwrites same-named outputs (it refuses to overwrite the source, :94). Fix: export to an empty folder. MIT (LICENSE).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Python 3.9+): git clone https://github.com/iamaanahmad/agents-video-editing-skills ; cd agents-video-editing-skills ; git checkout 981466bde5d5044d08cb5af391770bfd16f9c4e4 ; python scripts/install.py --agent claude --scope user --dry-run , rename any of your skills with the same names, then python scripts/install.py --agent claude --scope user (add --rules only if you want a block in CLAUDE.md). Keep command permission prompts on and approve each package install with a pinned version; set ELEVENLABS_API_KEY only in the session that needs it; export to an empty folder.
claude.ai, Hermes, Android: not supported by the README installers (no target for them).

## YOLO install

YOLO (your own risk): skips the pinned commit, the dry run and the permission-prompt and key rules. README: npx agents-video-editing-skills --agent claude --rules

## Install notes

Safe with fixes: install from a clone at commit 981466b with python scripts/install.py (not npx, which takes the newest release); dry-run first, because it replaces same-named skill folders; --rules edits CLAUDE.md, so leave it out if unwanted; approve the packages skills ask to install one by one. No keys needed except optional ElevenLabs TTS. Fits the faceless video channel: FFmpeg, Remotion, captions, voiceover and vertical Shorts playbooks.
