def test_cities_success_status_200(client, logged_in_client):
  assert client.get('/cities/get_all_cities/1', headers={
    "Authorization": f"Bearer {logged_in_client}"
  }).status_code == 200

def test_cities_failed_status_404_by_parameter_wrong(client):
  
  response = client.get('/cities/get_all_cities/city_id')
  assert response.status_code == 404

def test_cities_return_data(client, logged_in_client):
  response = client.get('/cities/get_all_cities/1', headers={
    "Authorization": f"Bearer {logged_in_client}"
  })
  assert "records" in response.json

def test_cities_not_return_data(client, logged_in_client):
  response = client.get('/cities/get_all_cities/29', headers={
    "Authorization": f"Bearer {logged_in_client}"
  })
  assert len(response.json["records"]) == 0

def test_cities_not_authenticated(client):
  assert client.get('/cities/get_all_cities/1').status_code == 403

def test_cities_authenticated_but_no_has_bearer(client, logged_in_client):
  assert client.get('/cities/get_all_cities/1', headers={
    "Authorization": f"{logged_in_client}"
  }).status_code == 401