from config import headers, base_url, json, data_to_json
import requests

class BaseAPI : 
    
    def __init__(self, uri) : 
        self.uri = f'{base_url}/{uri}'

    def print_response(self, method, res) :         
        print(f'{self.uri} : {method}, {res.status_code}')
        print('Response body : ')
        print(f'{res.text}')
   
    def get(self) : 
        res = requests.get(self.uri, headers = headers)
        self.print_response('GET', res)
        return res

    def post(self, data) : 
        data = data_to_json(data)
        res = requests.post(self.uri, data = data, headers = headers)
        self.print_response('POST', res)
        return res        

    def put(self, data) : 
        data = data_to_json(data)
        res = requests.put(self.uri, data = data, headers = headers)
        self.print_response('PUT', res)
        return res

    def patch(self, data) : 
        data = data_to_json(data)
        res = requests.patch(self.uri, data = data, headers = headers)
        self.print_response('PATCH', res)
        return res