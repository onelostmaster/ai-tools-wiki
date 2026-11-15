# VoiceStudio

- **Type:** app
- **Category:** voice and audio
- **Official URL:** https://github.com/debpalash/VoiceStudio
- **GitHub repo:** [https://github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- **Price:** Free (AGPL)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code scan, da74a6f, a project a review, 2026-10-31): Use with caution. `curl|sh` installer; some engines load Hugging Face models with `trust_remote_code=True`, which runs model-repo code; PostHog analytics are opt-in; the server binds `127.0.0.1`; it ships a Claude skill plus an MCP at `localhost:3900/mcp`. About 6 months old, single developer. No fix: the release installers are prebuilt binaries nobody has reviewed (only the source was read), from a single developer.

## Safe install

Safe install (fixes applied):
Windows: download the Windows installer from the official GitHub releases page (github.com/debpalash/VoiceStudio/releases/latest, README.md:221) instead of the `irm https://voicestudio.sh/install.ps1 | iex` one-liner (README.md:218). Android: the APK from the same releases page (README.md:393). Do not turn on the MOSS-TTS engines: they load Hugging Face model code with trust_remote_code=True (backend/services/tts_backend.py:2517, backend/engines/moss_tts_v15/main.py:308,318; checked at HEAD 0d71fe7 on 2026-11-14). Run the desktop app, not the Docker image: the Docker entrypoint listens on 0.0.0.0 (backend/docker_entrypoint.py:14), the app and MCP shim default to 127.0.0.1 (backend/mcp_shim/__main__.py:61). Leave PostHog analytics off (opt-in). Claude Code: add its MCP only as http://127.0.0.1:3900/mcp when the app is running.

## YOLO install

YOLO (your own risk): skips the release download (pipes the official script into PowerShell) and allows the MOSS-TTS engines.
irm https://voicestudio.sh/install.ps1 | iex

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
