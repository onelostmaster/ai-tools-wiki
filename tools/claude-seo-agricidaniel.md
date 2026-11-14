# claude-seo (AgriciDaniel)

- **Type:** skill
- **Category:** research, building a site
- **Official URL:** https://github.com/AgriciDaniel/claude-seo
- **GitHub repo:** https://github.com/AgriciDaniel/claude-seo @ 6be93f4 (MIT; not a fork)
- **Price:** Free, MIT (github.com, checked 2026-11-02); optional extensions use paid APIs (DataForSEO, Firecrawl, Ahrefs, SE Ranking, Moz and others, per `PRIVACY.md`).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @6be93f4, a review, 2026-11-02): caution. A PostToolUse hook runs a local Python schema check after every Edit/Write (`hooks/hooks.json:3-5`; `validate-schema.py` only reads the file). Google sign-in asks for full Search Console (webmasters), Indexing and Analytics read scopes (`scripts/google_auth.py:51-55`). Uninstall tip is curl|bash (`install.sh:211`). PRIVACY.md says no telemetry; none found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: per its README; avoid the curl|bash install/uninstall; grant Google scopes only if needed.
