import requests
from pprint import pprint


def get():
    response = requests.get('http://127.0.0.1:8000/address/')
    pprint(response.json())


def get():
    data = {
        "id": 2,
        "country": "Аргентина",
        "city": "Rivne",
        "zip_code": 33000,
        "street": "Orlova",
        "house_num": 45,
        "apartaments": 121
    }
    response = requests.post('http://127.0.0.1:8000/address/', data=data)
    pprint(response.json(), response.status_code)


if __name__ == '__main__':
    get()
