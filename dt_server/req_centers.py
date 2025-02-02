from config import base_url, headers
import requests
import json

data = {
    'name' : 'my center', 
    'address' : 'my center addreadd 11231-123'
}

data = json.dumps(data)

def post_req() : 
    uri = f'{base_url}/centers'

    res = requests.post(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

def get_req() : 
    center_id = 1
    uri = f'{base_url}//centers/{center_id}'

    res = requests.get(uri, data = data, headers = headers)
    print(res.status_code)
    print(res.text)

# post_req()
get_req()