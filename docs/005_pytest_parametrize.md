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
***[Next: Pytest Markers](006_pytest_markers.md)***