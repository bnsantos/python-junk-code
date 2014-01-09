__author__ = 'bruno'
import algorithms.sort.quickSort as QuickSort
import unittest


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_quick_sort_recursive1(self):
        self.assertEqual([], QuickSort.recursive_sort([]))

    def test_quick_sort_recursive2(self):
        self.assertEqual([1], QuickSort.recursive_sort([1]))

    def test_quick_sort_recursive3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_quick_sort_recursive4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([2, 6, 9, 3, 4, 1, 8, 5, 7]))

    def test_quick_sort_recursive5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], QuickSort.recursive_sort([5, 3, 4, 1, 8, 2, 9]))

    def test_quick_sort_recursive6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([9, 2, 7, 5, 8, 1, 4, 3, 6]))

    def test_quick_sort_recursive7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([7, 1, 5, 8, 2, 6, 9, 3, 4]))

    def test_quick_sort_recursive8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([8, 2, 4, 5, 3, 7, 9, 1, 6]))

    def test_quick_sort_recursive9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.recursive_sort([3, 4, 2, 1, 6, 7, 5, 8, 9]))

    def test_quick_sort_recursive10(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], QuickSort.recursive_sort(['e', 'b', 'd', 'a', 'c']))

    def test_quick_sort_iterative1(self):
        self.assertEqual([], QuickSort.iterative_sort([]))

    def test_quick_sort_iterative2(self):
        self.assertEqual([1], QuickSort.iterative_sort([1]))

    def test_quick_sort_iterative3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_quick_sort_iterative4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([2, 6, 9, 3, 4, 1, 8, 5, 7]))

    def test_quick_sort_iterative5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], QuickSort.iterative_sort([5, 3, 4, 1, 8, 2, 9]))

    def test_quick_sort_iterative6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([9, 2, 7, 5, 8, 1, 4, 3, 6]))

    def test_quick_sort_iterative7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([7, 1, 5, 8, 2, 6, 9, 3, 4]))

    def test_quick_sort_iterative8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([8, 2, 4, 5, 3, 7, 9, 1, 6]))

    def test_quick_sort_iterative9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], QuickSort.iterative_sort([3, 4, 2, 1, 6, 7, 5, 8, 9]))

    def test_quick_sort_iterative10(self):
       self.assertEqual(['a', 'b', 'c', 'd', 'e'], QuickSort.iterative_sort(['e', 'b', 'd', 'a', 'c']))