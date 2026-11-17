# ROS 2

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://docs.ros.org
- **GitHub repo:** https://github.com/ros2/ros2 @ f6edfcd (repos manifest, branch rolling; pushed 2026-10-20)
- **Price:** Free, open source (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @f6edfcd, a review, 2026-11-02): safe, official ROS 2 manifest repo, maintained; code not reviewed line by line. Install from the official docs or packages, not third-party scripts.

## Safe install

Safe install (fixes applied):
Windows 10/11: install ROS 2 Jazzy Jalisco (LTS, supported to May 2029 per docs.ros.org Releases) from the official binary archive: https://docs.ros.org/en/jazzy/Installation/Windows-Install-Binary.html, only the steps on that page (no third-party scripts). Or WSL2 Ubuntu 24.04: official apt packages per https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html. Lyrical Luth (May 2026, LTS to May 2031) is the newest release; use it only once its install page for your platform is live. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the LTS choice and the official-docs-only rule.
Install the rolling distro from docs.ros.org.

## Install notes

Safe, but ask the user before installing.
Any platform: install per the official docs at https://docs.ros.org (supported platforms listed there; not re-checked today).
