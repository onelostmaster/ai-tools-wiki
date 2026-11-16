# Agent Blackbox

- **Type:** plugin
- **Category:** Hermes add-ons, security
- **Official URL:** https://umanitek.ai/blackbox
- **GitHub repo:** [https://github.com/umanitek/agent-blackbox](https://github.com/umanitek/agent-blackbox)
- **Price:** unknown
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude targeted read @fa73aff6 (2026-11-15; a full Hermes distribution, too big to read): unreviewed. Checked: community sharing is off until you opt in (community/consent.py:110-115); the dashboard binds 127.0.0.1. Unverified: the bundled Hermes runtime, and blackbox attach wiring every Hermes home on the machine (README:88) -> Contain: only in a spare Windows account or VM, manual install, never the curl|bash line.

## Safe install

Unreviewed: contain it: spare account or VM only; manual install at tag blackbox-v1.4.0 (README 'Manual install'), pin @origintrail-official/dkg@10.0.27 instead of @latest; leave sharing off. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: spare account or VM only; manual install at tag blackbox-v1.4.0 (README 'Manual install'), pin @origintrail-official/dkg@10.0.27 instead of @latest; leave sharing off.
