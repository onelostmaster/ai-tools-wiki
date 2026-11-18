# TokenEconomizer (Microsoft)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://tokeneconomizer.github.io
- **GitHub repo:** https://github.com/microsoft/TokenEconomizer @ fb85398 (MIT; reviewed commit)
- **Price:** Free, MIT (its judge and fact calls use your own agent's plan)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @fb85398, 2026-11-16: safe with the Install notes fixes. No network client or telemetry (only a 127.0.0.1 probe, tokeneconomizer/plugin/toolcheck.py:162); state in ~/.tokeneconomizer, mode 0700 (tokeneconomizer/plugin/paths.py:31,46); its own model calls run with no tools and no MCP (claude -p --tools "" --strict-mcp-config, tokeneconomizer/plugin/sidecall.py:264-301; Hermes -t bot_room, never -z, tokeneconomizer/plugin/sidecall.py:516). Verified risks, each fixed: tool pruning defaults to auto and writes deny rules to .claude/settings.local.json (tokeneconomizer/plugin/config.py:186, tokeneconomizer/plugin/denylist.py:52; fix: config set toolprune=propose --global, then toolprune apply by hand); runs from a git clone updated by git pull (README; fix: checkout fb85398, no pull until re-review); tested only on Claude Code 2.1.300-2.1.310 (README "Supported versions"; unverified on newer, contain: /tokeneconomizer:status first, TE_DISABLE=1 to switch off). a review bot spot-checked LICENSE, README install/versions and config.py:186, denylist.py:52, toolcheck.py:162, paths.py:31,46, sidecall.py:264-301,516 at fb85398, 2026-11-16 (paths corrected to tokeneconomizer/plugin/, license is MIT).

## Safe install

Safe install (fixes applied):
Claude Code on Windows (local, PowerShell or Git Bash): `git clone https://github.com/microsoft/TokenEconomizer.git`, `git -C TokenEconomizer checkout fb85398`, `claude plugin marketplace add "$PWD/TokenEconomizer"`, `claude plugin install tokeneconomizer@tokeneconomizer`; in claude: `/tokeneconomizer:config set toolprune=propose --global`, then `/tokeneconomizer:status`. Keep micro-skills and history_import off at first; never `git pull` in the clone until re-review; `TE_DISABLE=1` switches it off. claude.ai, Hermes, Android: no (local Claude Code only).

## YOLO install

YOLO (your own risk): skips the commit pin and toolprune=propose (auto pruning writes deny rules to .claude/settings.local.json).
`git clone https://github.com/microsoft/TokenEconomizer.git && claude plugin marketplace add "$PWD/TokenEconomizer" && claude plugin install tokeneconomizer@tokeneconomizer`

## Install notes

Ask the user first. Local Claude Code only: git clone https://github.com/microsoft/TokenEconomizer.git && git -C TokenEconomizer checkout fb85398 && claude plugin marketplace add "$PWD/TokenEconomizer" && claude plugin install tokeneconomizer@tokeneconomizer; then /tokeneconomizer:config set toolprune=propose --global and /tokeneconomizer:status. Keep micro-skills and history_import off at first. No git pull until a re-review.
