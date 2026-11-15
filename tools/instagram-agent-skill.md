# Instagram Agent skill

- **Type:** plugin
- **Category:** research, social posting
- **Official URL:** https://github.com/Jakeschincariol/instagram-agent-skill
- **GitHub repo:** [https://github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
- **Price:** Free (MIT)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (code read, d03c56b, a project, 2026-10-31): safe. v1.0.0, MIT; Markdown plus local Python, no network, never posts.

## Safe install

Safe install (fixes applied):
Claude Code (Windows), project-local (only that project gets it): `git clone https://github.com/Jakeschincariol/instagram-agent-skill.git`, `git -C instagram-agent-skill checkout d03c56b` (the reviewed commit, still HEAD on 2026-11-14), then copy `skills/ig-*` into the project's `.claude/skills/` (README Install). The plugin route `/plugin marketplace add Jakeschincariol/instagram-agent-skill` then `/plugin install instagram-agent` (README:40-41) installs it for your user in every project; use it only if you want that. a project: it is already listed in .claude/settings.json (PR #5); it loads in new threads only once tool-scout/setup-script-plugins.sh runs from the environment setup script. No network code and it never posts (code read d03c56b), so nothing else to switch off.

## YOLO install

YOLO (your own risk): skips the commit pin and installs for your user in every project.
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent

## Install notes

Claude Code (a project): listed in the project's `.claude/settings.json` (PR #5), but per a project tool scout it does not load in new threads until the setup-script fix (`tool-scout/setup-script-plugins.sh`).
Claude Code (other projects): no confirmed command yet; follow the official docs at [https://github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)
