# awesome-gamedev-agent-skills

- **Type:** skill
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/gamedev-skills/awesome-gamedev-agent-skills
- **GitHub repo:** https://github.com/gamedev-skills/awesome-gamedev-agent-skills @ c6ca6c4 (Apache-2.0; HEAD on 2026-11-13, last commit 2026-11-12; earlier row noted 19d93f9)
- **Price:** Free (Apache-2.0 LICENSE, checked at commit c6ca6c4 on 2026-11-13)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @c6ca6c4, 2026-11-13, no-intake review): Safe. 80 SKILL.md skills (router + 79) in Markdown, no allowed-tools, hooks or MCP servers in any skill or in .claude-plugin/marketplace.json (11 plugins, skill paths only). 15 helper Python scripts under skills/*/scripts use only the standard library plus Pillow (create-game-assets); they read project folders and print reports, no network calls; new_game.py writes a starter Go project (lines 100-116); the only subprocess is lipo in package_macos_app.py line 168 (Mac-only, rmtree of the old .app at line 151). Go starter files, GDScript and Luau checks are sample code for your own game. Not reviewed: the README npx skills add installer (lines 15, 87) and npx tools some skills suggest (threejs-gltf-loading lines 29, 123; pixijs-rendering line 134). Repo scripts/ and tests/ are maintainer CI only. Replaces the earlier unreviewed status.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): from reviewed commit c6ca6c4 of github.com/gamedev-skills/awesome-gamedev-agent-skills copy only the skill folders you need (for example skills/router and skills/web-engines/threejs-scene-setup) into %USERPROFILE%\.claude\\skills\\<name> and start a new session; the marketplace route installs HEAD. Helper scripts need Python 3 (create-game-assets also needs Pillow); skip package_macos_app.py (Mac-only). Say no when a skill asks to run npx @gltf-transform/cli or playwright (threejs-gltf-loading lines 29, 123; pixijs-rendering line 134; not reviewed). Skip the npx skills add installer. No keys; type store logins for steam-publish or itch-publish yourself.
claude.ai: zip one skill folder and upload it under Settings, Capabilities, Skills.

## YOLO install

YOLO (your own risk): skips the commit pin and saying no to the npx tools.
claude plugin marketplace add gamedev-skills/awesome-gamedev-agent-skills then claude plugin install gamedev@awesome-gamedev-agent-skills (all 80 skills, HEAD; README lines 96-108).

## Install notes

Code-reviewed by a review bot @c6ca6c4 (safe). Claude Code on Windows: claude plugin marketplace add gamedev-skills/awesome-gamedev-agent-skills, then install only what you need, e.g. claude plugin install router@awesome-gamedev-agent-skills plus one engine pack such as godot@ or web-engines@ (README lines 96-108); the gamedev@ plugin loads all 80 skills. Or copy single skill folders (for example skills/web-engines/threejs-scene-setup) into %USERPROFILE%\.claude\\skills\\<name>. The README's npx skills add command is a third-party installer that was not reviewed. Helper scripts need Python 3 (create-game-assets also needs Pillow); package_macos_app.py is Mac-only, skip it on Windows. Some skills ask the agent to run npx tools (@gltf-transform/cli, playwright) that were not reviewed; say no if unsure. claude.ai: zip one skill folder and upload it under Settings, Capabilities, Skills. No keys; steam-publish and itch-publish need your own store login, typed by you. Unpinned: later commits arrive without a review.
