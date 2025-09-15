# app.py
import streamlit as st
from notebook import predict_url   # function from notebook.py

st.title("Phishing URL Detector")

url = st.text_input("Enter a URL:")
if url:
    result = predict_url(url)
    st.success(f"Prediction: {result}")
