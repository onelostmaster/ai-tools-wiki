# Anthropic TypeScript SDK

- **Type:** library
- **Category:** developer tools, AI
- **Official URL:** https://github.com/anthropics/anthropic-sdk-typescript
- **GitHub repo:** https://github.com/anthropics/anthropic-sdk-typescript
- **Price:** SDK code free; reviewed current version 1.6.0 Apache-2.0 (README.md:58-60, package.json:11). Earlier releases/contributions retain MIT via LICENSE-MIT; do not blindly call current SDK MIT. API requests billed separately; official pricing https://platform.claude.com/docs/en/about-claude/pricing checked online 2026-11-08. Existing Claude subscription does not imply API quota. No model-rate quote needed.
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

CAUTION: a cloud API client, not local-only review. The quoted review script sends MOTION.md and the supplied source file to the API and consumes billed tokens. SDK src/client.ts:989-1037 reads API key/baseURL environment and defaults to api.anthropic.com, rejects browsers unless dangerouslyAllowBrowser is set; :1636 sends network requests. Keep keys server-side, leave browser override off, verify baseURL, and redact private code/secrets. SDK v1.6.0 has OpenTelemetry support: src/internal/tracing.ts:196-230 enables spans/propagation unless disabled, defaults contentMode to metadata_only, uses the app/global tracer provider; this does not prove automatic export to an SDK-owned collector. Set openTelemetry:false for no SDK spans/propagation. Debug logging can include request options/body; internal/utils/log.ts:115-160 redacts listed auth/cookie headers, NOT arbitrary prompt secrets. Avoid debug/content tracing. package.json:27 prepare executes build/git-swap for git installs; no automatic updater/permission bypass found in targeted core scan. No API call or repo script run. Not a full auth/dependency/exporter audit.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

CAUTION: show Safety reason and ask before installing/using. Documentation only, NOT run: npm install @anthropic-ai/sdk (README.md:14). Current source supports Node 20+ non-EOL, TypeScript 5+ (README). API key must stay server-side; no user key read or requested. Prefer published reviewed version, not git-install prepare hook; set openTelemetry:false, avoid debug/content logging, keep dangerouslyAllowBrowser false, verify endpoint, sanitize source before any API request and set a usage budget. Agent-written calling code possible in Claude Code/Hermes; no bundled MCP or tested agent integration; no direct claude.ai/Android-native installation route. Do not execute the article npx tsx review snippet without reviewing/pinning its separate runner/dependencies.
