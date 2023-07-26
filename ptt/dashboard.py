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


def ytd_client(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "dashboard/clients?year=2022", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


ytd_client(token=access_token(), url="https://dev-api.pttapp.com/api/")


def dashboard_details(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "dashboard/details?currency=EUR", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


dashboard_details(token=access_token(), url="https://dev-api.pttapp.com/api/")


def clients_category(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "dashboard/clients-category", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


clients_category(token=access_token(), url="https://dev-api.pttapp.com/api/")


def upload_transactions(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "dashboard/uploaded-transactions?fromDate=2023-01-01&toDate=2023-01-12&client=",
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


upload_transactions(token=access_token(), url="https://dev-api.pttapp.com/api/")
