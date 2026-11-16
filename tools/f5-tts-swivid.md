# F5-TTS (SWivid)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/SWivid/F5-TTS
- **GitHub repo:** https://github.com/SWivid/F5-TTS @ 600e5fd (code MIT; pre-trained weights CC-BY-NC; pip f5-tts 1.1.22)
- **Price:** Free; code MIT, weights CC-BY-NC (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @600e5fd, 2026-11-03): safe for inference. Loads safetensors or torch.load with weights_only=True (`src/f5_tts/infer/utils_infer.py:112,200`) from the official SWivid Hugging Face repo (`src/f5_tts/api.py:71`); no telemetry in inference; wandb is the default logger only for training (`src/f5_tts/model/trainer.py:43,59`). The optional socket_server binds 0.0.0.0 by default (`src/f5_tts/socket_server.py:210`), use 127.0.0.1. The finetune Gradio app builds shell commands from its form (`src/f5_tts/train/finetune_gradio.py:330,469`) and torch.loads .pt without weights_only (`:981`), so only load your own files. Weights CC-BY-NC (`README.md:278`): no commercial use.

## Safe install

Safe install (fixes applied):
Windows: in a venv, install PyTorch (CUDA or CPU build from pytorch.org), then `pip install f5-tts==1.1.22` (latest on PyPI, 2026-11-15). Use the CLI or the inference Gradio app. If you run the socket server, start it with `--host 127.0.0.1` (default is 0.0.0.0, src/f5_tts/socket_server.py:210). In the finetune Gradio app, load only your own .pt files (it torch.loads without weights_only, src/f5_tts/train/finetune_gradio.py:981). Pre-trained weights are CC-BY-NC (README.md:278): it will be non-commercial unless you train your own, so not for a monetized channel. wandb logging is used only in training (src/f5_tts/model/trainer.py:43,59); pass a different logger or set WANDB_MODE=offline there. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the venv, version pin and the 127.0.0.1 bind.
pip install f5-tts

## Install notes

Safe, but ask the user before installing.
Windows: Python + PyTorch (CUDA or CPU), `pip install f5-tts` (`README.md:103`), then the Gradio app or CLI. Pre-trained weights are non-commercial, so not for a monetized channel unless you train your own. Android: no.
