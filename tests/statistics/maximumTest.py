__author__ = 'bruno'
import algorithms.statistics.maximum as Maximum
import unittest


class TestMaximum(unittest.TestCase):
    def setUp(self):
        pass

    def test_maximum1(self):
        self.assertEqual(9, Maximum.find_maximum([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_maximum2(self):
        self.assertEqual(9, Maximum.find_maximum([9, 9, 9, 9, 9, 9, 9, 9, 9]))

    def test_maximum3(self):
        self.assertEqual(199, Maximum.find_maximum(range(200)))

    def test_maximum4(self):
        self.assertEqual(300, Maximum.find_maximum(range(301)))

    def test_maximum5(self):
        self.assertEqual(88, Maximum.find_maximum([1, 2, 3, 4, 5, 88, 7, 8, 9]))

    def test_maximum6(self):
        self.assertEqual(45, Maximum.find_maximum([1, 2, 3, 4, 5, 6, 7, 45, 9]))

    def test_maximum7(self):
        self.assertEqual(76, Maximum.find_maximum([1, 2, 3, 4, 5, 76, 7, 8, 9]))

    def test_maximum8(self):
        self.assertEqual(10, Maximum.find_maximum([10, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_maximum9(self):
        self.assertEqual(19, Maximum.find_maximum([1, 2, 3, 4, 5, 6, 7, 8, 19]))

    def test_maximum10(self):
        self.assertEqual(23, Maximum.find_maximum([1, 2, 23, 4, 5, 6, 7, 8, 9]))