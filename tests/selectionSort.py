__author__ = 'bruno'
import algorithms.sort.selectionSort as SelectionSort
import unittest


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_selection_sort1(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], SelectionSort.sort([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_selection_sort2(self):
        self.assertEqual([1], SelectionSort.sort([1]))

    def test_selection_sort3(self):
        self.assertEqual([1, 4, 5, 6, 7, 8, 9], SelectionSort.sort([5, 7, 4, 1, 8, 6, 9]))

    def test_selection_sort4(self):
        self.assertEqual([6, 7, 8, 9], SelectionSort.sort([9, 6, 8, 7]))

    def test_selection_sort5(self):
        self.assertEqual([], SelectionSort.sort([]))

    def test_selection_sort6(self):
        self.assertEqual(['a', 'b', 'c'], SelectionSort.sort(['c', 'a', 'b']))

    def test_selection_sort7(self):
        self.assertEqual(['A', 'B', 'a', 'b'], SelectionSort.sort(['B', 'a', 'A', 'b']))

    def test_selection_sort8(self):
        self.assertEqual([1, 4, 5, 6, 7, 8, 9], SelectionSort.sort([5, 7, 4, 1, 8, 6, 9]))

    def test_selection_sort9(self):
        self.assertEqual([567, 678, 765, 789, 876, 987], SelectionSort.sort([987, 789, 678, 876, 567, 765]))

    def test_selection_sort10(self):
        self.assertEqual(['a', 'g', 'k', 't'], SelectionSort.sort(['k', 'g', 'a', 't']))