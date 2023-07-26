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


def banking_anomalies(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(
        url + "banking/anomalies/625f965bc4b57cdb24ef5e4b?query=&sortKey=status&sortOrder=1&page=&size=",
        headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


banking_anomalies(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_anomalies_export(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "banking/anomalies/625f965bc4b57cdb24ef5e4b/export?query=&sortKey=status&sortOrder=1",
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


banking_anomalies_export(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_payments_export(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "banking/payments/625f9719c4b57cdb24ef5e4d/export?query=&sortKey=&sortOrder=",
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


banking_payments_export(token=access_token(), url="https://dev-api.pttapp.com/api/")


def banking_get_transaction(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "banking/get-transaction/623c1a34a93d253120cb3fc0", headers=headers)
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
    response = requests.get(
        url + "banking/get-transaction?supplierName=f0be81e0-72a5-4234-92ad-85f5a9292&clientId=62fb53eb8af7efee9e56e08d",
        headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


banking_get_transaction_suppliername(token=access_token(), url="https://dev-api.pttapp.com/api/")
