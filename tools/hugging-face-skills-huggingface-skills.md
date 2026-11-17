# Hugging Face skills (huggingface/skills)

- **Type:** skill
- **Category:** research, developer tools
- **Official URL:** https://github.com/huggingface/skills
- **GitHub repo:** https://github.com/huggingface/skills @ 25910b3 (Apache-2.0)
- **Price:** Free skills (Apache-2.0); HF Jobs and paid compute cost extra (price not checked, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @25910b3, a review, 2026-11-02): safe, official vendor. The hf-cli skill installs the CLI with a curl | bash line (`skills/hf-cli/SKILL.md:6`): use pip instead. Trainer skills need an HF_TOKEN and run paid HF Jobs.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `/plugin marketplace add huggingface/skills` then `/plugin install hf-cli@huggingface/skills` (README.md:30,36). Verified: the hf-cli skill installs the CLI with curl | bash (skills/hf-cli/SKILL.md:6). Fix: install it instead in a venv with `pip install huggingface_hub==2.4.0` (PyPI, 2026-10-29; the version the skill was generated with) and set HF_HUB_DISABLE_TELEMETRY=1 and HF_HUB_DISABLE_UPDATE_CHECK=1 (huggingface_hub env-var docs). Add other skills one by one with `hf skills add <name>`. Trainer and job skills need an HF_TOKEN and run paid HF Jobs: use a read-only token unless you mean to upload or pay. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the pinned pip install, telemetry and update-check opt-outs and the read-only token.
/plugin marketplace add huggingface/skills; /plugin install hf-cli@huggingface/skills; let it run the curl | bash installer.

## Install notes

Safe, but ask the user before installing.
Claude Code: add the skills you need per its README; install the hf CLI with pip, not curl | bash.
Windows: works in Claude Code on Windows. Android: no.
