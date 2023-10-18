import streamlit as st
import requests

# prepare API key and API url
api_key = ("HzORnbY4yEtkpGLiS9g2edxEODi5pgqLgvA4dDtF")
url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

# get the request data as a dictionary
data_response = requests.get(url)
data = data_response.json()

# extract the image title, url, and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# download the image
image_filepath = "img.png"
image_response = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(image_response.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)