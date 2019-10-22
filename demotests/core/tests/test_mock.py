import os

import pytest
from unittest import mock

from core.managers import Client, get_pokemon


def test_validate_age(marina):
    assert marina.validate_age()

def test_error_in_validate_age_with_mock(marina):
    marina.validate_age = mock.MagicMock(return_value=False)

    assert not marina.validate_age()

def test_get_cupom_with_mock_side_effect(joao):
    cupoms = [3490, 4545, 5655]

    joao.get_cupom = mock.MagicMock(side_effect=cupoms)

    for cupom in cupoms:
        assert joao.get_cupom() == cupom


@mock.patch('os.listdir', mock.MagicMock(return_value='C:/'))
def test_mock_patch_decorator():
    assert os.listdir() == 'C:/'


@mock.patch.object(Client, 'get_cupom', mock.MagicMock(return_value='1298'))
def test_mock_patch_decorator(marina):
    assert marina.get_cupom() ==  '1298'


def test_get_pokemon_pikachu():
    response = get_pokemon('pikachu')
    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)