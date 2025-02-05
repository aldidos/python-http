from config import base_url, headers
import requests
import json

user_id = 3

def get_req(user_id) : 
    uri = f'{base_url}/users/{user_id}/workout_report/recent'

    params = {'perspective' : 'body_part'}

    res = requests.get(uri, params = params, headers = headers)
    print(res.status_code)
    print(res.text)

get_req(user_id)