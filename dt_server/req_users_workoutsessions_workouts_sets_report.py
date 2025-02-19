'''
====================================================================================
API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/<set_id>/report
    Path params : 
        user_id : User 데이터의 고유키
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
    uri = f'/users/{user_id}/workout_sessions/<{workout_session_id}>/workouts/{workout_id}/sets/{set_id}/report'
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()


