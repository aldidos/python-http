'''
====================================================================================
API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/workout_metrics
    Path params : 
        user_id : User의 고유키
        workout_session_id : WorkoutSession 고유키
        workout_id : Workout 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/<set_id>/workout_metrics
    Path params : 
        user_id : User의 고유키
        workout_session_id : WorkoutSession 고유키
        workout_id : Workout 고유키
        set_id : WorkoutSet 고유키키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI

user_id = 1
workout_session_id = 1
workout_id = 1
set_id = 1

def main() :    
    #### API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/workout_metrics
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}/sets/workout_metrics'
    api = BaseAPI(uri)

    api.get()

    #### API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/<set_id>/workout_metrics
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}/sets/{set_id}/workout_metrics'
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()