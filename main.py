import yt_dlp
from pathlib import Path

DOWNLOAD_DIR = Path.home() / "Downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

def download_mp3(url: str):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "ffmpeg_location": "C:\\ffmpeg\\ffmpeg-master-latest-win64-gpl\\bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Paste YouTube URL: ").strip()
    download_mp3(url)
