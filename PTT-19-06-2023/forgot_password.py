import pytest
import requests

def test_forgot_password():
    response = requests.post('https://dev-api.pttapp.com/api/forgot-password', json={

    "username": "jerrish"


    })

    assert response.status_code == 500