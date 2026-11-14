# LLM4Decompile

- **Type:** library
- **Category:** security, research
- **Official URL:** https://github.com/albertan017/LLM4Decompile
- **GitHub repo:** https://github.com/albertan017/LLM4Decompile @ 85b364b (last commit 2026-02-12; code MIT, models under the DeepSeek model licence `LICENSE-MODEL`)
- **Price:** Free (code MIT, models DeepSeek model licence, github.com, checked 2026-11-02); needs a GPU for the 9B model.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @85b364b, a review, 2026-11-02): caution. Research code: the evaluation script compiles and runs model-written C with shell=True and no sandbox (`evaluation/run_evaluation_llm4decompile_singleGPU.py:48-66`); the Ghidra demo shells out to Ghidra headless (`ghidra/demo.py:23,40`). Run only in a container. No telemetry or curl|bash found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Any platform: run only in a container or VM with a GPU for the 9B model; no Windows steps checked. Only reverse-engineer software you own or are allowed to.
