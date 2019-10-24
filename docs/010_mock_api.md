## **Mock - API**

API Function:

```
def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'

    response = requests.get(url)
    return response.json()
```

Test:
```
def test_get_pokemon_pikachu():
    response = get_pokemon('pikachu')
    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)
```

### Using only mock

```
@mock.patch('core.managers.get_pokemon')
def test_get_pokemon_pikachu_mocked(mocked):
    mocked.return_value = json_pikachu

    response = get_pokemon('pikachu')
    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)    
```

### Using lib VCRpy

`https://github.com/kevin1024/vcrpy`

```
@vcr.use_cassette('recorded/test_get_pokemon_pikachu_with_vcrpy.yaml')
def test_get_pokemon_pikachu_with_vcrpy():
    response = get_pokemon('pikachu')

    assert response['base_experience'] == 112
    assert isinstance(response['abilities'], list)
```

### Testing error with responses

`https://github.com/getsentry/responses`

```
@responses.activate
def test_get_pokemon_pikachu_not_found():
    responses.add(
        responses.GET,
        'https://pokeapi.co/api/v2/pokemon/pikachu/',
        json={'error': 'not found'}, status=404
    )

    with pytest.raises(GetPokemonNotFoundError):
        get_pokemon('pikachu')


@responses.activate
def test_get_pokemon_pikachu_not_found():
    responses.add(
        responses.GET,
        'https://pokeapi.co/api/v2/pokemon/pikachu/',
        json={'error': 'generic'}, status=500
    )

    with pytest.raises(GetPokemonGenericError):
        get_pokemon('pikachu')
```

### With asyncio

```
from asyncio import coroutine
from unittest.mock import patch, Mock
 

async def test_audiences_comm_ab_test(
    self, comm_ab_test, mock_response_payload
):
    with patch.object(
        self.backend, 'get_response_ab_test'
    ) as get_mock:
        coro = Mock(
            name="CoroutineResult",
            return_value=mock_response_payload,
        )
        get_mock.side_effect = coroutine(coro)
        comm = await self.backend.get_audience(comm_ab_test)

    assert isinstance(comm.customers, list)
    assert len(comm.customers) == 1000000
```

---
***[Next: Load Testing](011_load_testing.md)***