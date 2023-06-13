import pytest
import requests


def test_get_endpoint():
    url = 'https://api.example.com/endpoint'

    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response content type is JSON
    assert response.headers['Content-Type'] == 'application/json'

    # Add more assertions to validate the response data, if needed
    # For example, you can assert specific values in the response JSON

    # Example assertion: Assert that the 'status' key in the response JSON is 'success'
    response_json = response.json()
    assert response_json['status'] == 'success'
