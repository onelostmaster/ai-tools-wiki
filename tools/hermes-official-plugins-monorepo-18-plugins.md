# Hermes official plugins (monorepo, 18 plugins)

- **Type:** plugin
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins (seen @ a50b0fe on 2026-11-02 with accent-picker and bubblewrap folders; see their own rows)
- **Price:** Free plugin code; vendor API usage may cost (not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read, a project a review, #3, #16): Looks safe. Nous-maintained, catalog SHA-pinned. Only 5 of the 18 were spot-checked (xchat, camofox, meshy, elevenlabs, advanced-delegation): network only to the vendor APIs. `meshy/mcp.json` runs `npx @meshy-ai/meshy-mcp-server@0.6.5` (third-party code, not reviewed).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install <name>`, where `<name>` is the plugin's name in the official catalog (README:47; installs at the reviewed pin). Vendor API keys go in secrets/env vars, never in chat.
