# oh-my-hermes

- **Type:** plugin
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/rlaope/oh-my-hermes
- **GitHub repo:** [https://github.com/rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (targeted code read, a project a review, #50 at b906cb4, #58 at 812ec53): Use with caution. Too big to fully audit; no telemetry or data exfiltration found. Installer is `curl|sh` / `irm|iex` pulling latest main with no checksum; the plugin registers Hermes hooks on every session and tool call; self-update machinery (an 'auto' mode is offered in setup); optional `omh_jev_ask` sends your questions plus your key to `api.typesafe.ai` or `openrouter.ai`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
Hermes: a review bot gave no steps (verdict isn't Looks safe); the project's own installer is `curl|sh` / `irm|iex` from latest main, which the Safety reason flags.
