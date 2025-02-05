from config import base_url, headers
import requests
import json

user_id = [1,2,3]
workout_session_id = [1,2,3]
workout_id = [1,2,3]

data = {    
    'workout_metrics' : [
        {
            'set' : 1, 
            'rep' : 1, 
            'weight' : 1, 
            'volume' : 1, 
            'peak_velocity' : 11, 
            'mean_velocity' : 1, 
            'peak_power' : 1, 
            'mean_power' : 1, 
            'height' : 1, 
            'power' : 1, 
            'created_at' : '2025-02-04 10:18:00',
        },
        {
            'set' : 1, 
            'rep' : 2, 
            'weight' : 1, 
            'volume' : 1, 
            'peak_velocity' : 12, 
            'mean_velocity' : 1, 
            'peak_power' : 1, 
            'mean_power' : 1, 
            'height' : 1, 
            'power' : 1, 
            'created_at' : '2025-02-04 10:18:00',
        },
        {
            'set' : 1, 
            'rep' : 3, 
            'weight' : 1, 
            'volume' : 1, 
            'peak_velocity' : 50, 
            'mean_velocity' : 1, 
            'peak_power' : 1, 
            'mean_power' : 1, 
            'height' : 1, 
            'power' : 1, 
            'created_at' : '2025-02-04 10:18:00', 
        }
        ]
}

def post_req(user_id, workout_session_id, workout_id, data) : 
    uri = f'{base_url}//users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}/workout_metrics'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

post_req(user_id[0], workout_session_id[0], workout_id[0], data)
post_req(user_id[1], workout_session_id[1], workout_id[1], data)
post_req(user_id[2], workout_session_id[2], workout_id[2], data)