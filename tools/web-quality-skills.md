# web-quality-skills

- **Type:** skill
- **Category:** building a site, developer tools
- **Official URL:** https://github.com/addyosmani/web-quality-skills
- **GitHub repo:** https://github.com/addyosmani/web-quality-skills @ afa8da9 (MIT; plugin 2.0.0; committed 2026-08-24 17:07 ET per git log, HEAD on 2026-11-08)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read @afa8da9, plugin 2.0.0, 2026-11-08, no-intake review): Looks safe. .claude-plugin/plugin.json and marketplace.json declare only the skills: no hooks, MCP servers or install scripts. The repo is Markdown (6 skills plus references). The only script, skills/web-quality-audit/scripts/analyze.sh (113 lines), is read-only: it greps local .html files and prints JSON with jq, no network, no writes, no eval (lines 2, 34-77, 100-113). Skills suggest `npx lighthouse` and `npm install @axe-core/cli -g` for live audits (accessibility/SKILL.md:413-417), which fetch packages from npm only if you run them. No telemetry or keys.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (works on Windows): inside Claude Code run `/plugin marketplace add addyosmani/web-quality-skills` then `/plugin install web-quality-skills@addy-web-quality-skills` (README lines 64-73); skills show up as `/web-quality-skills:performance` and similar. Or copy the `skills/` folders into `%USERPROFILE%\.claude\skills\`. The README's `npx skills add` route uses a separate third-party installer CLI, so prefer the plugin route. The skills are instructions only. The audit helper `skills/web-quality-audit/scripts/analyze.sh` needs bash and jq (Git Bash on Windows); live audits use Lighthouse or axe through npx when you ask for them. Fits a project web and phone app design work (performance, accessibility, SEO checks).
