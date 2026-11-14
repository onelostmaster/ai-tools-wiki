# claude-reflect

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/BayramAnnakov/claude-reflect
- **GitHub repo:** [https://github.com/BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect)
- **Price:** Free (MIT open-source code)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

Claude (code read, v3.3.1 b6c4232, 2026-10-31): caution, 5/10. Raw prompt text is queued on every matching message with no secret filtering; /reflect pre-approves Read, Edit, Write and Bash and defaults to "Apply all"; it shells out to `claude -p` with your full permissions, so queued web or repo text can become a permanent rule (prompt injection). No telemetry or self-update. a review bot : Looks safe, no network code.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: pin the reviewed release: `claude plugin marketplace add bayramannakov/claude-reflect#v3.3.1`, then `claude plugin install claude-reflect@claude-reflect-marketplace --scope local` from the one repo you want it in.
Claude Code: run `/reflect --dry-run` first and choose "Select which to apply", never "Apply all"; avoid `--scan-history` on sessions that read untrusted pages or repos.
Claude Code: the same marketplace also has `reflect-mod` . Never install both; Claude's review covers the plugin, so skip the mod.
Claude Code: on Windows the hooks call `python3`; turn off the python3 App execution alias and put a real `python3.exe` on PATH, or the hooks fail silently.
Hermes: not needed; Hermes already does this natively.
