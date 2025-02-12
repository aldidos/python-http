import sys
sys.path.append('.')

from dt_server.config import base_url, headers, data_to_json
import requests
import json

data = {
    'name' : '김정일'    
}

def post_users(data) : 
    uri = f'{base_url}/users'

    data = data_to_json(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)


def get_req() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_req()
# post_users(data)