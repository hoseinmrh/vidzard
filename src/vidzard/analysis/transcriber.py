import whisper

def transcribe_video(video_path, model_size="base"):
    """Transcribes a video using Whisper."""
    model = whisper.load_model(model_size)
    result = model.transcribe(video_path, verbose=False)
    return result["segments"]
