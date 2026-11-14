# Orca (Stably AI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/stablyai/orca
- **GitHub repo:** https://github.com/stablyai/orca
- **Price:** Free/open-source MIT app (official README License and online search checked 2026-11-07); existing agent subscription/API usage and optional remote machines/cloud cost extra. No model quota included.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted code read @2daee44e, not full dependency/binary audit. CAUTION: new-install defaults are full-access for native chat and agent permissions (src/shared/default-global-settings.ts:164,253); Claude full-access passes --dangerously-skip-permissions (src/main/claude/structured/launch/claude-structured-launch-resolution.ts:106-108), Hermes uses --yolo (src/shared/agent-launch/permissions/tui-agent-permissions.ts:38). Worktrees separate branches/files, NOT a security sandbox. Agent processes can access local files/credentials/network under the host account. Telemetry: PostHog host src/main/telemetry/posthog-transport.ts:82; consent.ts:78-90 waits for banner/choice, env DO_NOT_TRACK=1 or ORCA_TELEMETRY_DISABLED=1 overrides at :52-57. Banner acknowledgement can opt in (src/preload/api/telemetry-api.ts:57-58). Credentials: src/main/credentials/encrypted-api-key-file-store.ts:123 encrypts via secret store, :130-134 falls back to plaintext if unavailable (not an unconditional encrypted vault). Hooks: src/main/claude/hook-service.ts:123-142 installs managed event hooks in agent settings; workspace hooks can execute shell scripts (src/main/workspace-hooks/worktree-runner-script.ts:146; effective-hook-config.ts:35-44). Build postinstall compiles packages/native deps (package.json:166). Updates: docs/install says auto-update by default; updater/lifecycle/updater-setup.ts:149 sets low-level autoDownload=false and :155-158 controls install/relaunch; do not assume no update machinery. Windows signature verification intentionally retained (:170). No first-party curl-to-shell install instruction or general eval call found in targeted README/docs/main scan (not a dependency/binary audit).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

NOT installed. User approval required before any install. Before trying: disposable repo, one agent, native chat Ask / agent Own with underlying CLI approval prompts (not full-access or YOLO), telemetry disabled via ORCA_TELEMETRY_DISABLED=1, review hooks, no production/API secrets, no mobile/cloud/SSH setup until separately approved. Worktree is not a sandbox. Windows native PowerShell/CMD support; Android paired companion (README.md:77-81).
