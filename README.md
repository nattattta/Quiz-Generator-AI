# Quiz-Generator-AI

An AI-powered application that automatically generates multiple-choice quizzes from various content types including text files, PDFs, audio recordings, and videos.

## Overview

Quiz-Generator-AI utilizes OpenAI's GPT and Whisper models to:
1. Extract content from different file formats
2. Generate relevant multiple-choice questions
3. Present an interactive quiz experience
4. Score user responses in real-time

## Features

- Supports multiple file formats:
  - Text files (.txt)
  - PDF documents (.pdf)
  - Audio files (.mp3)
  - Video files (.mp4)
- Automatic transcription of audio content
- Extraction of audio from video files
- Dynamic quiz generation based on content
- Interactive command-line quiz interface
- Real-time scoring and feedback

## Requirements

- Python 3.7+
- OpenAI API key
- FFmpeg (for audio/video processing)

## Dependencies

- openai: For GPT and Whisper API access
- python-dotenv: For environment variable management
- PyPDF2: For PDF content extraction
- ffmpeg-python: Python wrapper for FFmpeg

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Quiz-Generator-AI.git
   cd Quiz-Generator-AI
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install FFmpeg (required for audio/video processing):
   - On macOS: `brew install ffmpeg`
   - On Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

4. Set up environment variables:
   - Copy the `.env.example` file to `.env`
   - Add your OpenAI API key to the `.env` file

## Usage

Run the main script:
```
python main.py
```

Follow the interactive prompts:
1. Select the file type (Text, PDF, Audio, or Video)
2. Enter the path to your file
3. The system will process the content and generate quiz questions
4. Answer the multiple-choice questions when prompted
5. Get immediate feedback and a final score

## How It Works

1. **Content Extraction**:
   - Text files are read directly
   - PDF content is extracted using PyPDF2
   - Audio is transcribed using OpenAI's Whisper model
   - Video files have audio extracted via FFmpeg and then transcribed

2. **Quiz Generation**:
   - Content is analyzed by OpenAI's GPT model
   - Multiple-choice questions are created based on the content
   - Each question includes 4 options and a correct answer

3. **Quiz Experience**:
   - Questions are presented one by one
   - User inputs their answer choice
   - Immediate feedback is provided
   - Final score is calculated and displayed

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

- If you encounter issues with video or audio processing, ensure FFmpeg is properly installed
- For transcription or quiz generation problems, verify your OpenAI API key is valid and has sufficient credits