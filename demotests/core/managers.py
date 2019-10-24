import random

import requests

from core.exceptions import GetPokemonNotFoundError, GetPokemonGenericError


class Client:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def get_cupom(self):
        cupom = random.randint(1000, 9999)
        return cupom

    def validate_age(self):
        if self.age < 18:
            return False
        else:
            return True


def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise GetPokemonNotFoundError
    else:
        raise GetPokemonGenericError


def get_github_user(user):
    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    return response.json()