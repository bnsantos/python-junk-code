__author__ = 'bruno'
import algorithms.search.selectionSearch as SelectionSearch
import unittest


class TestSelectionSearch(unittest.TestCase):
    def setUp(self):
        pass

    def test_selection_search1(self):
        self.assertEqual(3, SelectionSearch.search([5, 6, 7, 3, 4, 1, 8, 2, 9], 2))

    def test_selection_search2(self):
        self.assertEqual(1, SelectionSearch.search([1], 0))

    def test_selection_search3(self):
        self.assertEqual(7, SelectionSearch.search([5, 7, 4, 1, 8, 6, 9], 4))

    def test_selection_search4(self):
        self.assertEqual(9, SelectionSearch.search([9, 6, 8, 7], 3))

    def test_selection_search5(self):
        self.assertEqual(1, SelectionSearch.search([1], 0))

    def test_selection_search6(self):
        self.assertEqual('b', SelectionSearch.search(['c', 'a', 'b'], 1))

    def test_selection_search7(self):
        self.assertEqual('a', SelectionSearch.search(['B', 'a', 'A', 'b'], 2))

    def test_selection_search8(self):
        self.assertEqual(4, SelectionSearch.search([5, 7, 4, 1, 8, 6, 9], 1))

    def test_selection_search9(self):
        self.assertEqual(789, SelectionSearch.search([987, 789, 678, 876, 567, 765], 3))

    def test_selection_search10(self):
        self.assertEqual('k', SelectionSearch.search(['k', 'g', 'a', 't'], 2))