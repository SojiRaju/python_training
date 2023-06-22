import pytest
import requests

def access_token():
# To get Access Token
  payload = {"username": "nismal", "password": "Simple2022$"}
  url = "https://dev-api.pttapp.com/api/"
  response = requests.post(url + "login", json=payload)
  data = response.json()
  token = data["authenticationResult"]["AccessToken"]
  return token
access_token()

def forgot_password(token, url):
    payload = {"username": "jerrish"}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "forgot-password", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")
forgot_password(token=access_token(), url="https://dev-api.pttapp.com/api/")


