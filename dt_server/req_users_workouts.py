'''
====================================================================================
 API : /users/<user_id>/workouts/equipments/<equipment_id>/recent
    Path params : 
        user_id : User의 고유키
        equipment_id : Equipment의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found    

API : /users/<user_id>/workouts/equipments/<equipment_id>/most_recent
    Path params : 
        user_id : User의 고유키
        equipment_id : Equipment의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/recent
    Path params : 
        user_id : User의 고유키
        exercise_library_id : ExerciseLibrary의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found    

API : /users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/most_recent
    Path params : 
        user_id : User의 고유키
        exercise_library_id : ExerciseLibrary의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found

API : /users/<user_id>/workouts/body_parts/<body_part_id>/recent
    Path params : 
        user_id : User의 고유키
        body_part_id : BodyPart의 고유키
    Methods : 
        GET : 
            status code : 
                200 : OK
                404 : Not Found    

API : /users/<user_id>/workouts/body_parts/<body_part_id>/most_recent
    Path params : 
        user_id : User의 고유키
        body_part_id : BodyPart의 고유키
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
equipment_id = 11
exercise_library_id = 1
body_part_id = 4

def main() :     
    uri = f'/users/{user_id}/workouts/equipments/{equipment_id}/recent'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workouts/equipments/{equipment_id}/most_recent'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workouts/exercise_libraries/{exercise_library_id}/recent'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workouts/exercise_libraries/{exercise_library_id}/most_recent'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workouts/body_parts/{body_part_id}/recent'
    api = BaseAPI(uri)
    api.get()

    uri = f'/users/{user_id}/workouts/body_parts/{body_part_id}/most_recent'
    api = BaseAPI(uri)
    api.get()


if __name__ == '__main__' : 
    main()