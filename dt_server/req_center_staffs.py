'''
====================================================================================
API : /centers/<center_id>/staffs
    Path params : 
        center_id : Center 데이터의 고유키

    Methods : 
        Post : 
            status code: 
                201 : 데이터 생성 성공
                400 : Bad Request
                404 : Not Found
        GET : 
            status code : 
                200 : OK
                404 : Not Found
====================================================================================
'''
import sys
sys.path.append('.')

from base_uri import BaseAPI
import json

data = {
    'center' : 1, 
    'name' : '임시직원',
    'birth_day' : '2000-01-01'
}

center_id = 1

def post(data) : 
    center_id = data['center']
    uri = f'/centers/{center_id}/staffs'
    api = BaseAPI(uri)
    res = api.post(data)
    if res == 201 : 
        return json.loads(res.text)
    return None

def get() : 
    uri = f'/centers/{center_id}/staffs'
    api = BaseAPI(uri)

    api.get()

def main() : 
    post(data)
    get()

if __name__ == '__main__' : 
    main()    
