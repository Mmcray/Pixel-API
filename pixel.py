from dotenv import load_dotenv
from os import getenv
import fastapi
import uvicorn
import requests



def pixel(x,y,rgb):
    
    load_dotenv("pixel.env")
    
    token = getenv("TOKEN")

    HEADERS = {
        "Authorization":  f"Bearer {token}"
        }

    data = {
        "x":  x,
        "y":  y,
        "rgb":  rgb
        }

    result = requests.post(
        "https://pixels.pythondiscord.com/set_pixel",
        json=data,
        headers=HEADERS
        )

    print(result.json()["message"])
        
