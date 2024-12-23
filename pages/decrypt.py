import streamlit as st
from pypdf import PdfReader, PdfWriter

st.set_page_config(
    page_title="Decrypt",
    page_icon="👋",
)

st.write("""
# Decrypt your pdf.""")
st.write("""
Name for your encrypted pdf:""")
name = st.text_input(label='name of pdf', 
                     value="Name your file here", 
                     max_chars=255, 
                     type="default", 
                     placeholder="combined", 
                     disabled=False, 
                     label_visibility="collapsed")
st.write("""
Password for your encrypted pdf:""")
pw = st.text_input(label='password of pdf', 
                     value="Password", 
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
    
    if reader.is_encrypted:
        reader.decrypt(pw)

    writer = PdfWriter(clone_from=reader)

    with open(name, "wb") as f:
        writer.write(f)
    
    with open(name, "rb") as f:
        decryptedfile = f.read()

    st.download_button(label='Download decrypted pdf', 
                   data=decryptedfile, 
                   file_name=file_name,
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)
    writer.close()
else:
    st.write("Upload your files to get started.")
