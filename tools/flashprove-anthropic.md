# FlashProve (Anthropic)

- **Type:** library
- **Category:** research, security
- **Official URL:** https://github.com/anthropics/FlashProve
- **GitHub repo:** https://github.com/anthropics/FlashProve @ 9e2bdd8f (Apache-2.0, `LICENSE:1`; 0.16.0-rc.26, first public release 2026-10-30)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-03)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @9e2bdd8f, 2026-11-03): safe. No telemetry found; network only to the user-set --server, no redirects (`integrations/ask_and_check.py:203-218`, `integrations/check_proof.py:513-554`); vLLM usage stats switched off (`integrations/vllm/end_to_end/end_to_end.py:983`); only curl|sh is Lean's official elan installer in docs (`lean/CHECKING.md:183`); exec() only in local Lean check scripts (`lean/scripts/check.py:116`); no git hooks or auto-update. Repo says not maintained (`README.md:3`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Proving needs one NVIDIA H100 (`README.md:18-21`); verifying runs on CPU on Linux. Windows: only via WSL with g++13. Android: no. Not a Claude Code or Hermes tool.
