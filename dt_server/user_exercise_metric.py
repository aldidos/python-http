from config import base_url, headers
import requests
import json

data = {    
    'user_id' : 1, 
    'exercise_library_id' : 1,
    'weight' : 75.0 
}

def post_req(data) : 
    user_id = 1
    exercise_lib_id = 1
    uri = f'{base_url}/users/{user_id}/weight_metric/{exercise_lib_id}>'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_req() : 
    user_id = 1
    exercise_lib_id = 1
    uri = f'{base_url}/users/{user_id}/weight_metric/{exercise_lib_id}>'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def patch_req(data) : 
    user_id = 1
    exercise_lib_id = 1
    uri = f'{base_url}/users/{user_id}/weight_metric/{exercise_lib_id}>'

    data['weight'] = 85.5   

    data = json.dumps(data)
    res = requests.get(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

post_req(data)
get_req()
patch_req(data)