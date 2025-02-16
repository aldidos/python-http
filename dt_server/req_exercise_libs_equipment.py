'''
====================================================================================
API : /exercise_libraries/<equipment_id>
    Methods : 
        GET : 
            status code : 
                200 : OK
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI

def main() : 
    equipment_id = 1
    uri = f'/exercise_libraries/{equipment_id}' 
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()