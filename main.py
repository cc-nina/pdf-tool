import streamlit as st
import pandas as pd
from pypdf import PdfWriter
import os

def removefromdir():
    for i in os.listdir('/'):
        if i.endswith('.pdf'):
            os.remove(i)

merger = PdfWriter()

st.write("""
# PDF Combiner""")

st.write("""
Combine your pdfs.""")
uploaded_files = st.file_uploader(label="combine pdfs", type=['pdf'], accept_multiple_files=True, key=None, disabled=False, label_visibility="collapsed")
st.write("""
Name of your combined pdf:""")
name = st.text_input(label='name of pdf', 
                     value="bobb", 
                     max_chars=255, 
                     type="default", 
                     placeholder="combined", 
                     disabled=False, 
                     label_visibility="collapsed")
name = name+".pdf"
file_name = name

for file in uploaded_files:
    merger.append(file)
    
merger.write(name)

with open(name, "rb") as pdf_file:
    combinedfile = pdf_file.read()

st.download_button(label='download combined pdf', 
                   data=combinedfile, 
                   file_name=file_name,
                   on_click=removefromdir(),
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)

merger.close()
