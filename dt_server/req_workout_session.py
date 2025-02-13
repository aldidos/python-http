'''
====================================================================================
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

from base_uri import BaseAPI
import json

user_id = 1
workout_session_id = 1

class WorkoutSessionAPI(BaseAPI) : 

    def get(self) : 
        res = super().get()

        if res.status_code == 200 : 
            return json.loads(res.text)
        return None

def main() : 
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}' 
    api = WorkoutSessionAPI(uri)

    workout_session = api.get()
    if workout_session : 
        workout_session['is_completed'] = True
        workout_session['status'] = 'Complete'
        api.patch(workout_session)

if __name__ == '__main__' : 
    main()