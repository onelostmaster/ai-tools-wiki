# karpathy-guidelines (andrej-karpathy-skills)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/forrestchang/andrej-karpathy-skills
- **GitHub repo:** https://github.com/forrestchang/andrej-karpathy-skills @ 2c60614 (MIT; GitHub redirects to multica-ai/andrej-karpathy-skills; written by a fan, not by Karpathy, `SKILL.md:9`)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @2c60614, a review, 2026-11-02): safe. One 67-line Markdown file, no hooks or scripts. Not by Karpathy (`SKILL.md:9`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): /plugin marketplace add forrestchang/andrej-karpathy-skills#2c60614 (reviewed commit), then /plugin install andrej-karpathy-skills@karpathy-skills (README.md:99-110, .claude-plugin/marketplace.json). One Markdown file, no hooks or scripts. Not written by Karpathy (SKILL.md:9).
Hermes: copy the SKILL.md folder into ~/.hermes/skills/<category>/karpathy-guidelines/.

## YOLO install

YOLO (your own risk): skips the commit pin.
/plugin marketplace add forrestchang/andrej-karpathy-skills, then /plugin install andrej-karpathy-skills@karpathy-skills (README.md:105-110).

## Install notes

Safe, but ask the user before installing.
Claude Code: via /plugin rather than the npx skills CLI (Claude, a review).
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
