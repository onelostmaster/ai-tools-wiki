# Lots of Sounds (lotsofsounds)

- **Type:** plugin
- **Category:** voice and audio
- **Official URL:** https://www.lotsofsounds.com
- **GitHub repo:** https://github.com/lotsofsounds/agent-skills @ 342a2bf (MIT; the scout gave only the name; this is the vendor's own agent plugin, matching its "unpinned npx CLI")
- **Price:** Free tier (10 downloads/day, no API); Pro $15/month or $150/year; Enterprise $49/month (lotsofsounds.com, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-10-31

## Safety reason

a project tool scout (2026-10-31): ❌ ★★: a hosted service with a login and an unpinned `npx` CLI. Not code-reviewed. Its README: `npx lotsofsounds login` opens a browser sign-in; the CLI saves your API key and email in `~/.config/lotsofsounds/config.json`; searches and the key go to `api.lotsofsounds.com`, which keeps usage records with your search words.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: `/plugin marketplace add lotsofsounds/agent-skills` then `/plugin install lotsofsounds@lotsofsounds` (README); full search and downloads need an account (`npx lotsofsounds login`).
