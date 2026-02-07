# YouTube to MP3 Converter 🎧

A simple, safe, and local **YouTube → MP3 converter** built using modern Python tooling.  
Designed especially for **karaoke tracks, instrumentals, and singing practice**.

No ads. No shady websites. Runs completely on your machine.

---

## ✨ Features

- 🎵 Downloads **best available audio quality**
- 🔄 Converts audio to **MP3**
- 📂 Saves files directly to your **Windows Downloads folder**
- ⚡ Uses **yt-dlp** (actively maintained)
- 🧪 Uses **uv** for fast & reproducible environments
- 🛡️ No malware, no pop-ups

---

## 🛠 Tech Stack

- **Python 3.11**
- **uv** – modern Python package manager
- **yt-dlp** – YouTube downloader
- **FFmpeg** – audio extraction & conversion

---

## 📦 Project Structure

.
├── main.py # Main script
├── pyproject.toml # Project & dependency config
├── uv.lock # Locked dependencies (reproducible)
├── .python-version # Python version pin
├── .gitignore
└── README.md


---

## 🚀 Setup Instructions

### 1️⃣ Install Python
Make sure Python **3.11+** is installed.
Make sure you download the dependencies ffmpeg and yt-dlp. (ANY YOUTUBE TUTORIAL IS ENOUGH)

### Check:
```bash
python --version
pip install uv
uv --version

uv sync


## 📦 Project Structure

