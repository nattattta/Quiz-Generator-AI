import os
from dotenv import load_dotenv
import openai
import PyPDF2
import subprocess

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf_file(file_path):
    reader = PyPDF2.PdfReader(file_path)
    return "\n".join([page.extract_text() or "" for page in reader.pages])

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def extract_audio_from_video(video_path, audio_path="temp_audio.mp3"):
    cmd = f'ffmpeg -y -i "{video_path}" -q:a 0 -map a "{audio_path}"'
    try:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL  # suppress all output
        )
    except subprocess.CalledProcessError as e:
        print("❌ Error: FFmpeg failed to extract audio.")
        print(f"Details: {e}")
        return None
    except FileNotFoundError:
        print("❌ FFmpeg is not installed or not found in PATH.")
        return None
    return audio_path