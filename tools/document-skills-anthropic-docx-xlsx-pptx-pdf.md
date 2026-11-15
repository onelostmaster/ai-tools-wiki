# document-skills (Anthropic: docx, xlsx, pptx, pdf)

- **Type:** plugin
- **Category:** Notion and productivity, editing
- **Official URL:** https://github.com/anthropics/skills
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (plugin document-skills: skills/docx, xlsx, pptx, pdf; latest commit 2026-10-28)
- **Price:** Included with Claude; source-available, all rights reserved (`skills/docx/LICENSE.txt`, github.com, checked 2026-11-02)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

a review bot (vendor repo read @ca45fc4, a review, 2026-11-02): safe. Official Anthropic skills; the office scripts set an LD_PRELOAD socket shim for LibreOffice in sandboxes (`skills/xlsx/scripts/office/soffice.py:33`, Linux only). Source-available, not open source (`skills/docx/LICENSE.txt`: all rights reserved).

## Safe install

Safe install (fixes applied):
claude.ai: nothing to install; built in on paid plans (anthropics/skills README.md:55). Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills`. The LibreOffice LD_PRELOAD shim (skills/xlsx/scripts/office/soffice.py:33) is Linux-only and does nothing on Windows.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
claude.ai: already available on paid plans (anthropics/skills `README.md:55`).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` (`.claude-plugin/marketplace.json`).
