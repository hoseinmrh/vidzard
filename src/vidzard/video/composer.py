import os
from src.vidzard.video.editor import cut_segment, save_individual_clip, concat_segments

def create_highlight_video(video_path, transcript, videos_time_cut, output_path):
    """Creates a highlight video from specified segments."""
    temp_files = []
    clips_folder = "individual_clips"
    os.makedirs(clips_folder, exist_ok=True)

    try:
        for i, segment in enumerate(videos_time_cut):

            start_time = max(0, segment['start'] - 0.2)
            end_time = segment['end'] + 0.2
            temp_output_path_ts = f"temp_{i}.ts"
            temp_files.append(temp_output_path_ts)
            cut_segment(video_path, start_time, end_time, temp_output_path_ts, fmt='mpegts')

            individual_clip_path = os.path.join(clips_folder, f"clip_{i}.mp4")
            save_individual_clip(video_path, start_time, end_time, individual_clip_path)

        if temp_files:
            concat_segments(temp_files, output_path)
            print(f"Highlight video saved to {output_path}")
            print(f"Individual clips saved in '{clips_folder}/' folder.")
        else:
            print("No segments found to create a highlight video.")

    finally:
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)
