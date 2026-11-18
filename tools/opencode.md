# opencode

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://opencode.ai
- **GitHub repo:** https://github.com/anomalyco/opencode @ 21e66f2 (MIT; formerly sst/opencode)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model providers bill separately
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Claude docs read @1cb0633 v2.3.0 (2026-11-17): safe with fixes. Most permissions default to allow, so bash and edits run without asking (services/site/src/docs/v1/content/permissions.mdx:174-177). experimental.image_generate turns paid image calls on or off (packages/schema/src/config/experimental.ts:34). autoupdate false stops update checks (config.mdx:629-634). Fix: ask rules, image off, pinned version.

## Safe install

Safe install (fixes applied):
npm install @opencode/cli@2.3.0 in a tools folder (no -g, no curl|bash); opencode.json: \{"permission":\{"bash":"ask","edit":"ask","webfetch":"ask"\},"experimental":\{"image_generate":false\},"autoupdate":false\}.

## YOLO install

YOLO (your own risk): skips the ask rules, image off and the pin.
curl -fsSL https://opencode.ai/v2/install | bash with default allow.

## Install notes

Ask the user before installing. npm install @opencode/cli@2.3.0 in a tools folder (no -g, no curl|bash); opencode.json: \{"permission":\{"bash":"ask","edit":"ask","webfetch":"ask"\},"experimental":\{"image_generate":false\},"autoupdate":false\}.
