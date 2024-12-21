import streamlit as st
import pandas as pd

st.write("""
# PDF Combiner""")

st.write("""
Combine your pdfs.""")
uploaded_files = st.file_uploader(label="combine pdfs", type=['pdf'], accept_multiple_files=True, key=None, disabled=False, label_visibility="collapsed")
