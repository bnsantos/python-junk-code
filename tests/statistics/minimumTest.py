__author__ = 'bruno'
import algorithms.statistics.minimum as Minimum
import unittest


class TestMinimum(unittest.TestCase):
    def setUp(self):
        pass

    def test_minimum1(self):
        self.assertEqual(1, Minimum.find_minimum([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_minimum2(self):
        self.assertEqual(9, Minimum.find_minimum([9, 9, 9, 9, 9, 9, 9, 9, 9]))

    def test_minimum3(self):
        self.assertEqual(-10, Minimum.find_minimum(range(-10, 200)))

    def test_minimum4(self):
        self.assertEqual(0, Minimum.find_minimum(range(301)))

    def test_minimum5(self):
        self.assertEqual(-22, Minimum.find_minimum([1, -22, 3, 4, 5, 88, 7, 8, 9]))

    def test_minimum6(self):
        self.assertEqual(-45, Minimum.find_minimum([1, 2, 3, 4, 5, 6, 7, -45, 9]))

    def test_minimum7(self):
        self.assertEqual(-3, Minimum.find_minimum([1, 2, -3, 4, 5, 76, 7, 8, 9]))

    def test_minimum8(self):
        self.assertEqual(-10, Minimum.find_minimum([-10, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_minimum9(self):
        self.assertEqual(-4, Minimum.find_minimum([1, 2, 3, -4, 5, 6, 7, 8, 19]))

    def test_minimum10(self):
        self.assertEqual(-23, Minimum.find_minimum([1, 2, -23, 4, 5, 6, 7, 8, 9]))