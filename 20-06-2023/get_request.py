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
def user_details(token, url):
  headers = {
   'Authorization': f'Bearer {access_token()}'
   }
  response = requests.get(url + "user-details", headers=headers)
  if response.status_code == 200:
   data = response.json()
   print(data)
  else:
   print(f"Error: {response.status_code}")
user_details(token=access_token(), url="https://dev-api.pttapp.com/api/")

def user_list(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "list-user", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
user_list(token=access_token(), url="https://dev-api.pttapp.com/api/")


def user_profile_download(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "profile-download", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
user_profile_download(token=access_token(), url="https://dev-api.pttapp.com/api/")


def list_client(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "client/list?claimFromTBR=", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
list_client(token=access_token(), url="https://dev-api.pttapp.com/api/")


def profile_update(token, url):
    payload = {"name": "nismal", "email": "nithincgeorge98@gmail.com"}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "profile-update", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")
profile_update(token=access_token(),  url="https://dev-api.pttapp.com/api/")


def client_list_search(token, url, null=None):
    payload = {"query": null}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.post(url + "client/search", json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Pretty-print the JSON response
        formatted_json = json.dumps(data, indent=4)
        # Print the formatted JSON
        print(formatted_json)
    else:
        print(f"Error: {response.status_code}")
client_list_search(token=access_token(),  url="https://dev-api.pttapp.com/api/")


def client_list_search_export(token, url, null=None):
    payload = {"query": null}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.post(url + "client/search/export", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success and status_code is: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")
client_list_search_export(token=access_token(),  url="https://dev-api.pttapp.com/api/")
