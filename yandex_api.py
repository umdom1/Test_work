import requests


def create_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = ''
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

    response = requests.put(f'{url}?path={path}', headers=headers)
    return response.status_code



