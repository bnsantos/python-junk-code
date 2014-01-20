__author__ = 'bruno'
import unittest
import algorithms.string.combinations as Combinatinos


class TestCombinations(unittest.TestCase):
    def setUp(self):
        pass

    def test_combinations_1(self):
        self.assertEqual(['a'], Combinatinos.recursive_combinations('a'))

    def test_combinations_2(self):
        self.assertEqual(['a', 'ab', 'b'], Combinatinos.recursive_combinations('ab'))

    def test_combinations_3(self):
        self.assertEqual(['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], Combinatinos.recursive_combinations('abc'))

    def test_combinations_4(self):
        out = ['a', 'ab', 'abc', 'abcd', 'abd', 'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']
        self.assertEqual(out, Combinatinos.recursive_combinations('abcd'))

    def test_combinations_5(self):
        out = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abce', 'abd', 'abde', 'abe', 'ac', 'acd', 'acde', 'ace',
               'ad', 'ade', 'ae', 'b', 'bc', 'bcd', 'bcde', 'bce', 'bd', 'bde', 'be', 'c', 'cd', 'cde', 'ce',
               'd', 'de', 'e']
        self.assertEqual(out, Combinatinos.recursive_combinations('abcde'))