from config import base_url, headers
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

def post_req() : 
    center_id = 1
    uri = f'{base_url}/centers/{center_id}/members'

    data = json.dumps(data)
    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_center_members() : 
    center_id = 1    
    uri = f'{base_url}/centers/{center_id}/members'

    data = json.dumps(data)
    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def get_center_member() : 
    center_id = 1
    member_id = 2    
    uri = f'{base_url}/centers/{center_id}/members/{member_id}'

    data = json.dumps(data)
    res = requests.get(uri, headers = headers)
    print(res.status_code)
    print(res.text)

def put_center_member(data) : 
    center_id = 1
    member_id = 2        
    data['id'] = member_id
    data['visit_date'] = '2024-12-26'
    uri = f'{base_url}/centers/{center_id}/members/{member_id}'

    data = json.dumps(data)
    res = requests.put(uri, data = data,  headers = headers)
    print(res.status_code)
    print(res.text)

put_center_member(data)