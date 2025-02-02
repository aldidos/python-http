from config import base_url, headers
import requests
import json

data = {
    'user_name' : 'jikim'    
}

data = json.dumps(data)

def save_session_id(session_id) : 
    with open('./temp_session_id.json', 'w', encoding='utf-8') as f : 
        json.dump({'session' : session_id}, f)

def load_session_id() : 
    with open('./temp_session_id.json', 'r', encoding='utf-8') as f : 
        return json.load(f)


def post() : 
    uri = f'{base_url}/test_session'    

    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code) 
    session_id = res.cookies.get('session')
    save_session_id(session_id)

def get( ) : 
    uri = f'{base_url}/test_session'    

    temp_session = load_session_id()

    cookie = {
        'session' : temp_session['session']
    }

    # res = requests.get(uri, data = data, headers = headers, cookies=cookie)    
    res = requests.get(uri, data = data, headers = headers) 
    print(res.status_code)    

# post() 
get( )