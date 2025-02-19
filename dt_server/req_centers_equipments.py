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
    'location' : 20,
    'usage' : False
}

class CentersEquipmentsAPI(BaseAPI) : 

    def post(self, data) : 
        res = super().post(data)        
        if res.status_code == 201 : 
            return json.loads(res.text)
        return None    

center_id = 1

def main() : 
    uri = f'/centers/{center_id}/equipments'
    api = CentersEquipmentsAPI(uri)    
    
    api.get()    
    center_equipment = api.post(data)

    if center_equipment : 
        center_equipment_id = center_equipment['id']

        uri = f'/centers/{center_id}/equipments/{center_equipment_id}'
        api = BaseAPI(uri)

        center_equipment['usage'] = True

        api.patch( center_equipment) 

        api.get()

if __name__ == '__main__' : 
    main()