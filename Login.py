import pytest
import requests

@pytest.fixture
def api_client():
  return requests.Session() # Create an API client session

  #def test_successful_login(api_client):
  # url = "https://reqres.in/api/login"
  # payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
  # response = api_client.post(url, json=payload)
  # assert response.status_code == 200
  # assert response.json()['success'] == True
def test_failed_login(api_client):
  url = 'https://reqres.in/api/login'
  payload = {"username": "testuser", "password": "wrongpassword"}
  response = api_client.post(url, json=payload)

  assert response.status_code == 400
  #assert response.json()['success'] == False


