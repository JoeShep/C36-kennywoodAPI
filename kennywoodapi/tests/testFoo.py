import unittest
from unittest import skip
from django.test import TestCase

class TestFoo(TestCase):
    @skip
    def test_foo(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()
