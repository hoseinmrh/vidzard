import argparse
import yt_dlp

def download_video(url, output_path="."):
    """Downloads a YouTube video from the given URL using yt-dlp.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str, optional): The path to save the video. Defaults to ".".
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_path}/video',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded video to '{output_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a YouTube video.")
    parser.add_argument("url", type=str, help="The URL of the YouTube video.")
    parser.add_argument("--output_path", type=str, default=".", help="The path to save the video.")
    args = parser.parse_args()

    download_video(args.url, args.output_path)
