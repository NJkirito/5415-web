from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent.parent  # web/

st.title("WELCOME TO SWEETY!")

st.title("My banner:")
st.image(str(BASE_DIR / 'assets' / 'banner.png'))

st.title("My poster:")
st.image(str(BASE_DIR / 'assets' / 'poster.png'))
