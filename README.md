# Video Summarizer App

This Streamlit app allows you to upload a video, extract the audio using FFmpeg, transcribe the speech to text using OpenAI's Whisper model, and generate a summary using a BART-based transformer from Hugging Face.

---

##  Features

-  **Audio Extraction** from uploaded videos using FFmpeg
-  **Speech Transcription** using OpenAI's Whisper model
-  **Text Summarization** using the BART model (`facebook/bart-large-cnn`)
-  **Interactive Streamlit Web App** for easy use

---

##  Installation Instructions (Local Deployment)

Follow these steps to run the app on your local machine.

---

###  1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/sujaya1025/video_summarizer.git
cd video_summarizer
```
###  2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate

```

### 3. Install Python Dependencies
 ```bash
pip install -r requirements.txt

```
### 4. Install `ffmpeg`:

- **Windows**: Download `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html), extract it, and add the `bin` folder to your system's PATH.
- **macOS**: Use Homebrew to install `ffmpeg`:
  ```bash
  brew install ffmpeg
  ```
- **Linux**: Use your package manager to install `ffmpeg`:
  ```bash
  sudo apt install ffmpeg
  ```
  ### 5. Run the Streamlit App
   Start the app with the following command:

```bash
streamlit run streamlit_app.py
```

## How to use?
- **Upload a video file:** Choose a video file (e.g., .mp4 or .mov) from your local machine.
- **Generate Summary:** Click "Generate Summary"
- The summary will be displayed below the button.
  
