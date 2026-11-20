# Orca (Stably AI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/stablyai/orca
- **GitHub repo:** https://github.com/stablyai/orca
- **Price:** Free/open-source MIT app (official README License and online search checked 2026-11-07); existing agent subscription/API usage and optional remote machines/cloud cost extra. No model quota included.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @2daee44 v1.4.214 (2026-11-19): safe with fixes. Full-access defaults (src/shared/default-global-settings.ts:164,253) are settings: switch both to Ask. Telemetry stops with ORCA_TELEMETRY_DISABLED=1 (src/main/telemetry/consent.ts:52-57). Keys are encrypted via Electron safeStorage, which on Windows uses DPAPI; the plaintext fallback (encrypted-api-key-file-store.ts:120-134) is for hosts without it. Fix: Ask modes, env var, pin.

## Safe install

Safe install (fixes applied):
Windows: download orca-windows-setup.exe from the v1.4.214 release https://github.com/stablyai/orca/releases/tag/v1.4.214 (README.md:265; the reviewed 2daee44), decline in-app updates until a new version is reviewed and keep Windows signature verification on (updater-setup.ts:170). Before the first launch set ORCA_TELEMETRY_DISABLED=1 as a user environment variable (consent.ts:52-57) and decline the telemetry banner. Immediately in Settings change native chat from full access to Ask and agent permissions from full access to the agent's own prompts: the new-install default is full access (default-global-settings.ts:164,253), which launches Claude with --dangerously-skip-permissions and Hermes with --yolo. Review the event hooks Orca adds to your agent settings (hook-service.ts:123-142) and add no workspace hooks. A worktree is not a sandbox: with Ask on, every agent action still needs your OK. Leave mobile pairing, SSH and cloud machines off until a separate OK. Android: the companion APK from https://www.onorca.dev/download/android (README.md:285) only after the desktop setup is locked down. claude.ai: no route.

## YOLO install

YOLO (your own risk): skips telemetry opt-out, the permission changes and the hook review; runs with the full-access defaults.
https://github.com/stablyai/orca/releases/latest/download/orca-windows-setup.exe

## Install notes

NOT installed. User approval required before any install. Before trying: disposable repo, one agent, native chat Ask / agent Own with underlying CLI approval prompts (not full-access or YOLO), telemetry disabled via ORCA_TELEMETRY_DISABLED=1, review hooks, no production/API secrets, no mobile/cloud/SSH setup until separately approved. Worktree is not a sandbox. Windows native PowerShell/CMD support; Android paired companion (README.md:77-81).
