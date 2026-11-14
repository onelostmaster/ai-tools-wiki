# Motion (React/JS animation library)

- **Type:** library
- **Category:** frontend, design
- **Official URL:** https://motion.dev
- **GitHub repo:** https://github.com/motiondivision/motion
- **Price:** Free MIT library verified online 2026-11-08 at https://motion.dev/docs/react and official GitHub README/license. Motion+ paid extras are separate and not required; no Motion+ price claimed.
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

Targeted runtime read @78f3ff5 (Motion package 14.10.1), not a complete dependency/security audit. Local browser animation library; no telemetry SDK, network fetch/beacon, general eval/new Function or subprocess execution found in scoped motion/framer-motion/motion-dom/motion-utils runtime scan. Regex .exec calls are not code execution. packages/motion/package.json:44-48 exports motion/react; packages/framer-motion/src/utils/reduced-motion/use-reduced-motion.ts:37 provides preference handling. Root package.json:22 prepare runs turbo build/measure for source installs; :26-28 site/Slack publisher scripts are maintainer tools, not evidence of runtime reporting. Published package/install artifacts not audited. React hooks are UI behavior, not agent permission hooks. Use npm package rather than running repository maintainer scripts; no automatic software update seen in scoped runtime.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Ask the user before installing. Documentation only, NOT run: npm install motion (README.md:16); import from motion/react. Windows development; standards-based web UI usable in Android browsers, specific device performance untested. Claude Code/Hermes can author code using it, not native agent plugins. claude.ai can advise/generate code but cannot install local npm packages. Respect reduced motion, focus/keyboard behavior and real-device testing. Article bottom sheet lacks complete focus-management/keyboard safeguards; aria-modal alone is insufficient, and reducing duration alone does not disable drag elasticity. Do not treat snippet/linter as production-ready. Agent AI Kit/MCP mentioned by upstream docs is a separate product not reviewed in this send.
