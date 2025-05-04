#  Video Summarizer

This Streamlit app allows you to upload a video file, extract the audio, transcribe the audio using OpenAI's Whisper model, and generate a concise summary using a transformer-based model (BART).

---

##  Features

- **Audio Extraction**: Extracts audio from uploaded video using FFmpeg.
- **Speech-to-Text Transcription**: Uses Whisper model (via `openai-whisper`) for accurate transcription.
- **Text Summarization**: Uses Hugging Face's `facebook/bart-large-cnn` model to generate a readable summary of the video content.
- **Streamlit Interface**: Interactive, clean UI for easy use.

---



Follow these steps to run the project locally on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/sujaya1025/video_summarizer.git
cd video_summarizer

### 2. Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

### 3. Install Python Dependencies
 pip install -r requirements.txt

### 4. Install FFmpeg (Required)
Windows:

Download from https://ffmpeg.org/download.html

Extract the ZIP file.

Add the bin folder path (e.g., C:\ffmpeg\bin) to your system's PATH.

Open a new terminal and run: ffmpeg -version

 ### Run the App
To start the Streamlit app, run:
 streamlit run streamlit_app.py

Then open your browser and go to:
http://localhost:8501
