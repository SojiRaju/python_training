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

def trust_balance_report(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "reports/trust-balance?client=62fb53eb8af7efee9e56e08d&page=&size=&currency=GBP", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


trust_balance_report(token=access_token(), url="https://dev-api.pttapp.com/api/")


def trust_balance_report_export(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "reports/trust-balance/export?client=62fb53eb8af7efee9e56e08d&page=1&size=10", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


trust_balance_report_export(token=access_token(), url="https://dev-api.pttapp.com/api/")


def client_files_report(token, url):
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "reports/client-files?client=62fb53eb8af7efee9e56e08d&fromDate=2022-02-24&toDate=2022-02-24&page=1&size=3", headers=headers)
  if response.status_code == 200:
    data = response.json()
    print(data)
  else:
    print(f"Error: {response.status_code}")


client_files_report(token=access_token(), url="https://dev-api.pttapp.com/api/")