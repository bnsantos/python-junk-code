__author__ = 'bruno'
import unittest
import algorithms.string.firstNonRepeatedChar as FirstNonRepeatedChar


class TestFirstNonRepeatedChar(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_non_repeated_char_1(self):
        self.assertEqual('o', FirstNonRepeatedChar.find_first_non_repeated_char('total'))

    def test_first_non_repeated_char_2(self):
        self.assertEqual('r', FirstNonRepeatedChar.find_first_non_repeated_char('teeter'))

    def test_first_non_repeated_char_3(self):
        self.assertEqual(None, FirstNonRepeatedChar.find_first_non_repeated_char(''))

    def test_first_non_repeated_char_4(self):
        self.assertEqual(None, FirstNonRepeatedChar.find_first_non_repeated_char(None))

    def test_first_non_repeated_char_5(self):
        self.assertEqual('f', FirstNonRepeatedChar.find_first_non_repeated_char('first'))

    def test_first_non_repeated_char_6(self):
        self.assertEqual('f', FirstNonRepeatedChar.find_first_non_repeated_char('aabbccddeef'))

    def test_first_non_repeated_char_7(self):
        self.assertEqual(None, FirstNonRepeatedChar.find_first_non_repeated_char('aabbccddeeffgghh'))

    def test_first_non_repeated_char_8(self):
        self.assertEqual('n', FirstNonRepeatedChar.find_first_non_repeated_char('programmingproai'))

    def test_first_non_repeated_char_9(self):
        self.assertEqual('s', FirstNonRepeatedChar.find_first_non_repeated_char('fortyninersfortyniner'))

    def test_first_non_repeated_char_10(self):
        self.assertEqual('h', FirstNonRepeatedChar.find_first_non_repeated_char('hi'))