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


def get_presigned_url(token, url, client_id):
  payload = {
    "clientId": f"{client_id}",
    "fileName": "20221205-XYZ-Banking_2",
  }
  headers = {
    'Authorization': f'Bearer {access_token()}'
  }
  response = requests.get(url + "banking/upload/presigned-url", params=payload, headers=headers)
  if response.status_code == 200:
    data = response.json()
    presignedUrl = data["presignedUrl"]
    fileId = data['fileId']
  assert response.status_code == 200

  response = requests.put(presignedUrl, headers={"Content-Type": "application/vnd.ms-excel"})
  if response.status_code == 200:
    print("presignedUrl is posted")

  payload ={
    "clientId": client_id,
    "fileName": "20221205-XYZ-Banking_2",
    "fileId": fileId,
    "claimFromTBR": "false"
  }
  response = requests.post(url + "banking/upload", json=payload, headers=headers)
  if response.status_code == 201:
    print("Banking Upload success")
  else:
    print("Banking upload failed")
    print(response)
  else:
    print("error in post presignedurl")

  else:
    print(f"Error in get_presigned_url: {response.status_code}")
    data = response.json()
  print(data)
get_presigned_url(token=access_token(), url=url, client_id=pttapi.basic_nfo(token=access_token(), url=url))