import sys
sys.path.append('.')

from dt_server.config import base_url, headers
import requests
import json

user_account = {
    'login_id' : 'jungilkim', 
    'login_pw' : 'aaaaaabb'
}

user_info = {
    'name' : 'kim jung il', 
    'weight' : 75.5, 
    'height' : 178.4, 
    'birthday' : '1983-04-24', 
    'contact' : '010-1123-2841', 
    'gender' : '남'
}

data = {
    'user_account' : user_account, 
    'user_info' : user_info
}

data = json.dumps(data)

def post_signup() : 
    uri = f'{base_url}/signup'

    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

post_signup()    