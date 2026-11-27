# OrenCut (OrenFang)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://orenfang.github.io/orencut/
- **GitHub repo:** https://github.com/OrenFang/orencut @ 4aac9b3 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: for Codex, put the whole repo folder as .agents/skills/orencut/ in a project or ~/.agents/skills/orencut/ for all projects; the Studio runs in the browser at orenfang.github.io and exports MP4 locally; single components download as ZIPs from GitHub releases. Code MIT; locally imported fonts and third-party visuals keep their own licenses. Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: copy the folder from the pinned commit 4aac9b3 into one sandbox project (project scope, not ~/.agents), no API keys (it needs none), network off except the npm install for the Remotion scenes. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Codex: copy the repo folder to <project>/.agents/skills/orencut/ (README). No Claude Code install documented; the Remotion scenes are in src/scenes/.
