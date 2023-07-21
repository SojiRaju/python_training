import requests
def access_token():
  # To get Access Token
  payload = {"username": "nithin", "password": "Simple2022$"}
  url = "https://dev-api.pttapp.com/api/"
  response = requests.post(url + "login", json=payload)
  data = response.json()
  token = data["authenticationResult"]["AccessToken"]
  return token
access_token()

def banking_search(token, url):
  payload = {
    "query": "",
    "client": "634fb054474a06e0a8c54b97",
    "assignedTo": "",
    "fromDate": "2020-03-12",
    "toDate": "2024-03-12",
    "status": "",
    "date": "",
    "page": 1,
    "size": 10
  }

  headers = {
    'Authorization': f'Bearer {access_token()}'
  }

  response = requests.post(url + "banking/search", json=payload, headers=headers)
  if response.status_code == 200:
    print(f"success: {response.json()}")

  else:
    print(f"Error: {response.status_code}")

banking_search(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_details(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/details/64b8fb5bd8977cadb2f8b94b", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


banking_details(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_payments(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/payments/64b8fb5bd8977cadb2f8b94b?query=&page=&size=18&sortKey=currencyCode&sortOrder=1", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


banking_payments(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_anomalies(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/anomalies/64b8fb5bd8977cadb2f8b94b?query=&sortKey=status&sortOrder=1&page=&size=", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


banking_anomalies(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_get_transaction(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/get-transaction/63c67c01eec134a363cf42c1", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


banking_get_transaction(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_get_transaction_suppliername(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/get-transaction?supplierName=Edstem, Nithin&clientId=634fb054474a06e0a8c54b97", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


banking_get_transaction_suppliername(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_update(token, url):
  payload ={
  "bankingId": "64b8fb5bd8977cadb2f8b94b",
  "notes": "string1",
  "status": "string",
  "assignedTo": "6204d9d61eed04813999f227"
  }

  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.put(url + "banking/update", json=payload, headers=headers)
  if response.status_code == 200:
    print(f"Success : {response.json()}")
  else:
    print(f"Error: {response.status_code}")

banking_update(token=access_token(), url="https://dev-api.pttapp.com/api/")

