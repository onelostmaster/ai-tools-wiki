# Bubblewrap terminal backend (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, security
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/bubblewrap
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins (folder bubblewrap) @ a50b0fe (MIT; v1.3.0; needs Hermes 0.22.6+)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @a50b0fe, Hermes a review, 2026-11-02): safe. Hides credential stores like .ssh, .aws, .config/gh and .git-credentials (`bubblewrap/README.md:112-113`); subprocess calls only start bwrap (`sandbox.py:996,1761`). Default profile is "network" (host network on); pick "restricted" or "workspace" to cut the network (`plugin.yaml` config_schema).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Hermes: Linux only, Hermes 0.22.6+; choose the restricted or workspace profile for untrusted work.
Windows: WSL at most (not tested). Android: no.
