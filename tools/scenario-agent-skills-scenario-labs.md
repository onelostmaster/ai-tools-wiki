# Scenario Agent Skills (scenario-labs)

- **Type:** skill
- **Category:** 3D and games, generating videos, design
- **Official URL:** https://github.com/scenario-labs/skills
- **GitHub repo:** https://github.com/scenario-labs/skills @ 7f4b801 (MIT; official Scenario vendor repo)
- **Price:** Skills free (MIT); Scenario free tier 50 credits/day (personal use only), Starter $15/mo 1,500 credits, Pro $45/mo, Max $75/mo (scenario.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @7f4b801, 2026-11-03): caution for spend and local code execution. Every generation spends Scenario credits; skills price first with dry_run unless told cost does not matter (skills/scenario/SKILL.md:96-97), but in unattended runs take the top-ranked model and proceed (SKILL.md:236). Expert skills run Python inside a running editor via Unreal Python Remote Execution (skills/game-engines/unreal/scenario-unreal-expert/scripts/ue_remote.py:330-336, multicast TTL 0 at :249) and similar bridges. Text overlay fetches Google Fonts (skills/scenario-text-overlay/scripts/pillow_render.py:32). The repo's own .claude/settings.json SessionStart hook runs pnpm install only if you open the cloned repo in Claude Code (.claude/hooks/ensure-husky.sh:14). Installer npx skills add is an unpinned third-party tool (README.md:50-75). No telemetry found in skill scripts. Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (skill folders copied at 7f4b801 instead of the unpinned npx installer, cloned repo never opened as a Claude Code project, dry_run price asked every time and never run unattended, Unreal/editor bridges used only on purpose); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Claude Code on Windows: do not use the unpinned npx skills add installer; instead copy the skill folders you want from https://github.com/scenario-labs/skills at commit 7f4b801 into %USERPROFILE%\.claude\\skills. Do not open the cloned repo itself as a Claude Code project (its .claude/settings.json SessionStart hook runs pnpm install, .claude/hooks/ensure-husky.sh:14). Every generation spends Scenario credits: ask for the dry_run price first each time (skills/scenario/SKILL.md:96-97) and never run it unattended, because unattended runs take the top-ranked model and proceed (SKILL.md:236). Only use the Unreal/editor expert skills when you want it to run Python inside your open editor (ue_remote.py:330-336). Text overlay fetches Google Fonts (pillow_render.py:32). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the per-run price check and the no-unattended rule.
Claude Code on Windows: npx skills add scenario-labs/skills (README.md:50-75) plus the hosted Scenario MCP; unattended runs spend credits on the top-ranked model without asking.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Claude Code on Windows: npx skills add scenario-labs/skills (README.md:50-75) plus the hosted Scenario MCP; ask for price checks before each generation. Android: no.
