__author__ = 'bruno'
import algorithms.math.prime as Prime
import unittest


class TestPrimeNumber(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_prime_number1(self):
        self.assertEqual(False, Prime.is_prime(0))

    def test_is_prime_number2(self):
        self.assertEqual(True, Prime.is_prime(2))

    def test_is_prime_number3(self):
        self.assertEqual(False, Prime.is_prime(15))

    def test_is_prime_number4(self):
        self.assertEqual(True, Prime.is_prime(17))

    def test_is_prime_number5(self):
        self.assertEqual(True, Prime.is_prime(23))

    def test_is_prime_number6(self):
        self.assertEqual(False, Prime.is_prime(39))

    def test_is_prime_number7(self):
        self.assertEqual(True, Prime.is_prime(1117))

    def test_is_prime_number8(self):
        self.assertEqual(True, Prime.is_prime(2207))

    def test_is_prime_number9(self):
        self.assertEqual(False, Prime.is_prime(0))

    def test_is_prime_number10(self):
        self.assertEqual(False, Prime.is_prime(0))