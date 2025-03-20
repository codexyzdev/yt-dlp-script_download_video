import yt_dlp
import os
import sys

def download_video(url, directory, extension):
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': extension,
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'verbose': True,
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',  # More efficient than converting
            'preferedformat': extension,
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nError during download: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: You must provide at least the URL")
        print("Usage: python script.py <URL> [directory] [extension]")
        print("Example 1: python downloads.py https://youtu.be/example")
        print("Example 2: python downloads.py https://youtu.be/example /path/downloads mp4")
        print("Example 3: python downloads.py https://youtu.be/example /path/downloads [FFmpeg(mkv, mp4, webm, etc.)]")
        
        sys.exit(1)
    
    url = sys.argv[1]
    directory = sys.argv[2] if len(sys.argv) >= 3 else os.getcwd()
    extension = sys.argv[3] if len(sys.argv) >= 4 else 'mkv'

    # Basic URL validation
    if not url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)

    download_video(url, directory, extension)