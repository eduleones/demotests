## **Pytest - Markers**

By using the pytest.mark helper you can easily set metadata on your test functions. There are some builtin markers, for example:

* **skip** - always skip a test function
* **skipif** - skip a test function if a certain condition
* **xfail** - mark test functions as expected to fail
* **parametrize** 

#### skip

```
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...
```

#### skipif

```
@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function(self):
        "Windows? :) Linux > Microsoft"
        ...
```

#### xfail

```
@pytest.mark.xfail
def test_type():
    assert isinstance('hello', int)
```

---

### Custom Markers

You can “mark” a test function with custom metadata like this:

```
@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app
```
run mark:

```
py.test -m webtest
```

#### Registering markers

```
pytest.ini:
    [pytest]
    markers =
        hello: mark a test as a hello.
```
`py.test --markers`

#### Using Marks from Fixtures

```
conftest.py:
    @pytest.fixture
    def redis_client(request):
        marker = request.node.get_closest_marker('redis_db')

        if not marker:
            db = 0
        else:
            db = marker.args[0]
        return f"Redis connect in DB {db}"
```

```
@pytest.mark.redis_db(2)
def test_connect_redis(redis_client):
    print(redis_client)
    pass
```

---
***[Next: Pytest Hooks](007_pytest_hooks.md)***