'''
====================================================================================
API : /users/<user_id>/workout_sessions/report
    Path params : 
        user_id : User 데이터의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workout_sessions/report/recent
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
import requests

class WorkoutSessionReportAPI(BaseAPI) : 

    def get(self, params) : 
        res = requests.get(self.uri, params = params)
        self.print_response('GET', res)

user_id = 1

def main() : 
    uri = f'/users/{user_id}/workout_sessions/report/recent' 
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workout_sessions/report' 
    api = WorkoutSessionReportAPI(uri)
    api.get({'from_date' : '2025-01-01', 'to_date' : '2025-03-01'})


if __name__ == '__main__' : 
    main()