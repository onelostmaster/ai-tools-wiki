# Bubblewrap terminal backend (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, security
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/bubblewrap
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins (folder bubblewrap) @ a50b0fe (MIT; v1.3.0; needs Hermes 0.22.6+)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @a50b0fe, Hermes a review, 2026-11-02): safe. Hides credential stores like .ssh, .aws, .config/gh and .git-credentials (`bubblewrap/README.md:112-113`); subprocess calls only start bwrap (`sandbox.py:996,1761`). Default profile is "network" (host network on); pick "restricted" or "workspace" to cut the network (`plugin.yaml` config_schema).

## Safe install

Safe install (fixes applied):
Hermes (Linux, Hermes 0.22.6+; on Windows only inside WSL, untested): `sudo apt install bubblewrap` (0.9.0+), then `hermes plugins install bubblewrap` (catalog install at the reviewed pin) and `hermes config set terminal.backend bubblewrap` (bubblewrap/README.md:17-25). Do not use `hermes plugins install NousResearch/hermes-official-plugins#bubblewrap`: that installs straight from main, not a reviewed pin (bubblewrap/README.md:28-29). Verified: the default profile is "network", which shares the host network with no egress filter (README.md:214, 243-249). Fix: `hermes config set plugins.entries.bubblewrap.settings.profile workspace` (or restricted for read-only work) and switch to network only for jobs that need it. Check with `hermes doctor` that the sandbox probe passes. claude.ai, Claude Code, Android: no.

## YOLO install

YOLO (your own risk): skips the reviewed-pin install and the no-network profile (keeps host network on).
hermes plugins install NousResearch/hermes-official-plugins#bubblewrap; hermes config set terminal.backend bubblewrap

## Install notes

Safe, but ask the user before installing.
Hermes: Linux only, Hermes 0.22.6+; choose the restricted or workspace profile for untrusted work.
Windows: WSL at most (not tested). Android: no.
