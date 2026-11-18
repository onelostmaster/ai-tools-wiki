# revid-skills (Revid MCP plugin)

- **Type:** plugin
- **Category:** generating videos, social posting
- **Official URL:** https://www.revid.ai/mcp
- **GitHub repo:** https://github.com/tmakersas/revid-skills @ 745cbfc (MIT)
- **Price:** Plugin free, MIT; the Revid service is paid (a project report), plan prices unknown (not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed for safety. Front end for a paid hosted service that can post to social accounts (per the repo description); a project Tool Scout (Claude, 2026-11-03) rated it for fit only. Repo and homepage confirmed from github.com metadata, 2026-11-03.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: read it on GitHub first (https://github.com/tmakersas/revid-skills @ 745cbfc); if you try it, install it at that exact commit only in a throwaway Claude Code project in a devcontainer or WSL sandbox (not your main Claude Code config on Windows), no API keys in its env except a separate Revid key you can revoke, and connect no social accounts (its repo says it can post to them), no network unless a step needs it, and do not run its install scripts. Get a review before real use. Android: no.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Needs a Revid account; it can post publicly to your social accounts, so keep posting off unless you approve each post.
