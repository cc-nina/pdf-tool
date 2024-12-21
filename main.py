import streamlit as st
import pandas as pd
 
st.write("""
# PDF Combiner""")
st.write("""
# PDF Combiner""")

st.file_uploader(label="pdf", type=['pdf'], accept_multiple_files=True, key=None, disabled=False, label_visibility="visible")
