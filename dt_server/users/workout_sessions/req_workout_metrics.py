import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

user_id = [1,2,3]
workout_session_id = [1,2,3]
workout_id = [1,2,3]
sets = [1,2,3]
reps = [1,2,3,4,5]

def post_req(user_id, workout_session_id, workout_id, sets, reps) : 
    uri = f'{base_url}//users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}/workout_metrics'

    data = make_data(workout_id, sets, reps)

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def make_data(workout_id, sets, reps) : 
    list_data = []    
    
    for set in sets : 
        for rep in reps : 
            data = {
                'workout' : workout_id,
                'set' : set,
                'rep' : rep,
                'weight' : 10, 
                'peak_velocity_con' : 1.2, 
                'mean_velocity_con' : 0.6, 
                'peak_power_con' : 2.2, 
                'mean_power_con' : 1.6, 
                'peak_foce_con' : 2.2, 
                'mean_foce_con' : 1.6, 
                'peak_acceleration_con' : 0.8, 
                'mean_acceleration_con' : 0.4, 
                'peak_velocity_ecc' : 1.2, 
                'mean_velocity_ecc' : 0.6, 
                'peak_power_ecc' : 0.9, 
                'mean_power_ecc' : 0.45,               
                'peak_foce_ecc' : 0.9, 
                'mean_foce_ecc' : 0.45, 
                'peak_acceleration_ecc' : 1.2, 
                'mean_acceleration_ecc' : 0.6, 
                'rep_duration_con' : 0.05,
                'rep_duration_ecc' : 0.05,
                'top_stay_duration' : 0.05,
                'bottom_stay_duration' : 0.05,
                'rep_duration' : 0.05,                 
                'RSI' : 20.1,
                'RFD' : 30.5                
            }            

            list_data.append(data)

    return list_data
    
for i in range(3) : 
    post_req(user_id[0], workout_session_id[i], workout_id[i], sets, reps)
