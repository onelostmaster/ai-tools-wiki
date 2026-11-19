# HyperFrames

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/heygen-com/hyperframes
- **GitHub repo:** [https://github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- **Price:** Free framework; optional paid HeyGen (not verified)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @6741072 v0.9.66 (2026-11-18): safe with fixes. HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 stops PostHog (packages/cli/src/telemetry/policy.ts:6-32). The skill tells the agent to post feedback to a public channel after renders unless telemetry is off (skills/hyperframes-cli/references/feedback.md:3). Auto-install stops with HYPERFRAMES_NO_UPDATE_CHECK=1 (utils/autoUpdate.ts:350). Fix: those env vars, pin.

## Safe install

Safe install (fixes applied):
Env HYPERFRAMES_NO_TELEMETRY=1 and HYPERFRAMES_NO_UPDATE_CHECK=1 and HYPERFRAMES_NO_AUTO_INSTALL=1; run as npx hyperframes@0.9.66; never hyperframes feedback --file-issue.

## YOLO install

YOLO (your own risk): skips the env vars and pin.
Install latest and let the skill post feedback after every render.

## Install notes

Ask the user before installing.
Claude Code: no steps given (the source withholds them for caution items).
