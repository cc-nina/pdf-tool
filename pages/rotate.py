import streamlit as st
from pypdf import PdfReader, PdfWriter

st.set_page_config(
    page_title="Rotate",
    page_icon="👋",
)

st.write("""
# Rotate your pdfs.""")
st.write("""
Name for your rotated pdf:""")
name = st.text_input(label='name of pdf', 
                     value="Name your file here", 
                     max_chars=255, 
                     type="default", 
                     placeholder="combined", 
                     disabled=False, 
                     label_visibility="collapsed")

uploaded_files = st.file_uploader(label="combine pdfs", 
                                  type=['pdf'], 
                                  accept_multiple_files=True, 
                                  key=None, disabled=False, 
                                  label_visibility="collapsed")

st.write("""
Pages to rotate:""")
first = st.number_input(label='First page', 
                      min_value=None, 
                      max_value=None, 
                      value="min", 
                      step=None, 
                      format=None, 
                      key=None, 
                      help=None, 
                      on_change=None, 
                      args=None, 
                      kwargs=None, 
                      placeholder=None, 
                      disabled=False, 
                      label_visibility="visible")

last = st.number_input(label='Last page', 
                      min_value=None, 
                      max_value=None, 
                      value="min", 
                      step=None, 
                      format=None, 
                      key=None, 
                      help=None, 
                      on_change=None, 
                      args=None, 
                      kwargs=None, 
                      placeholder=None, 
                      disabled=False, 
                      label_visibility="visible")