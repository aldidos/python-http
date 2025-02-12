'''
====================================================================================
API : /end_wokrout_session
    Methods : 
        PUT : 
            status code: 
                200 : OK      
====================================================================================
'''

import sys
sys.path.append('.')

from config import base_url, headers
import requests
import json
from base_uri import BaseAPI

class EndWorkoutSessionAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)    

    def load_session_id(self, ) : 
        with open('./temp_session_id.json', 'r', encoding='utf-8') as f : 
            return json.load(f)

    def put(self) : 
        session_info = self.load_session_id()

        cookie = {
            'session' : session_info['session']
        }
        res = requests.put(self.uri, headers = headers, cookies=cookie)
        self.print_response('GET', res)

if __name__ == '__main__' : 
    uri = f'/end_wokrout_session' 
    api = EndWorkoutSessionAPI(uri)
    
    api.put()