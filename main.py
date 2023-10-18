import streamlit as st
import requests

api_key = ("HzORnbY4yEtkpGLiS9g2edxEODi5pgqLgvA4dDtF")
url = ("https://api.nasa.gov/planetary/apod"
       f"{api_key}")

request = requests.get(url)

content = request.json()

body = ("")
for picture in content:
    body = picture["image"]
    print(body)