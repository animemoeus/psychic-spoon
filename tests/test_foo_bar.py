import unittest

from .utils import is_prime


def foo_bar():
    for i in range(1, 100 + 1)[::-1]:
        if is_prime(i):
            continue

        if i % 3 == 0 and i % 5 == 0:
            print("FooBar", end=", ")
        elif i % 3 == 0:
            print("Foo", end=", ")
        elif i % 5 == 0:
            print("Bar", end=", ")
        else:
            print(i, end=", ")


class TestFooBar(unittest.TestCase):
    def test_foo_bar(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(11), True)

        print(foo_bar())
