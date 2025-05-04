import streamlit as st
import os
from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunk_summary

def video_to_summary(video_path):
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)
    transcript = transcribe_audio(audio_path, model_size="base")
    summary = chunk_summary(
        transcript,
        summarize_func=lambda txt: summarize_text(txt, model_name="facebook/bart-large-cnn"),
        max_chunk_size=2000
    )
    os.remove(audio_path)
    return summary

st.title("🎬 Video Summarizer App")
st.write("Upload a video and get a summary of its spoken content!")

uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if uploaded_video:
    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.info("Processing video... this may take some time ⏳")

    try:
        summary = video_to_summary(video_path)
        st.success("Summary generated!")
        st.text_area("📝 Summary", summary, height=300)
        os.remove(video_path)
    except Exception as e:
        st.error(f"❌ Error: {e}")
