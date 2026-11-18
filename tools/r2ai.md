# r2ai

- **Type:** plugin
- **Category:** security, developer tools
- **Official URL:** https://github.com/radareorg/r2ai
- **GitHub repo:** https://github.com/radareorg/r2ai @ 08afde5 (release 1.5.3, 2026-10-18; MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02). Needs an LLM: a local Ollama model (free) or a paid API key (Anthropic, OpenAI, etc.).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @9077de9 1.5.4 (2026-11-17): safe with fixes. Auto mode asks before risky commands; r2ai.auto.yolo is false by default (src/r2ai.c:780). On Windows the HTTP backend is system curl (src/http.c:150-152), so a cloud API key sits on the command line where local programs see it. Disassembly goes to whichever model you set. Fix: a local Ollama model, yolo off.

## Safe install

Safe install (fixes applied):
r2pm -Uci r2ai (README.md:64); point r2ai at a local Ollama model, no cloud key on Windows; keep r2ai.auto.yolo=false; only reverse-engineer software you own or have permission to analyse.

## YOLO install

YOLO (your own risk): skips the local model and yolo off.
Use a cloud key on Windows and set r2ai.auto.yolo=true.

## Install notes

Ask the user before installing.
Windows: plugin for radare2 (see its README); prefer a local Ollama model so binaries and keys stay on the PC; keep auto-mode confirmations on. Only reverse-engineer software you own or are allowed to.
