import requests
import json
import random


def access_token():
    # To get Access Token
    payload = {"username": "nismal", "password": "Simple2022$"}
    url = "https://dev-api.pttapp.com/api/"
    response = requests.post(url + "login", json=payload)
    data = response.json()
    token = data["authenticationResult"]["AccessToken"]
    print(token)
    return token


access_token()


def basic_info(token, url):
    # Generate a random number for ID
    cId = random.randint(1004, 9999)  # Replace the range with desired values
    print("Random ID:", cId)
    payload = {
        "friendlyName": f"ApiTest_{cId}",
        "fullName": f"ApiTest00_{cId}",
        "typeOfTrustAccount": "61ef4e0da0d0ef7c56884319",
        "cId": f"_{cId}",
        "existingClient": "false",
        "create": "true",
        "goLiveDate": "2021-10-02",
        "reuseOldBooking": "false",
        "additionChecks": [],
        "address": {
            "line1": "",
            "line2": "",
            "line3": "",
            "town": "pta",
            "country": "ind",
            "postcode": ""
        },
        "limits": [{
            "totalAnnualRevenue": 12,
            "maximumNoOfClaims": 1,
            "currency": "EUR"
        }, {
            "totalAnnualRevenue": 100,
            "maximumNoOfClaims": 2,
            "currency": "USD"
        }],
        "frequency": [
            "61ee2f1dcf10b991afdaf54a"
        ],
        "email": "abbc@122334.com",
        "pointOfContact": ""}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/basic-info", json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        client_id = data["clientId"]
        return client_id
    else:
        print(f"Error: {response.status_code}")
        print(response.json())


basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/")
