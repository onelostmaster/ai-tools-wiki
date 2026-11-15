# earshot

- **Type:** MCP
- **Category:** voice and audio, editing
- **Official URL:** https://github.com/Leonxlnx/earshot
- **GitHub repo:** [https://github.com/Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) @ 591fa3e (MIT; cited in a project a review)
- **Price:** Free (MIT, per a review; MIT also shown in web listings, checked 2026-10-31). The optional Gemini critique needs your own `GEMINI_API_KEY`.
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, 591fa3e, 2026-10-31): Looks safe. No telemetry; models are pinned Hugging Face revisions (safetensors only), offline switch `EARSHOT_OFFLINE=1`; subprocesses are only ffmpeg/ffprobe; the only upload is the opt-in Gemini critique, but over MCP the agent passes consent itself, so don't set `GEMINI_API_KEY`. First use downloads ~1.1 GB of models + CPU torch. Claude (read 591fa3e): network is only Hugging Face and that opt-in critique.

## Safe install

Safe install (fixes applied):
Windows (Claude Code, PowerShell): `git clone https://github.com/Leonxlnx/earshot; cd earshot; git checkout 591fa3e` (the reviewed commit); `python -m venv .venv`; `.venv\Scripts\python -m pip install torch --index-url https://download.pytorch.org/whl/cpu`; `.venv\Scripts\python -m pip install -e ".[mcp]"` (no llm extra); then `claude mcp add earshot --scope user -e EARSHOT_THREADS=3 -- C:\path\to\earshot\.venv\Scripts\python.exe -m earshot mcp`, and copy skills\\earshot into %USERPROFILE%\.claude\\skills\. Never set GEMINI_API_KEY (over MCP the agent gives consent for the Gemini upload itself). After the first run has downloaded the ~1.1 GB of pinned models, set EARSHOT_OFFLINE=1. Hermes: unconfirmed: the same MCP command under mcp_servers in ~/.hermes/config.yaml. Android: not used.

## YOLO install

YOLO (your own risk): skips the commit pin, the CPU-only torch index and offline mode.
`git clone https://github.com/Leonxlnx/earshot` then `pip install -e ".[mcp]"` and `claude mcp add earshot -- python -m earshot mcp` (still never set GEMINI_API_KEY).

## Install notes

Claude Code (Windows PowerShell): `git clone https://github.com/Leonxlnx/earshot; cd earshot; python -m venv .venv; .venv\Scripts\python -m pip install torch --index-url https://download.pytorch.org/whl/cpu; .venv\Scripts\python -m pip install -e ".[mcp]"` (skip the `llm` extra), then `claude mcp add earshot --scope user -e EARSHOT_THREADS=3 -- C:\path\to\earshot\.venv\Scripts\python.exe -m earshot mcp` (replace `C:\path\to\earshot` with your clone's folder), and copy `skills\earshot` (+ optional `skills\real-sound`) into `%USERPROFILE%\.claude\skills\` (README, per a review; Windows paths unconfirmed). Don't set `GEMINI_API_KEY`; never paste keys into chat.
Hermes: unconfirmed: the same earshot MCP command under `mcp_servers` in `~/.hermes/config.yaml`, and copy the skill folders into `~/.hermes/skills/` .
