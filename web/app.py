import io
from pathlib import Path
import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="SWEETY", page_icon="🍰", layout="wide")

pages=['pages/images.py', 'pages/videos.py']
pg=st.navigation(pages)
pg.run()

with st.sidebar:
    st.image('assets/logo.png')



