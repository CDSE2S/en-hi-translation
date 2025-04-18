import streamlit as st
import requests

API_URL = "http://localhost:8000/translate/"

st.title("English to Hindi Translator")
text = st.text_area("Enter English text:")

if st.button("Translate"):
    response = requests.get(API_URL, params={"text": text})
    translation = response.json().get("translated_text", "Error in translation.")
    st.write("**Hindi Translation:**", translation)