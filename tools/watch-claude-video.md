# Watch (claude-video)

- **Type:** plugin
- **Category:** video analysis
- **Official URL:** https://github.com/bradautomates/claude-video
- **GitHub repo:** https://github.com/bradautomates/claude-video @ 03ceb42 (MIT; committed 2026-09-24 21:25 ET per git log, still HEAD on 2026-11-03; plugin watch 0.3.2)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); the Gemini engine uses your Google AI Studio key.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @03ceb42, plugin 0.3.2, 2026-11-03, no-intake review): Looks safe. hooks/hooks.json adds one SessionStart hook (timeout 5 s) that runs hooks/scripts/check-setup.sh, which only calls setup.py --check (setup.py:185-191, local binary check, no network). All subprocess calls use argument lists, no shell=True or eval (runtime.py:25-28, frames.py:457, download.py:42-70 yt-dlp). Network goes only where you choose: Gemini Files API upload then delete (gemini.py:20, 119-161), Groq or OpenAI transcription if you add their key (whisper.py:31-34), and the opt-in WhisperX setup (setup.py:239-263, pinned whisperx 3.8.6 and torch 2.8.0; uv via Astral's official installer). Browser cookies are passed to yt-dlp only if you ask (download.py:30-35). No telemetry. SKILL.md:128 treats video content as untrusted; SKILL.md:51 offers pasting API keys in chat (don't).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (works on Windows): `/plugin marketplace add bradautomates/claude-video` then `/plugin install watch@claude-video` (README); not for claude.ai chat. Windows: needs Python 3.10+, then `winget install --id Gyan.FFmpeg --exact`, `winget install --id yt-dlp.yt-dlp --exact` and `winget install --id DenoLand.Deno --exact` (setup.py prints these; it never runs winget itself). Pick the engine: `local` keeps everything on your PC (frames + captions, no key); `gemini` uploads the video to Google (deleted after the answer) and needs a free Gemini key. Put any key in `~/.config/watch/.env` yourself with Notepad; don't paste keys into chat even though SKILL.md offers that. The optional local WhisperX transcriber (`setup.py --install-whisperx`) downloads about 1.5 GB and, on Windows, installs uv with `irm https://astral.sh/uv/install.ps1 | iex` (Astral's official installer); Windows is marked untested. The plugin adds a SessionStart hook that only runs a 5-second offline setup check. Useful for the faceless AI video channel idea: let Claude watch reference videos and pull timestamps.
