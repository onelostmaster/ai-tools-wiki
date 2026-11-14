# impeccable

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/pbakaus/impeccable
- **GitHub repo:** [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read, 2f97a85, a review): Use with caution. Its SessionStart, PostToolUse and Stop hooks (`plugin/hooks/hooks.json`) run outside approval and auto-download a prebuilt engine binary from GitHub releases (checksum-pinned). A manual skill-only copy skips the hook. Re-checked 2026-11-01 (a review bot, new commits up to e89e3ad, a review): same verdict; new commits only fix Windows/VS Code hooks and make the launcher chmod itself.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
