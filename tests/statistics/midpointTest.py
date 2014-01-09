__author__ = 'bruno'
import algorithms.statistics.midpoint as Midpoint
import unittest


class TestMidpoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_midpoint1(self):
        self.assertEqual(5, Midpoint.find_midpoint([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_midpoint2(self):
        self.assertEqual(9, Midpoint.find_midpoint([9, 9, 9, 9, 9, 9, 9, 9, 9]))

    def test_midpoint3(self):
        self.assertEqual(95, Midpoint.find_midpoint(range(-10, 201)))

    def test_midpoint4(self):
        self.assertEqual(150, Midpoint.find_midpoint(range(301)))

    def test_midpoint5(self):
        self.assertEqual(33, Midpoint.find_midpoint([1, -22, 3, 4, 5, 88, 7, 8, 9]))

    def test_midpoint6(self):
        self.assertEqual(-18, Midpoint.find_midpoint([1, 2, 3, 4, 5, 6, 7, -45, 9]))

    def test_midpoint7(self):
        self.assertEqual(36, Midpoint.find_midpoint([1, 2, -3, 4, 5, 76, 7, 8, 9]))

    def test_midpoint8(self):
        self.assertEqual(-1, Midpoint.find_midpoint([-10, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_midpoint9(self):
        self.assertEqual(7, Midpoint.find_midpoint([1, 2, 3, -4, 5, 6, 7, 8, 19]))

    def test_midpoint10(self):
        self.assertEqual(-7, Midpoint.find_midpoint([1, 2, -23, 4, 5, 6, 7, 8, 9]))