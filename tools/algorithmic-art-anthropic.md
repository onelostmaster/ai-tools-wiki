# algorithmic-art (Anthropic)

- **Type:** skill
- **Category:** design
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/algorithmic-art
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (folder skills/algorithmic-art; Apache-2.0; latest commit on 2026-10-28)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor repo, ca45fc4, 2026-11-01): safe. Anthropic's own example skill (Apache-2.0), text plus HTML templates; the generated page loads p5.js from `cdnjs.cloudflare.com`. No keys, hooks or telemetry.

## Safe install

Safe install (fixes applied):
claude.ai: already built in on paid plans (anthropics/skills README.md:55), nothing to install.
Claude Code (Windows): copy only skills/algorithmic-art from reviewed commit ca45fc4 into ~/.claude/skills (HEAD is newer and not reviewed). Text and HTML templates; no scripts. The pages it makes load p5.js from cdnjs.cloudflare.com when you open them.
Hermes: copy the same folder into ~/.hermes/skills/<category>/algorithmic-art/ (<category> = any folder name you choose).

## YOLO install

YOLO (your own risk): skips copying only the one folder at the reviewed commit.
/plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills (installs all 12 example skills at HEAD).

## Install notes

claude.ai: already available on paid plans (anthropics/skills README); turn skills on as in Anthropic's "Using skills in Claude" help article (https://support.claude.com/en/articles/12512180-using-skills-in-claude).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (README; this plugin bundles 12 example skills).
