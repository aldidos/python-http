from config import base_url, headers
import requests
import json

user_id = 1

def get_recent(user_id) : 
    uri = f'{base_url}/users/{user_id}/workout_summary/recent'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get(user_id, from_date, to_date) : 
    uri = f'{base_url}/users/{user_id}/workout_summary'

    params = {'from_date' : from_date, 'to_date' : to_date}

    res = requests.get(uri, params = params, headers = headers)
    print(res.status_code)
    print(res.text)

get_recent(user_id)

from_date = '2025-02-01'
to_date = '2025-02-08'

get(user_id, from_date, to_date)