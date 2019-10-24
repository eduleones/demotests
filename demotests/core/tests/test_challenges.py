import pytest
import statistics
from unittest.mock import patch

from core.managers import get_github_user

"""
1 - Finding the median of a list
"""


def median(_list):
    return statistics.median(_list)


@pytest.mark.parametrize(
    "_list,result",
    [
        ([19, 46, 21, 18, 30], 21),
        ([39, 20.2, 112, 78, 88], 78),
        ([2.2, 1.9, 2.6, 1.8, 2.9, 1.5, 2.5], 2.2),
    ],
)
def test_median(_list, result):
    assert median(_list) == result


"""
2 - Write the algorithm for the test
"""


def sum_fist_and_last(e):
    if isinstance(e, list):
        return (e[0] + e[-1]) * 2
    else:
        raise NotImplementedError


def test_sum_fist_and_last_element():
    assert sum_fist_and_last(['dog', 'cat', 'duck']) == 'dogduckdogduck'
    assert sum_fist_and_last([33, 45, 6, 65, 1, 34, 78]) == 222

    with pytest.raises(TypeError):
        sum_fist_and_last(['dog', 6, 'cat', 4])

    with pytest.raises(NotImplementedError):
        sum_fist_and_last({'dog': 6, 'cat': 4})


"""
3 - Create test with mock
"""

@patch('core.managers.get_github_user')
def test_get_github_user(mock_get, mock_dafiti_json):
    mock_get.return_value = mock_dafiti_json
    response = get_github_user('dafiti')

    assert response['login'] == 'dafiti'
    assert response['id'] == 5245637