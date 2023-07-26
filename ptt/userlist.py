import requests


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


# check only failure condition

def change_password(token, url):
    payload = {"currentPassword": "Simple@2022$", "password": "Simple@2022$1"}
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "change-password", json=payload, headers=headers)
    if response.status_code == 403:
        print(f"success: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


change_password(token=access_token(), url="https://dev-api.pttapp.com/api/")
