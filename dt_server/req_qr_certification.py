'''
====================================================================================
API : /qr_certification
    Methods : 
        PUT : 
            status code: 
                200 : OK
                400 : Bad Request
        GET : 
            status code : 
                200 : OK
                404 : Not Found
====================================================================================
'''
import sys
sys.path.append('.')

from config import base_url, headers
import requests
import json
from base_uri import BaseAPI

class QRcertificationAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

    def save_session_id(self, session_id) : 
        with open('./temp_session_id.json', 'w', encoding='utf-8') as f : 
            json.dump({'session' : session_id}, f)

    def load_session_id(self, ) : 
        with open('./temp_session_id.json', 'r', encoding='utf-8') as f : 
            return json.load(f)

    def put(self, data) : 
        res = super().put(data)        
        session_id = res.cookies.get('session')
        self.save_session_id(session_id)

    def get(self, data) : 
        session_info = self.load_session_id()

        cookie = {
            'session' : session_info['session']
        }
        res = requests.get(self.uri, data = data, headers = headers, cookies=cookie)
        self.print_response('GET', res)        

data = {
    'user_id' : 1, 
    'center_equipment_id' : 1, 
    'workout_session_id' : 1
}
     
if __name__ == '__main__' : 
    uri = f'/qr_certification' 
    api = QRcertificationAPI(uri)

    # api.put(data)

    api.get(data)