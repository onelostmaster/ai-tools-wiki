# taste-skill

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/Leonxlnx/taste-skill
- **GitHub repo:** https://github.com/Leonxlnx/taste-skill @ f6b7657 (v2.5.1, MIT; commit 2026-11-07 confirmed via GitHub API)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @f6b7657 (v2.5.1), 2026-11-14: safe with the Install notes fixes. No telemetry found. Verified risk, fixed: SKILL.md:14-19 declares a Stop hook that runs `node scripts/gate.mjs` at every Claude Code stop (600 s timeout; exits at once when there is no `.taste-skill/build.json`, gate.mjs:20-23); fix: delete that hooks block before install. Network only when its scripts run, to public sources: Wikimedia Commons and picsum (photos.mjs:667,785), jsDelivr icons (icons.mjs:65-66), Google Fonts links (start.mjs:288). `scripts/assets.mjs` no longer exists.

## Safe install

Safe install (fixes applied):
Claude Code: from a clone checked out at `f6b7657`, copy `skills/taste-skill` to `~/.claude/skills/design-taste-frontend`. Do not run `install.sh` (it symlinks the folder, so a later git pull changes the installed skill). Then delete lines 14-19 (the `hooks:` block) from that copy's SKILL.md frontmatter. Run `node ~/.claude/skills/design-taste-frontend/scripts/gate.mjs` by hand when you want its page check. Needs Node 22+ and Chrome. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json. Re-review before bumping the pin.

## YOLO install

YOLO (your own risk): skips the commit pin, the ban on install.sh, and deleting the Stop hook, so gate.mjs can run on every Claude Code stop.
Run the repo's `install.sh` from HEAD, leaving the hooks block in SKILL.md.

## Install notes

Claude Code only; ask the user first. From a clone checked out at `f6b7657`, copy `skills/taste-skill` to `~/.claude/skills/design-taste-frontend` (don't run `install.sh`: it symlinks the folder, so a later `git pull` changes the installed skill), then delete lines 14-19 (the `hooks:` block) from that copy's SKILL.md frontmatter. Run `node ~/.claude/skills/design-taste-frontend/scripts/gate.mjs` by hand when you want its page check. Needs Node 22+ and Chrome. 40 MB, too large to be a practical claude.ai skill upload.
