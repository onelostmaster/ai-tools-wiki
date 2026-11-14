# CopilotKit

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://copilotkit.ai
- **GitHub repo:** https://github.com/CopilotKit/CopilotKit @ 35a9dd9 (MIT)
- **Price:** Library free (MIT); CopilotKit Cloud Developer free, Pro $39/mo, Team $100 per seat a month (copilotkit.ai, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @35a9dd9, a review, 2026-11-02): caution. Sends telemetry to `telemetry.copilotkit.ai` (`packages/web-inspector/src/lib/telemetry.ts:92`) unless COPILOTKIT_TELEMETRY_DISABLED=1 or DO_NOT_TRACK=1 (`packages/shared/src/telemetry/telemetry-disabled.ts:14-20`). README onboarding uses unpinned npx copilotkit@latest.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `npm install @copilotkit/react-core @copilotkit/runtime` (README); set COPILOTKIT_TELEMETRY_DISABLED=1. Android: no.
