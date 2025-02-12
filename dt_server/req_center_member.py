'''
====================================================================================
API : /centers/<center_id>/members
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
                400 : Bad Request

API : /centers/<center_id>/members/<member_id>
    Path params : 
        center_id : Center 데이터의 고유키
        member_id : CenterMember 데이터의 고유키(Primary key)
    Methods : 
        PATCH :     
            status code: 
                200 : OK
        GET : 
            status code: 
                200 : OK
                404 : Not Found
====================================================================================
'''
import sys
sys.path.append('.')

from base_uri import BaseAPI
import json

center_id = 1

data = {
    'center' : center_id, 
    'name' : '임시직',
    'birth_day' : '1983-03-12', 
    'contact' : '010-9999-9999', 
    'reg_from' : '2024-12-20', 
    'reg_to' : '2025-06-30', 
    'visit_date' : None, 
}

class CenterMembersAPI(BaseAPI) : 

    def post(self, data) : 
        res = super().post(data)

        if res.status_code == 201 : 
            center_member = json.loads(res.text)
            return center_member
        return None
    
class CenterMemberAPI(BaseAPI) : 

    def patch(self, data) : 
        res = super().patch(data)
        if res.status_code == 200 : 
            center_member = json.loads(res.text)
            return center_member
        return None
    
    def get(self) : 
        res = super().get()
        if res.status_code == 200 : 
            return json.loads(res.text)
        return None

def main() : 
    centerMembersAPI = CenterMembersAPI(f'/centers/{center_id}/members')
    centerMembersAPI.get()
    center_member = centerMembersAPI.post(data)    
    if center_member : 
        center_member_id = center_member['id']
        centerMemberAPI = CenterMemberAPI(f'/centers/{center_id}/members/{center_member_id}')
        center_member = centerMemberAPI.get()
        if center_member :
            center_member['visit_date'] = '2025-02-12'
            centerMemberAPI.patch(center_member)


if __name__ == '__main__' : 
    main()
    
