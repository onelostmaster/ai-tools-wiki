# Onyx

- **Type:** app
- **Category:** research, Notion and productivity
- **Official URL:** https://onyx.app
- **GitHub repo:** https://github.com/onyx-dot-app/onyx @ 3eb6420 (MIT Community Edition plus a separate Enterprise Edition; latest commit on 2026-10-31; the post's card links `senlindesign/taste-skill` by mistake)
- **Price:** Community Edition free to self-host; Business $20 per user/month billed annually; Enterprise custom (`onyx.app`, checked 2026-11-01).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-01

## Safety reason

a review bot (vendor README and pricing page, 2026-11-01): safe. Official product of Onyx, MIT Community Edition. Quick install is `curl -fsSL https://onyx.app/install_onyx.sh | bash` (read it first); it indexes your connected documents and sends queries to the LLM you configure; Onyx Cloud keeps your data with Onyx.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Server (Docker): `curl -fsSL https://onyx.app/install_onyx.sh | bash`, or the Docker, Kubernetes and Helm guides at https://docs.onyx.app (README).
Claude Code: point it at your Onyx server's MCP endpoint (README; steps in the Onyx docs).
