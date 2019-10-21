## **What is PyTest?**

Pytest is a testing framework which allows us to write test codes using python. You can write code to test anything like database , API, even UI if you want. But pytest is mainly being used in industry to write tests for APIs.

**Why use PyTest?**

*   Very easy to start with because of its simple and easy syntax.
    
*   Can run tests in parallel.
    
*   Can run a specific test or a subset of tests
    
*   Automatically detect tests
    * test_*.py or *_test.py
    
*   Skip tests
    
*   Open source


---

### Install:

`pip install pytest`

### Configure:


```
pytest.ini:
        [pytest]
        markers =
            slow: marks tests as slow
            serial
        env =
            DB_PASS_TEST='kllsjfu949'
            D:TESTING=True     

```

### Run:
`py.test [options] [file_or_dir]`


---
***[Next: Pytest vs Unittest](002_pytest_vs_unittest.md)***