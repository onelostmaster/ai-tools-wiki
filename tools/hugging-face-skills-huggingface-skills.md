# Hugging Face skills (huggingface/skills)

- **Type:** skill
- **Category:** research, developer tools
- **Official URL:** https://github.com/huggingface/skills
- **GitHub repo:** https://github.com/huggingface/skills @ 25910b3 (Apache-2.0)
- **Price:** Free skills (Apache-2.0); HF Jobs and paid compute cost extra (price not checked, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @25910b3, a review, 2026-11-02): safe, official vendor. The hf-cli skill installs the CLI with a curl | bash line (`skills/hf-cli/SKILL.md:6`): use pip instead. Trainer skills need an HF_TOKEN and run paid HF Jobs.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: add the skills you need per its README; install the hf CLI with pip, not curl | bash.
Windows: works in Claude Code on Windows. Android: no.
