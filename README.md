# OmniDownloader Extensions Repository (`omnidl-extensions`)
This repository serves as the official and community-curated **Resolver Extensions Hub** for **OmniDownloader** (Android & Desktop).
Extensions are sandboxed Userscripts (`.user.js`) that teach OmniDownloader how to resolve direct high-speed streams from file hosts, video sites, AI model hubs, and developer platforms without requiring an app or APK update.
---
## 🚀 Pushing to GitHub
To publish this repository under your own GitHub account:
```bash
cd omnidl-extensions
# 1. Initialize git (if not already initialized)
git init
git branch -M main
# 2. Add your GitHub remote
# Replace "user" with your actual GitHub username/organization:
git remote add origin https://github.com/user/omnidl-extensions.git
# 3. Stage, commit, and push
git add .
git commit -m "feat: initial release of 15 curated OmniDownloader extensions"
git push -u origin main
```
Once pushed, your extensions will be live and accessible over-the-air via:
- **Repository Index**: `https://raw.githubusercontent.com/user/omnidl-extensions/main/extensions.json`
- **Script Direct URL**: `https://raw.githubusercontent.com/user/omnidl-extensions/main/userscripts/<script-name>.user.js`
---
## 📦 Curated Resolver Extensions (15 Included)
| Extension | Category | Target Platforms | Direct Raw Link |
| :--- | :--- | :--- | :--- |
| **All-in-One Video Downloader (HD)** | Media | YouTube, TikTok, Instagram, Threads, Facebook, X/Twitter, TED | [Install](https://raw.githubusercontent.com/user/omnidl-extensions/main/userscripts/all-in-one-video-downloader.user.js) |
| **Buzzheavier Direct Resolver** | Filehost | `buzzheavier.com` | [Install](https://raw.githubusercontent.com/user/omnidl-extensions/main/userscripts/buzzheavier.user.js) |
