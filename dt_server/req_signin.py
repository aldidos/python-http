from config import base_url, headers
import requests
import json

data = {
    'login_id' : 'qwertyui', 
    'login_pw' : 'aaaaaabb'
}

data = json.dumps(data)

def get_signin() : 
    uri = f'{base_url}/signin'

    res = requests.get(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

get_signin()    