import pytest

# Custom Marker
@pytest.fixture
def redis_client(request):
    marker = request.node.get_closest_marker('redis_db')

    if not marker:
        db = 0
    else:
        db = marker.args[0]
    return f"Redis connect in DB {db}"


# Hook commandline
def pytest_addoption(parser):
    parser.addoption(
        "--ci",
        action="store_true",
        default=False,
        help="Indicate test are run on CI",
    )


@pytest.fixture
def get_db(request):
    option = request.config.getoption('--ci')
    if option:
        print(f'Run on CI: {option}')
