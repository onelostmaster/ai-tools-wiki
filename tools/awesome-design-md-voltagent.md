# Awesome DESIGN.md (VoltAgent)

- **Type:** dataset
- **Category:** design, building a site
- **Official URL:** https://getdesign.md/
- **GitHub repo:** https://github.com/VoltAgent/awesome-design-md @ fcc7028 (MIT; HEAD on 2026-11-13, latest commit on 2026-10-28)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); custom requests on `getdesign.md` not priced here.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @fcc7028, 2026-11-13, no-intake review): Safe. Repo is 173 files: 84 design-md/<brand>/ folders each holding a DESIGN.md (YAML front matter of colors, type and spacing tokens plus prose design notes) and a README.md that only links to getdesign.md; plus the root README, CONTRIBUTING, MIT LICENSE and two .github files (FUNDING.yml, an issue form asking for a website URL and an email). No scripts, hooks, MCP servers or install steps. Scanned all DESIGN.md files for commands, URLs and prompt-injection phrases: the only URLs are curl install lines quoted as page content in ollama/DESIGN.md line 420 and opencode.ai/DESIGN.md line 409 (descriptions of those sites, not steps for the agent). Caution kept from before: copying a brand's look closely can raise trademark issues; getdesign.md paid requests were not reviewed. Replaces the earlier unreviewed status.

## Safe install

Safe install (fixes applied):
Nothing to install and nothing runs. Claude Code (Windows): download one file, github.com/VoltAgent/awesome-design-md/blob/fcc7028/design-md/<brand>/DESIGN.md (reviewed commit; Raw, save) into your project root and ask Claude to follow it (README lines 23, 33). claude.ai and Android (claude.ai app): attach that DESIGN.md to a project or chat. Use it as a style guide only; do not copy the brand's logo or name into your own product.

## YOLO install

YOLO (your own risk): skips the commit pin.
Download the DESIGN.md from the main branch (newer files are not reviewed).

## Install notes

Code-reviewed by a review bot @fcc7028 (safe). Nothing to install: each brand is one Markdown file at design-md/<brand>/DESIGN.md. Claude Code on Windows: download one DESIGN.md (open it on GitHub, Raw, save) into your project root and ask Claude to follow it (README lines 23, 33). claude.ai: attach the DESIGN.md to a project or chat. Android: works through claude.ai only. The per-folder README.md files just point to getdesign.md; the request form and starter kit there are a separate paid service, not reviewed. Use the files as style guides; do not copy a brand's logo or name into your own product.
