__author__ = 'bruno'
import algorithms.search.linearSearch as LinearSearch
import unittest


class TestLinearSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_linear_search1(self):
        self.assertEqual(False, LinearSearch.search('key', []))

    def test_linear_search2(self):
        self.assertEqual(True, LinearSearch.search('1', ['1', 1, 2, 4]))

    def test_linear_search3(self):
        self.assertEqual(False, LinearSearch.search('1', [1, '2', '3', '4', '5']))

    def test_linear_search4(self):
        self.assertEqual(True, LinearSearch.search([1, 2, 3], [[1, 2, 3], 4, 5, 6, [7, 8, 9]]))

    def test_linear_search5(self):
        self.assertEqual(False, LinearSearch.search('key', ['elephant', 'giraffe', 'gorilla']))

    def test_linear_search6(self):
        self.assertEqual(True, LinearSearch.search('python', ['java', 'c', 'perl', 'python', 'javascript', 'ruby']))

    def test_linear_search7(self):
        self.assertEqual(True, LinearSearch.search(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

    def test_linear_search8(self):
        self.assertEqual(True, LinearSearch.search('key', ['key', 'key', 'key', 'key']))

    def test_linear_search9(self):
        self.assertEqual(False, LinearSearch.search('key', ['hi', 'hello', 'world', 'python']))

    def test_linear_search10(self):
        self.assertEqual(True, LinearSearch.search(4, [1, 2, 3 ,4 ,5]))