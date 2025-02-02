from config import base_url, headers
import requests
import json

def get_req() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_req()