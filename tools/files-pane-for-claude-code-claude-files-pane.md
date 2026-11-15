# Files pane for Claude Code (claude-files-pane)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/Marius-Adam/claude-files-pane
- **GitHub repo:** https://github.com/Marius-Adam/claude-files-pane @ 3794eea (2026-11-01, plugin files-pane v0.8.2, MIT, not a fork)
- **Price:** Free, MIT (LICENSE, checked 2026-11-02); optional Ko-fi tip link.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read of hooks/ @3794eea, a review, 2026-11-02; Claude spot-checked): no network calls, telemetry, eval, curl|bash, install script or auto-update. Starts only read-only git with --no-optional-locks inside the session repo (`hooks/disk.ts:28-76`), editor lookup and your chosen editor (`hooks/editors.ts:35,61,87`), and on Windows a fixed Reveal script (`editors.ts:115-149`). Caveats: three-day-old repo, one author, few stars; reads your project tree locally.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing. Claude Code (terminal, desktop app or VS Code extension, Windows works): claude plugin marketplace add Marius-Adam/claude-files-pane, then claude plugin install files-pane@marius-adam (README Installation); restart Claude Code and run /files. Uninstall: claude plugin uninstall files-pane. Not for claude.ai, Hermes or Android.
