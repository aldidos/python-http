from config import base_url, headers
import requests
import json

def get_req() : 
    center_id = 1
    uri = f'{base_url}/centers/{center_id}/equipments'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_req()