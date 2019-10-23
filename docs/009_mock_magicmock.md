## **Mock - MagicMock**

MagicMock is a subclass of Mock with all the magic methods pre-created and ready to use. These are the pre-created magic methods and its default values for MagicMock.


```
from unittest.mock import MagicMock

from core.managers import Client

self.marina = Client('Marina', 21, True)
self.marina.validate_age = mock.MagicMock(return_value=False)
assert not self.marina.validate_age()
```

### return_value

`self.joao.get_cupom = mock.MagicMock(return_value=1298)`


### side_effect

```
cupoms = [3490, 4545, 5655]

self.joao.get_cupom = mock.MagicMock(side_effect=cupoms)

self.joao.get_cupom()
```

### Decorators:

Patch:

mock.patch() takes a string which will be resolved to an object when applying the patch
```
@mock.patch('core.managers.Client.get_cupom', mock.MagicMock(return_value=1298))
def test_mock_patch_decorator(marina):
    assert marina.get_cupom() == 1298


@mock.patch('core.managers.Client.get_cupom')
def test_mock_patch_decorator_with_parameter(mocked, marina):
    mocked.return_value = 1298
    assert marina.get_cupom() == 1298
```

Patch.object:

mock.patch.object() takes a direct reference
```
@mock.patch.object(Client, 'get_cupom', 1298)
def test_mock_patch_object_decorator(marina):
    assert marina.get_cupom == 1298


@mock.patch.object(Client, 'get_cupom')
def test_mock_patch_object_decorator_with_parameter(mocked, marina):
    mocked.return_value = 1298
    assert marina.get_cupom() == 1298
```

---
***[Next: Mock API](010_mock_api.md)***