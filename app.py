"Streamlit" 
import streamlit as st
import requests
from PIL import Image

# FastAPI backend URL
FASTAPI_URL = "http://localhost:8000/caption/"

st.title("Image Captioning with BLIP")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...",
                                  type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Send image to FastAPI backend
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(FASTAPI_URL, files=files, timeout=20)

    # Display the caption
    if response.status_code == 200:
        caption = response.json()
        st.write("Generated Caption:", caption)
    else:
        st.write("Error:", response.text)
#Streamlit run app.py 