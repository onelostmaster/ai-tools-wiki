# AiSOC (beenuar/AiSOC)

- **Type:** app
- **Category:** security
- **Official URL:** https://github.com/beenuar/AiSOC
- **GitHub repo:** https://github.com/beenuar/AiSOC @ 0c0e6fc (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @0c0e6fc, a review, 2026-11-02): caution. 66 prebuilt .whl files are committed at the repo root (binaries you cannot read). Windows installer is irm | iex (`README.md:48`, `install.ps1:463`). Pins Ollama llama3.2 3B (`README.md:148`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Do not use the irm | iex installer. Claude says skip it anywhere.
Windows: not recommended. Android: no.
