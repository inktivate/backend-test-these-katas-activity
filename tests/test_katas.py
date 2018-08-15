import unittest
from katas import *


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(45, 69), 114)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 19), 76)
        self.assertEqual(multiply(-1, 0), 0)
        self.assertEqual(multiply(30, 30), 900)

    def test_power(self):
        self.assertEqual(power(2, 8), 256)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), 8)
        self.assertEqual(fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()
