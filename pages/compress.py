import streamlit as st
from pypdf import PdfReader, PdfWriter
from PyPDF2 import PdfReader, PdfWriter

st.set_page_config(
    page_title="Compress",
    page_icon="👋",
)

st.write("""
# Compress your pdf.""")
st.write("""
Name for your combined pdf:""")
name = st.text_input(label='name of pdf', 
                     value="Name your file here", 
                     max_chars=255, 
                     type="default", 
                     placeholder="combined", 
                     disabled=False, 
                     label_visibility="collapsed")
uploaded_file = st.file_uploader(label="compress pdfs", 
                                  type=['pdf'], 
                                  accept_multiple_files=False, 
                                  key=None, 
                                  disabled=False, 
                                  label_visibility="collapsed")

if uploaded_file:
    name = name+".pdf"
    file_name = name

    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)

    with open(name, "wb") as f:
        writer.write(f)

    with open(name, "rb") as pdf_file:
        compressedfile = pdf_file.read()

    st.download_button(label='Download compressed pdf', 
                   data=compressedfile, 
                   file_name=file_name,
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)
else:
    st.write("Upload your files to get started.")

