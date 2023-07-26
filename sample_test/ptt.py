import pytest
import requests


@pytest.fixture
def api_client():
    return requests.Session()  # Create an API client session


def test_successful_login(api_client):
    url = "https://dev-api.pttapp.com/api/login"
    payload = {"username": "nismal", "password": "Simple2022$"}
    response = api_client.post(url, json=payload)
    assert response.status_code == 200
    # assert response.json()['success'] == True
