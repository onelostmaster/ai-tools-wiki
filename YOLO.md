# YOLO installs

The tool's own defaults: no fixes, no sandbox, at your own risk. Never offered for avoid or unreviewed tools.

- [agent-browser](tools/agent-browser.md): YOLO (your own risk): skips the pin, --ignore-scripts, AGENT_BROWSER_NO_VERSION_CHECK=1, the domain/action/output limits, and the ban on attach modes and plugins.
`npm install -g agent-browser`, then `agent-browser install` (README / agent-browser.dev/installation).
- [AgenticSeek](tools/agenticseek.md): YOLO (your own risk): skips Docker, so model-written shell runs as you.
python3 cli.py on the host with WORK_DIR set to your files.
- [Apify (API + MCP)](tools/apify-api-mcp.md): YOLO (your own risk): skips telemetry off, the tool allowlist and price checks.
npx @apify/actors-mcp-server with defaults.
- [Astryx](tools/astryx.md): YOLO (your own risk): skips the pinned version, --ignore-scripts, NO_UPDATE_NOTIFIER=1, the deny rule against global npm, and staying off the hosted MCP and `astryx init --user`.
`npm i -g @astryxdesign/cli` (README), or install the Astryx skill, which tells an agent to run that command when `astryx` is not found (SKILL.md:19).
- [Claude in Chrome](tools/claude-in-chrome.md): YOLO (your own risk): skips per-action approval.
'Automatically approve' mode in your main Chrome profile.
- [Claude Quickstarts](tools/claude-quickstarts.md): YOLO (your own risk): skips the commit pin, Docker isolation, the no-extra-mounts rule, and skipping Managed Agents and macOS-native samples.
Clone https://github.com/anthropics/claude-quickstarts and follow each sample's README, including the `docker run` that mounts `$HOME/.anthropic` (computer-use-demo/README.md:51-58).
- [claude-3d-animated-shorts (thuann-vn)](tools/claude-3d-animated-shorts-thuann-vn.md): YOLO (your own risk): skips the commit pin.
git clone https://github.com/thuann-vn/claude-3d-animated-shorts %USERPROFILE%\.claude\\skills\\claude-3d-animated-shorts, then scripts/fetch-assets.sh and npm install in engine/
- [claude-code-video-toolkit](tools/claude-code-video-toolkit.md): YOLO (your own risk): skips R2 and the patch, so your voice, photo and video inputs go to public hosts.
Clone and run as the README says.
- [Cloudflare Pages](tools/cloudflare-pages.md): YOLO (your own risk): skips single-repo GitHub access, the pinned project-local Wrangler, telemetry off and the No to the skills prompt.
Connect GitHub with "All repositories"; `npm i -g wrangler` and accept its prompts.
- [creator-generalist (codepawl)](tools/creator-generalist-codepawl.md): YOLO (your own risk): skips the commit pin, the local marketplace and the per-tool no answers.
/plugin marketplace add codepawl/creator-generalist
/plugin install <name>@creator-generalist (each of the five plugins)
- [Demucs (htdemucs)](tools/demucs-htdemucs.md): YOLO (your own risk): skips the virtual environment and the exact pin (the built-in-models-only rule still applies).
`pip install demucs`
- [earshot](tools/earshot.md): YOLO (your own risk): skips the commit pin, the CPU-only torch index and offline mode.
`git clone https://github.com/Leonxlnx/earshot` then `pip install -e ".[mcp]"` and `claude mcp add earshot -- python -m earshot mcp` (still never set GEMINI_API_KEY).
- [ElevenLabs connector (Claude directory)](tools/elevenlabs-connector-claude-directory.md): YOLO (your own risk): skips the ask-before-video rule and scope limits.
Connect with every permission and generate freely.
- [Emscripten (emsdk)](tools/emscripten-emsdk.md): YOLO (your own risk): skips the digest-pinned container.
Local `./emsdk install latest` then `./emsdk activate latest` (emscripten.org).
- [faster-whisper](tools/faster-whisper.md): YOLO (your own risk): skips the virtual environment, the exact pin and offline mode.
`pip install faster-whisper`
- [find-skills (vercel-labs/skills)](tools/find-skills-vercel-labs-skills.md): YOLO (your own risk): skips the deny and telemetry off.
npx skills add vercel-labs/skills@find-skills -g -y.
- [GitHub Actions (official actions/*)](tools/github-actions-official-actions.md): YOLO (your own risk): skips the SHA pins and the read-only token.
`uses: actions/checkout@v7` with the repo's default token permissions.
- [GitHub Pages](tools/github-pages.md): YOLO (your own risk): skips the SHA pins and the minimal permissions.
Turn on Pages from a branch in the repo settings, or use the starter workflow with tag versions (actions/deploy-pages@v4).
- [gltfjsx](tools/gltfjsx.md): YOLO (your own risk): skips the folder install and the exact reviewed version.
`npx gltfjsx model.glb` (runs npm latest 6.5.3).
- [Google Fonts](tools/google-fonts.md): YOLO (your own risk): skips self-hosting, so every page load sends the viewer's IP and the page URL to Google.
A stylesheet link tag to fonts.googleapis.com in the page head.
- [herdr](tools/herdr.md): YOLO (your own risk): skips the SHA-256 check, the ban on piped installers, and turning off background version and manifest checks.
Windows: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` (README.md:45).
- [Hermes Agent (Nous Research)](tools/hermes-agent-nous-research.md): YOLO (your own risk): skips the container, approvals and script read.
iex (irm https://hermes-agent.nousresearch.com/install.ps1) on the local backend.
- [img2threejs](tools/img2threejs.md): YOLO (your own risk): skips the pin and adds the hosted add-ons.
npx --yes img2threejs@latest install then img2 add img2glb --yes.
- [Instagram Agent skill](tools/instagram-agent-skill.md): YOLO (your own risk): skips the commit pin and installs for your user in every project.
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
- [last30days skill](tools/last30days-skill.md): YOLO (your own risk): skips the pin and the cookie switches, so it reads your browser's X cookies.
Install the latest skill as its README says and run setup with --allow-browser-cookies.
- [librosa](tools/librosa.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install librosa`
- [oh-my-hermes](tools/oh-my-hermes.md): YOLO (your own risk): skips the pin, script read and test profile.
curl -fsSL https://omher.app/install | sh with the auto update mode.
- [Playwright + Chromium](tools/playwright-chromium.md): YOLO (your own risk): skips the venv and version pin, and downloads every browser.
pip install playwright
playwright install
- [print3d](tools/print3d.md): YOLO (your own risk): skips the container.
Add the print3d MCP to Hermes on your PC's local backend.
- [pykakasi](tools/pykakasi.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pykakasi`
- [pyloudnorm](tools/pyloudnorm.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pyloudnorm`
- [PySceneDetect](tools/pyscenedetect.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install --upgrade scenedetect`
- [RapidOCR](tools/rapidocr.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install rapidocr onnxruntime`
- [React Three Fiber (R3F)](tools/react-three-fiber-r3f.md): YOLO (your own risk): skips the exact reviewed pins.
`npm install three @react-three/fiber`
- [Remotion (framework, v4)](tools/remotion-framework-v4.md): YOLO (your own risk): skips the exact pins.
`npx create-video@latest`
- [Remotion agent skills (official)](tools/remotion-agent-skills-official.md): YOLO (your own risk): skips the installer version pin and the telemetry switch.
npx skills add remotion-dev/skills
- [RustDesk](tools/rustdesk.md): YOLO (your own risk): skips 2FA and the Tailscale whitelist.
Default install with the public ID server and one-time passwords.
- [shazamio](tools/shazamio.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install shazamio`
- [taste-skill](tools/taste-skill.md): YOLO (your own risk): skips the commit pin, the ban on install.sh, and deleting the Stop hook, so gate.mjs can run on every Claude Code stop.
Run the repo's `install.sh` from HEAD, leaving the hooks block in SKILL.md.
- [Terminal Browser](tools/terminal-browser.md): YOLO (your own risk): skips telemetry off and the script read.
curl -fsSL https://terminal-browser.sh/install | bash.
- [three-bvh-csg (with three-mesh-bvh)](tools/three-bvh-csg-with-three-mesh-bvh.md): YOLO (your own risk): skips the exact pins on the reviewed versions.
`npm install three-bvh-csg three-mesh-bvh`
- [three.js (three@0.186.1)](tools/three-js-three-0-186-1.md): YOLO (your own risk): skips the exact reviewed pin.
`npm install three`
- [Threejs-Awesome-Graphics-Agent-Skills (scottstts)](tools/threejs-awesome-graphics-agent-skills-scottstts.md): YOLO (your own risk): skips the pinned commit and the hand-picked folders.
`npx threejs-awesome-graphics-agent-skills install`
- [TinyFish (MCP + Claude Code plugin + connector)](tools/tinyfish-mcp-claude-code-plugin-connector.md): YOLO (your own risk): skips the wallet deny and the doctor block.
Install the plugin as its README says and allow every tool.
- [Transformers.js (@huggingface/transformers)](tools/transformers-js-huggingface-transformers.md): YOLO (your own risk): skips the exact pin and the pinned model revisions.
`npm install @huggingface/transformers`
- [tstack (t3dotgg)](tools/tstack-t3dotgg.md): YOLO (your own risk): skips the commit pin and the deny rules that block `gh pr merge` and the GitHub MCP merge tool, so full-send can merge PRs and force-push.
Copy the skills as the README says, without those deny rules.
- [UI SDK (vercel-labs/ui)](tools/ui-sdk-vercel-labs-ui.md): YOLO (your own risk): skips the pin, --ignore-scripts, and the pin-or-self-host rule for web.js.
`npm install @ui-sdk/react @ui-sdk/core` (or the adapter) and `npx skills add vercel-labs/ui --skill ui-sdk` (README).
- [ui-ux-pro-max skill](tools/ui-ux-pro-max-skill.md): YOLO (your own risk): skips leaving out the stack/ template (auto-enables its project MCP servers and allows reading your home folder).
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill, then copy stack/ into the project as stack/docs/SETUP.md describes.
- [Upload-Post MCP](tools/upload-post-mcp.md): YOLO (your own risk): skips the hosted-only rule (local npx mode can upload any absolute local file path, src/tools/upload.ts:625).
Install the official Upload-Post plugin from the Claude directory (README.md:23).
- [Vercel](tools/vercel.md): YOLO (your own risk): skips the pinned project-local CLI and telemetry off.
`npm i -g vercel` (Vercel CLI docs).
- [Vite](tools/vite.md): YOLO (your own risk): skips the exact reviewed pin.
`npm create vite@latest` (vite.dev Getting Started).
- [VoiceStudio](tools/voicestudio.md): YOLO (your own risk): skips the release download (pipes the official script into PowerShell) and allows the MOSS-TTS engines.
irm https://voicestudio.sh/install.ps1 | iex
- [web-artifacts-builder (Anthropic)](tools/web-artifacts-builder-anthropic.md): YOLO (your own risk): skips installing pnpm yourself first, so the script runs `npm install -g pnpm` globally.
`/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills`
- [wllama](tools/wllama.md): YOLO (your own risk): skips the source build at the reviewed commit c10c211.
`npm install @wllama/wllama` (official npm package, latest 3.13.0 on 2026-11-14).
- [yt-dlp](tools/yt-dlp.md): YOLO (your own risk): skips the pin, config and plugin blocks and the no-cookies rule.
pip install -U yt-dlp then yt-dlp --cookies-from-browser chrome URL.
- [Zapier (connector)](tools/zapier-connector.md): YOLO (your own risk): skips managed mode, so it can write and run code.
Agentic mode with all actions.
- [Zernio MCP + Claude plugin](tools/zernio-mcp-claude-plugin.md): YOLO (your own risk): skips unticking the paid ads tools.
/plugin marketplace add zernio-dev/zernio-claude-plugin
/plugin install zernio@zernio
