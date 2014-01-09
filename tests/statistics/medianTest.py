__author__ = 'bruno'
import algorithms.statistics.median as Median
import unittest


class TestMedian(unittest.TestCase):
    def setUp(self):
        pass

    def test_median1(self):
        self.assertEqual(5, Median.median([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_median2(self):
        self.assertEqual(7, Median.median(range(0, 15)))

    def test_median3(self):
        self.assertEqual(32, Median.median(range(0, 65)))

    def test_median4(self):
        self.assertEqual(25, Median.median(range(51)))

    def test_median5(self):
        self.assertEqual(5, Median.median([1, -22, 3, 4, 5, 88, 7, 8, 9]))

    def test_median6(self):
        self.assertEqual(4, Median.median([1, 2, 3, 4, 5, 6, 7, -45, 9]))

    def test_median7(self):
        self.assertEqual(5, Median.median([1, 2, -3, 4, 5, 76, 7, 8, 9]))

    def test_median8(self):
        self.assertEqual(5, Median.median([-10, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_median9(self):
        self.assertEqual(5, Median.median([1, 2, 3, -4, 5, 6, 7, 8, 19]))

    def test_median10(self):
        self.assertEqual(5, Median.median([1, 2, -23, 4, 5, 6, 7, 8, 9]))