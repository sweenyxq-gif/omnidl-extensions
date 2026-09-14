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
git remote add origin https://github.com/sweenyxq-gif/omnidl-extensions.git

# 3. Stage, commit, and push
git add .
git commit -m "feat: initial release of 15 curated OmniDownloader extensions"
git push -u origin main
```

Once pushed, your extensions will be live and accessible over-the-air via:
- **Repository Index**: `https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/extensions.json`
- **Script Direct URL**: `https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/<script-name>.user.js`

---

## 📦 Curated Resolver Extensions (15 Included)

| Extension | Category | Target Platforms | Direct Raw Link |
| :--- | :--- | :--- | :--- |
| **All-in-One Video Downloader (HD)** | Media | YouTube, TikTok, Instagram, Threads, Facebook, X/Twitter, TED | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/all-in-one-video-downloader.user.js) |
| **Buzzheavier Direct Resolver** | Filehost | `buzzheavier.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/buzzheavier.user.js) |
| **FileAxa Direct Resolver** | Filehost | `fileaxa.com`, `s*.fileaxa.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/fileaxa.user.js) |
| **Gofile Direct Stream Resolver** | Filehost | `gofile.io` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/gofile.user.js) |
| **Pixeldrain Direct Resolver** | Filehost | `pixeldrain.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/pixeldrain.user.js) |
| **MediaFire Direct Resolver** | Filehost | `mediafire.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/mediafire.user.js) |
| **1Fichier Direct Resolver** | Filehost | `1fichier.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/1fichier.user.js) |
| **Krakenfiles Direct Resolver** | Filehost | `krakenfiles.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/krakenfiles.user.js) |
| **Hugging Face Model & Dataset Resolver** | AI Models | `huggingface.co` (.safetensors, .gguf) | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/huggingface.user.js) |
| **Civitai AI Model Direct Resolver** | AI Models | `civitai.com` (Checkpoints, LoRAs, VAEs) | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/civitai.user.js) |
| **GitHub Release Assets Resolver** | Development | `github.com` (APKs, archives, binaries) | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/github-releases.user.js) |
| **GitLab Release Assets Resolver** | Development | `gitlab.com` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/gitlab-releases.user.js) |
| **Internet Archive Files Resolver** | Archives | `archive.org` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/internet-archive.user.js) |
| **SourceForge Project Files Resolver** | Development | `sourceforge.net` | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/sourceforge.user.js) |
| **Universal Media & Stream Sniffer** | Media | All web pages (HTML5, M3U8, MPD) | [Install](https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts/universal-media-sniffer.user.js) |

---

## 🛠️ Adding New Extensions & Updating Index

Whenever you add or update a script in `userscripts/`:

1. Put your `.user.js` in `userscripts/`.
2. Run the automatic manifest generator:
   ```bash
   python build_manifest.py
   ```
3. Commit and push:
   ```bash
   git add .
   git commit -m "feat: add new resolver extension"
   git push
   ```
OmniDownloader clients will automatically discover the new or updated extension on their next check!
