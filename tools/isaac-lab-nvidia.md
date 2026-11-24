# Isaac Lab (NVIDIA)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://isaac-sim.github.io/IsaacLab
- **GitHub repo:** https://github.com/isaac-sim/IsaacLab @ 5c40dd7 (BSD-3, Apache-2.0 for isaaclab_mimic per LICENSE-mimic; 3.0.0)
- **Price:** Free (BSD-3 style; Isaac Sim is a free NVIDIA download; github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

a review bot read @5c40dd7: safe with these fixes. Verified 1: network use in Isaac Lab's own code is the loading-screen artwork refresh, the SimReady asset search and asset downloads only: the loading screen fetches greeting artwork from huggingface.co/datasets/nvidia (source/isaaclab/isaaclab/app/_remote_greetings.py:33) and refreshes it every 300 s (:31), started from app/loading_screen.py:376; it is off when ISAACLAB_REMOTE_GREETINGS=0 (_remote_greetings.py:47). Fix: set ISAACLAB_REMOTE_GREETINGS=0. search_simready_usd_paths posts your query to search.simready.omniverse.nvidia.com (utils/assets.py:280,691) only when you call it; assets come from NVIDIA's S3/CDN and raw.githubusercontent.com/newton-physics (utils/assets.py:77,92,276). No analytics upload code found. Verified 2: every torch.load in source/ uses weights_only=True (e.g. isaaclab_rl/entrypoints/backends/play_torchrl.py:131, isaaclab_contrib/rl/rlinf/extension.py:266); no pickle.load. Fix: still play only checkpoints you trained yourself, since the RL libraries (rsl_rl, rl_games, skrl) load their own checkpoints outside this repo. Verified 3: the Windows install doc runs uv's installer as irm ... | iex (docs/source/isaaclab/installation.rst:222) and sets the LongPathsEnabled registry key from an elevated PowerShell (:212-216). Fix: install uv with py -m pip install uv instead of the piped script; the long-path key is required for the clone and cannot be skipped (one admin registry change, nothing else runs as admin). Verified 4: the repo ships uv.lock, so uv sync --locked installs the pinned versions; uv run installs dependencies on first use (installation.rst:243). Fix: run uv sync --locked once, then uv run --locked. Verified 5: the default Newton backend needs no Isaac Sim; --extra isaacsim pulls isaacsim[all,extscache]==6.2.0.0 (pyproject.toml:180) from pypi.nvidia.com (pyproject.toml:394), a closed NVIDIA binary. unverified: what Isaac Sim's closed binary sends over the network. Fix: use the default Newton backend; if you need Isaac Sim, run it in its own venv on a GPU machine without personal files and accept NVIDIA's licence yourself.

## Safe install

Safe install (fixes applied):
Windows 11 (RTX GPU, driver 595.97+ per installation.rst:91): elevated PowerShell once: New-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\FileSystem" -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force ; then a normal Command Prompt: py -m pip install --user uv ; git clone https://github.com/isaac-sim/IsaacLab C:\\IsaacLab ; cd C:\\IsaacLab ; git checkout 5c40dd797baac01eb0dd3d0022eea6873db852d3 ; set ISAACLAB_REMOTE_GREETINGS=0 ; uv sync --locked ; uv run --locked isaaclab train --rl_library rsl_rl --task Isaac-Cartpole-Direct (default Newton backend, no Isaac Sim). Play only your own checkpoints.
Claude Code on Windows: same commands in its terminal, inside C:\\IsaacLab.
claude.ai, Hermes, Android: not supported (needs a local NVIDIA RTX GPU and Python 3.12).

## YOLO install

YOLO (your own risk): skips the pinned commit, the lockfile flag, the greetings switch and the Newton-only choice. Windows: the docs' irm https://astral.sh/uv/install.ps1 | iex, clone main, uv run --extra isaacsim isaaclab train --rl_library rsl_rl --task Isaac-Cartpole-Direct (pulls NVIDIA's closed Isaac Sim 6.2 from pypi.nvidia.com).

## Install notes

Safe with fixes: NVIDIA's open robot-learning framework (GPU physics, RL training, 30+ ready tasks). Pin commit 5c40dd7, uv sync --locked, set ISAACLAB_REMOTE_GREETINGS=0 so the loading screen doesn't fetch artwork every 5 min, install uv with pip instead of the piped script, and stay on the default Newton backend so NVIDIA's closed Isaac Sim binary is never installed. Needs one admin registry change (long paths) on Windows. Needs an NVIDIA RTX GPU.
