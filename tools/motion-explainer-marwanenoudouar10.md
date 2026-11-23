# motion-explainer (Marwanenoudouar10)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/Marwanenoudouar10/motion-explainer
- **GitHub repo:** https://github.com/Marwanenoudouar10/motion-explainer @ b0ec17d (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-22); TTS service cost depends on the one you pick
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-22

## Safety reason

Not code-reviewed for safety. README states it needs whisper.cpp plus a model download from huggingface.co and voice-over from a TTS site you use by hand (no API key). Its install lines are Mac (brew). Unverified: scripts/doctor.sh and skill scripts -> Contain: separate folder, pinned commit, no keys, permission prompts on. Checked 2026-11-22.

## Safe install

Unreviewed: contain it: clone into a separate project folder on Windows, git checkout b0ec17d, read SKILL.md and scripts/doctor.sh first; its brew lines are Mac-only, so get whisper.cpp from its official GitHub releases instead, install npm packages only from the lockfile in each new project folder, add no API keys, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: clone into a separate project folder on Windows, git checkout b0ec17d, read SKILL.md and scripts/doctor.sh first; its brew lines are Mac-only, so get whisper.cpp from its official GitHub releases instead, install npm packages only from the lockfile in each new project folder, add no API keys, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions).
