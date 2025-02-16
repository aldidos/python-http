'''
====================================================================================
API : /centers/<center_id>/equipments<center_equipment_id>
    Path params : 
        center_id : Center 데이터의 고유키
        center_equipment_id : CenterEquipment 고유키키
    Methods : 
        PATCH : 
            status code: 
                200 : OK                
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
    'location' : 1,
    'usage' : True
}

center_id = 1
center_equipment_id = 1

def main() : 
    uri = f'/centers/{center_id}/equipments/{center_equipment_id}'
    api = BaseAPI(uri)

    api.patch( data) 

    api.get()

if __name__ == '__main__' : 
    main()