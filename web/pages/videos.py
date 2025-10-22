import streamlit as st
from pathlib import Path

# 获取 videos.py 所在目录
BASE_DIR = Path(__file__).parent.parent  # web/

st.title("WELCOME TO SWEETY!")
st.title("My video:")

# 视频文件路径
video1_path = BASE_DIR / "assets" / "video1.MP4"
video2_path = BASE_DIR / "assets" / "video2.MP4"

col1, col2 = st.columns(2)
with col1:
    st.video(str(video1_path))
with col2:
    st.video(str(video2_path))

