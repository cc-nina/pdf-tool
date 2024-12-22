import streamlit as st
from pypdf import PdfWriter

st.set_page_config(
    page_title="Combine",
    page_icon="👋",
)

merger = PdfWriter()

st.write("""
# Combine your pdfs.""")
st.write("""
Name for your combined pdf:""")
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

if uploaded_files:
    name = name+".pdf"
    file_name = name

    for file in uploaded_files:
        merger.append(file)
        
    merger.write(name)

    with open(name, "rb") as pdf_file:
        combinedfile = pdf_file.read()
    st.download_button(label='Download combined pdf', 
                   data=combinedfile, 
                   file_name=file_name,
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)
else:
    st.write("Upload your files")

merger.close()
