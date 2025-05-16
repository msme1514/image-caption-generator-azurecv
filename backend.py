from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()  # Load variables from .env

## for local enviroment
# AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
# AZURE_KEY = os.getenv("AZURE_KEY")

## for production enviroment
AZURE_ENDPOINT = st.secrets["AZURE_ENDPOINT"]
AZURE_KEY = st.secrets["AZURE_KEY"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/caption_from_url")
def caption_from_url(image_url: str = Form(...)):
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/json"
    }
    data = {"url": image_url}
    response = requests.post(AZURE_ENDPOINT, headers=headers, json=data)
    return response.json()
