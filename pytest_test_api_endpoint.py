import requests


def test_get_api_endpoint():
  url = "https://reqres.in/api/users?page=2" # Replace with your API endpoint URL
  response = requests.get(url)
  response_data = response.json()
  user_data = response_data["data"][0] # Assuming you want to compare the first user object

  # Print the response status code
  print("Response Status Code:", response.status_code)

  # Print the response content (data)
  print("Response Content:", response.content)

  # Print the response JSON data
  print("Response JSON Data:", response_data)

  # Print the expected data
  expected_data = {"first_name": "Michael", "last_name": "Lawson"} # Replace with your expected data
  print("Expected Data:", expected_data)

  # Assert that the response status code is 200 (OK)
  assert response.status_code == 200

  # Assert that the response contains the expected data
  assert user_data["first_name"] == expected_data["first_name"]
  assert user_data["last_name"] == expected_data["last_name"]


test_get_api_endpoint()

