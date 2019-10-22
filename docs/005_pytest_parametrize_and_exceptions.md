## **Pytest - Parametrize**

Parameterizing of a test is done to run the test against multiple sets of inputs.

`@pytest.mark.parametrize`

```
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```

#### Parametrizing fixtures

```
import pytest
import smtplib


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()
```

---

## **Pytest - Exceptions**

In order to write assertions about raised exceptions, you can use pytest.raises as a context manager like this:

```
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

```
import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError):
        myfunc()
```

---
***[Next: Pytest Markers](006_pytest_markers.md)***