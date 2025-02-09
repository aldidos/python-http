import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

def get_recent() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions/recent'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions'

    from_date = '2025-01-01'
    to_date = '2025-03-01'
    date = '2025-02-04'
    params = { 'from_date' : from_date, 'to_date' : to_date, 'search_date' : 'period' }
    params = { 'date' : date }

    res = requests.get(uri, params=params,  headers = headers)
    print(res.status_code)
    print(res.text)

def get_one() : 
    user_id = 1
    workout_session_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions/{workout_session_id}'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def post() : 
    user_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions'

    res = requests.post(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_recent()
get()
get_one()
