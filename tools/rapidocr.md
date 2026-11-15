# RapidOCR

- **Type:** library
- **Category:** video analysis
- **Official URL:** https://rapidai.github.io/RapidOCRDocs
- **GitHub repo:** https://github.com/RapidAI/RapidOCR @ bd941da (tag v3.10.0, 2026-10-08, Apache-2.0; python/ folder)
- **Price:** Free (Apache-2.0, per PyPI, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot: Looks safe. Network use is only (1) a one-time download of the default ONNX models from ModelScope under the RapidAI/RapidOCR namespace, pinned to v3.10.0 with a SHA256 per file (python/rapidocr/default_models.yaml:313 on; inference_engine/onnxruntime/main.py:44-61; utils/download_file.py:67-76), and (2) fetching an image when the caller passes a URL instead of a file (utils/load_image.py:70). The SHA256 is checked when a cached model is reused, not right after the first download (utils/download_file.py:50-63). No subprocess, shell, telemetry, hooks or auto-updates; the only console script is the rapidocr CLI (python/pyproject.toml:43-44). eval() appears only in the optional PyTorch network builders, on class names from the package's own model configs (inference_engine/pytorch/networks/heads/__init__.py:40, transforms/__init__.py:30); PyTorch weights load with weights_only=True (pytorch/networks/main.py:66). Not reviewed: the legacy rapidocr_onnxruntime 1.2.3 package that is also installed (no v1.2.3 tag in the repo).

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install rapidocr==3.10.0 onnxruntime` (3.10.0 is the reviewed tag bd941da). Use the default pinned models (SHA256-checked on reuse) or files from the official model list only, and pass local image files, not URLs (a URL input is fetched with requests, utils/load_image.py:70). Don't use the legacy rapidocr_onnxruntime 1.x package (not reviewed). Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install rapidocr onnxruntime`

## Install notes

Claude Code: `pip install rapidocr onnxruntime` (official RapidOCR docs; since rapidocr 2.0.6 its default engine, ONNX Runtime, is a separate install)
Models: the default models download once from ModelScope (RapidAI/RapidOCR, pinned to the release) into the package folder. Only point model_path or model_root_dir at files from the official model list, and pass local image files rather than URLs from untrusted pages (a URL input is fetched with requests). The separate legacy package rapidocr_onnxruntime (1.x) was not part of this review.
