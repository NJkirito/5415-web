from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent  

st.set_page_config(page_title="SWEETY", page_icon="🍰", layout="wide")

pages = ['pages/images.py', 'pages/videos.py']
pg = st.navigation(pages)
pg.run()

with st.sidebar:
    logo_path = BASE_DIR / 'assets' / 'logo.png'
    st.image(str(logo_path))
