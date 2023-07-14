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

def anomalies_banking(token, url):
  payload = {
    "clientId": "1",
    "query": "str",
    "fromDate": "",
    "toDate": "",
    "page": "",
    "size": ""
}

  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  print(payload)
  response = requests.post(url + "anomaly/banking", json=payload, headers=headers)
  if response.status_code == 200:
    print(f"success: {response.json()}")

  else:
    print(f"Error: {response.status_code}")