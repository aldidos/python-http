'''
====================================================================================
API : /lounge
    Methods : 
        GET : 
            status code: 
                200 : OK                
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI, requests, headers, data_to_json

data = {
    'user_id' : 1, 
    'center_id' : 1
}

class LoungeAPI(BaseAPI) : 

    def get(self, data) : 
        data = data_to_json(data)
        res = requests.get(self.uri, data = data, headers = headers)
        self.print_response('GET', res)

def main() : 
    uri = f'/lounge' 
    api = LoungeAPI(uri)

    api.get(data)

if __name__ == '__main__' : 
    main()