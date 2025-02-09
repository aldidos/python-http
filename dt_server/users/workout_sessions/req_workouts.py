import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

def get_workouts() : 
    user_id = 1
    workout_session_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions/{workout_session_id}/workouts'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get_workout() : 
    user_id = 1
    workout_session_id = 1
    workout_id = 1
    uri = f'{base_url}/users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

