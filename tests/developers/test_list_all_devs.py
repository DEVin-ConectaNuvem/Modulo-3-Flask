from urllib import response
from flask import json

def test_developers_success_status_200(client, logged_in_client):
    assert client.get('/developers/', headers={
        "Authorization": f"Bearer {logged_in_client}"
    }).status_code == 200

def test_developers_by_search_developers(client, logged_in_client):
    response = client.get("/developers/search_developers", headers={
        "Authorization": f"Bearer {logged_in_client}"
    })

    assert "records" in response.json

def test_developers_by_name_error_query_param(client, logged_in_client):
    response = client.get("/developers/search_developers?name='12333'",
    headers={
        "Authorization": f"Bearer {logged_in_client}"
    }).status_code == 403

    assert response.json["error"] == "Não existe Developers com esse nome."

def test_developers_by_name(client, logged_in_client):
    response = client.get("/developers/search_developers?name='joao'",
    headers={
        "Authorization": f"Bearer {logged_in_client}"
    }).status_code == 200

    
    assert "records" in response.json
