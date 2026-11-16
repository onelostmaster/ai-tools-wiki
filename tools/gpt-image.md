# GPT Image

- **Type:** API
- **Category:** design
- **GitHub repo:** unknown
- **Price:** Paid per use (not verified)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-15

## Safety reason

Claude fix-mode re-review (2026-11-15): safe with fixes, Skip. Official OpenAI image API, paid per image; the old caution was a review bot's own with no finding. Prompts and images go to OpenAI under your key. Fix: a dedicated project key with a monthly budget, kept in env, and ask before batches.

## Safe install

Safe install (fixes applied):
A separate OpenAI project with a monthly budget; its key as OPENAI_API_KEY in env or secrets; ask the user before any batch of images.

## YOLO install

YOLO (your own risk): skips the separate project and budget, so spend has no cap.
Use your main API key.

## Install notes

Ask the user before installing. A separate OpenAI project with a monthly budget; its key as OPENAI_API_KEY in env or secrets; ask the user before any batch of images.
