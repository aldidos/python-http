import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

data = {    
    'center_id' : 1, 
    'name' : 'jikim',
    'birth_day' : '1983-03-12', 
    'contact' : '010-9876-9999', 
    'reg_from' : '2024-12-20', 
    'reg_to' : '2025-06-30', 
    'visit_date' : None, 
}

def post_req(data) : 
    center_id = 1
    uri = f'{base_url}/centers/{center_id}/members'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_center_members(data) : 
    center_id = 1    
    uri = f'{base_url}/centers/{center_id}/members'

    params = { 'center_member_name' : 'jikim', 'center_member_birth_day' : '1983-03-12', 'center_member_contact' : '010-9876-9999' }
    
    data = json.dumps(data)
    res = requests.get(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

# post_req(data)
get_center_members(data)