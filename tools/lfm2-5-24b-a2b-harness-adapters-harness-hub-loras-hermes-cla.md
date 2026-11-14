# LFM2.5-24B-A2B harness adapters (harness-hub LoRAs: hermes, claude-code)

- **Type:** library
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://huggingface.co/collections/harness-hub/lfm25-24b-harness-adapters
- **GitHub repo:** none (Hugging Face only): huggingface.co/harness-hub/LFM2.5-24B-A2B-hermes @ d4bb6d2, -hermes-GGUF @ 2e25bfa, LFM2.5-24B-A2B-claude-code @ df72375; base LiquidAI/LFM2.5-24B-A2B
- **Price:** Free download; base model under the LFM Open License v1.0: commercial use only while your organisation has under $10M yearly revenue (huggingface.co, checked 2026-11-02). Hardware: 14.5-25.5 GB GGUF or about 48 GB BF16 for vLLM.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (file read @d4bb6d2, 2e25bfa, df72375, a review / Hermes #102, 2026-11-02): safe (weights only). safetensors/GGUF weights, stock PEFT adapter_config.json (no remote code), chat_template byte-identical to LiquidAI's base. No pickle or scripts. Publisher is an unverified 2-member team, not Liquid AI or Nous. Around it: the card's Hermes step is a curl|bash installer (`README.md:86`); keep llama.cpp/vLLM on localhost and Hermes approvals on.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Hermes (Windows): download LiquidAI/LFM2.5-24B-A2B-GGUF (Q4_K_M 14.5 GB) and the adapter GGUF, run `llama-server.exe -m <base>.gguf --lora <adapter>.gguf -c 65536 --port 8080` (<base>/<adapter> = the downloaded file names; the card says "llama serve"), then in Hermes choose Custom endpoint `http://localhost:8080/v1`.
Claude Code (local only): serve the same way and point Claude Code at the local endpoint with ANTHROPIC_BASE_URL (per the card); the vLLM route needs Linux/WSL2.
