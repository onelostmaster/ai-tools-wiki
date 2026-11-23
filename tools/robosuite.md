# robosuite

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://robosuite.ai
- **GitHub repo:** https://github.com/ARISE-Initiative/robosuite @ 5ce6643 (MIT; v1.5.2; commit 2026-07-11)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

a review bot read @5ce6643: safe with these fixes. No network calls, telemetry or downloads in the package code (no requests/urllib/socket use in robosuite/); subprocess is imported but never called (robosuite/utils/binding_utils.py:21). Verified 1: the Keyboard and SpaceMouse teleop devices start a pynput keyboard listener as soon as they are created (robosuite/devices/keyboard.py:35-38, robosuite/devices/spacemouse.py:177); pynput hears key presses system-wide, not only in the sim window, and the handlers only map keys to robot moves (keyboard.py:107+), nothing is logged or sent. Fix: don't type passwords or private text in other apps while a keyboard/SpaceMouse demo or collect_human_demonstrations is running; close the demo when done. The tune_camera/tune_joints/browse_mjcf_model scripts do the same (scripts/tune_camera.py:13, tune_joints.py:21, browse_mjcf_model.py:58). Verified 2: the IK demo loads .pkl files with pickle.load (robosuite/utils/ik_utils.py:89) and demo collection loads .npz with allow_pickle=True (scripts/collect_human_demonstrations.py:164); a pickle file can run code when loaded. Fix: load only pickle/npz files you recorded yourself, never downloaded ones. Verified 3: setup_macros.py copies macros.py to macros_private.py inside the installed package folder (scripts/setup_macros.py:15-31). Fix: none needed; it stays in the env. Verified 4: file logging is off by default and writes /tmp/robosuite_<time>_<pid>.log only if FILE_LOGGING_LEVEL is set (robosuite/macros.py:47-48, utils/log_utils.py:75). Fix: none needed. Verified 5: install pulls pytest, opencv-python, pynput and MuJoCo 3.3-3.9 (setup.py:19-31). Fix: install into its own conda env, pinned robosuite==1.5.2. Windows: officially macOS and Linux (docs/installation.md:2); the docs have a Windows section (docs/installation.md:56+) and the code loads mujoco.dll on Windows (binding_utils.py:27-28). Unverified: whether the demos run cleanly on your Windows GPU. Containment: own conda env, test with python -m robosuite.demos.demo_random_action first.

## Safe install

Safe install (fixes applied):
Windows (Anaconda Prompt): conda create -n robosuite python=3.10 ; conda activate robosuite ; pip install robosuite==1.5.2 . If you get "mujoco.dll not found", follow the Windows steps in docs/installation.md (copy mujoco.dll from site-packages\\mujoco into site-packages\\robosuite\\utils). Test with python -m robosuite.demos.demo_random_action . Load only .pkl/.npz files you recorded yourself. While a keyboard or SpaceMouse teleop demo runs it hears every key press system-wide, so don't type passwords elsewhere until you close it.
Claude Code: same commands in that env. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the separate env and version pin: pip install robosuite (docs/installation.md:12) into your main Python.

## Install notes

Safe with fixes: robot-learning simulation framework on MuJoCo, no network calls or telemetry in its code. Install pinned 1.5.2 in its own conda env; load only pickle/npz files you made; keyboard/SpaceMouse teleop demos listen to key presses system-wide while running, so close them before typing anything private. Officially macOS/Linux; Windows works via the docs' Windows steps (mujoco.dll copy).
