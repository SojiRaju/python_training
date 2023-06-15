import pytest
import requests

@pytest.fixture
def api_client():
    return requests.Session()

def test_invalid_url(api_client):
    url = "https://api.example.com/invalid"
    with pytest.raises(requests.exceptions.RequestException):
        api_client.get(url)
