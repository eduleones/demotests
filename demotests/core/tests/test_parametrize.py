import pytest

from ..primes import is_prime


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


@pytest.mark.parametrize('n', [2, 3, 5, 13])
def test_is_prime_with_parameterized(n):
    assert is_prime(n)


@pytest.mark.parametrize('n', [4, 6, 9, 15])
def test_is_prime_with_parameterized(n):
    assert not is_prime(n)
