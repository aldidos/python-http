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

user_id = 1
workout_session_id = 1

def main() : 
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}' 
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()