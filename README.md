# Vidzard-Core: AI-Powered Video Highlight Generator

This project is a Python-based solution for automatically generating highlight reels from video content. It leverages AI to transcribe and analyze video transcripts, identify the most significant moments, and then programmatically edits the video to create a final highlight clip.

## Features

- **YouTube Video Downloader**: Downloads videos from YouTube for processing. (Handled externally, `video.mp4` is the expected input)
- **Video Transcription**: Uses OpenAI's Whisper model to generate accurate, timestamped transcripts.
- **AI-Powered Analysis**: Employs the Gemini API to analyze the transcript and select the most important segments based on a user-provided prompt.
- **Automated Video Editing**: Uses `ffmpeg` to cut and concatenate the selected video segments into a seamless highlight video.
- **Modular & Extensible**: The code is organized into a modular structure, making it easy to extend and customize.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd vidzard-core
    ```

2.  **Create and activate a Python environment.** It is recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    Or using conda:
    ```bash
    conda create -n vidzard python=3.10
    conda activate vidzard
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API key:**
    - Create a `.env` file in the project root.
    - Add your Gemini API key to the `.env` file:
      ```
      GEMINI_API_KEY="your_api_key_here"
      ```

5.  **Place your video file:**
    - Place the video you want to process in the project root and name it `video.mp4`, or use the `--video_path` argument to specify a different location.

## Usage

You can run the entire pipeline using the `main.py` script.

### Basic Usage

To run the highlight generation with default settings, simply run:

```bash
python main.py
```

### Command-Line Arguments

You can customize the behavior of the script using command-line arguments:

-   `--video_path`: Path to the input video file (default: `video.mp4`).
-   `--user_prompt`: The prompt to guide the AI in selecting important segments (default: "This is an interview about an urban project. Identify the most important segments.").
-   `--output_path`: Path to save the final highlight video (default: `final_highlight.mp4`).
-   `--transcript_path`: Path to save or load the transcript JSON file (default: `transcript.json`).
-   `--important_ids_path`: Path to save or load the important segment IDs JSON file (default: `important_ids.json`).
-   `--chunk_size`: The number of transcript segments to process in each API call (default: 20).

### Example

```bash
python main.py --video_path my_interview.mp4 --user_prompt "Find the key moments where the guest discusses their childhood." --output_path childhood_highlights.mp4
```

## Project Structure

```
vidzard-core/
├── .env                  # For API keys and environment variables
├── .gitignore            # Git ignore file
├── main.py               # Main script to run the full pipeline
├── requirements.txt      # Project dependencies
├── scripts/
│   └── video_cutter.py   # Standalone script for video cutting (can be adapted)
└── src/
    └── vidzard/
        ├── __init__.py
        ├── analysis/
        │   ├── __init__.py
        │   ├── analyzer.py       # Handles transcript analysis with Gemini
        │   └── transcriber.py    # Handles video transcription with Whisper
        ├── data/
        │   ├── __init__.py
        │   └── data_handler.py   # Utility functions for data handling (JSON, etc.)
        └── video/
            ├── __init__.py
            ├── composer.py       # Composes the final video from clips
            └── editor.py         # Handles video editing tasks (cutting, etc.)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
