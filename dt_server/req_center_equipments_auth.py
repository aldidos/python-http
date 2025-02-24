'''
====================================================================================
API : /centers/<center_id>/equipments/<center_equipment_id>/auth
    Path params : 
        center_id : Center 데이터의 고유키
        center_equipment_id : CenterEquipment 고유키
    Methods : 
        PUT : 
            status code: 
                200 : OK
                400 : Bad Request 
        GET :     
            status code: 
                200 : OK
                400 : Bad Request
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI, data_to_json, requests, headers

center_id = 1
center_equipment_id = 1
machine_key = '1R@3s$^ixwpAWch%$@aox'

data = {
    'machine_key' : machine_key, 
    'user_id' : 1,
    'workout_session_id' : 1
}

class CenterEquipmentAuthAPI(BaseAPI) : 

    def get(self, data) : 
        data = data_to_json(data)
        res = requests.get(self.uri, data = data, headers = headers)
        self.print_response('GET', res)

def main() : 
    uri = f'/centers/{center_id}/equipments/{center_equipment_id}/auth'
    api = CenterEquipmentAuthAPI(uri)
    
    api.put(data)    

    api.get({'machine_key' : machine_key })

if __name__ == '__main__' : 
    main()