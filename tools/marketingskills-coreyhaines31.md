# marketingskills (coreyhaines31)

- **Type:** skill
- **Category:** social posting, building a site
- **Official URL:** https://github.com/coreyhaines31/marketingskills
- **GitHub repo:** https://github.com/coreyhaines31/marketingskills @ 88c79f6 (MIT; not a fork)
- **Price:** Free, MIT (github.com, checked 2026-11-02); sponsor tools named in ai-seo are paid.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @88c79f6, a review, 2026-11-02): safe. The five named skills are only Markdown and evals JSON; no hooks or scripts. ai-seo names sponsor tools Omnia (`SKILL.md:411,425`) and Ploy (`references/agent-readiness.md:79`), disclosed as paid partners (`README.md:17`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: use the repo's /plugin route (per a review) rather than the npx skills CLI.
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
