from flask import current_app
from jwt import encode

def is_table_empty(query, table):
    if query == None:
        print(f"Populating {table}...")
        return True
    else:
        print(f"{table} is populated!")
        return False

def exist_key(request_json, list_keys):
  keys_not_have_in_request = []

  for key in list_keys:
    if key in request_json:
      continue
    else:
      keys_not_have_in_request.append(key)

  if len(keys_not_have_in_request) == 0: 
    return request_json

  return {"error":  f"Está faltando o item {keys_not_have_in_request}", "status_code": 422 }

def exist_value(request_json):
  
  for json in request_json.items():
    key, value = json
    if value != None:
      pass
    else:
      return {"error":  f"O valor deste campo ['{key}'] não pode ser nulo"}
  return request_json
  
def generate_jwt(payload):
    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")

    return token