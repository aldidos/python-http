'''
====================================================================================
API : /users/<user_id>/workout_sessions
    Path params : 
        user_id : User 데이터의 고유키
    Methods : 
        Post : 
            status code: 
                201 : 데이터 생성 성공                                
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workout_sessions/recent
    Path params : 
        user_id : User 데이터의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workout_sessions/<workout_session_id>
    Path params : 
        user_id : User 고유키
        workout_session_id : WorkoutSession 고유키
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

from base_uri import BaseAPI, headers
import requests
from datetime import date
import json

class UserWorkoutSessionsAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

    def get(self, query_params) : 
        res = requests.get(self.uri, params=query_params,  headers = headers)
        self.print_response('GET', res)

    def post(self, data) : 
        res = super().post(data)
        if res.status_code == 201 : 
           return json.loads(res.text) 
        return None

data = {
    'user' : 1, 
    'date' : date.today().isoformat(), 
    'status' : 'Process',
    'is_completed' : False    
}

query_params = {
    'from_date' : '2025-01-01', 
    'to_date' : '2025-03-01', 
    'search_date' : 'period'
}

query_params = {
    'from_date' : '2025-01-01', 
    'to_date' : '2025-03-01', 
    'search_date' : 'period'
}

user_id = 1
workout_session_id = 1

class WorkoutSessionAPI(BaseAPI) : 

    def get(self) : 
        res = super().get()

        if res.status_code == 200 : 
            return json.loads(res.text)
        return None

def main() : 
    #### API : /users/<user_id>/workout_sessions
    uri = f'/users/{user_id}/workout_sessions' 
    api = UserWorkoutSessionsAPI(uri)    

    api.get({
        'from_date' : '2025-01-01', 
        'to_date' : '2025-03-01', 
        'search_date' : 'period'
    })

    api.get({
         'date' : '2025.02-11' 
    })       

    #### API : /users/<user_id>/workout_sessions/recent
    uri = f'/users/{user_id}/workout_sessions/recent' 
    api = BaseAPI(uri)

    api.get()

    #### API : /users/<user_id>/workout_sessions/<workout_session_id>
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}' 
    api = WorkoutSessionAPI(uri)

    workout_session = api.get()
    if workout_session : 
        workout_session['is_completed'] = True
        workout_session['status'] = 'Complete'
        api.patch(workout_session)

if __name__ == '__main__' : 
    main()