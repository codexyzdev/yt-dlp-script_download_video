# YouTube Video Downloader

A Python script for downloading YouTube videos in various formats using yt-dlp.

## Features
- Downloads highest quality video+audio combination
- Supports multiple output formats (MKV, MP4, WEBM, etc.)
- Customizable output directory
- Preserves original video title
- Error handling and input validation

## Requirements
- Python 3.6+
- [FFmpeg](https://ffmpeg.org/) (must be installed and added to system PATH)
- Python dependencies listed in `requirements.txt`

## Installation
1. Install FFmpeg:
   - Windows: [Download from official site](https://ffmpeg.org/download.html)
   - Linux: `sudo apt install ffmpeg`
   - Mac: `brew install ffmpeg`

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt



Usage
bash
Copy
python downloader.py [URL] [OUTPUT_DIRECTORY] [FILE_FORMAT]
Examples:
bash
Copy
# Default settings (current directory, MKV format)
python downloader.py https://youtu.be/example_video

# Custom directory and MP4 format
python downloader.py https://youtu.be/example_video ~/Downloads mp4

# WEBM format
python downloader.py https://youtu.be/example_video ~/Videos webm
Notes
The script uses remuxing instead of re-encoding for faster processing

Supported formats: Any container format supported by FFmpeg (MKV, MP4, WEBM, etc.)

Files will be named automatically using the video's title

Disclaimer
This script is intended for educational purposes only. Respect copyright laws and YouTube's terms of service. Download only content you have rights to access.