import pytest
import requests


def change_password_incorrect_current_password():
    response = requests.post('https://dev-api.pttapp.com/api/change-password', json={
        "currentPassword": "Simple2020$",
        "password": "Simple2022$"

    })
    assert response.status_code == 401
# def change_password_successful():
# response = requests.post('https://dev-api.pttapp.com/api/change-password', json={
# "currentPassword": "Simple2020$",
# "password": "Simple2022$123"

# })
# assert response.status_code == 200
