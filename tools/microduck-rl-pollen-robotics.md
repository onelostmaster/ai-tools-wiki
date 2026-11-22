# microduck_rl (Pollen Robotics)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://pollen-robotics.com/microduck
- **GitHub repo:** https://github.com/pollen-robotics/microduck_rl @ 0daab16 (code Apache-2.0, models CC-BY-NC-SA-4.0 per pyproject.toml)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); the real Microduck robot is sold by Pollen Robotics (not priced)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-21

## Safety reason

a review bot read @0daab16: safe with fixes. RL training environments for the Microduck robot on mjlab 1.3.0 / MuJoCo Warp; no .sh files in the repo at this commit (0 found), no install hooks (uv_build backend, pyproject.toml:1-3). Verified points and fixes: (1) train ... --hf-jobs sends your cached Hugging Face token and your WANDB_API_KEY (from the env or ~/.netrc) to a Hugging Face Jobs run as job secrets (train_hook.py:61-76, hf_jobs.py:310-345); fix: never pass --hf-jobs and keep no HF or wandb login in the training environment. (2) uv run publish and share-training create a Hugging Face model repo and upload to it (publish/cli.py:234-255); fix: use publish --dry-run only (writes a local folder, publish/cli.py:225-231). (3) --wandb-run-path downloads checkpoints from wandb (export.py:137-196); fix: use --checkpoint-file with a local model_N.pt. (4) duck-body opens TCP servers on 127.0.0.1:7801+ and 7901+ by default (sim/body_server.py:510-511,520,562,569); fix: keep the default --host, never 0.0.0.0. (5) the bam dependency points at a git branch (pyproject.toml [tool.uv.sources]) but uv.lock:106 pins commit 62bd8ce; fix: install with uv sync --locked. unverified: whether mjlab 1.3.0's train logs online to wandb by default (mjlab code not read); containment: set WANDB_MODE=offline before training. Licence note: code Apache-2.0, trained models CC-BY-NC-SA-4.0 (pyproject.toml license; LICENSE-MODELS.md), so no commercial use of its models.

## Safe install

Safe install (fixes applied): Windows: inside WSL2 (Ubuntu) with an NVIDIA GPU and uv installed: git clone https://github.com/pollen-robotics/microduck_rl && cd microduck_rl && git checkout 0daab16 && uv sync --locked; then export WANDB_MODE=offline and run training locally, e.g. uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096. Never add --hf-jobs, never run publish or share-training without --dry-run, use --checkpoint-file instead of --wandb-run-path, keep duck-body on its default 127.0.0.1, and keep no Hugging Face or wandb login in that environment. Claude Code (Windows): same, from a WSL2 terminal. claude.ai, Hermes, Android: no (needs a CUDA GPU, README.md:24).

## YOLO install

YOLO (your own risk): skips the pinned commit, --locked, offline wandb and the no-cloud rules. git clone https://github.com/pollen-robotics/microduck_rl && cd microduck_rl && uv sync, then uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096 (add --hf-jobs to train on Hugging Face Jobs with your HF token and wandb key; uv run publish to upload policies to the Hub).

## Install notes

Safe with fixes: Pollen Robotics' RL training code for the Microduck robot (walk, stand-up, ball kick, roller tasks) on mjlab / MuJoCo Warp, read @0daab16. Needs an NVIDIA CUDA GPU; on Windows run it in WSL2. Its cloud features are opt-in flags: --hf-jobs (uploads your HF token and wandb key as job secrets), publish/share-training (uploads to the Hugging Face Hub) and --wandb-run-path; skip them and set WANDB_MODE=offline. Trained models are CC-BY-NC-SA-4.0 (no commercial use). Fit: robot-pet or game-AI experiments, not the video projects.
