import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("🧠 Image Caption Generator using Azure Computer Vision")

image_url = st.text_input("Enter image URL:")

if image_url:
    st.image(image_url, caption="Input Image", use_container_width =True)
    if st.button("Generate Caption"):
        res = requests.post(f"{BACKEND_URL}/caption_from_url", data={"image_url": image_url})
        if res.status_code == 200:
            data = res.json()
            caption = data.get("description", {}).get("captions", [{}])[0].get("text", "No caption found")
            confidence = data.get("description", {}).get("captions", [{}])[0].get("confidence", None)
            st.success(f"Caption: {caption}")
            if confidence is not None:
                st.info(f"Confidence: {round(confidence * 100, 2)}%")
        else:
            st.error("Failed to generate caption. Check the image URL and try again.")
