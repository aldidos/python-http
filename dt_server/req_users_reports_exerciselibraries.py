'''
====================================================================================
 API : /users/<user_id>/reports/recent/exercise_libraries/<exercise_library_id>
    Path params : 
        user_id : User의 고유키
        exercise_library_id : ExerciseLibrary의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found    

API : /users/<user_id>/reports/recent/exercise_libraries/<exercise_library_id>/<set_number>
    Path params : 
        user_id : User의 고유키
        exercise_library_id : ExerciseLibrary의 고유키
        set_number : workout set 번호
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

user_id = 1
exercise_library_id = 1
set_number = 1

def main() :     
    uri = f'/users/{user_id}/reports/recent/exercise_libraries/{exercise_library_id}/{set_number}'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/reports/recent/exercise_libraries/{exercise_library_id}'
    api = BaseAPI(uri)
    api.get()


if __name__ == '__main__' : 
    main()