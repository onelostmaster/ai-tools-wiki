# r2ai

- **Type:** plugin
- **Category:** security, developer tools
- **Official URL:** https://github.com/radareorg/r2ai
- **GitHub repo:** https://github.com/radareorg/r2ai @ 08afde5 (release 1.5.3, 2026-10-18; MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02). Needs an LLM: a local Ollama model (free) or a paid API key (Anthropic, OpenAI, etc.).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @08afde5, a review, 2026-11-02): caution. Sends disassembly to the LLM you pick (cloud if you set a cloud key). Auto mode runs model-chosen r2 commands, asking first by default (`src/r2ai.c:780`; `src/tools.c:329-331`). On Windows and builds without libcurl it calls system curl with your API key on the command line (`src/http.c:150-157`), visible to local programs. Keys in `~/.config/r2ai/apikeys.txt`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: plugin for radare2 (see its README); prefer a local Ollama model so binaries and keys stay on the PC; keep auto-mode confirmations on. Only reverse-engineer software you own or are allowed to.
