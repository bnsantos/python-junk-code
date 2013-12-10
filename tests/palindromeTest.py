__author__ = 'bruno'
import unittest
import algorithms.palindrome as Palindrome


class PalindromeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_palindrome_false(self):
        self.assertEqual(False, Palindrome.check_character_palindrome('ola'))

    def test_check_palindrome_true_one_letter(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('a'))

    def test_check_palindrome_true_lower1(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('aba'))

    def test_check_palindrome_true_lower_and_capital(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('abA'))

    def test_check_palindrome_true_lower2(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('civic'))

    def test_check_palindrome_true_lower3(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('kayak'))

    def test_check_palindrome_true_lower4(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('reviver'))

    def test_check_palindrome_true_lower5(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('madam'))

    def test_check_palindrome_true_lower6(self):
        self.assertEqual(True, Palindrome.check_character_palindrome('level'))

    def test_generate_palindrome(self):
        for i in range(10):
            self.assertEqual(True, Palindrome.check_character_palindrome(Palindrome.generate_palindrome(9)))