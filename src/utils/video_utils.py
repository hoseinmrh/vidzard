# Utility functions for video processing
import subprocess
import os

def cut_segment(video_path, start_time, end_time, output_path, fmt='mpegts'):
    """Cuts a segment from the video using ffmpeg and saves it to output_path."""
    command = [
        'ffmpeg', '-y', '-ss', str(start_time), '-to', str(end_time),
        '-i', video_path, '-c', 'copy'
    ]
    if fmt == 'mpegts':
        command += ['-f', 'mpegts']
    command.append(output_path)
    subprocess.run(command, check=True, capture_output=True)

def save_individual_clip(video_path, start_time, end_time, output_path):
    """Saves an individual segment as an mp4 file for inspection."""
    command = [
        'ffmpeg', '-y', '-ss', str(start_time), '-to', str(end_time),
        '-i', video_path, '-c', 'copy', output_path
    ]
    subprocess.run(command, check=True, capture_output=True)

def concat_segments(temp_files, output_path):
    """Concatenates .ts files into a single output video using ffmpeg."""
    concat_string = "concat:" + "|".join(temp_files)
    command = [
        'ffmpeg', '-y', '-i', concat_string,
        '-c', 'copy', '-bsf:a', 'aac_adtstoasc', output_path
    ]
    subprocess.run(command, check=True, capture_output=True)
