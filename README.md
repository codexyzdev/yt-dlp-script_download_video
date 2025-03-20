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