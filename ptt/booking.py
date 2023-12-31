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


def booking_claims(token, url):
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "HAY-3739474",
        "query": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }

    response = requests.post(url + "booking/claims", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


booking_claims(token=access_token(), url="https://dev-api.pttapp.com/api/")


def booking_anomalies(token, url):
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "HAY-3739474",
        "query": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }

    response = requests.post(url + "booking/anomalies", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


booking_anomalies(token=access_token(), url="https://dev-api.pttapp.com/api/")


def booking_payments(token, url):
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "bookingReference": "3669195",
        "query": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }

    response = requests.post(url + "booking/payments", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


booking_payments(token=access_token(), url="https://dev-api.pttapp.com/api/")


def booking_search(token, url):
    payload = {
        "clientId": "634fb054474a06e0a8c54b97",
        "bookingReference": "20261725"
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.post(url + "booking/search", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


booking_search(token=access_token(), url="https://dev-api.pttapp.com/api/")


def booking_claims_checks(token, url):
    payload = {
        "clientId": "635132a4dc29b4bad9e74d90",
        "transactionId": "61f3614d14dfe6ab93037177"
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }

    response = requests.post(url + "booking/claim-checks", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")


booking_claims_checks(token=access_token(), url="https://dev-api.pttapp.com/api/")
