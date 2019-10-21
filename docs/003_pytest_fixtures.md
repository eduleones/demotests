## **Pytest - Fixtures**

Fixtures are functions, which will run before each test function to which it is applied. 

``` 
import pytest  

@pytest.fixture
def smtp():
	import smtplib
	return smtplib.SMTP("smtp.gmail.com")

def test_ehlo(smtp):
	response, msg = smtp.ehlo()
	assert response == 250
	assert 0 # for demo purposes
```

**Scope:** module, function, session
```
import pytest

class App:
def __init__(self, smtp):
    self.smtp = smtp

@pytest.fixture(scope="module")
def app(smtp):
    return App(smtp)

def test_smtp_exists(app):
    assert app.smtp

```

```
@pytest.fixture(scope="session")
def smtp():
	import smtplib
	return smtplib.SMTP("smtp.gmail.com")
```
 **Autouse**

```
@pytest.fixture(autouse=True)
def transact(self, request, db):
	db.begin(request.function.__name__)
	request.addfinalizer(db.rollback)
```

---
***[Next: Pytest Confest / Setup & Teardown](004_pytest_conftest_and_setup.md)***