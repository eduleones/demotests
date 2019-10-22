import pytest

from core.managers import Client

@pytest.fixture
def content_payload():
    return {
        "name": "Campanha dias dos país - 2019",
        "tag": "T38470-283728",
        "url": "http://dafiti.com.br/dia-dos-pais/",
        "content_type": "cp",
        "gender": "m",
        "goal": "awar",
        "is_active": "True",
    }


@pytest.fixture
def content_invalid_payload():
    return {
        "name": "Campanha dias dos país - 2019",
        "tag": "T38470-283728",
        "url": "dia-dos-pais/",
        "content_type": "cp",
        "gender": "m",
        "goal": "awar",
        "is_active": "True",
    }


@pytest.fixture
def content_payload_partial():
    return {"name": "Partial Name"}


@pytest.fixture
def banner_payload():
    return {"description": "Banner principal", "is_active": True}


@pytest.fixture
def marina():
    return Client('Marina', 21, True)

@pytest.fixture
def joao():
    return Client('João', 28, False)