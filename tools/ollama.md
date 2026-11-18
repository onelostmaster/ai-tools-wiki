# Ollama

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://ollama.com
- **GitHub repo:** [https://github.com/ollama/ollama](https://github.com/ollama/ollama) (linked from `ollama.com`, checked 2026-10-31)
- **Price:** Free for local models; optional cloud plans: Pro $20/mo ($200/yr), Max $100/mo, Team $500/mo (`ollama.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Ollama (official vendor; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: the Linux install is a curl | sh script; Windows uses the `OllamaSetup.exe` installer. Local models run on your machine; cloud models are a separate paid service.

## Safe install

Safe install (fixes applied):
Windows: run OllamaSetup.exe from https://ollama.com/download (official docs; installs in your user account, no admin rights). Use local models only; cloud models are a separate paid service, so do not sign in to an Ollama account unless you want them.
Linux: download https://ollama.com/install.sh, read it, then run it (do not pipe curl straight into sh).

## YOLO install

YOLO (your own risk): skips reading the Linux script first.
Linux: curl -fsSL https://ollama.com/install.sh | sh (official docs). Windows is the same as Safe install.

## Install notes

Windows: run the `OllamaSetup.exe` installer from [https://ollama.com/download](https://ollama.com/download) (official docs; installs in your account without admin rights).
Linux: `curl -fsSL https://ollama.com/install.sh | sh` (official docs; a curl | sh script, so read it first).
