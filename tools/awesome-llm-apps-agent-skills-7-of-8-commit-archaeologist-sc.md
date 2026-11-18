# awesome-llm-apps agent skills (7 of 8: commit-archaeologist, scope-creep-detector, project-graveyard, dependency-doctor, first-reader, thinking-out-loud, self-improving-agent-skills)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills
- **GitHub repo:** https://github.com/Shubhamsaboo/awesome-llm-apps @ 6c16b23, folder `agent_skills/` (Apache-2.0; first-reader has no licence in `registry.json`)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @6c16b23, a review / Hermes a review, 2026-11-02): safe. Read-only git calls (`agent_skills/commit-archaeologist/archaeologist.py:30-42`, `scope_creep.py:427`); graveyard scans only folders you name (`graveyard.py:18,52-58`); dependency-doctor offline unless you opt in to PyPI lookups (`dep_doctor.py:389-392`); first-reader talks only to 127.0.0.1 (`feed.py:303`). No curl | bash (`agent_skills/README.md:56-58`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): download agent_skills/<skill> from https://github.com/Shubhamsaboo/awesome-llm-apps at reviewed commit 6c16b23 and copy only the skill folders you want into %USERPROFILE%\.claude\\skills\\ (pinned so later commits do not arrive unreviewed). Hermes: same folders into ~/.hermes/skills/ (agent_skills/README.md:52). Leave dependency-doctor's PyPI lookup off unless you want it to go online (dep_doctor.py:389-392). first-reader talks only to 127.0.0.1 (feed.py:303). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin.
The registry's npx skills add install (latest commit).

## Install notes

Safe, but ask the user before installing.
Claude Code: copy the skill folder you want into `~/.claude/skills/` (the registry lists `npx skills add` installs); read its script first.
Hermes: folder into `~/.hermes/skills/` (`agent_skills/README.md:52`).
Windows: works in Claude Code on Windows. Android: no.
