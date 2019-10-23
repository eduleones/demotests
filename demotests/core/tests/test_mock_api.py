from unittest import mock
import pytest
import responses
import vcr

from core.managers import get_pokemon
from core.exceptions import GetPokemonNotFoundError, GetPokemonGenericError

from .json_responses import json_pikachu


def test_get_pokemon_pikachu():
    response = get_pokemon('pikachu')

    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)


@mock.patch('core.managers.get_pokemon')
def test_get_pokemon_pikachu_mocked(mocked):
    mocked.return_value = json_pikachu

    response = get_pokemon('pikachu')
    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)


@vcr.use_cassette('recorded/test_get_pokemon_pikachu_with_vcrpy.yaml')
def test_get_pokemon_pikachu_with_vcrpy():
    response = get_pokemon('pikachu')

    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)


@responses.activate
def test_get_pokemon_pikachu_not_found():
    responses.add(
        responses.GET,
        'https://pokeapi.co/api/v2/pokemon/pikachu/',
        json={'error': 'not found'},
        status=404,
    )

    with pytest.raises(GetPokemonNotFoundError):
        get_pokemon('pikachu')


@responses.activate
def test_get_pokemon_pikachu_not_found():
    responses.add(
        responses.GET,
        'https://pokeapi.co/api/v2/pokemon/pikachu/',
        json={'error': 'generic'},
        status=500,
    )

    with pytest.raises(GetPokemonGenericError):
        get_pokemon('pikachu')
