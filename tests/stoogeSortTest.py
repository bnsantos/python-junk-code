__author__ = 'bruno'
import algorithms.sort.stoogeSort as StoogeSort
import unittest


class TestStoogeSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_stooge_sort1(self):
        self.assertEqual([], StoogeSort.sort([], 0, 0))

    def test_stooge_sort2(self):
        self.assertEqual([1], StoogeSort.sort([1], 0, 0))

    def test_stooge_sort3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([5, 6, 7, 3, 4, 1, 8, 2, 9], 0, 8))

    def test_stooge_sort4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([2, 6, 9, 3, 4, 1, 8, 5, 7], 0, 8))

    def test_stooge_sort5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], StoogeSort.sort([5, 3, 4, 1, 8, 2, 9], 0, 6))

    def test_stooge_sort6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([9, 2, 7, 5, 8, 1, 4, 3, 6], 0, 8))

    def test_stooge_sort7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([7, 1, 5, 8, 2, 6, 9, 3, 4], 0, 8))

    def test_stooge_sort8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([8, 2, 4, 5, 3, 7, 9, 1, 6], 0, 8))

    def test_stooge_sort9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], StoogeSort.sort([3, 4, 2, 1, 6, 7, 5, 8, 9], 0, 8))

    def test_stooge_sort10(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], StoogeSort.sort(['e', 'b', 'd', 'a', 'c'], 0, 4))