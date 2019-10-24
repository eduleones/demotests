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


@pytest.fixture
def mock_dafiti_json():
    return """
    {
        "login": "dafiti",
        "id": 5245637,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjUyNDU2Mzc=",
        "avatar_url": "https://avatars0.githubusercontent.com/u/5245637?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dafiti",
        "html_url": "https://github.com/dafiti",
        "followers_url": "https://api.github.com/users/dafiti/followers",
        "following_url": "https://api.github.com/users/dafiti/following{/other_user}",
        "gists_url": "https://api.github.com/users/dafiti/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dafiti/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dafiti/subscriptions",
        "organizations_url": "https://api.github.com/users/dafiti/orgs",
        "repos_url": "https://api.github.com/users/dafiti/repos",
        "events_url": "https://api.github.com/users/dafiti/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dafiti/received_events",
        "type": "Organization",
        "site_admin": false,
        "name": "Dafiti OpenSource",
        "company": null,
        "blog": "http://www.dafiti.com.br",
        "location": "Sao Paulo",
        "email": null,
        "hireable": null,
        "bio": "Dafiti",
        "public_repos": 41,
        "public_gists": 0,
        "followers": 0,
        "following": 0,
        "created_at": "2013-08-16T15:29:42Z",
        "updated_at": "2019-06-05T05:13:51Z"
    }
    """
