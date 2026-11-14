# Postiz agent (MCP + CLI + skill)

- **Type:** MCP
- **Category:** social posting
- **Official URL:** https://postiz.com
- **GitHub repo:** [https://github.com/gitroomhq/postiz-agent](https://github.com/gitroomhq/postiz-agent)
- **Price:** Self-host free (AGPL); cloud from $29/mo, 7-day trial, no free plan (postiz.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 17f1e27, a project a review, 2026-10-30): Use with caution. The skill tells the agent to run `npm install -g postiz` unpinned if missing; the CLI passes the auth server's verification_uri into a shell exec; the skill and CLI push a separate agent-media CLI. No telemetry or exfiltration found. It posts to your social accounts (IG, YT, TikTok).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
