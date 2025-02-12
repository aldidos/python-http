'''
====================================================================================
API : /center_authentication
    Methods : 
        PUT : 
            status code: 
                201 : OK
                400 : Bad Request
        GET : 
            status code : 
                200 : OK
                404 : Not Found
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI, headers, data_to_json
import requests

class CenterAuthAPI(BaseAPI) : 

    def get(self, data) : 
        data = data_to_json(data)
        res = requests.get(self.uri, data = data, headers=headers)
        self.print_response('GET', res)

user_id = 1

put_data = {
    'center_name' : 'test_center_1', 
    'center_address' : 'test_center_address_1dshjkdsa',
    'user_id' : user_id
}

get_data = {
    'user_id' : 1,
    'center_id' : 1
}

def main() : 
    uri = f'/center_authentication' 
    api = CenterAuthAPI(uri)

    api.put(put_data)

    api.get(get_data)

if __name__ == '__main__' : 
    main()