import random
from flask import json

mimetype = 'application/json'
url = "/user/create"

def test_create_missing_field(client, logged_in_client):
  keys = ["city_id", "name", "age", "email", "password"]
  keys_not_have_in_request = keys.pop(random.randrange(len(keys)))
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  headers["Authorization"] = f"Bearer {logged_in_client}"
  
  data = {
    "email": "luisdasilva@gmail.com",
    "city_id": 1,
    "name": "Luis da Silva",
    "age": 25,
    "password": "1234567!teste"
  }

  del data[keys_not_have_in_request]

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 422
  assert response.json["error"] == f"Está faltando o item ['{keys_not_have_in_request}']"

def test_create_not_authorized(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  
  response = client.post(url, headers=headers)
  assert response.status_code == 403
  assert response.json["error"] == "Você não tem permissão"

def test_create_user_success(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  headers['Authorization'] = f"Bearer {logged_in_client}"
  data = {
      'email': "loivaci.lopes3@example.com",
      'city_id': 2,
      'name': 'Luis Lopes',
      'age': 30,
      'password': '123Mudar!'
  }
  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 201
  assert response.json['message'] == "Usuário foi criado com sucesso."

def test_create_user_failed_exist_user(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  headers['Authorization'] = f"Bearer {logged_in_client}"
  data = {
      'email': "luislopes@gmail.com",
      'city_id': 2,
      'name': 'Luis Lopes',
      'age': 30,
      'password': '123Mudar!'
  }
  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 400
  assert response.json['message'] == "Não foi possível criar o usuário"