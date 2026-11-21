# Vibe Kanban (BloopAI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/BloopAI/vibe-kanban
- **GitHub repo:** https://github.com/BloopAI/vibe-kanban @ 7c38070 (Apache-2.0; committed 2026-10-28; community-maintained since the company shut down)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); the paid cloud closed in May 2026
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @7c38070 + 0.1.46 diff (2026-11-20): safe with fixes. Found: the default Claude profile adds --dangerously-skip-permissions (crates/executors/default_profiles.json:3-9); a profiles.json override is merged (crates/executors/src/profile.rs:278-299) and approvals:true routes each tool call to you (claude.rs:166-172). 0.1.46 removes PostHog and Sentry (5f06193e); binaries are SHA-256 checked (npx-cli/src/download.ts:132).

## Safe install

Safe install (fixes applied):
Windows (Node.js 18+): npx vibe-kanban@0.1.46 (npm latest; 0.1.45 was pulled from npm; 0.1.46 has PostHog analytics and Sentry crash reports removed, commit 5f06193e, and checks each downloaded binary's SHA-256 against GitHub releases, npx-cli/src/download.ts:16-17,132). Before the first task, open Settings > Agents and set the Claude Code DEFAULT profile to "dangerously_skip_permissions": false, "approvals": true (the shipped default skips permissions, crates/executors/default_profiles.json:3-9); do the same for any other agent you enable (Gemini/Qwen yolo, Codex danger-full-access, Amp allow-all in that file). Approve each tool call in its UI. Use one repo you can lose, no production keys. Android and claude.ai: no.

## YOLO install

YOLO (your own risk): skips the permission-profile change; agents run with --dangerously-skip-permissions or their yolo modes.
npx vibe-kanban with defaults.

## Install notes

Ask the user before installing.
Windows: `npx vibe-kanban` (README), needs Node; turn analytics off in settings. Android: no.
