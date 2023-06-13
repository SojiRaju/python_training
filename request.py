import re
import requests


def test_get_api_endpoint():
    url = "https://reqres.in/api/users/2"  # Replace with the desired API endpoint URL

    response = requests.get(url)
    response_data = response.json()
    # Assuming you want to compare the first user object
    user_data = response_data["data"]
    print(user_data)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response data matches the expected data
    assert user_data["id"] == 2
    assert user_data["first_name"] == "Janet"
    assert user_data["last_name"] == "Weaver"
    # Assert that the avatar is a valid image URL using a regular expression pattern
    avatar_url = user_data["avatar"]
    image_url_pattern = r"https?://.*\.(?:png|jpg|jpeg|gif|bmp)"
    assert re.match(image_url_pattern, avatar_url) is not None
    # Assert that the email is a valid email address using a regular expression pattern
    email_address = user_data["email"]
    email_pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    assert re.match(email_pattern, email_address) is not None


test_get_api_endpoint()