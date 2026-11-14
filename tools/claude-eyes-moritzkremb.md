# claude-eyes (moritzkremb)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/moritzkremb/claude-eyes
- **GitHub repo:** https://github.com/moritzkremb/claude-eyes @ a540961 (0.2.0; MIT; committed 2026-10-16 10:11 ET, still HEAD on 2026-11-09)
- **Price:** Free, MIT (github.com, checked 2026-11-06)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-10

## Safety reason

a review bot (code read @a540961, 2026-11-09, no-intake review): Caution for agent behaviour, code itself looks clean. Runs locally: src/eyes/ (about 2,000 lines of Python) indexes videos into ~/.cache/eyes with ffmpeg, Pillow, numpy and RapidOCR; no telemetry, hooks or MCP config found. Network use: yt-dlp downloads the URL you give without cookies (media.py lines 48-62); _download_model fetches a whisper.cpp model from huggingface.co/ggerganov (cli.py 442-452, transcript.py 27); opt-in --transcriber elevenlabs uploads audio to api.elevenlabs.io (transcript.py 20, 201-226), with the key from the environment or a .env file in the working folder (common.py 44-56). eyes setup --fix runs installers itself: winget install Gyan.FFmpeg on Windows, brew on macOS, sudo -n apt-get on Linux (cli.py 455-470). install-skill only copies SKILL.md into ~/.claude/skills/eyes and/or ~/.agents/skills/eyes (cli.py 527-548). view and report write local HTML with no external scripts. Why caution: skills/eyes/SKILL.md section 0 and AGENTS.md tell the agent to install from unpinned git HEAD and run setup --fix 'without asking the user for routine steps', which clashes with the ask-before-install rule. Not reviewed: docs images and the explainer video.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Code-reviewed by a review bot @a540961 (caution: the skill tells the agent to install software without asking). Claude Code on Windows: install it yourself rather than letting an agent do it. Install the eyes command with pipx install git+https://github.com/moritzkremb/claude-eyes@a540961 (pin the commit), then run eyes install-skill, which only copies one SKILL.md into %USERPROFILE%\.claude\\skills\\eyes. eyes setup --fix runs winget install Gyan.FFmpeg on Windows and downloads a whisper.cpp model (about 570 MB) from huggingface.co/ggerganov; whisper.cpp itself must be installed by hand on Windows. Before using the skill, remove or ignore its 'without asking the user' install steps (SKILL.md section 0) so the agent asks first. Only use --transcriber elevenlabs if you accept uploading the audio; it reads ELEVENLABS_API_KEY from the environment or a .env file in the working folder.
