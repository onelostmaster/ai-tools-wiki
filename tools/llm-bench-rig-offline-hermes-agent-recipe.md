# llm-bench-rig (offline Hermes Agent recipe)

- **Type:** dataset
- **Category:** Hermes add-ons, developer tools
- **Official URL:** https://github.com/notwitcheer/llm-bench-rig
- **GitHub repo:** https://github.com/notwitcheer/llm-bench-rig @ 7c302ca (no licence file per the GitHub API)
- **Price:** Free repo (no licence file); a local 27B model needs your own strong hardware (cost unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @7c302ca, Hermes a review, 2026-11-01): Looks safe as a recipe. Offline harness is stdlib Python; containers run --network none, --cap-drop ALL, no-new-privileges, read-only mounts; no curl|bash, telemetry or secrets. The wider rig runs model-written code by design (`lib/agentic/sandbox.py:24` exec, `tools_repo.py:131-135` bash -c) and needs the author's private scripts, so it will not run as-is.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Nothing to install; it is a write-up. Hermes: to reproduce, follow `reports/offline-hermes.md` and `agenttest/offline/` (Docker plus a local model server). Exact commands not confirmed beyond the repo docs. Ask the user before running anything.
New report @27026a9 (2026-11-02): `reports/pheromone-replay.md` re-runs arXiv 2601.08129 (fading-marks coordination; official code in the pressure-field-experiment (Govcraft) row). Do not run `pheromone/05-pheromone-pf.sh`: it sources the author's private night-lib.sh (:25) and kills and restarts local servers (:98-111).
