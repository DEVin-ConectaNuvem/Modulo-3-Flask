from flask import json
import random

mimetype = 'application/json'
url = "/user/update"

def test_update_not_authorized(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  
  response = client.put(url, headers=headers)
  assert response.status_code == 403

def test_update_authorized_update_id(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }

  data = {
    "id": 1000
  }
  
  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 400
  assert response.json["error"] == "Não é possível alterar este campo."

def test_update_exist_user(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }

  data = {
    "name": "Jorge"
  }
  
  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 204

def test_update_not_found_user(client, logged_in_client_with_user_deleted):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client_with_user_deleted}'
  }

  data = {
    "name": "Jorge"
  }
  
  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 403
  assert response.json["error"] == "O Token é inválido"

def test_update_change_email_failed_same_other_email(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }

  data = {
    "email": "corinta.lima@example.com"
  }
  
  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 403
  assert response.json["error"] == "Você não pode alterar o e-mail."

def test_update_body_empty(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }

  data = {}
  
  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 400
  assert response.json["error"] == "Não foi enviado nenhum dado para fazer alteração."

def test_update_change_fields_not_null(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }
  keys = ["city_id", "name", "age", "email", "password"]
  keys_not_have_in_request = keys.pop(random.randrange(len(keys)))
  
  data = {
    "city_id": 1, 
    "name": "Jorge da Silva", 
    "age": 19, 
    "email": "corinta1.lima@example.com", 
    "password": "123Trocar!"
  }
  data[keys_not_have_in_request] = None 

  response = client.put(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 400
  assert response.json["error"] == f"O valor deste campo ['{keys_not_have_in_request}'] não pode ser nulo"