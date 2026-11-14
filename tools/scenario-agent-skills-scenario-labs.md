# Scenario Agent Skills (scenario-labs)

- **Type:** skill
- **Category:** 3D and games, generating videos, design
- **Official URL:** https://github.com/scenario-labs/skills
- **GitHub repo:** https://github.com/scenario-labs/skills @ 7f4b801 (MIT; official Scenario vendor repo)
- **Price:** Skills free (MIT); Scenario free tier 50 credits/day (personal use only), Starter $15/mo 1,500 credits, Pro $45/mo, Max $75/mo (scenario.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @7f4b801, 2026-11-03): caution for spend and local code execution. Every generation spends Scenario credits; skills price first with dry_run unless told cost does not matter (`skills/scenario/SKILL.md:96-97`), but in unattended runs take the top-ranked model and proceed (`SKILL.md:236`). Expert skills run Python inside a running editor via Unreal Python Remote Execution (`skills/game-engines/unreal/scenario-unreal-expert/scripts/ue_remote.py:330-336`, multicast TTL 0 at `:249`) and similar bridges. Text overlay fetches Google Fonts (`skills/scenario-text-overlay/scripts/pillow_render.py:32`). The repo's own .claude/settings.json SessionStart hook runs pnpm install only if you open the cloned repo in Claude Code (`.claude/hooks/ensure-husky.sh:14`). Installer `npx skills add` is an unpinned third-party tool (`README.md:50-75`). No telemetry found in skill scripts.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code on Windows: `npx skills add scenario-labs/skills` (`README.md:50-75`) plus the hosted Scenario MCP; ask for price checks before each generation. Android: no.
