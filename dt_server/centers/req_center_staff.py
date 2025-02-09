import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

data = {    
    'center_id' : 1, 
    'name' : 'mlksdjf',
    'birth_day' : '1982-02-12' 
}

def post_req(data) : 
    center_id = 1
    uri = f'{base_url}/centers/{center_id}/staffs'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_req() : 
    center_id = 1
    uri = f'{base_url}/centers/{center_id}/staffs'

    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

# post_req(data)
get_req()