# agent-browser

- **Type:** CLI
- **Category:** developer tools, automation, agents
- **Official URL:** https://agent-browser.dev
- **GitHub repo:** https://github.com/vercel-labs/agent-browser @ f18b8bb (v0.43.0; Apache-2.0; official Vercel Labs repo, not a fork, not archived; default-branch commit 2026-11-13 20:11 ET; 50,960 stars at check)
- **Price:** Free, Apache-2.0 (LICENSE, npm and agent-browser.dev, checked 2026-11-14). Runs locally. Optional cloud browser providers (Browserbase, Browserless and others) bill separately.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @f18b8bb, v0.43. No usage-telemetry SDK in the Rust CLI. Verified risks, each fixed: postinstall downloads a GitHub release binary, with no checksum check, only when the platform package is missing (scripts/postinstall.js:41-43,115-137; fix: pinned npm install, the Windows x64 package ships the binary, :103-114); `--cdp`, `--auto-connect` and `--profile` drive an existing, signed-in Chrome (security.mdx:36; fix: never pass them); navigation, action and output limits are off by default (security.mdx:8; fix: `--allowed-domains`, `--action-policy` denying eval, `--confirm-actions`, `--content-boundaries`, `--max-output`); a Chrome release-blog version check (fix: `AGENT_BROWSER_NO_VERSION_CHECK=1`); `--no-sandbox` is added when CI is set, as root or in containers (cli/src/native/cdp/chrome.rs:1727-1751; fix: run as a normal Windows user with CI unset); stealth/captcha plugins and the auth vault (security.mdx:44-126; fix: don't install or use them).

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder, `npm install -E --ignore-scripts agent-browser@0.43.0` (the Windows x64 optional package ships the binary, so postinstall does not download). Then `npx agent-browser install` for Chrome for Testing. Set `AGENT_BROWSER_NO_VERSION_CHECK=1` and `DO_NOT_TRACK=1`, and leave `CI` unset. Run as a normal user, not as Administrator. Always pass `--allowed-domains` with only the site you are testing, `--action-policy` that denies eval, `--confirm-actions`, `--content-boundaries` and `--max-output`. Never pass `--cdp`, `--auto-connect` or `--profile`. Do not use the auth vault or stealth/captcha plugins. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json. Re-review before bumping the pin.

## YOLO install

YOLO (your own risk): skips the pin, --ignore-scripts, AGENT_BROWSER_NO_VERSION_CHECK=1, the domain/action/output limits, and the ban on attach modes and plugins.
`npm install -g agent-browser`, then `agent-browser install` (README / agent-browser.dev/installation).

## Install notes

Ask the user before installing. Windows: `npm install -E agent-browser@0.43.0` inside the project (the Windows x64 package ships the binary, so postinstall downloads nothing), then `npx agent-browser install` for Chrome for Testing. Run it as a normal user with the env var CI unset, and set `AGENT_BROWSER_NO_VERSION_CHECK=1`. Always pass `--allowed-domains` with only the site you are testing, `--action-policy` that denies eval, `--confirm-actions`, `--content-boundaries` and `--max-output`. Never pass `--cdp`, `--auto-connect` or `--profile` (they attach to a logged-in Chrome), don't use the auth vault, and don't install stealth or captcha plugins. Optional paid cloud browsers are separate. Android: no. Hermes compatibility untested.
