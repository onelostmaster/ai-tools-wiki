# Hermes official plugins (monorepo, 18 plugins)

- **Type:** plugin
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins (seen @ a50b0fe on 2026-11-02 with accent-picker and bubblewrap folders; see their own rows)
- **Price:** Free plugin code; unverified: which plugins call paid vendor APIs; containment: read each plugin's README before enabling it, and set a spend limit on any API key you give it
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read, a project a review, #3, #16): Looks safe. Nous-maintained, catalog SHA-pinned. Only 5 of the 18 were spot-checked (xchat, camofox, meshy, elevenlabs, advanced-delegation): network only to the vendor APIs. `meshy/mcp.json` runs `npx @meshy-ai/meshy-mcp-server@0.6.5` (third-party code, not reviewed).

## Safe install

Safe install (fixes applied):
Hermes: hermes plugins install <name> from the official catalog (README:47; the catalog is SHA-pinned). Vendor keys go in Hermes secrets, never in chat. Only xchat, camofox, meshy, elevenlabs and advanced-delegation were spot-checked ; unverified: the other 13, so install those only after their own review. Keep meshy's MCP pin at @meshy-ai/meshy-mcp-server@0.6.5.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install <name>`, where `<name>` is the plugin's name in the official catalog (README:47; installs at the reviewed pin). Vendor API keys go in secrets/env vars, never in chat.
