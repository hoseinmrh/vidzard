import argparse
import os
from src.vidzard.data.data_handler import load_json
from src.vidzard.video.composer import create_highlight_video

def main():
    parser = argparse.ArgumentParser(description="Create a highlight video from a video and a list of important segment IDs.")
    parser.add_argument('--video_path', type=str, default='video.mp4', help='Path to the video file.')
    parser.add_argument('--transcript_path', type=str, default='transcript.json', help='Path to the transcript JSON file.')
    parser.add_argument('--important_ids_path', type=str, default='important_ids.json', help='Path to the JSON file containing important segment IDs.')
    parser.add_argument('--output_path', type=str, default='final_highlight.mp4', help='Path to save the final highlight video.')
    
    args = parser.parse_args()

    try:
        transcript = load_json(args.transcript_path)
        important_ids = load_json(args.important_ids_path)
        create_highlight_video(args.video_path, transcript, important_ids, args.output_path)
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure the transcript and important IDs files exist.")

if __name__ == "__main__":
    main()
