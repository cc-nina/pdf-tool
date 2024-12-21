import streamlit as st
import pandas as pd
from pypdf import PdfWriter

merger = PdfWriter()

st.write("""
# PDF Combiner""")

st.write("""
Combine your pdfs.""")
uploaded_files = st.file_uploader(label="combine pdfs", type=['pdf'], accept_multiple_files=True, key=None, disabled=False, label_visibility="collapsed")
st.write("""
Name of your combined pdf:""")
name = st.text_input(label='name of pdf', 
                     value="combined", 
                     max_chars=255, 
                     type="default", 
                     placeholder='combined', 
                     disabled=False, 
                     label_visibility="collapsed")

name = name+".pdf"
for file in uploaded_files:
    merger.append(file)
    
merger.write(name)

st.download_button(label='download combined pdf', 
                   data=name, 
                   file_name=name, 
                   mime=None, 
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)

merger.close()
