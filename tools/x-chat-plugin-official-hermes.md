# X Chat plugin (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, messaging
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/xchat
- **GitHub repo:** [https://github.com/NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins)
- **Price:** Free plugin; X API pricing unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, a project a review and Hermes a review, 2026-10-28): Looks safe. Talks only to `api.x.ai` and `api.x.com`; E2EE keys stored with 0600 permissions; the allowlist defaults to your own self-chat. Heads-up: setting `XCHAT_ALLOW_ALL_USERS` would let anyone DM-prompt your agent.

## Safe install

Safe install (fixes applied):
Hermes: `hermes plugins install xchat` (hermes-official-plugins README:147, checked 2026-11-14), then `hermes xchat setup` (README:148) to see which account it runs as. Leave XCHAT_ALLOW_ALL_USERS unset so only your self-chat can prompt the agent. Use a separate X account if you do not want Hermes acting as your main account. Needs an X developer app with chat API access (README:148). Other platforms: Hermes only.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install xchat` (README:147); never set `XCHAT_ALLOW_ALL_USERS`.
