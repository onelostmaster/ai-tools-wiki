# marketingskills (coreyhaines31)

- **Type:** skill
- **Category:** social posting, building a site
- **Official URL:** https://github.com/coreyhaines31/marketingskills
- **GitHub repo:** https://github.com/coreyhaines31/marketingskills @ 88c79f6 (MIT; not a fork)
- **Price:** Free, MIT (github.com, checked 2026-11-02); sponsor tools named in ai-seo are paid.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @88c79f6, a review, 2026-11-02): safe. The five named skills are only Markdown and evals JSON; no hooks or scripts. ai-seo names sponsor tools Omnia (`SKILL.md:411,425`) and Ploy (`references/agent-readiness.md:79`), disclosed as paid partners (`README.md:17`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy only the skill folders you want (e.g. skills/copywriting, skills/cro) from reviewed commit 88c79f6 into ~/.claude/skills. Markdown and evals JSON only, no hooks or scripts. ai-seo names paid sponsor tools Omnia and Ploy (skills/ai-seo/SKILL.md:411,425; README.md:17): treat those picks as ads.
Hermes: copy the same folders into ~/.hermes/skills/<category>/.

## YOLO install

YOLO (your own risk): skips picking folders at the reviewed commit.
/plugin marketplace add coreyhaines31/marketingskills, then install marketing-skills (all 53 skills, README.md:158-166), or npx skills add coreyhaines31/marketingskills -a claude-code (README.md:155).

## Install notes

Safe, but ask the user before installing.
Claude Code: use the repo's /plugin route (per a review) rather than the npx skills CLI.
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
