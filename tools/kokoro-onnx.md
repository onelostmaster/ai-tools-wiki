# kokoro-onnx

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/thewh1teagle/kokoro-onnx
- **GitHub repo:** https://github.com/thewh1teagle/kokoro-onnx @ 3596b26 (pyproject 0.6.1; MIT; Kokoro model Apache-2.0; committed 2026-09-01 16:26 ET, still HEAD on 2026-11-10)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-10

## Safety reason

a review bot (code read @3596b26, 2026-11-10, no-intake review): Safe for local use. About 1,800 lines of Python in src/kokoro_onnx/; no subprocess, os.system, eval/exec, network calls or telemetry. Voices load with np.load at its default allow_pickle=False (__init__.py line 74), so a tampered voices file cannot run code; the model runs in ONNX Runtime with CPU or any available accelerator, overridable with ONNX_PROVIDER (session.py lines 43-66). tokenizer.py lines 31-55 load the espeak-ng shared library with ctypes from the espeakng-loader package, or from PHONEMIZER_ESPEAK_LIBRARY if set, falling back to a system-wide espeak-ng. Model files are never fetched by the code (config.py lines 32-37 only print where to download them). Not reviewed: examples/, scripts/ (export.py, fetch_voices.py are maintainer tools) and dependencies (onnxruntime, phonemizer, espeakng-loader).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @3596b26 (pyproject version 0.6.1; PyPI 0.6.1 uploaded 2026-08-18 ET, a little older than this commit) (safe). Windows (Python 3.10 to 3.13): pip install kokoro-onnx==0.6.1 soundfile, or kokoro-onnx[gpu]==0.6.1 for an NVIDIA card. Download kokoro-v1.0.onnx (or the smaller int8 file) and voices-v1.0.bin by hand from the project's own GitHub releases page (https://github.com/thewh1teagle/kokoro-onnx/releases) into your project folder; the library never downloads anything itself and does not check the files, so get them only from that page. espeak-ng comes bundled through the espeakng-loader package, so nothing else to install on Windows. Runs fully offline after that.
