import pytest

from ..primes import is_prime


def func_multi_a(x):
    return 'a' * x


def test_func_aaa_with_1():
    assert func_multi_a(1)


def test_func_aaa_with_3():
    assert func_multi_a(3) == 'aaa'


# With parametrize
@pytest.mark.parametrize(
    'number, expected', [(1, 'a'), (3, 'aaa'), (5, 'aaaaa'), (10, 'aaaaaaaaaa')]
)
def test_func_multi_a(number, expected):
    assert func_multi_a(number) == expected


# Test is_prime
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


@pytest.mark.parametrize('n', [2, 3, 5, 13])
def test_is_prime_with_parameterized(n):
    assert is_prime(n)


@pytest.mark.parametrize('n', [4, 6, 9, 15])
def test_is_not_prime_with_parameterized(n):
    assert not is_prime(n)


# Exceptions
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
