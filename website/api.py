import requests
import json

API_URL = 

raw_data = requests.get(API_URL)

parsed_data = json.loads(raw_data.text)

print(parsed_data)

key= AIzaSyAyD6pp0ypm5IwN90yniQ8-Il2CHJgk3H4