## **Pytest - conftest**

We can define the fixture functions in this file to make them accessible across multiple test files.

``` 
conftest.py:
	import pytest 

	@pytest.fixture 
	def input_value(): 
		return 39
```

```
test_div_by_3_6.py:
	import pytest

	def test_divisible_by_3(input_value):
		assert input_value %  3  ==  0

	@pytest.mark.usefixtures("input_value")
	def test_divisible_by_6():  
		assert input_value %  6  ==  0
```



## **Setup / Teardown**

```
class Test:
	def setup(self):
		self.redis = redis.connect()

	...

	def teardown(self)
		self.redis.close()
```

with fixtures:

```
@pytest.fixture(scope="module")
def redis():
	redis = redis.connect()
	yield redis
	redis.close()
```



---
***[Next: Pytest Parametrize](005_pytest_parametrize.md)***
