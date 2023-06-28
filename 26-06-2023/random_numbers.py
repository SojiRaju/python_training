import json
import random
from asyncore import read

import pytest
import requests

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


def access_token():
  pass


basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/")


def step2(token, url, client_id):
    print(client_id)
    payload = {
        "clientId": f"{client_id}",
        "data": [
            {
                "bankName": "updated",
                "accountNumber": "string",
                "sortCode": "string",
                "currency": "string",
                "iban": "47548"
            },
            {
                "bankName": "updated",
                "accountNumber": "string",
                "sortCode": "string",
                "currency": "string",
                "iban": "5755"
            }
        ]
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/bank-account", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


step2(token=access_token(), url="https://dev-api.pttapp.com/api/",
      client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def step3(token, url, client_id):
    print(client_id)
    payload = {
        "clientId": f"{client_id}",
        "insurance": [
            {
                "policyNumber": "222",
                "provider": "ABCD",
                "files": [
                    "be761366-9579-4e0d-890b-8ab1e6b82dfh"
                ],
                "supplierListFile": "be761366-9579-4e0d-890b-8ab1e6b82dhj",
                "expiryDate": "2025-02-02"
            },
            {
                "policyNumber": "224",
                "provider": "ABC",
                "files": [
                    "be761366-9579-4e0d-890b-8ab1e6b82d3a",
                    "be761366-9579-4e0d-890b-8ab1e6b82dgh"
                ],
                "expiryDate": "2024-02-07"
            }
        ],
        "atol": [
            {
                "license": "222",
                "startDate": "2020-02-02",
                "files": [
                    "be761366-9579-4e0d-890b-8ab1e6b82dfh",
                    "be761366-9579-4e0d-890b-8ab1e6b82dhj"
                ],
                "expiryDate": "2025-02-02"
            }
        ]
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/insurance-and-atol", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success Insurance-and-atol added : {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


step3(token=access_token(), url="https://dev-api.pttapp.com/api/",
      client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def anomalies_step4(token, url, client_id):
    print(client_id)
    payload = {
        "clientId": f"{client_id}",
        "anomalies": [
            {
                "anomalyId": "11ef4bff0a719ab106fdc14e"
            },
            {
                "anomalyId": "11ef4bff0a719ab106fdc14e",
                "customFieldValue": 34
            }
        ]
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/anomalies", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success anomalies added : {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


anomalies_step4(token=access_token(), url="https://dev-api.pttapp.com/api/",
                client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def banking_columns_step5(token, url, client_id):
    print(client_id)
    payload = {
        "clientId": f"{client_id}",
        "columns": ["61efc57260cc72bf21f1c441"]
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/banking-columns", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success banking-columns added : {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


banking_columns_step5(token=access_token(), url="https://dev-api.pttapp.com/api/",
                      client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def claim_columns_step6(token, url, client_id):
    print(client_id)
    payload = {
        "clientId": f"{client_id}",
        "columns": ["61efcfb8466aef6133536960"],
        "status": "string"
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.put(url + "client/claim-columns", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success claim-columns added : {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


claim_columns_step6(token=access_token(), url="https://dev-api.pttapp.com/api/",
                    client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def client_details(token, url, client_id):
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + f"client/{client_id}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Pretty-print the JSON response
        formatted_json = json.dumps(data, indent=4)
        # Print the formatted JSON
        print(f"client details is: {formatted_json}")
    else:
        print(f"Error: {response.status_code}")


client_details(token=access_token(), url="https://dev-api.pttapp.com/api/",
               client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))

def trust_balance(token, url, client_id):

    payload = {
        "client": f"{client_id}",
        "page": "",
        "size": "",
        "currency": "GBP"
    }

    print(payload)
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "reports/trust-balance?", json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Pretty-print the JSON response
        formatted_json = json.dumps(data, indent=4)
        # Print the formatted JSON
        print(f"trust_balance is: {formatted_json}")

    else:
        print(f"Error: {response.status_code}")
trust_balance(token=access_token(), url="https://dev-api.pttapp.com/api/", client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def trust_balance_export(token, url, client_id):

    payload = {
        "client": f"{client_id}",
        "page": "",
        "size": "",
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "reports/trust-balance/export?", json=payload, headers=headers)
    if response.status_code == 202:
        data = response.json()
        print(data)

    else:
        print(f"Error: {response.status_code}")
        data = response.json()
        print(data)
trust_balance_export(token=access_token(), url="https://dev-api.pttapp.com/api/", client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def client_file_report(token, url, client_id):

    payload = {
        "client": f"{client_id}",
        "fromDate": "2022-02-24",
        "toDate": "2022-02-24",
        "page": "",
        "size": ""
    }

    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "reports/client-files?", json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Pretty-print the JSON response
        formatted_json = json.dumps(data, indent=4)
        # Print the formatted JSON
        print(f"client_file_report is: {formatted_json}")

    else:
        print(f"Error: {response.status_code}")
client_file_report(token=access_token(), url="https://dev-api.pttapp.com/api/", client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


def client_file_export(token, url, client_id):

    payload = {
        "client": f"{client_id}",
        "fromDate": "2022-02-24",
        "toDate": "2022-02-24",
        "page": "",
        "size": ""
    }
    headers = {
        'Authorization': f'Bearer {access_token()}'
    }
    response = requests.get(url + "reports/client-files/export?", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Success: {response.status_code}")

    else:
        print(f"Error: {response.status_code}")
        data = response.json()
        print(data)
client_file_export(token=access_token(), url="https://dev-api.pttapp.com/api/", client_id=basic_info(token=access_token(), url="https://dev-api.pttapp.com/api/"))


