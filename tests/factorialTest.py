__author__ = 'bruno'
import unittest
import algorithms.factorial as Factorial


class TestFactorial(unittest.TestCase):
    def setUp(self):
        pass

    def test_recursive_factorial1(self):
        self.assertEqual(1, Factorial.recursive(0))

    def test_recursive_factorial2(self):
        self.assertEqual(3628800, Factorial.recursive(10))

    def test_recursive_factorial3(self):
        self.assertEqual(10888869450418352160768000000L, Factorial.recursive(27))

    def test_recursive_factorial4(self):
        self.assertEqual(1307674368000, Factorial.recursive(15))

    def test_recursive_factorial5(self):
        self.assertEqual(121645100408832000, Factorial.recursive(19))

    def test_incremental_factorial1(self):
        self.assertEqual(1, Factorial.incremental(0))

    def test_incremental_factorial2(self):
        self.assertEqual(3628800, Factorial.incremental(10))

    def test_incremental_factorial3(self):
        self.assertEqual(10888869450418352160768000000L, Factorial.incremental(27))

    def test_incremental_factorial4(self):
        self.assertEqual(1307674368000, Factorial.incremental(15))

    def test_incremental_factorial5(self):
        self.assertEqual(121645100408832000, Factorial.incremental(19))