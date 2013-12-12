__author__ = 'bruno'
import algorithms.greatestCommonDivisor as GreatestCommonDivisor
import unittest


class TestGreatestCommonDivisor(unittest.TestCase):
    def setUp(self):
        pass

    def test_greatest_common_divisor1(self):
        self.assertEqual(1, GreatestCommonDivisor.gcd_euclidean(1, 1))

    def test_greatest_common_divisor2(self):
        self.assertEqual(6, GreatestCommonDivisor.gcd_euclidean(54, 24))

    def test_greatest_common_divisor3(self):
        self.assertEqual(6, GreatestCommonDivisor.gcd_euclidean(120, 6))

    def test_greatest_common_divisor4(self):
        self.assertEqual(4, GreatestCommonDivisor.gcd_euclidean(12, 20))

    def test_greatest_common_divisor5(self):
        self.assertEqual(3, GreatestCommonDivisor.gcd_euclidean(6, 15))

    def test_greatest_common_divisor6(self):
        self.assertEqual(6, GreatestCommonDivisor.gcd_euclidean(48, 30))

    def test_greatest_common_divisor7(self):
        self.assertEqual(6, GreatestCommonDivisor.gcd_euclidean(30, 18))

    def test_greatest_common_divisor8(self):
        self.assertEqual(6, GreatestCommonDivisor.gcd_euclidean(24, 54))

    def test_greatest_common_divisor9(self):
        self.assertEqual(30, GreatestCommonDivisor.gcd_euclidean(120, 90))

    def test_greatest_common_divisor10(self):
        self.assertEqual(10, GreatestCommonDivisor.gcd_euclidean(10, 20))