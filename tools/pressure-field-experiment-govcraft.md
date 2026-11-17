# pressure-field-experiment (Govcraft)

- **Type:** library
- **Category:** research, Hermes add-ons
- **Official URL:** https://github.com/Govcraft/pressure-field-experiment
- **GitHub repo:** https://github.com/Govcraft/pressure-field-experiment @ d3b0d5b (MIT/Apache-2.0, Rust; last push 2026-08-12; official code of arXiv 2601.08129)
- **Price:** Free, MIT/Apache-2.0 (github.com, checked 2026-11-02); runs on your own GPU
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @d3b0d5b, a review, 2026-11-02): safe. Only talks to the model host you give it (OLLAMA_HOST default localhost, `crates/schedule-experiment/src/main.rs:26`; `vllm_client.rs:113-117,182`); no std::process or Command anywhere, no telemetry, no build.rs or install scripts; Taskfile.yml only runs cargo/typst.

## Safe install

Safe install (fixes applied):
Windows (Rust + Ollama): download the repo at commit d3b0d5b, `cargo build`, then `set OLLAMA_HOST=http://localhost:11434` and `cargo run -p schedule-experiment` (README.md:25-41), with Ollama serving qwen2.5:0.5b, 1.5b and 3b (README.md:72). The crates use edition 2024, so you need Rust 1.85 or newer (README.md:71 says 1.75+). Unverified: crate dependency versions, because no Cargo.lock is committed (repo root, GitHub contents API) -> contain: build it in WSL or a devcontainer with no keys, run `cargo generate-lockfile` once and keep that lock file for later builds. Keep OLLAMA_HOST on localhost (crates/schedule-experiment/src/main.rs:26). Claude Code: can build and run it for you. claude.ai, Hermes, Android: no (Hermes: idea source only).

## YOLO install

YOLO (your own risk): skips the commit pin, the container and the kept lock file.
git clone https://github.com/Govcraft/pressure-field-experiment; cargo build; cargo run -p schedule-experiment

## Install notes

Safe, but ask the user before installing.
Windows: Rust toolchain plus Ollama with small Qwen2.5 models (the paper used an 8 GB RTX 4070 laptop); not tested. Android: no.
Hermes: idea source for multi-profile Hermes coordination, not a plugin.
