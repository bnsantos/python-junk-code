__author__ = 'bruno'
import algorithms.sort.oddEvenSort as OddEvenSort
import unittest


class TestOddEvenSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_odd_even_sort1(self):
        self.assertEqual([], OddEvenSort.odd_even_sort([]))

    def test_odd_even_sort2(self):
        self.assertEqual([1], OddEvenSort.odd_even_sort([1]))

    def test_odd_even_sort3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_odd_even_sort4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([2, 6, 9, 3, 4, 1, 8, 5, 7]))

    def test_odd_even_sort5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], OddEvenSort.odd_even_sort([5, 3, 4, 1, 8, 2, 9]))

    def test_odd_even_sort6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([9, 2, 7, 5, 8, 1, 4, 3, 6]))

    def test_odd_even_sort7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([7, 1, 5, 8, 2, 6, 9, 3, 4]))

    def test_odd_even_sort8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([8, 2, 4, 5, 3, 7, 9, 1, 6]))

    def test_odd_even_sort9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], OddEvenSort.odd_even_sort([3, 4, 2, 1, 6, 7, 5, 8, 9]))

    def test_odd_even_sort10(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], OddEvenSort.odd_even_sort(['e', 'b', 'd', 'a', 'c']))