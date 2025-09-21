import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent  # web/

st.title("WELCOME TO SWEETY!")
st.title("My video:")


video_path = BASE_DIR / "assets" / "sunset.MP4"

col1, col2, col3 = st.columns(3)
with col1:
    st.video(str(video_path))
with col2:
    st.video(str(video_path))
with col3:
    st.video(str(video_path))
