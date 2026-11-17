# llm-bench-rig (offline Hermes Agent recipe)

- **Type:** dataset
- **Category:** Hermes add-ons, developer tools
- **Official URL:** https://github.com/notwitcheer/llm-bench-rig
- **GitHub repo:** https://github.com/notwitcheer/llm-bench-rig @ 7c302ca (no licence file per the GitHub API)
- **Price:** Free repo (no licence file); a local 27B model needs your own strong hardware (cost unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @7c302ca, Hermes a review, 2026-11-01): Looks safe as a recipe. Offline harness is stdlib Python; containers run --network none, --cap-drop ALL, no-new-privileges, read-only mounts; no curl|bash, telemetry or secrets. The wider rig runs model-written code by design (`lib/agentic/sandbox.py:24` exec, `tools_repo.py:131-135` bash -c) and needs the author's private scripts, so it will not run as-is.

## Safe install

Safe install (fixes applied):
Nothing to install; it is a write-up to read (reports/offline-hermes.md). To reproduce on Windows, use Docker Desktop with WSL2 and keep the repo's container settings as written. Fix: run the agentic parts only inside those containers, because they execute model-written code by design (lib/agentic/sandbox.py:24, tools_repo.py:131-135). Do not run pheromone/05-pheromone-pf.sh: it sources the author's private night-lib.sh (:25) and kills and restarts local servers (:98-111). Pin the reviewed commit 7c302ca (git checkout 7c302ca).

## YOLO install

YOLO (your own risk): skips the container-only rule, the commit pin and the pheromone/05 ban.
Run the repo scripts on your machine as the reports describe.

## Install notes

Nothing to install; it is a write-up. Hermes: to reproduce, follow `reports/offline-hermes.md` and `agenttest/offline/` (Docker plus a local model server). Exact commands not confirmed beyond the repo docs. Ask the user before running anything.
New report @27026a9 (2026-11-02): `reports/pheromone-replay.md` re-runs arXiv 2601.08129 (fading-marks coordination; official code in the pressure-field-experiment (Govcraft) row). Do not run `pheromone/05-pheromone-pf.sh`: it sources the author's private night-lib.sh (:25) and kills and restarts local servers (:98-111).
