import json

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

def respond_to_auth_challenge(token, url):
  headers = {
  'Authorization': f'Bearer {access_token()}'
  }
  response = requests.post(url + "respond-to-auth-challenge", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")

respond_to_auth_challenge(token=access_token(), url="https://dev-api.pttapp.com/api/")
