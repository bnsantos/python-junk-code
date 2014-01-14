__author__ = 'bruno'
import unittest
import algorithms.string.removeString as RemoveString


class TestRemoveString(unittest.TestCase):
    def setUp(self):
        pass

    def test_remove_string_1(self):
        self.assertEqual('Bttl f th Vwls: Hw vs. Grzny',
                         RemoveString.remove_pattern('Battle of the Vowels: Hawaii vs. Grozny', 'aeiou'))

    def test_remove_string_2(self):
        self.assertEqual('', RemoveString.remove_pattern('aeiou', 'aeiou'))

    def test_remove_string_3(self):
        self.assertEqual(None, RemoveString.remove_pattern(1, 1))

    def test_remove_string_4(self):
        self.assertEqual(None, RemoveString.remove_pattern('1', None))

    def test_remove_string_5(self):
        self.assertEqual(None, RemoveString.remove_pattern(None, '1'))

    def test_remove_string_6(self):
        self.assertEqual('ddddd',
                         RemoveString.remove_pattern('adadadadad', 'a'))

    def test_remove_string_7(self):
        self.assertEqual('aeiou', RemoveString.remove_pattern('aeiou', ''))

    def test_remove_string_8(self):
        self.assertEqual('SpiderMan', RemoveString.remove_pattern('Spider-Man', '-'))

    def test_remove_string_9(self):
        self.assertEqual('heo', RemoveString.remove_pattern('hello', 'l'))

    def test_remove_string_10(self):
        self.assertEqual('hell', RemoveString.remove_pattern('hello', 'o'))