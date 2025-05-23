# Azure Computer Vision Caption Generator

This is a simple web application that generates image captions using the **Azure Computer Vision API**.  
Users can provide an image URL, and the app returns a natural language caption describing the image.

---

## Features

- Input image via URL
- Get descriptive captions with confidence scores
- Simple, clean interface using **Streamlit**
- Backend API using **FastAPI** to interact with Azure Computer Vision service

---

## Architecture

User (Streamlit frontend)
↓
FastAPI backend (handles API requests)
↓
Azure Computer Vision API (image captioning)
