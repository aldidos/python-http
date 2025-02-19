'''
====================================================================================
API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts
    Path params : 
        user_id : User 고유키
        workout_session_id : WorkoutSession 고유키
    Methods : 
        POST : 
            status code: 
                201 : OK
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>
    Path params : 
        user_id : User 고유키
        workout_session_id : WorkoutSession 고유키
        workout_id : Workout 고유키
    Methods : 
        PATCH : 
            status code: 
                200 : OK
        GET : 
            status code : 
                200 : OK
                404 : Not Found
====================================================================================
'''
import sys
sys.path.append('.')

from base_uri import BaseAPI, data_to_json, headers
import requests
import json
from datetime import datetime, timedelta

def create_workout(workout_session_id, equipment, completed_sets, start_time, end_time) : 
    return {
        'workout_session' : workout_session_id, 
        'equipment' : equipment, 
        'completed_sets' : completed_sets, 
        'start_time' : start_time, 
        'end_time' : end_time
    }

def create_dumydata(workout_session_id) : 
    cur_datetime = datetime.now()
    workout_start_time = cur_datetime     
    wokrout_end_time =  workout_start_time + timedelta(minutes = 15)

    return create_workout(workout_session_id, 1, 2, workout_start_time.isoformat(), wokrout_end_time.isoformat() )

user_id = 1
workout_session_id = 1
data = create_dumydata(workout_session_id)

class WorkoutSessionWorkoutsAPI (BaseAPI) : 

    def post(self, data) : 
        res = super().post(data)
        if res.status_code == 201 : 
            return json.loads(res.text)
        return None
    
    def get(self, params) : 
        res = requests.get(self.uri, params = params, headers = headers)
        self.print_response('GET', res)

def main() : 
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts' 
    api = WorkoutSessionWorkoutsAPI(uri)

    workout = api.post(data)
    print('POSTED workout id : ', workout['id'])
    
    api.get({'search_date' : 'period', 'from_date' : '2025-01-01', 'to_date' : '2025-03-01'})

    api.get({'date' : '2025-02-14'})

    ####
    workout_id = 1
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}' 
    api = BaseAPI(uri)    

    api.patch(data)

    api.get()

if __name__ == '__main__' : 
    main()


  