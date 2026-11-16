# Orca (Stably AI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/stablyai/orca
- **GitHub repo:** https://github.com/stablyai/orca
- **Price:** Free/open-source MIT app (official README License and online search checked 2026-11-07); existing agent subscription/API usage and optional remote machines/cloud cost extra. No model quota included.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted code read @2daee44e, not full dependency/binary audit. CAUTION: new-install defaults are full-access for native chat and agent permissions (src/shared/default-global-settings.ts:164,253); Claude full-access passes --dangerously-skip-permissions (src/main/claude/structured/launch/claude-structured-launch-resolution.ts:106-108), Hermes uses --yolo (src/shared/agent-launch/permissions/tui-agent-permissions.ts:38). Worktrees separate branches/files, NOT a security sandbox. Agent processes can access local files/credentials/network under the host account. Telemetry: PostHog host src/main/telemetry/posthog-transport.ts:82; consent.ts:78-90 waits for banner/choice, env DO_NOT_TRACK=1 or ORCA_TELEMETRY_DISABLED=1 overrides at :52-57. Banner acknowledgement can opt in (src/preload/api/telemetry-api.ts:57-58). Credentials: src/main/credentials/encrypted-api-key-file-store.ts:123 encrypts via secret store, :130-134 falls back to plaintext if unavailable (not an unconditional encrypted vault). Hooks: src/main/claude/hook-service.ts:123-142 installs managed event hooks in agent settings; workspace hooks can execute shell scripts (src/main/workspace-hooks/worktree-runner-script.ts:146; effective-hook-config.ts:35-44). Build postinstall compiles packages/native deps (package.json:166). Updates: docs/install says auto-update by default; updater/lifecycle/updater-setup.ts:149 sets low-level autoDownload=false and :155-158 controls install/relaunch; do not assume no update machinery. Windows signature verification intentionally retained (:170). No first-party curl-to-shell install instruction or general eval call found in targeted README/docs/main scan (not a dependency/binary audit). No fix: agents launched by Orca have your full user rights (worktrees only separate files), and saved API keys fall back to a plaintext file when no OS secret store is available (encrypted-api-key-file-store.ts:130-134); contained by Ask permissions, no saved keys and a disposable repo.

## Safe install

Safe install (fixes applied):
Windows: download orca-windows-setup.exe from https://github.com/stablyai/orca/releases/latest (README.md:265) and keep Windows signature verification on (updater-setup.ts:170). Before the first launch set ORCA_TELEMETRY_DISABLED=1 as a user environment variable (consent.ts:52-57) and decline the telemetry banner. Immediately in Settings change native chat from full access to Ask and agent permissions from full access to the agent's own prompts: the new-install default is full access (default-global-settings.ts:164,253), which launches Claude with --dangerously-skip-permissions and Hermes with --yolo. Review the event hooks Orca adds to your agent settings (hook-service.ts:123-142) and add no workspace hooks. Use one disposable repo, one agent, no production keys; a worktree is not a sandbox. Leave mobile pairing, SSH and cloud machines off until a separate OK. Android: the companion APK from https://www.onorca.dev/download/android (README.md:285) only after the desktop setup is locked down. claude.ai: no route.

## YOLO install

YOLO (your own risk): skips telemetry opt-out, the permission changes and the hook review; runs with the full-access defaults.
https://github.com/stablyai/orca/releases/latest/download/orca-windows-setup.exe

## Install notes

NOT installed. User approval required before any install. Before trying: disposable repo, one agent, native chat Ask / agent Own with underlying CLI approval prompts (not full-access or YOLO), telemetry disabled via ORCA_TELEMETRY_DISABLED=1, review hooks, no production/API secrets, no mobile/cloud/SSH setup until separately approved. Worktree is not a sandbox. Windows native PowerShell/CMD support; Android paired companion (README.md:77-81).
