'''
====================================================================================
API : /signup 
    Methods : 
        POST : 
            status code: 
                201 : OK
                400 : Bad Request        
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI

user_account = {
    'login_id' : 'tester_id', 
    'login_pw' : 'tester_id_pw'
}

user_info = {
    'name' : '테스터', 
    'weight' : 75.5, 
    'height' : 175.4, 
    'birthday' : '1984-03-18', 
    'contact' : '010-1123-2841', 
    'gender' : '여'
}

data = {
    'user_account' : user_account, 
    'user_info' : user_info
}

def main() : 
    uri = f'/signup' 
    api = BaseAPI(uri)

    api.post(data)

if __name__ == '__main__' : 
    main()