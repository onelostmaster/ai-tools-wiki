# DeepSeek-V4.1-Flash Uncensored GGUF (AtomicChat)

- **Type:** dataset
- **Category:** Hermes add-ons, research
- **Official URL:** https://huggingface.co/AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF
- **GitHub repo:** unknown (Hugging Face model AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF @ 4f1d2f7, MIT, updated 2026-10-31)
- **Price:** Free download, MIT (huggingface.co, checked 2026-11-02); DeepSeek API version $0.30/$1.20 per 1M tokens at peak (api-docs.deepseek.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-02

## Safety reason

a review bot (model card read @4f1d2f7, Hermes a review, 2026-11-02): caution. Refusals removed on purpose (`README.md:94`), so it also follows injected instructions more readily: a bad fit for an agent that reads the web. Needs 64 GB RAM plus a separate 110 GB Engram file (`README.md:48-49,84`). Strata-only runtime, not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: only via the Strata runtime (not reviewed); 12 GB GPU, 64 GB RAM and a fast SSD per the model card.
