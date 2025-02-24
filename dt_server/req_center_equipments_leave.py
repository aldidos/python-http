'''
====================================================================================
API : /centers/<center_id>/equipments/<center_equipment_id>/leave
    Path params : 
        center_id : Center 데이터의 고유키
        center_equipment_id : CenterEquipment 고유키
    Methods : 
        PUT : 
            status code: 
                200 : OK                        
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI, data_to_json, requests, headers

center_id = 1
center_equipment_id = 1
user_id = 1
machine_key = '1R@3s$^ixwpAWch%$@aox'

data = {
    'machine_key' : machine_key, 
    'user_id' : 1    
}

def main() : 
    uri = f'/centers/{center_id}/equipments/{center_equipment_id}/leave'
    api = BaseAPI(uri)
    
    api.put(data)        

if __name__ == '__main__' : 
    main()