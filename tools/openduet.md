# OpenDuet

- **Type:** app
- **Category:** automation, Notion and productivity
- **Official URL:** https://copilotkit.ai/openduet
- **GitHub repo:** https://github.com/CopilotKit/OpenDuet (MIT)
- **Price:** Free, open source (MIT); needs a CopilotKit Intelligence account: free hosted tier 1,000 interactions a month, paid hosted from $49/month (copilotkit.ai, checked 2026-11-01), plus your own model key or Claude subscription.
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @b32ec10 (2026-11-16): safe with fixes, Skip. The supervisor and SPIRE agent mount the Docker socket (openbot/docker-compose.yml:181, 252); :ro does not limit the API, so that is host control. Fix: point ENGINE_SOCKET at rootless Podman (the compose notes cover it) or run in a VM. Telemetry off with COPILOTKIT_TELEMETRY_DISABLED=true (openbot/desktop/TELEMETRY.md:3). Threads and memory live in CopilotKit Intelligence.

## Safe install

Safe install (fixes applied):
Dedicated VM or rootless Podman with ENGINE_SOCKET=$XDG_RUNTIME_DIR/podman/podman.sock; env COPILOTKIT_TELEMETRY_DISABLED=true; clone at b32ec10; use npx copilotkit@4.34.0 instead of @latest; connect Gmail only if needed.

## YOLO install

YOLO (your own risk): skips the VM or rootless engine and telemetry off, so the supervisor controls your host Docker.
Follow the README on your main machine.

## Install notes

Ask the user before installing.
Claude Code: no install steps given (the source withholds them until the tool is rated safe); it runs as a self-hosted Docker app on the Claude Agent SDK, see the official repo https://github.com/CopilotKit/OpenDuet.
