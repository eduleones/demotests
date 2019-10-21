import pytest
import sys


@pytest.mark.skip(reason="no way of currently testing this")
def test_type_string():
    assert isinstance('hello', str)


@pytest.mark.skipif(
    sys.version_info < (3, 6), reason="requires python3.6 or higher"
)
def test_type_string():
    assert isinstance('hello', str)


@pytest.mark.xfail
def test_type():
    assert isinstance('hello', int)


@pytest.mark.skip
@pytest.mark.linux
def test_os_systems():
    print(
        """
            ,d                             
            88                             
            MM88MMM 88       88 8b,     ,d8  
            88    88       88  `Y8, ,8P'   
            88    88       88    )888(     
            88,   "8a,   ,a88  ,d8" "8b,   
            "Y888  `"YbbdP'Y8 8P'     `Y8  
    """
    )
    linux = 10
    windows = 0
    assert linux > windows



# UsingMarks
@pytest.mark.redis_db(2)
def test_connect_redis(redis_client):
    print(redis_client)
    pass