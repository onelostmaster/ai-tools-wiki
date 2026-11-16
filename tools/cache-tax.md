# Cache Tax

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/karanb192/cache-tax
- **GitHub repo:** [https://github.com/karanb192/cache-tax](https://github.com/karanb192/cache-tax) (read at e4940af)
- **Price:** Free (MIT open-source code); keepwarm pings spend your Claude usage
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @771b3d8 (2026-11-15): safe with fixes, Skip. No network beyond the model. By default a paid cold write arms keepwarm for three hours of background pings that spend your usage. Fix: set the Auto keepwarm option to off in /config, so keepwarm runs only when you arm it with /keepwarm and a short window; /keepwarm off stops it.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add karanb192/claude-code-mods#fb1f9c0, claude plugin install cache-tax@claude-code-mods; then /config > cache-tax > Auto keepwarm = off. Arm by hand only, for example /keepwarm 90m.

## YOLO install

YOLO (your own risk): skips the pin and Auto keepwarm off, so pings spend usage after every cold write.
Install from the marketplace with defaults.

## Install notes

Ask the user before installing. claude plugin marketplace add karanb192/claude-code-mods#fb1f9c0, claude plugin install cache-tax@claude-code-mods; then /config > cache-tax > Auto keepwarm = off. Arm by hand only, for example /keepwarm 90m.
