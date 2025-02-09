import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

data = {    
    'user_id' : 1, 
    'workout_goal' : 'training',    
}

def post_req(data) : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}/survey'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_req() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}/survey'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

post_req(data)
get_req()