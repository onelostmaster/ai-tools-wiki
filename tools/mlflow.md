# MLflow

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/mlflow/mlflow
- **GitHub repo:** https://github.com/mlflow/mlflow @ b900a0d (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @b900a0d, a review, 2026-11-02): caution. Usage telemetry on unless MLFLOW_DISABLE_TELEMETRY or DO_NOT_TRACK is set (`mlflow/telemetry/utils.py:153-158`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install mlflow` in a venv; set MLFLOW_DISABLE_TELEMETRY=true.
