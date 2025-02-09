import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

user_id = 1

def get_recent(user_id) : 
    uri = f'{base_url}/users/{user_id}/workout_sessions/reports/recent'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get(user_id) : 
    uri = f'{base_url}/users/{user_id}/workout_sessions/reports'

    # params = {'search_date' : 'period', 'from_date' : '2025-01-01', 'to_date' : '2025-03-01'}
    params = {'search_date' : 'date', 'date' : '2025-02-03'}

    res = requests.get(uri, params = params, headers = headers)
    print(res.status_code)
    print(res.text)

def get_by_wo_sessions_id(user_id) : 
    workout_session_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions/{workout_session_id}/report'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

get_by_wo_sessions_id(user_id)