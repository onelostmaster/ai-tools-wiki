# SupoClip

- **Type:** app
- **Category:** editing, video
- **Official URL:** https://www.supoclip.com/
- **GitHub repo:** https://github.com/FujiwaraChoki/supoclip (AGPL-3.0, about 3.3k stars, confirmed via GitHub API 2026-11-16)
- **Price:** Free self-hosted (needs an AssemblyAI key and an LLM key, or local Whisper + Ollama); hosted plan price unknown
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed (README only, Claude, 2026-11-16). unverified: what the Docker stack sends off-machine besides the AssemblyAI and LLM calls it names; contain it as in Safe install until a code read.

## Safe install

Unreviewed: contain it: run it only in Docker Desktop on Windows from a commit you pin, with the local Whisper + Ollama option so no AssemblyAI or LLM keys are given, ports bound to 127.0.0.1, and no social accounts connected. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
No confirmed safe install yet: needs a Claude code read first. README: docker-compose up -d with ASSEMBLY_AI_API_KEY and an LLM key; local Whisper + Ollama per its self-hosting tutorial.
