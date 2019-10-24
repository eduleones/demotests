## **Challenges**

**1** - Finding the median of a list

| Input  | Output  |
|---|---|
|  [19, 46, 21, 18, 30] | 21  |
|  [39, 20.2, 112, 78, 88] | 78   |
|  [2.2, 1.9, 2.6, 1.8, 2.9, 1.5, 2.5]  | 2.2  |

**TDD - Writing the tests first**

---

**2** - Write the algorithm for the test:

```
def test_sum_fist_and_last_element():
    assert sum_fist_and_last(['dog', 'cat', 'duck']) == 'dogduckdogduck'
    assert sum_fist_and_last([33, 45, 6, 65, 1, 34, 78]) == 222

    with pytest.raises(TypeError):
        sum_fist_last(['dog', 6, 'cat', 4])

    with pytest.raises(NotImplementedError):
        sum_fist_last({'dog': 6, 'cat': 4})  
```

**3** - Create test with mock:

```
def get_github_user(user):
    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    return response.json()
```
