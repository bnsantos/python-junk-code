__author__ = 'bruno'
import algorithms.statistics.mean as Mean
import unittest


class TestMean(unittest.TestCase):
    def setUp(self):
        pass

    def test_mean1(self):
        self.assertEqual(5, Mean.get_mean([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_mean2(self):
        self.assertEqual(9, Mean.get_mean([9, 9, 9, 9, 9, 9, 9, 9, 9]))

    def test_mean3(self):
        self.assertEqual(94, Mean.get_mean(range(-10, 200)))

    def test_mean4(self):
        self.assertEqual(150, Mean.get_mean(range(301)))

    def test_mean5(self):
        self.assertEqual(11, Mean.get_mean([1, -22, 3, 4, 5, 88, 7, 8, 9]))

    def test_mean6(self):
        self.assertEqual(-1, Mean.get_mean([1, 2, 3, 4, 5, 6, 7, -45, 9]))

    def test_mean7(self):
        self.assertEqual(12, Mean.get_mean([1, 2, -3, 4, 5, 76, 7, 8, 9]))

    def test_mean8(self):
        self.assertEqual(3, Mean.get_mean([-10, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_mean9(self):
        self.assertEqual(5, Mean.get_mean([1, 2, 3, -4, 5, 6, 7, 8, 19]))

    def test_mean10(self):
        self.assertEqual(2, Mean.get_mean([1, 2, -23, 4, 5, 6, 7, 8, 9]))