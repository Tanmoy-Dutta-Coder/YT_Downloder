import shutil
from pathlib import Path

import yt_dlp

Url = input("Youtube URL: ").strip()
ffmpeg_path = shutil.which("ffmpeg")
if ffmpeg_path is None:
    winget_packages = (
        Path.home()
        / "AppData"
        / "Local"
        / "Microsoft"
        / "WinGet"
        / "Packages"
    )
    ffmpeg_matches = winget_packages.rglob("ffmpeg.exe")
    ffmpeg_path = next(ffmpeg_matches, None)

format_selection = (
    "bestvideo+bestaudio/best"
    if ffmpeg_path
    else "best[ext=mp4]/best"
)

options = {
    "format": format_selection,
}
if ffmpeg_path:
    options["ffmpeg_location"] = str(Path(ffmpeg_path).parent)

yt_dlp.YoutubeDL(options).download([Url])