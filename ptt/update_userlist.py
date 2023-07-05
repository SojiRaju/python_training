import json
import pytest
import requests
def access_token():
# To get Access Token
  payload = {"username": "anisha", "password": "Anisha@12345"}
  url = "https://dev-api.pttapp.com/api/"
  response = requests.post(url + "login", json=payload)
  data = response.json()
  token = data["authenticationResult"]["AccessToken"]
  return token
access_token()


def update_userlist(token, url):
  payload = {
    "userId":"ee4006bd-23ab-499a-9adc-cf7c6f195c48",
    "confirmationStatus":"",
    "role":"",
    "booking":"true",
    "transaction":"true",
    "reports":["weekly fortnightly reporting","trust balance"]
    }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }

  response = requests.put(url + "user-update", json=payload, headers=headers)
  if response.status_code == 200:
    print(f"success: {response.status_code}")
  else:
    print(f"Error: {response.status_code}")


update_userlist(token=access_token(), url="https://dev-api.pttapp.com/api/")

