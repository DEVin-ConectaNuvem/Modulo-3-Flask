from flask import json

mimetype = 'application/json'
url = "/user/update"

def test_update_not_authorized(client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
  }
  
  response = client.put(url, headers=headers)
  assert response.status_code == 204
