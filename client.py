import requests
from pprint import pprint


def get():
    response = requests.get('http://127.0.0.1:8000/address/')
    pprint(response.json())


def post():
    data = {'apartaments': 34,
            'city': 'Рівне',
            'country': 'Україна',
            'house_num': 46,
            'street': 'Київська',
            'zip_code': 33027}
    response = requests.post('http://127.0.0.1:8000/address/',
                             data=data)
    print(response.json(), response.status_code)


def update():
    data = {'apartaments': 34,
            'city': 'Рівне',
            'country': 'Україна',
            'house_num': 46,
            'street': 'Київська',
            'zip_code': 33027}
    response = requests.put('http://127.0.0.1:8000/address/',
                            data=data)
    print(response.json(), response.status_code)


def delete():
    response = requests.delete('http://127.0.0.1:8000/address/')
    print(response.status_code)


if __name__ == "__main__":
    # post()
    # get()
    # update()
    # delete()
    pass
