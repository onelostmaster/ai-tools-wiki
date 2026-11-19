# Bubblewrap

- **Type:** CLI
- **Category:** building a site, developer tools
- **Official URL:** https://github.com/GoogleChromeLabs/bubblewrap
- **GitHub repo:** https://github.com/GoogleChromeLabs/bubblewrap
- **Price:** Free (Apache-2.0)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot code read @364d82f: safe with the fixes in Safe install. The npm packages have no install hooks (packages/*/package.json scripts are build/lint/test only; the root postinstall is for repo development, not the published package). No telemetry. It writes its config to %USERPROFILE%\.bubblewrap\\config.json (packages/cli/src/lib/config.ts:28-30) and runs the JDK's keytool and the project's gradlew.bat as child processes (packages/core/src/lib/GradleWrapper.ts:42, jdk/KeyTool.ts:77). Verified behaviour and fixes: (1) on first run init offers to download JDK 17 from Adoptium on GitHub and the Android command-line tools from dl.google.com into .bubblewrap\\jdk and .bubblewrap\\android_sdk, with no checksum check (packages/cli/src/lib/JdkInstaller.ts:22-25,104-117; AndroidSdkToolsInstaller.ts:23-26,60-64), and on Windows it picks the 32-bit JDK (JdkInstaller.ts:30); fix: answer No to both prompts (config.ts:38,61) and give the paths of a 64-bit Temurin 17 JDK and the Android command-line tools you downloaded from adoptium.net and developer.android.com and checked against the SHA-256 shown there. (2) The generated Android project's Gradle wrapper downloads Gradle 8.11.1 from services.gradle.org with no distributionSha256Sum (packages/core/template_project/gradle/wrapper/gradle-wrapper.properties); fix: add distributionSha256Sum with the checksum from gradle.org/release-checksums before the first build. (3) build reads the keystore passwords from BUBBLEWRAP_KEYSTORE_PASSWORD and BUBBLEWRAP_KEY_PASSWORD if both are set, else prompts (packages/cli/src/lib/cmds/build.ts:78-91); fix: type them at the prompt, don't set them in the environment, keep the keystore out of git and back it up yourself. (4) validate sends the site URL to Google's PageSpeed Insights API (packages/validator/src/lib/psi/PageSpeedInsights.ts:20); only use it on a public URL. The play command uses a Google Play service-account key (packages/core/src/lib/GooglePlay.ts:232); fix: skip it and upload in Play Console by hand. Dependencies use ^ ranges; fix: exact pin and npm ci.

## Safe install

Safe install (fixes applied): Claude Code on Windows, only if the PWA needs a Play Store listing: in a separate project folder, npm install --save-exact @bubblewrap/cli@1.27.0 (Node 18+), commit package-lock.json, use npm ci afterwards and run it with npx bubblewrap from that folder, not -g. Before init, download a 64-bit Temurin JDK 17 from adoptium.net and the Android command-line tools from developer.android.com yourself and check each SHA-256 against the value on that page; at the two download prompts in npx bubblewrap init answer No and give those paths (or set them later with npx bubblewrap updateConfig --jdkPath <path> --androidSdkPath <path>). Before the first npx bubblewrap build, add distributionSha256Sum=<checksum of gradle-8.11.1-bin.zip from gradle.org/release-checksums> to gradle\\wrapper\\gradle-wrapper.properties. Type the keystore passwords at the prompt (don't set BUBBLEWRAP_KEYSTORE_PASSWORD/BUBBLEWRAP_KEY_PASSWORD), keep the keystore and passwords out of git and chat, and back the keystore up yourself. Don't use the play command; upload the .aab in Play Console. claude.ai and Hermes: no install route. Android: nothing to install for the tool; the built app installs on Android.

## YOLO install

YOLO (your own risk): skips the exact pin, the lockfile install, the checked JDK/SDK downloads (you get the unchecked 32-bit JDK on Windows) and the Gradle checksum. npm i -g @bubblewrap/cli, then bubblewrap init --manifest https://<your-site>/manifest.json and accept the downloads, then bubblewrap build (README).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Only needed if a project PWA later needs a Play Store listing; PWA first was the advice.
