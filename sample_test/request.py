import requests


def test_get_api_endpoint():
    url = "https://reqres.in/api/users?page=2"  # Replace with your API endpoint URL
    response = requests.get(url)
    print(response.content)
