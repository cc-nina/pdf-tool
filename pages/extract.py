import streamlit as st
from pypdf import PdfReader, PdfWriter
import PyPDF2

st.set_page_config(
    page_title="Extract Text",
    page_icon="👋",
)

st.write("""
# Extract text from your pdfs.""")

uploaded_file = st.file_uploader(label="combine pdfs", 
                                  type=['pdf'], 
                                  accept_multiple_files=False, 
                                  key=None, 
                                  disabled=False, 
                                  label_visibility="collapsed")

if uploaded_file:
    pdfReader = PyPDF2.PdfReader(uploaded_file)
    total = len(pdfReader.pages)

    st.write("""
    Pages to extract text from:""")
    first = st.number_input(label='This page', 
                        min_value=1, 
                        max_value=total, 
                        value=1, 
                        step=1, 
                        placeholder=None, 
                        disabled=False, 
                        label_visibility="visible")

    last = st.number_input(label='To this page', 
                        min_value=first, 
                        max_value=total, 
                        value=first, 
                        step=1, 
                        placeholder=None, 
                        disabled=False, 
                        label_visibility="visible")
    
    reader = PdfReader(uploaded_file)
    

    # do a single loop, check if in the range of changing things
    for i in range(total):
        if i in range((first - 1), last):
            page = reader.pages[i]
            st.write(page.extract_text())
        else:
            st.write("""""")

else:
    st.write("Upload a file to get started.")

