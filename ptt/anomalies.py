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
        "clientId": "62fb53eb8af7efee9e56e08d",
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


anomalies_banking(token=access_token(), url="https://dev-api.pttapp.com/api/")


def anomalies_claim(token, url):
    payload = {
        "clientId": "62fb53eb8af7efee9e56e08d",
        "query": "",
        "fromDate": "",
        "toDate": "",
        "page": "",
        "size": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "anomaly/claims", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


anomalies_claim(token=access_token(), url="https://dev-api.pttapp.com/api/")


def anomalies_banking_export(token, url):
    payload = {
        "clientId": "62fb53eb8af7efee9e56e08d",
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
    response = requests.post(url + "anomaly/banking/export", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


anomalies_banking_export(token=access_token(), url="https://dev-api.pttapp.com/api/")


def anomalies_claim_export(token, url):
    payload = {
        "clientId": "62fb53eb8af7efee9e56e08d",
        "query": "",
        "fromDate": "",
        "toDate": "",
        "page": "",
        "size": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "anomaly/claims/export", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


anomalies_claim_export(token=access_token(), url="https://dev-api.pttapp.com/api/")


def anomaly_status_update(token, url):
    payload = {
        "anomalyId": "62fb53eb8af7efee9e56e08d",
        "status": "done"
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "anomaly/claim/update-status", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success : {response.json()}")
    else:
        print(f"Error: {response.status_code}")


anomaly_status_update(token=access_token(), url="https://dev-api.pttapp.com/api/")
