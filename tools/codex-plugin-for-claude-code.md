# Codex plugin for Claude Code

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/openai/codex-plugin-cc
- **GitHub repo:** [https://github.com/openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)
- **Price:** Needs a paid OpenAI login (price not verified)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, db52e28, a review; official OpenAI): Looks safe. Sends your code to OpenAI under your login; needs the Codex CLI; the Stop review gate is off by default; rescue runs Codex with approvals 'never' and workspace-write.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): npm install -g @openai/codex (installs the Codex CLI globally; that is the required route), then /plugin marketplace add openai/codex-plugin-cc, /plugin install codex@openai-codex and /codex:setup. Sign in with your own OpenAI login; never paste keys into chat. It sends your code to OpenAI. The rescue command runs Codex with approvals "never" and workspace-write , so use it only in a git repo with everything committed so you can revert. Leave the Stop review gate off (default).

## YOLO install

Not written yet.

## Install notes

Claude Code: `npm install -g @openai/codex` first, then `/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex` and `/codex:setup`. Needs your paid OpenAI/ChatGPT login; never paste keys into chat.
