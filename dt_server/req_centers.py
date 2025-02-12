'''
====================================================================================
API : /centers
    Methods : POST
        POST : 
            status code: 
                201 : 데이터 생성 성공
                400 : Bad Request       

API : /centers/<center_id>
    Path params : 
        center_id : Center 데이터의 고유키
    Methods : 
        GET :     
            status code: 
                200 : OK
                400 : Bad Request 
====================================================================================
'''
import sys
sys.path.append('.')

from base_uri import BaseAPI
import json

data = {
    'name' : 'Heyday Workouts', 
    'address' : '대구 중구 오성 550-112'
}

def post_centers() : 
    uri = f'/centers' 
    api = BaseAPI(uri)

    res = api.post(data)
    if res.status_code == 201 : 
        center = json.loads(res.text)
        return center['id']
    return None

def get_centers_centerid(center_id) :     
    uri = f'/centers/{center_id}' 
    api = BaseAPI(uri)

    api.get()

def main() : 
    center_id = post_centers()
    if center_id : 
        get_centers_centerid(center_id)    

if __name__ == '__main__' : 
    main()    