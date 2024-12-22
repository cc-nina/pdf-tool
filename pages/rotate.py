import streamlit as st
from pypdf import PdfReader, PdfWriter
import PyPDF2

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

uploaded_file = st.file_uploader(label="combine pdfs", 
                                  type=['pdf'], 
                                  accept_multiple_files=False, 
                                  key=None, 
                                  disabled=False, 
                                  label_visibility="collapsed")

if uploaded_file:
    name = name+".pdf"
    file_name = name
    # not working
    # page_count = len(uploaded_file.pages)

    # after downloading pypdf2
    pdfReader = PyPDF2.PdfReader(uploaded_file)
    total = len(pdfReader.pages)

    st.write("""
    Pages to rotate:""")
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
    
    amnt = st.number_input(label='How many times clockwise', 
                        min_value=0, 
                        value=first, 
                        step=1, 
                        placeholder=None, 
                        disabled=False, 
                        label_visibility="visible")
    amnt = amnt % 4
    amnt = amnt * 90
    
    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    # do a single loop, check if in the range of changing things
    for i in range(total):
        if i in range((first - 1), last):
            writer.add_page(reader.pages[i])
            writer.pages[i].rotate(amnt)
        else:
            writer.add_page(reader.pages[i])


    #if first == last:
  #      writer.add_page(reader.pages[(first - 1)])
        # index error here
    #    writer.pages[0].rotate(amnt)
 #   else:
    #    for i in range((first - 1), last):
    #        writer.add_page(reader.pages[i])
    #        writer.pages[i].rotate(amnt)
        
    #if last != total:
#for i in range(last, total):
    #        writer.add_page(reader.pages[i])
    #need to add in pages that aren't specified
    with open(name, "wb") as fp:
        writer.write(fp)
    
    with open(name, "rb") as pdf_file:
        rotatedfile = pdf_file.read()

    st.download_button(label='Download rotated pdf', 
                   data=rotatedfile, 
                   file_name=file_name,
                   type="secondary", 
                   icon=":material/download:", 
                   disabled=False, 
                   use_container_width=False)
    writer.close()
else:
    st.write("Upload your files")

