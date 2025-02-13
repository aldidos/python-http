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

def main() : 
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

if __name__ == '__main__' : 
    main()