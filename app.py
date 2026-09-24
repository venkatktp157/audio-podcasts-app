import os
import streamlit as st

st.set_page_config(layout="wide")  # Gives more screen space for side-by-side view
st.title("🎙️ Media Podcasts")

AUDIO_FOLDER = "audio_files"

audio_extensions = (".mp3", ".wav", ".ogg", ".mpeg", ".m4a")
video_extensions = (".mp4", ".mov", ".avi", ".mkv")

all_files = os.listdir(AUDIO_FOLDER)
audio_files = [f for f in all_files if f.lower().endswith(audio_extensions)]
video_files = [f for f in all_files if f.lower().endswith(video_extensions)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎧 Audio Section")
    if audio_files:
        selected_audio = st.selectbox("Select Audio:", audio_files, key="audio_select")
        st.audio(os.path.join(AUDIO_FOLDER, selected_audio))
    else:
        st.info("No audio files found.")

with col2:
    st.subheader("🎬 Video Section")
    if video_files:
        selected_video = st.selectbox("Select Video:", video_files, key="video_select")
        st.video(os.path.join(AUDIO_FOLDER, selected_video))
    else:
        st.info("No video files found.")