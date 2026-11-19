# AutoGen (Microsoft)

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/microsoft/autogen
- **GitHub repo:** https://github.com/microsoft/autogen @ d07c667 (code MIT, docs CC-BY-4.0; archived)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @8390985 (2026-11-18): caution. Microsoft archived it: "not providing bug fixes, security fixes, new features, or support" (README.md:17-24). No fix: nobody patches its code or pins, so a found hole stays open. Use the AG2 row or Microsoft Agent Framework instead.

## Safe install

Safe install (fixes applied):
Use the AG2 row or Microsoft Agent Framework instead. If you must read old code: clone at 8390985 into a throwaway venv; never deploy it.

## YOLO install

YOLO (your own risk): skips moving to a maintained fork.
pip install autogen-agentchat and build on it.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: do not start new work on it; use AG2 instead. Android: no.
