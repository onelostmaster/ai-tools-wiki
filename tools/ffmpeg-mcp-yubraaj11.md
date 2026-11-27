# ffmpeg-mcp (yubraaj11)

- **Type:** MCP
- **Category:** editing, generating videos
- **Official URL:** https://github.com/yubraaj11/ffmpeg-mcp
- **GitHub repo:** https://github.com/yubraaj11/ffmpeg-mcp @ dcb591e (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: needs Python 3.12+ and FFmpeg/ffprobe on PATH; runs with uvx ffmpeg-mcp-studio (PyPI package, unpinned) added to your MCP client config; tools check that input paths exist before FFmpeg runs. unverified: which folders it writes output to. Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: run it from a clone at the pinned commit dcb591e (not the unpinned PyPI package) inside a devcontainer or sandbox, give it one working folder of copies of your clips, no API keys (it needs none), network off after install. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code (Windows): winget install ffmpeg, then add an MCP server that runs uvx ffmpeg-mcp-studio (README Quick Start).
