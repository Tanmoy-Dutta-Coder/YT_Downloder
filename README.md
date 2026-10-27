# YT_Downloder
# YouTube Video Downloader

This script downloads a YouTube video using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). It prompts for a video URL and selects a format based on whether FFmpeg is available.

## Requirements

- Python
- `yt-dlp`
- FFmpeg (optional; recommended for the best available video and audio quality)

Install `yt-dlp` with:

```powershell
py -m pip install yt-dlp
```

## Usage

From the folder containing `yt.py`, run:

```powershell
py yt.py
```

When prompted, paste a YouTube video URL. The downloaded file is saved to the current working directory.

## Format selection

- If FFmpeg is found on `PATH`, or in the standard WinGet packages directory, the script requests the best video and audio streams and uses FFmpeg to combine them.
- If FFmpeg is not found, it requests the best MP4 format available, falling back to the best available format.

To make FFmpeg available, install it and ensure `ffmpeg.exe` is on `PATH`. The WinGet fallback is Windows-specific.

## Responsible use

Only download videos when you have the right to do so. Follow YouTube's terms and respect copyright and the creator's rights.
