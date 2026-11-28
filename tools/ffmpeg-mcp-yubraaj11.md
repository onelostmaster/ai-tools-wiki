# ffmpeg-mcp (yubraaj11)

- **Type:** MCP
- **Category:** editing, generating videos
- **Official URL:** https://github.com/yubraaj11/ffmpeg-mcp
- **GitHub repo:** https://github.com/yubraaj11/ffmpeg-mcp @ dcb591e (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-27

## Safety reason

a review bot read @dcb591e: safe with these fixes. A local stdio MCP server (main.py:93) that builds FFmpeg commands through ffmpeg-python; it needs no API keys, makes no web calls of its own, and its direct subprocess calls pass fixed argument lists to ffmpeg or ffprobe (validate_input_video_path.py:26, loudness.py:14, silence.py:19). Verified 1: every output goes under one root folder: FFMPEG_MCP_OUTPUT_DIR if set, else ~/ffmpeg-mcp-output for a pip/uvx install, else ffmpeg_mcp/processed_elements in a clone (paths.py:18-23); caller file names are cut to their base name (paths.py:46), so it does not write outside that folder. Its deletes (paths.py:64, concat_clips_with_transition.py:104 and :109) remove only its own job, normalized_video_clips and Intermediate_files folders inside that root. Fix: set FFMPEG_MCP_OUTPUT_DIR to a folder used only by this tool. Verified 2: it overwrites files with the same name in that folder (overwrite_output=True, runner.py:26), and two tools always use one fixed name (scale_video.py:15 final_edited_video.mp4; concat_clips_with_transition.py:19 output_concatenated_video.mp4). Fix: copy each finished video out of the output folder before the next call. Verified 3: the first caption or transcribe call downloads a faster-whisper model from Hugging Face (transcribe.py:20-21). Fix: run one transcribe once, then set HF_HUB_OFFLINE=1 in the server env. Verified 4: the README's uvx ffmpeg-mcp-studio (README:152) installs the newest PyPI release and pyproject.toml lists only minimum versions, while the repo ships uv.lock. Fix: run from a clone at the pinned commit with uv sync --frozen (README:208). Note: extract_frames.py:60 calls eval() on ffprobe's r_frame_rate, which ffprobe always prints as two integers (for example 30/1); it reads no other input. MIT (LICENSE); bundled Montserrat font under OFL.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): winget install Gyan.FFmpeg and install uv yourself; git clone https://github.com/yubraaj11/ffmpeg-mcp ; cd ffmpeg-mcp ; git checkout dcb591e130d409bee5795fa11f82c5eaf4d3b28f ; uv sync --frozen . Then: claude mcp add ffmpeg-mcp -e FFMPEG_MCP_OUTPUT_DIR=%USERPROFILE%\\Videos\\ffmpeg-mcp -- uv run --frozen --directory <your clone path> ffmpeg-mcp-studio . Give it copies of your clips, copy each finished video out of that folder before the next call, and after the first transcribe add -e HF_HUB_OFFLINE=1.
claude.ai, Hermes, Android: not supported (local stdio server that needs FFmpeg on the same computer).

## YOLO install

YOLO (your own risk): skips the pinned commit and lockfile, the dedicated output folder and offline model. README: claude mcp add ffmpeg-mcp -- uvx ffmpeg-mcp-studio

## Install notes

Safe with fixes: run from a clone at pinned commit dcb591e with uv sync --frozen (not the unpinned uvx package); set FFMPEG_MCP_OUTPUT_DIR to its own folder, because it overwrites same-named files there; the first caption call downloads a Whisper model, then set HF_HUB_OFFLINE=1. No API keys. Fits the faceless video channel: captions, Shorts/Reels formatting, jump cuts and beat-synced cuts from an AI client.
