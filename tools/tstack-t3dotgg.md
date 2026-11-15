# tstack (t3dotgg)

- **Type:** skill
- **Category:** coding, developer tools
- **GitHub repo:** https://github.com/t3dotgg/tstack @ 11e37a7 (MIT, LICENSE; commit 2026-11-11 confirmed via GitHub API)
- **Price:** Free (MIT)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @11e37a7, 2026-11-14: safe with the Install notes fixes. Text skills plus one Python script (skills/babysit-pr/scripts/pr-wait) that only runs the gh CLI (pr-wait:127) and keeps state in ~/.local/state/pr-wait. No telemetry, no other network. Verified risk, fixed: full-send grants itself permission to merge PRs and force-push with --force-with-lease (skills/full-send/SKILL.md:16-19); fix: Claude Code deny rules for `Bash(gh pr merge:*)` and `mcp__github__merge_pull_request` (full-stop, which never merges per SKILL.md:8-9, still loads full-send per README, so keep the rules either way). council and sol-loop need subagents on other providers' models (README Requirements); without them they report and stop.

## Safe install

Safe install (fixes applied):
Claude Code: from a clone checked out at `11e37a7`, copy only the skills you want: `cp -R tstack/skills/\{full-stop,full-send,file-pr,babysit-pr,sol-loop,leaving-pr-comments\} ~/.claude/skills/`. Keep these deny rules in settings.json: `"permissions": \{"deny": ["Bash(gh pr merge:*)", "mcp__github__merge_pull_request"]\}`. Also use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json. Needs `gh` and `python3`. Re-review before bumping the pin.

## YOLO install

YOLO (your own risk): skips the commit pin and the deny rules that block `gh pr merge` and the GitHub MCP merge tool, so full-send can merge PRs and force-push.
Copy the skills as the README says, without those deny rules.

## Install notes

Ask the user first. Copy only the skills you want: `cp -R tstack/skills/{full-stop,full-send,file-pr,babysit-pr,sol-loop,leaving-pr-comments} ~/.claude/skills/`. full-stop pulls full-send in as a dependency (README), so pair it with these settings.json deny rules: `"permissions": {"deny": ["Bash(gh pr merge:*)", "mcp__github__merge_pull_request"]}`. Needs `gh auth login` and python3.
