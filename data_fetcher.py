import json
import requests
import animals_web_generator

API_KEY = "I/qKGCs0oxX2XFwmfBo46A==whYupgYwUBaeWAdy"

def fetch_data(animal_name):
    res = requests.get("https://api.api-ninjas.com/v1/animals", headers={"x-api-key": API_KEY}, params={"name": animal_name})
    return res.json()
