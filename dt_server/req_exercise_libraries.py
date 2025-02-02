from config import base_url, headers
import requests
import json

def get_req() : 
    uri = f'{base_url}/exercise_libraries'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_req()