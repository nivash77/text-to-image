import requests
import streamlit as str
import streamlit.components.v1 as components

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

str.title("IMAGE GENERATE")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": str.text_input("Enter a text"),
})

import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if str.button('Generate'):
	str.image(image)