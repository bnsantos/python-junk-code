__author__ = 'bruno'
import algorithms.sort.combSort as CombSort
import unittest


class TestCombSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_comb_sort1(self):
        self.assertEqual([], CombSort.comb_sort([]))

    def test_comb_sort2(self):
        self.assertEqual([1], CombSort.comb_sort([1]))

    def test_comb_sort3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_comb_sort4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([2, 6, 9, 3, 4, 1, 8, 5, 7]))

    def test_comb_sort5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], CombSort.comb_sort([5, 3, 4, 1, 8, 2, 9]))

    def test_comb_sort6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([9, 2, 7, 5, 8, 1, 4, 3, 6]))

    def test_comb_sort7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([7, 1, 5, 8, 2, 6, 9, 3, 4]))

    def test_comb_sort8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([8, 2, 4, 5, 3, 7, 9, 1, 6]))

    def test_comb_sort9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], CombSort.comb_sort([3, 4, 2, 1, 6, 7, 5, 8, 9]))

    def test_comb_sort10(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], CombSort.comb_sort(['e', 'b', 'd', 'a', 'c']))