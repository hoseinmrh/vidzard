import whisper

def transcribe_video(video_path, model_size="base", device="cuda"):
    """Transcribes a video using Whisper."""
    print(f"Transcribing with Whisper on device: {device}")
    model = whisper.load_model(model_size, device=device)
    result = model.transcribe(video_path, verbose=False)
    return result["segments"]
