# pressure-field-experiment (Govcraft)

- **Type:** library
- **Category:** research, Hermes add-ons
- **Official URL:** https://github.com/Govcraft/pressure-field-experiment
- **GitHub repo:** https://github.com/Govcraft/pressure-field-experiment @ d3b0d5b (MIT/Apache-2.0, Rust; last push 2026-08-12; official code of arXiv 2601.08129)
- **Price:** Free, MIT/Apache-2.0 (github.com, checked 2026-11-02); runs on your own GPU
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @d3b0d5b, a review, 2026-11-02): safe. Only talks to the model host you give it (OLLAMA_HOST default localhost, `crates/schedule-experiment/src/main.rs:26`; `vllm_client.rs:113-117,182`); no std::process or Command anywhere, no telemetry, no build.rs or install scripts; Taskfile.yml only runs cargo/typst.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: Rust toolchain plus Ollama with small Qwen2.5 models (the paper used an 8 GB RTX 4070 laptop); not tested. Android: no.
Hermes: idea source for multi-profile Hermes coordination, not a plugin.
