# SkillEvaluator (NVIDIA)

- **Type:** CLI
- **Category:** developer tools, security
- **Official URL:** https://docs.nvidia.com/skills/skillevaluator/
- **GitHub repo:** https://github.com/NVIDIA/SkillEvaluator @ 2a385d0 (Apache-2.0; reviewed commit; main is 7f9d2c5 as of 2026-11-16, not reviewed)
- **Price:** Free, Apache-2.0 (Tier 2/3 need a paid model key; Tier 3 also Docker)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @2a385d0, 2026-11-16: safe with the Install notes fixes. Scanner downloads (SkillSpector 2.13.4, Gitleaks 8.30.0) are sha256-pinned (utils/scanner_install.py:27-41, 61-73); no telemetry found; Tier 1 lints skill scripts, does not run them. Verified risks, each fixed: Tier 1 LLM checks default to on when any NVIDIA/OpenAI/Anthropic key is in the environment (cli.py:3544, provider_config.py:846-858), sending skill text to that model (fix: --no-llm and unset the keys); ci init pushes branches and opens a PR (ci_onboarding.py:604, 759-791; fix: never run ci init); npx skills add route (fix: don't use, call the CLI); 0.9.0 is 3 days old (fix: pin 0.9.0); no Windows Gitleaks build (scanner_install.py:35-40; fix: run in a cloud session). a review bot spot-checked scanner_install.py:27-41, cli.py:3544, provider_config.py:846-858 and ci_onboarding.py:604,759 at 2a385d0, and PyPI 0.9.0 (uploaded 2026-11-13), 2026-11-16.

## Safe install

Safe install (fixes applied):
Claude Code (cloud session, Linux): `uv tool install skillevaluator==0.9.0`, then `env -u ANTHROPIC_API_KEY -u OPENAI_API_KEY -u NVIDIA_API_KEY -u SKILL_EVAL_LLM_PROVIDER skillevaluator tier1 ./skill --no-llm -r json -o /tmp/se-reports`. Never run `ci init`; no npx skills route; no Tier 3. Windows: no native Gitleaks build (scanner_install.py:35-40), so use the cloud session. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, --no-llm and the key unsetting.
`uv tool install skillevaluator` then `skillevaluator tier1 ./skill` (sends skill text to whichever model key is set).

## Install notes

Ask the user first. In a Claude cloud session: uv tool install skillevaluator==0.9.0, then env -u ANTHROPIC_API_KEY -u OPENAI_API_KEY -u NVIDIA_API_KEY -u SKILL_EVAL_LLM_PROVIDER skillevaluator tier1 ./skill --no-llm -r json -o /tmp/se-reports. No ci init, no npx skill, no Tier 3.
