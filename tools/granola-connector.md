# Granola (connector)

- **Type:** connector
- **Category:** Notion and productivity
- **Official URL:** https://www.granola.ai
- **GitHub repo:** unknown
- **Price:** Basic free (MCP reaches only the last 30 days; transcript and folder tools need a paid plan); Business $14/user/month; Enterprise $35/user/month (`granola.ai`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

Granola (official vendor connector; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Granola's docs: it reads your meeting notes and transcripts as you (OAuth) and can add or remove notes from folders; Granola trains on anonymized user data unless you opt out in Settings.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): already connected on the Claude account; elsewhere: Settings > Connectors, search Granola, connect (Granola docs).
Claude Code: `claude mcp add granola --transport http https://mcp.granola.ai/mcp`, then `/mcp` > Authenticate (Granola docs).
