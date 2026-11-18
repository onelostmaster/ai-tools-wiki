# LLM4Decompile

- **Type:** library
- **Category:** security, research
- **Official URL:** https://github.com/albertan017/LLM4Decompile
- **GitHub repo:** https://github.com/albertan017/LLM4Decompile @ 85b364b (last commit 2026-02-12; code MIT, models under the DeepSeek model licence `LICENSE-MODEL`)
- **Price:** Free (code MIT, models DeepSeek model licence, github.com, checked 2026-11-02); needs a GPU for the 9B model.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @85b364b (2026-11-17): safe with fixes. The evaluation compiles and runs model-written C with shell=True and no sandbox (evaluation/run_evaluation_llm4decompile_singleGPU.py:48-66). The repo ships a Dockerfile and a GPU docker run line (README.md:176-180). No telemetry or curl|bash. Fix: run everything in that container with no network. Only decompile software you own or have permission to analyse.

## Safe install

Safe install (fixes applied):
Clone at 85b364b; docker build -t llm4decompile .; docker run --gpus all --network none -it llm4decompile /bin/bash after the model download; run evaluation and demo.py only inside it.

## YOLO install

YOLO (your own risk): skips the container.
Run the evaluation scripts on the host as the README shows.

## Install notes

Ask the user before installing.
Any platform: run only in a container or VM with a GPU for the 9B model; no Windows steps checked. Only reverse-engineer software you own or are allowed to.
