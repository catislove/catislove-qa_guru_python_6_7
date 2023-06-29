import os.path

import requests

# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
url = 'https://selenium.dev/images/selenium_logo_square_green.png'


def test_download_file_with_requests():
    response = requests.get(url)
    downloaded_request = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'selenium_logo.png')
    with open(downloaded_request, 'wb') as file:
        file.write(response.content)

    assert os.path.getsize(downloaded_request) == 30803