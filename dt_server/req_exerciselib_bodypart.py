'''
====================================================================================
API : /exerciselib_bodyparts
    Methods : 
        GET : 
            status code : 
                200 : OK

API : /exerciselib_bodyparts/<exerciselib_id>/<body_part_id>
Path params : 
    exerciselib_id : ExerciseLibrary 고유키
    body_part_id : BodyPart 고유키
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

def main() : 
    uri = f'/exerciselib_bodyparts' 
    api = BaseAPI(uri)
    api.get()

    exerciselib_id = 1
    body_part_id = 4
    uri = f'/exerciselib_bodyparts/{exerciselib_id}/{body_part_id}' 
    api = BaseAPI(uri)
    api.get()

if __name__ == '__main__' : 
    main()

