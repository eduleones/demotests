from unittest.case import TestCase


def add(x, y):
    return x + y


class MyTest(TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_float(self):
        self.assertIsInstance(add(10.32, 7.3), float)
