# Accent Picker plugin (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, design
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/accent-picker
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins (folder accent-picker) @ a50b0fe (MIT; v1.0.0)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @a50b0fe, Hermes a review, 2026-11-02): safe. No agent tools, hooks or env vars (`accent-picker/plugin.yaml`); no fetch, eval, new Function or URLs in `desktop/plugin.js` (298 lines); no install scripts in package.json.

## Safe install

Safe install (fixes applied):
Hermes Desktop (Windows): Capabilities -> Plugins, search accent-picker, install, then flip its switch; or `hermes plugins install accent-picker` (accent-picker/README.md:17-25). Both install at the catalog's reviewed pin (repo README.md:42-47). It only copies desktop/plugin.js into ~/.hermes/desktop-plugins/ (accent-picker/README.md:25); no agent tools, hooks or env vars (plugin.yaml). Nothing to fix. claude.ai, Claude Code, Android: no.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Hermes: turn it on from Hermes Desktop's Capabilities catalog.
Windows: works in Hermes Desktop. Android: no.
