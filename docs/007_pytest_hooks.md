## **Pytest - Hooks**

It is easy to implement local conftest plugins for your own project or pip-installable plugins that can be used throughout many projects, including third party projects. 

A plugin contains one or multiple hook functions. Writing hooks explains the basics and details of how you can write a hook function yourself. pytest implements all aspects of configuration, collection, running and reporting by calling well specified hooks.


#### Using commandline options

```
#conftest.py:
def pytest_addoption(parser):
    parser.addoption("--ci", action="store_true", default=False,
                    help="Indicate test are run on CI")


@pytest.fixture
def get_db(request):
    if request.config.getoption('--ci'):
        print(f'Run on CI: {request.config.getoption('--ci')}')
```

```
def test_get_db(get_db):
    pass
```