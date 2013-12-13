__author__ = 'bruno'
import algorithms.sort.patienceSort as PatienceSort
import unittest


class TestPatienceSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_patience_sort1(self):
        self.assertEqual([], PatienceSort.sort([]))

    def test_patience_sort2(self):
        self.assertEqual([1], PatienceSort.sort([1]))

    def test_patience_sort3(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_patience_sort4(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([2, 6, 9, 3, 4, 1, 8, 5, 7]))

    def test_patience_sort5(self):
        self.assertEqual([1, 2, 3, 4, 5, 8, 9], PatienceSort.sort([5, 3, 4, 1, 8, 2, 9]))

    def test_patience_sort6(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([9, 2, 7, 5, 8, 1, 4, 3, 6]))

    def test_patience_sort7(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([7, 1, 5, 8, 2, 6, 9, 3, 4]))

    def test_patience_sort8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([8, 2, 4, 5, 3, 7, 9, 1, 6]))

    def test_patience_sort9(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], PatienceSort.sort([3, 4, 2, 1, 6, 7, 5, 8, 9]))

    def test_patience_sort10(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], PatienceSort.sort(['e', 'b', 'd', 'a', 'c']))