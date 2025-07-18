import os
import argparse
from dotenv import load_dotenv
import torch
from src.vidzard.data.data_handler import load_json, save_json, process_important_ids
from src.vidzard.analysis.transcriber import transcribe_video
from src.vidzard.analysis.analyzer import get_important_segments
from src.vidzard.video.composer import create_highlight_video

def main():
    parser = argparse.ArgumentParser(description="Generate a highlight video from a video file.")
    parser.add_argument('--video_path', type=str, default='video.mp4', help='Path to the video file.')
    parser.add_argument('--user_prompt', type=str, default="This is an interview about an urban project. Identify the most important segments.", help='Prompt for the AI to identify important segments.')
    parser.add_argument('--output_path', type=str, default='final_highlight.mp4', help='Path to save the final highlight video.')
    parser.add_argument('--transcript_path', type=str, default='transcript.json', help='Path to save or load the transcript.')
    parser.add_argument('--important_ids_path', type=str, default='important_ids.json', help='Path to save or load the important segment IDs.')
    parser.add_argument('--chunk_size', type=int, default=20, help='Number of transcript segments to process in each chunk.')
    parser.add_argument('--device', type=str, default='cuda', choices=['cuda', 'cpu'], help='Device to use for transcription (cuda or cpu).')
    
    args = parser.parse_args()

    device = args.device
    if device == 'cuda' and not torch.cuda.is_available():
        print("CUDA not available, switching to CPU.")
        device = 'cpu'

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    # 1. Transcribe video
    if not os.path.exists(args.transcript_path):
        segments = transcribe_video(args.video_path, device=device)
        save_json(segments, args.transcript_path)
    
    # 2. Analyze transcript
    transcript = load_json(args.transcript_path)
    transcript_chunks = [transcript[i:i + args.chunk_size] for i in range(0, len(transcript), args.chunk_size)]
    if not os.path.exists(args.important_ids_path):
        important_ids = get_important_segments(transcript_chunks, args.user_prompt, api_key)
        save_json(important_ids, args.important_ids_path)
    else:
        important_ids = load_json(args.important_ids_path)

    # 3. Process important IDs to get video time cuts
    if not os.path.exists('videos_time_cut.json'):
        process_important_ids()
        
    videos_time_cut = load_json('videos_time_cut.json')
    # 3. Create highlight video
    create_highlight_video(args.video_path, transcript, videos_time_cut, args.output_path)

if __name__ == "__main__":
    main()
