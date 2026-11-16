# Filetree (claude-code-filetree)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/data-goblin/claude-code-filetree
- **GitHub repo:** [https://github.com/data-goblin/claude-code-filetree](https://github.com/data-goblin/claude-code-filetree) (read at 0ad31a6)
- **Price:** Free (MIT open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @3ce5b1c (2026-11-15): safe with fixes, Skip (no need). No network code. Windows is now supported (README:157). It opens files with gio, xdg-open or tmux (hooks/open.ts:13-37) and blocks find write flags such as -delete and -exec (hooks/git.ts:215). Fix: pin the marketplace commit. Needs Claude Code 2.1.287+.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add data-goblin/claude-code-filetree#3ce5b1c, then claude plugin install filetree@claude-code-filetree.

## YOLO install

YOLO (your own risk): skips the pin, so updates arrive unread.
Install from the marketplace as the README says.

## Install notes

Ask the user before installing. claude plugin marketplace add data-goblin/claude-code-filetree#3ce5b1c, then claude plugin install filetree@claude-code-filetree.
