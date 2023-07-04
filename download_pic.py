import requests
import pytest

def download_picture(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False

@pytest.mark.parametrize('url, filename', [
    ('https://amazon.com/image1.jpg', 'image1.jpg'),
    ('https://amazon.com/image2.png', 'image2.png'),
    # Add more URLs and filenames as needed
])
def test_download_picture(url, filename):
    assert download_picture(url, filename) is True

