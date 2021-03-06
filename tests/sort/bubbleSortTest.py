__author__ = 'bruno'
import algorithms.sort.bubbleSort as BubbleSort
import unittest


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_bubble_sort1(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], BubbleSort.bubble([5, 6, 7, 3, 4, 1, 8, 2, 9]))

    def test_bubble_sort2(self):
        self.assertEqual([1], BubbleSort.bubble([1]))

    def test_bubble_sort3(self):
        self.assertEqual([1, 4, 5, 6, 7, 8, 9], BubbleSort.bubble([5, 7, 4, 1, 8, 6, 9]))

    def test_bubble_sort4(self):
        self.assertEqual([6, 7, 8, 9], BubbleSort.bubble([9, 6, 8, 7]))

    def test_bubble_sort5(self):
        self.assertEqual([], BubbleSort.bubble([]))

    def test_bubble_sort6(self):
        self.assertEqual(['a', 'b', 'c'], BubbleSort.bubble(['c', 'a', 'b']))

    def test_bubble_sort7(self):
        self.assertEqual(['A', 'B', 'a', 'b'], BubbleSort.bubble(['B', 'a', 'A', 'b']))

    def test_bubble_sort8(self):
        self.assertEqual([1, 4, 5, 6, 7, 8, 9], BubbleSort.bubble([5, 7, 4, 1, 8, 6, 9]))

    def test_bubble_sort9(self):
        self.assertEqual([567, 678, 765, 789, 876, 987], BubbleSort.bubble([987, 789, 678, 876, 567, 765]))

    def test_bubble_sort10(self):
        self.assertEqual(['a', 'g', 'k', 't'], BubbleSort.bubble(['k', 'g', 'a', 't']))