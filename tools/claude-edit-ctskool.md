# claude-edit (ctskool)

- **Type:** skill
- **Category:** editing
- **Official URL:** https://ctskool.github.io/claude-edit/
- **GitHub repo:** https://github.com/ctskool/claude-edit @ c7e2381 (MIT per README; github.com lists NOASSERTION)
- **Price:** Free on GitHub, MIT per README (checked 2026-11-23)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-23

## Safety reason

Not code-reviewed for safety. README: one-line installer piped from the internet (Windows: irm .../install.ps1 | iex) puts the editor in ~/claude-edit, builds Python and Node environments there and adds the /claude-edit skill for every folder on your machine (user-wide); needs Claude Code, Python 3.10+, Node 22+, git, ffmpeg; Codex optional. Bundled fonts and GSAP have their own notices in licenses/. Repo, license and latest commit confirmed from github.com metadata, 2026-11-23.

## Safe install

Unreviewed: contain it: do not pipe install.ps1 into iex; clone at the pinned commit c7e2381, read install.ps1, and follow INSTALL.md manual steps inside a Windows Sandbox or devcontainer, no API keys (it needs none), network on only for the package installs. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code on Windows (README): irm https://raw.githubusercontent.com/ctskool/claude-edit/main/install.ps1 | iex — installs user-wide into %USERPROFILE%\\claude-edit and your Claude Code skills. Manual steps are in INSTALL.md.
