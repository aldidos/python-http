import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

def send_request_put() : 

    data = {
        'center_name' : 'test_center_1', 
        'center_address' : 'test_center_address_1dshjkdsa',
        'user_id' : '1',
        'user_name' : 'test_user_1',
        'birthday' : '1982-01-31',
        'contact' : '010-2123-2111',
    }
    data = json.dumps(data)
    
    uri = f'{base_url}//center_authentication'

    res = requests.put(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def send_request_get() : 
    data = {
        'user_id' : 1,
        'center_id' : 1
    }
    data = json.dumps(data)

    uri = f'{base_url}//center_authentication'

    res = requests.get(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

# send_request_put()
send_request_get()