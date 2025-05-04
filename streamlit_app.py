import streamlit as st
import os
from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunk_summary
from main import video_to_summary  # Import the video summarization logic

# Make sure ffmpeg is installed and accessible
def check_ffmpeg():
    try:
        # Check if ffmpeg is available by running `ffmpeg -version`
        os.system("ffmpeg -version")
    except Exception as e:
        st.error("❌ Error: ffmpeg is not installed or not found. Please install ffmpeg and ensure it's in your PATH.")
        raise e

# Streamlit UI
st.title("🎬 Video Summarizer App")
st.write("Upload a video and get a summary of its spoken content!")

uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if uploaded_video:
    # Check if ffmpeg is installed before processing
    try:
        check_ffmpeg()  # Verify that ffmpeg is available
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()  # Stop the app if ffmpeg is not found

    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.info("Processing video... this may take some time ⏳")

    try:
        # Use the imported video_to_summary function here
        summary = video_to_summary(
            video_path,
            model_size="base",
            summarizer_model_name="facebook/bart-large-cnn",
            use_chunking=True  # Set to False if you don’t want chunking
        )
        st.success("Summary generated!")
        st.text_area("📝 Summary", summary, height=300)
        os.remove(video_path)
    except Exception as e:
        st.error(f"❌ Error: {e}")
