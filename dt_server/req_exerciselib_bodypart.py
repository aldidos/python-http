import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

def get_req() : 
    uri = f'{base_url}/exerciselib_bodyparts'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get_one() : 
    exerciselib_id = 1
    body_part_id = 4
    uri = f'{base_url}/exerciselib_bodyparts/{exerciselib_id}/{body_part_id}'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_req()