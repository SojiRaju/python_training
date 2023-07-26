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


def list_issue_log(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "issue-log?page=1&size=10&query=&status=&sortOrder=1&sortKey=dateResolved&priority=",
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


list_issue_log(token=access_token(), url="https://dev-api.pttapp.com/api/")


def create_issue_log(token, url):
    payload = {"clientId": "62fb53eb8af7efee9e56e08d",
               "opened": "string",
               "shortDescription": "string",
               "priority": "string",
               "resolutionNotes": "string",
               "status": "string",
               "dateResolved": "2022-1-1"
               }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    print(payload)
    response = requests.post(url + "issue-log", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"success: {response.json()}")

    else:
        print(f"Error: {response.status_code}")
