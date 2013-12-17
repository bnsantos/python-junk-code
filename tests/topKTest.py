__author__ = 'bruno'
import algorithms.statistics.topk as TopK
import unittest


class TestTopK(unittest.TestCase):
    def setUp(self):
        pass

    def test_top_k1(self):
        top_k = TopK.top_k([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 5)
        top_k.sort()
        self.assertEqual([11, 27, 28, 31, 33], top_k)

    def test_top_k2(self):
        top_k = TopK.top_k([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 3)
        top_k.sort()
        self.assertEqual([11, 27, 28], top_k)

    def test_top_k3(self):
        top_k = TopK.top_k([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 8)
        top_k.sort()
        self.assertEqual([11, 27, 28, 31, 33, 36, 45, 51], top_k)

    def test_top_k4(self):
        self.assertEqual([11], TopK.top_k([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 1))

    def test_top_k5(self):
        self.assertEqual([], TopK.top_k([99, 74, 65, 23, 30, 10, 6, 48, 234, 52], 0))

    def test_top_k6(self):
        top_k = TopK.top_k([99, 102, 48, 83, 52, 30, 2, 17, 68, 12, 44, 39], 10)
        top_k.sort()
        self.assertEqual([2, 12, 17, 30, 39, 44, 48, 52, 68, 83], top_k)

    def test_top_k7(self):
        top_k = TopK.top_k([12, 32, 23, 34, 54, 43, 33, 56, 48, 87, 99], 10)
        top_k.sort()
        self.assertEqual([12, 23, 32, 33, 34, 43, 48, 54, 56, 87], top_k)

    def test_top_k8(self):
        top_k = TopK.top_k([9, 8, 5, 2, 3, 5, 7, 3, 4], 3)
        top_k.sort()
        self.assertEqual([2, 3, 3], top_k)

    def test_top_k9(self):
        top_k = TopK.top_k([-1, -15, 2, 99, 84, -87, -33, 46, 27], 3)
        top_k.sort()
        self.assertEqual([-87, -33, -15], top_k)

    def test_top_k10(self):
        top_k = TopK.top_k([99, 88, 77, 66, 44, 55, 33, 22, 11, -13, -15, 18, -98], 5)
        top_k.sort()
        self.assertEqual([-98, -15, -13, 11, 18], top_k)