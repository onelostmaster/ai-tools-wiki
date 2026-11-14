# Trail of Bits skills (trailofbits/skills)

- **Type:** plugin
- **Category:** security, developer tools
- **Official URL:** https://github.com/trailofbits/skills
- **GitHub repo:** https://github.com/trailofbits/skills @ 711af09 (CC-BY-SA-4.0)
- **Price:** Free, CC-BY-SA-4.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @711af09, a review, 2026-11-02): safe. Some plugins change your setup: modern-python adds PATH shims (`setup-shims.sh:24`); gh-cli hooks intercept GitHub fetches and clean up clones (`cleanup-clones.sh:17-21`). Semgrep runs with --metrics=off.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: add the marketplace and install only the plugins you need, per its README.
Windows: works in Claude Code on Windows (shims and hooks assume a Unix shell; not tested). Android: no.
