import requests
def access_token():
  # To get Access Token
  payload = {"username": "anisha", "password": "Anisha@12345"}
  url = "https://dev-api.pttapp.com/api/"
  response = requests.post(url + "login", json=payload)
  data = response.json()
  token = data["authenticationResult"]["AccessToken"]
  print(token)
  return token
access_token()


def claim_upload(token, url,):
  payload = {
    "clientId": "62a810a2f5043cdcdf1f00ca",
    "fileName": "20221205-XYZ-Claim_2",
    "fileId": "{{claimFileId}}",
    "claimFromTBR": "false"
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.post(url + "claim/upload", json=payload, headers=headers)
  if response.status_code == 400:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")

claim_upload(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_update(token, url):
  payload = {
    "claimId": "62023b691eed04813999f201",
    "notes": "string2",
    "assignedTo": "6204d9d61eed04813999f227"
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.put(url + "claim/update", json=payload, headers=headers)
  if response.status_code == 400:
    print(f"Success : {response.json()}")
  else:
    print(f"Error: {response.status_code}")

claim_update(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_type(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "claim/quick_check/62037d1ac57a15c58fa5f8bf", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")
claim_type(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_transaction(token, url):

  payload = {
    "check": ""
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.put(url + "claim/transaction/620b75d59b53aa92cd5dbb1a", json=payload, headers=headers)
  if response.status_code == 400:
    print(f"Success : {response.status_code}")
  else:
    print(f"Error: {response.status_code}")

claim_transaction(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_transaction_update(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "claim/automated-transaction/620c7c619924a87c46042436", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")
claim_transaction_update(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_testing(token, url,):
  payload = {"query": "",
    "client": "",
    "fromDate": "",
    "toDate": "",
    "date" : "",
    "page": 1,
    "size": 1
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.post(url + "claim/claim-testing", json=payload, headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")
claim_testing(token=access_token(), url="https://dev-api.pttapp.com/api/")

def claim_search(token, url,):
  payload = {"fromDate": "2022-03-05",
    "toDate": "2022-11-04",
    "page":1,
    "size":10
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.post(url + "claim/search/summary_escrow", json=payload, headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")
claim_search(token=access_token(), url="https://dev-api.pttapp.com/api/")