# claude-code-video-toolkit

- **Type:** plugin
- **Category:** generating videos
- **Official URL:** https://github.com/digitalsamba/claude-code-video-toolkit
- **GitHub repo:** [https://github.com/digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)
- **Price:** Free code; many paid API keys (not verified)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @9b0c90d (2026-11-14): safe with fixes, Skip. Without R2, upload_to_storage falls back to public anonymous hosts litterbox.catbox.moe and 0x0.st (tools/file_transfer.py:183-192): set up R2 and delete that fallback loop in your copy. docker/modal-propainter/app.py:127 runs eval() on ffprobe's frame rate: replace with float(Fraction(fps_str)). Needs many paid API keys.

## Safe install

Safe install (fixes applied):
Clone at 9b0c90d; configure R2; delete tools/file_transfer.py lines 183-192; replace eval at docker/modal-propainter/app.py:127 with float(fractions.Fraction(fps_str)); keys in env.

## YOLO install

YOLO (your own risk): skips R2 and the patch, so your voice, photo and video inputs go to public hosts.
Clone and run as the README says.

## Install notes

Ask the user before installing.
Claude Code: no steps given (the source withholds them for caution items).
