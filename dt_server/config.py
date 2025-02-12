import json

APP_TOKEN_VALUE = 'aDiQ2X@&a$!2hcoIJdtyaYwBcghP2)kc'

headers = {
    "Content-Type" : "application/json" 
}

base_url = f'http://127.0.0.1:5000'

def data_to_json(data) : 
    return json.dumps(data, ensure_ascii=False)