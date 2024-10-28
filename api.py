# backend.py
import os
from typing import Dict
from fastapi import FastAPI, UploadFile, File
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = os.getenv("API_URL")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

app = FastAPI()


def query_image(image_data: bytes) -> Dict:
    """
    Sends an image file (in bytes) to the Hugging Face BLIP model API 
    for caption generation.

    Args:
    - image_data (bytes): The image file content in byte format.

    Returns:
    - Dict: The JSON response from the Hugging Face API, containing thecaption.
    """
    
    response = requests.post(
        API_URL, 
        headers=headers, 
        data=image_data,    
        timeout=20
    )
    
    return response.json()


@app.post("/caption/")
async def get_caption(file: UploadFile = File(...)):
    """
    Receives an image upload from the client, reads the content, 
    and sends it to the Hugging Face API for caption generation.

    Args:
    - file (UploadFile): The uploaded image file from the client.

    Returns:
    - JSON response with the generated caption.
    """

    image_data = await file.read()
    caption_response = query_image(image_data)
    return caption_response
#uvicorn api:app --host 0.0.0.0 --port 8000