# claude-seo (AgriciDaniel)

- **Type:** skill
- **Category:** research, building a site
- **Official URL:** https://github.com/AgriciDaniel/claude-seo
- **GitHub repo:** https://github.com/AgriciDaniel/claude-seo @ 6be93f4 (MIT; not a fork)
- **Price:** Free, MIT (github.com, checked 2026-11-02); optional extensions use paid APIs (DataForSEO, Firecrawl, Ahrefs, SE Ranking, Moz and others, per `PRIVACY.md`).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @468ed5b (2026-11-16): safe with fixes. The PostToolUse hook only runs a local schema check after Edit/Write (hooks/hooks.json). Google sign-in now asks for read-only Search Console and Analytics (scripts/google_auth.py:60) and adds Indexing only when you ask (line 552). The README's one-liner is curl into a file then run (README.md:225-231): use the plugin route. Fits the website project.

## Safe install

Safe install (fixes applied):
/plugin marketplace add AgriciDaniel/claude-seo#468ed5b, /plugin install claude-seo@agricidaniel-claude-seo; grant only the read-only Google scopes; paid SEO API keys in env.

## YOLO install

YOLO (your own risk): skips the pin and scope limit.
Run the curl install script and grant Indexing.

## Install notes

Ask the user before installing.
Claude Code: per its README; avoid the curl|bash install/uninstall; grant Google scopes only if needed.
