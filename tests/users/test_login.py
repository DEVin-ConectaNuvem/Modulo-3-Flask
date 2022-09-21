from flask import json

mimetype = 'application/json'
url = "/user/login"

def test_login_failed_email_wrong(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {
    "email": "testeteste@gmail.com",
    "password": "1234567"
  }

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 500
  assert response.json["error"] == "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."

def test_login_failed_password_wrong(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {
    "email": "luislopes@gmail.com",
    "password": "1234567"
  }

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 401
  assert response.json["error"] == "Suas credênciais estão incorretas!"

def test_login_failed_email_missing(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {
    "password": "1234567"
  }

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 422
  assert response.json["error"] == f"Está faltando o item ['email']"


def test_login_failed_password_missing(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {
    "email": "luislopes@gmail.com"
  }

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 422
  assert response.json["error"] == f"Está faltando o item ['password']"


def test_login_failed_missing_all_fields(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {}

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 422
  assert response.json["error"] == f"Está faltando o item ['email', 'password']"

def test_login_success(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }

  data = {
    "email": "luislopes@gmail.com",
    "password": "123Mudar!"
  }

  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 200
  assert "token" in response.json