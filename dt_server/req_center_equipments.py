'''
====================================================================================
API : /centers/<center_id>/equipments
    Path params : 
        center_id : Center 데이터의 고유키
    Methods : 
        POST : 
            status code: 
                201 : 데이터 생성 성공
                400 : Bad Request 
        GET :     
            status code: 
                200 : OK
                404 : Bad Request
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI
import json

data = {
    'center' : 1, 
    'equipment' : 1,
    'exercise_library' : 1, 
    'location_x' : 50,
    'location_y' : 100, 
    'usage' : False
}

def post(data) : 
    center_id = data['center']
    uri = f'/centers/{center_id}/equipments'
    api = BaseAPI(uri)
    res = api.post(data)
    if res == 201 : 
        return json.loads(res.text)
    return None

def get(center_id) : 
    uri = f'/centers/{center_id}/equipments'
    api = BaseAPI(uri)

    api.get()

def main() : 
    post(data)
    get(1)

if __name__ == '__main__' : 
    main()