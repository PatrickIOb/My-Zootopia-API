import json
import requests
import os
from dotenv import load_dotenv

#load the API_KEY
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    res = requests.get("https://api.api-ninjas.com/v1/animals", headers={"x-api-key": API_KEY}, params={"name": animal_name})
    return res.json()
