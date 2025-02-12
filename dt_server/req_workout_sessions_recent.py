'''
====================================================================================
API : /users/<user_id>/workout_sessions/recent
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

from dt_server.base_uri import BaseAPI

user_id = 1

def main() : 
    uri = f'/users/{user_id}/workout_sessions/recent' 
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()