import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai
import streamlit as st
import PyPDF2
from main import summarize
import time
import streamlit as st

with st.form('Gemini Paper Summarizer'):
    st.header("Gemini Summarizer")
    uploaded_file = st.file_uploader('', type='pdf')

    col1, col2 = st.columns(2)

    with col1:
        if uploaded_file is not None:
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                text_content = ""
            
        for page in pdf_reader.pages:
                text_content += page.extract_text()
            
            if text_content.strip():
                with col2:
                    response = summarize(text_content)
                    st.write("DONE!")
                    summarized_text = (response.text)
                    st.write(summarized_text)
                        
        
