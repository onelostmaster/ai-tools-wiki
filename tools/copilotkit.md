# CopilotKit

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://copilotkit.ai
- **GitHub repo:** https://github.com/CopilotKit/CopilotKit @ 35a9dd9 (MIT)
- **Price:** Library free (MIT); CopilotKit Cloud Developer free, Pro $39/mo, Team $100 per seat a month (copilotkit.ai, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @35a9dd9, a review, 2026-11-02): caution. Sends telemetry to telemetry.copilotkit.ai (packages/web-inspector/src/lib/telemetry.ts:92) unless COPILOTKIT_TELEMETRY_DISABLED=1 or DO_NOT_TRACK=1 (packages/shared/src/telemetry/telemetry-disabled.ts:14-20). README onboarding uses unpinned npx copilotkit@latest. Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (COPILOTKIT_TELEMETRY_DISABLED=1 (or DO_NOT_TRACK=1) set before first run, pinned packages, pinned npx copilotkit@<version> not @latest); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: npm install @copilotkit/react-core@<release matching 35a9dd9> @copilotkit/runtime@<same release> (README). Set COPILOTKIT_TELEMETRY_DISABLED=1 (or DO_NOT_TRACK=1) before first run; otherwise it sends telemetry to telemetry.copilotkit.ai (packages/web-inspector/src/lib/telemetry.ts:92; packages/shared/src/telemetry/telemetry-disabled.ts:14-20). Use a pinned npx copilotkit@<version>, not @latest, for onboarding. Android: no.

## YOLO install

YOLO (your own risk): skips the version pins and the telemetry switch.
Windows: npx copilotkit@latest and default npm install; telemetry to telemetry.copilotkit.ai stays on.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: npm install @copilotkit/react-core @copilotkit/runtime (README); set COPILOTKIT_TELEMETRY_DISABLED=1. Android: no.
