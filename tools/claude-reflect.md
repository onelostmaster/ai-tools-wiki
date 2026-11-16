# claude-reflect

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/BayramAnnakov/claude-reflect
- **GitHub repo:** [https://github.com/BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect)
- **Price:** Free (MIT open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @b6c4232 = v3.3.1 (2026-11-15): safe with fixes, Skip. No network code or self-update. /reflect pre-approves Read, Edit, Write and Bash (commands/reflect.md:3) and offers "Apply all" (line 354), which lets queued web or repo text become a permanent rule. Fix: review each learning yourself (dry run, select one by one). The semantic check calls claude -p for JSON only (scripts/lib/semantic_detector.py:77).

## Safe install

Safe install (fixes applied):
claude plugin marketplace add bayramannakov/claude-reflect#v3.3.1, claude plugin install claude-reflect@claude-reflect-marketplace --scope local; run /reflect --dry-run, then pick learnings one by one, never Apply all; no --scan-history on sessions that read untrusted pages; skip reflect-mod.

## YOLO install

YOLO (your own risk): skips the pin and the review, so every queued learning is applied.
Install from the marketplace and use Apply all.

## Install notes

Ask the user before installing. claude plugin marketplace add bayramannakov/claude-reflect#v3.3.1, claude plugin install claude-reflect@claude-reflect-marketplace --scope local; run /reflect --dry-run, then pick learnings one by one, never Apply all; no --scan-history on sessions that read untrusted pages; skip reflect-mod.
