import streamlit as st
import os

# Title
st.title("🎧 Audio Podcasts")

# Path to your audio folder
AUDIO_FOLDER = "audio_files"

# Get list of audio files
audio_files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith((".mp3", ".wav", ".ogg", ".mpeg", ".m4a"))]

# Dropdown to select audio file
selected_file = st.selectbox("Select an audio file to play:", audio_files)

if selected_file:
    file_path = os.path.join(AUDIO_FOLDER, selected_file)
    st.audio(file_path)
