import random
from flask import json

def test_create_missing_field(client):
  keys = ["city_id", "name", "age", "email", "password"]
  keys_not_have_in_request = keys.pop(random.randrange(len(keys)))

  data = {
    "email": "luisdasilva@gmail.com",
    "city_id": 1,
    "name": "Luis da Silva",
    "age": 25,
    "password": "1234567!teste"
  }

  del data[keys_not_have_in_request]

  response = client.post("/user/create", data=json.dumps(data), headers={
    "Content-Type": "application/json",
    "Accept": "application/json"
  })
  assert response.status_code == 422
  assert response.json["error"] == f"Está faltando o item ['{keys_not_have_in_request}']"