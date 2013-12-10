__author__ = 'bruno'
import unittest
import sys
sys.path.insert(0, '../algorithms')
import algorithms.factorial as Factorial


class TestFactorial(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_input_negative(self):
        self.assertEqual(False, Factorial.validate_input(-2))

    def test_validate_input_positive(self):
        self.assertEqual(True, Factorial.validate_input(2))

    def test_validate_input_string(self):
        self.assertEqual(False, Factorial.validate_input('oi'))

    def test_validate_input_float(self):
        self.assertEqual(False, Factorial.validate_input(2.0))

    def test_recursive_factorial1(self):
        self.assertEqual(1, Factorial.recursive(0))

    def test_recursive_factorial2(self):
        self.assertEqual(3628800, Factorial.recursive(10))

    def test_recursive_factorial3(self):
        self.assertEqual(10888869450418352160768000000L, Factorial.recursive(27))

    def test_incremental_factorial1(self):
        self.assertEqual(1, Factorial.incremental(0))

    def test_incremental_factorial2(self):
        self.assertEqual(3628800, Factorial.incremental(10))

    def test_incremental_factorial3(self):
        self.assertEqual(10888869450418352160768000000L, Factorial.incremental(27))