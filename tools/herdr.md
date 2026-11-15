# herdr

- **Type:** app
- **Category:** developer tools, agents, automation
- **Official URL:** https://herdr.dev
- **GitHub repo:** https://github.com/herdrdev/herdr @ ee5bfb5 (v0.9.5; Apache-2.0; official herdrdev repo, not a fork, not archived; master HEAD 2026-10-29 08:56 ET; later branches pushed 2026-11-07; 50,920 stars at check)
- **Price:** Free, Apache-2.0 (LICENSE; herdr.dev FAQ answers "Is it free?" with yes, checked 2026-11-14). You still pay for the coding agents you run inside it. No paid Herdr plan published at check time.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot: safe with the Install notes fixes. No usage-telemetry SDK found. Verified risks, each fixed: the official install pipes curl|sh or irm|iex (README.md:45; fix: download the release binary and check its SHA-256, which install.sh:41-114 and install.ps1:334 also require); background version and agent-detection manifest checks go to herdr.dev (src/update.rs:25-26, src/detect/manifest_update.rs:16; fix: `version_check = false` and `manifest_check = false` under [update] in config.toml, src/config/model.rs:35-44, honoured at src/app/runtime.rs:97-127); updates install only on a manual `herdr update` (src/update.rs:1-5); plugins, the socket API and remote SSH machines let agents spawn panes (fix: add no plugins and no machine profiles). Android/Termux is not supported (install.sh:24-26).

## Safe install

Safe install (fixes applied):
Windows/Claude Code: download the v0.9.5 Windows x86_64 release asset from github.com/herdrdev/herdr/releases, then check its SHA-256 against the sha256 field in herdr.dev/latest.json (`Get-FileHash`). Do not pipe `install.sh` or `install.ps1` into a shell. In config.toml set `[update] version_check = false` and `manifest_check = false`. Run `herdr update` only by hand, after a re-review. Add no plugins and no `herdr machine add` profiles. Set `DO_NOT_TRACK=1`. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json (it denies curl|sh).
Android: local binaries are not supported; SSH from the phone to a supported host instead.

## YOLO install

YOLO (your own risk): skips the SHA-256 check, the ban on piped installers, and turning off background version and manifest checks.
Windows: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` (README.md:45).

## Install notes

Ask the user before installing. Windows x86_64: download the v0.9.5 release asset from the official releases page `github.com/herdrdev/herdr/releases`, check its SHA-256 against the sha256 field in `herdr.dev/latest.json` (`Get-FileHash`), and don't pipe install.sh or install.ps1 into a shell. In herdr's config.toml set `[update]` `version_check = false` and `manifest_check = false`. Run `herdr update` only by hand, after a re-review. Add no plugins and no `herdr machine add` profiles. Android: not supported (SSH from the phone to a supported host instead). Hermes compatibility untested.
