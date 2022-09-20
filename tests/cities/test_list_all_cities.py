def test_cities_success_status_200(client):
  assert client.get('/cities/get_all_cities/1').status_code == 200

def test_cities_failed_status_404_by_parameter_wrong(client):
  
  response = client.get('/cities/get_all_cities/city_id')
  assert response.status_code == 404

def test_cities_return_data(client):
  response = client.get('/cities/get_all_cities/1')
  assert "records" in response.json

def test_cities_not_return_data(client):
  response = client.get('/cities/get_all_cities/29')
  assert len(response.json["records"]) == 0