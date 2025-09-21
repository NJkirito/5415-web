import streamlit as st

st.title("WELCOME TO SWEETY!")

st.title("My video:")

col1, col2, col3 = st.columns(3)
with col1:
    st.video("assets/sunset.MP4")
with col2:
    st.video("assets/sunset.MP4")
with col3:
    st.video("assets/sunset.MP4")