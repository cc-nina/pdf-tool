import streamlit as st
from pypdf import PdfReader, PdfWriter

st.set_page_config(
    page_title="Decrypt",
    page_icon="👋",
)

st.write("""
# Decrypt your pdf.""")