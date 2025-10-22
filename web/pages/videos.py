import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent  # web/

st.title("WELCOME TO SWEETY!")
st.title("My video:")

video1_path = BASE_DIR / 'assets' / 'video1.mp4'
video2_path = BASE_DIR / 'assets' / 'video2.mp4'

col1, col2 = st.columns(2)
with col1:
    st.video(str(video1_path))
with col2:
    st.video(str(video2_path))

