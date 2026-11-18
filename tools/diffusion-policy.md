# Diffusion Policy

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://diffusion-policy.cs.columbia.edu/
- **GitHub repo:** https://github.com/real-stanford/diffusion_policy @ 5ba07ac (MIT; last push 2024-12-24)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @5ba07ac (2026-11-17): safe with fixes. No commit since 2024-12-24. Checkpoints load with full pickle via dill (eval.py:31, workspace/base_workspace.py:97), so a .ckpt from anyone else runs code. Training logs go to wandb online by default (config/train_diffusion_unet_hybrid_workspace.yaml:111). Fix: load only checkpoints you trained, WANDB_MODE=offline.

## Safe install

Safe install (fixes applied):
Linux + NVIDIA GPU; clone at 5ba07ac into its own conda env per README; env WANDB_MODE=offline; train your own checkpoints and never load a .ckpt you did not make.

## YOLO install

YOLO (your own risk): skips offline logging and the own-checkpoints rule.
Clone, log to wandb and run the downloaded pretrained checkpoints.

## Install notes

Ask the user before installing.
Linux with an NVIDIA GPU per README; no Windows steps checked.
