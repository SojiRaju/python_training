import requests
import json
import random


def access_token():
    # To get Access Token
    payload = {"username": "anisha", "password": "Anisha@12345"}
    url = "https://dev-api.pttapp.com/api/"
    response = requests.post(url + "login", json=payload)
    data = response.json()
    token = data["authenticationResult"]["AccessToken"]
    print(token)
    return token


access_token()


def lookup_anomalies(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/anomalies", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


lookup_anomalies(token=access_token(), url="https://dev-api.pttapp.com/api/")


def lookup_trust(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/trust-types", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


lookup_trust(token=access_token(), url="https://dev-api.pttapp.com/api/")


def claim_columns(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/claim-columns", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


claim_columns(token=access_token(), url="https://dev-api.pttapp.com/api/")


def default_checks(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/default-checks", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


default_checks(token=access_token(), url="https://dev-api.pttapp.com/api/")


def list_admin(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/list-admin", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


list_admin(token=access_token(), url="https://dev-api.pttapp.com/api/")


def list_client(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/list-client", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


list_client(token=access_token(), url="https://dev-api.pttapp.com/api/")


def claim_elements(token, url):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "lookup/claim-elements", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


claim_elements(token=access_token(), url="https://dev-api.pttapp.com/api/")
