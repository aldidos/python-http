import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

data = {    
    'user_id' : 1, 
    'center_equipment_id' : 1
}

data = json.dumps(data)

def save_session_id(session_id) : 
    with open('./temp_session_id.json', 'w', encoding='utf-8') as f : 
        json.dump({'session' : session_id}, f)

def load_session_id() : 
    with open('./temp_session_id.json', 'r', encoding='utf-8') as f : 
        return json.load(f)

def post_qr_certification() : 
    uri = f'{base_url}/qr_certification'

    res = requests.post(uri, data = data, headers = headers)    
    print(res.status_code)
    print(res.text)
    session_id = res.cookies.get('session')
    save_session_id(session_id)

def get_qr_certification() : 
    uri = f'{base_url}/qr_certification' 

    session_info = load_session_id()

    cookie = {
        'session' : session_info['session']
    }

    res = requests.get(uri, data = data, headers = headers, cookies=cookie)
    print(res.status_code)
    print(res.text)    

post_qr_certification() 
get_qr_certification()