# Codex CLI (OpenAI)

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://developers.openai.com/codex
- **GitHub repo:** https://github.com/openai/codex @ 67f0994 (Apache-2.0; latest commit on 2026-10-30)
- **Price:** Included in ChatGPT plans: Free $0, Go $8/month, Plus $20/month, Pro from $100/month; API-key use billed per token (`learn.chatgpt.com`, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor README and pricing page, 2026-11-01): safe. Official OpenAI product, open source (Apache-2.0). Sends your prompts and code to OpenAI under your ChatGPT login or API key; the agent edits files and runs commands in your project, so keep approvals on; the quick installers pipe a script from `chatgpt.com` into the shell (read it first).

## Safe install

Safe install (fixes applied):
Windows: npm install -g @openai/codex@0.169.0 (pinned; latest on npm 2026-11-16) instead of the irm ... | iex installer, which runs a script fetched from chatgpt.com at install time (README line 25). This installs globally (npm -g); that cannot be avoided for a CLI you run as codex. Then run codex and pick Sign in with ChatGPT yourself; never paste keys into chat. Keep the default approvals and sandbox: never pass --dangerously-bypass-approvals-and-sandbox (codex-rs/cli/src/main.rs:2158-2163 turns both off with it). Your prompts and code go to OpenAI under your account.

## YOLO install

YOLO (your own risk): skips the version pin and reading the installer.
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex" (README line 25), latest version.

## Install notes

Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"` or `npm install -g @openai/codex`, then run `codex` and choose Sign in with ChatGPT yourself (README); never paste keys into chat.
