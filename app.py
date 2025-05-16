import streamlit as st
import requests

AZURE_ENDPOINT = st.secrets["AZURE_ENDPOINT"]
AZURE_KEY = st.secrets["AZURE_KEY"]

def analyze_image_url(image_url):
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/json"
    }
    data = {"url": image_url}
    response = requests.post(AZURE_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def analyze_image_bytes(image_bytes):
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(AZURE_ENDPOINT, headers=headers, data=image_bytes)
    response.raise_for_status()
    return response.json()

# Streamlit UI
st.set_page_config(page_title="Image Caption Generator", page_icon="🧠")
st.title("🧠 Image Caption Generator")
st.write("Upload an image or enter a URL to get a caption.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_url = st.text_input("Or enter an image URL:")

image_data = None
source = None

if uploaded_file:
    image_data = uploaded_file.read()
    st.image(image_data, caption="Uploaded Image", use_column_width=True)
    source = "file"

elif image_url:
    st.image(image_url, caption="Image from URL", use_column_width=True)
    source = "url"

if st.button("Generate Caption"):
    if not (image_data or image_url):
        st.warning("Please upload an image or enter a valid URL.")
    else:
        with st.spinner("Analyzing..."):
            try:
                if source == "file":
                    result = analyze_image_bytes(image_data)
                else:
                    result = analyze_image_url(image_url)

                captions = result.get("description", {}).get("captions", [])
                if captions:
                    caption = captions[0]["text"]
                    confidence = captions[0]["confidence"]
                    st.success(f"Caption: {caption}")
                    st.info(f"Confidence: {round(confidence * 100, 2)}%")
                else:
                    st.warning("No caption found.")
            except Exception as e:
                st.error(f"Error: {e}")
