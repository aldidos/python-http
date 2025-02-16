'''
====================================================================================
API : /users    
    Methods : 
        POST : 
            status code: 
                200 : OK
        GET : 
            status code : 
                200 : OK
                400 : Bad request

API : /users/<user_id>
    Path params : 
        user_id : User 고유키
    Methods : 
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
    'name' : '공휴일',
    'weight' : 88,
    'height' : 182,
    'birthday' : '1989-05-05',
    'contact' : '111-1111-1111',
    'gender' : '남'
}

def main() : 
    uri = f'/users'
    api = BaseAPI(uri)

    api.post(data)    

    user_id = 1
    uri = f'/users/{user_id}'
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()