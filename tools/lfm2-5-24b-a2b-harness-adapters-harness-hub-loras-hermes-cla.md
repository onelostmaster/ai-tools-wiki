# LFM2.5-24B-A2B harness adapters (harness-hub LoRAs: hermes, claude-code)

- **Type:** library
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://huggingface.co/collections/harness-hub/lfm25-24b-harness-adapters
- **GitHub repo:** none (Hugging Face only): huggingface.co/harness-hub/LFM2.5-24B-A2B-hermes @ d4bb6d2, -hermes-GGUF @ 2e25bfa, LFM2.5-24B-A2B-claude-code @ df72375; base LiquidAI/LFM2.5-24B-A2B
- **Price:** Free download; base model under the LFM Open License v1.0: commercial use only while your organisation has under $10M yearly revenue (huggingface.co, checked 2026-11-02). Hardware: 14.5-25.5 GB GGUF or about 48 GB BF16 for vLLM.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (file read @d4bb6d2, 2e25bfa, df72375, a review / Hermes #102, 2026-11-02): safe (weights only). safetensors/GGUF weights, stock PEFT adapter_config.json (no remote code), chat_template byte-identical to LiquidAI's base. No pickle or scripts. Publisher is an unverified 2-member team, not Liquid AI or Nous. Around it: the card's Hermes step is a curl|bash installer (`README.md:86`); keep llama.cpp/vLLM on localhost and Hermes approvals on.

## Safe install

Safe install (fixes applied):
Windows (Hermes): download LiquidAI/LFM2.5-24B-A2B-GGUF (Q4_K_M) and the adapter GGUF from harness-hub/LFM2.5-24B-A2B-hermes-GGUF pinned to the reviewed revision 2e25bfa (hf download <repo> --revision <full commit id from the repo History page>); start llama.cpp's official release llama-server.exe -m <base>.gguf --lora <adapter>.gguf -c 65536 --host 127.0.0.1 --port 8080 so it listens only on your PC; in Hermes choose Custom endpoint http://localhost:8080/v1 and keep approvals on. Fix: skip the card's curl|bash Hermes installer (README.md:86); install Hermes by its own official route.
Claude Code (Windows, local only): serve the claude-code adapter (revision df72375) the same way and set ANTHROPIC_BASE_URL to the local endpoint for that session only. Weights only (safetensors/GGUF, no remote code), so nothing else to fix.

## YOLO install

YOLO (your own risk): skips the revision pins, the localhost-only bind and avoiding the card's curl|bash Hermes step.
Follow the model card as written (README.md:86 curl|bash, then llama serve with the latest adapter files).

## Install notes

Safe, but ask the user before installing.
Hermes (Windows): download LiquidAI/LFM2.5-24B-A2B-GGUF (Q4_K_M 14.5 GB) and the adapter GGUF, run `llama-server.exe -m <base>.gguf --lora <adapter>.gguf -c 65536 --port 8080` (<base>/<adapter> = the downloaded file names; the card says "llama serve"), then in Hermes choose Custom endpoint `http://localhost:8080/v1`.
Claude Code (local only): serve the same way and point Claude Code at the local endpoint with ANTHROPIC_BASE_URL (per the card); the vLLM route needs Linux/WSL2.
