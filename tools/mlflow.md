# MLflow

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/mlflow/mlflow
- **GitHub repo:** https://github.com/mlflow/mlflow @ b900a0d (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @b900a0d, a review, 2026-11-02): caution. Usage telemetry on unless MLFLOW_DISABLE_TELEMETRY or DO_NOT_TRACK is set (`mlflow/telemetry/utils.py:153-158`).

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install mlflow==<release matching b900a0d>. Set the user env var MLFLOW_DISABLE_TELEMETRY=true (or DO_NOT_TRACK=1) before first use; otherwise usage telemetry is on (mlflow/telemetry/utils.py:153-158). Run mlflow ui on localhost only (default 127.0.0.1). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and the telemetry switch.
Windows: pip install mlflow; usage telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install mlflow` in a venv; set MLFLOW_DISABLE_TELEMETRY=true.
