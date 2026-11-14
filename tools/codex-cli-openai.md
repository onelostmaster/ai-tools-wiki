# Codex CLI (OpenAI)

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://developers.openai.com/codex
- **GitHub repo:** https://github.com/openai/codex @ 67f0994 (Apache-2.0; latest commit on 2026-10-30)
- **Price:** Included in ChatGPT plans: Free $0, Go $8/month, Plus $20/month, Pro from $100/month; API-key use billed per token (`learn.chatgpt.com`, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-01

## Safety reason

a review bot (vendor README and pricing page, 2026-11-01): safe. Official OpenAI product, open source (Apache-2.0). Sends your prompts and code to OpenAI under your ChatGPT login or API key; the agent edits files and runs commands in your project, so keep approvals on; the quick installers pipe a script from `chatgpt.com` into the shell (read it first).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"` or `npm install -g @openai/codex`, then run `codex` and choose Sign in with ChatGPT yourself (README); never paste keys into chat.
