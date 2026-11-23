# ThinkingOrbs (haplollc)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://github.com/haplollc/ThinkingOrbs
- **GitHub repo:** https://github.com/haplollc/ThinkingOrbs @ 1.1.0 (e2c07bb; MIT)
- **Price:** Free (MIT LICENSE file, checked 2026-11-22)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

Claude code read @7b09b5f, 2026-11-22: safe with the Install notes fix. Library imports only CoreGraphics, Foundation, SwiftUI (Sources/ThinkingOrbs/*.swift); no network, file or analytics code; no dependencies (Package.swift); Scripts/ are maintainer-only. Verified risk, fixed: README install floats to any 1.x (from: "1.0.0"); fix: exact 1.1.0 (Sources identical to main).

## Safe install

Safe install (fixes applied): only inside an iOS/macOS SwiftUI app project on a Mac with Xcode 16+: add the package with Dependency Rule Exact Version 1.1.0, i.e. .package(url: "https://github.com/haplollc/ThinkingOrbs", exact: "1.1.0") in Package.swift. Windows, Android, claude.ai, Claude Code, Hermes: not installable (Swift/SwiftUI only); use thinking-orbs (Jakub Antalik) for web pages and artifacts instead.

## YOLO install

YOLO (your own risk): skips the exact 1.1.0 pin: README default .package(url: "https://github.com/haplollc/ThinkingOrbs", from: "1.0.0"), which floats to any later 1.x.

## Install notes

Skip for fit, not safety. Ask the user first. Only for an iOS/macOS SwiftUI app: Xcode > Add Package Dependencies > https://github.com/haplollc/ThinkingOrbs, Dependency Rule Exact Version 1.1.0 (Package.swift: .package(url: "https://github.com/haplollc/ThinkingOrbs", exact: "1.1.0")). Repo is 31 MB (README GIFs), downloaded once. Runs on: Mac with Xcode 16+ (iOS 17+, macOS 14+ apps) only.
