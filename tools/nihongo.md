# nihongo

- **Type:** skill
- **Category:** a project
- **Official URL:** https://github.com/AnIT012/nihongo
- **GitHub repo:** https://github.com/AnIT012/nihongo @ 15de10bc (v3.0.0, MIT; commit 2026-11-22 11:52 ET confirmed via GitHub API)
- **Price:** Free (MIT License). Confirmed on the official repo LICENSE and GitHub license field, 2026-11-23. The skill itself is unpaid; uploading it into ChatGPT or Claude follows those apps' own plan rules.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot code read @15de10bc (v3.0.0), 2026-11-23: safe with the Install notes fixes. No network or telemetry in nihongo/scripts (Python 3.10+ standard library only; pyproject.toml lists no dependencies). git is started as an argument list, not a shell (cli.py:264-271). Hook file paths are limited to the git repo (cli.py:285-297,517-521). Verified risks, fixed: (1) README.md:31,153,180,191,214 installs and updates with unpinned `npx skills add` / `npx skills update`; fix: install from the v3.0.0 release zip after SHA-256 34625762a4865de9a1a41a54690e3450d9dbfe23d72024dab839db267d374d19 (optional `gh attestation verify nihongo-v3.0.0.zip -R AnIT012/nihongo`), or copy `nihongo/` from a clone at `15de10bc`, and do not run `npx skills update`. (2) examples/hooks/claude-code-hook.json:2-11 is an opt-in PostToolUse hook that runs `cli.py git --hook` on every Edit|Write of .md/.txt; it reads the file and runs git and does not write the file back (cli.py:456-589); fix: leave the hook off and run the CLI by hand. (3) `nihongo-check fix` overwrites the path given as <out> (cli.py:420-421); fix: write to a new file. (4) ALWAYS.md:9 tells the agent to append to ~/.nihongo/profile.md after a one-line confirm; the CLI only reads that file (cli.py:103-105) and does not write it; fix: keep secrets and personal names out, review the file, and refuse silent writes.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: download `nihongo-v3.0.0.zip` from github.com/AnIT012/nihongo/releases/tag/v3.0.0, check SHA-256 `34625762a4865de9a1a41a54690e3450d9dbfe23d72024dab839db267d374d19` (`Get-FileHash`), optionally `gh attestation verify nihongo-v3.0.0.zip -R AnIT012/nihongo`, then copy the `nihongo/` folder to `~/.claude/skills/nihongo`. Or clone `--branch v3.0.0` and stay at `15de10bc`. If you want Lite on every chat, add `@~/.claude/skills/nihongo/ALWAYS.md` to CLAUDE.md yourself. Do not run `npx skills add` or `npx skills update`. Run checks with `python3 ~/.claude/skills/nihongo/scripts/cli.py` (Python 3.10+). Leave the PostToolUse hook off. Do not put secrets or personal names in `~/.nihongo/profile.md`. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json. Re-review before bumping the pin.
claude.ai / Android: upload that same verified v3.0.0 zip (not GitHub's Source Download ZIP).
Codex: copy the same pinned `nihongo/` folder; do not use unpinned `npx skills add`.

## YOLO install

YOLO (your own risk): skips the release pin, the SHA-256 / attestation check, the ban on `npx skills update`, and leaving the PostToolUse hook off.
`npx skills add AnIT012/nihongo -g -a claude-code` then `echo '@~/.claude/skills/nihongo/ALWAYS.md' >> ~/.claude/CLAUDE.md` (README.md:31-32). Optional: copy `examples/hooks/claude-code-hook.json` into Claude Code hooks, and `pip install "git+https://github.com/AnIT012/nihongo.git@v3.0.0"`.

## Install notes

Windows/Claude Code: from a clone at `15de10bc`, or from the official v3.0.0 zip after SHA-256 34625762a4865de9a1a41a54690e3450d9dbfe23d72024dab839db267d374d19, copy the `nihongo/` folder to `~/.claude/skills/nihongo`. If you want Lite on every chat, add `@~/.claude/skills/nihongo/ALWAYS.md` to CLAUDE.md yourself. Do not run `npx skills add` or `npx skills update`. Run the checker with `python3 ~/.claude/skills/nihongo/scripts/cli.py` (Python 3.10+). Leave the PostToolUse hook off unless you want it to run on every Edit|Write of .md/.txt. Keep `~/.nihongo/profile.md` free of secrets and names, and review it before any append. claude.ai / Android (Claude app): upload that same verified v3.0.0 release zip; do not upload GitHub's Code → Download ZIP (README.md:208: SKILL.md is one folder too deep). Paste ALWAYS.md into custom instructions if you want Lite on every chat. Codex: copy the same pinned `nihongo/` folder into the Codex skills directory; do not use unpinned `npx skills add`. Paste ALWAYS.md into AGENTS.md if you want Lite always on. `nihongo-check fix` writes the output path you give it; use a new file.
