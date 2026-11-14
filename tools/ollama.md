# Ollama

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://ollama.com
- **GitHub repo:** [https://github.com/ollama/ollama](https://github.com/ollama/ollama) (linked from `ollama.com`, checked 2026-10-31)
- **Price:** Free for local models; optional cloud plans: Pro $20/mo ($200/yr), Max $100/mo, Team $500/mo (`ollama.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

Ollama (official vendor; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: the Linux install is a curl | sh script; Windows uses the `OllamaSetup.exe` installer. Local models run on your machine; cloud models are a separate paid service.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: run the `OllamaSetup.exe` installer from [https://ollama.com/download](https://ollama.com/download) (official docs; installs in your account without admin rights).
Linux: `curl -fsSL https://ollama.com/install.sh | sh` (official docs; a curl | sh script, so read it first).
