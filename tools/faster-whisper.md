# faster-whisper

- **Type:** library
- **Category:** voice and audio, research
- **Official URL:** https://github.com/SYSTRAN/faster-whisper
- **GitHub repo:** https://github.com/SYSTRAN/faster-whisper @ 9e472ae (2026-10-16, v1.2.1, MIT)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @9e472ae, v1.2. The only network use is model download from Hugging Face via huggingface_hub.snapshot_download, limited to model files (`faster_whisper/utils.py:91-115`); pass local_files_only=True or download_root to stay offline (`transcribe.py:631-685`). VAD uses a bundled ONNX file (`vad.py:332-351`). No telemetry, shell, subprocess, pickle or prompt injection; the only exec is setup.py reading its own version file (`setup.py:18`). Dependencies are mainstream (ctranslate2, onnxruntime, av, tokenizers).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install faster-whisper` (PyPI); its models come from Hugging Face, which is blocked in the a project sandbox.
